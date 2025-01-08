
Set fso = CreateObject("Scripting.FileSystemObject")



strFileName = WScript.Arguments.Item(0)

'strFileName = "C:\Users\alfeu_souza\Downloads\Relatorio_robo_portal_de_assinaturas_290323.xlsx"


Set objExcel = CreateObject("Excel.Application")
objExcel.Visible = False
objExcel.DisplayAlerts= False

strXLSfile = strFileName


Set objWorkbook = objExcel.Workbooks.Open (strFileName)
Set objWorkSheet = objWorkbook.Worksheets(1)

objWorkSheet.Name = "Planilha1"

objWorkbook.ActiveSheet.UsedRange.RemoveDuplicates Array(1), 1

j = 1
y = 2
Do While objWorkSheet.Range("G" & j).value <> ""

if objWorkSheet.Range("E" & j).value = "" or objWorkSheet.Range("A" & j).value = "" then

	objWorkSheet.Range("E" & j).EntireRow.Delete
else

j = j + 1
y = y + 1
End If
Loop

objWorkSheet.Range("AN1").value = "status_documento"
objWorkSheet.Range("AO1").value = "caminho_documento"
objWorkSheet.Range("AP1").value = "status_api"
objWorkSheet.Range("AQ1").value = "num_doc_api"
objWorkSheet.Range("AR1").value = "mensagem"
'objWorkSheet.Range("AS1").value = "chave"

j = 1

Do While objWorkSheet.Range("G" & j).value <> ""

if objWorkSheet.Range("AP" & j).value = "" then

	objWorkSheet.Range("AP" & j).value = "0"
	objWorkSheet.Range("AQ" & j).value = "0"
	objWorkSheet.Range("AR" & j).value = "0"
	objWorkSheet.Range("AS" & j).value = "0"
	objWorkSheet.Range("AT" & j).value = "0"
	objWorkSheet.Range("AU" & j).value = "0"
else

j = J + 1
End If
Loop



objWorkbook.SaveAs(strFileName)
objExcel.Quit()
Set ObjExcel = Nothing


