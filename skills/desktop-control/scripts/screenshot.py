#!/usr/bin/env python3
import sys
import pyautogui

def main():
    output_path = sys.argv[1] if len(sys.argv) > 1 else "screenshot.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(output_path)
    print(f"Screenshot saved to: {output_path}")
    w, h = pyautogui.size()
    print(f"Screen size: {w}x{h}")

if __name__ == "__main__":
    main()
