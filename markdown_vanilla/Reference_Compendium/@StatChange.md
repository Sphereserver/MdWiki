## Description

This trigger fires when a character's strength, dexterity, intelligence, food, maxhits, maxmana or maxstam is changed.

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
| ------------ | ------------ | ----------------------------------------- | -------- |
| ARGN1 | In | The stat being changed. <table> **Value** | **Stat** |
| 0 | Strength |  |  |
| 1 | Intelligence |  |  |
| 2 | Dexterity |  |  |
| 3 | Food |  |  |
| 4 | MaxHits |  |  |
| 5 | MaxMana |  |  |
| 6 | MaxStam |  |  |
| 7 | Maxfood |  |  |
| 8 | Modstr |  |  |
| 9 | Modint |  |  |
| 10 | Moddex |  |  |
|  |  |  |  |</td>
</tr> <tr> <td><p>ARGN2</p></td> <td><p>In</p></td> <td><p>The current stat value.</p></td> </tr> <tr> <td><p>ARGN3</p></td> <td><p>I/O</p></td> <td><p>The new stat value.</p></td> </tr> </tbody> </table>

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Prevents the character's stat from being changed, even if argn3 has been changed. |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink")
