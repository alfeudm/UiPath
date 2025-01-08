Const xlTextQualifierDoubleQuote = 1
Const xlInsertDeleteCells = 1
Const xlFixedWidth = 2
Set fso = CreateObject("Scripting.FileSystemObject")

dd = Date
dd = replace(dd, "/", "")

strFileName = "\\10.5.129.95\c$\Users\alfeu_souza\Documents\UiPath\Automcao_Juntos_Diario\Files\juntos_cad.xlsm"

Set objExcel = CreateObject("Excel.Application")
objExcel.Visible = True
objExcel.DisplayAlerts= False

strXLSfile = strFileName

Set objWorkbook = objExcel.Workbooks.Open (strFileName)
Set objWorkSheet = objWorkbook.Worksheets(1)

objWorkSheet.Range("A1").value = "STATUS"
objWorkSheet.Range("B1").value = "CONTA"
objWorkSheet.Range("C1").value = "DT_ULT_ATU_CAD"
objWorkSheet.Range("D1").value = "DATA_NASCIMENTO"
objWorkSheet.Range("E1").value = "TELEFONE"
objWorkSheet.Range("F1").value = "CELULAR"
objWorkSheet.Range("G1").value = "ENDERECO"
objWorkSheet.Range("H1").value = "BAIRRO"
objWorkSheet.Range("I1").value = "MUNICIPIO"
objWorkSheet.Range("J1").value = "CEP"
objWorkSheet.Range("K1").value = "EMAIL_TXT"
objWorkSheet.Range("L1").value = "EMAIL_PROFISSIONAL"
objWorkSheet.Range("M1").value = "CPF_CNPJ"
objWorkSheet.Range("N1").value = "PREJUIZO"
objWorkSheet.Range("O1").value = "AGENCIA"
objWorkSheet.Range("P1").value = "CARTEIRA"
objWorkSheet.Range("Q1").value = "GESTOR CARTEIRA"
objWorkSheet.Range("R1").value = "TIPO PESSOA"
objWorkSheet.Range("S1").value = "IDADE"
objWorkSheet.Range("T1").value = "NOME ASSOCIADO"
objWorkSheet.Range("U1").value = "DATA ASSOCIACAO"
objWorkSheet.Range("V1").value = "CBO"
objWorkSheet.Range("W1").value = "CNAE"
objWorkSheet.Range("X1").value = "SEXO"
objWorkSheet.Range("Y1").value = "MC ASSOCIADO"
objWorkSheet.Range("Z1").value = "ISA"
objWorkSheet.Range("AA1").value = "PROD_CRED_FINANC"
objWorkSheet.Range("AB1").value = "PROD_CREDITO_RURAL"
objWorkSheet.Range("AC1").value = "PROD_CREDITO_GERAL"
objWorkSheet.Range("AD1").value = "PROD_CHEQUE_ESPECIAL"
objWorkSheet.Range("AE1").value = "PROD_DESC_RECEB"
objWorkSheet.Range("AF1").value = "PROD_CAPITAL_SOCIAL"
objWorkSheet.Range("AG1").value = "PROD_POUPANCA"
objWorkSheet.Range("AH1").value = "PROD_DEPOSITO_A_PRAZO"
objWorkSheet.Range("AI1").value = "PROD_FUNDOS"
objWorkSheet.Range("AJ1").value = "PROD_PREVIDENCIA"
objWorkSheet.Range("AK1").value = "PROD_DEBITO_CONTA"
objWorkSheet.Range("AL1").value = "PROD_COBRANCA"
objWorkSheet.Range("AM1").value = "PROD_FOLHA_PAGAMENTO"
objWorkSheet.Range("AN1").value = "PROD_PAGTO_FORN"
objWorkSheet.Range("AO1").value = "PROD_CUSTODIA_CHEQUE"
objWorkSheet.Range("AP1").value = "PROD_PAGAMENTOS"
objWorkSheet.Range("AQ1").value = "PROD_CARTAO_DEBITO"
objWorkSheet.Range("AR1").value = "PROD_CARTAO_CREDITO"
objWorkSheet.Range("AS1").value = "PROD_DOMICILIO"
objWorkSheet.Range("AT1").value = "PROD_CESTA_RELACIONAMENTO"
objWorkSheet.Range("AU1").value = "PROD_CONSORCIO_SERVICOS"
objWorkSheet.Range("AV1").value = "PROD_CONSORCIO_IMOVEIS"
objWorkSheet.Range("AW1").value = "PROD_CONSORCIO_AUTOMOVEIS"
objWorkSheet.Range("AX1").value = "PROD_CONSORCIO_MOTOS"
objWorkSheet.Range("AY1").value = "PROD_CONSORCIO_PESADOS"
objWorkSheet.Range("AZ1").value = "PROD_SEGURO_RURAL"
objWorkSheet.Range("BA1").value = "PROD_SEGURO_PATR"
objWorkSheet.Range("BB1").value = "PROD_SEGURO_VIDA"
objWorkSheet.Range("BC1").value = "PROD_SEGURO_AUTOMOVEL"
objWorkSheet.Range("BD1").value = "PROD_SEGURO_RESIDENCIAL"
objWorkSheet.Range("BE1").value = "PROD_CANAIS"
objWorkSheet.Range("BF1").value = "PROD_ADQ"
objWorkSheet.Range("BG1").value = "PROD_CAMBIO"
objWorkSheet.Range("BH1").value = "PROD_CTASAL"
objWorkSheet.Range("BI1").value = "PROD_LCA"
objWorkSheet.Range("BJ1").value = "NOME DA MAE"
objWorkSheet.Range("BK1").value = "CIDADE DE NASCIMENTO"
objWorkSheet.Range("M:O").Columns.NumberFormat = "@"
objWorkSheet.Range("C:C").Columns.NumberFormat = "dd/MM/yyyy"
objWorkSheet.Range("U:U").Columns.NumberFormat = "dd/MM/yyyy"



