# Set up the ODBC connection to Denodo 
$dsn = "DenodoODBC"
$conn = New-Object System.Data.Odbc.OdbcConnection("DSN=$dsn")
$conn.Open()

# Set the default database and schema
$db = "cooperativa"
$schema = "ldw"

# Define the tables to retrieve
$tables = @(

"""0109_pessoas_endereco""",
"""0109_cesta_de_relacionamento_vigente_atual"""

)

# Retrieve data from each table and save to CSV files
foreach ($table in $tables) {
    $query = "SELECT * FROM $db.$table"
    $cmd = New-Object System.Data.Odbc.OdbcCommand($query, $conn)
    $adapter = New-Object System.Data.Odbc.OdbcDataAdapter($cmd)
    $dataset = New-Object System.Data.DataSet
    $adapter.Fill($dataset)
    
    $table = $table.Replace('"',"")

    $csvFilename = "C:\Users\Public\Documents\base_geral\" + "$table.csv"
    $dataset.Tables[0] | Export-Csv -Path $csvFilename -NoTypeInformation -Delimiter ";"
}

# Close the ODBC connection
$conn.Close()
