# SkillAdjusted

This command returns the skill value adjusted by stat bonuses (BONUS_STR, BONUS_DEX, BONUS_INT, BONUS_STATS). This adjusted value is used by Sphere for calculating the chance of success for non-combat skills and ResistingSpells.

## Ficha

|              |                   |
|--------------|-------------------|
| **Command**  | **SkillAdjusted** |
| **Type**     | Character         |
| **Access**   | Read              |
| **Sphere X** | Yes               |

## Syntax

`SkillAdjusted.skillnumber` or `SkillAdjusted.skillkey`

## Examples

- `SkillAdjusted.1`
- `SkillAdjusted.Anatomy`

## Notes

- The adjusted skill value is visible in the Skill Menu when the "Show Real" option is turned OFF.
- This command provides a direct way to access the correct chance of success in scripts without complex calculations.

[Category: Commands](CategoryCommands.md)
