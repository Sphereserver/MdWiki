## Description

This trigger fires when a player attempts to switch between war and
peace mode.

Fires on:

- [Players](Characters#Players "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [player](Characters#Players "wikilink") changing between war and peace mode. |
| [SRC](SRC "wikilink") | The [player](Characters#Players "wikilink") changing between war and peace mode. |

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
<td><p>If 0, the player is entering peace mode.<br />
If 1, the player is entering war mode.</p></td>
</tr>
<tr>
<td><p>ARGN2</p></td>
<td><p>I</p></td>
<td><p>If 1 will trigger skill fail for the current skill.</p></td>
</tr>
<tr>
<td><p>ARGN3</p></td>
<td><p>I</p></td>
<td><p>Setting it to 1 will force a attacker's cleanup.</p></td>
</tr>
</tbody>
</table>

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                                          |
|------------------|----------------------------------------------------------|
| **Return Value** | **Description**                                          |
| 1                | Prevents the player from changing to the requested mode. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink") [Category:
Characters](Category:_Characters "wikilink") [Category:
Players](Category:_Players "wikilink")
