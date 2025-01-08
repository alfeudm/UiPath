import httpx
import requests
import pandas as pd
import time
import csv
import os
from enum import Enum
import sys


class ApiResponse(Enum):
    JSON = "application/json"
    TEXT = "application/text"

class op:
    ORG = "0109.fluid"
    TOKEN = "58a65552226917bc7cc737e5f081d2cd9368c8aaa467c52e42022289f2df2ea5"
    BASE_URL = "https://0109.fluid.sicredi.io/pato/process/api/v2/"
    USER_FLUID = "993"
    HEADER_FLUID         = {'Content-type': 'application/json', 'Accept-Charset': 'UTF-8',
                            'organization': f'{ORG}', 'authorization': f'token {TOKEN}'}
    
class obter_impressos:
    
    def __init__(self, org: str = op.ORG, api_key: str = op.TOKEN, 
        user: str = op.USER_FLUID, BASE_URL: str = op.BASE_URL):        
        self.org = org        
        self.tkn = api_key        
        self.user = user
        self.BASE_URL = BASE_URL
        self.header = op.HEADER_FLUID
        self.session = requests.Session()
        self.processosInBox = []     
        
        
    def get_printeds(self, proc_id: str, nome_doc, caminho_arquivo) -> dict:
        url = f"{self.BASE_URL}process/{proc_id}/document/attach/download"
        payload = {"attachIds": []}
        ret = self._make_request("post", url, data=payload)
        arquivo = ""
        if ret is not None:
            with open(output, 'w', newline='') as file_csv:
                csv_writer = csv.writer(file_csv)

                for file in nome_doc:
                        try:
                            for r in ret:
                                if r["fileName"].upper().startswith(file):
                                    doc_url = r['url']
                                    file_name = r["fileName"] + "." + r["extension"]
                                    arquivo = (caminho_arquivo + '\\' + proc_id + "_" + file_name)
                                    documento = requests.get(doc_url)
                                    fb = open(arquivo, 'wb')
                                    fb.write(documento.content)
                                    print(f"Arquivo: {file} encontrado")
                                    row_data = [arquivo]
                            csv_writer.writerow(row_data)        
                        except:
                            row_data = [arquivo]
                            continue
        else:
           print("erro na chamada api")
                        
    def _handle_response(self, response: httpx.Response) -> dict:
        content_type = response.headers.get("content-type", "")
        # print("APICLASS: ", ApiResponse.JSON.value, "RESPONSE HEADER: ", content_type)
        if ApiResponse.JSON.value in content_type:
            return response.json()
        elif ApiResponse.TEXT.value in content_type:
            return response.text()
        elif content_type == "":
            return None
        else:
            raise ValueError(f"- Unsupported response type: {content_type}")

    def _make_request(self, method: str, url: str, params: dict = None, data: dict = None, max_retries: int = 10) -> dict:
        retries = 0
        backoff_factor = 2  # exponetial backoff factor        

        while retries < max_retries:
            try:
                with httpx.Client() as client:
                    #x = client.request("get",self.BASE_URL+"process/draft/groups", headers=self.header)
                    response = client.request(method, url, params=params, json=data, headers=self.header)

                    # z = client.request("put",self.BASE_URL+'process/709134/protocol/node/35272/action/0', headers=self.header)
                    response.raise_for_status()  # Raise HTTPError for bad status codes
                    print("Relatório obtido com sucesso")
                    return self._handle_response(response)

            except httpx.RequestError as exc:
                print(f"- Request error: {exc.request.url}")
                if isinstance(exc, httpx.TimeoutException):
                    print("- Timeout occurred. Retrying...")
                    retries += 1
                    time.sleep(backoff_factor)  # Exponential backoff
                    backoff_factor += 2
                else:
                    print(f"- Request failed: {exc}")
                    raise
            except httpx.HTTPStatusError as exc:
                if exc.response.status_code == 204:
                    print("- No content Recived.")
                    return None
                else:
                    print(f"- HTTP error: {exc.response.status_code} - {exc.response.text}")
                    if 'Erro ao listar as tarefas' in exc.response.text:
                        return True
                    else:
                        raise
            except Exception as e: 
                print(f"- Request Exception: {e}")
                retries += 1
                time.sleep(backoff_factor)  # Exponential backoff
                backoff_factor += 2
                
        raise RuntimeError("- Maximo de tentativas excedida. Unable to complete request.")

    
##    
##proc_id = '251104'
##caminho_arquivo = r'C:\Users\alfeu_souza\Downloads'
##file_name_to_search = ["PROPOSTA_", "CONTRATO_", "tag", "termo"]


proc_id = sys.argv[1]
caminho_arquivo = sys.argv[2]
file_name_to_search = sys.argv[3]

print(proc_id)
print(caminho_arquivo)
print(file_name_to_search)

caminho_arquivo = caminho_arquivo.rstrip('\\')
file_name_to_search = file_name_to_search.split(',')
    
oi = obter_impressos()
#output = caminho_arquivo+"\\output"+ proc_id +".txt"
output = 'records.csv'
oi.get_printeds(proc_id, file_name_to_search, caminho_arquivo) 
