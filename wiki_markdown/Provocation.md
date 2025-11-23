## Description

The Provocation skill allows a character to provoke creatures into attacking each other.

## Ficha

|              |             |
|--------------|-------------|
| **Skill**    | **Provocation** |
| **Sphere X** | Yes         |

## Notes
- If `ACTARG1` is set to the UID of an instrument, that instrument's sound will be played when using this skill.
- The `TAG.BARDING.DIFF` tag can be used to determine the difficulty of this skill. If not set, the old behavior is used.
- NPC ally groups have been updated, affecting hostility calculations and this skill.
- In the `@Start` trigger, `ACTARG3` is set to 1 if the provoked character is in the same ally group as the targeted character, otherwise it's 0. This allows scripting to always permit provocation by setting `ACTARG3=0`.
- The `PROVOCATION_KIND` defmessage is now shown if the skill is aborted due to characters being in the same ally group.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Skills](./CategorySkills.md)