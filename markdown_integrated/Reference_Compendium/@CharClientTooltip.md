## Description

This trigger fires when a client requests tooltips for another character. the [ADDCLILOC](ADDCLILOC "wikilink") function can be called on the [I](I "wikilink") object to send custom tooltips to the client.

Fires on:

- [Clients](Characters#Clients "wikilink")

## References

The following object references are explicitly available for this trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ACT](ACT "wikilink") | The [character](Characters "wikilink") whose tooltips are to be sent. |
| [I](I "wikilink") | The [client](Characters#Clients "wikilink") who is receiving tooltips. |
| [SRC](SRC "wikilink") | The [character](Characters "wikilink") whose tooltips are to be sent. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

*No arguments are set for this trigger.*

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                                |
|------------------|------------------------------------------------|
| **Return Value** | **Description**                                |
| 1                | Prevents Sphere from sending its own tooltips. |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink")
