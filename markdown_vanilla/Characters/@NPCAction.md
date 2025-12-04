## Description

This trigger fires when an NPC is making a decision to perform an AI action.

The revision notes for this trigger say "This trigger will fire only if EF_NPCAct_Triggers is set and EF_Minimize_Triggers is NOT set in the sphere.ini file...", however in more recent versions this trigger may be controlled by the NPC_AI_EXTRA setting.

AI-related trigger. If the situation is such that the NPC will do something due to it's AI - things like animals pooping the ground, vendors going off/on duty, (un)equipping a lightsource when it's dark, (un)equipping a weapon when fighting, stabler feeding animals or giving players food for their animals etc... this trigger will be fired.

On `RETURN`0 the NPC will continue with what it wants to do, `RETURN`1 will abort it.

Fires on:

- [NPCs](Characters#NPCs "wikilink")

## References

The following object references are explicitly available for this trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [NPC](Characters#NPCs "wikilink") performing the action. |
| [SRC](SRC "wikilink") | The [NPC](Characters#NPCs "wikilink") performing the action. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

*No arguments are set for this trigger.*

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                                |
|------------------|------------------------------------------------|
| **Return Value** | **Description**                                |
| 1                | Prevents any hardcoded AI action taking place. |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink") [Category: Characters](Category:_Characters "wikilink") [Category: NPCS](Category:_NPCS "wikilink")
