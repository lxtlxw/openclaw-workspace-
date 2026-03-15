#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动整理素材分类工具
功能：将下载的素材自动按分类整理，方便快速检索和发给客户
"""
import os
import shutil
from pathlib import Path

# 配置分类目录
CATEGORIES = [
    "小红书文案",
    "抖音文案",
    "海报模板",
    "PPT模板",
    "短视频素材",
    "电商主图",
    "设计源文件",
    "其他"
]

def organize_materials(download_dir: str, output_dir: str):
    """自动整理下载文件夹中的素材到分类目录"""
    download_path = Path(download_dir)
    output_path = Path(output_dir)
    
    # 创建分类目录
    for cat in CATEGORIES:
        (output_path / cat).mkdir(exist_ok=True)
    
    # 遍历下载目录中的文件
    for file in download_path.iterdir():
        if file.is_file() and file.suffix.lower() not in [".exe", ".zip", ".rar"]:
            # 根据文件名关键词判断分类
            filename = file.name.lower()
            cat = "其他"
            
            if any(k in filename for k in ["小红书", "文案", "文章"]):
                cat = "小红书文案"
            elif any(k in filename for k in ["抖音", "短视频", "视频"]):
                cat = "短视频素材"
            elif any(k in filename for k in ["海报", "设计", "psd"]):
                cat = "海报模板"
            elif any(k in filename for k in ["ppt", "pptx"]):
                cat = "PPT模板"
            elif any(k in filename for k in ["主图", "电商"]):
                cat = "电商主图"
            
            # 移动文件
            shutil.move(str(file), str(output_path / cat / file.name))
            print(f"✅ 已整理：{file.name} → {cat}")

if __name__ == "__main__":
    # 修改这里为你的下载目录和输出目录
    DOWNLOAD_FOLDER = os.path.expanduser("~/Downloads")
    OUTPUT_FOLDER = "./materials"
    organize_materials(DOWNLOAD_FOLDER, OUTPUT_FOLDER)
    print("\n🎉 素材整理完成！")
