## Description

This trigger fires when someone is being deleted from my attacker list.

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

|                       |                                           |
|-----------------------|-------------------------------------------|
| **Name**              | **Description**                           |
| [I](I "wikilink")     | Myself.                                   |
| [SRC](SRC "wikilink") | The character being removed from my list. |

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
<td><p>Shows if the deletion was forced by your scripts (1) or called by
Sphere (0)</p></td>
</tr>
<tr>
<td><p>ARGN2</p></td>
<td><p>I</p></td>
<td><table>
<tbody>
<tr>
<td><p><strong>Type description</strong></p></td>
<td><p><strong>Values</strong></p></td>
</tr>
<tr>
<td><p>Forced (Blocked attack, default uncategorized
actions...)</p></td>
<td><p>0</p></td>
</tr>
<tr>
<td><p>Max fight time has reached (Elapsed)</p></td>
<td><p>1</p></td>
</tr>
<tr>
<td><p>Distance/LOS</p></td>
<td><p>2</p></td>
</tr>
<tr>
<td><p>The character is no longer existing</p></td>
<td><p>3</p></td>
</tr>
<tr>
<td><p>Forced via attacker.delete methods (ingame/script)</p></td>
<td><p>4</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Prevents src of leaving my list, however I'll try to delete him as soon as possible. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink") [Category:
Characters](Category:_Characters "wikilink") [Category:
Combat](Category:_Combat "wikilink")
