\_\_FORCETOC\_\_ A spell block defines the basic properties and
behaviours of a spell.

## Properties

The following properties are available when defining a spell:

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [CAST_TIME](CAST_TIME "wikilink") | RW | Gets or sets the length of time it takes to cast the spell, in tenths of a second. Accepts multiple values to adjust based on skill level. |
| [DEFNAME](DEFNAME "wikilink") | RW | Gets or sets the spell's defname. |
| [DURATION](DURATION "wikilink") | RW | Gets or sets the duration of the spell's affect in tenths of a second, if applicable. Accepts multiple values to adjust based on skill level. |
| [EFFECT](EFFECT "wikilink") | RW | Gets or sets the strength of the spell. Accepts multiple values to adjust based on skill level. |
| [EFFECT_ID](EFFECT_ID "wikilink") | RW | Gets or sets the ID of the spell's visual effect. |
| [FLAGS](FLAGS "wikilink") | RW | Gets or sets the spell's attribute flags. |
| [GROUP](GROUP "wikilink") | RW | Gets or sets the spell's group flags. |
| [INTERRUPT](INTERRUPT "wikilink") | RW | Gets or sets the chance of a character being interrupted when hit in combat while casting the spell. Accepts multiple values to adjust based on skill level. |
| [MANAUSE](MANAUSE "wikilink") | Rw | Gets or sets the number of mana points needed to cast the spell. |
| [NAME](NAME "wikilink") | RW | Gets or sets the name of the spell. |
| [PROMPT_MSG](PROMPT_MSG "wikilink") | RW | Gets or sets the message shown when a character casts the spell, and also forces characters to select a target when non-empty. |
| [RESOURCES](RESOURCES "wikilink") | RW | Gets or sets the resources that are needed to cast the spell. |
| [RESOURCES](RESOURCES "wikilink")*.n.KEY* | R | Gets the [BASEID](BASEID "wikilink") of the nth resource needed to cast the spell. (zero-based) |
| [RESOURCES](RESOURCES "wikilink")*.n.VAL* | R | Gets the amount of the nth resource needed to cast the spell. (zero-based) |
| [RUNE_ITEM](RUNE_ITEM "wikilink") | RW | Gets or sets the [BASEID](BASEID "wikilink") of the item that should be equipped when a spell has a duration. |
| [RUNES](RUNES "wikilink") | RW | Gets or sets the spell's words of power. |
| [SCROLL_ITEM](SCROLL_ITEM "wikilink") | RW | Gets or sets the [BASEID](BASEID "wikilink") of the scroll that casts the spell. |
| [SKILLREQ](SKILLREQ "wikilink") | RW | Gets or sets a list of skills that are needed to cast the spell. |
| [SOUND](SOUND "wikilink") | RW | Gets or sets the ID of the sound that will be played when the spell is cast. |

## Triggers

The following table lists all of the triggers that can be placed under a
spell definition. All of the triggers here have an equivalent @Spell
trigger on the [character](Characters "wikilink") object.

|  |  |  |
|----|----|----|
| **Name** | **Description** | **Sphere X only?** |
| [@Effect](@Effect "wikilink") | Fires when a character or item is hit by the spell. |  |
| [@EffectAdd](@EffectAdd "wikilink") | Fires when a spell memory item is being added. |  |
| [@EffectRemove](@EffectRemove "wikilink") | Fires when a spell memory item is removed. | X |
| [@EffectTick](@EffectTick "wikilink") | Fires when a character is under effect of a periodic spell (like Poison spell). | X |
| [@Fail](@Fail_(Spell_Trigger) "wikilink") | Fires when a character fails to cast the spell. |  |
| [@Select](@Select_(Spell_Trigger) "wikilink") | Fires when a character selects to cast the spell, or when Sphere checks if a character is capable of casting it. |  |
| [@Start](@Start_(Spell_Trigger) "wikilink") | Fires when a character starts to cast the spell. |  |
| [@Success](@Success_(Spell_Trigger) "wikilink") | Fires when a character successfully casts the spell. |  |
| [@TargetCancel](@TargetCancel "wikilink") | Fires when a character cancels target selection for a spell they are casting. |  |

## Examples

<spherescript> // // Clumsy spell from the default script pack. //
\[SPELL 1\] DEFNAME=s_clumsy NAME=Clumsy SOUND=snd_SPELL_CLUMSY RUNES=UJ
CAST_TIME=1.0 RESOURCES=i_reag_blood_moss,i_reag_nightshade
RUNE_ITEM=i_rune_CLUMSY SCROLL_ITEM=i_scroll_CLUMSY
FLAGS=SPELLFLAG_TARG_CHAR \| SPELLFLAG_DIR_ANIM \| SPELLFLAG_HARM \|
SPELLFLAG_FX_TARG \| SPELLFLAG_RESIST EFFECT_ID=i_fx_curse EFFECT=3,15
DURATION=2\*60.0,3\*60.0 MANAUSE=4 SKILLREQ=MAGERY 10.0
INTERRUPT=100.0,100.0 </spherescript>

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Definitions](Category:_Definitions "wikilink")
