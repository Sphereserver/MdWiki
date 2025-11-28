## Description

This trigger fires when a player presses a button on a Kingdom Reborn
toolbar.

Fires on:

- [Players](Characters#Players "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [player](Characters#Players "wikilink") pressing the button. |
| [SRC](SRC "wikilink") | The [player](Characters#Players "wikilink") pressing the button. |

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
<td><p>The button command type. Known values are:</p>
<table>
<tbody>
<tr>
<td><p><strong>Type</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>Cast spell</p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p>Weapon ability</p></td>
</tr>
<tr>
<td><p>3</p></td>
<td><p>Use skill</p></td>
</tr>
<tr>
<td><p>4</p></td>
<td><p>Use item</p></td>
</tr>
<tr>
<td><p>5</p></td>
<td><p>Scroll</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p>ARGN2</p></td>
<td><p>I</p></td>
<td><p>The button's command parameter.</p></td>
</tr>
</tbody>
</table>

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                              |
|------------------|----------------------------------------------|
| **Return Value** | **Description**                              |
| 1                | Prevents Sphere from processing the command. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink") [Category:
Characters](Category:_Characters "wikilink") [Category:
Players](Category:_Players "wikilink")
