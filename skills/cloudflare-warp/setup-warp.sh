#!/bin/bash
# CloudFlare WARP 一键安装脚本
# 无需自有云服务器，免费使用CloudFlare网络加速

echo "=== CloudFlare WARP 一键安装 ==="

# 一键安装脚本
curl -fsSL https://pkg.cloudflareclient.com/install | bash

echo ""
echo "=== 安装完成 ==="
echo "运行 'warp-cli --help' 查看帮助"
echo "运行 'warp-cli connect' 连接"
echo "运行 'warp-cli status' 查看状态"
echo ""
echo "CloudFlare WARP 提供免费VPN/网络加速，无需服务器"
echo "官方网站: https://cloudflarewarp.com"
