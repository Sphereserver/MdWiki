## Description

This trigger fires when a character hits an item with a spell. The item
may have been targeted directly or it may have been hit by an
area-effect spell.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ACT](./ACT.md) | The [item](./Items.md) being hit by the spell. |
| [ARGO](./ARGO.md) | The [item](./Items.md) used to cast the spell (e.g. a wand or scroll). |
| [I](./I.md) | The [character](./Characters.md) responsible for the spell. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

<table>
<tbody>
<tr>
<td><p><strong>Argument</strong></p></td>
<td><p><strong>In/Out</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p>ARGN1</p></td>
<td><p>IO</p></td>
<td><p>The number of the spell that has hit the object.</p></td>
</tr>
<tr>
<td><p>ARGN2</p></td>
<td><p>IO</p></td>
<td><p>The strength of the spell.</p></td>
</tr>
<tr>
<td><p>ARGN3</p></td>
<td><p>IO</p></td>
<td><p>A multiplier for the spell's duration or effect.<br />
<strong>Note:</strong> Only used when a character is hit by a
spell.</p></td>
</tr>
</tbody>
</table>

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                                     |
|------------------|-----------------------------------------------------|
| **Return Value** | **Description**                                     |
| 1                | Prevents the item from being affected by the spell. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
