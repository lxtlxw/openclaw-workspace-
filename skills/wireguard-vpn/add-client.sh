#!/bin/bash
# 添加WireGuard客户端脚本

set -e

if [ -z "$1" ]; then
    echo "用法: ./add-client.sh <客户端名称>"
    exit 1
fi

CLIENT_NAME=$1
SERVER_IP=$(curl -s https://api.ipify.org)
SERVER_PUBKEY=$(cat /etc/wireguard/publickey)

# 生成客户端密钥
cd /etc/wireguard
wg genkey | tee ${CLIENT_NAME}_privatekey | wg pubkey > ${CLIENT_NAME}_publickey
CLIENT_PRIVKEY=$(cat ${CLIENT_NAME}_privatekey)
CLIENT_PUBKEY=$(cat ${CLIENT_NAME}_publickey)

# 分配IP
CLIENT_IP="10.0.0.$(($(ls /etc/wireguard/*_privatekey | wc -l) + 1))/24"

# 添加到服务端配置
wg set wg0 peer $CLIENT_PUBKEY allowed-ips $(echo $CLIENT_IP | cut -d/ -f1)/32
wg-quick save wg0

# 生成客户端配置
cat > ${CLIENT_NAME}.conf << EOF
[Interface]
PrivateKey = $CLIENT_PRIVKEY
Address = $CLIENT_IP
DNS = 8.8.8.8, 1.1.1.1

[Peer]
PublicKey = $SERVER_PUBKEY
Endpoint = $SERVER_IP:51820
AllowedIPs = 0.0.0.0/0, ::/0
PersistentKeepalive = 25
EOF

echo ""
echo "=== 客户端 $CLIENT_NAME 创建完成 ==="
echo "客户端配置文件: /etc/wireguard/${CLIENT_NAME}.conf"
echo "QR码 (手机扫描):"
qrencode -t ansiutf8 < /etc/wireguard/${CLIENT_NAME}.conf
echo ""
echo "配置内容:"
cat /etc/wireguard/${CLIENT_NAME}.conf
