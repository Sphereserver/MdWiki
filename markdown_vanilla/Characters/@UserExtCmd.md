## Description

This trigger fires when a player sends an extended command packet
(packet 0x12).

Fires on:

- [Players](Characters#Players "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [player](Characters#Players "wikilink") sending the command. |
| [SRC](SRC "wikilink") | The [player](Characters#Players "wikilink") sending the command. |

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
<td><p>The command type. Known commands are:</p>
<table>
<tbody>
<tr>
<td><p><strong>Command</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p>0x24</p></td>
<td><p>Use Skill macro</p></td>
</tr>
<tr>
<td><p>0x27</p></td>
<td><p>Cast spell from book</p></td>
</tr>
<tr>
<td><p>0x2F</p></td>
<td><p>Auto targeting macro</p></td>
</tr>
<tr>
<td><p>0x43</p></td>
<td><p>Open Spellbook macro</p></td>
</tr>
<tr>
<td><p>0x56</p></td>
<td><p>Cast Spell macro</p></td>
</tr>
<tr>
<td><p>0x88</p></td>
<td><p>Open Door macro</p></td>
</tr>
<tr>
<td><p>0x6B</p></td>
<td><p>God Client command</p></td>
</tr>
<tr>
<td><p>0xC7</p></td>
<td><p>Bow or Salute macro</p></td>
</tr>
<tr>
<td><p>0xF4</p></td>
<td><p>Invoke Virtue macro</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p>ARGS</p></td>
<td><p>IO</p></td>
<td><p>The command text.</p></td>
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
