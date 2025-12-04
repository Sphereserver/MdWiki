## Description

This trigger fires when a client attempts to access the virtue dialog
```
for a character, or double clicks a virtue icon on the dialog.

Fires on:

- [Clients](Characters#Clients "wikilink")

```
## References
```

The following object references are explicitly available for this trigger:

```
|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](ARGO "wikilink") | The [character](Characters "wikilink") whose virtue dialog is being requested. |
| [I](I "wikilink") | The [client](Characters#Clients "wikilink") attempting to access or use the virtue dialog. |
| [SRC](SRC "wikilink") | The [client](Characters#Clients "wikilink") attempting to access or use the virtue dialog. |
```

```
## Arguments
```

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

```
| **Argument** | **In/Out** | **Description** |  |
| --- | --- | --- | --- |
| ARGN1 | I | The action that the client is attempting. Known values are: <table> **Action** | **Description** |
| 1 | Requesting [ARGO](ARGO)'s virtue dialog. |  |  |
| 105 | Compassion button double clicked. |  |  |
| 106 | Honesty button double clicked. |  |  |
| 107 | Honoe button double clicked. |  |  |
| 108 | Humility button double clicked. |  |  |
| 109 | Justice button double clicked. |  |  |
| 110 | Sacrifice button double clicked. |  |  |
| 111 | Spirituality button double clicked. |  |  |
| 112 | Virtue button double clicked. |  |  |</td>
```
</tr> </tbody> </table>

```
## Return Values
```

The following return values are explicitly defined for this trigger:

*No return values are handled for this trigger.*

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink") [Category: Characters](Category:_Characters "wikilink") [Category: Players](Category:_Players "wikilink")
```
