$c = [System.IO.File]::ReadAllBytes('c:\Users\ADMIN\Desktop\N5 T12-2021\update_ps.ps1')
$b = [byte[]](0xEF, 0xBB, 0xBF)
[System.IO.File]::WriteAllBytes('c:\Users\ADMIN\Desktop\N5 T12-2021\update_ps_bom.ps1', $b + $c)
powershell.exe -ExecutionPolicy Bypass -File 'c:\Users\ADMIN\Desktop\N5 T12-2021\update_ps_bom.ps1'
