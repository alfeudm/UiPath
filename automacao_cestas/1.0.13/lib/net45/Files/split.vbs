    inputFile = "C:\Temp\MOVIMENT.txt"

    maxRows = 300000

        
    ReDim outputLines(maxRows - 1)
    p = InStrRev(inputFile, ".")
    part = 0
    n = 0
        
    Set FSO = CreateObject("Scripting.FileSystemObject")
        
    Set TSRead = FSO.OpenTextFile(inputFile)
    
    While Not TSRead.AtEndOfStream
        outputLines(n) = TSRead.ReadLine
        n = n + 1
        If n = maxRows Then
            part = part + 1
            outputFile = Left(inputFile, p - 1) & " PART" & part & Mid(inputFile, p)
            Set TSWrite = FSO.CreateTextFile(outputFile, True)
            TSWrite.Write Join(outputLines, vbCrLf)
            TSWrite.Close
            ReDim outputLines(maxRows - 1)
            n = 0
        End If
    Wend
    
    TSRead.Close

    If n > 0 Then
        ReDim outputlines2(n - 1)
        For i = 0 To n - 1
            outputlines2(i) = outputLines(i)
        Next
        part = part + 1
        outputFile = Left(inputFile, p - 1) & " PART" & part & Mid(inputFile, p)
        Set TSWrite = FSO.CreateTextFile(outputFile, True)
        TSWrite.Write Join(outputlines2, vbCrLf)
        TSWrite.Close
    End If