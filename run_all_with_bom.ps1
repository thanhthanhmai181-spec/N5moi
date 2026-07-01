$c = [System.IO.File]::ReadAllBytes('c:\Users\ADMIN\Desktop\N5 T12-2021\update_all_listen.ps1')
$b = [byte[]](0xEF, 0xBB, 0xBF)
[System.IO.File]::WriteAllBytes('c:\Users\ADMIN\Desktop\N5 T12-2021\update_all_listen_bom.ps1', $b + $c)
powershell.exe -ExecutionPolicy Bypass -File 'c:\Users\ADMIN\Desktop\N5 T12-2021\update_all_listen_bom.ps1'
