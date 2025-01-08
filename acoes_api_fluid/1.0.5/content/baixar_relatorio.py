import httpx
import requests
import pandas as pd
import time
import os
from enum import Enum
import sys

#versão 1.0.0
#atualizado em 27/08/2024

##################################################################################
################################--INSTRUÇÕES--####################################
##################################################################################                              
####                                                                          ####   
#### - Os argumentos devem seguir a seguinte ordem:                           ####
####     ID do relatório, data inicial, data final com formato YYYY-MM-DD,    ####
####      Formato do arquivo (csv ou xlsx), e o caminho destino do arquivo;   ####
####                                                                          ####          
#### - O Token é uma variavel de ambiente;                                    ####
####                                                                          ####
#### - Crie um arquivo .bat na mesma pasta que esse script está salvo         ####    
####   Conteúdo do bat:                                                       ####
####                                                                          #### 
####    python.exe <nome_desse_arquivo.py> "argumento1" "arg2" "arg3" "arg4"  #### 
####                                                                          ####   
####                                                                          ####
##################################################################################
##################################################################################
##################################################################################


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

class baixar_relatorio:
    
    def __init__(self, org: str = op.ORG, api_key: str = op.TOKEN, 
        user: str = op.USER_FLUID, BASE_URL: str = op.BASE_URL):        
        self.org = org        
        self.tkn = api_key        
        self.user = user
        self.BASE_URL = BASE_URL
        self.header = op.HEADER_FLUID
        self.session = requests.Session()
        self.processosInBox = [] 

    def get_report_data(self, report_id: str, initial_date: str, final_date: str, page: int = 1, situation: int = 0) -> dict:
            url = f"{self.BASE_URL}process/reports/{report_id}/period/{initial_date}/{final_date}"
            params = {"page": page, "situation": situation}
            return self._make_request("get", url, params=params)

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

    def _convert_json_to_df(self, data):
        df = pd.DataFrame(data['bodyReport'], columns=data['header'])
        df = df.fillna('')
        return df

    def save_to_csv(self, df, path, id):
        csv_filename = f"\\relatorio_{id}.csv"
        path = path + csv_filename
        df.to_csv(path, index=False, sep=';', encoding='utf-16')
        
    def save_to_xls(self, df, path, id):
        filename = f"\\relatorio_{id}.xlsx"    
        path = path + filename
        df.to_excel(path, index=False)
        
if __name__ == "__main__":
    
    br = baixar_relatorio()
    # id_relatorio = '1102'
    # data_ini = '2024-09-20'
    # data_fim = '2024-09-24'
    # formato = 'xlsx' # ou csv
    # caminho_arquivo = 'c:\\Temp'
    
    id_relatorio = sys.argv[1]
    data_ini = sys.argv[2] 
    data_fim = sys.argv[3] 
    formato = sys.argv[4] 
    caminho_arquivo = sys.argv[5] 
    
    print("Dados Obtidos:")
    print('id_relatorio: '+ id_relatorio)
    print('data_ini: ' + data_ini)
    print('data_fim: ' + data_fim)
    print('formato: ' + formato)
    print('caminho_arquivo: ' + caminho_arquivo)
    
    retorno = br.get_report_data(id_relatorio, data_ini, data_fim)
    df = br._convert_json_to_df(retorno)
    print("Salvando Relatório em: "+ caminho_arquivo)
    if formato == 'csv':
        br.save_to_csv(df, caminho_arquivo, id_relatorio)
    else:
        br.save_to_xls(df, caminho_arquivo, id_relatorio)
           
    for _ in range(5, 0, -1):
        print(f"Saindo em {_}")
        time.sleep(1)
    print("bye")             