
dd = Date
dd = replace(dd, "/", "")

strFileName = "C:\Temp\juntos_cad" & dd & ".xlsm"

Set objExcel = CreateObject("Excel.Application")
objExcel.Visible = False
objExcel.DisplayAlerts= False
Set objWorkbook = objExcel.Workbooks.Open (strFileName)
Set objWorkSheet = objWorkbook.Worksheets(1)




