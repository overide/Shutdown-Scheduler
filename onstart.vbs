Set WshShell = CreateObject("WScript.Shell" ) 
WshShell.Run chr(34) & "c:\Python34\onstart.bat" & Chr(34), 0 
Set WshShell = Nothing 