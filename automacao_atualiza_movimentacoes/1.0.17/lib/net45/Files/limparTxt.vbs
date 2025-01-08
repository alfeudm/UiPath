Const ForReading = 1
Const ForWriting = 2

Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objFile = objFSO.OpenTextFile("C:\Temp\MOVIMENT.txt", ForReading)

strText = objFile.ReadAll
objFile.Close
strText = Replace(strText, "=====================================================================================================================================", "")
strText = Replace(strText, "------------------------------------------------------------------------------------------------------------------------------------", "")
strText = Replace(strText, "------------------------------------------------------------------------------------------------------------------------------------", "")
strText = Replace(strText, "                                                     C.C.P.I. CAMINHO DAS AGUAS                                                      ", "")
strText = Replace(strText, "                                SISTEMA SICREDI - SISTEMA DE ATENDIMENTO - A.31                                PAGINA: ", "")
strText = Replace(strText, "                       MOVIMENTO DIARIO DO CONTA CORRENTE", "")
strText = Replace(strText, "Origem  Conta   Nome Correntista                Docto     Cod Descricao                 DR              Debito            Credito Id", "")
strText = Replace(strText, "                                                                                                                           Data/Hora", "")
strText = Replace(strText, " - POSTO: 01 A ZZ                      ", "")
strText = Replace(strText, "                                        Total UA: ", "")
strText = Replace(strText, " ==>        LCTOS : ", "")
strText = Replace(strText, "", "")
strEspaco = " " & vbCr & "                                                                                                        "
strEspaco = " " & vbCr & "                                                                                                        "
strEspaco = "" & vbCr & "                                                                                                        "
strText = Replace(strText, strEspaco, "")
strText = Replace(strText, "====================================================================================================================================", "")
strText = Replace(strText, "                                        TOTAIS DO DIA", "")
strText = Replace(strText, "                                                     TOTAL GERAL", "")
strText = Replace(strText, "Legenda----------------------------------------DR -> Dia do Lancamento Retroativo     Id -> Identificacao do Posto Origem    Origem -> Movimentos ONLINE onde       9999/99 - UA/PAC origem                ----------------------------------------", "")
Set objFile = objFSO.OpenTextFile("C:\Temp\MOVIMENT.txt", ForWriting)
objFile.WriteLine strText

objFile.Close