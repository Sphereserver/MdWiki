## Description

This trigger fires when tooltips are about to be sent to a client. the [ADDCLILOC](ADDCLILOC "wikilink") function can be called on the [SRC](SRC "wikilink") object to send custom tooltips to the client.

Fires on:

- [Characters](Characters "wikilink")
- [Items](Items "wikilink")

## References

The following object references are explicitly available for this trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](I "wikilink") | The [character](Characters "wikilink") or [item](Items "wikilink") whose tooltips are to be sent. |
| [SRC](SRC "wikilink") | The [client](Characters#Clients "wikilink") who is receiving tooltips. |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

*No arguments are set for this trigger.*

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                                |
|------------------|------------------------------------------------|
| **Return Value** | **Description**                                |
| 1                | Prevents Sphere from sending its own tooltips. |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink") [Category: Characters](Category:_Characters "wikilink") [Category: Items](Category:_Items "wikilink")
