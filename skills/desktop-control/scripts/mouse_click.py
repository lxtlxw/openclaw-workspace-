#!/usr/bin/env python3
import sys
import pyautogui

def main():
    if len(sys.argv) < 3:
        print("Usage: python mouse_click.py <x> <y> [button]")
        print("button: left (default), right, middle")
        sys.exit(1)
    
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    button = sys.argv[3] if len(sys.argv) > 3 else "left"
    
    pyautogui.click(x=x, y=y, button=button)
    print(f"Clicked {button} at ({x}, {y})")

if __name__ == "__main__":
    main()
