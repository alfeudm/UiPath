Const xlTextQualifierDoubleQuote = 1
Const xlInsertDeleteCells = 1
Const xlFixedWidth = 2
Set fso = CreateObject("Scripting.FileSystemObject")

for f = 1 to 31

if f < 10 then
f = "0" & f
End if

strFileName = "C:\Temp\historico_debito\" & f & "DEBITO.xlsx"
strTextFile = "C:\Temp\DEBITO" & f & ".PRN"

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
    .TextFileFixedColumnWidths = Array(8, 34, 9, 17, 67)
    .TextFileTrailingMinusNumbers = True
    .Refresh False

End With


objWorkSheet.Range("B:B").EntireColumn.Delete
objWorkSheet.Range("C:C").EntireColumn.Delete
objWorkSheet.Range("D:D").EntireColumn.Delete
objWorkSheet.Range("A:A").Replace "-", ""
objWorkSheet.Range("A1").value = "num_conta"
objWorkSheet.Range("B1").value = "vlr_cesta"
objWorkSheet.Range("C1").value = "obs"


objWorkbook.SaveAs(strFileName)
objExcel.Quit()
Set ObjExcel = Nothing
End if

Next
