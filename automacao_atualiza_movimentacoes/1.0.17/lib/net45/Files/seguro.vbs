Const xlTextQualifierDoubleQuote = 1
Const xlInsertDeleteCells = 1
Const xlFixedWidth = 2
Const xlWhole = 1 
Const xlPart  = 2 

Set fso = CreateObject("Scripting.FileSystemObject")

for f = 1 to 200

strFileName = "C:\Temp\seeg\seeg" & f & ".xlsx"
strTextFile = "C:\Temp\MOVIMENT PART" & f & ".txt"

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
    .TextFileStartRow = 1
    .TextFileParseType = xlFixedWidth
    .TextFileTextQualifier = xlTextQualifierDoubleQuote
    .TextFileConsecutiveDelimiter = False
    .TextFileTabDelimiter = False
    .TextFileSemicolonDelimiter = False
    .TextFileCommaDelimiter = False
    .TextFileSpaceDelimiter = False
    .TextFileOtherDelimiter = False '"#"
    .TextFileFixedColumnWidths = Array(8, 8, 31, 11, 4, 71)
    .TextFileTrailingMinusNumbers = True
    .Refresh False

End With


objWorkSheet.Range("H:H").EntireColumn.Delete
objWorkSheet.Range("G:G").EntireColumn.Delete
objWorkSheet.Range("F:F").EntireColumn.Delete
objWorkSheet.Range("C:C").EntireColumn.Delete
objWorkSheet.Range("A:A").EntireColumn.Delete
'objWorkSheet.Range("E:E").EntireColumn.Delete
objWorkSheet.Range("A:A").Replace "-", ""
objWorkSheet.Range("A1").value = "Conta"
objWorkSheet.Range("B1").value = "desc"
objWorkSheet.Range("C1").value = "cod"

objWorkbook.SaveAs(strFileName)
objExcel.Quit()
Set ObjExcel = Nothing
End if

Next
