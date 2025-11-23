## Description

This property holds the third argument (ARGN3) related to a character's current action or skill. Its value can be set and is often used to pass parameters to skill triggers.

## Ficha

|              |             |
|--------------|-------------|
| **Property** | **ACTARG3** |
| **Type**     | Character   |
| **Access**   | Read/Write  |
| **Sphere X** | Yes         |

## Notes
- `ACTARG3` (along with `ACTARG1` and `ACTARG2`) values are now saved only if their value is different from 0 and the character's action is a valid skill or is one of the actions that uses `ACTARG1/ACTARG2/ACTARG3` (NPCACT_FLEE, NPCACT_TALK, NPCACT_TALKFOLLOW, NPCACT_RIDDEN).
- Previous changes that zeroed `ACTARG3` at skill success, abort, or failure if `SKF_SCRIPTED` was set have been reverted. They are now zeroed only at the end of a skill (success, abort, or failure), not before `@PreStart`.
- In the `@Start` trigger for Provocation, `ACTARG3` is set to 1 if the provoked character is in the same ally group as the targeted character, otherwise it's 0. This can be used to override hardcoded provocation behavior.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)