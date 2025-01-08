Const xlTextQualifierDoubleQuote = 1
Const xlInsertDeleteCells = 1
Const xlFixedWidth = 2
Const xlWhole = 1 
Const xlPart  = 2 

Set fso = CreateObject("Scripting.FileSystemObject")

for f = 1 to 200

strFileName = "C:\Temp\moov\moov" & f & ".xlsx"
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
    .TextFileFixedColumnWidths = Array(8, 8, 42, 4, 35, 14, 19, 3)
    .TextFileTrailingMinusNumbers = True
    .Refresh False

End With

objWorkSheet.Range("A:A").EntireColumn.Delete
'objWorkSheet.Range("H:H").EntireColumn.Delete
objWorkSheet.Range("G:G").EntireColumn.Delete
objWorkSheet.Range("D:D").EntireColumn.Delete
objWorkSheet.Range("B:B").EntireColumn.Delete
objWorkSheet.Range("E:E").EntireColumn.Delete
objWorkSheet.Range("A:A").Replace "-", ""
objWorkSheet.Range("A1").value = "Conta"
objWorkSheet.Range("B1").value = "cod"
objWorkSheet.Range("C1").value = "vlr_credito"
objWorkSheet.Range("D1").value = "vlr_movimento"

LastRow = objWorkSheet.Range("D" & objWorkSheet.Rows.Count).End(-4162).Row
objWorkSheet.Range("D2:D" & LastRow).Copy
objWorkSheet.Range("E1").PasteSpecial

objWorkSheet.Range("E1").value = "data_movimento"

objWorkbook.SaveAs(strFileName)
objExcel.Quit()
Set ObjExcel = Nothing
End if

Next
