 Generally speaking, there are two types of "things" in the game; characters and items. Compared to characters, items are very complex. Items have a number of different uses, for example a sword is an item that players can see and equip to increase the damage they can do in combat. Some items in the game can not be seen by the players, but they have as much impact on the player as their sword, for example, a memory item is equipped every time a player is under the effects of a spell. Some [special types of item](Special_Items "wikilink") also have additional properties that can be accessed via scripts. The following tables detail the various properties of items in SphereServer:

## References

References return pointers to other objects (e.g. the REGION referenceallows you to access the REGION that an object is in). These can either be accessed by using *\<REFNAME\>* to return the [UID](UID "wikilink") (1 for object types that don't have UIDs) of the object or 0 if it doesn't exist, or by using *\<REFNAME.KEY\>* where KEY is a valid property/function/reference for the *REFNAME* object. Click on the name
```
for more detailed information such as usage and examples.

```
|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [CONT](CONT "wikilink") | RW | Gets or sets the [character](Characters "wikilink") or [container item](Special_Items#Containers "wikilink") that the object is inside. When an item's CONT is changed, it bypasses the typical behavior (for example, you can force an item to be "in" a container and bypass @dropon triggers, or force an item to be equipped to a player and bypass @equiptest and @equip triggers -- but be careful, because in this second scenario it may end up in an invalid layer.) |
| [LINK](LINK "wikilink") | RW | Gets or sets the [character](Characters "wikilink") or [item](Items "wikilink") that the item is linked to. Note, you can make circular LINK's, but a single item cannot be linked to more than one other item. |
| [REGION](Regions "wikilink") | R | Gets the [region](Regions "wikilink") that the object is in. |
| [ROOM](ROOM "wikilink") | R | Gets the [room](Rooms "wikilink") that the object is in. |
| [P](P "wikilink") | RW | Gets or sets the [position](Map_Points "wikilink") that the object is at. |
| [SECTOR](Sectors "wikilink") | R | Gets the [sector](Sectors "wikilink") that the object is in. |
| [TOPOBJ](TOPOBJ "wikilink") | R | Gets the top-most [character](Characters "wikilink") or [item](Items "wikilink") in the world that contains the item. |
| [TYPEDEF](TYPEDEF_(Reference) "wikilink") | R | Gets the [ITEMDEF](ITEMDEF "wikilink") that defines the item. |
```

```
## Properties and Functions
```

Here is a list of all item properties and functions. If a function is marked as readable then it can return a value when used as <KEY>. Click on the name for more detailed information such as usage and examples. If an attempt is made to access a property that does not exist on the item, the property from the [ITEMDEF](ITEMDEF "wikilink") will be accessed instead.

```
| Name | **Read/Write** | **Description** |
| --- | --- | --- |
| [ADDCIRCLE](ADDCIRCLE) *spell_circle* | W | Adds all of the spells in the given Magery circle to the spellbook. |
| [ADDSPELL](ADDSPELL) *spell_id* | RW | Gets whether or not a spell exists in the spellbook, or adds a spell to the spellbook. |
| [AMMOANIM](AMMOANIM) | RW | Overrides TDATA4 for bow/crossbow type weapons. |
| [AMMOANIMHUE](AMMOANIMHUE) | RW | Sets the color of the effect when firing bow/crossbow type weapons. |
| [AMMOANIMRENDER](AMMOANIMRENDER) | RW | Sets the render mode of the effect when firing bow/crossbow type weapons. |
| [AMMOCONT](AMMOCONT) | RW | Sets the container UID or ID where to search for ammos for bow/crossbow type weapons. |
| [AMMOSOUNDHIT](AMMOSOUNDHIT) | RW | Overrides the hit sound on weapons. |
| [AMMOSOUNDMISS](AMMOSOUNDMISS) | RW | Overrides the miss sound on weapons. |
| [AMMOTYPE](AMMOTYPE) | RW | Overrides TDATA3 for bow/crossbow type weapons. |
| [AMOUNT](AMOUNT) | RW | Gets the amount of items this icon represents (e.g. a pile of gold or any stacked item). |
| [ATTR](ATTR) | RW | Gets or sets the item's attribute flags. |
| [BOUNCE](BOUNCE) | W | Moves the item to SRC's backpack (triggering the *you put the item in your pack* message. || [CAN](CAN) | RW | Gets or Sets the can_flags (Setting can be only done in the Itemdef itself). Only readable in X branch. |
| [CANMASK](CANMASK) | RW | Stores the CAN flags to be dynamically switched on or off from the base CAN property. |
| [CANSEE](CANSEE) | R | Returns 1 if SRC can see the item. |
| [CANSEELOS](CANSEELOS) *point_or_uid* | R | Returns 1 if SRC has line of sight to the item or character (uid) or point (location). |
| [CANSEELOSFLAG](CANSEELOSFLAG) *flags,point_or_uid* | R | Returns 1 if SRC has line of sight to the item. The *flags* are defined in the los_flags section of the sphere_defs.scp file and can be used to modify what tests take place. The *point_or_uid* is an object or position that can be used to test line of sight to something other than SRC. Note, the delimiter for FLAG values is |
| [CLEARTAGS](CLEARTAGS) *prefix* | W | Removes all TAGs from the item that start with the given prefix. |
| [COLOR](COLOR) | RW | Gets or sets the object's hue. |
| [CONSUME](CONSUME) *amount* | W | Deducts an amount from the item, deleting it at 0. |
| [CONTCONSUME](CONTCONSUME) *resource_list* | W | Deletes items from inside the container. |
| [CONTGRID](CONTGRID) | RW | If in a container, gets or sets the grid number that the item occupies (in KR's grid view) |
| [CONTP](CONTP) | RW | Gets or sets the position of the item within its container. |
| [DAMAGE](DAMAGE) *chance, type, source* | W | If *chance* is greater than (Rand(maxhits*16)), inflicts damage of *type* (the damage type flags are defined in the sphere_defs.scp file) upon the item. You can optionally specify the *source* of the damage. |
| [DCLICK](DCLICK) | W | Double clicks the item, with SRC as the source of the event. |
| [DECAY](DECAY) *time* | W | Sets the decay timer (in tenths of a second) for the item. |
| [DESTROY](DESTROY) | W | Deletes the object, not stopped by a return 1 in [@Destroy](@Destroy) |
| [DIALOG](DIALOG_(Function)) *dialog_id, page, parameters* | W | Displays a dialog to SRC. |
| [DISPID](DISPID) | RW | Gets or sets the ID that the item will appear as to players. |
| [DISPIDDEC](DISPIDDEC) | RW | Same as [DISPID](DISPID), except it returns the ID as a decimal number. |
| [DISTANCE](DISTANCE) *point_or_uid* | R | Gets the distance between this object and SRC. If *point_or_uid* is used, SRC can be replaced with a map location or another object. |
| [DMGCOLD](DMGCOLD) | RW | Gets or sets the amount of cold damage the weapon will give. |
| [DMGENERGY](DMGENERGY) | RW | Gets or sets the amount of energy damage the weapon will give. |
| [DMGFIRE](DMGFIRE) | RW | Gets or sets the amount of fire damage the weapon will give. |
| [DMGPOISON](DMGPOISON) | RW | Gets or sets the amount of poison damage the weapon will give. |
| [DROP](DROP) | W | Drops the item to the ground. |
| [DUPE](DUPE) | W | Clones the item. |
| [EDIT](EDIT) | W | Displays an editing dialog for the item to SRC. |
| [EFFECT](EFFECT) *type, item_id, speed, loop, explode, colour, rendermode* | W | Displays an effect to nearby clients. |
| [EMOTE](EMOTE) *message* | W | Displays a *You see* message to all nearby clients. |
| [EQUIP](EQUIP) | W | Equips the item to SRC. |
| [EVENTS](EVENTS_(Property)) *event_defname* | RW | Gets a list of events attached to the object, or adds or removes an event to or from the object. |
| [FIX](FIX) | W | Re-aligns the item or character's Z level to ground level (if items are on the ground, the top item's *Z+HEIGHT* is used). |
| [FLIP](FLIP) | W | Rotates the item clockwise. |
| [FRUIT](FRUIT) | RW | Gets or sets the fruit that will be produced by the crops. |
| [HEIGHT](HEIGHT) | R | Gets the height of the item. |
| [HITS](HITS) | RW | Gets or sets the number of hitpoints the item has. |
| [HITPOINTS](HITPOINTS) | RW | Gets or sets the number of hitpoints the item has. |
| [ID](ID) | RW | Gets or sets the ID of the item. |
| [INFO](INFO) | W | Displays an information dialog about the item to SRC. |
| [ISARMOR](ISARMOR) *object_uid* | R | Returns 1 if the object is armour. |
| [ISCHAR](ISCHAR) | R | Returns 1 if the object is a character. |
| [ISCONT](ISCONT) | R | Returns 1 if the object is a container. |
| [ISEVENT](ISEVENT)*.event_defname* | R | Returns 1 if the object has an event attached to it. |
| [ISITEM](ISITEM) | R | Returns 1 if the object is an item. |
| [ISNEARTYPE](ISNEARTYPE) *type, distance, flags* | R | Returns 1 if a nearby item has the given TYPE and is within *distance*. |
| [ISNEARTYPETOP](ISNEARTYPETOP) *type, distance, flags* | R | Returns a nearby world location of a nearby item which has the given TYPE and is within *distance*. |
| [ISPLAYER](ISPLAYER) | R | Returns 1 if the object is a player character. |
| [ISTEVENT](ISTEVENT)*.event_defname* | R | Returns 1 if the object has an event attached to its ITEMDEF. |
| [ISTIMERF](ISTIMERF)*.function* | R | Returns the number of seconds left on the specified timerf if it exists. |
| [ISWEAPON](ISWEAPON) *object_uid* | R | Returns 1 if the object is a weapon. |
| [LAYER](LAYER) | RW | Gets or sets the layer that the item occupies when equipped (possible layers are defined in the sphere_defs.scp file). |
| [MAP](MAP) | RW | Gets or sets the map that this object is located. |
| [MAXHITS](MAXHITS) | RW | Gets or sets the maximum number of hitpoints the item can have. |
| [MENU](MENU_(Function)) *menu_defname* | W | Displays a menu to SRC. |
| [MESSAGE](MESSAGE) *message* | W | Displays a message above this item to SRC. |
| [MESSAGEUA](MESSAGEUA) *colour, talkmode, font, lang_id, message* | W | Displays a UNICODE message above this item to SRC. |
| [MODAR](MODAR) | RW | Gets or sets a modifier for the item's armour rating if it is clothing, armor, or a shield. This gets or sets a modifier for the item's damage if it is a weapon type. |
| [MORE1](MORE1) | RW | Gets or sets the MORE1 value for the item. |
| [MORE1H](MORE1H) | RW | Gets or sets the upper 4 bytes of the item's MORE1 value. |
| [MORE1L](MORE1L) | RW | Gets or sets the lower 4 bytes of the item's MORE1 value. |
| [MORE2](MORE2) | RW | Gets or sets the MORE2 value for the item. |
| [MORE2H](MORE2H) | RW | Gets or sets the upper 4 bytes of the item's MORE2 value. |
| [MORE2L](MORE2L) | RW | Gets or sets the lower 4 bytes of the item's MORE2 value. |
| [MOREM](MOREM) | RW | Gets or sets the MOREM value for the item. |
| [MOREX](MOREX) | RW | Gets or sets the MOREX value for the item. |
| [MOREY](MOREY) | RW | Gets or sets the MOREY value for the item. |
| [MOREZ](MOREZ) | RW | Gets or sets the MOREZ value for the item. |
| [MOREP](MOREP) | RW | Gets or sets the MOREP value for the item. |
| [MOVE](MOVE) *direction amount* [MOVE](MOVE) *x y* | W | Moves the object relative to its current position. Possible *direction* values are N,S,W, or E. Note, you can combine directions (like: MOVE SW 1) but nonsensical directions (like: MOVE WE 2) have the nonsense removed. |
| [MOVENEAR](MOVENEAR) *object_uid, distance* | W | Moves the object to a random location near another object within a certain distance. |
| [MOVETO](MOVETO) *location* | W | Moves the object to a specific location (note, the AREADEF or ROOMDEF must have a P defined). |
| [NAME](NAME) | RW | Gets or sets the object's name. |
| [NUDGEDOWN](NUDGEDOWN) *amount* | W | Decreases the object's Z level. |
| [NUDGEUP](NUDGEUP) *amount* | W | Increases the object's Z level. |
| [PROMPTCONSOLE](PROMPTCONSOLE) *function, prompt_message* | W | Displays a prompt message to SRC and passes their response into a specified function. |
| [PROMPTCONSOLEU](PROMPTCONSOLEU) *function, prompt_message* | W | Displays a prompt message to SRC and passes their response into a specified function, supporting UNICODE response. |
| [REMOVE](REMOVE) | W | Deletes the object. |
| [REMOVEFROMVIEW](REMOVEFROMVIEW) | W | Removes the object from nearby clients' screens. |
| [RESCOUNT](RESCOUNT) *item_defname* | R | Returns the total amount of a specific item inside a container. |
| [RESENDTOOLTIP](RESENDTOOLTIP) | W | Forces Sphere to update the tooltips for nearby clients. |
| [SAY](SAY) *message* | W | Makes the object speak a message. |
| [SAYU](SAYU) *message* | W | Makes the object speak a UTF-8 message |
| [SAYUA](SAYUA) *colour, talkmode, font, lang_id, text* | W | Makes the object speak a UNICODE message. |
| [SDIALOG](SDIALOG) *dialog_id, page, parameters* | W | Displays a dialog to SRC, providing that it is not already open. |
| [SERIAL](SERIAL) | R | Gets the item's unique ID in the world. |
| [SEXTANTP](SEXTANTP) *location* | R | Converts the item's location or a specified location into sextant coordinates. |
| [SOUND](SOUND) *sound_id, repeat* | W | Plays a sound from this object. |
| [SPELLEFFECT](SPELLEFFECT) *spell_id, strength, source_character_uid, source_item_uid* | W | Causes the item to be affected by a spell. |
| [TAG](TAG)*.name* | RW | Gets or sets the value of a TAG. |
| [TAGAT](TAGAT)*.index* | R | Gets a TAG at the given zero-based index. |
| [TAGAT](TAGAT)*.index*.KEY | R | Gets the name of the TAG at the given zero-based index. |
| [TAGAT](TAGAT)*.index*.VAL | R | Gets the value of the TAG at the given zero-based index. |
| [TAGCOUNT](TAGCOUNT) | R | Gets the number of TAGs stored on the item. |
| [TAGLIST](TAGLIST) | W | Outputs a list of the object's TAGs. |
| [TARGET](TARGET)*FGMW* *function* | W | Displays a targeting cursor to SRC. *F* makes the *function* available, and when added, the function name must be the 1st argument. *M* allows you to place a *multi* item, in which case the multi number must be passed as an argument. *G* forces the target to only be the ground. *W* checks the criminal status of the player before (or after?) the target selection is made. |
| [TIMER](TIMER) | RW | Gets or sets the length of time before the item's timer expires, in seconds. |
| [TIMERD](TIMERD) | RW | Gets or sets the length of time before the item's timer expires, in tenths of a second. |
| [TIMERF](TIMERF) *time, function* | W | Schedules a function to be executed on this object in *time* seconds. |
| [TIMERF](TIMERF) *CLEAR* | W | Clears all scheduled functions from the object. |
| [TIMERF](TIMERF) *STOP, function* | W | Stops the specified function from the item. (On X version wild character * is available for defining the function name or the argument) |
| [TRIGGER](TRIGGER) *trig_name, trigger_argtype, argument1, argument2, ...* | R | Fires a custom trigger (trig_name), allowing you to define the behavior of the arguments (the types are defined under trigger_argtype in the sphere_defs.scp file). The result of the trigger's RETURN value is returned. For example: `LOCAL.result=&lt;TRIGGER @CustomTrigger,&lt;DEF.tat_as_argn&gt;,1,2,3&gt;` |
| [TYPE](TYPE) | RW | Gets or sets the item type. You can use built-in or custom [TYPEDEFs](TYPEDEF) as a value. |
| [UID](UID) | R | Gets the item's unique ID in the world. |
| [UNEQUIP](UNEQUIP) | W | Unequips the item and places it in SRC's backpack. |
| [UPDATE](UPDATE) | W | Updates the state of the item to nearby clients. |
| [UPDATEX](UPDATEX) | W | Updates the state of the item to nearby clients, removing it from their view first to ensure a full refresh. |
| [USESCUR](USESCUR) | W | X branch only. Gets or sets the current uses of an item. Only partially supported. |
| [USESMAX](USESMAX) | W | X branch only. Gets or sets the maximum uses of an item. Only partially supported. |
| [USE](USE) *check_los* | W | Uses the item, as if SRC had double clicked it. |
| [USEITEM](USEITEM) | W | Double clicks the item, with SRC as the source of the event, without checking for line of sight. |
| [WEIGHT](WEIGHT) | R | Gets the weight of the item. |
| [Z](Z) | R | Gets the Z position of the item. |
```

```
## Triggers
```

Here is a list of all item triggers. Click on the trigger name for more detailed information such as arguments and examples.

```
|  |  |  |
|----|----|----|
| **Name** | **Description** | **Sphere X Only?** |
| [@AfterClick](@AfterClick "wikilink") | Fires when the object has been single-clicked, just before the overhead name is shown. |  |
| [@Buy](@Buy "wikilink") | Fires when the item is being bought from a vendor. |  |
| [@Click](@Click "wikilink") | Fires when the object has been single-clicked. |  |
| [@ClientTooltip](@ClientTooltip "wikilink") | Fires when tooltips are about to be sent to a client. |  |
| [@ContextMenuRequest](@ContextMenuRequest "wikilink") | Fires when a client requests the context menu options for the object. |  |
| [@ContextMenuSelect](@ContextMenuSelect "wikilink") | Fires when a client selects a context menu option for the object. |  |
| [@Carve](@Carve "wikilink") | Fires when a corpse item is being carved. | X |
| [@Create](@Create "wikilink") | Fires when the object is initially created, before it is placed in the world. |  |
| [@Damage](@Damage "wikilink") | Fires when the item receives damage. |  |
| [@DClick](@DClick "wikilink") | Fires when the object is double-clicked. |  |
| [@Destroy](@Destroy "wikilink") | Fires when the object is being deleted. |  |
| [@DropOn_Char](@DropOn_Char "wikilink") | Fires when the item has been dropped on to a character. |  |
| [@DropOn_Ground](@DropOn_Ground "wikilink") | Fires when the item has been dropped on to the ground. |  |
| [@DropOn_Item](@DropOn_Item "wikilink") | Fires when the item is dropped on to another item. |  |
| [@DropOn_Self](@DropOn_Self "wikilink") | Fires when an item has been dropped on to this item. |  |
| [@DropOn_Trade](@DropOn_Trade "wikilink") | Fires when an item is being dropped on a Trade Window. |  |
| [@Dye](@Dye "wikilink") | Fires when an item is having its colored changed. |  |
| [@Equip](@Equip "wikilink") | Fires when the item has been equipped. |  |
| [@EquipTest](@EquipTest "wikilink") | Fires when the item is about to be equipped. |  |
| [@HouseDesignBegin](@HouseDesignBegin "wikilink") | A trigger for t_multi_custom, called when the player enters on design mode. | X |
| [@HouseDesignCommitItem](@HouseDesignCommitItem "wikilink") | Fires for each commited item in house design system. | X |
| [@PickUp_Ground](@PickUp_Ground "wikilink") | Fires when the item ihas been picked up from the ground. |  |
| [@PickUp_Pack](@PickUp_Pack "wikilink") | Fires when the item is picked up from inside a container. |  |
| [@PickUp_Self](@PickUp_Self "wikilink") | Fires when an item has been picked up from inside the item. |  |
| [@PickUp_Stack](@PickUp_Stack "wikilink") | Fires when the item is picked up from a stack. |  |
| [@Redeed](@Redeed "wikilink") | Fires when multi item is about to redeed (t_multi, t_ship, t_multi_custom, t_addon). |  |
| [@Sell](@Sell "wikilink") | Fires when the item is sold to a vendor. |  |
| [@Smelt](@Smelt "wikilink") | Fires when the item is being smelt. | X |
| [@SpellEffect](@SpellEffect "wikilink") | Fires when the object is hit by the effects of a spell. |  |
| [@Step](@Step "wikilink") | Fires when a character steps on the item. |  |
| [@TargOn_Cancel](@TargOn_Cancel "wikilink") | Fires when a target is cancelled from the item. |  |
| [@TargOn_Char](@TargOn_Char "wikilink") | Fires when a character is targeted from the item. |  |
| [@TargOn_Ground](@TargOn_Ground "wikilink") | Fires when the ground is targeted from the item. |  |
| [@TargOn_Item](@TargOn_Item "wikilink") | Fires when an item is targeted from this item. |  |
| [@Timer](@Timer "wikilink") | Fires when the item's timer expires. |  |
| [@ToolTip](@ToolTip "wikilink") | Fires when old-style tooltips are requested for the item. |  |
| [@UnEquip](@UnEquip "wikilink") | Fires when the item is unequipped. |  |
```

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Objects](Category:_Objects "wikilink")
```
