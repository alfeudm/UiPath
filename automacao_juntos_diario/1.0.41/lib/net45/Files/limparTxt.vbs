Const ForReading = 1
Const ForWriting = 2

Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objFile = objFSO.OpenTextFile("C:\Temp\CONTAS.PRN", ForReading)

strText = objFile.ReadAll
objFile.Close
strText = Replace(strText, "====================================================================================================", "")
strText = Replace(strText, "----------------------------------------------------------------------------------------------------", "")
strText = Replace(strText, " CONTA   TITULAR                                          UA/NUCLEO CARTEIRA DT. ABERT.   TIPO", "")
strText = Replace(strText, "                                     C.C.P.I. CAMINHO DAS AGUAS                                     ", "")
strText = Replace(strText, "                            SISTEMA SICREDI - SISTEMA DE ATENDIMENTO                        PAGINA: ", "")
strText = Replace(strText, "P", "")
strText = Replace(strText,"                                RELATORIO DE ABERTURA DE CONTAS                                ", "")
strText = Replace(strText,"                      SISTEMA SICREDI - AUXILIAR - 8.92                       PAGINA: ", "")
strText = Replace(strText,"CB", "")
strText = Replace(strText,"LEGENDA: [*]-CONTA ENCERRADA.", "")
Set objFile = objFSO.OpenTextFile("C:\Temp\CONTAS.PRN", ForWriting)
objFile.WriteLine strText

objFile.Close