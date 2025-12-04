## Description

This trigger fires when a character selects to cast a spell. It fires multiple times during the different stages of a spell being cast.

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

| **Argument** | **In/Out** | **Description** |  |
| --- | --- | --- | --- |
| ARGN1 | IO | The spell being cast. |  |
| ARGN2 | IO | The amount of mana needed to cast the spell. |  |
| ARGN3 | I | Flags representing what stage of the casting process the trigger is being used at. <table> **Flag** | **Meaning** |
| 01 | Just a test (no reagents or mana will be consumed) |  |  |
| 02 | Display fail message if unable to cast |  |  |
| **Spell Casting Stage** | **Expected Flags** |
| ------------------------------------- | ------------------ |
| Spell selected for casting | 01 |
| Spell is about to start casting | 03 |
| Spell is about to finish casting | 03 |
| Spell casting finished successfully | 02 |
| Spell casting finished unsuccessfully | 00 |</td>
</tr> </tbody> </table>

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 0 | Allows the spell to be cast. |
| 1 | Prevents the spell from being cast. |
| 6 | Allows the spell to be cast without checking mana, spellbook, and reagent(s). |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink")
