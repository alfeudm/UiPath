import mysql.connector
import time
import datetime

# Connect to MySQL
conn = mysql.connector.connect(
    host='BD-RPA-01-0109',
    user="root",
    password='robo@001_UNA',
    database="baixa_de_garantia"
)

today = datetime.datetime.today().weekday()
# Check if today is Monday (0) or Tuesday (1)
x = 2
if today == 0: 
# Monday
    x = 4
elif today == 1: 
# Tuesday
    x = 4
else: x = 2

# Create cursor
cursor = conn.cursor()

# List of queries
queries = [
"""    UPDATE baixa_de_garantia.liquidados_gestao_garantias_atual
SET cod_chassi = TRIM(`cod_chassi`),
cod_titulo = TRIM(`cod_titulo`),
num_conta_tomador = TRIM(`num_conta_tomador`),
dat_ultimo_pgto = TRIM(`dat_ultimo_pgto`),
dat_venc_titulo = TRIM(`dat_venc_titulo`),
nome_tomador = TRIM(`nome_tomador`),
cod_agencia = TRIM(`cod_agencia`),
nom_gestor_carteira = (TRIM(TRAILING '\\\\' FROM (REPLACE(REPLACE(REPLACE(nom_gestor_carteira, '\\\\n', ' '), '\\r', ' '), '\\\\', ' '))));""",
"""  UPDATE baixa_de_garantia.colaboradores_por_cargo
SET Nome = (TRIM(TRAILING '\\\\' FROM (REPLACE(REPLACE(REPLACE(Nome, '\\\\n', ' '), '\\r', ' '), '\\\\', ' ')))),
email_comercial = TRIM(`email_comercial`),
cadastro = TRIM(`cadastro`);""",
"""   UPDATE baixa_de_garantia.colaboradores_por_cargo
SET Nome = TRIM(Nome),
email_comercial = TRIM(`email_comercial`),
cadastro = TRIM(`cadastro`);""",
"""  UPDATE baixa_de_garantia.liquidados_gestao_garantias_atual
SET cod_chassi = TRIM(`cod_chassi`),
cod_titulo = TRIM(`cod_titulo`),
num_conta_tomador = TRIM(`num_conta_tomador`),
dat_ultimo_pgto = TRIM(`dat_ultimo_pgto`),
dat_venc_titulo = TRIM(`dat_venc_titulo`),
nome_tomador = TRIM(`nome_tomador`),
cod_agencia = TRIM(`cod_agencia`),
nom_gestor_carteira = TRIM(nom_gestor_carteira);""",
"""UPDATE baixa_de_garantia.liquidados_gestao_garantias_atual
SET cod_chassi = TRIM(`cod_chassi`),
cod_titulo = TRIM(`cod_titulo`),
num_conta_tomador = TRIM(`num_conta_tomador`),
dat_ultimo_pgto = TRIM(`dat_ultimo_pgto`),
dat_venc_titulo = TRIM(`dat_venc_titulo`),
nome_tomador = TRIM(`nome_tomador`),
cod_agencia = TRIM(`cod_agencia`),
nom_gestor_carteira = TRIM(nom_gestor_carteira);""",
f"""insert into baixa_de_garantia.processos_baixa_titulo
(Processo_Id, tp_garantia, Email, user_id, cod_chassi, cod_titulo, num_conta_tomador, dat_ultimo_pgto,
nome_tomador, ag, nom_gestor_carteira, cpf_cnpj_tomador, endereco,
tpo_instrumento, cep, bairro, municipio, dat_contratacao_titulo,
vlr_finan_titulo, data_importacao, dt_abert_processo)
(Select 0 as Processo_Id, 
case when (cod_chassi <> '') then('veiculo') else('imovel') end as tp_garantia
, C.`Email` as 'Email', C.ID as 'user_id',
cod_chassi, cod_titulo, num_conta_tomador, dat_ultimo_pgto,
nome_tomador, cod_agencia, nom_gestor_carteira, cpf_cnpj_tomador, endereco,
trim(right(tpo_instrumento, length(tpo_instrumento)-4)) as tpo_instrumento , cep, bairro, municipio, 
dat_contratacao_titulo, round(vlr_finan_titulo, 2), now() as 'data_importacao', null as dt_abert_processo
from baixa_de_garantia.liquidados_gestao_garantias_atual G
left join baixa_de_garantia.colaboradores_por_cargo CPC on G.nom_gestor_carteira LIKE CPC.Nome
left join baixa_de_garantia.colaboradores C on CPC.email_comercial = C.`Email`
Where date(dat_ultimo_pgto) = CURDATE() - INTERVAL {x} DAY 
and cod_titulo not in (select cod_titulo from baixa_de_garantia.processos_baixa_titulo)
);""",
"""UPDATE baixa_de_garantia.processos_baixa_titulo 
SET cod_chassi = TRIM(`cod_chassi`),
cod_titulo = TRIM(`cod_titulo`),
num_conta_tomador = TRIM(`num_conta_tomador`),
dat_ultimo_pgto = TRIM(`dat_ultimo_pgto`),
nome_tomador = TRIM(`nome_tomador`),
nom_gestor_carteira = TRIM(nom_gestor_carteira),
cpf_cnpj_tomador = TRIM(cpf_cnpj_tomador),
endereco = TRIM(endereco),
tpo_instrumento = TRIM(tpo_instrumento),
cep = TRIM(cep),
bairro = TRIM(bairro),
municipio = TRIM(municipio),
dat_contratacao_titulo = TRIM(dat_contratacao_titulo),
vlr_finan_titulo = TRIM(vlr_finan_titulo);"""]

update_user_id = """set @cod = (select cod_titulo from baixa_de_garantia.processos_baixa_titulo where user_id is null limit 1);
set @var_email = (select email from baixa_de_garantia.agencias where agencia = (select cod_agencia*1 from baixa_de_garantia.liquidados_gestao_garantias_atual
where cod_titulo = @cod));
update baixa_de_garantia.processos_baixa_titulo
set user_id = (select ID*1 from baixa_de_garantia.colaboradores where Email = @var_email),
Email = @var_email
where user_id is null and cod_titulo = @cod;"""


try:
    # Execute each query
    x = 1
    for query in queries:
        cursor.execute(query)
        time.sleep(1)
        conn.commit()
        print("Query "+str(x) + " ok")
        x = x + 1
    
    qtd_rows = 1
    while qtd_rows != 0:
        for result in cursor.execute(update_user_id, multi=True):
            if 'update' in result.statement: 
                print("id atualizado")
        qtd_rows = result.rowcount   
        conn.commit()
    
    print("All queries executed successfully!")
    file_name = f"query_baixa_garantia.txt"
    with open(file_name, 'w') as file:
        file.write("200")
except mysql.connector.Error as err:
    print("Error executing query:", err)

# Close cursor and connection
cursor.close()
conn.close()