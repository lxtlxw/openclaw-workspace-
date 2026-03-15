#!/bin/bash
# WireGuard VPN 一键部署脚本
# 适用于Ubuntu/Debian/CentOS

set -e

echo "=== WireGuard VPN 一键部署 ==="

# 更新系统
echo "[1/6] 更新系统包..."
apt update -y && apt upgrade -y || yum update -y

# 安装WireGuard
echo "[2/6] 安装WireGuard..."
if [ -f /etc/debian_version ]; then
    apt install -y wireguard wireguard-tools qrencode
elif [ -f /etc/redhat-release ]; then
    dnf install -y wireguard-tools qrencode
fi

# 生成密钥
echo "[3/6] 生成密钥对..."
mkdir -p /etc/wireguard
cd /etc/wireguard
wg genkey | tee privatekey | wg pubkey > publickey

# 获取服务器公网IP
SERVER_IP=$(curl -s https://api.ipify.org)
echo "检测到服务器公网IP: $SERVER_IP"

# 生成服务端配置
echo "[4/6] 生成服务端配置..."
PRIVATE_KEY=$(cat /etc/wireguard/privatekey)
cat > /etc/wireguard/wg0.conf << EOF
[Interface]
PrivateKey = $PRIVATE_KEY
Address = 10.0.0.1/24
ListenPort = 51820
SaveConfig = true
PostUp = iptables -A FORWARD -i %i -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE; ip6tables -A FORWARD -i %i -j ACCEPT; ip6tables -t nat -A POSTROUTING -j MASQUERADE
PostDown = iptables -D FORWARD -i %i -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE; ip6tables -D FORWARD -i %i -j ACCEPT; ip6tables -t nat -D POSTROUTING -j MASQUERADE
EOF

# 开启IP转发
echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf
echo "net.ipv6.conf.all.forwarding = 1" >> /etc/sysctl.conf
sysctl -p

# 开启防火墙
ufw allow 51820/udp || firewalld-cmd --add-port=51820/udp --permanent && firewalld-cmd --reload

# 启动服务
echo "[5/6] 启动WireGuard服务..."
systemctl enable wg-quick@wg0
systemctl start wg-quick@wg0

echo ""
echo "=== 部署完成 ==="
echo "服务端配置: /etc/wireguard/wg0.conf"
echo "私钥: $(cat /etc/wireguard/privatekey)"
echo "公钥: $(cat /etc/wireguard/publickey)"
echo "服务器地址: $SERVER_IP:51820"
echo ""
echo "要添加客户端，请运行: ./add-client.sh <客户端名称>"
