 Clients are able to form parties with each other by using the `/add` command. When in a party, the party object can be referenced by using **PARTY.KEY** from the [client](Characters#Clients "wikilink") object. The following tables detail the various properties of parties in SphereServer:

## References

References return pointers to other objects (e.g. the CHAR.n referenceallows you to access the characters that are attached to the account). These can either be accessed by using *\<REFNAME\>* to return the [UID](UID "wikilink") (1 for object types that don't have UIDs) of the object or 0 if it doesn't exist, or by using *\<REFNAME.KEY\>* where KEY is a valid property/function/reference for the *REFNAME* object. Click on the name for more detailed information such as usage and examples.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [MASTER](MASTER "wikilink") | R | Gets the party master, the [character](Characters "wikilink") who originally formed the party. |
| [MEMBER](MEMBER "wikilink")*.n* | R | Gets the nth [party member](Characters "wikilink"). (zero-based) |

## Properties and Functions

Here is a list of all party properties and functions. If a function is marked as readable then it can return a value when used as <KEY>. Click on the name for more detailed information such as usage and examples.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [ADDMEMBER](ADDMEMBER "wikilink") *character_uid* | W | Adds a character to the party. |
| [ADDMEMBERFORCED](ADDMEMBERFORCED "wikilink") *character_uid* | W | Adds a character to the party. If the character is already in a party then they will be forced out of it. The character will be added even if the party has reached the maximum size of 10. |
| [CLEARTAGS](CLEARTAGS "wikilink") | W | Removes all TAGs from the party. |
| [DISBAND](DISBAND "wikilink") | W | Disbands the party. |
| [ISSAMEPARTYOF](ISSAMEPARTYOF "wikilink") *character_uid* | R | Returns 1 if a specified character is a member of this party. |
| [MEMBERS](MEMBERS "wikilink") | R | Gets the total number of characters in the party. |
| [REMOVEMEMBER](REMOVEMEMBER "wikilink") *character_uid* | W | Removes a character from the party. |
| [REMOVEMEMBER](REMOVEMEMBER "wikilink") @*n* | W | Removes the nth character from the party. (zero-based) |
| [SPEECHFILTER](SPEECHFILTER "wikilink") | RW | Gets or sets a function that will be called every time a party member speaks to the party. |
| [SYSMESSAGE](SYSMESSAGE "wikilink") *character_uid, message* | W | Sends a message to a party member (0 = Entire party). |
| [SYSMESSAGE](SYSMESSAGE "wikilink") @*n, message* | W | Sends a message to the nth party member. |
| [TAG](TAG "wikilink") | RW | Gets or sets the value of a TAG. |
| [TAGAT](TAGAT "wikilink")*.index* | R | Gets a TAG at the given zero-based index. |
| [TAGAT](TAGAT "wikilink")*.index*.KEY | R | Gets the name of the TAG at the given zero-based index. |
| [TAGAT](TAGAT "wikilink")*.index*.VAL | R | Gets the value of the TAG at the given zero-based index. |
| [TAGCOUNT](TAGCOUNT "wikilink") | R | Gets the number of TAGs stored on the party. |
| [TAGLIST](TAGLIST "wikilink") | W | Displays a list of all TAGs to SRC. |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Objects](Category:_Objects "wikilink")
