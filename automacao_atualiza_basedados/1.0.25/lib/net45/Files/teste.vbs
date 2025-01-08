
strFileName = "C:\Temp\moov\moov1.xlsx"

Set objExcel = CreateObject("Excel.Application")
objExcel.Visible = True
objExcel.DisplayAlerts= False

Set objWorkbook = objExcel.Workbooks.Open (strFileName)
Set ws = objWorkbook.Worksheets(1)

WScript.sleep 8000

const xlUp = -4162

LastRow = ws.Range("G" & ws.Rows.Count).End(xlUp).Row

ws.Range("G2:G" & LastRow).Copy

ws.Range("L1").PasteSpecial

'objWorkbook.SaveAs(strFileName)
'objExcel.Quit()
'Set ObjExcel = Nothing