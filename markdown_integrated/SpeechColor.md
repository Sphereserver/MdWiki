## Description

This property controls the speech color of NPCs and reflects the last speech hue sent by the client for players.

## Ficha

|              |             |
|--------------|-------------|
| **Property** | **SpeechColor** |
| **Type**     | Character   |
| **Access**   | Read/Write (NPCs) / Read-only (Players) |
| **Sphere X** | Yes         |

## Notes
- For NPCs, this property gets or sets their speech hue. A value of `946` (or `0x382`), which is the default gray hue for NPC speech, disables the override.
- For players, this property is read-only and contains the last speech hue sent by the client.
- When a hue is not specified for `SAY` and `MSG` commands, `SpeechColor` will be used (or `SpeechColorOverride` if set).
- On Enhanced Clients, NPC speech color was previously always yellow. A workaround forces system (0) talkmode instead of say (3) for Enhanced Clients, which requires `SAY_DEF_UNICODE` to be set to `1` in `sphere_msgs.scp` for Unicode speech packets.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)