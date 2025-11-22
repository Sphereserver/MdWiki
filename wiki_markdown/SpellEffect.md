## Description

This trigger fires when an object is hit by the effects of a spell. The
object may have been targeted directly or it may have been hit by an
area-effect spell.

Fires on:

- [Characters](./Characters.md)
- [Items](./Items.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](./ARGO.md) | The [item](./Items.md) used to cast the spell (e.g. a wand or scroll). |
| [I](./I.md) | The [character](./Characters.md) or [item](./Items.md) being hit by the spell. |
| [SRC](./SRC.md) | The [character](./Characters.md) responsible for the spell. |

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
<td><p>The number of the spell that has hit the object.</p></td>
</tr>
<tr>
<td><p>ARGN2</p></td>
<td><p>IO</p></td>
<td><p>The strength of the spell.</p></td>
</tr>
<tr>
<td><p>ARGN3</p></td>
<td><p>IO</p></td>
<td><p>A multiplier for the spell's duration or effect.<br />
<strong>Note:</strong> Only used when a character is hit by a
spell.</p></td>
</tr>
<tr>
<td><p>LOCAL.DamageType</p></td>
<td><p>IO</p></td>
<td><p>Can be used to override the damage flags for spells that have
SPELLFLAG_DAMAGE. The value can be a bitmask of dam_* flags. For
example, to change the s_magic_arrow SPELL definition to cause physical
and magic damage:</p>
<p><code>ON=@Effect</code><br />
<code>  LOCAL.DAMAGETYPE=(&lt;DEF.dam_physical&gt;|&lt;DEF.dam_magic&gt;)</code></p></td>
</tr>
<tr>
<td><p>LOCAL.AreaRadius</p></td>
<td><p>IO</p></td>
<td><p>Can be used to override the default radius (which is 5) for
spells that have SPELLFLAG_AREA.</p></td>
</tr>
<tr>
<td><p>Local.CreateObject1</p></td>
<td><p>IO</p></td>
<td><p>Changes the ID of the effect for this spell, IE:
Local.CreateObject1=0eed in FlameStrike spell will change the Fire
Column for a Gold Coin.</p></td>
</tr>
<tr>
<td><p>local.EffectColor</p></td>
<td><p>IO</p></td>
<td><p>Changes the color of the effect for this spell.</p></td>
</tr>
<tr>
<td><p>local.EffectRender</p></td>
<td><p>IO</p></td>
<td><p>Changes the Render Mode for this spell's effect.</p></td>
</tr>
<tr>
<td><p>local.EffectExplode</p></td>
<td><p>IO</p></td>
<td><p>Sets wether the effect should explode or not after reaching the
target.</p></td>
</tr>
<tr>
<td><p>local.Resist</p></td>
<td><p>IO</p></td>
<td><p>Changes the default behavior on Magic Resistance (being
local.resist 100 the same as resisting 100%. [Effect = Effect *
Local.resist/100])</p></td>
</tr>
</tbody>
</table>

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 0 | For scripted spells, prevents any hardcoded behaviour from taking place. |
| 1 | Prevents the object from being affected by the spell. |

**Note:** For the recall and gate travel spells, returning 0 prevents
the spell from proceeding and returning 1 has no effect.

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
