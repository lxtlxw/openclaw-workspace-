#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动发货机器人
功能：客户添加好友/付款后，自动回复素材链接和提取码，支持分销
"""
import time
import json
from pathlib import Path

# 素材库配置，添加你自己的链接
MATERIALS = {
    "自媒体全品类素材终身VIP": {
        "price": "88",
        "link": "https://pan.baidu.com/s/1g5SpjwAZbXLm7z22QTDlIg",
        "pwd": "iwej",
        "desc": "包含10000+素材：小红书爆款文案/抖音热门短视频/PPT模板/海报设计模板/电商主图素材，终身更新"
    }
}

def save_config():
    """保存配置"""
    with open("materials_config.json", "w", encoding="utf-8") as f:
        json.dump(MATERIALS, f, ensure_ascii=False, indent=2)

def get_delivery_text(product_name: str) -> str:
    """获取自动发货文案"""
    if product_name not in MATERIALS:
        return "❌ 未找到该商品，请联系客服确认"
    
    product = MATERIALS[product_name]
    return f"""🎉 感谢购买【{product_name}】
💰 价格：{product['price']}
📎 下载链接：{product['link']}
🔑 提取码：{product['pwd']}
ℹ️  {product['desc']}

如果链接失效，请随时联系我补发！
"""

def auto_reply_loop():
    """自动回复循环，配合微信自动回复工具使用"""
    print("🤖 自动发货机器人已启动，输入商品名称即可获取发货文案")
    while True:
        product = input("\n请输入商品名称：")
        if product.lower() in ["exit", "quit", "q"]:
            break
        print("\n" + get_delivery_text(product))

if __name__ == "__main__":
    save_config()
    auto_reply_loop()
