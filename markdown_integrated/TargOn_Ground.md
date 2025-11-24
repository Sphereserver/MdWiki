## Description

This trigger fires when the ground is targeted with an item.

Fires on:

- [Items](./Items.md)

## References

The following object references are explicitly available for this
trigger:

<table>
<tbody>
<tr>
<td><p><strong>Name</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p><a href="I" title="wikilink">I</a></p></td>
<td><p>The <a href="Items" title="wikilink">item</a> that the target
cursor originated from.</p></td>
</tr>
<tr>
<td><p><a href="SRC" title="wikilink">SRC</a></p></td>
<td><p>The <a href="Characters#Players" title="wikilink">player</a>
targeting the ground.<br />
<strong>Note:</strong> The <a href="TARGP" title="wikilink">TARGP</a>
property on the player can be used to acquire the target
coordinates.</p></td>
</tr>
</tbody>
</table>

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                                                    |
|--------------|------------|----------------------------------------------------|
| **Argument** | **In/Out** | **Description**                                    |
| ARGN1        | I          | If a static item was targeted, the ID of the item. |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Prevents Sphere from processing the default target behaviour. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
