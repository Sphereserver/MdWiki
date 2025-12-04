## Description

This trigger fires when a player attempts to switch between war and peace mode.

Fires on:

- [Players](Characters#Players "wikilink")

## References

The following object references are explicitly available for this trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [player](Characters#Players "wikilink") changing between war and peace mode. |
| [SRC](SRC "wikilink") | The [player](Characters#Players "wikilink") changing between war and peace mode. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

| **Argument** | **In/Out** | **Description** |
| --- | --- | --- |
| ARGN1 | I | If 0, the player is entering peace mode. If 1, the player is entering war mode. |
| ARGN2 | I | If 1 will trigger skill fail for the current skill. |
| ARGN3 | I | Setting it to 1 will force a attacker's cleanup. |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                                          |
|------------------|----------------------------------------------------------|
| **Return Value** | **Description**                                          |
| 1                | Prevents the player from changing to the requested mode. |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink") [Category: Characters](Category:_Characters "wikilink") [Category: Players](Category:_Players "wikilink")
