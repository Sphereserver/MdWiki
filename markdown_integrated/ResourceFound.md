## Description

This trigger fires when a resource is being created.

Fires on:

- [Region Resources](./REGIONRESOURCE.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](./ARGO.md) | The [worldgem bit](./Items.md) that represents the resource in the world. |
| [I](./I.md) | The [region resource](./REGIONRESOURCE.md) being gathered. |
| [SRC](./SRC.md) | The [character](./Characters.md) gathering the resource. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

*No arguments are set for this trigger.*

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Sets the amount of resource to zero, preventing it from being gathered. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
