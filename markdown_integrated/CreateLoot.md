## Description

This trigger fires when an NPC dies, specifically if it is allowed to have loot (i.e., not a player, not conjured, and without the `DEATHF_NOLOOT` flag). The main advantage of using this trigger is that items are created only when needed, reducing save file sizes and preventing GMs from seeing potential drops prematurely.

## Ficha

|              |                    |
|--------------|--------------------|
| **Trigger**  | **@CreateLoot**    |
| **Fires on** | NPCs (on death)    |
| **Sphere X** | Yes                |

## Notes
- This trigger is an alternative to `@NPCRestock` and `@Create` for loot generation.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Triggers](./CategoryTriggers.md)