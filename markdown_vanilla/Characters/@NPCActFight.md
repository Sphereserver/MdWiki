## Description

This trigger fires periodically whilst an NPC is fighting.

Fires on:

- [NPCs](Characters#NPCs "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [NPC](Characters#NPCs "wikilink") who is fighting. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") the NPC is fighting with. |

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
<td><p>The distance between the NPC and its target.</p></td>
</tr>
<tr>
<td><p>ARGN2</p></td>
<td><p>IO</p></td>
<td><p>The NPC's motivation level to fight.<br />
<strong>Note:</strong> NPCs, excluding pets, with a motivation less than
zero will flee from their target.</p></td>
</tr>
<tr>
<td><p>local.Skill</p></td>
<td><p>O</p></td>
<td><p>Force the NPC to stop current checks and start this
skill.</p></td>
</tr>
<tr>
<td><p>local.Spell</p></td>
<td><p>O</p></td>
<td><p>Force to cast an specific spell in case LOCAL.SKILL is set to a
SKF_MAGIC skill.</p></td>
</tr>
</tbody>
</table>

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 0 | Allows the NPC to fight, but skips making a decision to use a special action such as fire breathing or rock throwing. |
| 1 | Stops the NPC from taking any action. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink") [Category:
Characters](Category:_Characters "wikilink") [Category:
NPCS](Category:_NPCS "wikilink")
