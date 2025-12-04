## Description

This trigger fires when a character successfully casts a spell.

Fires on:

- [Spells](SPELL "wikilink")

## References

The following object references are explicitly available for this trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](ARGO "wikilink") | The source of the spell. Could be the [item](Items "wikilink") used to cast the spell (e.g. a wand or scroll) or the [character](Characters "wikilink") casting the spell. |
| [I](I "wikilink") | The [character](Characters "wikilink") casting the spell. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") casting the spell. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

| **Argument** | **In/Out** | **Description** |
| --- | --- | --- |
| ARGN1 | I | The spell that was cast. |
| ARGN2 | I | The strength of the spell. |
| LOCAL.CREATEOBJECT1 | IO | For field spells, overrides the item [BASEID](BASEID) to use for the east-west direction. For summon spells, overrides the character [BASEID](BASEID) to summon. |
| LOCAL.CREATEOBJECT2 | IO | For field spells, overrides the item [BASEID](BASEID) to use for the north-south direction. |
| LOCAL.FIELDGAUGE | IO | For field spells, overrides the default gauge of the field (1). |
| LOCAL.FIELDWIDTH | IO | For field spells, overrides the default width of the field (5). |
| LOCAL.AREARADIUS | IO | For Area of effect (AoE) spells, overrides the default radius of the effect (4). |
| LOCAL.EFFECTCOLOR | IO | For field spells, overrides the color of the fields. |
| LOCAL.DURATION | IO | Overrides the default duration of spell in tenths of second (local.duration = 10 is 1 second). |
| LOCAL.DAMAGETYPE | IO | Overrides the default damage type of spell. (Check sphere_defs.scp "dam_flags" definition for damage types) |

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                           |
|------------------|---------------------------|
| **Return Value** | **Description**           |
| 1                | Aborts casting the spell. |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink")
