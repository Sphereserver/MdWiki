## Description

This tag allows overriding the moverate checks for NPCs, setting the next movement to a specified timer in milliseconds.

## Ficha

|              |                          |
|--------------|--------------------------|
| **Tag**      | **tag.override.movedelay** |
| **Type**     | NPC                      |
| **Access**   | Read/Write               |
| **Sphere X** | Yes                      |

## Usage

`tag.override.movedelay = <milliseconds>`

## Notes
- Example: `tag.override.movedelay=250` makes the NPC move every 250 milliseconds when walking.
- The final value (with or without tags, running or walking) cannot be lower than 1 tenth of a second or higher than 5 seconds.
- This is the walking speed; running speed and walking speed while mounted is half (125ms using the example), running while mounted is 4 times faster (62.5ms, defaulted to 100ms).
- This tag completely overrides default moverate checks; `TAG.OVERRIDE.MOVERATE` is ignored.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Tags](./CategoryTags.md)