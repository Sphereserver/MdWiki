## Description

This trigger fires periodically whilst an NPC is fighting.

Fires on:

- [NPCs](Characters#NPCs "wikilink")

## References

The following object references are explicitly available for this trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [NPC](Characters#NPCs "wikilink") who is fighting. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") the NPC is fighting with. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

| **Argument** | **In/Out** | **Description** |
| --- | --- | --- |
| ARGN1 | IO | The distance between the NPC and its target. |
| ARGN2 | IO | The NPC's motivation level to fight. **Note:** NPCs, excluding pets, with a motivation less than zero will flee from their target. |
| local.Skill | O | Force the NPC to stop current checks and start this skill. |
| local.Spell | O | Force to cast an specific spell in case LOCAL.SKILL is set to a SKF_MAGIC skill. |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 0 | Allows the NPC to fight, but skips making a decision to use a special action such as fire breathing or rock throwing. |
| 1 | Stops the NPC from taking any action. |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink") [Category: Characters](Category:_Characters "wikilink") [Category: NPCS](Category:_NPCS "wikilink")
