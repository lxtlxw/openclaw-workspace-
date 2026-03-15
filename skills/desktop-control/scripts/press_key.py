#!/usr/bin/env python3
import sys
import pyautogui

def main():
    if len(sys.argv) < 2:
        print("Usage: python press_key.py \"key-name\"")
        print("Examples: \"enter\", \"esc\", \"ctrl+c\", \"win+r\"")
        sys.exit(1)
    
    key = sys.argv[1]
    # Handle combinations like "ctrl+c"
    keys = key.split('+')
    if len(keys) > 1:
        pyautogui.hotkey(*keys)
        print(f"Pressed hotkey: {key}")
    else:
        pyautogui.press(key)
        print(f"Pressed key: {key}")

if __name__ == "__main__":
    main()
