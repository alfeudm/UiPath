
dd = Date
dd = replace(dd, "/", "")

strFileName = "C:\Users\APP_0109_ROBO001UNA\Documents\UiPath\Automcao_Juntos_Diario\Files\juntos_cad.xlsm"
'strFileName = "C:\Temp\juntos_cad.xlsm"


Set xlApp = CreateObject("Excel.Application")
xlApp.Visible = false
Set wb = xlApp.Workbooks.Open(strFileName)
Set ws = wb.Worksheets(1)
Set c = ws.range("A1")

ws.Range("A2:BM9999").ClearContents

wb.Save
wb.close
xlApp.Quit

Set wb = Nothing
Set ws = Nothing
Set xlApp = Nothing