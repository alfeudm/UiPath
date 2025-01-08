
strFileName = "C:\Users\Public\Documents\tb_Tipo_cesta.csv"

Set objExcel = CreateObject("Excel.Application")
objExcel.Visible = False
objExcel.DisplayAlerts= False

strCSVfile = strTextFile
strXLSfile = strFileName

'SERVICOS ISENTOS PJ=0
'CESTA BASICA EMPRESARIAL=20
'CESTA EMPRESARIAL=56.5
'CESTA EMPRESARIAL 01=39.9
'CESTA EMPRESARIAL 02=39.9
'CESTA EMPRESARIAL 03=69.9
'CESTA EMPRESARIAL 04=119.9
'CESTA EMPRESARIAL 05=99.9
'CESTA EMPRESARIAL 06=256.5
'CESTA EMPRESARIAL 07=189.9
'CESTA MEI=35
'CESTA CONNECT=149.9
'CESTA CHEQUE EMPRESARIAL=19.52
'SEM PACOTE DE SERVICO=30
'SERVICOS ISENTOS=0
'CESTA BENEFICIARIO INSS=0
'CESTA TOUCH=4.9
'CESTA FOLHA DE PAGAMENTO=7.9
'CESTA PRATICA=7.9
'CESTA PLUS=49.9
'CESTA POP=0
'CESTA SIMPLES=7.9
'CESTA JUNTOS=19.9
'CESTA VIP=29.9
'PACOTE PADRONIZADO I=15
'PACOTE PADRONIZADO II=22.5
'PACOTE PADRONIZADO III=34
'PACOTE PADRONIZADO IV=45.5
'CESTA TOP=69.9
'CESTA ESSENCIAL=22.9
'CESTA PLUS II=49.9
'CESTA ESPECIAL=29.9
'CESTA FACIL=19.9
'CESTA APOSENTADO=9.9
'CESTA 24 HORAS=61


Set objWorkbook = objExcel.Workbooks.Open (strFileName)
Set objWorkSheet = objWorkbook.Worksheets(1)

j = 1
Do While objWorkSheet.Range("A" & j).value <> ""


Select case objWorkSheet.Range("E" & j).value

Case "SERVICOS ISENTOS" 
	objWorkSheet.Range("E" & j).value = 0
Case "CESTA BENEFICIARIO INSS"
	objWorkSheet.Range("E" & j).value = 0
Case "CESTA TOUCH"
	objWorkSheet.Range("E" & j).value = 4.9
Case "CESTA FOLHA DE PAGAMENTO"
	objWorkSheet.Range("E" & j).value = 7.9
Case "CESTA PRATICA"
	objWorkSheet.Range("E" & j).value = 7.9
Case "CESTA PLUS"
	objWorkSheet.Range("E" & j).value = 49.9
Case "CESTA POP"
	objWorkSheet.Range("E" & j).value = 0
Case "CESTA SIMPLES"
	objWorkSheet.Range("E" & j).value = 7.9
Case "CESTA JUNTOS"
	objWorkSheet.Range("E" & j).value = 19.9
Case "CESTA VIP"
	objWorkSheet.Range("E" & j).value = 29.9
Case "PACOTE PADRONIZADO I"
	objWorkSheet.Range("E" & j).value = 15
Case "PACOTE PADRONIZADO II"
	objWorkSheet.Range("E" & j).value = 22.5
Case "PACOTE PADRONIZADO III"
	objWorkSheet.Range("E" & j).value = 34
Case "PACOTE PADRONIZADO IV"
	objWorkSheet.Range("E" & j).value = 45.5
Case "CESTA TOP"
	objWorkSheet.Range("E" & j).value = 69.9
Case "CESTA ESSENCIAL"
	objWorkSheet.Range("E" & j).value = 22.9
Case "CESTA PLUS II"
	objWorkSheet.Range("E" & j).value = 49.9
Case "CESTA ESPECIAL"
	objWorkSheet.Range("E" & j).value = 29.9
Case "CESTA FACIL"
	objWorkSheet.Range("E" & j).value = 19.9
Case "CESTA APOSENTADO"
	objWorkSheet.Range("E" & j).value = 9.9
Case "SERVICOS ISENTOS PJ"
	objWorkSheet.Range("E" & j).value = 0
Case "CESTA BASICA EMPRESARIAL"
	objWorkSheet.Range("E" & j).value = 20
Case "CESTA EMPRESARIAL"
	objWorkSheet.Range("E" & j).value = 56.5
Case "CESTA EMPRESARIAL 01"
	objWorkSheet.Range("E" & j).value = 39.9
Case "CESTA EMPRESARIAL 02" 
	objWorkSheet.Range("E" & j).value = 39.9
Case "CESTA EMPRESARIAL 03" 
	objWorkSheet.Range("E" & j).value = 69.9
Case "CESTA EMPRESARIAL 04" 
	objWorkSheet.Range("E" & j).value = 119.9
Case "CESTA EMPRESARIAL 05" 
	objWorkSheet.Range("E" & j).value = 99.9
Case "CESTA EMPRESARIAL 06" 
	objWorkSheet.Range("E" & j).value = 256.5
Case "CESTA EMPRESARIAL 07" 
	objWorkSheet.Range("E" & j).value = 189.9
Case "CESTA MEI" 
	objWorkSheet.Range("E" & j).value = 35
Case "CESTA CONNECT" 
	objWorkSheet.Range("E" & j).value = 149.9
Case "CESTA CHEQUE EMPRESARIAL" 
	objWorkSheet.Range("E" & j).value = 19.52
Case "SEM PACOTE DE SERVICO"
	objWorkSheet.Range("E" & j).value = 30


End Select

Loop

objExcel.Visible = True
objWorkbook.SaveAs(strFileName)
'objExcel.Quit()
'Set ObjExcel = Nothing