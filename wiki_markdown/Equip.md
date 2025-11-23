## Description

This trigger fires when an item is equipped.

Fires on:

- [Items](./Items.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [item](./Items.md) being equipped. |
| [SRC](./SRC.md) | The [character](./Characters.md) equipping the item. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

*No arguments are set for this trigger.*

## Return Values

The following return values are explicitly defined for this trigger:

<table>
<tbody>
<tr>
<td><p><strong>Return Value</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>Treats the item as failed to equip.<br />
<strong>Note:</strong> This trigger is not reliable for blocking the
equipping of an item. Use the <a href="@EquipTest"
title="wikilink">@EquipTest</a> trigger instead which is designed for
blocking the equip action.</p></td>
</tr>
</tbody>
</table>

## Notes
- When a player attempts to equip non-equippable items, they are now bounced to the pack.

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
