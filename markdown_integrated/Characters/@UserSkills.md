## Description

This trigger fires when a skill update is sent to a client. This
normally fires when the player accesses their skill menu, or when they
receive a skill gain. It can also fire when the [INFO](INFO "wikilink")
command is used.

Fires on:

- [Clients](Characters#Clients "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [client](Characters#Clients "wikilink") receiving the skill update. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") whose skill(s) they are receiving. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | I | The skill number they are receiving an update for. (-1 = All skills) |
| ARGN2 | I | If 1, then the skills update is being sent due to the [INFO](INFO "wikilink") command being used. |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                             |
|------------------|---------------------------------------------|
| **Return Value** | **Description**                             |
| 1                | Prevents the skills update from being sent. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink") [Category:
Characters](Category:_Characters "wikilink") [Category:
Players](Category:_Players "wikilink")
