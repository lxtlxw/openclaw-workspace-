# Update GitHub hosts with latest IPs
$hostsPath = "C:\Windows\System32\drivers\etc\hosts"
$newHosts = Get-Content "C:\Users\Administrator\.openclaw\workspace\latest_github_hosts.txt"

# Check if already has GitHub hosts
$currentHosts = Get-Content $hostsPath
if ($currentHosts -match "#Github Hosts Start") {
    Write-Host "GitHub hosts already exists, removing old entries..."
    $newCurrent = $currentHosts | Select-String -NotMatch "#Github Hosts Start|#Github Hosts End|github\.com|githubusercontent|githubassets"
} else {
    $newCurrent = $currentHosts
}

# Append new hosts
$final = $newCurrent + "`n`n" + $newHosts
$final | Out-File -FilePath $hostsPath -Encoding ASCII

Write-Host "GitHub hosts updated successfully!"
Write-Host "Flushing DNS cache..."
ipconfig /flushdns
Write-Host "Done!"
