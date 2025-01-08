Const xlTextQualifierDoubleQuote = 1
Const xlInsertDeleteCells = 1
Const xlFixedWidth = 2

strFileName = "C:\Temp\rel.xlsx"
strTextFile = "C:\Temp\SALDO022.txt"

Set objExcel = CreateObject("Excel.Application")
objExcel.Visible = False
objExcel.DisplayAlerts= False

strCSVfile = strTextFile
strXLSfile = strFileName

Set objWorkbook = objExcel.Workbooks.Add
objWorkbook.SaveAs(strFileName)
Set objWorkbook = objExcel.Workbooks.Open (strFileName)
Set objWorkSheet = objWorkbook.Worksheets(1)
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
    .TextFileFixedColumnWidths = Array(8,89,16,21)
    .TextFileTrailingMinusNumbers = True
    .Refresh False
End With

objWorkSheet.Range("B:B").EntireColumn.Delete
objWorkSheet.Range("C:C").EntireColumn.Delete
objWorkSheet.Range("A1").value = "Conta"
objWorkSheet.Range("B1").value = "Saldo Disponivel"
objWorkSheet.Range("A:A").Replace "-", ""
objWorkSheet.Range("B:B").Replace ",", "."
'WScript.Sleep 1000

objWorkbook.SaveAs(strFileName)
objExcel.Quit()
Set ObjExcel = Nothing