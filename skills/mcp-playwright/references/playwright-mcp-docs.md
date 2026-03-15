# Playwright MCP 官方文档整理

## Repository

GitHub: https://github.com/microsoft/playwright-mcp

## Features

- **AI-driven browser interaction**: AI can navigate, click, type, fill forms just like a human
- **Accessibility-first**: Uses Playwright's accessibility tree to give AI a semantic view of the page
- **Works with all modern browsers**: Chromium, Firefox, WebKit
- **Headless/headed modes**: Can run headless for automation or headed for debugging
- **Multi-tab support**: Full management of browser tabs

## Available Tools

### `navigate`
Navigate to a URL.
Parameters:
```json
{
  "url": "string"
}
```

### `click`
Click an element by its accessibility role and name.
Parameters:
```json
{
  "role": "string",
  "name": "string"
}
```

### `type`
Type text into an input element.
Parameters:
```json
{
  "role": "string",
  "name": "string",
  "text": "string"
}
```

### `screenshot`
Take a screenshot of the current page or element.
Parameters:
```json
{
  "fullPage": "boolean (default: true)"
}
```
Returns: PNG image as base64.

### `snapshot`
Get the accessibility snapshot of the current page.
Returns: Formatted accessibility tree with roles and names.

### `newTab`
Open a new browser tab.
Returns: New tab ID.

### `switchTab`
Switch to an existing tab.
Parameters:
```json
{
  "tabId": "string"
}
```

### `closeTab`
Close the current tab.

### `goBack`
Go back in history.

### `goForward`
Go forward in history.

### `reload`
Reload the current page.

### `close`
Close the browser.

## Running

```bash
# Run directly with npx
npx @playwright/mcp

# Installed globally
playwright-mcp
```

## Environment Variables

- `PLAYWRIGHT_HEADED` - Run in headed mode (show browser window)
- `PLAYWRIGHT_SLOW_MO` - Slow down operations by X milliseconds
- `PLAYWRIGHT_DEVICE` - Emulate a specific device (e.g. "iPhone 15")

## Best Practices

1. **Always get a snapshot after navigation** to understand the current page state
2. **Use accessibility roles and names** to locate elements - more reliable than CSS selectors for AI
3. **Take screenshots** to verify the result visually
4. **Use headed mode for debugging** to see what the AI is doing
