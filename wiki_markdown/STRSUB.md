# STRSUB

The `STRSUB` function extracts a portion of a string. It takes a source string, a starting index, and an ending index, and returns the substring between these points. The function supports negative values for `end_index` to specify positions relative to the end of the string.

## Syntax

`STRSUB(source_string, start_index, end_index)`

- `source_string`: The original string from which to extract a substring.
- `start_index`: The starting position (0-based) for the substring.
- `end_index`: The ending position (0-based, exclusive) for the substring. A value of -1 or omission typically indicates to extract until the end of the `source_string`.

[Category: Functions](./CategoryFunctions.md)