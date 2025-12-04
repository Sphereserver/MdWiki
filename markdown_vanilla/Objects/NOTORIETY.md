## Properties and Functions

Here is a list of all notoriety properties and functions. If a function is marked as readable then it can return a value when used as <KEY>. Click on the name for more detailed information such as usage and examples. Notoriety list saved on you holds the values others can read when seeing you or retrieving any notoriety data, ie: notosave.1.value=01 and notosave.2.value=07 will make you appear as NOTO_GOOD (1) for the character in slot 1 of your list and NOTO_INVUL (7) for the character number 2 of your `list.`

|  |  |  |
|----|----|----|
| **NOTOSAVE***.key* | **Read/Write** | **Description** |
|  | R | Gets the number of characters you've sent your notoriety. |
| *n* | R | Gets the UID of the nth character for who you have stored your notoriety. (zero-based) |
| [ID](ID "wikilink") | R | Get's the id on the list for the character with the given UID. |
| *n*.[VALUE](VALUE "wikilink") | R | Get's the value of notoriety I have to send to this character. |
| *n*.[COLOR](COLOR "wikilink") | R | Get's the color of notoriety I have to send to this character. |
| *n*.[ELAPSED](ELAPSED "wikilink") | R | Get's the time elapsed since this index has been saved, when reaching ini's setting 'NotoTimeout' the notoriety for this character will be refreshed if needed. |

To reset the Notoriety list for this character use [NotoUpdate](NotoUpdate "wikilink").

## Modifying Notoriety

All Notoriety changes are made inside the [@NotoSend](@NotoSend "wikilink") trigger

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Objects](Category:_Objects "wikilink")
