
strFileName = "C:\Users\Public\Documents\format.xlsm"

Set objExcel = CreateObject("Excel.Application")
objExcel.Visible = False
objExcel.DisplayAlerts= False
Set objWorkbook = objExcel.Workbooks.Open (strFileName)
Set objWorkSheet = objWorkbook.Worksheets(1)

objExcel.Application.Run "format.xlsm!layout"



