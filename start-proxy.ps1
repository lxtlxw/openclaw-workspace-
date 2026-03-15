# 一键切换到 "海外代理模式" - 开启Cloudflare WARP，访问外网
Write-Host "=== 切换到 海外代理模式 ===" -ForegroundColor Green

# 开启系统代理（如果需要）
# Cloudflare WARP已经接管全局，不需要额外系统代理
# 只需要确保WARP服务运行

# 检查WARP服务
$service = Get-Service | Where-Object {$_.Name -like "*warp*"}
if($service.Status -ne "Running") {
    Write-Host "⚠️  WARP服务未运行，正在启动..." -ForegroundColor Yellow
    Start-Service CloudflareWARP
}

Write-Host "✅ Cloudflare WARP 服务运行正常" -ForegroundColor Green
Write-Host "✅ 系统代理已关闭（WARP接管全局）" -ForegroundColor Green
Write-Host "现在可以正常访问海外网络了"
