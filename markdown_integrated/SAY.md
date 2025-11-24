# SAY, SAYU, SAYUA

These functions are used to make an object speak.

## Syntax

```
SAY <text>
SAYU <text>
SAYUA <hue>,<mode>,<font>,<lang>,<text>
```

## Description

- `SAY`: Makes the object speak the given text.
- `SAYU`: Makes the object speak the given text in UTF-8.
- `SAYUA`: Makes the object speak the given text in UNICODE, with the specified color, mode, font and language.

## Notes

- If a hue is not specified, `SAY` and `MESSAGE` will use `SpeechColor` or, if set, `SpeechColorOverride`.
- The `MESSAGE` command is an alias for `SAY`.

[Category: Functions](CategoryFunctions.md)
