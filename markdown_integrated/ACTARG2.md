# ACTARG2

This property holds the second argument (ARGN2) related to a character's current action or skill. Its value can be set and is often used to pass parameters to skill triggers.

## Ficha

|              |             |
|--------------|-------------|
| **Property** | **ACTARG2** |
| **Type**     | Character   |
| **Access**   | Read/Write  |
| **Sphere X** | Yes         |

## Notes
- `ACTARG2` (along with `ACTARG1` and `ACTARG3`) values are now saved only if their value is different from 0 and the character's action is a valid skill or is one of the actions that uses `ACTARG1/ACTARG2/ACTARG3` (NPCACT_FLEE, NPCACT_TALK, NPCACT_TALKFOLLOW, NPCACT_RIDDEN).
- Previous changes that zeroed `ACTARG2` at skill success, abort, or failure if `SKF_SCRIPTED` was set have been reverted. They are now zeroed only at the end of a skill (success, abort, or failure), not before `@PreStart`.

[Category: Properties](CategoryProperties.md)
