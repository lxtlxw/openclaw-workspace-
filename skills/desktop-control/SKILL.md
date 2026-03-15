---
name: desktop-control
description: 桌面自动化控制，屏幕截图、鼠标控制（移动/点击/拖拽）、键盘输入、图像定位点击，支持游戏操作、浏览器自动化、桌面应用操作。使用当：需要AI控制电脑鼠标键盘、操作游戏、点击浏览器、自动化桌面操作。
---

# Desktop Control - 电脑桌面自动化控制

## Overview

本技能提供完整的桌面自动化控制能力，基于 PyAutoGUI：
- 全屏截图获取屏幕内容
- 鼠标移动/左键点击/右键点击/拖拽
- 键盘输入/按键按下/快捷键
- 图像模板匹配定位点击
- 支持游戏操作、浏览器点击、桌面应用自动化

## Core Capabilities

### 1. 屏幕截图
- 全屏截图保存为图像文件
- 可用于AI视觉分析识别屏幕内容

### 2. 鼠标控制
- 移动鼠标到指定坐标
- 左键单击/双击
- 右键单击
- 拖拽鼠标从起点到终点
- 滚轮滚动

### 3. 键盘控制
- 输入文本字符串
- 按下单个按键
- 组合键/快捷键
- 长按按键

### 4. 图像匹配点击
- 根据模板图像匹配找到屏幕上位置
- 自动点击匹配位置
- 用于点击游戏按钮、UI元素等

## Installation 安装

### Prerequisites
- Python 3 已安装
- pip 可用

### Install dependencies
```bash
pip install pyautogui pillow opencv-python
```

### Verify installation
```bash
python -c "import pyautogui; print('OK')"
```

## Available Scripts

All scripts are in `scripts/` directory:

### `scripts/screenshot.py`
Take full screen screenshot.
Usage:
```bash
python scripts/screenshot.py [output-path]
```
Default output: `screenshot.png`

### `scripts/mouse_click.py`
Click at specific coordinates.
Usage:
```bash
python scripts/mouse_click.py <x> <y> [button]
# button: left (default) | right | middle
```

### `scripts/mouse_move.py`
Move mouse to specific coordinates.
Usage:
```bash
python scripts/mouse_move.py <x> <y>
```

### `scripts/mouse_drag.py`
Drag mouse from start to end.
Usage:
```bash
python scripts/mouse_drag.py <start_x> <start_y> <end_x> <end_y>
```

### `scripts/type_text.py`
Type text string.
Usage:
```bash
python scripts/type_text.py "text-to-type"
```

### `scripts/press_key.py`
Press a single key or combination.
Usage:
```bash
python scripts/press_key.py "key-name"
# Examples: "enter", "esc", "ctrl+c", "win+r"
```

### `scripts/image_click.py`
Find image on screen and click it.
Usage:
```bash
python scripts/image_click.py template.png [confidence]
# confidence: 0-1, default 0.8
```

## Common Workflows

### Game automation workflow
1. `screenshot.py` - 获取当前游戏画面
2. AI视觉分析识别需要点击的位置/按钮
3. `mouse_click.py` - 点击目标位置
4. 重复执行需要的操作序列

### Find and click workflow
1. 模板图像保存为 `template.png`
2. `image_click.py template.png` - 自动找到并点击
3. 如果匹配失败，调整 confidence 参数

## Game Operation Examples

### Example: Click play button
If play button is at (1000, 500):
```bash
python scripts/mouse_click.py 1000 500
```

### Example: Click by template image
```bash
python scripts/image_click.py play-button.png 0.8
```

### Example: Move character with WASD
```bash
python scripts/press_key.py w
# wait, then
python scripts/press_key.py a
```

## References

- [PYAUTOGUI_REFERENCE.md](references/pyautogui-reference.md) - PyAutoGUI 按键名称参考
- [INSTALL.md](references/install.md) - 详细安装说明

