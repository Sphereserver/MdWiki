# BARK

This function plays the specified sound (or the character's generic sound if not specified) to nearby clients from this character.

## Ficha

|              |             |
|--------------|-------------|
| **Function** | **BARK**    |
| **Type**     | Character   |
| **Access**   | Write       |
| **Sphere X** | Yes         |

## Syntax

`[char].BARK [sound_id]`

## Notes
- `BARK` accepts a sound type as a parameter, not a sound ID (use `SOUND` for sound IDs).
- New sound types (`SOUNDACT_RAND`, `SOUNDACT_IDLE`, `SOUNDACT_NOTICE`, `SOUNDACT_HIT`, `SOUNDACT_GETHIT`, `SOUNDACT_DIE`) are available for use with `BARK`.

[Category: Functions](CategoryFunctions.md)
