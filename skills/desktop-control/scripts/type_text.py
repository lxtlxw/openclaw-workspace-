#!/usr/bin/env python3
import sys
import pyautogui

def main():
    if len(sys.argv) < 2:
        print("Usage: python type_text.py \"text-to-type\"")
        sys.exit(1)
    
    text = sys.argv[1]
    pyautogui.write(text)
    print(f"Typed: {text}")

if __name__ == "__main__":
    main()
