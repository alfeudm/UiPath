Const xlTextQualifierDoubleQuote = 1
Const xlInsertDeleteCells = 1
Const xlFixedWidth = 2
Set fso = CreateObject("Scripting.FileSystemObject")

dd = Date
dd = replace(dd, "/", "")

strFileName = "C:\Temp\juntos" & dd & ".xlsx"


If (fso.FileExists(strFileName)) Then

Set objExcel = CreateObject("Excel.Application")
objExcel.Visible = False
objExcel.DisplayAlerts= False

strXLSfile = strFileName


Set objWorkbook = objExcel.Workbooks.Open (strFileName)
Set objWorkSheet = objWorkbook.Worksheets(1)

objWorkSheet.Range("E:E").EntireColumn.Delete
objWorkSheet.Range("D:D").EntireColumn.Delete
objWorkSheet.Range("C:C").EntireColumn.Delete
objWorkSheet.Range("B:B").EntireColumn.Delete
objWorkSheet.Range("A:A").EntireColumn.Delete

objWorkSheet.Range("A1").value = "num_conta"
objWorkSheet.Range("B1").value = "Nome"
objWorkSheet.Range("C1").value = "AG"
objWorkSheet.Range("D1").value = "carteira"
objWorkSheet.Range("E1").value = "dt_abertura"
objWorkSheet.Range("E:E").Replace " 00:00:00", ""
objWorkSheet.Range("E:E").NumberFormat = "dd/mm/yyyy"


objWorkbook.SaveAs(strFileName)
objExcel.Quit()
Set ObjExcel = Nothing
End if

