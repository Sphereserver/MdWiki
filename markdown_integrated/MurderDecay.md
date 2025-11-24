## Description

This trigger fires when a character's murder count
([KILLS](./KILLS.md) property) is about to decrease.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [character](./Characters.md) whose murder count is changing. |
| [SRC](./SRC.md) | The [character](./Characters.md) whose murder count is changing. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | IO | The new murder count that will be set. |
| ARGN2 | IO | The length of time until the murder count will next decay, in tenths of a second. |

## Return Values

The following return values are explicitly defined for this trigger:

*No return values are handled by this trigger.*

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
Combat](./_Combat.md)
