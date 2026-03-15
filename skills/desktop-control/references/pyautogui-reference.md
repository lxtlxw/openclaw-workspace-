# PyAutoGUI Key Names Reference

## Common Key Names

### Alphabet keys:
`a, b, c, ..., z, A, B, C, ..., Z

### Number keys:
`0, 1, 2, ..., 9

### Function keys:
`f1, f2, f3, ..., f12

### Special keys:
`enter, return, esc, escape, space, tab, backspace, delete, insert,
home, end, pageup, pagedown, up, down, left, right,
shift, ctrl, alt, win, command, option`

### Arrow keys:
`up, down, left, right`

### Numpad keys:
`num0, num1, ..., num9, numenter`

### Modifier combinations:
`ctrl+c, ctrl+v, ctrl+x, ctrl+a, ctrl+s, ctrl+z, ctrl+alt+delete`

## Mouse Buttons

- `left` - Left mouse button (default)
- `right` - Right mouse button
- `middle` - Middle mouse button

## Coordinate System

- Origin (0, 0) is top-left corner of screen
- X increases to the right
- Y increases downward
- Get screen size: `pyautogui.size()`

## Safety Features

- PyAutoGUI has 0.1 second pause after each action by default
- You can adjust with `pyautogui.PAUSE = 0.1`
- Moving mouse to (0, 0) aborts the program (fail-safe)
