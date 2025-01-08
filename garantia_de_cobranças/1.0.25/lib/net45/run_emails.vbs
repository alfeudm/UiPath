dd = Date
dd = replace(dd, "/", ".")
dd = replace(dd, "2022", "22")

strFileName = "C:\Users\alfeu_souza\Documents\cobranca_em_carteira" & dd & ".xlsm"

Set objExcel = CreateObject("Excel.Application")
objExcel.Visible = False
objExcel.DisplayAlerts= False
Set objWorkbook = objExcel.Workbooks.Open (strFileName)
Set objWorkSheet = objWorkbook.Worksheets(1)




