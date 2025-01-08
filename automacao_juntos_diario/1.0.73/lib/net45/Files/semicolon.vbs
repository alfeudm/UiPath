Const ForReading = 1
Const ForWriting = 2

strFileName = WScript.Arguments.Item(0)

'strFileName ="C:\Users\app_0109_pva\Documents\juntos_cad07032023.csv"

Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objFile = objFSO.OpenTextFile(strFileName, ForReading)

strText = objFile.ReadAll
objFile.Close
strText = Replace(strText,",", ";")
Set objFile = objFSO.OpenTextFile(strFileName, ForWriting)
objFile.WriteLine strText

objFile.Close