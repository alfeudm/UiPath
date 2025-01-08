import httpx
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError
import os
import time
from datetime import datetime
import urllib3
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
    VEICULO = 31952
    IMOVEL = 47863 #35265

class FazTudoFluid:
    
    def __init__(self, org: str = op.ORG, api_key: str = op.TOKEN, 
                 user: str = op.USER_FLUID, BASE_URL: str = op.BASE_URL):        
        self.org = org        
        self.tkn = api_key        
        self.user = user
        self.BASE_URL = BASE_URL
        self.header = op.HEADER_FLUID
        self.session = requests.Session()
        self.processosInBox = []
        
        #########################--DEBUG--###############################
        # self.tp_garantia= "veiculo" 
        # self.tp_garantia= "imovel"
        # self.user_id= "1051" 
        # self.cod_titulo= "C015314681" 
        # self.num_conta_tomador= "952184" 
        # self.dat_ultimo_pgto= "07/10/2024"
        # self.nome_tomador= "JUCELINO BARROS DE OLIVEIRA"
        # self.chassis = "9BGRG48F0CG232991"
        # self.agencia = '15'
        # self.cpf = "5265986000145"
        # self.dat_ultimo_pgto = "2024-09-30"
        # self.logradouro = "AV. HERMES DA FONSECA, 195"
        # self.Instrumento = "CEDULA DE CREDITO BANCARIA"
        # self.cep = "95548-000"
        # self.bairro = "QUINTAO" 
        # self.cidade = "PALMARES DO SUL"    
        # self.valor = "97602"
        # self.data_contrat = "2021-04-15"
        # self.valor_extenso = "NOVENTA E SETE MIL SEISCENTOS E DOIS REAIS"
        ########################################################
        self.uf = ""
        self.tp_garantia = sys.argv[1] 
        self.user_id = sys.argv[2]
        self.cod_titulo = sys.argv[3]
        self.num_conta_tomador = sys.argv[4]
        self.dat_ultimo_pgto = sys.argv[5]
        self.nome_tomador = sys.argv[6]
        self.chassis = sys.argv[7]
        self.agencia = sys.argv[8]
        data = datetime.strptime(self.dat_ultimo_pgto, '%Y-%m-%d')
        self.dat_ultimo_pgto = data.strftime('%d/%m/%Y')
        
        if self.tp_garantia == 'imovel':
            self.cpf = sys.argv[9]
            self.logradouro = sys.argv[10]
            self.Instrumento = sys.argv[11]
            self.cep = sys.argv[12]
            self.bairro = sys.argv[13]
            self.cidade = sys.argv[14]   
            self.valor = sys.argv[15]
            self.data_contrat = sys.argv[16]
            self.valor_extenso = sys.argv[17]
            data = datetime.strptime(self.data_contrat, '%Y-%m-%d')
            self.data_contrat = data.strftime('%d/%m/%Y')
            

        print("tp_garantia: "+ self.tp_garantia)
        print("user_id: "+ self.user_id)
        print("cod_titulo: "+ self.cod_titulo)
        print("num_conta_tomador: "+ self.num_conta_tomador)
        print("dat_ultimo_pgto: "+ self.dat_ultimo_pgto)
        print("nome_tomador: "+ self.nome_tomador)
        
        if self.tp_garantia == 'imovel':
            print("cpf_cnpj: "+self.cpf)
            print("dat_ultimo_pgto: "+self.dat_ultimo_pgto)
            print("logradouro: "+self.logradouro)
            print("Instrumento: "+self.Instrumento)
            print("cep: "+self.cep)
            print("bairro: "+self.bairro)
            print("cidade: "+self.cidade)  
            print("valor: "+self.valor)
            print("data_contrat: "+self.data_contrat)
            print("valor por extenso: "+self.valor_extenso)
            
            
        
    def create_draft_process(self):
        
        imovel = op.IMOVEL
        veiculo = op.VEICULO
        
        if self.tp_garantia == 'imovel':
            confecNode = imovel
            if self.cep[0] == '9':
                self.uf = 'RS'
            else:
                self.uf = 'SC'
            print(f"UF: {self.uf}")      
        else:    
            confecNode = veiculo
        
        if len(self.agencia) == 1:
            self.agencia = '0' + self.agencia
            
        ag = self._obter_cod_ag(self.agencia)    
                
        nodo = confecNode
        
        data={
        "confectionNode": confecNode,
        "destinationCompany": 0,
        "destinationResponsible": 0,
        "openingResponsible": int(self.user_id),
        "originCompany": ag,
        "time": 1080
        }
        id_process = ""
        
        try:
            
            ######
            #Obter o confectionNode por meio do endpoint 
            url = f"{self.BASE_URL}process/draft/groups" 
            confection_node = self._make_request("get", url)
            
            ######
            
            url = f"{self.BASE_URL}process/draft"
            procId = self._make_request("post", url, data=data)
            id_process = procId["processId"]
            self.get_data_to_protocol(id_process, nodo, 0)
            ret = self.save_form_fields(id_process, confecNode)
            self.protocol_process(id_process, confecNode)
            self.get_node(id_process)

            file_name = self.cod_titulo + '.txt'
            with open(file_name, 'w') as file:
                file.write(str(id_process))
        except  Exception as e:
            file_name = self.cod_titulo + '.txt'
            id_process = "Erro "+ str(e)
            with open(file_name, 'w') as file:
                file.write(
                            id_process+" "+"tp_garantia: "+ self.tp_garantia+
                            " user_id: "+ str(self.user_id)+
                            " cod_titulo: "+ self.cod_titulo+
                            " num_conta_tomador: "+ self.num_conta_tomador+
                            " dat_ultimo_pgto: "+ self.dat_ultimo_pgto+
                            " nome_tomador: "+ self.nome_tomador)
                                    
                
    def save_form_fields(self, proc_id: str, work_id):
       
        if work_id == 31952:        
            fields_data = {
                "1": f"{self.nome_tomador}",
                "29": f"{self.num_conta_tomador}",
                "302": f"{self.dat_ultimo_pgto}",
                "306": f"{self.cod_titulo}",
                "183": f"{self.chassis}"         
                }
        else:
            fields_data = {
                "1": f"{self.nome_tomador}",
                "29": f"{self.num_conta_tomador}",
                "107": f"{self.cpf}",
                #"302": f"{self.dat_ultimo_pgto}",
                "318": f"{self.cod_titulo}",
                "1231": f"{self.logradouro}",
                "305": f"{self.Instrumento}",
                "2037": f"{self.cep}",
                "2040": f"{self.bairro}",
                "2041": f"{self.cidade}",      
                "2429": f"{self.valor}",      
                "2290": f"{self.data_contrat}",
                "2430": f"{self.valor_extenso}",
                "20": f"{self.uf}"        
                }        
        print(fields_data)
        url = f"{self.BASE_URL}process/{proc_id}/node/{work_id}/form/fields"
        return self._make_request("post", url, data=fields_data)

    def get_node(self, proc_id: str) -> None:
        url = f"{self.BASE_URL}process/{proc_id}/visualize/main"
        self._make_request("get", url)

    def get_data_to_protocol(self, proc_id: str, work_id, action: int):        
        url = f"{self.BASE_URL}process/{proc_id}/protocol/node/{work_id}/action/{action}"
        return self._make_request("put", url)

    def protocol_process(self, proc_id: str, confecNode) -> dict:
        
        protocol_data = {
            "acao": 0,
            "empDestino": 0,
            "parecer": "",
            "parecerRestrito": 0,
            "respDestino": 0,
            "tempo": 0,
            "tempoRetorno": 0,
            "votoJus": "",
            "votoOpt": 0,
            "workId": confecNode
        }
        
        url = f"{self.BASE_URL}process/{proc_id}/protocol"
        return self._make_request("post", url, data=protocol_data)
    
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
        retries = 2
        backoff_factor = 2  # exponetial backoff factor        

        while retries < max_retries:
            try:
                with httpx.Client() as client:
                    #print(f"Payload: {data}")
                    #x = client.request("get",self.BASE_URL+"process/draft/groups", headers=self.header)
                    response = client.request(method, url, params=params, json=data, headers=self.header)

                    # z = client.request("put",self.BASE_URL+'process/709134/protocol/node/35272/action/0', headers=self.header)
                    response.raise_for_status()  # Raise HTTPError for bad status codes
                    return self._handle_response(response)

            except httpx.RequestError as exc:
                print(f"- Request error: {exc.request.url}")
                time.sleep(10)
                if isinstance(exc, httpx.TimeoutException):
                    print("- Timeout occurred. Retrying...")
                    retries += 1
                    time.sleep(backoff_factor)  # Exponential backoff
                    backoff_factor += 2
                else:
                    print(f"- Request failed: {exc}")
                    time.sleep(10)
                    raise
            except httpx.HTTPStatusError as exc:
                if exc.response.status_code == 204:
                    print("- No content Recived.")
                    return None
                else:
                    print(f"- HTTP error: {exc.response.status_code} - {exc.response.text}")
                    time.sleep(10)
                    if 'Erro ao listar as tarefas' in exc.response.text:
                        return True
                    else:
                        raise
            except Exception as e: 
                print(f"- Request Exception: {e}")
                time.sleep(10)
                retries += 1
                time.sleep(backoff_factor)  # Exponential backoff
                backoff_factor += 2
                
        raise RuntimeError("- Maximo de tentativas excedida. Unable to complete request.")
    
    def _obter_cod_ag(self, ag):
        if ag == '01': return 39
        if ag == '02': return 23
        if ag == '03': return 24
        if ag == '04': return 25
        if ag == '05': return 26
        if ag == '06': return 27
        if ag == '07': return 28
        if ag == '08': return 29
        if ag == '09': return 30
        if ag == '10': return 31
        if ag == '11': return 32
        if ag == '12': return 33
        if ag == '13': return 34
        if ag == '14': return 35
        if ag == '15': return 36
        if ag == '16': return 37
        if ag == '17': return 38
        if ag == '18': return 40
        if ag == '19': return 41
        if ag == '20': return 43
        if ag == '21': return 42
        if ag == '22': return 44
        if ag == '23': return 45
        if ag == '24': return 47
        if ag == '25': return 48
        if ag == '26': return 49
        if ag == '27': return 46
        else: return 1
        
        
       
        
                
if __name__ == "__main__":
    
    try:
        x = FazTudoFluid()
        x.create_draft_process()
    except Exception as e:
        print(e)
        time.sleep(10)
            