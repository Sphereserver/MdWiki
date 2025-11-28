## Description

This trigger fires when a player attempts to invoke a virtue by using a
macro.

Fires on:

- [Players](Characters#Players "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](ARGO "wikilink") | The [player](Characters#Players "wikilink") invoking the virtue. |
| [I](I "wikilink") | The [player](Characters#Players "wikilink") invoking the virtue. |
| [SRC](SRC "wikilink") | The [player](Characters#Players "wikilink") invoking the virtue. |

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
<td><p>The virtue being invoked. Known values are:</p>
<table>
<tbody>
<tr>
<td><p><strong>Value</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>Honor</p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p>Sacrifice</p></td>
</tr>
<tr>
<td><p>3</p></td>
<td><p>Valor</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

## Return Values

The following return values are explicitly defined for this trigger:

*No return values are handled for this trigger.*

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink") [Category:
Characters](Category:_Characters "wikilink") [Category:
Players](Category:_Players "wikilink")
