Const xlTextQualifierDoubleQuote = 1
Const xlInsertDeleteCells = 1
Const xlFixedWidth = 2

strFileName = "C:\Temp\relcheque.xlsx"
strTextFile = "C:\Temp\CHEQUE20.txt"

Set objExcel = CreateObject("Excel.Application")
objExcel.Visible = False
objExcel.DisplayAlerts= False

strCSVfile = strTextFile
strXLSfile = strFileName

Set objWorkbook = objExcel.Workbooks.Add
objWorkbook.SaveAs(strFileName)
Set objWorkbook = objExcel.Workbooks.Open (strFileName)
Set objWorkSheet = objWorkbook.Worksheets(1)
objWorkSheet.Range("A:A").NumberFormat = "@"
With objWorkSheet.QueryTables.Add("TEXT;" & strCSVfile, objWorkSheet.Range("$A$1"))
    .Name = "input"
    .FieldNames = False
    .RowNumbers = False
    .FillAdjacentFormulas = False
    .PreserveFormatting = True
    .RefreshOnFileOpen = False
    .RefreshStyle = xlInsertDeleteCells
    .SavePassword = False
    .SaveData = True
    .AdjustColumnWidth = True
    .RefreshPeriod = 0
    .TextFilePromptOnRefresh = False
    .TextFilePlatform = 437
    .TextFileStartRow = 8
    .TextFileParseType = xlFixedWidth
    .TextFileTextQualifier = xlTextQualifierDoubleQuote
    .TextFileConsecutiveDelimiter = False
    .TextFileTabDelimiter = False
    .TextFileSemicolonDelimiter = False
    .TextFileCommaDelimiter = False
    .TextFileSpaceDelimiter = False
    .TextFileOtherDelimiter = False '"#"
    .TextFileFixedColumnWidths = Array(8,20,15,89)
    .TextFileTrailingMinusNumbers = True
    .Refresh False
End With

objWorkSheet.Range("B:B").EntireColumn.Delete
objWorkSheet.Range("C:C").EntireColumn.Delete
objWorkSheet.Range("A1").value = "Conta"
objWorkSheet.Range("B1").value = "Saldo Disponivel"
objWorkSheet.Range("C:C").EntireColumn.Delete
'objWorkSheet.Range("A:A").Replace "-", ""
'WScript.Sleep 1000
objWorkSheet.Range("A:A").Replace "========", ""
objWorkSheet.Range("A:A").Replace "-", ""

LastRow = objWorkSheet.Range("B" & objWorkSheet.Rows.Count).End(-4162).Row
objWorkSheet.Range("B2:B" & LastRow).Copy
objWorkSheet.Range("C1").PasteSpecial
objWorkSheet.Range("B:B").EntireColumn.Delete
objWorkSheet.Range("B1").value = "Saldo Disponivel"


'objExcel.Application.Run "rel.xlsm!separar_coluna"

objWorkbook.SaveAs(strFileName)
objExcel.Quit()
Set ObjExcel = Nothing