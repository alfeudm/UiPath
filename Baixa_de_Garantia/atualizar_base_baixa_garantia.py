import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
from datetime import datetime
from urllib.parse import quote_plus
from time import sleep
import mysql
import mysql.connector


def fetch_data_with_retry(table, retries=3, delay=5):
                  
    # Denodo REST API endpoint
    url = f"https://virtualizador.sicredi.net/denodo-restfulws/cooperativa/views/{table}"
    # API authentication credentials
    username = 'RPA_0109_estornos'
    password = 'La976sh3aA'

    headers = {
        'Accept': 'application/json',
    }
    
    limite = 300
    for attempt in range(retries + 1):
        try:
            
            response = requests.get(url, auth=HTTPBasicAuth(username, password), headers=headers)
            
            if response.status_code == 200:
                data_json = response.json()
                df = pd.DataFrame(data_json['elements'])
                #print(df.head())
            else:
                print(f"Failed to retrieve data. Status code: {response.status_code}, Message: {response.text}")
                raise ValueError()
            
            if df.shape[0] < limite:
                raise
            print(table + " " + str(df.shape[0]) + " linhas")
            return df
            
        except Exception as e:
            if attempt < retries:
                print(f"Attempt {attempt + 1} failed, retrying after {delay} seconds...")
                sleep(delay)
            else:
                return None
        

def reformat_date(date_str):     
    for date_format in ["%d/%m/%Y", "%Y-%m-%d", "%Y-%m-%dT%H:%M:%S"]:  # Add more formats if needed         
        if date_str != None:
            date_str = str(date_str)
            try:             
                return datetime.strptime(date_str, date_format).strftime("%Y-%m-%d")         
            except:             
                continue
            
            
def save_to_csv(df, file_path):
    df.to_csv(file_path, sep=';', index=False)


def load_csv_into_mysql(file_path, table, mysql_config, df):
    
    config = {
            'user': mysql_config['user'],
            'password': mysql_config['password'],
            'host': mysql_config['host'],
            'database': mysql_config['database'],
            'allow_local_infile': True
            #'client_flags': [ClientFlag.LOCAL_FILES],
        }
                
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    table_name = table.replace('0109_', '')
    table_name = table_name.replace('_BAIXA_GARANTIA', '')
    
    if table_name == 'liquidados_gestao_garantias_atual':    
        df['dat_ultimo_pgto'] = df['dat_ultimo_pgto'].apply(reformat_date)
        df['dat_contratacao_titulo'] = df['dat_contratacao_titulo'].apply(reformat_date)
            
    
    save_to_csv(df, file_path)
    
    
    query = f"DELETE FROM {table_name}"
    cursor.execute(query)
    cnx.commit()
        
    query = (
        f"LOAD DATA LOCAL INFILE '{file_path}' "
        f"INTO TABLE {table_name} "
        f"FIELDS TERMINATED BY ';' "
        f"LINES TERMINATED BY '\\n' "
        f"IGNORE 1 LINES;"
    )

    cursor.execute(query)
    cnx.commit()
    qtd_rows = cursor.rowcount
    qtd_base = df.shape[0]
    print(f"table {table_name}: {str(qtd_rows)} de {str(qtd_base)} importadas")
    if qtd_rows < qtd_base:
        raise

def save_output():
    file_name = f"out_baixa_garantia.txt"
    with open(file_name, 'w') as file:
        file.write("200")


if __name__ == "__main__":

    mysql_user = 'root'
    mysql_password = 'robo@001_UNA'
    mysql_host = 'BD-RPA-01-0109'
    mysql_db = 'baixa_de_garantia'
    encoded_password = quote_plus(mysql_password)
    mysql_config = {        
                    'user': f'{mysql_user}',         
                    'password': f'{mysql_password}',         
                    'host': f'{mysql_host}',         
                    'database': f'{mysql_db}'
    }

    tables = [
        #"0109_colaboradores_por_cargo_BAIXA_GARANTIA",       
        "0109_liquidados_gestao_garantias_atual_BAIXA_GARANTIA"
               
    ]
    for table in tables:
        file_path = f"C:/Users/Public/Documents/base_geral/{table}.csv"
        df = fetch_data_with_retry(table)
        if df is not None:
            load_csv_into_mysql(file_path, table, mysql_config, df)
    
    save_output()   
        