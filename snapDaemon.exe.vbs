pythonScriptPath = "C:\Absolute\Path\To\snapDaemon.py"

' --- EXECUTION ---
' Make changes as required.
' pythonw.exe       -> Runs Python without a console window.
' -t h -f 4         -> Sets frequency to 4 captures per hour.
' -p "C:\Captures"  -> Sets the custom save path.
command = "pythonw.exe """ & pythonScriptPath & """ -t h -f 4 -p ""C:\Captures"""


Set WshShell = WScript.CreateObject("WScript.Shell")
WshShell.Run command, 0, False
Set WshShell = Nothing