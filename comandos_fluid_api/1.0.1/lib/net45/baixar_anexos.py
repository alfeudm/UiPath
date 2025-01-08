import requests
import os, re, time
import json
import csv
import sys

req = requests.Session()

#id_processo = '620181'
#diretorio_anexos = (r'C:\Users\alfeu_souza\Downloads\Automacao_Assinaturas')
#file_name_to_search = ["PROPOSTA_", "CONTRATO_", "tag", "termo"]

id_processo = sys.argv[1]
diretorio_anexos = sys.argv[2]
file_name_to_search = sys.argv[3]
file_name_to_search = file_name_to_search.split(',')


print(id_processo)
print(diretorio_anexos)
print(file_name_to_search)

time.sleep(5)

diretorio_anexos = diretorio_anexos.rstrip('\\')

output = 'records.csv'

aws_url = 'https://api.fluid.prd.sicredi.cloud/v1/processos/visualizar/'+id_processo+'/993'
aws_headers = {
    "organization": "0109.fluid",
    "authorization": "token f7b19aaf01b9c7272d40600786320bab5f4557d5de7ec26cef9341aa9af35bd5",
    "Content-Type": "application/json"
}
aws_payload = {
    "processo": id_processo,
    "hashs": []
}

try:
    aws_response = req.get(aws_url, headers=aws_headers)

    # Check if the request was successful (status code 200)
    if aws_response.status_code == 200:
        
        json_data = aws_response.content
        data = json.loads(json_data)
        with open(output, 'w', newline='') as file_csv:
            csv_writer = csv.writer(file_csv)
            
            for file in file_name_to_search:
                hash_value = None
                
                for item in data["anexos"]:
                    if item["nome"].startswith(file):
                        hash_value = item["hash"]
                        break
                
                if hash_value is None:
                    for item in data["anexos"]:
                        item_atual = item["nome"]; item_atual = item_atual.upper(); file = file.upper()
                        if file in item_atual:
                            hash_value = item["hash"]
                            break    

                if hash_value:  # Check if hash_value is not None
                    payload = {"processo": id_processo, "hashs": [hash_value]}
                    print(f'-> Preparando para baixar a(s) urls do(s) documento(s)')

                    try:
                        r = req.post(f'https://api.fluid.prd.sicredi.cloud/v1/processos/download', json=payload,
                                    headers=aws_headers)
                        link_anexo = r.content
                        link = json.loads(link_anexo)
                        url = link[0]["url"]
                        file_name = link[0]["nome"] + "." + link[0]["extensao"]
                        arquivo = (diretorio_anexos + '\\' + id_processo + "_" + file_name)
                        documento = req.get(url)
                        fb = open(arquivo, 'wb')
                        fb.write(documento.content)
                        print(arquivo)

                    # Create a row_data list for this file
                        row_data = [arquivo]

                    except Exception as e:
                        print(f"An error occurred while processing {file}: {str(e)}")
                        row_data = ["An error occurred while processing {file}: {str(e)}"]
                        
                else:
                    print(file + ' nao encontrado')
                    row_data = [file + ' nao encontrado']

            # Write the row_data to the CSV file
                csv_writer.writerow(row_data)                 
    else:
        print("File attachment failed. Status code:", aws_response.status_code)
        # Optionally, you can access the error message if available in the response.
        # print("Error message:", aws_response.text)

except Exception as e:
    print('An error occurred while attaching the file:', e)
    
    
