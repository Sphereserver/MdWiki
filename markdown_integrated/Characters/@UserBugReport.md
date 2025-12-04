## Description

This trigger fires when a player submits a bug report.

Fires on:

- [Players](Characters#Players "wikilink")

## References

The following object references are explicitly available for this trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [player](Characters#Players "wikilink") submitting the report. |
| [SRC](SRC "wikilink") | The [player](Characters#Players "wikilink") submitting the report. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

| **Argument** | **In/Out** | **Description** |  |
| --- | --- | --- | --- |
| ARGN1 | I | The report category code. Expected codes are: <table> **Code** | **Meaning** |
| 1 | Environment |  |  |
| 2 | Wearables |  |  |
| 3 | Combat |  |  |
| 4 | UI |  |  |
| 5 | Crash |  |  |
| 6 | Stuck |  |  |
| 7 | Animations |  |  |
| 8 | Performance |  |  |
| 9 | NPCs |  |  |
| 10 | Creatures |  |  |
| 11 | Pets |  |  |
| 12 | Housing |  |  |
| 13 | Lost Item |  |  |
| 14 | Exploit |  |  |
| 15 | Other |  |  |</td>
</tr> <tr> <td><p>ARGS</p></td> <td><p>I</p></td> <td><p>The report text.</p></td> </tr> <tr> <td><p>LOCAL.LANG</p></td> <td><p>I</p></td> <td><p>The language the report was submitted in.</p></td> </tr> </tbody> </table>

## Return Values

The following return values are explicitly defined for this trigger:

*No return values are handled this trigger.*

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink") [Category: Characters](Category:_Characters "wikilink") [Category: Players](Category:_Players "wikilink")
