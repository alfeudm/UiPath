Const xlTextQualifierDoubleQuote = 1
Const xlInsertDeleteCells = 1
Const xlFixedWidth = 2
Set fso = CreateObject("Scripting.FileSystemObject")

dd = Date
dd = replace(dd, "/", "")

strFileName = "C:\Temp\juntos_cad" & dd & ".xlsm"


If (fso.FileExists(strFileName)) Then

Set objExcel = CreateObject("Excel.Application")
objExcel.Visible = False
objExcel.DisplayAlerts= False

strXLSfile = strFileName


Set objWorkbook = objExcel.Workbooks.Open (strFileName)
Set objWorkSheet = objWorkbook.Worksheets(1)

objWorkSheet.Range("L:L").Value = Replace(objWorkSheet.Range("E:E").Value, ".com.", ".com"


objWorkbook.SaveAs(strFileName)
objExcel.Quit()
Set ObjExcel = Nothing
End if

