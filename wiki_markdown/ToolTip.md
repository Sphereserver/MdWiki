## Description

This trigger fires when a client requests old-style tooltips for an
object.

Fires on:

- [Characters](./Characters.md)
- [Items](./Items.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [character](./Characters.md) or [item](./Items.md) whose tooltip is being requested. |
| [SRC](./SRC.md) | The [client](./CharactersClients.md) requesting the tooltip. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

*No arguments are set for this trigger.*

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                        |
|------------------|----------------------------------------|
| **Return Value** | **Description**                        |
| 1                | Prevents the tooltip from being shown. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
