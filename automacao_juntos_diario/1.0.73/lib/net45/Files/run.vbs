
dd = Date
dd = replace(dd, "/", "")

strFileName = "C:\Temp\juntos_cad" & dd & ".xlsm"
'strFileName = "C:\Temp\juntos_cad.xlsm"


Set objExcel = CreateObject("Excel.Application")
objExcel.Visible = False
objExcel.DisplayAlerts = False
Set objWorkbook = objExcel.Workbooks.Open (strFileName)
Set objWorkSheet = objWorkbook.Worksheets(1)

'objExcel.Application.Run "juntos_cad.xlsm!ajuste"

objWorkbook.Save
objExcel.Quit

Set objWorkbook = Nothing
Set objWorkSheet = Nothing
Set objExcel = Nothing