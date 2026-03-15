#!/usr/bin/env python3
import sys
import pyautogui

def main():
    if len(sys.argv) < 5:
        print("Usage: python mouse_drag.py <start_x> <start_y> <end_x> <end_y>")
        sys.exit(1)
    
    start_x = int(sys.argv[1])
    start_y = int(sys.argv[2])
    end_x = int(sys.argv[3])
    end_y = int(sys.argv[4])
    
    pyautogui.dragTo(start_x, start_y, end_x, end_y)
    print(f"Dragged from ({start_x}, {start_y}) to ({end_x}, {end_y})")

if __name__ == "__main__":
    main()
