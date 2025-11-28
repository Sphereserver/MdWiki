## Description

This trigger fires when a character fails to cast a spell.

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](ARGO "wikilink") | The [item](Items "wikilink") used to cast the spell (e.g. a wand or scroll). |
| [I](I "wikilink") | The [character](Characters "wikilink") failing to cast the spell. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") failing to cast the spell. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                                |
|--------------|------------|--------------------------------|
| **Argument** | **In/Out** | **Description**                |
| ARGN1        | I          | The spell that was being cast. |

The following arguments are use only in the X version:

<table>
<tbody>
<tr>
<td><p><strong>Argument</strong></p></td>
<td><p><strong>In/Out</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p>ARGN2</p></td>
<td><p>IO</p></td>
<td><p>The mana loss if the spell is failed.</p></td>
</tr>
<tr>
<td><p>local.tithingloss</p></td>
<td><p>IO</p></td>
<td><p>The tithing points loss if the spell is failed.</p>
<p><code>        While both are writeable, they only works if  ManaLossFail or ReagentLossFail ( also for tithing points) are enabled in the sphere.ini</code></p></td>
</tr>
</tbody>
</table>

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Prevents normal fail behaviours (fail message, fizzle effect, reagent loss). |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
