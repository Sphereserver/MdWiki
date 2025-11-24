```{=mediawiki}
{{Languages|Items}}
```
\_\_FORCETOC\_\_ Generally speaking, there are two types of \"things\"
in the game; characters and items. Compared to characters, items are
very complex. Items have a number of different uses, for example a sword
is an item that players can see and equip to increase the damage they
can do in combat. Some items in the game can not be seen by the players,
but they have as much impact on the player as their sword, for example,
a memory item is equipped every time a player is under the effects of a
spell. Some [special types of item](Special_Items "wikilink") also have
additional properties that can be accessed via scripts. The following
tables detail the various properties of items in SphereServer:

## References

References return pointers to other objects (e.g. the REGION reference
allows you to access the REGION that an object is in). These can either
be accessed by using *\<REFNAME\>* to return the [UID](UID "wikilink")
(1 for object types that don\'t have UIDs) of the object or 0 if it
doesn\'t exist, or by using *\<REFNAME.KEY\>* where KEY is a valid
property/function/reference for the *REFNAME* object. Click on the name
for more detailed information such as usage and examples.

  ------------------------------------------- ---------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                                    **Read/Write**   **Description**
  [CONT](CONT "wikilink")                     RW               Gets or sets the [character](Characters "wikilink") or [container item](Special_Items#Containers "wikilink") that the object is inside. When an item\'s CONT is changed, it bypasses the typical behavior (for example, you can force an item to be \"in\" a container and bypass \@dropon triggers, or force an item to be equipped to a player and bypass \@equiptest and \@equip triggers \-- but be careful, because in this second scenario it may end up in an invalid layer.)
  [LINK](LINK "wikilink")                     RW               Gets or sets the [character](Characters "wikilink") or [item](Items "wikilink") that the item is linked to. Note, you can make circular LINK\'s, but a single item cannot be linked to more than one other item.
  [REGION](Regions "wikilink")                R                Gets the [region](Regions "wikilink") that the object is in.
  [ROOM](ROOM "wikilink")                     R                Gets the [room](Rooms "wikilink") that the object is in.
  [P](P "wikilink")                           RW               Gets or sets the [position](Map_Points "wikilink") that the object is at.
  [SECTOR](Sectors "wikilink")                R                Gets the [sector](Sectors "wikilink") that the object is in.
  [TOPOBJ](TOPOBJ "wikilink")                 R                Gets the top-most [character](Characters "wikilink") or [item](Items "wikilink") in the world that contains the item.
  [TYPEDEF](TYPEDEF_(Reference) "wikilink")   R                Gets the [ITEMDEF](ITEMDEF "wikilink") that defines the item.
  ------------------------------------------- ---------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Properties and Functions {#properties_and_functions}

Here is a list of all item properties and functions. If a function is
marked as readable then it can return a value when used as
`<KEY>`{=html}. Click on the name for more detailed information such as
usage and examples. If an attempt is made to access a property that does
not exist on the item, the property from the
[ITEMDEF](ITEMDEF "wikilink") will be accessed instead.

+-------------------------+----------------+-------------------------+
| Name                    | **Read/Write** | **Description**         |
+=========================+================+=========================+
| [ADDCIRCLE              | W              | Adds all of the spells  |
| ](ADDCIRCLE "wikilink") |                | in the given Magery     |
| *spell_circle*          |                | circle to the           |
|                         |                | spellbook.              |
+-------------------------+----------------+-------------------------+
| [ADDSPEL                | RW             | Gets whether or not a   |
| L](ADDSPELL "wikilink") |                | spell exists in the     |
| *spell_id*              |                | spellbook, or adds a    |
|                         |                | spell to the spellbook. |
+-------------------------+----------------+-------------------------+
| [AMMOANI                | RW             | Overrides TDATA4 for    |
| M](AMMOANIM "wikilink") |                | bow/crossbow type       |
|                         |                | weapons.                |
+-------------------------+----------------+-------------------------+
| [AMMOANIMHUE](          | RW             | Sets the color of the   |
| AMMOANIMHUE "wikilink") |                | effect when firing      |
|                         |                | bow/crossbow type       |
|                         |                | weapons.                |
+-------------------------+----------------+-------------------------+
| [AMMOANIMRENDER](AMM    | RW             | Sets the render mode of |
| OANIMRENDER "wikilink") |                | the effect when firing  |
|                         |                | bow/crossbow type       |
|                         |                | weapons.                |
+-------------------------+----------------+-------------------------+
| [AMMOCON                | RW             | Sets the container UID  |
| T](AMMOCONT "wikilink") |                | or ID where to search   |
|                         |                | for ammos for           |
|                         |                | bow/crossbow type       |
|                         |                | weapons.                |
+-------------------------+----------------+-------------------------+
| [AMMOSOUNDHIT](A        | RW             | Overrides the hit sound |
| MMOSOUNDHIT "wikilink") |                | on weapons.             |
+-------------------------+----------------+-------------------------+
| [AMMOSOUNDMISS](AM      | RW             | Overrides the miss      |
| MOSOUNDMISS "wikilink") |                | sound on weapons.       |
+-------------------------+----------------+-------------------------+
| [AMMOTYP                | RW             | Overrides TDATA3 for    |
| E](AMMOTYPE "wikilink") |                | bow/crossbow type       |
|                         |                | weapons.                |
+-------------------------+----------------+-------------------------+
| [AMO                    | RW             | Gets the amount of      |
| UNT](AMOUNT "wikilink") |                | items this icon         |
|                         |                | represents (e.g. a pile |
|                         |                | of gold or any stacked  |
|                         |                | item).                  |
+-------------------------+----------------+-------------------------+
| [ATTR](ATTR "wikilink") | RW             | Gets or sets the        |
|                         |                | item\'s attribute       |
|                         |                | flags.                  |
+-------------------------+----------------+-------------------------+
| [BOU                    | W              | Moves the item to       |
| NCE](BOUNCE "wikilink") |                | SRC\'s backpack         |
|                         |                | (triggering the *you    |
|                         |                | put the item in your    |
|                         |                | pack* message.          |
+-------------------------+----------------+-------------------------+
| [CAN](CAN "wikilink")   | RW             | Gets or Sets the        |
|                         |                | can_flags (Setting can  |
|                         |                | be only done in the     |
|                         |                | Itemdef itself). Only   |
|                         |                | readable in X branch.   |
+-------------------------+----------------+-------------------------+
| [CANMA                  | RW             | Stores the CAN flags to |
| SK](CANMASK "wikilink") |                | be dynamically switched |
|                         |                | on or off from the base |
|                         |                | CAN property.           |
+-------------------------+----------------+-------------------------+
| [CAN                    | R              | Returns 1 if SRC can    |
| SEE](CANSEE "wikilink") |                | see the item.           |
+-------------------------+----------------+-------------------------+
| [CANSEELOS              | R              | Returns 1 if SRC has    |
| ](CANSEELOS "wikilink") |                | line of sight to the    |
| *point_or_uid*          |                | item or character (uid) |
|                         |                | or point (location).    |
+-------------------------+----------------+-------------------------+
| [CANSEELOSFLAG](CA      | R              | Returns 1 if SRC has    |
| NSEELOSFLAG "wikilink") |                | line of sight to the    |
| *flags,point_or_uid*    |                | item. The *flags* are   |
|                         |                | defined in the          |
|                         |                | los_flags section of    |
|                         |                | the sphere_defs.scp     |
|                         |                | file and can be used to |
|                         |                | modify what tests take  |
|                         |                | place. The              |
|                         |                | *point_or_uid* is an    |
|                         |                | object or position that |
|                         |                | can be used to test     |
|                         |                | line of sight to        |
|                         |                | something other than    |
|                         |                | SRC. Note, the          |
|                         |                | delimiter for FLAG      |
|                         |                | values is ;             |
+-------------------------+----------------+-------------------------+
| [CLEARTAGS              | W              | Removes all TAGs from   |
| ](CLEARTAGS "wikilink") |                | the item that start     |
| *prefix*                |                | with the given prefix.  |
+-------------------------+----------------+-------------------------+
| [C                      | RW             | Gets or sets the        |
| OLOR](COLOR "wikilink") |                | object\'s hue.          |
+-------------------------+----------------+-------------------------+
| [CONSU                  | W              | Deducts an amount from  |
| ME](CONSUME "wikilink") |                | the item, deleting it   |
| *amount*                |                | at 0.                   |
+-------------------------+----------------+-------------------------+
| [CONTCONSUME](          | W              | Deletes items from      |
| CONTCONSUME "wikilink") |                | inside the container.   |
| *resource_list*         |                |                         |
+-------------------------+----------------+-------------------------+
| [CONTGRI                | RW             | If in a container, gets |
| D](CONTGRID "wikilink") |                | or sets the grid number |
|                         |                | that the item occupies  |
|                         |                | (in KR\'s grid view)    |
+-------------------------+----------------+-------------------------+
| [C                      | RW             | Gets or sets the        |
| ONTP](CONTP "wikilink") |                | position of the item    |
|                         |                | within its container.   |
+-------------------------+----------------+-------------------------+
| [DAM                    | W              | If *chance* is greater  |
| AGE](DAMAGE "wikilink") |                | than                    |
| *chance, type, source*  |                | (Rand(maxhits\*16)),    |
|                         |                | inflicts damage of      |
|                         |                | *type* (the damage type |
|                         |                | flags are defined in    |
|                         |                | the sphere_defs.scp     |
|                         |                | file) upon the item.    |
|                         |                | You can optionally      |
|                         |                | specify the *source* of |
|                         |                | the damage.             |
+-------------------------+----------------+-------------------------+
| [DCL                    | W              | Double clicks the item, |
| ICK](DCLICK "wikilink") |                | with SRC as the source  |
|                         |                | of the event.           |
+-------------------------+----------------+-------------------------+
| [D                      | W              | Sets the decay timer    |
| ECAY](DECAY "wikilink") |                | (in tenths of a second) |
| *time*                  |                | for the item.           |
+-------------------------+----------------+-------------------------+
| [DESTR                  | W              | Deletes the object, not |
| OY](DESTROY "wikilink") |                | stopped by a return 1   |
|                         |                | in                      |
|                         |                | [\@Destro               |
|                         |                | y](@Destroy "wikilink") |
+-------------------------+----------------+-------------------------+
| [DIALOG](DIALOG         | W              | Displays a dialog to    |
| _(Function) "wikilink") |                | SRC.                    |
| *dialog_id, page,       |                |                         |
| parameters*             |                |                         |
+-------------------------+----------------+-------------------------+
| [DIS                    | RW             | Gets or sets the ID     |
| PID](DISPID "wikilink") |                | that the item will      |
|                         |                | appear as to players.   |
+-------------------------+----------------+-------------------------+
| [DISPIDDEC              | RW             | Same as                 |
| ](DISPIDDEC "wikilink") |                | [DISP                   |
|                         |                | ID](DISPID "wikilink"), |
|                         |                | except it returns the   |
|                         |                | ID as a decimal number. |
+-------------------------+----------------+-------------------------+
| [DISTANC                | R              | Gets the distance       |
| E](DISTANCE "wikilink") |                | between this object and |
| *point_or_uid*          |                | SRC. If *point_or_uid*  |
|                         |                | is used, SRC can be     |
|                         |                | replaced with a map     |
|                         |                | location or another     |
|                         |                | object.                 |
+-------------------------+----------------+-------------------------+
| [DMGCO                  | RW             | Gets or sets the amount |
| LD](DMGCOLD "wikilink") |                | of cold damage the      |
|                         |                | weapon will give.       |
+-------------------------+----------------+-------------------------+
| [DMGENERGY              | RW             | Gets or sets the amount |
| ](DMGENERGY "wikilink") |                | of energy damage the    |
|                         |                | weapon will give.       |
+-------------------------+----------------+-------------------------+
| [DMGFI                  | RW             | Gets or sets the amount |
| RE](DMGFIRE "wikilink") |                | of fire damage the      |
|                         |                | weapon will give.       |
+-------------------------+----------------+-------------------------+
| [DMGPOISON              | RW             | Gets or sets the amount |
| ](DMGPOISON "wikilink") |                | of poison damage the    |
|                         |                | weapon will give.       |
+-------------------------+----------------+-------------------------+
| [DROP](DROP "wikilink") | W              | Drops the item to the   |
|                         |                | ground.                 |
+-------------------------+----------------+-------------------------+
| [DUPE](DUPE "wikilink") | W              | Clones the item.        |
+-------------------------+----------------+-------------------------+
| [EDIT](EDIT "wikilink") | W              | Displays an editing     |
|                         |                | dialog for the item to  |
|                         |                | SRC.                    |
+-------------------------+----------------+-------------------------+
| [EFF                    | W              | Displays an effect to   |
| ECT](EFFECT "wikilink") |                | nearby clients.         |
| *type, item_id, speed,  |                |                         |
| loop, explode, colour,  |                |                         |
| rendermode*             |                |                         |
+-------------------------+----------------+-------------------------+
| [E                      | W              | Displays a \*You see\*  |
| MOTE](EMOTE "wikilink") |                | message to all nearby   |
| *message*               |                | clients.                |
+-------------------------+----------------+-------------------------+
| [E                      | W              | Equips the item to SRC. |
| QUIP](EQUIP "wikilink") |                |                         |
+-------------------------+----------------+-------------------------+
| [EVENTS](EVENTS         | RW             | Gets a list of events   |
| _(Property) "wikilink") |                | attached to the object, |
| *event_defname*         |                | or adds or removes an   |
|                         |                | event to or from the    |
|                         |                | object.                 |
+-------------------------+----------------+-------------------------+
| [FIX](FIX "wikilink")   | W              | Re-aligns the item or   |
|                         |                | character\'s Z level to |
|                         |                | ground level (if items  |
|                         |                | are on the ground, the  |
|                         |                | top item\'s *Z+HEIGHT*  |
|                         |                | is used).               |
+-------------------------+----------------+-------------------------+
| [FLIP](FLIP "wikilink") | W              | Rotates the item        |
|                         |                | clockwise.              |
+-------------------------+----------------+-------------------------+
| [F                      | RW             | Gets or sets the fruit  |
| RUIT](FRUIT "wikilink") |                | that will be produced   |
|                         |                | by the crops.           |
+-------------------------+----------------+-------------------------+
| [HEI                    | R              | Gets the height of the  |
| GHT](HEIGHT "wikilink") |                | item.                   |
+-------------------------+----------------+-------------------------+
| [HITS](HITS "wikilink") | RW             | Gets or sets the number |
|                         |                | of hitpoints the item   |
|                         |                | has.                    |
+-------------------------+----------------+-------------------------+
| [HITPOINTS              | RW             | Gets or sets the number |
| ](HITPOINTS "wikilink") |                | of hitpoints the item   |
|                         |                | has.                    |
+-------------------------+----------------+-------------------------+
| [ID](ID "wikilink")     | RW             | Gets or sets the ID of  |
|                         |                | the item.               |
+-------------------------+----------------+-------------------------+
| [INFO](INFO "wikilink") | W              | Displays an information |
|                         |                | dialog about the item   |
|                         |                | to SRC.                 |
+-------------------------+----------------+-------------------------+
| [ISARM                  | R              | Returns 1 if the object |
| OR](ISARMOR "wikilink") |                | is armour.              |
| *object_uid*            |                |                         |
+-------------------------+----------------+-------------------------+
| [ISC                    | R              | Returns 1 if the object |
| HAR](ISCHAR "wikilink") |                | is a character.         |
+-------------------------+----------------+-------------------------+
| [ISC                    | R              | Returns 1 if the object |
| ONT](ISCONT "wikilink") |                | is a container.         |
+-------------------------+----------------+-------------------------+
| [ISEVENT](ISEVENT "wik  | R              | Returns 1 if the object |
| ilink")*.event_defname* |                | has an event attached   |
|                         |                | to it.                  |
+-------------------------+----------------+-------------------------+
| [ISI                    | R              | Returns 1 if the object |
| TEM](ISITEM "wikilink") |                | is an item.             |
+-------------------------+----------------+-------------------------+
| [ISNEARTYPE]            | R              | Returns 1 if a nearby   |
| (ISNEARTYPE "wikilink") |                | item has the given TYPE |
| *type, distance, flags* |                | and is within           |
|                         |                | *distance*.             |
+-------------------------+----------------+-------------------------+
| [ISNEARTYPETOP](IS      | R              | Returns a nearby world  |
| NEARTYPETOP "wikilink") |                | location of a nearby    |
| *type, distance, flags* |                | item which has the      |
|                         |                | given TYPE and is       |
|                         |                | within *distance*.      |
+-------------------------+----------------+-------------------------+
| [ISPLAYE                | R              | Returns 1 if the object |
| R](ISPLAYER "wikilink") |                | is a player character.  |
+-------------------------+----------------+-------------------------+
| [                       | R              | Returns 1 if the object |
| ISTEVENT](ISTEVENT "wik |                | has an event attached   |
| ilink")*.event_defname* |                | to its ITEMDEF.         |
+-------------------------+----------------+-------------------------+
| [ISTIMERF](ISTIMERF     | R              | Returns the number of   |
|  "wikilink")*.function* |                | seconds left on the     |
|                         |                | specified timerf if it  |
|                         |                | exists.                 |
+-------------------------+----------------+-------------------------+
| [ISWEAPO                | R              | Returns 1 if the object |
| N](ISWEAPON "wikilink") |                | is a weapon.            |
| *object_uid*            |                |                         |
+-------------------------+----------------+-------------------------+
| [L                      | RW             | Gets or sets the layer  |
| AYER](LAYER "wikilink") |                | that the item occupies  |
|                         |                | when equipped (possible |
|                         |                | layers are defined in   |
|                         |                | the sphere_defs.scp     |
|                         |                | file).                  |
+-------------------------+----------------+-------------------------+
| [MAP](MAP "wikilink")   | RW             | Gets or sets the map    |
|                         |                | that this object is     |
|                         |                | located.                |
+-------------------------+----------------+-------------------------+
| [MAXHI                  | RW             | Gets or sets the        |
| TS](MAXHITS "wikilink") |                | maximum number of       |
|                         |                | hitpoints the item can  |
|                         |                | have.                   |
+-------------------------+----------------+-------------------------+
| [MENU](MENU             | W              | Displays a menu to SRC. |
| _(Function) "wikilink") |                |                         |
| *menu_defname*          |                |                         |
+-------------------------+----------------+-------------------------+
| [MESSA                  | W              | Displays a message      |
| GE](MESSAGE "wikilink") |                | above this item to SRC. |
| *message*               |                |                         |
+-------------------------+----------------+-------------------------+
| [MESSAGEUA              | W              | Displays a UNICODE      |
| ](MESSAGEUA "wikilink") |                | message above this item |
| *colour, talkmode,      |                | to SRC.                 |
| font, lang_id, message* |                |                         |
+-------------------------+----------------+-------------------------+
| [M                      | RW             | Gets or sets a modifier |
| ODAR](MODAR "wikilink") |                | for the item\'s armour  |
|                         |                | rating if it is         |
|                         |                | clothing, armor, or a   |
|                         |                | shield. This gets or    |
|                         |                | sets a modifier for the |
|                         |                | item\'s damage if it is |
|                         |                | a weapon type.          |
+-------------------------+----------------+-------------------------+
| [M                      | RW             | Gets or sets the MORE1  |
| ORE1](MORE1 "wikilink") |                | value for the item.     |
+-------------------------+----------------+-------------------------+
| [MOR                    | RW             | Gets or sets the upper  |
| E1H](MORE1H "wikilink") |                | 4 bytes of the item\'s  |
|                         |                | MORE1 value.            |
+-------------------------+----------------+-------------------------+
| [MOR                    | RW             | Gets or sets the lower  |
| E1L](MORE1L "wikilink") |                | 4 bytes of the item\'s  |
|                         |                | MORE1 value.            |
+-------------------------+----------------+-------------------------+
| [M                      | RW             | Gets or sets the MORE2  |
| ORE2](MORE2 "wikilink") |                | value for the item.     |
+-------------------------+----------------+-------------------------+
| [MOR                    | RW             | Gets or sets the upper  |
| E2H](MORE2H "wikilink") |                | 4 bytes of the item\'s  |
|                         |                | MORE2 value.            |
+-------------------------+----------------+-------------------------+
| [MOR                    | RW             | Gets or sets the lower  |
| E2L](MORE2L "wikilink") |                | 4 bytes of the item\'s  |
|                         |                | MORE2 value.            |
+-------------------------+----------------+-------------------------+
| [M                      | RW             | Gets or sets the MOREM  |
| OREM](MOREM "wikilink") |                | value for the item.     |
+-------------------------+----------------+-------------------------+
| [M                      | RW             | Gets or sets the MOREX  |
| OREX](MOREX "wikilink") |                | value for the item.     |
+-------------------------+----------------+-------------------------+
| [M                      | RW             | Gets or sets the MOREY  |
| OREY](MOREY "wikilink") |                | value for the item.     |
+-------------------------+----------------+-------------------------+
| [M                      | RW             | Gets or sets the MOREZ  |
| OREZ](MOREZ "wikilink") |                | value for the item.     |
+-------------------------+----------------+-------------------------+
| [M                      | RW             | Gets or sets the MOREP  |
| OREP](MOREP "wikilink") |                | value for the item.     |
+-------------------------+----------------+-------------------------+
| [MOVE](MOVE "wikilink") | W              | Moves the object        |
| *direction amount*\     |                | relative to its current |
| [MOVE](MOVE "wikilink") |                | position. Possible      |
| *x y*                   |                | *direction* values are  |
|                         |                | N,S,W, or E. Note, you  |
|                         |                | can combine directions  |
|                         |                | (like: MOVE SW 1) but   |
|                         |                | nonsensical directions  |
|                         |                | (like: MOVE WE 2) have  |
|                         |                | the nonsense removed.   |
+-------------------------+----------------+-------------------------+
| [MOVENEA                | W              | Moves the object to a   |
| R](MOVENEAR "wikilink") |                | random location near    |
| *object_uid, distance*  |                | another object within a |
|                         |                | certain distance.       |
+-------------------------+----------------+-------------------------+
| [MOV                    | W              | Moves the object to a   |
| ETO](MOVETO "wikilink") |                | specific location       |
| *location*              |                | (note, the AREADEF or   |
|                         |                | ROOMDEF must have a P   |
|                         |                | defined).               |
+-------------------------+----------------+-------------------------+
| [NAME](NAME "wikilink") | RW             | Gets or sets the        |
|                         |                | object\'s name.         |
+-------------------------+----------------+-------------------------+
| [NUDGEDOWN              | W              | Decreases the object\'s |
| ](NUDGEDOWN "wikilink") |                | Z level.                |
| *amount*                |                |                         |
+-------------------------+----------------+-------------------------+
| [NUDGE                  | W              | Increases the object\'s |
| UP](NUDGEUP "wikilink") |                | Z level.                |
| *amount*                |                |                         |
+-------------------------+----------------+-------------------------+
| [PROMPTCONSOLE](PR      | W              | Displays a prompt       |
| OMPTCONSOLE "wikilink") |                | message to SRC and      |
| *function,              |                | passes their response   |
| prompt_message*         |                | into a specified        |
|                         |                | function.               |
+-------------------------+----------------+-------------------------+
| [PROMPTCONSOLEU](PRO    | W              | Displays a prompt       |
| MPTCONSOLEU "wikilink") |                | message to SRC and      |
| *function,              |                | passes their response   |
| prompt_message*         |                | into a specified        |
|                         |                | function, supporting    |
|                         |                | UNICODE response.       |
+-------------------------+----------------+-------------------------+
| [REM                    | W              | Deletes the object.     |
| OVE](REMOVE "wikilink") |                |                         |
+-------------------------+----------------+-------------------------+
| [REMOVEFROMVIEW](REM    | W              | Removes the object from |
| OVEFROMVIEW "wikilink") |                | nearby clients\'        |
|                         |                | screens.                |
+-------------------------+----------------+-------------------------+
| [RESCOUN                | R              | Returns the total       |
| T](RESCOUNT "wikilink") |                | amount of a specific    |
| *item_defname*          |                | item inside a           |
|                         |                | container.              |
+-------------------------+----------------+-------------------------+
| [RESENDTOOLTIP](RE      | W              | Forces Sphere to update |
| SENDTOOLTIP "wikilink") |                | the tooltips for nearby |
|                         |                | clients.                |
+-------------------------+----------------+-------------------------+
| [SAY](SAY "wikilink")   | W              | Makes the object speak  |
| *message*               |                | a message.              |
+-------------------------+----------------+-------------------------+
| [SAYU](SAYU "wikilink") | W              | Makes the object speak  |
| *message*               |                | a UTF-8 message         |
+-------------------------+----------------+-------------------------+
| [S                      | W              | Makes the object speak  |
| AYUA](SAYUA "wikilink") |                | a UNICODE message.      |
| *colour, talkmode,      |                |                         |
| font, lang_id, text*    |                |                         |
+-------------------------+----------------+-------------------------+
| [SDIAL                  | W              | Displays a dialog to    |
| OG](SDIALOG "wikilink") |                | SRC, providing that it  |
| *dialog_id, page,       |                | is not already open.    |
| parameters*             |                |                         |
+-------------------------+----------------+-------------------------+
| [SER                    | R              | Gets the item\'s unique |
| IAL](SERIAL "wikilink") |                | ID in the world.        |
+-------------------------+----------------+-------------------------+
| [SEXTANT                | R              | Converts the item\'s    |
| P](SEXTANTP "wikilink") |                | location or a specified |
| *location*              |                | location into sextant   |
|                         |                | coordinates.            |
+-------------------------+----------------+-------------------------+
| [S                      | W              | Plays a sound from this |
| OUND](SOUND "wikilink") |                | object.                 |
| *sound_id, repeat*      |                |                         |
+-------------------------+----------------+-------------------------+
| [SPELLEFFECT](          | W              | Causes the item to be   |
| SPELLEFFECT "wikilink") |                | affected by a spell.    |
| *spell_id, strength,    |                |                         |
| source_character_uid,   |                |                         |
| source_item_uid*        |                |                         |
+-------------------------+----------------+-------------------------+
| [TAG]                   | RW             | Gets or sets the value  |
| (TAG "wikilink")*.name* |                | of a TAG.               |
+-------------------------+----------------+-------------------------+
| [TAGAT](TA              | R              | Gets a TAG at the given |
| GAT "wikilink")*.index* |                | zero-based index.       |
+-------------------------+----------------+-------------------------+
| [TAGAT](TAGAT           | R              | Gets the name of the    |
| "wikilink")*.index*.KEY |                | TAG at the given        |
|                         |                | zero-based index.       |
+-------------------------+----------------+-------------------------+
| [TAGAT](TAGAT           | R              | Gets the value of the   |
| "wikilink")*.index*.VAL |                | TAG at the given        |
|                         |                | zero-based index.       |
+-------------------------+----------------+-------------------------+
| [TAGCOUN                | R              | Gets the number of TAGs |
| T](TAGCOUNT "wikilink") |                | stored on the item.     |
+-------------------------+----------------+-------------------------+
| [TAGLI                  | W              | Outputs a list of the   |
| ST](TAGLIST "wikilink") |                | object\'s TAGs.         |
+-------------------------+----------------+-------------------------+
| [TARGET](T              | W              | Displays a targeting    |
| ARGET "wikilink")*FGMW* |                | cursor to SRC. *F*      |
| *function*              |                | makes the *function*    |
|                         |                | available, and when     |
|                         |                | added, the function     |
|                         |                | name must be the 1st    |
|                         |                | argument. *M* allows    |
|                         |                | you to place a *multi*  |
|                         |                | item, in which case the |
|                         |                | multi number must be    |
|                         |                | passed as an argument.  |
|                         |                | *G* forces the target   |
|                         |                | to only be the ground.  |
|                         |                | *W* checks the criminal |
|                         |                | status of the player    |
|                         |                | before (or after?) the  |
|                         |                | target selection is     |
|                         |                | made.                   |
+-------------------------+----------------+-------------------------+
| [T                      | RW             | Gets or sets the length |
| IMER](TIMER "wikilink") |                | of time before the      |
|                         |                | item\'s timer expires,  |
|                         |                | in seconds.             |
+-------------------------+----------------+-------------------------+
| [TIM                    | RW             | Gets or sets the length |
| ERD](TIMERD "wikilink") |                | of time before the      |
|                         |                | item\'s timer expires,  |
|                         |                | in tenths of a second.  |
+-------------------------+----------------+-------------------------+
| [TIM                    | W              | Schedules a function to |
| ERF](TIMERF "wikilink") |                | be executed on this     |
| *time, function*        |                | object in *time*        |
|                         |                | seconds.                |
+-------------------------+----------------+-------------------------+
| [TIM                    | W              | Clears all scheduled    |
| ERF](TIMERF "wikilink") |                | functions from the      |
| *CLEAR*                 |                | object.                 |
+-------------------------+----------------+-------------------------+
| [TIM                    | W              | Stops the specified     |
| ERF](TIMERF "wikilink") |                | function from the item. |
| *STOP, function*        |                | (On X version wild      |
|                         |                | character \* is         |
|                         |                | available for defining  |
|                         |                | the function name or    |
|                         |                | the argument)           |
+-------------------------+----------------+-------------------------+
| [TRIGG                  | R              | Fires a custom trigger  |
| ER](TRIGGER "wikilink") |                | (trig_name), allowing   |
| *trig_name,             |                | you to define the       |
| trigger_argtype,        |                | behavior of the         |
| argument1, argument2,   |                | arguments (the types    |
| \...*                   |                | are defined under       |
|                         |                | trigger_argtype in the  |
|                         |                | sphere_defs.scp file).  |
|                         |                | The result of the       |
|                         |                | trigger\'s RETURN value |
|                         |                | is returned. For        |
|                         |                | example:                |
|                         |                |                         |
|                         |                | `LOCAL.result=<TR       |
|                         |                | IGGER @CustomTrigger,<D |
|                         |                | EF.tat_as_argn>,1,2,3>` |
+-------------------------+----------------+-------------------------+
| [TYPE](TYPE "wikilink") | RW             | Gets or sets the item   |
|                         |                | type. You can use       |
|                         |                | built-in or custom      |
|                         |                | [TYPEDE                 |
|                         |                | Fs](TYPEDEF "wikilink") |
|                         |                | as a value.             |
+-------------------------+----------------+-------------------------+
| [UID](UID "wikilink")   | R              | Gets the item\'s unique |
|                         |                | ID in the world.        |
+-------------------------+----------------+-------------------------+
| [UNEQU                  | W              | Unequips the item and   |
| IP](UNEQUIP "wikilink") |                | places it in SRC\'s     |
|                         |                | backpack.               |
+-------------------------+----------------+-------------------------+
| [UPD                    | W              | Updates the state of    |
| ATE](UPDATE "wikilink") |                | the item to nearby      |
|                         |                | clients.                |
+-------------------------+----------------+-------------------------+
| [UPDAT                  | W              | Updates the state of    |
| EX](UPDATEX "wikilink") |                | the item to nearby      |
|                         |                | clients, removing it    |
|                         |                | from their view first   |
|                         |                | to ensure a full        |
|                         |                | refresh.                |
+-------------------------+----------------+-------------------------+
| [USESC                  | W              | X branch only. Gets or  |
| UR](USESCUR "wikilink") |                | sets the current uses   |
|                         |                | of an item. Only        |
|                         |                | partially supported.    |
+-------------------------+----------------+-------------------------+
| [USESM                  | W              | X branch only. Gets or  |
| AX](USESMAX "wikilink") |                | sets the maximum uses   |
|                         |                | of an item. Only        |
|                         |                | partially supported.    |
+-------------------------+----------------+-------------------------+
| [USE](USE "wikilink")   | W              | Uses the item, as if    |
| *check_los*             |                | SRC had double clicked  |
|                         |                | it.                     |
+-------------------------+----------------+-------------------------+
| [USEIT                  | W              | Double clicks the item, |
| EM](USEITEM "wikilink") |                | with SRC as the source  |
|                         |                | of the event, without   |
|                         |                | checking for line of    |
|                         |                | sight.                  |
+-------------------------+----------------+-------------------------+
| [WEI                    | R              | Gets the weight of the  |
| GHT](WEIGHT "wikilink") |                | item.                   |
+-------------------------+----------------+-------------------------+
| [Z](Z "wikilink")       | R              | Gets the Z position of  |
|                         |                | the item.               |
+-------------------------+----------------+-------------------------+

## Triggers

Here is a list of all item triggers. Click on the trigger name for more
detailed information such as arguments and examples.

  -------------------------------------------------------------- ---------------------------------------------------------------------------------------- --------------------
  **Name**                                                       **Description**                                                                          **Sphere X Only?**
  [\@AfterClick](@AfterClick "wikilink")                         Fires when the object has been single-clicked, just before the overhead name is shown.   
  [\@Buy](@Buy "wikilink")                                       Fires when the item is being bought from a vendor.                                       
  [\@Click](@Click "wikilink")                                   Fires when the object has been single-clicked.                                           
  [\@ClientTooltip](@ClientTooltip "wikilink")                   Fires when tooltips are about to be sent to a client.                                    
  [\@ContextMenuRequest](@ContextMenuRequest "wikilink")         Fires when a client requests the context menu options for the object.                    
  [\@ContextMenuSelect](@ContextMenuSelect "wikilink")           Fires when a client selects a context menu option for the object.                        
  [\@Carve](@Carve "wikilink")                                   Fires when a corpse item is being carved.                                                X
  [\@Create](@Create "wikilink")                                 Fires when the object is initially created, before it is placed in the world.            
  [\@Damage](@Damage "wikilink")                                 Fires when the item receives damage.                                                     
  [\@DClick](@DClick "wikilink")                                 Fires when the object is double-clicked.                                                 
  [\@Destroy](@Destroy "wikilink")                               Fires when the object is being deleted.                                                  
  [\@DropOn_Char](@DropOn_Char "wikilink")                       Fires when the item has been dropped on to a character.                                  
  [\@DropOn_Ground](@DropOn_Ground "wikilink")                   Fires when the item has been dropped on to the ground.                                   
  [\@DropOn_Item](@DropOn_Item "wikilink")                       Fires when the item is dropped on to another item.                                       
  [\@DropOn_Self](@DropOn_Self "wikilink")                       Fires when an item has been dropped on to this item.                                     
  [\@DropOn_Trade](@DropOn_Trade "wikilink")                     Fires when an item is being dropped on a Trade Window.                                   
  [\@Dye](@Dye "wikilink")                                       Fires when an item is having its colored changed.                                        
  [\@Equip](@Equip "wikilink")                                   Fires when the item has been equipped.                                                   
  [\@EquipTest](@EquipTest "wikilink")                           Fires when the item is about to be equipped.                                             
  [\@HouseDesignBegin](@HouseDesignBegin "wikilink")             A trigger for t_multi_custom, called when the player enters on design mode.              X
  [\@HouseDesignCommitItem](@HouseDesignCommitItem "wikilink")   Fires for each commited item in house design system.                                     X
  [\@PickUp_Ground](@PickUp_Ground "wikilink")                   Fires when the item ihas been picked up from the ground.                                 
  [\@PickUp_Pack](@PickUp_Pack "wikilink")                       Fires when the item is picked up from inside a container.                                
  [\@PickUp_Self](@PickUp_Self "wikilink")                       Fires when an item has been picked up from inside the item.                              
  [\@PickUp_Stack](@PickUp_Stack "wikilink")                     Fires when the item is picked up from a stack.                                           
  [\@Redeed](@Redeed "wikilink")                                 Fires when multi item is about to redeed (t_multi, t_ship, t_multi_custom, t_addon).     
  [\@Sell](@Sell "wikilink")                                     Fires when the item is sold to a vendor.                                                 
  [\@Smelt](@Smelt "wikilink")                                   Fires when the item is being smelt.                                                      X
  [\@SpellEffect](@SpellEffect "wikilink")                       Fires when the object is hit by the effects of a spell.                                  
  [\@Step](@Step "wikilink")                                     Fires when a character steps on the item.                                                
  [\@TargOn_Cancel](@TargOn_Cancel "wikilink")                   Fires when a target is cancelled from the item.                                          
  [\@TargOn_Char](@TargOn_Char "wikilink")                       Fires when a character is targeted from the item.                                        
  [\@TargOn_Ground](@TargOn_Ground "wikilink")                   Fires when the ground is targeted from the item.                                         
  [\@TargOn_Item](@TargOn_Item "wikilink")                       Fires when an item is targeted from this item.                                           
  [\@Timer](@Timer "wikilink")                                   Fires when the item\'s timer expires.                                                    
  [\@ToolTip](@ToolTip "wikilink")                               Fires when old-style tooltips are requested for the item.                                
  [\@UnEquip](@UnEquip "wikilink")                               Fires when the item is unequipped.                                                       
  -------------------------------------------------------------- ---------------------------------------------------------------------------------------- --------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Objects](Category:_Objects "wikilink")
