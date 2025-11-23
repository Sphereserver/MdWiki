## Description

This property overrides the default speech color for a character. It can be used on both players and NPCs.

## Ficha

|              |                               |
|--------------|-------------------------------|
| **Property** | **SpeechColorOverride**       |
| **Type**     | Player, NPC                   |
| **Access**   | Read/Write                    |
| **Sphere X** | Yes                           |

## Notes
- If a hue is not specified in a SAY or MSG command, the value of this property will be used. If this property is not set, SpeechColor will be used instead.
- This property now works for both NPCs and Clients.
- A value of `0` (instead of `52`), which is the new default, disables the override.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)