## Description

This command plays a specified sound from the character to nearby clients. It accepts a sound type, not a direct sound ID.

## Ficha

|              |             |
|--------------|-------------|
| **Command**  | **BARK**    |
| **Type**     | Character   |
| **Access**   | Write       |
| **Sphere X** | Yes         |

## Syntax

`[character].BARK <sound_type>`

## Parameters

- `sound_type`: A specific sound type definition (e.g., `SOUNDACT_RAND`, `SOUNDACT_IDLE`, `SOUNDACT_NOTICE`, `SOUNDACT_HIT`, `SOUNDACT_GETHIT`, `SOUNDACT_DIE`). These are defined in scripts.

## Example

`BARK SOUNDACT_IDLE` - Plays the character's idle sound.

## Notes
- `BARK` accepts a sound *type* as a parameter, not a direct sound ID. Use the `SOUND` command for specific sound IDs.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Commands](./CategoryCommands.md)