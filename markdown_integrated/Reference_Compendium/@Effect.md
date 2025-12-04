## Description

This trigger fires when an object is hit by the effects of a spell. The object may have been targeted directly or it may have been hit by an area-effect spell.

Fires on:

- [Spells](SPELL "wikilink")

## References

The following object references are explicitly available for this trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](ARGO "wikilink") | The [item](Items "wikilink") used to cast the spell (e.g. a wand or scroll). |
| [I](I "wikilink") | The [character](Characters "wikilink") or [item](Items "wikilink") being hit by the spell. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") responsible for the spell. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

| **Argument** | **In/Out** | **Description** |
| --- | --- | --- |
| ARGN1 | IO | The number of the spell that has hit the object. |
| ARGN2 | IO | The strength of the spell. |
| ARGN3 | IO | A multiplier for the spell's duration or effect. **Note:** Only used when a character is hit by a spell. |
| Local.CreateObject1 | IO | Changes the ID of the effect for this spell, IE: Local.CreateObject1=0eed in FlameStrike spell will change the Fire Column for a Gold Coin. |
| local.Duration | IO | Overrides the default duration of spell in tenths of second (local.duration = 10 is 1 second). |
| local.Effect | IO | Changes the EFFECT value of the spell (For changing EFFECT_ID see Local.CreateObject1). |
| local.EffectColor | IO | Changes the color of the effect for this spell. |
| local.EffectRender | IO | Changes the Render Mode for this spell's effect. |
| local.EffectExplode | IO | Sets wether the effect should explode or not after reaching the target. |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 0 | For scripted spells, prevents any hardcoded behaviour from taking place. |
| 1 | Prevents the object from being affected by the spell. |

**Note:** For the recall and gate travel spells, returning 0 prevents the spell from proceeding and returning 1 has no effect.

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink")
