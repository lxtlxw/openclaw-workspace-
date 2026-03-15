#!/usr/bin/env python3
"""
直接开始技能循环，已经在神庙里的时候用
用法: python start_skill_cycle.py [seconds]
默认 90 秒
"""

import sys
import time
import random
import pyautogui

# ========== 配置 ==========
SKILL_CYCLE_SECONDS = 90 if len(sys.argv) < 2 else int(sys.argv[1])
SKILL1_KEY = '1'               # 飞雷神主要输出
SKILL2_KEY = '2'               # 位移技能
FLASK_KEY = 'q'                 # 药水
SKILL_CAST_INTERVAL_MIN = 0.3
SKILL_CAST_INTERVAL_MAX = 0.8
MOVE_RANDOM_RANGE = 50

def cast_skill_cycle(duration_seconds):
    """飞雷神技能循环：随机放技能，随机小范围移动"""
    print(f"\nStarting skill casting cycle for {duration_seconds} seconds...")
    print(f"Skills: {SKILL1_KEY}=main, {SKILL2_KEY}=movement, {FLASK_KEY}=flask")
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
    
    print("\n✅ Skill cycle completed!")
    return True

if __name__ == "__main__":
    try:
        cast_skill_cycle(SKILL_CYCLE_SECONDS)
    except KeyboardInterrupt:
        print("\n\nStopped by user")
