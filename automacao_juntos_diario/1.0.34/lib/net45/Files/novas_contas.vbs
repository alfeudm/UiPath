Const xlTextQualifierDoubleQuote = 1
Const xlInsertDeleteCells = 1
Const xlFixedWidth = 2
Set fso = CreateObject("Scripting.FileSystemObject")

dd = Date
dd = replace(dd, "/", "")

strFileName = "C:\Temp\juntos" & dd & ".xlsx"
strTextFile = "C:\Temp\CONTAS.PRN"

If (fso.FileExists(strTextFile)) Then

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
    .TextFileStartRow = 2
    .TextFileParseType = xlFixedWidth
    .TextFileTextQualifier = xlTextQualifierDoubleQuote
    .TextFileConsecutiveDelimiter = False
    .TextFileTabDelimiter = False
    .TextFileSemicolonDelimiter = False
    .TextFileCommaDelimiter = False
    .TextFileSpaceDelimiter = False
    .TextFileOtherDelimiter = False '"#"
    .TextFileFixedColumnWidths = Array(9, 48, 8, 8, 14)
    .TextFileTrailingMinusNumbers = True
    .Refresh False

End With


objWorkSheet.Range("F:F").EntireColumn.Delete
objWorkSheet.Range("A:A").Replace "-", ""
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

