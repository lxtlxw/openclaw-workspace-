# Desktop Control Installation Guide

## Windows

```powershell
# Install dependencies
pip install pyautogui pillow opencv-python

# If you get error about cv2, try:
pip install --upgrade opencv-python
```

## macOS

```bash
pip3 install pyautogui pillow opencv-python

# For macOS permissions:
# You may need to enable accessibility permissions for Terminal/IDE in System Preferences → Security & Privacy → Accessibility
```

## Linux

```bash
pip3 install python3-xlib pyautogui pillow opencv-python
sudo apt-get install python3-tk python3-dev
```

## Verify Installation

```bash
python -c "import pyautogui; print('PyAutoGUI version:', pyautogui.__version__); print('Screen size:', pyautogui.size())"
```

Should output something like:
```
PyAutoGUI version: 0.9.54
Screen size: (1920, 1080)
```

## Troubleshooting

### ImportError: No module named 'pyautogui'
- Make sure you installed with the correct pip
- Check which Python you are using: `which python`

### Image matching not working
- Check that the template image matches what's on screen
- Try lowering the confidence threshold (e.g., from 0.8 to 0.7)
- Make sure the template image doesn't have extra padding/transparency

### Mouse moving too fast
- The default speed is okay, you can add `time.sleep()` between actions
- Adjust `pyautogui.PAUSE` to add more pause between actions
