# One-click switch to "POE2 Game Mode" - close proxy to fix login error 1067104
Write-Host "=== Switch to Game Mode ===" -ForegroundColor Green

# Close system proxy
Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings' -name ProxyEnable -value 0
# Clear environment variables
[Environment]::SetEnvironmentVariable("HTTP_PROXY", $null, "User")
[Environment]::SetEnvironmentVariable("HTTPS_PROXY", $null, "User")
$env:HTTP_PROXY=$null
$env:HTTPS_PROXY=$null

Write-Host "✅ System proxy closed" -ForegroundColor Green
Write-Host "✅ Environment proxy cleared" -ForegroundColor Green
Write-Host "You can now start POE2, login error 1067104 should be fixed"
