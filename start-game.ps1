# 一键切换到 "玩POE2游戏模式" - 关闭代理，解决登录错误1067104
Write-Host "=== 切换到 游戏模式 ===" -ForegroundColor Green

# 关闭系统代理
Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings' -name ProxyEnable -value 0
# 清除环境变量
[Environment]::SetEnvironmentVariable("HTTP_PROXY", $null, "User")
[Environment]::SetEnvironmentVariable("HTTPS_PROXY", $null, "User")
$env:HTTP_PROXY=$null
$env:HTTPS_PROXY=$null

Write-Host "✅ 系统代理已关闭" -ForegroundColor Green
Write-Host "✅ 环境变量代理已清除" -ForegroundColor Green
Write-Host "现在可以正常启动 POE2 游戏，不会报 1067104 错误了"
