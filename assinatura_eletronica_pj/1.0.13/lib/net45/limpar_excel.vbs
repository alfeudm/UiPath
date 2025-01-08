
Set fso = CreateObject("Scripting.FileSystemObject")



strFileName = WScript.Arguments.Item(0)

'strFileName = "C:\Users\alfeu_souza\Downloads\Relatorio_robo_portal_de_assinaturas_PJ021023.xlsx"


Set objExcel = CreateObject("Excel.Application")
objExcel.Visible = False
objExcel.DisplayAlerts= False

strXLSfile = strFileName


Set objWorkbook = objExcel.Workbooks.Open (strFileName, False)
Set objWorkSheet = objWorkbook.Worksheets(1)

objWorkSheet.Name = "Planilha1"

objWorkSheet.Range("CX1").value = "doc_pf_1"
objWorkSheet.Range("CY1").value = "doc_pf_2"
objWorkSheet.Range("CZ1").value = "anexo"

j = 2
y = 2
Do While objWorkSheet.Range("E" & j).value <> ""

if objWorkSheet.Range("M" & j).value = "" or objWorkSheet.Range("L" & j).value = "" or objWorkSheet.Range("P" & y).value = "" then

	objWorkSheet.Range("A" & j).EntireRow.Delete

else

j = j + 1
y = y + 1
End If
Loop

'y = 1
'Do While objWorkSheet.Range("E" & y).value <> ""

'if objWorkSheet.Range("P" & y).value = "" then

'	objWorkSheet.Range("A" & y).Value = "ok"
'	objWorkSheet.Range("B" & y).Value = "ERRO - Sem Modelo de assinatura"

'End If

'y = y + 1
'Loop


objWorkbook.ActiveSheet.UsedRange.RemoveDuplicates Array(5), 1

objWorkbook.SaveAs(strFileName)
objExcel.Quit()
Set ObjExcel = Nothing


