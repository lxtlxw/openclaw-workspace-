#!/usr/bin/env python3
"""
POE2 流放之路2 法师(学法) 飞雷神 自动刷神庙脚本
用法：
1. 准备好 templates/ 目录下三张模板图
2. 运行 python poe2-farm-temple-ele.py [rounds]
3. 保证游戏窗口可见，脚本会：
   - 点击神庙入口 → 确认进入
   - 自动循环放飞雷神技能清图
   - 打完点退出传送门回藏身处
"""

import sys
import time
import random
import pyautogui
import cv2
import numpy as np

# ========== 配置 - 根据你的实际情况调整 ==========
CONFIDENCE = 0.7               # 匹配阈值，匹配不到就调低
DELAY_AFTER_CLICK = 1.0        # 点击后等待
DELAY_LOADING = 6.0            # 进图加载等待
DELAY_EXIT_LOADING = 8.0       # 退出加载等待
SKILL_CYCLE_SECONDS = 90       # 清图时间，根据神庙层数调整
SKILL1_KEY = '1'               # 飞雷神主要输出技能按键
SKILL2_KEY = '2'               # 位移技能按键
FLASK_KEY = 'q'                 # 药瓶/抗性药水按键
SKILL_CAST_INTERVAL_MIN = 0.3  # 最小技能间隔
SKILL_CAST_INTERVAL_MAX = 0.8  # 最大技能间隔
MOVE_RANDOM_RANGE = 50         # 随机移动范围，避免站着不动

# ========== 核心函数 ==========
def find_and_click(template_path, confidence=CONFIDENCE):
    """Find template on screen and click it"""
    template = cv2.imread(template_path)
    if template is None:
        print(f"ERROR: Cannot load {template_path}")
        return False
    
    screenshot = pyautogui.screenshot()
    screen_np = np.array(screenshot)
    screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
    
    # Check if template is larger than screen, resize it
    screen_h, screen_w = screen_bgr.shape[:2]
    template_h, template_w = template.shape[:2]
    
    if template_h > screen_h or template_w > screen_w:
        # Template is larger than screen, this shouldn't happen
        # Try to resize it to fit
        scale = min(screen_h / template_h, screen_w / template_w)
        new_h = int(template_h * scale)
        new_w = int(template_w * scale)
        template = cv2.resize(template, (new_w, new_h), interpolation=cv2.INTER_AREA)
        print(f"WARNING: {template_path} was larger than screen, resized to {new_w}x{new_h}")
    
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

def cast_skill_cycle(duration_seconds):
    """飞雷神技能循环：随机放技能，随机小范围移动"""
    print(f"\nStarting skill casting cycle for {duration_seconds} seconds...")
    start_time = time.time()
    
    while time.time() - start_time < duration_seconds:
        # Random small mouse movement to avoid AFK detection
        rx = random.randint(-MOVE_RANDOM_RANGE, MOVE_RANDOM_RANGE)
        ry = random.randint(-MOVE_RANDOM_RANGE, MOVE_RANDOM_RANGE)
        pyautogui.moveRel(rx, ry, duration=0.2)
        
        # Cast main skill (飞雷神)
        pyautogui.press(SKILL1_KEY)
        interval = random.uniform(SKILL_CAST_INTERVAL_MIN, SKILL_CAST_INTERVAL_MAX)
        time.sleep(interval)
        
        # Occasionally cast second skill (movement/dash)
        if random.random() < 0.3:
            pyautogui.press(SKILL2_KEY)
            time.sleep(interval)
        
        # Occasionally use flask
        if random.random() < 0.1:
            pyautogui.press(FLASK_KEY)
            time.sleep(0.5)
    
    print("Skill cycle completed, map should be cleared")
    return True

def run_one_round():
    """Run one round of temple farming"""
    print("\n" + "="*40)
    print("Starting new temple round")
    print("="*40)
    
    # 1. Find and click temple entry button in hideout
    if not find_and_click("templates/entry-button.png"):
        print("Failed to find entry button, check your template screenshot")
        return False
    
    # 2. Click accept to enter
    time.sleep(1)
    if not find_and_click("templates/accept-button.png"):
        print("Failed to find accept button")
        return False
    
    # 3. Wait for map to load
    print(f"Waiting {DELAY_LOADING}s for temple to load...")
    time.sleep(DELAY_LOADING)
    
    # 4. Auto cast skills to clear temple
    cast_skill_cycle(SKILL_CYCLE_SECONDS)
    
    # 5. Find exit portal and click
    print("Looking for exit portal...")
    if not find_and_click("templates/exit-portal.png"):
        print("Failed to find exit portal")
        return False
    
    # 6. Wait back to hideout
    print(f"Waiting {DELAY_EXIT_LOADING}s returning to hideout...")
    time.sleep(DELAY_EXIT_LOADING)
    
    print("\n✅ Round complete!")
    return True

def main():
    rounds = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    print(f"POE2 Temple Farming - Mage (Elementalist) Fly Thunder")
    print(f"Total rounds: {rounds}")
    print("\n!!! IMPORTANT:")
    print(f"- Game window must be visible")
    print(f"- Templates must be in ./templates/ (entry-button.png, accept-button.png, exit-portal.png)")
    print(f"- Skills: {SKILL1_KEY}=main, {SKILL2_KEY}=movement, {FLASK_KEY}=flask")
    print(f"- Press Ctrl+C to stop anytime")
    print("\nStarting in 5 seconds...")
    time.sleep(5)
    
    success = 0
    for i in range(rounds):
        print(f"\n--- Round {i+1}/{rounds} ---")
        if run_one_round():
            success += 1
    
    print("\n" + "="*40)
    print(f"FINISHED: Total {rounds} rounds, Success {success}")
    print("="*40)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nStopped by user")
