#!/usr/bin/env python3
"""
POE2 流放之路2 神庙自动刷神庙脚本
基于 desktop-control 技能 + PyAutoGUI

使用前准备：
1. 在游戏主界面，截图保存神庙入口按钮为 templates/entry-button.png
2. 截图保存确认进入按钮为 templates/accept-button.png
3. 截图保存退出传送门为 templates/exit-portal.png
4. 调整 confidence 阈值根据实际匹配情况
5. 根据你的屏幕调整各个延时

运行：
python poe2-farm-temple.py [rounds]
默认 10 轮
"""

import sys
import time
import pyautogui
import cv2
import numpy as np

CONFIDENCE = 0.75
DELAY_AFTER_CLICK = 1.0
DELAY_LOADING = 5.0
DELAY_CLEAR = 120.0  # 清图时间，根据你的伤害调整

def find_and_click(template_path, confidence=CONFIDENCE):
    """Find template on screen and click it"""
    template = cv2.imread(template_path)
    if template is None:
        print(f"ERROR: Cannot load {template_path}")
        return False
    
    screenshot = pyautogui.screenshot()
    screen_np = np.array(screenshot)
    screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
    
    result = cv2.matchTemplate(screen_bgr, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    if max_val < confidence:
        print(f"No match found for {template_path} (confidence {max_val:.3f} < {confidence})")
        return False
    
    h, w = template.shape[:2]
    center_x = max_loc[0] + w // 2
    center_y = max_loc[1] + h // 2
    
    pyautogui.moveTo(center_x, center_y)
    time.sleep(0.2)
    pyautogui.click()
    print(f"Clicked {template_path} at ({center_x}, {center_y}) confidence {max_val:.3f}")
    time.sleep(DELAY_AFTER_CLICK)
    return True

def run_one_round():
    """Run one round of temple farming"""
    print("\n=== Starting new round ===")
    
    # 1. Find and click temple entry
    if not find_and_click("templates/entry-button.png"):
        print("Failed to find entry button")
        return False
    
    # 2. Wait for loading/animation and click accept
    time.sleep(2)
    if not find_and_click("templates/accept-button.png"):
        print("Failed to find accept button")
        return False
    
    # 3. Wait for map load
    print(f"Waiting {DELAY_LOADING}s for map loading...")
    time.sleep(DELAY_LOADING)
    
    # 4. Wait for clearing the temple
    print(f"Waiting {DELAY_CLEAR}s for clearing... (you kill the mobs)")
    # If you have a fully automatic build, you can add more logic here
    # to auto-pickup items, auto-move to chest, etc.
    time.sleep(DELAY_CLEAR)
    
    # 5. Find exit portal and click
    if not find_and_click("templates/exit-portal.png"):
        print("Failed to find exit portal")
        return False
    
    # 6. Wait back to hideout
    print(f"Waiting {DELAY_LOADING}s for returning to hideout...")
    time.sleep(DELAY_LOADING)
    
    print("=== Round complete ===")
    return True

def main():
    rounds = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    print(f"Starting POE2 temple farming, total {rounds} rounds")
    print("Make sure game window is open and visible on screen!")
    print("Press Ctrl+C to stop")
    time.sleep(3)
    
    success = 0
    for i in range(rounds):
        print(f"\n--- Round {i+1}/{rounds} ---")
        if run_one_round():
            success += 1
    
    print(f"\n=== Finished ===")
    print(f"Total: {rounds} rounds, Success: {success}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped by user")
