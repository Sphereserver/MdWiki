## Description

This trigger fires when a character is going to regenerate any stat
(Hits,Mana,Stam or Food).

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
<td><p>local.StatID</p></td>
<td><p>I/O</p></td>
<td><p>The stat being changed.</p>
<table>
<tbody>
<tr>
<td><p><strong>Value</strong></p></td>
<td><p><strong>Stat</strong></p></td>
</tr>
<tr>
<td><p>0</p></td>
<td><p>Hits</p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>Mana</p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p>Stam</p></td>
</tr>
<tr>
<td><p>3</p></td>
<td><p>Food</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p>local.Value</p></td>
<td><p>I/O</p></td>
<td><p>The amount of points being regenerated (or decreased in food's
case).</p></td>
</tr>
<tr>
<td><p>local.StatLimit</p></td>
<td><p>I/O</p></td>
<td><p>by default=<MaxStat>, allow this stat to pass the limit when
regenerating, or limit it lower.</p></td>
</tr>
</tbody>
</table>

## Aditional Notes

Stat regens checks now work on a tenth-second basis instead of a second basis.

Mounted characters now receive stat regens. To prevent this, add an event with `ON=@RegenStat return 1` when mounting them.

`RegenHitsD`, `RegenManaD`, `RegenStamD`, and `RegenFoodD` are new properties that accept values in tenths of seconds.

local.Value: It can be set to negative values, 0 will stop any default
action like return 1. By default its set to RegenValStatID (ie:
RegenValHits)

Local.StatLimit: Stats over this value will go down in each tick until
they reach their limit. This does not work with food as food shouldn't
ignore its limit (0).

RegenStat is checked before this trigger but it can be changed inside so
the next time the trigger will be fired will correspond to this value,
setting it to high values is the only way to simulate a regeneration
stop.

You can see your current points in the current stat using
\<local.StatLimit\> as it retrieve (before you modify it) the current
stat value.

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                               |
|------------------|-------------------------------|
| **Return Value** | **Description**               |
| 1                | Prevents the process to ocur. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)