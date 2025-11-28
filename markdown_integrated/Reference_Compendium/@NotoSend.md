## Description

This trigger fires when a character's notoriety is being sent on a
packet update (its fired a lot of times, keep it light and clean of
code).

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [character](Characters "wikilink") whose noto is changing. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") retrieving this character's Notoriety. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | IO | The notoriety value. By default it's limited from 1 to 7, but this limitation is no longer enforced, allowing for custom notoriety values. |
| ARGN2 | IO | The color sent in the character's packet (what is seen in status bar, character's hover, etc). |

Notes:

`-`*`The default colors are listed above but you can set any color (note that the colors are not the same as for items/chars from hues.mul).`*  
`-`*`Modifying the argn1 value will stop default behaviours checks and make the function 'NotoGetFlag' to return this value.`*

## Notoriety Values

These are the default Notoriety Values (also listed in sphere.ini).

|               |        |                        |
|---------------|--------|------------------------|
| **Name**      | **ID** | **Description**        |
| NotoGood      | 1      | Blue character.        |
| NotoGuildSame | 2      | Green character (Ally) |
| NotoNeutral   | 3      | grey (can be attacked) |
| NotoCriminal  | 4      | grey (criminal)        |
| NotoGuildWar  | 5      | orange (enemy guild)   |
| NotoEvil      | 6      | red                    |
| NotoInvul     | 7      | yellow                 |

## Return Values

*This trigger doesn't have return values, notoriety something that must
always be sent.*

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
