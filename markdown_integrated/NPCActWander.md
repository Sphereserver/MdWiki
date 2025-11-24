## Description

This trigger is called each step an NPC takes while wandering. It allows for advanced control over the NPC's wandering behavior.

## Ficha

|              |             |
|--------------|-------------|
| **Trigger**  | **@NPCActWander** |
| **Fires on** | Characters  |
| **Sphere X** | Yes         |

## Arguments

- `ARGN1`:
    - `0`: NPC will continue to wander.
    - `1`: NPC is randomly deciding to stop.
    - `2`: NPC is deciding to stop because it found something interesting.
- `ARGN2`:
    - `1`: NPC is returning to its home.
    - `0`: Otherwise.

## Return Values

- `RETURN 1`: Stops decisions for this step, preventing the NPC from returning home, taking another step, or stopping wandering (for this step).

## Notes
- NPCs now perform AI checks ("look around") when wandering, which can cause the `@NpcLookAtChar` trigger to fire more frequently.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Triggers](./CategoryTriggers.md)