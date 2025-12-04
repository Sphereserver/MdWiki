 A character can be either a player or an NPC.

## References

References return pointers to other objects (e.g. the REGION referenceallows you to access the REGION that an object is in). These can either be accessed by using *\<REFNAME\>* to return the [UID](UID "wikilink") (1 for object types that don't have UIDs) of the object or 0 if it doesn't exist, or by using *\<REFNAME.KEY\>* where KEY is a valid property/function/reference for the *REFNAME* object. Click on the name
```
for more detailed information such as usage and examples.

```
|  |  |  |  |
|----|----|----|----|
| **Name** | **Read/Write** | **Description** | **Sphere X only?** |
| [ACCOUNT](Accounts "wikilink") | RW | Gets or sets the [account](Accounts "wikilink") that the character belongs to. |  |
| [ACT](ACT "wikilink") | RW | Gets or sets the [character](Characters "wikilink") or [item](Items "wikilink") that is related to the action the character is performing. |  |
| [FINDCONT](FINDCONT "wikilink")*.n* | R | Gets the nth [item](Items "wikilink") equipped to the character. (zero-based) |  |
| [FINDID](FINDID "wikilink")*.item_id* | R | Gets the first [item](Items "wikilink") found equipped to the character or inside their backpack, with the matching [BASEID](BASEID "wikilink"). |  |
| [FINDLAYER](FINDLAYER "wikilink")*.layer* | R | Gets the [item](Items "wikilink") that the character has equipped in a specified layer. |  |
| [FINDTYPE](FINDTYPE "wikilink")*.type* | R | Gets the first [item](Items "wikilink") found equipped to the character or inside their backpack, with the matching [TYPE](TYPE "wikilink"). |  |
| [MEMORYFINDTYPE](MEMORYFINDTYPE "wikilink")*.memory_flags* | R | Gets a [memory item](Items "wikilink") with the specified flags. |  |
| [MEMORYFIND](MEMORYFIND "wikilink").*object_uid* | R | Gets a [memory item](Items "wikilink") that is linked to the given object. |  |
| [OWNER](OWNER "wikilink") | R | Gets the character that owns this character. (RW in SphereServer-X Build) |  |
| [SPAWNITEM](SPAWNITEM "wikilink") | R | Gets the [spawn item](Items "wikilink") (t_spawn_char) that this character originated from. |  |
| [WEAPON](WEAPON "wikilink") | R | Gets the [weapon](Items "wikilink") that the character currently has equipped. |  |
| [P](P "wikilink") | RW | Gets or sets the [position](Map_Points "wikilink") that the character is at. |  |
| [REGION](Regions "wikilink") | R | Gets the [region](Regions "wikilink") that the character is currently located in. |  |
| [ROOM](Rooms "wikilink") | R | Gets the [room](Rooms "wikilink") that the character is in. |  |
| [SECTOR](Sectors "wikilink") | R | Gets the [sector](Sectors "wikilink") that the character is in. |  |
| [TOPOBJ](TOPOBJ "wikilink") | R | Gets the top-most [character](Characters "wikilink") or [item](Items "wikilink") in the world that contains the character. |  |
| [TYPEDEF](TYPEDEF_(Reference) "wikilink") | R | Gets the [CHARDEF](CHARDEF "wikilink") that defines the character. |  |
```

```
## Properties and Functions
```

Here is a list of all character properties and functions. If a function is marked as readable then it can return a value when used as <KEY>. Click on the name for more detailed information such as usage and examples. If an attempt is made to access a property that does not exist on the character, the property from the [CHARDEF](CHARDEF "wikilink") will be accessed instead.

```
| **Name** | **Read/Write** | **Description** | **Sphere X only?** |
| --- | --- | --- | --- |
| [AC](AC) | R | Returns the character's total defense. |  |
| [ACTARG1](ACTARG1) | RW | Gets or sets the character's ACTARG1 value. X branch only: for skills Enticement, Peacemaking and Provocation, if ACTARG1 is set to the UID of the instrument to play, it will be played the sound of that instrument. |  |
| [ACTARG2](ACTARG2) | RW | Gets or sets the character's ACTARG2 value. |  |
| [ACTARG3](ACTARG3) | RW | Gets or sets the character's ACTARG3 value. |  |
| [ACTDIFF](ACTDIFF) | RW | Gets or sets the difficulty of the character's current action. |  |
| [ACTION](ACTION) | RW | Gets or sets the skill that the character is currently using. |  |
| [ACTP](ACTP) | RW | Gets or sets the character's ACTP value. Can get x,y,z,position of the point in X branch. |  |
| [ACTPRV](ACTPRV) | RW | Gets or sets the character's ACTPRV value. |  |
| [ADDHOUSE uid](ADDHOUSE_uid) | W | X branch only. Adds the given uid to the player's house. If the player current count of houses is greater than the limit he has, the house will be redeeded. |  |
| [ADDSHIP uid](ADDSHIP_uid) | W | X branch only. Adds the given uid to the player's ship. If the player current count of ships is greater than the limit he has, the ship will be redeeded. |  |
| [AFK](AFK) | W | Gets or sets whether or not the character is in AFK mode. |  |
| [AGE](AGE) | R | Returns the age of the character since its creation, in seconds. |  |
| [ALLSKILLS](ALLSKILLS) *amount* | W | Sets all of the character's skills to the specified amount. |  |
| [ANIM](ANIM) *anim_id* | W | Plays the specified animation on the character. |  |
| [ATTACKER](ATTACKER)*.properties* | R | Gets the number of opponents who have damaged the character. |  |
| [BANK](BANK) *layer* | W | Opens the character's bank (or the container at the specified layer) for SRC to view. |  |
| [BANKBALANCE](BANKBALANCE) | R | Returns the total amount of gold in the character's bankbox. |  |
| [BARK](BARK) *sound_id* | W | Plays the specified sound (or the character's generic sound if not specified) to nearby clients from this character. |  |
| [BODY](BODY) | RW | Gets or sets the character's body. |  |
| [BOUNCE](BOUNCE) *item_uid* | W | Places a specified item in the character's backpack. |  |
| [BOW](BOW) | W | Makes the character bow to SRC. |  |
| [CAN](CAN_(Characters)) | RW | Gets or Sets the Can flags for this chardef. Only readable in X branch. |  |
| [CANCAST](CANCAST) *spell_id, check_antimagic* | R | Returns 1 if the character can cast a given spell, bypassing anti-magic field tests if *check_antimagic* set to 0. |  |
| [CANMAKE](CANMAKE) *item_id* | R | Returns 1 if the character has the skills and resources to craft a certain item. |  |
| [CANMAKESKILL](CANMAKESKILL) *item_id* | R | Returns 1 if the character has the skills to craft a certain item. |  |
| [CANMASK](CANMASK_(Characters)) | RW | X branch only. Stores the CAN flags to be dynamically switched on or off from the base CAN property. |  |
| [CANMOVE](CANMOVE) *direction* | R | Returns 1 if the character can move in the given direction. |  |
| [CANSEE](CANSEE) | R | Returns 1 if SRC can see the character. |  |
| [CANSEELOS](CANSEELOS) | R | Returns 1 if SRC has line of sight to the character. |  |
| [CANSEELOSFLAG](CANSEELOSFLAG) *flags* | R | Returns 1 if SRC has line of sight to the character, with flags to modify what tests take place. |  |
| [COLOR](COLOR) | RW | Gets or sets the character's hue. |  |
| [CONSUME](CONSUME) *resource_list* | W | Removes specified resources from SRC's backpack. |  |
| [COUNT](COUNT) | R | Returns the number of items equipped to the character. |  |
| [CREATE](CREATE) | RW (R only on X) | Gets or sets the character's age since creation, in seconds (Tenth of seconds on X). |  |
| [CRIMINAL](CRIMINAL) | W | Sets whether or not the character is a criminal. |  |
| [CURFOLLOWER](CURFOLLOWER) | RW | Gets or sets the number of current followers the character has, |  |
| [DAMAGE](DAMAGE) *amount, type, source* | W | Inflicts damage upon the character. `When using COMBAT_ELEMENTAL_ENGINE add the following parameters after`*`source`*`:`*`physical`*`,`*`fire`*`,`*`cold`*`,`*`poison`*`,`*`energy`*`. All the values are in %.` |  |
| [DELHOUSE uid](DELHOUSE_uid) | W | X branch only. Deletes the given uid from the player's list (Will not delete the house)(-1 clears the whole list). |  |
| [DELSHIP uid](DELSHIP_uid) | W | X branch only. Deletes the given uid from the player's list (Will not delete the ship)(-1 clears the whole list). |  |
| [DESTROY](DESTROY) | W | Deletes the object, not stopped by a return 1 in [@Destroy](@Destroy) |  |
| [DEX](DEX) | RW | Gets or sets the character's total dexterity. |  |
| [DIALOG](DIALOG_(Function)) *dialog_id, page, parameters* | W | Displays a dialog to SRC. |  |
| [DIALOGCLOSE](DIALOGCLOSE) *dialog_id button* | W | Closes a dialog that SRC has open, simulating a button press. |  |
| [DIALOGLIST](DIALOGLIST)*.COUNT* | R | Gets the number of number of dialogs currently considered to be visible on SRC's screen. |  |
| [DIALOGLIST](DIALOGLIST)*.n.ID* | R | Gets the ID of the nth dialog that SRC has open (zero-based). |  |
| [DIALOGLIST](DIALOGLIST)*.n.COUNT* | R | Gets the number of instances of nth dialog SRC has open (zero-based). |  |
| [DIR](DIR) | RW | Gets or setes the direction that the character is facing. |  |
| [DISCONNECT](DISCONNECT) | W | Disconnects the character. |  |
| [DISMOUNT](DISMOUNT) | W | Dismounts the character from their ride. |  |
| [DISPIDDEC](DISPIDDEC) | R | Gets the ID of the character as a decimal number. |  |
| [DISTANCE](DISTANCE) *point_or_uid* | R | Gets the distance between this object and either SRC, a map location or another object. |  |
| [DCLICK](DCLICK) | W | Double clicks the character, with SRC as the source of the event. |  |
| [DCLICK](DCLICK) *object_uid* | W | Double clicks an object, with the character as SRC. |  |
| [DRAWMAP](DRAWMAP) *radius* | W | Starts the cartography skill, drawing a map of the local area up to *radius* tiles. |  |
| [DROP](DROP) *item_uid* | W | Drops a specified item at the character's feet. |  |
| [DUPE](DUPE) | W | Creates a clone of the character. |  |
| [EDIT](EDIT) | W | Displays an editing dialog for the character to SRC. |  |
| [EFFECT](EFFECT) *type, item_id, speed, loop, explode, color, rendermode* | W | Displays an effect to nearby clients. |  |
| [EFFECTLOCATION](EFFECTLOCATION) *x,y,z,type,itemid,speed,loop,explode,color,render* | W | Similar to the EFFECT command but instead of an object it takes a terrain location as a target. | X |
| [EMOTE](EMOTE) *message* | W | Displays a *You see* message to all nearby clients. |  |
| [EMOTEACT](EMOTEACT) | RW | Gets, sets or toggles whether or not the character will emote all of its actions. |  |
| [EQUIP](EQUIP) *item_uid* | W | Equips an item to the character. |  |
| [EQUIPARMOR](EQUIPARMOR) | W | Equips the character with the best armour in their backpack. |  |
| [EQUIPHALO](EQUIPHALO) *timeout* | W | Equips a halo light to the character, lasting for *timeout* tenths of a second. |  |
| [EQUIPWEAPON](EQUIPWEAPON) | W | Equips the character with the best weapon in their backpack. |  |
| [EVENTS](EVENTS_(Property)) *event_defname* | RW | Gets a list of events attached to the object, or adds or removes an event to or from the object. |  |
| [EXP](EXP) | RW | Gets or sets the character's experience points. |  |
| [FACE](FACE) *object_uid* (P coords in X branch) | W | Turns the character to face a specified object or SRC. Admits coordinates instead uid in X branch. |  |
| [FAME](FAME) | RW | Gets or sets the character's fame. |  |
| [FAME](FAME)*.fame_group* | R | Returns 1 if the character's fame falls within the specified fame group. |  |
| [FCOUNT](FCOUNT) | R | Returns the total number of items equipped to the character, including subitems |  |
| [FLAGS](FLAGS) | RW | Gets or sets the character's flags. |  |
| [FIX](FIX) | W | Re-aligns the character's Z level to ground level. |  |
| [FIXWEIGHT](FIXWEIGHT) | W | Recalculates the character's total weight. |  |
| [FLIP](FLIP) | W | Rotates the character. |  |
| [FONT](FONT) | RW | Gets or sets the character's speech font. |  |
| [FOOD](FOOD) | RW | Gets or sets the character's food level. |  |
| [FORGIVE](FORGIVE) | W | Revokes the character's jailed status. |  |
| [GETHOUSEPOS uid](GETHOUSEPOS_uid) | R | Returns the position of the given UID on the houses list (-1 if not found). |  |
| [GETSHIPPOS uid](GETSHIPPOS_uid) | R | Returns the position of the given UID on the ships list (-1 if not found). |  |
| [GO](GO) *location* | W | Teleports the character to the specified location. |  |
| [GOCHAR](GOCHAR) *n* | W | Teleports the character to the nth character in the world. |  |
| [GOCHARID](GOCHARID) *character_defname* | W | Teleports the character to the next characer in the world with the specified [BASEID](BASEID) |  |
| [GOCLI](GOCLI) *n* | W | Teleports the character to the nth online player. (zero-based) |  |
| [GOITEMID](GOITEMID) *item_defname* | W | Teleports the character to the next item in the world with the specified [BASEID](BASEID). |  |
| [GOLD](GOLD) | RW | Gets or sets the amount of gold the character has. |  |
| [GONAME](GONAME) *name* | W | Teleports the character to the next character or item in the world with the specified name, accepts wildcards (*). |  |
| [GOSOCK](GOSOCK) *socket* | W | Teleports the character to the online player with the specified socket number. |  |
| [GOTYPE](GOTYPE) *item_type* | W | Teleports the character to the next item in the world with the specified [TYPE](TYPE). |  |
| [GOUID](GOUID) *object_uid* | W | Teleports the character to the object with the specified [UID](UID). |  |
| [GUILDABBREV](GUILDABBREV) | R | Returns the character's guild abbreviation. |  |
| [HEAR](HEAR) *text* | W | For NPCs, acts as if SRC had spoken the specified *text*. For players, displays *text* as a system message. |  |
| [HEIGHT](HEIGHT) | R | Gets the character's height. |  |
| [HITS](HITS) | RW | Gets or sets the character's hitpoints. |  |
| [HOME](HOME) | RW | Gets or sets the character's home location. |  |
| [HOUSE.n](HOUSE.n) | R | X branch only.Access the house in the Nth position, eg: house.3.Redeed |  |
| [HOUSES](HOUSES) | R | X branch only. Returns the number of houses on the player's list. |  |
| [HUNGRY](HUNGRY) | W | Displays this character's hunger level to SRC. |  |
| [ID](ID) | R | Gets the character's ID. |  |
| [INFO](INFO) | W | Displays an information dialog about the character to SRC. |  |
| [INT](INT) | RW | Gets or sets the character's total intelligence. |  |
| [INVIS](INVIS) | W | Sets whether or not the character is invisible. |  |
| [INVUL](INVUL) | W | Sets whether or not the character is invulnerable. |  |
| [ISARMOR](ISARMOR) *object_uid* | R | Returns 1 if the object is armour. |  |
| [ISCHAR](ISCHAR) | R | Returns 1 if the object is a character. |  |
| [ISCONT](ISCONT) | R | Returns 1 if the object is a container. |  |
| [ISDIALOGOPEN](ISDIALOGOPEN) *dialog_id* | R | Returns 1 if SRC has the specified dialog visible on their screen. |  |
| [ISEVENT](ISEVENT)*.event_defname* | R | Returns 1 if the object has an event attached to it. |  |
| [ISGM](ISGM) | R | Returns 1 if the character is in GM mode. |  |
| [ISINPARTY](ISINPARTY) | R | Returns 1 if the player is in a [party](party). |  |
| [ISITEM](ISITEM) | R | Returns 1 if the object is an item. |  |
| [ISMYPET](ISMYPET) | R | Returns 1 if the character belongs to SRC. |  |
| [ISNEARTYPE](ISNEARTYPE) *type, distance, flags* | R | Returns 1 if a nearby item has the given TYPE. |  |
| [ISNEARTYPETOP](ISNEARTYPETOP) *type, distance, flags* | R | Returns a nearby world location of a nearby item which has the given TYPE. |  |
| [ISONLINE](ISONLINE) | R | Returns 1 if the character is considered to be online. |  |
| [ISPLAYER](ISPLAYER) | R | Returns 1 if the object is a player. |  |
| [ISSTUCK](ISSTUCK) | R | Returns 1 if the character cannot walk in any direction. |  |
| [ISTEVENT](ISTEVENT)*.event_defname* | R | Returns 1 if the object has an event attached to its [CHARDEF](CHARDEF). |  |
| [ISTIMERF](ISTIMERF)*.function* | R | Returns the number of seconds left on the specified timerf if it exists. |  |
| [ISVENDOR](ISVENDOR) | R | Returns 1 if the character is a vendor. |  |
| [ISVERTICALSPACE](ISVERTICALSPACE) *location* | R | Returns 1 if the ceiling at the given location is high enough for the character to fit under. |  |
| [ISWEAPON](ISWEAPON) *object_uid* | R | Returns 1 if the object is a weapon. |  |
| [JAIL](JAIL) *cell* | W | Sends the character to jail, to a specified jail cell. |  |
| [KARMA](KARMA) | RW | Gets or sets the character's karma. |  |
| [KARMA](KARMA)*.karma_group* | R | Returns 1 if the character's karma falls within the specified karma group. |  |
| [KILL](KILL) | W | Kills the character. |  |
| [LEVEL](LEVEL) | RW | Gets or sets the character's experience level. |  |
| [LIGHT](LIGHT) | RW | Gets or sets the character's personal light level. |  |
| [LUCK](LUCK) | RW | Gets or sets the luck value for the character. |  |
| [MAKEITEM](MAKEITEM) *item_defname, amount* | \| W | Begins an attempt to craft the specified quantity of the given item. |  |
| [MANA](MANA) | RW | Gets or sets the character's mana. |  |
| [MAP](MAP) | RW | Gets or sets the map that this object is located. |  |
| [MAPWAYPOINT](MAPWAYPOINT) "ObjectUID, WaypointType" | W | Add/remove waypoints on client radar map (enhanced clients only). |  |
| [MAXFOLLOWER](MAXFOLLOWER) | RW | Gets or sets the maximum number of followers the character can have. |  |
| [MAXHITS](MAXHITS) | RW | Gets or sets the character's maximum hitpoints. |  |
| [MAXHOUSES](MAXHOUSES) | RW | Added to Accounts and Chars, when created they read this setting from the sphere.ini (if values on sphere.ini change, they will not reflect on already created accounts/chars). | X |
| [MAXMANA](MAXMANA) | RW | Gets or sets the character's maximum mana. |  |
| [MAXSHIPS](MAXSHIPS) | RW | Added Accounts and Chars, when created they read this new setting from the sphere.ini (if values on sphere.ini change, they will not reflect on already created accounts/chars). | X |
| [MAXSTAM](MAXSTAM) | RW | Gets or sets the character's maximum stamina. |  |
| [MAXWEIGHT](MAXWEIGHT) | R | Returns the maximum weight that the character can carry. |  |
| [MEMORY](MEMORY)*.object_uid* | RW | Gets or sets the memory flags the character has for the given object. |  |
| [MENU](MENU_(Function)) *menu_defname* | W | Displays a menu to SRC. |  |
| [MESSAGE](MESSAGE) *message* | W | Displays a message above this character to SRC. |  |
| [MESSAGEUA](MESSAGEUA) *colour, talkmode, font, lang_id, message* | W | Displays a UNICODE message above this character to SRC. |  |
| [MODAR](MODAR) | RW | Gets or sets a modifier for the character's armour rating. |  |
| [MODDEX](MODDEX) | RW | Gets or sets the character's dexterity modifier. |  |
| [MODINT](MODINT) | RW | Gets or sets the character's intelligence modifier. |  |
| [MODMAXWEIGHT](MODMAXWEIGHT) | RW | Gets or sets the character's maximum weight modifier. |  |
| [MODSTR](MODSTR) | RW | Gets or sets the character's strength modifier. |  |
| [MOUNT](MOUNT) | R | Gets the UID of the character's mount. |  |
| [MOUNT](MOUNT) *mount_uid* | W | Attempts to mount the character on to the specified mount. |  |
| [MOVE](MOVE) *direction* | R | Returns the movement flags for the tile in the given direction (see can_flags in sphere_defs.scp). |  |
| [MOVE](MOVE) *direction, amount* [MOVE](MOVE) *x y* | W | Moves the object relative to its current position. |  |
| [MOVENEAR](MOVENEAR) *object_uid, distance* | W | Moves the character to a random location near another object within a certain distance. |  |
| [MOVETO](MOVETO) *location* | W | Moves the character to a specific location. |  |
| [NAME](NAME) | RW | Gets or sets the character's name. |  |
| [NEWBIESKILL](NEWBIESKILL) *skill_id* | W | Distributes items that are associated with the specified skill, to the character. |  |
| [NEWGOLD](NEWGOLD) *amount* | W | Generates *amount* gold in the character's backpack. |  |
| [NEWLOOT](NEWLOOT) *item_or_template_defname* | W | Generates the specified item or template into the character's backpack, providing that they are an NPC that hasn't been summoned. |  |
| [NIGHTSIGHT](NIGHTSIGHT) | RW | Gets or sets whether or not the character has nightsight enabled. |  |
| [NOTOGETFLAG](NOTOGETFLAG) *viewer_uid, allow_incognito* | RW | Gets the character's notoriety flags as seen by the specified viewer. |  |
| [NPC](NPC) | RW | Gets or sets the character's AI type. |  |
| [NUDGEDOWN](NUDGEDOWN) *amount* | W | Decreases the character's Z level. |  |
| [NUDGEUP](NUDGEUP) *amount* | W | Increases the characer's Z level. |  |
| [OBODY](OBODY) | RW | Gets or sets the character's original body. |  |
| [OPENPAPERDOLL](OPENPAPERDOLL) | W | Displays the character's paperdoll to SRC. |  |
| [OPENPAPERDOLL](OPENPAPERDOLL) *character_uid* | W | Displays a specified character's paperdoll to this character. |  |
| [OSKIN](OSKIN) | RW | Gets or sets the character's original colour. |  |
| [ODEX](ODEX) | RW | Gets or sets the character's base dexterity (without modifiers). |  |
| [OINT](OINT) | RW | Gets or sets the character's base intelligence (without modifiers). |  |
| [OSTR](OSTR) | RW | Gets or sets the character's base strength (without modifiers). |  |
| [PACK](PACK) | W | Opens the character's backpack for SRC to view. |  |
| [POISON](POISON) *strength* | W | Poisons the character, with the specified poison strength. |  |
| [POLY](POLY) *character_id* | W | Begins casting the polymorph spell, with *character_id* being the character to turn into. |  |
| [PROMPTCONSOLE](PROMPTCONSOLE) *function, prompt_message* | W | Displays a prompt message to SRC and passes their response into a specified function. |  |
| [PROMPTCONSOLEU](PROMPTCONSOLEU) *function, prompt_message* | W | Displays a prompt message to SRC and passes their response into a specified function, supporting UNICODE response. |  |
| [PRIVSET](PRIVSET) *plevel* | W | Sets the PLEVEL of the character. |  |
| [RANGE](RANGE) | R | Gets the combat range of the character. |  |
| [RELEASE](RELEASE) | W | Clears the character's owners. |  |
| [REMOVE](REMOVE) *allow_player_removal* | W | Deletes the character. |  |
| [REMOVEFROMVIEW](REMOVEFROMVIEW) | W | Removes the object from nearby clients' screens. |  |
| [RESCOLD](RESCOLD) | RW | Gets or sets the character's resistance to cold. |  |
| [RESCOLDMAX](RESCOLDMAX) | RW | Gets or sets the character's maximum resistance to cold. |  |
| [RESCOUNT](RESCOUNT) *item_defname* | R | Returns the total amount of a specific item equipped to the character or inside their baackpack. |  |
| [RESENDTOOLTIP](RESENDTOOLTIP) *sendfull*,*usecache* | W | Forces Sphere to update the tooltips for nearby clients. If sendfull is 1 the entire tooltip is sent and if 0 then just the header is sent. If usecache is 1 then the cached version (if found) will be sent and if 0 then the cached version (if found) will be replaced and sent |  |
| [RESENERGY](RESENERGY) | RW | Gets or sets the character's resistance to energy. |  |
| [RESENERGYMAX](RESENERGYMAX) | RW | Gets or sets the character's maximum resistance to energy. |  |
| [RESFIRE](RESFIRE) | RW | Gets or sets the character's resistance to fire. |  |
| [RESFIREMAX](RESFIREMAX) | RW | Gets or sets the character's maximum resistance to fire. |  |
| [RESPOISON](RESPOISON) | RW | Gets or sets the character's resistance to poison. |  |
| [RESPOISONMAX](RESPOISONMAX) | RW | Gets or sets the character's maximum resistance to poison. |  |
| [RESTEST](RESTEST) *item_list* | R | Returns 1 if all of the items in the list can be found equipped to the character or inside their backpack. |  |
| [RESURRECT](RESURRECT) *force* | W | Resurrects the character. If *force* is 1 then usual anti-magic checks are bypasses. |  |
| [SALUTE](SALUTE) *object_uid* | W | Makes the character salute a specified object or SRC. |  |
| [SAY](SAY) *message* | W | Makes the character speak a message. |  |
| [SAYU](SAYU) *message* | W | Makes the character speak a UTF-8 message |  |
| [SAYUA](SAYUA) *colour, talkmode, font, lang_id, text* | W | MAkes the character speak a UNICODE message. |  |
| [SDIALOG](SDIALOG) *dialog_id, page, parameters* | W | Displays a dialog to SRC, providing that it is not already open. |  |
| [SERIAL](SERIAL) | R | Gets the item's unique ID in the world. |  |
| [SEX](SEX) *value_male:value_female* | R | Returns *value_male* or *value_female* depending on the character's gender. |  |
| [SEXTANTP](SEXTANTP) *location* | R | Converts the character's location or a specified location into sextant coordinates. |  |
| *skill_name* | RW | Gets or sets the character's skill level in *skill_name*. |  |
| [SHIP.n](SHIP.n) | R | X branch only. Added to access the ship in the Nth position, eg: ship.3.Redeed |  |
| [SHIPS](SHIPS) | R | X branch only. Return the ships on the player's list. |  |
| [SKILL](SKILL_(Function)) | W | Begins using a skill. |  |
| [SKILLADJUSTED](SKILLADJUSTED)."number or skill_name" (X branch only) | R | Returns the skill value adjusted by the stat bonus. Example “SkillAdjusted.1” or “SkillAdjusted.Anatomy”. |  |
| [SKILLCHECK](SKILLCHECK) *skill_id, difficulty* | R | Performs a check for skill success, returning 1 if the attempt was successful. |  |
| [SKILLBEST](SKILLBEST)*.n* | R | Returns the ID of the character's nth highest skill (0 = Highest) |  |
| [SKILLGAIN](SKILLGAIN) *skill, difficulty* | W | Invokes Sphere's skill gain for the specified skill, with the given difficulty (0-100) |  |
| [SKILLTEST](SKILLTEST) *skill_list* | R | Returns 1 if the character possess all of the skills in the list. |  |
| [SKILLTOTAL](SKILLTOTAL) | R | Returns the total value of all the character's skills. |  |
| [SKILLTOTAL](SKILLTOTAL) *skill_group* | R | Returns the total value of all the character's skills with the specified group flag(s). |  |
| [SKILLTOTAL](SKILLTOTAL) *-amount* | R | Returns the total value of all the character's skills that are under *amount*. |  |
| [SKILLTOTAL](SKILLTOTAL) *+amount* | R | Returns the total value of all the character's skills that are over *amount*. |  |
| [SKILLUSEQUICK](SKILLUSEQUICK) *skill_id, difficulty* | R | Quickly uses a skill, returning 1 if the attempt was successful. |  |
| [SLEEP](SLEEP) *fall_forwards* | W | Makes the character appear to sleep. |  |
| [SOUND](SOUND) *sound_id, repeat* | W | Plays a sound from this character. |  |
| [SPELLEFFECT](SPELLEFFECT) *spell_id, strength, source_character_uid, source_item_uid* | W | Causes the character to be affected by a spell. |  |
| [SPEECHCOLOROVERRIDE](SPEECHCOLOROVERRIDE) *value* | RW | Override client speech hue. |  |
| [STAM](STAM) | RW | Gets or sets the character's stamina. |  |
| [STEPSTEALTH](STEPSTEALTH) | RW | Gets or sets the amount of steps a character can do while using the Stealth skill. |  |
| [STONE](STONE) | RW | Gets or sets whether or not the character is trapped in stone. |  |
| [STR](STR) | RW | Gets or sets the character's total strength. |  |
| [SUICIDE](SUICIDE) | W | Forces the character to commit suicide. |  |
| [SUMMONCAGE](SUMMONCAGE) | W | Teleports the character to SRC's, surrounded by a cage multi. |  |
| [SUMMONTO](SUMMONTO) | W | Teleports the character to SRC's position. |  |
| [TAG](TAG)*.name* | RW | Gets or sets the value of a TAG. |  |
| [TAGAT](TAGAT)*.index* | R | Gets a TAG at the given zero-based index. |  |
| [TAGAT](TAGAT)*.index*.KEY | R | Gets the name of the TAG at the given zero-based index. |  |
| [TAGAT](TAGAT)*.index*.VAL | R | Gets the value of the TAG at the given zero-based index. |  |
| [TAGCOUNT](TAGCOUNT) | R | Gets the number of TAGs stored on the item. |  |
| [TAGLIST](TAGLIST) | W | Outputs a list of the object's TAGs. |  |
| [TARGET](TARGET)*FGMW* *function* | W | Displays a targeting cursor to SRC. |  |
| [TIMER](TIMER) | RW | Gets or sets the length of time before the item's timer expires, in seconds. |  |
| [TIMERD](TIMERD) | RW | Gets or sets the length of time before the item's timer expires, in tenths of a second. |  |
| [TIMERF](TIMERF) *time, function* | W | Scheduled a function to be executed on this object in *time* seconds. |  |
| [TIMERF](TIMERF) *CLEAR* | W | Clears all scheduled functions from the character. |  |
| [TIMERF](TIMERF) *STOP, function* | W | Stops the specified function from the character. (On X version wild character * is available for defining the function name or the argument) |  |
| [TIMERMS](TIMERMS) | W | Set an object timer to elapse after the given number of milliseconds. |  |
| [TITHING](TITHING) | RW | Gets or sets the number of tithing points the character has. |  |
| [TITLE](TITLE) | RW | Gets or sets the character's title. |  |
| [TOWNABBREV](TOWNABBREV) | R | Returns the character's town abbreviation. |  |
| [TRIGGER](TRIGGER) *trig_name, trig_type* | R | Fires a custom trigger and returns the RETURN value. |  |
| [UID](UID) | R | Gets the item's unique ID in the world. |  |
| [UNDERWEAR](UNDERWEAR) | W | Toggles the display of underwear on the character. |  |
| [UNEQUIP](UNEQUIP) *item_uid* | W | Unequips an item from the character, placing it in their backpack. |  |
| [UPDATE](UPDATE) | W | Updates the state of the character to nearby clients. |  |
| [UPDATEX](UPDATEX) | W | Updates the state of the character to nearby clients, removing it from their view first to ensure a full refresh. |  |
| [USEITEM](USEITEM) | W | Double clicks the character, with SRC as the source of the event, without checking for line of sight. |  |
| [USEITEM](USEITEM) *object_uid* | W | Double clicks an object, with the character as SRC. |  |
| [VISUALRANGE](VISUALRANGE) | RW | Gets or sets the character's sight range. |  |
| [WEIGHT](WEIGHT) | R | Gets the weight of the character. |  |
| [WHERE](WHERE) | W | Describes the character's location to SRC. |  |
| [Z](Z) | R | Gets the Z position of the character. |  |
```

```
## Triggers
```

Here is a list of all character triggers. Click on the trigger name for more detailed information such as arguments and examples.

```
|  |  |  |
|----|----|----|
| **Name** | **Description** | **Sphere X only?** |
| [@AfterClick](@AfterClick "wikilink") | Fires when the object has been single-clicked, just before the overhead name is shown. |  |
| [@Attack](@Attack "wikilink") | Fires when the character begins attacking another. |  |
| [@CallGuards](@CallGuards "wikilink") | Fires when the character calls for guards. |  |
| [@CharAttack](@CharAttack "wikilink") | Fires when the character is attacked by another character. |  |
| [@CharClick](@CharClick "wikilink") | Fires when the character is clicked by another character. |  |
| [@CharClientTooltip](@CharClientTooltip "wikilink") | Fires when the tooltips are about to be sent to the character. |  |
| [@CharDClick](@CharDClick "wikilink") | Fires when the character double clicks another character. |  |
| [@CharTradeAccepted](@CharTradeAccepted "wikilink") | Fires when another character accepts trade with the character. |  |
| [@Click](@Click "wikilink") | Fires when the object has been single-clicked. |  |
| [@ClientTooltip](@ClientTooltip "wikilink") | Fires when tooltips for this character are about to be sent to a client. |  |
| [@CombatAdd](@CombatAdd "wikilink") | Fires when someone is being added to my attacker list. |  |
| [@CombatDelete](@CombatDelete "wikilink") | Fires when someone is deleted from my attacker list. |  |
| [@CombatEnd](@CombatEnd "wikilink") | Fires when someone is being deleted from my attacker list and I don't have any more viable targets. |  |
| [@CombatStart](@CombatStart "wikilink") | Fires when adding first attacker to my list. |  |
| [@ContextMenuRequest](@ContextMenuRequest "wikilink") | Fires when a client requests the context menu options for the object. |  |
| [@ContextMenuSelect](@ContextMenuSelect "wikilink") | Fires when a client selects a context menu option for the object. |  |
| [@Create](@Create "wikilink") | Fires when the object is initially created, before it is placed in the world. |  |
| [@Criminal](@Criminal "wikilink") | Fires when the character becomes a criminal. |  |
| [@DClick](@DClick "wikilink") | Fires when the object is double-clicked. |  |
| [@Death](@Death "wikilink") | Fires when the character's hitpoints reaches zero. |  |
| [@DeathCorpse](@DeathCorpse "wikilink") | Fires when a corpse is created for the character. |  |
| [@Destroy](@Destroy "wikilink") | Fires when the object is being deleted. |  |
| [@Dismount](@Dismount "wikilink") | Fires when the character dismounts their ride. |  |
| [@Dye](@Dye "wikilink") | Fires when the character is about to change their color or the color of an object. |  |
| [@Eat](@Eat "wikilink") | Fires when the character eats something. |  |
| [@EnvironChange](@EnvironChange "wikilink") | Fires when the environment changes for the character. |  |
| [@ExpChange](@ExpChange "wikilink") | Fires when the character's experience points change. |  |
| [@ExpLevelChange](@ExpLevelChange "wikilink") | Fires when the character's experience level changes. |  |
| [@FameChange](@FameChange "wikilink") | Fires when the character's fame changes. |  |
| [@GetHit](@GetHit "wikilink") | Fires when the character receives damage. |  |
| [@Hit](@Hit "wikilink") | Fires when the character hits another in combat. |  |
| [@HitMiss](@HitMiss "wikilink") | Fires when the character fails to hit another in combat. |  |
| [@HitParry](@HitParry "wikilink") | X branch only. Fires when the character is attempting to parry a hit. | X |
| [@HitTry](@HitTry "wikilink") | Fires when the character tries to hit another in combat. |  |
| [@HouseDesignCommit](@HouseDesignCommit "wikilink") | Fires when the character commits a new house design. |  |
| [@HouseDesignExit](@HouseDesignExit "wikilink") | Fires when the character exits house design mode. |  |
| [@Hunger](@Hunger "wikilink") | Fires when the character's food level decreases. |  |
| [@ItemAfterClick](@ItemAfterClick "wikilink") | Fires when the character single-clicks an item, just before the overhead name is shown. |  |
| [@ItemBuy](@ItemBuy "wikilink") | Fires when the character buys an item from a vendor. |  |
| [@ItemClick](@ItemClick "wikilink") | Fires when the character single-clicks an item. |  |
| [@ItemClientTooltip](@ItemClientTooltip "wikilink") | Fires when the tooltips are about to be sent to the client for an item. |  |
| [@ItemContextMenuRequest](@ItemContextMenuRequest "wikilink") | Fires when the character requests the context menu options for an item. |  |
| [@ItemContextMenuSelect](@ItemContextMenuSelect "wikilink") | Fires when the character selects a context menu option for an item. |  |
| [@ItemCreate](@ItemCreate "wikilink") | Fires when an item is initially created, before it is placed in the world, and the character is in some way responsible for it. |  |
| [@ItemDamage](@ItemDamage "wikilink") | Fires when the character damages an item. |  |
| [@ItemDClick](@ItemDClick "wikilink") | Fires when the character double-clicks an item. |  |
| [@ItemDropOn_Char](@ItemDropOn_Char "wikilink") | Fires when the character drops an item on to a character. |  |
| [@ItemDropOn_Ground](@ItemDropOn_Ground "wikilink") | Fires when the character drops an item on to the ground. |  |
| [@ItemDropOn_Item](@ItemDropOn_Item "wikilink") | Fires when the character drops an item on to another item. |  |
| [@ItemDropOn_Self](@ItemDropOn_Self "wikilink") | Fires when the character drops an item inside another item. |  |
| [@ItemEquip](@ItemEquip "wikilink") | Fires when the character equips an item. |  |
| [@ItemEquipTest](@ItemEquipTest "wikilink") | Fires when the characer is about to equip an item. |  |
| [@ItemPickUp_Ground](@ItemPickUp_Ground "wikilink") | Fires when the character picks an item up from the ground. |  |
| [@ItemPickUp_Pack](@ItemPickUp_Pack "wikilink") | Fires when the character picks an item up from inside a container. |  |
| [@ItemPickUp_Self](@ItemPickUp_Self "wikilink") | Fires when the character picks an item up from inside another item. |  |
| [@ItemPickUp_Stack](@ItemPickUp_Stack "wikilink") | Fires when the character picks up an item from a stack. |  |
| [@ItemSell](@ItemSell "wikilink") | Fires when the character sells an item to a vendor. |  |
| [@ItemSmelt](@ItemSmelt "wikilink") | Fires when the character smelt an item. | X |
| [@ItemSpellEffect](@ItemSpellEffect "wikilink") | Fires when the character hits an item with a spell. |  |
| [@ItemStep](@ItemStep "wikilink") | Fires when the character steps on an item. |  |
| [@ItemTargOn_Cancel](@ItemTargOn_Cancel "wikilink") | Fires when the character cancels an item's target cursor. |  |
| [@ItemTargOn_Char](@ItemTargOn_Char "wikilink") | Fires when the character targets a character with an item's target cursor. |  |
| [@ItemTargOn_Ground](@ItemTargOn_Ground "wikilink") | Fires when the character targets the ground with an item's target cursor. |  |
| [@ItemTargOn_Item](@ItemTargOn_Item "wikilink") | Fires when the character targets an item with an item's target cursor. |  |
| [@ItemToolTip](@ItemToolTip "wikilink") | Fires when the character requests old-style tooltips for an item. |  |
| [@ItemUnEquip](@ItemUnEquip "wikilink") | Fires when the character unequips an item. |  |
| [@Jailed](@Jailed "wikilink") | Fires when the character is sent to jail. |  |
| [@KarmaChange](@KarmaChange "wikilink") | Fires when the character's karma changes. |  |
| [@Kill](@Kill "wikilink") | Fires when the character kills another character. |  |
| [@Login](@Login "wikilink") | Fires when the character logs in. |  |
| [@Logout](@Logout "wikilink") | Fires when the character logs out. |  |
| [@Mount](@Mount "wikilink") | Fires when the character mounts a ride. |  |
| [@MurderDecay](@MurderDecay "wikilink") | Fires when one of the character's kills is about to decay. |  |
| [@MurderMark](@MurderMark "wikilink") | Fires when the character is about to gain a kill. |  |
| [@NotoSend](@NotoSend "wikilink") | Fires the status bar/character notoriety color is sent to another players. |  |
| [@NPCAcceptItem](@NPCAcceptItem "wikilink") | Fires when the NPC receives an item. |  |
| [@NpcActCast](@NpcActCast "wikilink") | Fires when the NPC is selecting the spell to cast. | X |
| [@NPCActFight](@NPCActFight "wikilink") | Fires when the NPC makes a combat decision. |  |
| [@NPCActFollow](@NPCActFollow "wikilink") | Fires when the NPC follows another character. |  |
| [@NPCAction](@NPCAction "wikilink") | Fires when the NPC is about to perform an AI action. |  |
| [@NPCActWander](@NPCActWander "wikilink") | X branch only. Fires each step an NPC does while wandering. |  |
| [@NPCHearGreeting](@NPCHearGreeting "wikilink") | Fires when the NPC hears a character for the first time. |  |
| [@NPCHearUnknown](@NPCHearUnknown "wikilink") | Fires when the NPC hears something they don't understand. |  |
| [@NPCLookAtChar](@NPCLookAtChar "wikilink") | Fires then the NPC looks at a character. |  |
| [@NPCLookAtItem](@NPCLookAtItem "wikilink") | Fires when the NPC looks at an item. |  |
| [@NPCLostTeleport](@NPCLostTeleport "wikilink") | Fires when the NPC is lost and is about to be teleported back to their [HOME](HOME "wikilink"). |  |
| [@NPCRefuseItem](@NPCRefuseItem "wikilink") | Fires when the NPC refuses an item being given to them. |  |
| [@NPCRestock](@NPCRestock "wikilink") | Fires when the NPC is having their items restocked. |  |
| [@NPCSeeNewPlayer](@NPCSeeNewPlayer "wikilink") | Fires when the NPC first sees a player. |  |
| [@NPCSeeWantItem](@NPCSeeWantItem "wikilink") | Fires when the NPC sees an item they want. |  |
| [@NPCSpecialAction](@NPCSpecialAction "wikilink") | Fires when the NPC is about to perform a special action (leaving fire trail, dropping web). |  |
| [@PayGold](@PayGold "wikilink") | Fires when the character receives a payment. (Experimental Build Only) |  |
| [@PersonalSpace](@PersonalSpace "wikilink") | Fires when the character is stepped on. |  |
| [@PetDesert](@PetDesert "wikilink") | Fires when the character deserts its owner. |  |
| [@Profile](@Profile "wikilink") | Fires when a player attempts to read the character's profile from the paperdoll. |  |
| [@ReceiveItem](@ReceiveItem "wikilink") | Fires when the NPC receives an item from another character, before they decide if they want it or not. |  |
| [@RegenStat](@RegenStat "wikilink") | Fires when a character is going to regenerate any stat point. |  |
| [@RegionEnter](@RegionEnter "wikilink") | Fires when the character enters a region. |  |
| [@RegionLeave](@RegionLeave "wikilink") | Fires when the character leaves a region. |  |
| [@RegionResourceFound](@RegionResourceFound "wikilink") | Fires after a resource has been selected and the resource bit has been created. |  |
| [@Rename](@Rename "wikilink") | Fires when the character renames another. |  |
| [@Resurrect](@Resurrect "wikilink") | Fires when the character is being resurrected. |  |
| [@SeeCrime](@SeeCrime "wikilink") | Fires when the character sees a crime take place. |  |
| [@SeeHidden](@SeeHidden "wikilink") | Fires when this character is about to see a hidden character. |  |
| [@SkillAbort](@SkillAbort "wikilink") | Fires when the character aborts a skill. |  |
| [@SkillChange](@SkillChange "wikilink") | Fires when the character's skill level changes. |  |
| [@SkillFail](@SkillFail "wikilink") | Fires when the character fails a skill. |  |
| [@SkillGain](@SkillGain "wikilink") | Fires when the character has a chance to gain in a skill. |  |
| [@SkillMakeItem](@SkillMakeItem "wikilink") | Fires when the character crafts an item. |  |
| [@SkillMenu](@SkillMenu "wikilink") | Fires when a skill menu is shown to the character. |  |
| [@SkillPreStart](@SkillPreStart "wikilink") | Fires when the character starts a skill, before any hardcoded action takes place. |  |
| [@SkillSelect](@SkillSelect "wikilink") | Fires when the character selects a skill on their skill menu. |  |
| [@SkillStart](@SkillStart "wikilink") | Fires when the character starts a skill. |  |
| [@SkillSuccess](@SkillSuccess "wikilink") | Fires when the character succeeds at a skill. |  |
| [@SkillUseQuick](@SkillUseQuick "wikilink") | Fires when the character quickly uses a skill. |  |
| [@SkillWait](@SkillWait "wikilink") | Fires when Sphere wants to check if a character must wait before starting a skill. |  |
| [@SpellBook](@SpellBook "wikilink") | Fires when the character opens their spellbook. |  |
| [@SpellCast](@SpellCast "wikilink") | Fires when the character casts a spell. |  |
| [@SpellEffect](@SpellEffect "wikilink") | Fires when the character is hit by the effects of a spell. |  |
| [@SpellEffectAdd](@SpellEffectAdd "wikilink") | Fires when a spell memory is added to the character. | X |
| [@SpellEffectRemove](@SpellEffectRemove "wikilink") | Fires the spell memory is removed from the character. | X |
| [@SpellEffectTick](@SpellEffectTick "wikilink") | Fires when the character is hit the effect of a periodic spell (like Poison spell). | X |
| [@SpellFail](@SpellFail "wikilink") | Fires when the character fails to cast a spell. |  |
| [@SpellSelect](@SpellSelect "wikilink") | Fires when the character selects a spell to cast. |  |
| [@SpellSuccess](@SpellSuccess "wikilink") | Fires when the character successfully casts a spell. |  |
| [@SpellTargetCancel](@SpellTargetCancel "wikilink") | Fires when the character cancels target selection for a spell they have just cast. |  |
| [@StatChange](@StatChange "wikilink") | Fires when the character's STR, DEX or INT is changed through skill gain. |  |
| [@StepStealth](@StepStealth "wikilink") | Fires when the character takes a step whilst hidden. |  |
| [@ToggleFlying](@ToggleFlying "wikilink") | Fires when a Gargoyle Player is going to Fly or to Land. |  |
| [@ToolTip](@ToolTip "wikilink") | Fires when a player requests old-style tooltips for this character. |  |
| [@TradeAccepted](@TradeAccepted "wikilink") | Fires when the character accepts a trade with another player. |  |
| [@TradeClose](@TradeClose "wikilink") | Fires when a trade window is closed. |  |
| [@TradeCreate](@TradeCreate "wikilink") | Fires when a player begins a trade with another player. |  |
| [@UserBugReport](@UserBugReport "wikilink") | Fires when the player submits a bug report. |  |
| [@UserChatButton](@UserChatButton "wikilink") | Fires when the player presses the Chat button on the paperdoll. |  |
| [@UserExtCmd](@UserExtCmd "wikilink") | Fires when the player sends an extended command packet. (used by some macros) |  |
| [@UserExWalkLimit](@UserExWalkLimit "wikilink") | Fires when the player's movement is restricted by the movement speed settings in Sphere.ini |  |
| [@UserGuildButton](@UserGuildButton "wikilink") | Fires when the player presses the Guild button on the paperdoll. |  |
| [@UserKRToolbar](@UserKRToolbar "wikilink") | Fires when the player presses a button on the toolbar. |  |
| [@UserMailBag](@UserMailBag "wikilink") | Fires when the player drags the mail bag on to another character. |  |
| [@UserQuestArrowClick](@UserQuestArrowClick "wikilink") | Fires when the player clicks the quest arrow. |  |
| [@UserQuestButton](@UserQuestButton "wikilink") | Fires when the player presses the Quest button on the paperdoll. |  |
| [@UserSkills](@UserSkills "wikilink") | Fires when the player opens their skill menu, or a skill update is sent to the player. |  |
| [@UserSpecialMove](@UserSpecialMove "wikilink") | Fires when the player uses a special move. |  |
| [@UserStats](@UserStats "wikilink") | Fires when the player opens the status window. |  |
| [@UserUltimaStoreButton](@UserUltimaStoreButton "wikilink") | Fires when click on 'Ultima Store' button on new clients 7.0.62+ |  |
| [@UserVirtue](@UserVirtue "wikilink") | Fires when the player presses on the Virtue button. |  |
| [@UserVirtueInvoke](@UserVirtueInvoke "wikilink") | Fires when the player invokes a virtue through macros. |  |
| [@UserWarmode](@UserWarmode "wikilink") | Fires when the player switches between war and peace mode. |  |
```

```
## Players
```

Characters that are attached to an account become Player Characters. In addition to the basic character references, properties and functions they also receive the following:

```
### References
```

References return pointers to other objects (e.g. the REGION referenceallows you to access the REGION that an object is in). These can either be accessed by using *\<REFNAME\>* to return the [UID](UID "wikilink") (1 for object types that don't have UIDs) of the object or 0 if it doesn't exist, or by using *\<REFNAME.KEY\>* where KEY is a valid property/function/reference for the *REFNAME* object. Click on the name for more detailed information such as usage and examples.

```
|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [GUILD](GUILD "wikilink") | R | Gets the [guild stone](Special_Items#Guild.2FTown_Stones "wikilink") that the player belongs to. |
| [SKILLCLASS](SKILLCLASS_(Reference) "wikilink") | RW | Gets or sets the player's [skillclass](SKILLCLASS "wikilink"). |
| [TOWN](TOWN "wikilink") | R | Gets the [town stone](Special_Items#Guild.2FTown_Stones "wikilink") that the player belongs to. |
```

```
### Properties and Functions
```

Here is a list of all player properties and functions. If a function is marked as readable then it can return a value when used as <KEY>. Click on the name for more detailed information such as usage and examples.

```
|  |  |  |  |
|----|----|----|----|
| **Name** | **Read/Write** | **Description** | **Sphere X only?** |
| [DEATHS](DEATHS "wikilink") | RW | Gets or sets the number of times the player has died. |  |
| [DSPEECH](DSPEECH "wikilink") *+/-speech_id* | RW | Gets a list of attached speech handlers, or adds or removes a speech handler to or from the player. |  |
| [GMPAGE](GMPAGE "wikilink")*.n.DELETE* | W | Deletes the nth GM page. (zero-based) |  |
| [GMPAGE](GMPAGE "wikilink")*.n.HANDLE* | W | Sets the player as the handler for the nth GM page. (zero-based) |  |
| [GMPAGE](GMPAGE "wikilink")*.n.key* | W | Executes the .page command with *key* as the arguments. |  |
| [ISDSPEECH](ISDSPEECH "wikilink")*.speech_id* | R | Returns 1 if the player has the given speech handler attached. |  |
| [KICK](KICK "wikilink") | W | Disconnects and blocks the player's account. |  |
| [KILLS](KILLS "wikilink") | RW | Gets the number of murders the player has committed. |  |
| [KRTOOLBARSTATUS](KRTOOLBARSTATUS "wikilink") | RW | Gets or sets whether or not the KR toolbar is enabled for this player. |  |
| [LASTUSED](LASTUSED "wikilink") | RW | Gets the length of time since the player was last attached to a client, in seconds. |  |
| [PASSWORD](PASSWORD "wikilink") | W | Sets or clears the player's password. |  |
| [PFLAG](PFLAG "wikilink") | RW | Gets or sets the player's PFLAG value. |  |
| [PROFILE](PROFILE "wikilink") | RW | Gets or sets the text to display on the player's profile. |  |
| [SKILLLOCK](SKILLLOCK "wikilink")*.skill_id* | RW | Gets or sets the lock state of the player's skill. 0 is Up. 1 is Down. 2 is Locked. |  |
| [SPEEDMODE](SPEEDMODE "wikilink") | RW | Gets or sets the speed that the player moves at. (0=Normal, 1=Double Speed on Foot, 2=Always walk, 3=Always Run on Foot/Always Walk on Mount, 4=Can not Walk or Run) |  |
| [STATLOCK](STATLOCK "wikilink")''.stat_id | RW | Gets or sets the lock state of the player's STR (0), DEX (2) or INT (1). \[0 = up, 1 = down, 2 = locked\] |  |
```

```
## NPCs
```

Characters that are not attached to an account are NPCs and are controlled by Sphere's AI. In addition to the basic character references, properties and functions they also receive the following:

```
### Properties and Functions
```

Here is a list of all NPC properties and functions. If a function is marked as readable then it can return a value when used as <KEY>. Click on the name for more detailed information such as usage and examples.

```
|  |  |  |  |
|----|----|----|----|
| **Name** | **Read/Write** | **Description** | **Sphere X only?** |
| [ACTPRI](ACTPRI "wikilink") | RW | Gets or sets the NPC's motivation towards their current action. |  |
| [BUY](BUY "wikilink") | W | Displays the shop window to SRC, in buy mode. |  |
| [BYE](BYE "wikilink") | W | Ends the NPC's current action. |  |
| [FLEE](FLEE "wikilink") *distance* | W | Begins moving the NPC away from its current location. |  |
| [GOTO](GOTO "wikilink") *location* | W | Begins moving the NPC towards the specified location. |  |
| [HIRE](HIRE "wikilink") | W | Begins the hiring process between the NPC and SRC. |  |
| [LEAVE](LEAVE "wikilink") *distance* | W | Begins moving the NPC away from its current location. |  |
| [NPC](NPC "wikilink") | RW | Gets or sets the NPC's AI type. |  |
| [HOMEDIST](HOMEDIST "wikilink") | RW | Gets or sets the distance that the NPC can wander from its [HOME](HOME "wikilink") position. |  |
| [PETRETRIEVE](PETRETRIEVE "wikilink") | W | Enables SRC to retrieve their stabled pets from the NPC. |  |
| [PETSTABLE](PETSTABLE "wikilink") | W | Enables SRC to stable their pet with the NPC. |  |
| [RESTOCK](RESTOCK "wikilink") *force* | W | Clears all of the NPC's stock, repopulating it when it is next accessed (or immediately if *force*=1) |  |
| [RUN](RUN "wikilink") *direction* | W | Forces the NPC to run one tile in the specified direction. |  |
| [SELL](SELL "wikilink") | W | Displays the shop window to SRC, in sell mode. |  |
| [SHRINK](SHRINK "wikilink") | W | Shrinks the NPC into a figurine item. |  |
| [SPEECH](SPEECH "wikilink") *+/-speech_id* | RW | Gets the list of speech handlers attached to the NPC, or adds or removes a speech handler to or from the NPC. |  |
| [SPEECHCOLOR](SPEECHCOLOR "wikilink") | RW | Gets or sets the colour of the NPC's speech. |  |
| [THROWDAM](THROWDAM "wikilink") *min,max* | RW | Gets or sets a range of damage used for thrown objects. (overrides chardef property) |  |
| [THROWDAM](THROWDAM "wikilink") *dam* | RW | Gets or sets the constant damage used for thrown objects. (overrides chardef property) |  |
| [THROWDAMTYPE](THROWDAMTYPE "wikilink") *damage flags* | RW | y | Gets or sets the damage flags used for thrown objects. (overrides chardef property) |
| [THROWOBJ](THROWOBJ "wikilink") *id* | RW | Gets or sets the ID of an object to be thrown by NPCs. (overrides chardef property) |  |
| [THROWRANGE](THROWRANGE "wikilink") *min,max* | RW | Gets or sets the range that an object can be thrown at. (overrides chardef property) |  |
| [THROWRANGE](THROWRANGE "wikilink") *max* | RW | Gets or sets the range that an object can be thrown at with a default min of 2. (overrides chardef property) |  |
| [TRAIN](TRAIN "wikilink") *skill* | W | Initiates training between the NPC and SRC. |  |
| [VENDCAP](VENDCAP "wikilink") | RW | Gets or sets the amount of gold a vendor will restock to. |  |
| [VENDGOLD](VENDGOLD "wikilink") | RW | Gets or sets the amount of gold a vendor has. |  |
| [WALK](WALK "wikilink") *direction* | W | Forces the NPC to walk one tile in the specified direction. |  |
```

```
## Clients
```

When a client is controlling a character, the following references, properties and functions will be available:

```
### References
```

References return pointers to other objects (e.g. the REGION referenceallows you to access the REGION that an object is in). These can either be accessed by using *\<REFNAME\>* to return the [UID](UID "wikilink") (1 for object types that don't have UIDs) of the object or 0 if it doesn't exist, or by using *\<REFNAME.KEY\>* where KEY is a valid property/function/reference for the *REFNAME* object. Click on the name for more detailed information such as usage and examples.

```
|  |  |  |  |
|----|----|----|----|
| **Name** | **Read/Write** | **Description** | **Sphere X only?** |
| [GMPAGEP](GMPAGEP "wikilink") | R | Gets the [GM page](GM_Pages "wikilink") that the client is currently handling. |  |
| [HOUSEDESIGN](HOUSEDESIGN "wikilink") | R | Gets the [building](Special_Items#Customizable_Multis "wikilink") that is currently being designed by the client. |  |
| [PARTY](PARTY "wikilink") | R | Gets the [party](Parties "wikilink") that the client is a member of. |  |
| [TARG](TARG "wikilink") | RW | Gets or sets the [character](Characters "wikilink") or [item](Items "wikilink") that the client has targeted. |  |
| [TARGP](TARGP "wikilink") | RW | Gets or sets the [location](Map_Points "wikilink") that the client has targeted. |  |
| [TARGPROP](TARGPROP "wikilink") | RW | Gets or sets the character whose skills are shown in the client's skill menu. |  |
| [TARGPRV](TARGPRV "wikilink") | RW | Gets or sets the [character](Characters "wikilink") or [item](Items "wikilink") that the client previously targeted. |  |
```

```
### Properties and Functions
```

Here is a list of all client properties and functions. If a function is marked as readable then it can return a value when used as <KEY>. Click on the name for more detailed information such as usage and examples.

```
|  |  |  |  |
|----|----|----|----|
| **Name** | **Read/Write** | **Description** | **Sphere X only?** |
| [ADD](ADD "wikilink") *item_defname* | W | Prompts the client to target a location to add the specified item at. |  |
| [ADDBUFF](ADDBUFF "wikilink") *icon, cliloc1, cliloc2, time, arg1, arg2, arg3* | W | Displays a buff icon in the client's buff icon bar. |  |
| [ADDCLILOC](ADDCLILOC "wikilink") *cliloc, args* | W | Adds a cliloc to the tooltip being sent to the client. Only valid in @ClientTooltip triggers. |  |
| [ADDCONTEXTENTRY](ADDCONTEXTENTRY "wikilink") *entry_id, cliloc, flags, colour* | W | Adds an entry to the context menu being sent to the client. Only valid in @ContextMenuRequest triggers. |  |
| [ALLMOVE](ALLMOVE "wikilink") | RW | Gets or sets whether or not the client has ALLMOVE privileges. |  |
| [ALLSHOW](ALLSHOW "wikilink") | RW | Gets or sets whether or not the client is able to see disconnected characters. |  |
| [ARROWQUEST](ARROWQUEST "wikilink") *x, y, id* | W | Displays an arrow on the client's screen that points to the specified world coordinates. If id is supplied multiple arrows can be displayed on the client at once (Newer clients only - 3.x+ clients confirm?). You can cancel the arrow by passing 0 for x and y and your id. Using ARROWQUEST without any arguments will cancel arrow with id 0 if present. |  |
| [BADSPAWN](BADSPAWN "wikilink") | W | Teleports the client to the first invalid spawn point in the world. |  |
| [BANKSELF](BANKSELF "wikilink") | W | Opens up the client's bankbox. |  |
| [CAST](CAST "wikilink") ''spell_id' | W | Begins casting a spell. |  |
| [CHARLIST](CHARLIST "wikilink") | W | Displays the client's character list screen. |  |
| [CLEARCTAGS](CLEARCTAGS "wikilink") | W | Removes all of the client's CTAGs. |  |
| [CLIENTIS3D](CLIENTIS3D "wikilink") | R | Returns 1 if the client is using the 3D client. |  |
| [CLIENTISKR](CLIENTISKR "wikilink") | R | Returns 1 if the client is using the KR client. |  |
| [CLIENTVERSION](CLIENTVERSION "wikilink") | R | Gets the client version the client is using, based on the encryption keys being used (unencrypted clients return 0). |  |
| [CTAG](CTAG "wikilink") | RW | Gets or sets the value of a CTAG. |  |
| [CTAGCOUNT](CTAGCOUNT "wikilink") | R | Gets the number of CTAGs stored on the client. |  |
| [CTAGLIST](CTAGLIST "wikilink") | W | Displays a list of the client's CTAGs to SRC. |  |
| [CTAGLIST](CTAGLIST "wikilink") LOG | W | Displays a list of the client's CTAGs on the server console. |  |
| [DEBUG](DEBUG "wikilink") | RW | Gets or sets whether or not the client is in debug mode. |  |
| [DETAIL](DETAIL "wikilink") | RW | Gets or sets whether or not the client receives additional detail, such as combat messages. |  |
| [EVERBTARG](EVERBTARG "wikilink") *command* | W | Prompts the client to enter a command, or arguments to the command if specified. The complete command with arguments is then executed on TARG. |  |
| [EXTRACT](EXTRACT "wikilink") *file, template_id* | W | Extracts static items from a targeted area on the map and saves them into the specified file. |  |
| [FLUSH](FLUSH "wikilink") | W | Forces queued network data to be immediately sent to the client. |  |
| [GM](GM "wikilink") | RW | Gets or sets whether or not the client is in GM mode. |  |
| [GMPAGE](GMPAGE "wikilink") *ADD message* | W | Sends a GM page from the client with the specified message, or if no arguments provided will prompt the client for a message. |  |
| [GOTARG](GOTARG "wikilink") | W | Teleports the client to their targeted item. |  |
| [HEARALL](HEARALL "wikilink") | RW | Gets or sets whether or not the client can hear all player speech regardless of location. |  |
| [INFO](INFO "wikilink") | W | Displays an information dialog to the client for an object they target. |  |
| [INFORMATION](INFORMATION "wikilink") | W | Displays server information to the client. |  |
| [LAST](LAST "wikilink") | W | Forces the client to target the object referenced by [ACT](ACT "wikilink"). |  |
| [LASTEVENT](LASTEVENT "wikilink") | RW | Returns the time when data was last received from the client. |  |
| [LINK](LINK "wikilink") | W | Allows the client to target two objects to link them together. |  |
| [MENU](MENU_(Function) "wikilink") *menu_id* | W | Displays a menu to the client. |  |
| [MIDILIST](MIDILIST "wikilink") *music1, music2, ...* | W | Selects a random music id from the given list and tells the client to play it. |  |
| [NUDGE](NUDGE "wikilink") *dx, dy, dz* | W | Allows the client to nudge an area of items by the given coordinates, relative to the items' position. |  |
| [NUKE](NUKE "wikilink") *command* | W | Allows the client to execute *command* on all items in a targeted area. |  |
| [NUKECHAR](NUKECHAR "wikilink") *command* | W | Allows the client to execute *command* on all NPCs in a targeted area. |  |
| [PAGE](PAGE "wikilink") | W | Displays the GM page menu to the client. |  |
| [PRIVSHOW](PRIVSHOW "wikilink") | W | Gets or sets whether or not the client's privilege level should show in their name. |  |
| [REMOVEBUFF](REMOVEBUFF "wikilink") *icon* | W | Removes a buff icon from the client's buff icon bar. |  |
| [REPAIR](REPAIR "wikilink") | W | Prompts the client to target an item for them to repair. |  |
| [REPORTEDCLIVER](REPORTEDCLIVER "wikilink") | R | Gets the client version the client is using, based on what it has identified itself as to the server. |  |
| [REPORTEDCLIVER](REPORTEDCLIVER "wikilink").FULL | R | Gets the client version the client is using, based on what it has identified itself as to the server, including the 4th digit. |  |
| [RESEND](RESEND "wikilink") | W | Forces a full refresh of the client's screen. |  |
| [SAVE](SAVE "wikilink") *immediate* | W | Begins a world save. If background saving is enabled then *[SAVE](SAVE "wikilink") 1* will force a foreground save. |  |
| [SCREENSIZE](SCREENSIZE "wikilink") | R | Gets the client's screen size. (width,height) |  |
| [SCREENSIZE](SCREENSIZE "wikilink").X | R | Gets the width of the client's screen size. |  |
| [SCREENSIZE](SCREENSIZE "wikilink").Y | R | Gets the height of the client's screen size. |  |
| [SCROLL](SCROLL "wikilink") *scroll_id* | W | Displays a message scroll to the client. |  |
| [SELF](SELF "wikilink") | W | Forces the client to target itself. |  |
| [SENDPACKET](SENDPACKET "wikilink") *data* | W | Sends a raw data packet to the client. |  |
| [SET](SET "wikilink") *command* | W | Prompts the client to target an object to execute *command* on. |  |
| [SHOWSKILLS](SHOWSKILLS "wikilink") | W | Refreshes the client's skills for the skill menu. |  |
| [SKILLMENU](SKILLMENU_(Function) "wikilink") *skillmenu_id* | W | Displays a skillmenu to the client. |  |
| [SKILLSELECT](SKILLSELECT "wikilink") *skill_id* | W | Simulates the client selecting a skill from their skill menu. |  |
| [SUMMON](SUMMON "wikilink") *character_id* | W | Casts the summon spell, with ''character_id'; being the character to summon. |  |
| [SYSMESSAGE](SYSMESSAGE "wikilink") *text* | W | Displays a system message to the client. |  |
| [SYSMESSAGELOC](SYSMESSAGELOC "wikilink") *hue, cliloc, args* | W | Displays a localized system message to the client. |  |
| [SYSMESSAGELOCEX](SYSMESSAGELOCEX "wikilink") *hue, cliloc, flags, affix, args* | W | Displays a localized system message to the client with affixed text. |  |
| [SYSMESSAGEUA](SYSMESSAGEUA "wikilink") *hue, font, mode, language, text* | W | Displays a UNICODE system message to the client. |  |
| [TARGETTEXT](TARGETTEXT "wikilink") | RW | Gets or sets the client's target text. |  |
| [TELE](TELE "wikilink") | W | Casts the teleport spell. |  |
| [TILE](TILE "wikilink") *z, item1, item2, ...* | W | Tiles the ground within a targeted area with the listed items, at the given Z level. |  |
| [UNEXTRACT](UNEXTRACT "wikilink") *file* | W | Unextracts previously extracted statics, as dynamic items at a targeted location. |  |
| [VERSION](VERSION "wikilink") | W | Displays the server description to the client. |  |
| [WEBLINK](WEBLINK "wikilink") *url* | W | Opens the client's web browser to send them to the specified url. |  |
| [X](X "wikilink")*command* | W | Prompts the client to target an object to execute *command* on. |  |
```

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Objects](Category:_Objects "wikilink")
```
