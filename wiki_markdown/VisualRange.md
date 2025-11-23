## Description

This property controls the sight range of a character, determining how far they can see in the game world.

## Ficha

|              |                 |
|--------------|-----------------|
| **Property** | **VisualRange** |
| **Type**     | Character       |
| **Access**   | Read/Write      |
| **Sphere X** | Yes             |

## Notes
- The maximum value for `VisualRange` is now 24 for Classic Clients 7.0.55.27+ and Enhanced Clients. Prior client versions support a maximum of 18.
- `DistanceTalk`, `DistanceWhisper`, and `DistanceYell` INI settings can now use a value of 0, meaning the sound will be heard if the distance from the source is less than or equal to the listener's `VisualRange`.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)