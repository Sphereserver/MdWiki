## Description

This command returns the skill value adjusted by relevant stat bonuses (BONUS_STR, BONUS_DEX, BONUS_INT, BONUS_STATS). This adjusted value is used internally by Sphere for calculating the chance of success for non-combat skills (including ResistingSpells).

## Ficha

|              |             |
|--------------|-------------|
| **Command**  | **SkillAdjusted** |
| **Type**     | Character Skill |
| **Access**   | Read        |
| **Sphere X** | Yes         |

## Syntax

`<SkillAdjusted.skillnumber>`
`<SkillAdjusted.skillkey>`

## Parameters

- `skillnumber`: The numerical ID of the skill.
- `skillkey`: The DEFNAME of the skill (e.g., `Anatomy`).

## Example

`SYSMESSAGE <SkillAdjusted.Anatomy>`
`SYSMESSAGE <SkillAdjusted.1>` (if skill ID 1 is Anatomy)

## Notes
- Stat bonuses (`BONUS_STR`, `BONUS_DEX`, `BONUS_INT`, `BONUS_STATS`) are defined in `sphere_skills.scp`.
- This command provides a direct way to retrieve the adjusted skill value, which previously required complex script calculations.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Skills](./CategorySkills.md)