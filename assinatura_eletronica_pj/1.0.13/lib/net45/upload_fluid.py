import os 
import requests

import sys

def save_printed_content_to_file(print_function, content, arq_ok):
    #original_stdout = sys.stdout  # Keep a reference to the original stdout
    try:
        with open(arq_ok, 'w') as file:
            #sys.stdout = file  # Redirect stdout to the file
            file.write(content)
            print(f"output salvo como: {content}")
    except Exception as e:
        print(e)
        #sys.stdout = original_stdout  # Restore the original stdout

#read_file_path = r'c:\temp\tete.txt'
#file_path = r'c:\temp\tete.pdf'

path_pdf = sys.argv[1]
#path_pdf = r"C:\Users\alfeu_souza\Downloads\646115\646115\646115.pdf"
# Extract process number and file name 
processo = os.path.basename(os.path.dirname(path_pdf)) 
nome_pdf = os.path.basename(path_pdf)
content = ""
arq_ok = r'c:\temp\output'+ processo +'.txt'
processo = int(processo)

# Step 1: Login to Fluid API
fluid_url = 'https://0109.fluid.prd.sicredi.cloud/usuario'
fluid_username = "993"
fluid_password = "123456"
fluid_payload = {
    "usuario": fluid_username,
    "senha": fluid_password
}


# Step 2: Attach file to process using AWS API
aws_url = 'https://api.fluid.sicredi.io/v1/processos/anexar'
aws_headers = {
    "organization": "0109.fluid",
    "authorization": "token f7b19aaf01b9c7272d40600786320bab5f4557d5de7ec26cef9341aa9af35bd5",
    "Content-Type": "application/json"
}
aws_payload = {
    "nome": nome_pdf,
    "tipo": 1,
    "processo": processo

}

try:
    aws_response = requests.post(aws_url, headers=aws_headers, json=aws_payload)

    # Check if the request was successful (status code 200)
    if aws_response.status_code == 200:
        print("File attached successfully!")
        # Optionally, you can access the response data if the API returns any.
        # response_data = aws_response.json()  # Assuming the response is in JSON format
        # print("Response data:", response_data)
    else:
        print("File attachment failed. Status code:", aws_response.status_code)
        # Optionally, you can access the error message if available in the response.
        # print("Error message:", aws_response.text)

except Exception as e:
    print('An error occurred while attaching the file:', e)

# Step 3: Sending the document to AWS (assuming it's the enviar_documento function)
try:
    url = aws_response.json()["url"]
    campos = aws_response.json()["fields"][0]
    documento = open((path_pdf), 'rb')
    infoFile = {
        "AWSAccessKeyId": campos['AWSAccessKeyId'],
        "key": campos['key'],
        "policy": campos['policy'],
        "signature": campos['signature'],
        "file": documento
    }

    request = requests.post(url, files=infoFile)
    documento.close()

    # Check if the request was successful (status code 204)
    if request.status_code >= 204 or request.status_code <= 210:
        print("Document sent successfully!")
        content = "200"
        print("200")
        save_printed_content_to_file(print, content, arq_ok)
        
    else:
        print("Failed to send the document. Status code:", request.status_code)
        content = "Failed to send the document. Status code:", request.status_code
        print("Failed to send the document. Status code:", request.status_code)
        save_printed_content_to_file(print, content, arq_ok)

except Exception as e:
    print("An error occurred while sending the document to AWS:", e)
    content = "An error occurred while sending the document to AWS:", e
    save_printed_content_to_file(print, content, arq_ok)








