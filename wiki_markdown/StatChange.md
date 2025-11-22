## Description

This trigger fires when a character's strength, dexterity, intelligence,
food, maxhits, maxmana or maxstam is changed.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [character](./Characters.md) whose strength, dexterity or intelligence is being changed. |
| [SRC](./SRC.md) | The [character](./Characters.md) whose strength, dexterity or intelligence is being changed. |

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
<td><p>In</p></td>
<td><p>The stat being changed.</p>
<table>
<tbody>
<tr>
<td><p><strong>Value</strong></p></td>
<td><p><strong>Stat</strong></p></td>
</tr>
<tr>
<td><p>0</p></td>
<td><p>Strength</p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>Intelligence</p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p>Dexterity</p></td>
</tr>
<tr>
<td><p>3</p></td>
<td><p>Food</p></td>
</tr>
<tr>
<td><p>4</p></td>
<td><p>MaxHits</p></td>
</tr>
<tr>
<td><p>5</p></td>
<td><p>MaxMana</p></td>
</tr>
<tr>
<td><p>6</p></td>
<td><p>MaxStam</p></td>
</tr>
<tr>
<td><p>7</p></td>
<td><p>Maxfood</p></td>
</tr>
<tr>
<td><p>8</p></td>
<td><p>Modstr</p></td>
</tr>
<tr>
<td><p>9</p></td>
<td><p>Modint</p></td>
</tr>
<tr>
<td><p>10</p></td>
<td><p>Moddex</p></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p>ARGN2</p></td>
<td><p>In</p></td>
<td><p>The current stat value.</p></td>
</tr>
<tr>
<td><p>ARGN3</p></td>
<td><p>I/O</p></td>
<td><p>The new stat value.</p></td>
</tr>
</tbody>
</table>

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Prevents the character's stat from being changed, even if argn3 has been changed. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
