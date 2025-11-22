## Description

This trigger fires when a character selects to cast a spell. It fires
multiple times during the different stages of a spell being cast.

Fires on:

- [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](./ARGO.md) | The source of the spell. Could be the [item](./Items.md) used to cast the spell (e.g. a wand or scroll) or the [character](./Characters.md) casting the spell. |
| [I](./I.md) | The [character](./Characters.md) casting the spell. |
| [SRC](./SRC.md) | The [character](./Characters.md) casting the spell. |

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
<td><p>The spell being cast.</p></td>
</tr>
<tr>
<td><p>ARGN2</p></td>
<td><p>IO</p></td>
<td><p>The amount of mana needed to cast the spell.</p></td>
</tr>
<tr>
<td><p>ARGN3</p></td>
<td><p>I</p></td>
<td><p>Flags representing what stage of the casting process the trigger
is being used at.</p>
<table>
<tbody>
<tr>
<td><p><strong>Flag</strong></p></td>
<td><p><strong>Meaning</strong></p></td>
</tr>
<tr>
<td><p>01</p></td>
<td><p>Just a test (no reagents or mana will be consumed)</p></td>
</tr>
<tr>
<td><p>02</p></td>
<td><p>Display fail message if unable to cast</p></td>
</tr>
</tbody>
</table>
<table>
<tbody>
<tr>
<td><p><strong>Spell Casting Stage</strong></p></td>
<td><p><strong>Expected Flags</strong></p></td>
</tr>
<tr>
<td><p>Spell selected for casting</p></td>
<td><p>01</p></td>
</tr>
<tr>
<td><p>Spell is about to start casting</p></td>
<td><p>03</p></td>
</tr>
<tr>
<td><p>Spell is about to finish casting</p></td>
<td><p>03</p></td>
</tr>
<tr>
<td><p>Spell casting finished successfully</p></td>
<td><p>02</p></td>
</tr>
<tr>
<td><p>Spell casting finished unsuccessfully</p></td>
<td><p>00</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                     |
|------------------|-------------------------------------|
| **Return Value** | **Description**                     |
| 1                | Prevents the spell from being cast. |
| 6                | Allows the spell to be cast.        |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
