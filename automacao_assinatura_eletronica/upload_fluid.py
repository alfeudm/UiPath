import os 
import requests

import sys

#read_file_path = r'c:\temp\tete.txt'
#path_pdf = 'C:\\Temp\\605221\\605221_LUIZ.pdf'

path_pdf = sys.argv[1]

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

try:
    loginFluid = requests.post(fluid_url, data=fluid_payload)
    # Check if the request was successful (status code 200)
    if loginFluid.status_code == 200:
        print("Login to Fluid successful!")
        # Optionally, you can access the response data if the API returns any.
        # response_data = loginFluid.json()  # Assuming the response is in JSON format
        # print("Response data:", response_data)
    else:
        print("Login to Fluid failed. Status code:", loginFluid.status_code)
        # Optionally, you can access the error message if available in the response.
        # print("Error message:", loginFluid.text)

except Exception as e:
    print('Could not log in to Fluid:', e)

# Step 2: Attach file to process using AWS API
aws_url = 'https://api.fluid.sicredi.io/v1/processos/anexar'
aws_headers = {
    "organization": "0109.fluid",
    "authorization": "token f7b19aaf01b9c7272d40600786320bab5f4557d5de7ec26cef9341aa9af35bd5",
    "Content-Type": "application/json"
}
aws_payload = {
    "nome": nome_pdf,
    "tipo": "0",
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
if aws_response.status_code != 400:
    try:
        url = aws_response.json()["url"]
        campos = aws_response.json()["fields"][0]
        documento = open(f'{path_pdf}', 'rb')
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
        if request.status_code == 204:
            print("Document sent successfully!")
            content = ("200")
            
        else:
            print("Failed to send the document. Status code:", request.status_code)
            content =  ("Failed to send the document. Status code:", request.status_code)
        
    except Exception as e:
        print("An error occurred while sending the document to AWS:", e)
        content = ("An error occurred while sending the document to AWS:", e)
else:
    content = aws_response.content

content = str(content)
with open(arq_ok, 'w') as file:
    file.write(content)  # Redirect stdout to the file
    print(content)







