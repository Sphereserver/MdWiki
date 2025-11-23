## Description

This trigger fires when tooltips for an item are about to be sent to a
client. Due to recent changes, tooltips are now cached on the item. This means the [ADDCLILOC](./ADDCLILOC.md) function needs to be called directly on the item (e.g., using `ACT.ADDCLILOC`), rather than on the player.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ACT](./ACT.md) | The [item](./Items.md) whose tooltips are to be sent. |
| [I](./I.md) | The [client](./CharactersClients.md) who is receiving tooltips. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

*No arguments are set for this trigger.*

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                                |
|------------------|------------------------------------------------|
| **Return Value** | **Description**                                |
| 1                | Prevents Sphere from sending its own tooltips. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
