## Description

This trigger fires when a character successfully casts a spell.

Fires on:

- [Spells](SPELL "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](ARGO "wikilink") | The source of the spell. Could be the [item](Items "wikilink") used to cast the spell (e.g. a wand or scroll) or the [character](Characters "wikilink") casting the spell. |
| [I](I "wikilink") | The [character](Characters "wikilink") casting the spell. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") casting the spell. |

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
<td><p>I</p></td>
<td><p>The spell that was cast.</p></td>
</tr>
<tr>
<td><p>ARGN2</p></td>
<td><p>I</p></td>
<td><p>The strength of the spell.</p></td>
</tr>
<tr>
<td><p>LOCAL.CREATEOBJECT1</p></td>
<td><p>IO</p></td>
<td><p>For field spells, overrides the item <a href="BASEID"
title="wikilink">BASEID</a> to use for the east-west direction.</p>
<p>For summon spells, overrides the character <a href="BASEID"
title="wikilink">BASEID</a> to summon.</p></td>
</tr>
<tr>
<td><p>LOCAL.CREATEOBJECT2</p></td>
<td><p>IO</p></td>
<td><p>For field spells, overrides the item <a href="BASEID"
title="wikilink">BASEID</a> to use for the north-south
direction.</p></td>
</tr>
<tr>
<td><p>LOCAL.FIELDGAUGE</p></td>
<td><p>IO</p></td>
<td><p>For field spells, overrides the default gauge of the field
(1).</p></td>
</tr>
<tr>
<td><p>LOCAL.FIELDWIDTH</p></td>
<td><p>IO</p></td>
<td><p>For field spells, overrides the default width of the field
(5).</p></td>
</tr>
<tr>
<td><p>LOCAL.AREARADIUS</p></td>
<td><p>IO</p></td>
<td><p>For Area of effect (AoE) spells, overrides the default radius of
the effect (4).</p></td>
</tr>
<tr>
<td><p>LOCAL.EFFECTCOLOR</p></td>
<td><p>IO</p></td>
<td><p>For field spells, overrides the color of the fields.</p></td>
</tr>
<tr>
<td><p>LOCAL.DURATION</p></td>
<td><p>IO</p></td>
<td><p>Overrides the default duration of spell in tenths of second
(local.duration = 10 is 1 second).</p></td>
</tr>
<tr>
<td><p>LOCAL.DAMAGETYPE</p></td>
<td><p>IO</p></td>
<td><p>Overrides the default damage type of spell. (Check
sphere_defs.scp "dam_flags" definition for damage types)</p></td>
</tr>
</tbody>
</table>

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                           |
|------------------|---------------------------|
| **Return Value** | **Description**           |
| 1                | Aborts casting the spell. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
