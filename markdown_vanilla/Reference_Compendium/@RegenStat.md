## Description

This trigger fires when a character is going to regenerate any stat (Hits,Mana,Stam or Food).

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [character](Characters "wikilink") whose strength, dexterity or intelligence is being changed. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") whose strength, dexterity or intelligence is being changed. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

| **Argument** | **In/Out** | **Description** |  |
| ------------ | ---------- | ----------------------------------------- | -------- |
| local.StatID | I/O | The stat being changed. <table> **Value** | **Stat** |
| 0 | Hits |  |  |
| 1 | Mana |  |  |
| 2 | Stam |  |  |
| 3 | Food |  |  |</td>
</tr> <tr> <td><p>local.Value</p></td> <td><p>I/O</p></td> <td><p>The amount of points being regenerated (or decreased in food'scase).</p></td> </tr> <tr> <td><p>local.StatLimit</p></td> <td><p>I/O</p></td> <td><p>by default=<MaxStat>, allow this stat to pass the limit when regenerating, or limit it lower.</p></td> </tr> </tbody> </table>

## Aditional Notes

local.Value: It can be set to negative values, 0 will stop any default action like `RETURN`1. By default its set to RegenValStatID (ie:RegenValHits)

Local.StatLimit: Stats over this value will go down in each tick until they reach their limit. This does not work with food as food shouldn't ignore its limit (0).

RegenStat is checked before this trigger but it can be changed inside so the next time the trigger will be fired will correspond to this value, setting it to high values is the only way to simulate a regeneration stop.

You can see your current points in the current stat using \<local.StatLimit\> as it retrieve (before you modify it) the current stat value.

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                               |
|------------------|-------------------------------|
| **Return Value** | **Description**               |
| 1                | Prevents the process to ocur. |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink")
