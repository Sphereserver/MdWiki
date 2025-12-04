 The world is split into fixed-size sectors (by default,64x64 tiles). Environmental settings (light, weather, etc) are stored on a per-sector basis. Accessing sectors in scripts can be accomplished using the SECTOR reference from a [character](Characters "wikilink"), [item](Items "wikilink") or [map point](Map_Points "wikilink") object. The following table details the various properties of the sector object in SphereServer:

## Properties and Functions

Here is a list of all sector properties and functions. If a function is marked as readable then it can return a value when used as <KEY>. Click on the name for more detailed information such as usage and examples.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [ALLCHARS](ALLCHARS "wikilink") *command* | R | Executes *command* on all characters inside the sector. |
| [ALLCHARSIDLE](ALLCHARSIDLE "wikilink") *command* | R | Executes *command* on all disconnected characters inside the sector. |
| [ALLCLIENTS](ALLCLIENTS "wikilink") *command* | R | Executes *command* on all clients inside the sector. |
| [ALLITEMS](ALLITEMS "wikilink") *command* | R | Executes *command* on all items inside the sector. |
| [CANSLEEP](CANSLEEP "wikilink") | R | Returns 1 if the sector have all condition to sleep. (X ONLY) |
| [CLIENTS](CLIENTS "wikilink") | R | Gets the number of clients in the sector. |
| [COLDCHANCE](COLDCHANCE "wikilink") | RW | Gets or sets the chance of snow for the sector. |
| [COMPLEXITY](COMPLEXITY "wikilink") | R | Gets the number of characters in the sector. |
| [COMPLEXITY](COMPLEXITY "wikilink").HIGH | R | Returns 1 if the sector has a high complexity. (less than 5 characters) |
| [COMPLEXITY](COMPLEXITY "wikilink").MEDIUM | R | Returns 1 if the sector has a medium complexity. (less than 10 characters) |
| [COMPLEXITY](COMPLEXITY "wikilink").LOW | R | Returns 1 if the sector has a low complexity. (10+ characters) |
| [DRY](DRY "wikilink") | W | Sets the weather to dry. |
| [ISDARK](ISDARK "wikilink") | R | Returns 1 if the light level in the sector is considered to be dark. |
| [ISNIGHTTIME](ISNIGHTTIME "wikilink") | R | Returns 1 if the local time of day is between 9pm and 7am. |
| [ISSLEEPING](ISSLEEPING "wikilink") | R | Returns 1 if the sector is sleeping. (X ONLY) |
| [ITEMCOUNT](ITEMCOUNT "wikilink") | R | Returns the number of items in the sector. |
| [LIGHT](LIGHT "wikilink") | RW | Gets or sets the light level for the sector. |
| [LOCALTIME](LOCALTIME "wikilink") | R | Gets the local time of day, as a descriptive string. |
| [LOCALTOD](LOCALTOD "wikilink") | R | Gets the local time of day, in minutes. |
| [NUMBER](NUMBER "wikilink") | R | Gets the index number of the sector. |
| [RAIN](RAIN "wikilink") | W | Sets the weather to raining. |
| [RAINCHANCE](RAINCHANCE "wikilink") | RW | Gets or sets the chance of rain for the sector. |
| [RESPAWN](RESPAWN "wikilink") *ALL* | W | Resurrects dead NPC characters (not corpses). If *ALL* is provided then all sectors will be affected. |
| [RESTOCK](RESTOCK "wikilink") *ALL* | W | Restocks all NPCs in the sector. If *ALL* is provided then all sectors will be affected. |
| [SEASON](SEASON "wikilink") | RW | Gets or sets the current season in the sector. |
| [SNOW](SNOW "wikilink") | W | Sets the weather to snowing. |
| [WEATHER](WEATHER "wikilink") | RW | Gets or sets the current weather in the sector. |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Objects](Category:_Objects "wikilink")
