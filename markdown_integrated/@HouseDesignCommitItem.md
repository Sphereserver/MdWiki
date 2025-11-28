## Description

X branch only. This trigger fires when an item is about to commit when
using house designer.

Fires on:

- [Items](Items "wikilink")

## References

The following object references are explicitly available for this
trigger:

|                   |                                              |
|-------------------|----------------------------------------------|
| **Name**          | **Description**                              |
| [I](I "wikilink") | The [item](Items "wikilink") being commited. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| local.id | I | ID of the item |
| local.p.x | I | The x location of the item |
| local.p.y | I | The y location of the item |
| local.p.z | I | The z location of the item |
| local.visible | I | 0 or 1 (non-visible items are things like doors and signs) return false will remove this item from the commit. If not return false a local.MaxZ will check the P.Z value of the item and update it if it's higher than the old one. |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                        |
|------------------|----------------------------------------|
| **Return Value** | **Description**                        |
| 1                | Prevents the item from being commited. |
