#!/usr/bin/env python3
import sys
import pyautogui
import cv2
import numpy as np
from PIL import Image

def main():
    if len(sys.argv) < 2:
        print("Usage: python image_click.py template.png [confidence]")
        print("confidence: 0-1, default 0.8")
        sys.exit(1)
    
    template_path = sys.argv[1]
    confidence = float(sys.argv[2]) if len(sys.argv) > 2 else 0.8
    
    # Read template
    template = cv2.imread(template_path)
    if template is None:
        print(f"Error: Could not read template image from {template_path}")
        sys.exit(1)
    
    # Take screenshot
    screenshot = pyautogui.screenshot()
    screen_np = np.array(screenshot)
    screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
    
    # Match template
    result = cv2.matchTemplate(screen_bgr, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    if max_val < confidence:
        print(f"No match found with confidence >= {confidence}")
        print(f"Best match confidence: {max_val:.3f}")
        sys.exit(1)
    
    # Calculate center point
    h, w = template.shape[:2]
    center_x = max_loc[0] + w // 2
    center_y = max_loc[1] + h // 2
    
    # Click
    pyautogui.click(center_x, center_y)
    print(f"Found match with confidence {max_val:.3f}")
    print(f"Clicked at ({center_x}, {center_y})")

if __name__ == "__main__":
    main()
