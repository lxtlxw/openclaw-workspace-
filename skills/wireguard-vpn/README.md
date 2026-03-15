# WireGuard VPN 自建部署方案

WireGuard 是目前最先进的VPN方案，性能好、体积小、加密安全。

## 一键部署步骤

### 1. 准备工作
- 一台海外云服务器（推荐阿里云新加坡/腾讯云香港/Vultr/DigitalOcean）
- 系统：Ubuntu 20.04+/Debian 10+/CentOS 8+
- 服务器允许51820 UDP端口入站

### 2. 一键部署

```bash
# 下载脚本
wget https://raw.githubusercontent.com/.../setup-wireguard.sh
# 或者直接在服务器上创建后粘贴内容

# 赋予执行权限
chmod +x setup-wireguard.sh

# 运行部署
sudo ./setup-wireguard.sh
```

### 3. 添加客户端

```bash
# 添加一个名为phone的客户端
sudo ./add-client.sh phone

# 添加一个名为laptop的客户端
sudo ./add-client.sh laptop
```

### 4. 客户端连接

**手机端**
1. 下载WireGuard App：iOS App Store / Google Play
2. 扫描终端输出的QR码，一键添加连接
3. 点击连接即可

**Windows/macOS端**
1. 从官网下载WireGuard客户端: https://www.wireguard.com/install/
2. 导入生成的`.conf`配置文件
3. 点击激活连接

## 特性

- ✅ 端到端加密，安全可靠
- ✅ 比OpenVPN快2-3倍
- ✅ 占用资源极小，1核1G服务器就能跑5-10人
- ✅ 支持手机、电脑多设备同时连接
- ✅ 漫游自动重连，切换网络不中断

## 客户端下载地址

- 官网: https://www.wireguard.com/install/
- GitHub: https://github.com/WireGuard/WireGuard

## 常见问题

**Q: 连接后不能上网？**
A: 检查服务器IP转发是否开启，检查防火墙UDP 51820是否开放。

**Q: 速度慢？**
A: 选择距离你近的服务器节点，WireGuard本身速度很快，瓶颈在服务器带宽。

**Q: 支持多设备同时连接吗？**
A: 支持，每个设备一个客户端配置即可。
