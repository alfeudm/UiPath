Const xlTextQualifierDoubleQuote = 1
Const xlInsertDeleteCells = 1
Const xlFixedWidth = 2

strFileName = "C:\Temp\tp_cesta.xlsx"
strTextFile = "C:\Temp\CONTATUA.PRN"

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
    .TextFileFixedColumnWidths = Array(61,8,2,2,17,4,2,17,10)
    .TextFileTrailingMinusNumbers = True
    .Refresh False
End With

objWorkSheet.Range("J:J").EntireColumn.Delete
objWorkSheet.Range("G:G").EntireColumn.Delete
objWorkSheet.Range("D:D").EntireColumn.Delete
objWorkSheet.Range("A:A").EntireColumn.Delete
objWorkSheet.Range("A1").value = "Conta"
objWorkSheet.Range("B1").value = "cod1"
objWorkSheet.Range("C1").value = "desc1"
objWorkSheet.Range("D1").value = "cod2"
objWorkSheet.Range("E1").value = "desc2"
objWorkSheet.Range("F1").value = "tp"
objWorkSheet.Range("A:A").Replace "-", ""
'objWorkSheet.Range("B:B").Replace ",", "."
'WScript.Sleep 1000

objWorkbook.SaveAs(strFileName)
objExcel.Quit()
Set ObjExcel = Nothing