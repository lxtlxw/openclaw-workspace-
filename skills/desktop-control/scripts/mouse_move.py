#!/usr/bin/env python3
import sys
import pyautogui

def main():
    if len(sys.argv) < 3:
        print("Usage: python mouse_move.py <x> <y>")
        sys.exit(1)
    
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    
    pyautogui.moveTo(x, y)
    print(f"Moved mouse to ({x}, {y})")

if __name__ == "__main__":
    main()
