## Description

X branch only. This trigger is called each step an NPC does while
wandering.

Fires on:

- [NPCs](Characters#NPCs "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [NPC](Characters#NPCs "wikilink") performing the action. |
| [SRC](SRC "wikilink") | The [NPC](Characters#NPCs "wikilink") performing the action. |

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
<td><p>0 if it will continue to wander, 1 if randomly deciding to stop,
2 if deciding to stop because</p>
<p><code>   after looking around it found something interesting.</code></p></td>
</tr>
<tr>
<td><p>ARGN2</p></td>
<td><p>IO</p></td>
<td><p>1 if it's returning to home, 0 otherwise.</p></td>
</tr>
</tbody>
</table>

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | stops decisions for this step, so it will not return to home, do another step or stop wandering (again, for this step). |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink") [Category:
Characters](Category:_Characters "wikilink") [Category:
NPCS](Category:_NPCS "wikilink")
