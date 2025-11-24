# SYSMESSAGEUA

The `SYSMESSAGEUA` function is used to display a Unicode system message to a client. It provides detailed control over the message's appearance and content.

## Syntax

`SYSMESSAGEUA hue, font, mode, language, text`

## Parameters

- `hue`: The color of the message.
- `font`: The font ID of the message.
- `mode`: The message mode (e.g., `TALKMODE_SYSTEM` for system messages).
- `language`: The language ID for the message.
- `text`: The Unicode message string.

## Notes

-   This function now returns an error if the number of arguments provided is insufficient, enforcing stricter usage.

[Category: Functions](./CategoryFunctions.md)