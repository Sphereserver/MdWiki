## Description

This trigger is used in skills definitions (a related[@SkillWait](@SkillWait "wikilink") exists for characters). This trigger is called whenever Sphere wants to check if a character must wait before starting a skill. Normally this will be when a skill is selected from the skill menu (before [@Select](@Select "wikilink")), but also when snooping a container or using a musical instrument.

Fires on:

- [Skills](SKILL "wikilink")

## References

The following object references are explicitly available for this trigger **(this needs to be tested/validated)**:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [character](Characters "wikilink") selecting the skill. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") selecting the skill. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behavior **(this needs to be tested/validated)**:

|              |            |                                        |
|--------------|------------|----------------------------------------|
| **Argument** | **In/Out** | **Description**                        |
| ARGN1        | ?          | The skill the character is attempting  |
| ARGN2        | ?          | the skill that is currently being used |

## Return Values

The following return values are explicitly defined for this trigger **(this needs to be tested/validated)**:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 0 | The character can start the other skill (bypasses default checks) |
| 1 | The character must wait (bypasses default checks) |
| 2 | Perform default checks |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink")
