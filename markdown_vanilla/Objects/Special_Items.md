Certain types of items have extended functionality, and therefore have additional properties, functions or references to the ones already listed on the [Items](Items "wikilink") page. The following sections describe what these are.

## Multis

Multis have a TYPE `t_multi`, `t_multi_custom` or `t_ship.` These are multi-piece items that are usually stored in the client's multi.mul file, but are only considered to be one item to both the server and client (so when you approach a castle, there is a significant reductionin lag since the server doesn't have to tell the client to display thousands of wall pieces).

### Properties and Functions

Here is a list of all multi properties and functions. If a function is marked as readable then it can return a value when used as \<KEY\>. Click on the name for more detailed information such as usage and examples.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [COMPS](COMPS "wikilink") | R | Gets the number of components defined in the [ITEMDEF](ITEMDEF "wikilink"). |
| [COMP](COMP "wikilink")*.n.key* | R | Gets the KEY (ID,DX,DY,DZ,D) of the nth component defined in the [ITEMDEF](ITEMDEF "wikilink"). |
| [MULTICREATE](MULTICREATE "wikilink") *owner_uid* | W | When a multi is created via SERV.[NEWITEM](NEWITEM "wikilink"), this function must be used to initialise the multi-region. |

## Customizable Multis

Customizable multis are represented by the TYPE of `t_multi_custom.` These are designed to be used with the AOS House Designer tool that is present since the 4.0.0 series of UO clients.

### References

References return pointers to other objects (e.g. the REGION referenceallows you to access the REGION that an object is in). These can either be accessed by using *\<REFNAME\>* to return the [UID](UID "wikilink") (1 for object types that don't have UIDs) of the object or 0 if it doesn't exist, or by using *\<REFNAME.KEY\>* where KEY is a valid property/function/reference for the *REFNAME* object. Click on the name
```
for more detailed information such as usage and examples.

```
|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [DESIGNER](DESIGNER "wikilink") | R | Gets the [character](Characters "wikilink") currently modifying the house design. |
```

```
### Properties and Functions
```

Here is a list of all custom multi properties and functions. If a function is marked as readable then it can return a value when used as \<KEY\>. Click on the name for more detailed information such as usage and examples.

```
|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [ADDITEM](ADDITEM "wikilink") *item_id, dx, dy, dz* | W | Adds an item to the house design. |
| [ADDMULTI](ADDMULTI "wikilink") *multi_id, dx, dy, dz* | W | Adds a multi to the house design. |
| [CLEAR](CLEAR "wikilink") | W | Removes all items from the house design. |
| [COMMIT](COMMIT "wikilink") | W | Commits all changes that have been made to the house design, updating the state of the building. |
| [COMPS](COMPS "wikilink") | R | Gets the number of components in the house design. |
| [CUSTOMIZE](CUSTOMIZE "wikilink") *character_uid* | W | Enters the building into edit mode for the specified character (or SRC). |
| [DESIGN](DESIGN "wikilink")*.n.KEY* | R | Gets a property (ID,DX,DY,DZ,D,FIXTURE) from the nth component in the house design. |
| [EDITAREA](EDITAREA "wikilink") | R | Gets the designable area rectangle of the multi (left,top,right,bottom) |
| [ENDCUSTOMIZE](ENDCUSTOMIZE "wikilink") | W | Exits the current designer from edit mode. |
| [FIXTURES](FIXTURES "wikilink") | R | Gets the number of fixtures in the house design. |
| [REMOVEITEM](REMOVEITEM "wikilink") *item_id, dx, dy, dz* | W | Removes an item from the house design. |
| [RESET](RESET "wikilink") | W | Resets the house design back to the house foundation. |
| [RESYNC](RESYNC "wikilink") *character_uid* | W | Resends the current building state to the specified character (or SRC). |
| [REVERT](REVERT "wikilink") | W | Undoes all of the changes made to the house design since the last commit. |
| [REVISION](REVISION "wikilink") | R | Gets the revision number of the house design. |
```

```
## Ships
```

Ships have the TYPE t_ship, and are another extended version of multis that are designed to be used to sail around the world.

```
### References
```

References return pointers to other objects (e.g. the REGION referenceallows you to access the REGION that an object is in). These can either be accessed by using *\<REFNAME\>* to return the [UID](UID "wikilink") (1 for object types that don't have UIDs) of the object or 0 if it doesn't exist, or by using *\<REFNAME.KEY\>* where KEY is a valid property/function/reference for the *REFNAME* object. Click on the name for more detailed information such as usage and examples.

```
|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [HATCH](HATCH "wikilink") | R | Gets the ship's [hatch](Items "wikilink"). |
| [TILLER](TILLER "wikilink") | R | Gets the ship's [tiller](Items "wikilink"). |
| [PLANK](PLANK "wikilink")*.n* | R | Gets the nth ship [plank](Items "wikilink"). (zero-based) |
```

```
### Properties and Functions
```

Here is a list of all ship properties and functions. If a function is marked as readable then it can return a value when used as \<KEY\>. Click on the name for more detailed information such as usage and examples.

```
|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [PLANKS](PLANKS "wikilink") | R | Gets the number of planks on the ship. |
| [SHIPANCHORDROP](SHIPANCHORDROP "wikilink") | W | Drops the ship's anchor, preventing it from moving. |
| [SHIPANCHORRAISE](SHIPANCHORRAISE "wikilink") | W | Raises the ship's anchor, allowing it to move. |
| [SHIPBACK](SHIPBACK "wikilink") | W | Begins moving the ship backwards. |
| [SHIPBACKLEFT](SHIPBACKLEFT "wikilink") | W | Begins moving the ship backwards and to its left. |
| [SHIPBACKRIGHT](SHIPBACKRIGHT "wikilink") | W | Begins moving the ship backwards and to its right. |
| [SHIPDOWN](SHIPDOWN "wikilink") | W | Begins moving the ship downards, if ATTR_MAGIC is set. |
| [SHIPDRIFTLEFT](SHIPDRIFTLEFT "wikilink") | W | Begins moving the ship to its left. |
| [SHIPDRIFTRIGHT](SHIPDRIFTRIGHT "wikilink") | W | Begins moving the ship to its right. |
| [SHIPFACE](SHIPFACE "wikilink") *direction* | W | Sets the direction of the ship. |
| [SHIPFORE](SHIPFORE "wikilink") | W | Begins moving the ship forwards. |
| [SHIPFORELEFT](SHIPFORELEFT "wikilink") | W | Begins moving the ship forwards and to its left. |
| [SHIPFORERIGHT](SHIPFORERIGHT "wikilink") | W | Begins moving the ship forwards and to its right. |
| [SHIPGATE](SHIPGATE "wikilink") *location* | W | Moves the entire ship and its contents to a specified location. |
| [SHIPLAND](SHIPLAND "wikilink") | W | Moves the ship to ground level, if ATTR_MAGIC is set. |
| [SHIPMOVE](SHIPMOVE "wikilink") *direction* | W | Begins moving the ship in the specified direction. |
| [SHIPSPEED](SHIPSPEED "wikilink").TILES | R | Gets the number of tiles that ths ship moves in one step. |
| [SHIPSPEED](SHIPSPEED "wikilink").PERIOD | R | Gets the length of time between each step, in tenths of a second. |
| [SHIPSTOP](SHIPSTOP "wikilink") | W | Stops the ship. |
| [SHIPTURN](SHIPTURN "wikilink") | W | Turns the ship to face the opposite direction. |
| [SHIPTURNLEFT](SHIPTURNLEFT "wikilink") | W | Rotates the ship to its left. |
| [SHIPTURNRIGHT](SHIPTURNRIGHT "wikilink") | W | Rotates the ship to its right. |
| [SHIPUP](SHIPUP "wikilink") | W | Begins moving the ship upwards, if ATTR_MAGIC is set. |
```

```
## Maps
```

The TYPEs t_map and t_map_blank are used to represent maps. These display a map to the player when used, that can be marked with a series of pins (markers) to plot a route.

```
### Properties and Functions
```

Here is a list of all map properties and functions. If a function is marked as readable then it can return a value when used as \<KEY\>. Click on the name for more detailed information such as usage and examples.

```
| **Name** | **Read/Write** | **Description** |
| --- | --- | --- |
| [PIN](PIN)*.n* [PIN](PIN) *x, y* | RW | Gets the position of the *nth* pin (zero-based), or adds a pin to the map at the specified location. |
| [MORE1H](MORE1H),[MORE1L](MORE1L) | RW | Gets the top left coordinates (x,y) of the area displayed on t_map. |
| [MORE2H](MORE2H),[MORE2L](MORE2L) | RW | Gets the bottom right coordinates (x,y) of the area displayed on t_map. |
```

```
## Messages / Books
```

Messages (t_message) and books (t_book) possess a range of properties and functions that are used to store their title, author and body text.

```
### Properties and Functions
```

Here is a list of all message properties and functions. If a function is marked as readable then it can return a value when used as \<KEY\>. Click on the name for more detailed information such as usage and examples.

```
|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [AUTHOR](AUTHOR "wikilink") | RW | Gets or sets the author of the message. |
| [BODY](BODY "wikilink")*.n* | RW | Gets the nth line of text from the message, or appends a new line of text to the message. |
| [ERASE](ERASE "wikilink") *page_num* | W | Removes all lines of text from the message, or if a page number (one-based) if supplied erases just a single line. |
| [PAGE](PAGE "wikilink")*.n* | W | Sets the text of the nth single line of the message. (zero-based) |
| [PAGES](PAGES "wikilink") | R | Gets the number of lines of text in the message. |
| [TITLE](TITLE "wikilink") | RW | Gets or sets the title of message. |
```

```
## Communication Crystals
```

Communication crystals have the TYPE of t_comm_crystal.

```
### Properties and Functions
```

Here is a list of all communication crystal properties and functions. If a function is marked as readable then it can return a value when used as \<KEY\>. Click on the name for more detailed information such as usage and examples.

```
|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [SPEECH](SPEECH "wikilink") *-/+speech_defname* | RW | Gets a list of attached SPEECH blocks, or adds to or removes from the attached speech.. |
```

```
## Guild/Town Stones
```

Guild and Town stones are defined by the types t_stone_guild and t_stone_town. Whilst a lot of functionality has been moved into the script pack, there are still some special properties, functions and references that can be used.

```
### References
```

References return pointers to other objects (e.g. the REGION referenceallows you to access the REGION that an object is in). These can either be accessed by using *\<REFNAME\>* to return the [UID](UID "wikilink") (1 for object types that don't have UIDs) of the object or 0 if it doesn't exist, or by using *\<REFNAME.KEY\>* where KEY is a valid property/function/reference for the *REFNAME* object. Click on the name for more detailed information such as usage and examples.

```
|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [GUILD](GUILD "wikilink")''.n | R | Gets the nth linked [guild or town](#Guild.2FTown_Members "wikilink"). (zero-based) |
| [GUILDFROMUID](GUILDFROMUID "wikilink")''stone_uid | R | Gets the linked [guild or town](#Guild.2FTown_Members "wikilink") with a specified UID. |
| [MEMBER](MEMBER "wikilink")''.n | R | Gets the nth member of the [guild or town](#Guild.2FTown_Members "wikilink"). (zero-based) |
| [MEMBERFROMUID](MEMBERFROMUID "wikilink").''character_uid | R | Gets the [member](#Guild.2FTown_Members "wikilink") of the guild with a specified UID. |
```

```
### Properties and Functions
```

Here is a list of all guild/town stone properties and functions. If a function is marked as readable then it can return a value when used as \<KEY\>. Click on the name for more detailed information such as usage and examples.

```
|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [ABBREV](ABBREV "wikilink") | RW | Gets or sets the guild/town abbreviation. |
| [ABBREVIATIONTOGGLE](ABBREVIATIONTOGGLE "wikilink") | R | Returns one of the *STONECONFIG_VARIOUSNAME\_\** defnames depending on whether SRC has their abbreviation showing or not. |
| [ALIGN](ALIGN "wikilink") | RW | Gets or sets the alignment of the guild/town. |
| [ALIGNTYPE](ALIGNTYPE "wikilink") | R | Returns the name of the guild or town's alignment. |
| [ALLGUILDS](ALLGUILDS "wikilink") *flags, command* | W | Performs the given comamnd on all linked guilds or towns based on flags. (0 = All, 1 = War Declared by 'Us' only, 2 = War Declared by 'Them' only, 3 = War Declayed by both) |
| [ALLMEMBERS](ALLMEMBERS "wikilink") *priv, command* | W | Performs the given command on all guild or town members with the specified privelege level. (-1 = All) |
| [APPLYTOJOIN](APPLYTOJOIN "wikilink") *character_uid* | W | Adds a character as a candidate to the guild or town. |
| [CHANGEALIGN](CHANGEALIGN "wikilink") *alignment* | W | Changes the guild or town alignment. |
| [DECLAREPEACE](DECLAREPEACE "wikilink") *stone_uid* | W | Declares peace towards another guild or town. |
| [DECLAREWAR](DECLAREWAR "wikilink") *stone_uid* | W | Declares war towards another guild or town. |
| [ELECTMASTER](ELECTMASTER "wikilink") | W | Selects a new guild or town master based on which member has the most votes. |
| [GUILD](GUILD "wikilink").COUNT | R | Gets the number linked guilds or towns. |
| [INVITEWAR](INVITEWAR "wikilink") *stone_uid, who_declared* | W | Invites another guild or town to go to war (*who_declared*, 0 = They declared, 1 = We declared) |
| [JOINASMEMBER](JOINASMEMBER "wikilink") *character_uid* | W | Adds a character as a full member of the guild or town. |
| [LOYALTO](LOYALTO "wikilink") | R | Returns the name of the guild or town member that SRC has declared fealty to. |
| [MASTER](MASTER "wikilink") | R | Returns the name of the guild or town master. |
| [MASTERGENDERTITLE](MASTERGENDERTITLE "wikilink") | R | Returns the gender of the guild or town mastser. |
| [MASTERTITLE](MASTERTITLE "wikilink") | R | Returns the title of the guild or town master. |
| [MASTERUID](MASTERUID "wikilink") | RW | Gets the UID of the guild/town master, or sets it to the UID of a new master. |
| [MEMBER](MEMBER "wikilink").COUNT *priv* | R | Gets the number of members in the guild/town with at least the given privileges (or all if not supplied). |
| [RESIGN](RESIGN "wikilink") *character_uid* | W | Removes a character from the guild or town. |
| [TOGGLEABBREVIATION](TOGGLEABBREVIATION "wikilink") *character_uid* | W | Toggles the display of guild/town abbreviation for a member or SRC. |
| [WEBPAGE](WEBPAGE "wikilink") | RW | Gets or sets the guild or town's webpage. |
| [CHARTER](CHARTER "wikilink")*.n* | EW | Gets or sets the nth line of the guild/town charter. (zero-based) |
```

```
## Guild/Town Members
```

When accessing a member of a guild or town via the [MEMBER](MEMBER "wikilink").x,r [MEMBERFROMUID](MEMBERFROMUID "wikilink").uid, [GUILD](GUILD "wikilink").x, or [GUILDFROMUID](GUILDFROMUID "wikilink").uid references, you access a special "Guild/Town Member" object which has specific properties, references and functions available. If you attempt to access something that doesn't exist in any of the following tables then the command is 'redirected' to the actual character or item the member object is linked to (so something like *\<MEMBER.x.STR\>* would work because the STRproperty exists on the [character](Characters "wikilink")).

```
### Properties and Functions
```

Here is a list of all guild/town member properties and functions. If a function is marked as readable then it can return a value when used as \<KEY\>. Click on the name for more detailed information such as usage and examples.

```
#### Character Members
```

```
|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [ACCOUNTGOLD](ACCOUNTGOLD "wikilink") | RW | Gets or sets the amount of gold the member has in their guild/town account. |
| [ISCANDIDATE](ISCANDIDATE "wikilink") | R | Returns 1 if the member is a candidate of the guild/town. |
| [ISMASTER](ISMASTER "wikilink") | R | Returns 1 if the member is a guild/town master. |
| [LOYALTO](LOYALTO "wikilink") | RW | Gets or sets the UID of who the member has declared fealty towards. |
| [PRIV](PRIV "wikilink") | RW | Gets or sets the member's privilege level within the guild/town. |
| [PRIVNAME](PRIVNAME "wikilink") | R | Returns the name of the member's privilege level within the guild/town. |
| [TITLE](TITLE "wikilink") | RW | Gets or sets the member's title within the guild/town. |
| [SHOWABBREV](SHOWABBREV "wikilink") | RW | Gets or sets whether or not the member's abbreviation is shown. |
```

```
#### Item Members
```

```
|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [ISENEMY](ISENEMY "wikilink") | R | Returns 1 if the other guild/town is considered an enemy. |
| [THEYALLIANCE](THEYALLIANCE "wikilink") | RW | Gets or sets whether or not the other guild/town has declared an alliance with the guild/town. |
| [THEYWAR](THEYWAR "wikilink") | RW | Gets or sets whether or not the other guild/town has declared war. |
| [WEALLIANCE](WEALLIANCE "wikilink") | RW | Gets or sets whether or not the guild/town has declared an alliance with the other guild/town. |
| [WEWAR](WEWAR "wikilink") | RW | Gets or sets whether or not the guild/town has declared war with the other guild/town. |
```

```
## Containers
```

Container items (backpacks, bankboxes, bags, etc) can be used to hold other items. These items have the [TYPE](TYPE "wikilink") of t_container.

```
### References
```

References return pointers to other objects (e.g. the REGION referenceallows you to access the REGION that an object is in). These can either be accessed by using *\<REFNAME\>* to return the [UID](UID "wikilink") (1 for object types that don't have UIDs) of the object or 0 if it doesn't exist, or by using *\<REFNAME.KEY\>* where KEY is a valid property/function/reference for the *REFNAME* object. Click on the name for more detailed information such as usage and examples.

```
|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [FINDCONT](FINDCONT "wikilink")*.n* | R | Gets the nth [item](Items "wikilink") from inside the container. (zero-based) |
| [FINDID](FINDID "wikilink")*.item_id* | R | Gets the first [item](Items "wikilink") found inside the container with the matching [BASEID](BASEID "wikilink"). |
| [FINDTYPE](FINDTYPE "wikilink")*.type* | R | Gets the first [item](Items "wikilink") found inside the container with the matching [TYPE](TYPE "wikilink"). |
```

```
### Properties and Functions
```

Here is a list of all custom multi properties and functions. If a function is marked as readable then it can return a value when used as \<KEY\>. Click on the name for more detailed information such as usage and examples.

```
|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [COUNT](COUNT "wikilink") | R | Returns the number of items inside the container. |
| [DELETE](DELETE "wikilink") *nth* | W | Deletes the nth item from inside the container. (1-based) |
| [EMPTY](EMPTY "wikilink") | W | Deletes all items inside the container. |
| [FCOUNT](FCOUNT "wikilink") | R | Returns the total number of items inside the container, including subcontainers. |
| [FIXWEIGHT](FIXWEIGHT "wikilink") | W | Recalculates the total weight of the container and its contained items. |
| [OPEN](OPEN "wikilink") | W | Opens the container, for SRC to view its contents. |
| [RESCOUNT](RESCOUNT "wikilink") *item_defname* | R | Returns the total amount of a specific item inside the container, including subcontainers. |
| [RESTEST](RESTEST "wikilink") *item_list* | R | Returns 1 if all of the items in the list can be found inside the container, including subcontainers. |
```

```
## Vendable Items
```

When an item has value, either explicitly in the ITEMDEF's [VALUE](VALUE "wikilink") property or implicity in the ITEMDEF's [RESOURCES](RESOURCES "wikilink") property, it is considered a "Vendable Item" that can be sold on vendors.

```
### Properties and Functions
```

Here is a list of all vendable item properties and functions. If a function is marked as readable then it can return a value when used as \<KEY\>. Click on the name for more detailed information such as usage and examples.

```
|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [PRICE](PRICE "wikilink") | RW | Gets or sets the price of the item. (affect only the sell/buy price on player vendor. NPC use the value) |
| [QUALITY](QUALITY "wikilink") | RW | Gets or sets the quality of the item. |
```

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Objects](Category:_Objects "wikilink")
```
