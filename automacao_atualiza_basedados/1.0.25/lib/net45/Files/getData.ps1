# Set up the ODBC connection to Denodo 
$dsn = "DenodoODBC"
$conn = New-Object System.Data.Odbc.OdbcConnection("DSN=$dsn")
$conn.Open()

# Set the default database and schema
$db = "cooperativa"
$schema = "ldw"

# Define the tables to retrieve
$tables = @(
"conta_corrente_atual",
"pessoas",
"cadastro_pessoa_receita_despesa_atual",
"cadastro_dependentes_atual",
"cadastro_conjuge_atual",
"cadastro_cotitular",
"cadastro_associado_risco",
"pessoas_endereco",
"telefones_associado",
"restritivos_bureau_atual",
"carteiras_por_gerente_atual",
"associados_total_diario",
"cesta_de_relacionamento_vigente_atual",
"capital_social_atual",
"subscricao_capital_social",
"from cooperativa.pessoas",
"cadastro_pessoa_receita_despesa_atual",
"cadastro_dependentes_atual",
"cadastro_conjuge_atual",
"cadastro_cotitular",
"cadastro_associado_risco",
"pessoas_endereco",
"telefones_associado",
"restritivos_bureau_atual",
"carteiras_por_gerente_atual",
"associados_total_diario",
"cesta_de_relacionamento_vigente_atual",
"capital_social_atual",
"subscricao_capital_social",
"associado_movimento",
"base_relacionamento",
"canais_usuarios_dispositivos_atual",
"base_relacionamento_atual",
"base_cartoes_atual",
"emissao_transacoes_debito_credito",
"base_cartoes_faturas",
"cartoes_risco_atual",
"movimento_cheques_compensados_atual",
"base_rel_fluxo_caixa_atual",
"cheques_devol_minha_coop",
"chq_solicitacao_taloes",
"indicadores_de_credito",
"portfolio",
"portfolio_atual",
"chegada_prejuizo"

)

# Retrieve data from each table and save to CSV files
foreach ($table in $tables) {
    $query = "SELECT * FROM $db.$schema.$table"
    $cmd = New-Object System.Data.Odbc.OdbcCommand($query, $conn)
    $adapter = New-Object System.Data.Odbc.OdbcDataAdapter($cmd)
    $dataset = New-Object System.Data.DataSet
    $adapter.Fill($dataset)

    $csvFilename = "C:\Users\Public\Documents\base geral\" + "$table.csv"
    $dataset.Tables[0] | Export-Csv -Path $csvFilename -NoTypeInformation -Delimiter ";"
}

# Close the ODBC connection
$conn.Close()
