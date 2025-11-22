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
spell. Some [special types of item](./Special_Items.md) also have
additional properties that can be accessed via scripts. The following
tables detail the various properties of items in SphereServer:

## References

References return pointers to other objects (e.g. the REGION reference
allows you to access the REGION that an object is in). These can either
be accessed by using *\<REFNAME\>* to return the [UID](./UID.md)
(1 for object types that don\'t have UIDs) of the object or 0 if it
doesn\'t exist, or by using *\<REFNAME.KEY\>* where KEY is a valid
property/function/reference for the *REFNAME* object. Click on the name
for more detailed information such as usage and examples.

  ------------------------------------------- ---------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                                    **Read/Write**   **Description**
  [CONT](./CONT.md)                     RW               Gets or sets the [character](./Characters.md) or [container item](./Special_ItemsContainers.md) that the object is inside. When an item\'s CONT is changed, it bypasses the typical behavior (for example, you can force an item to be \"in\" a container and bypass \@dropon triggers, or force an item to be equipped to a player and bypass \@equiptest and \@equip triggers \-- but be careful, because in this second scenario it may end up in an invalid layer.)
  [LINK](./LINK.md)                     RW               Gets or sets the [character](./Characters.md) or [item](./Items.md) that the item is linked to. Note, you can make circular LINK\'s, but a single item cannot be linked to more than one other item.
  [REGION](./Regions.md)                R                Gets the [region](./Regions.md) that the object is in.
  [ROOM](./ROOM.md)                     R                Gets the [room](./Rooms.md) that the object is in.
  [P](./P.md)                           RW               Gets or sets the [position](./Map_Points.md) that the object is at.
  [SECTOR](./Sectors.md)                R                Gets the [sector](./Sectors.md) that the object is in.
  [TOPOBJ](./TOPOBJ.md)                 R                Gets the top-most [character](./Characters.md) or [item](./Items.md) in the world that contains the item.
  [TYPEDEF](TYPEDEF_(Reference) "wikilink")   R                Gets the [ITEMDEF](./ITEMDEF.md) that defines the item.
  ------------------------------------------- ---------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Properties and Functions {#properties_and_functions}

Here is a list of all item properties and functions. If a function is
marked as readable then it can return a value when used as
`<KEY>`{=html}. Click on the name for more detailed information such as
usage and examples. If an attempt is made to access a property that does
not exist on the item, the property from the
[ITEMDEF](./ITEMDEF.md) will be accessed instead.

+-------------------------+----------------+-------------------------+
| Name                    | **Read/Write** | **Description**         |
+=========================+================+=========================+
| [ADDCIRCLE              | W              | Adds all of the spells  |
| ](./ADDCIRCLE.md) |                | in the given Magery     |
| *spell_circle*          |                | circle to the           |
|                         |                | spellbook.              |
+-------------------------+----------------+-------------------------+
| [ADDSPEL                | RW             | Gets whether or not a   |
| L](./ADDSPELL.md) |                | spell exists in the     |
| *spell_id*              |                | spellbook, or adds a    |
|                         |                | spell to the spellbook. |
+-------------------------+----------------+-------------------------+
| [AMMOANI                | RW             | Overrides TDATA4 for    |
| M](./AMMOANIM.md) |                | bow/crossbow type       |
|                         |                | weapons.                |
+-------------------------+----------------+-------------------------+
| [AMMOANIMHUE](./RW______________Sets_the_color_of_the___
_AMMOANIMHUE.md) |                | effect when firing      |
|                         |                | bow/crossbow type       |
|                         |                | weapons.                |
+-------------------------+----------------+-------------------------+
| [AMMOANIMRENDER](./AMM_____RW______________Sets_the_render_mode_of_
_OANIMRENDER.md) |                | the effect when firing  |
|                         |                | bow/crossbow type       |
|                         |                | weapons.                |
+-------------------------+----------------+-------------------------+
| [AMMOCON                | RW             | Sets the container UID  |
| T](./AMMOCONT.md) |                | or ID where to search   |
|                         |                | for ammos for           |
|                         |                | bow/crossbow type       |
|                         |                | weapons.                |
+-------------------------+----------------+-------------------------+
| [AMMOSOUNDHIT](./A_________RW______________Overrides_the_hit_sound_
_MMOSOUNDHIT.md) |                | on weapons.             |
+-------------------------+----------------+-------------------------+
| [AMMOSOUNDMISS](./AM_______RW______________Overrides_the_miss______
_MOSOUNDMISS.md) |                | sound on weapons.       |
+-------------------------+----------------+-------------------------+
| [AMMOTYP                | RW             | Overrides TDATA3 for    |
| E](./AMMOTYPE.md) |                | bow/crossbow type       |
|                         |                | weapons.                |
+-------------------------+----------------+-------------------------+
| [AMO                    | RW             | Gets the amount of      |
| UNT](./AMOUNT.md) |                | items this icon         |
|                         |                | represents (e.g. a pile |
|                         |                | of gold or any stacked  |
|                         |                | item).                  |
+-------------------------+----------------+-------------------------+
| [ATTR](./ATTR.md) | RW             | Gets or sets the        |
|                         |                | item\'s attribute       |
|                         |                | flags.                  |
+-------------------------+----------------+-------------------------+
| [BOU                    | W              | Moves the item to       |
| NCE](./BOUNCE.md) |                | SRC\'s backpack         |
|                         |                | (triggering the *you    |
|                         |                | put the item in your    |
|                         |                | pack* message.          |
+-------------------------+----------------+-------------------------+
| [CAN](./CAN.md)   | RW             | Gets or Sets the        |
|                         |                | can_flags (Setting can  |
|                         |                | be only done in the     |
|                         |                | Itemdef itself). Only   |
|                         |                | readable in X branch.   |
+-------------------------+----------------+-------------------------+
| [CANMA                  | RW             | Stores the CAN flags to |
| SK](./CANMASK.md) |                | be dynamically switched |
|                         |                | on or off from the base |
|                         |                | CAN property.           |
+-------------------------+----------------+-------------------------+
| [CAN                    | R              | Returns 1 if SRC can    |
| SEE](./CANSEE.md) |                | see the item.           |
+-------------------------+----------------+-------------------------+
| [CANSEELOS              | R              | Returns 1 if SRC has    |
| ](./CANSEELOS.md) |                | line of sight to the    |
| *point_or_uid*          |                | item or character (uid) |
|                         |                | or point (location).    |
+-------------------------+----------------+-------------------------+
| [CANSEELOSFLAG](./CA_______R_______________Returns_1_if_SRC_has____
_NSEELOSFLAG.md) |                | line of sight to the    |
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
| ](./CLEARTAGS.md) |                | the item that start     |
| *prefix*                |                | with the given prefix.  |
+-------------------------+----------------+-------------------------+
| [C                      | RW             | Gets or sets the        |
| OLOR](./COLOR.md) |                | object\'s hue.          |
+-------------------------+----------------+-------------------------+
| [CONSU                  | W              | Deducts an amount from  |
| ME](./CONSUME.md) |                | the item, deleting it   |
| *amount*                |                | at 0.                   |
+-------------------------+----------------+-------------------------+
| [CONTCONSUME](./W_______________Deletes_items_from______
_CONTCONSUME.md) |                | inside the container.   |
| *resource_list*         |                |                         |
+-------------------------+----------------+-------------------------+
| [CONTGRI                | RW             | If in a container, gets |
| D](./CONTGRID.md) |                | or sets the grid number |
|                         |                | that the item occupies  |
|                         |                | (in KR\'s grid view)    |
+-------------------------+----------------+-------------------------+
| [C                      | RW             | Gets or sets the        |
| ONTP](./CONTP.md) |                | position of the item    |
|                         |                | within its container.   |
+-------------------------+----------------+-------------------------+
| [DAM                    | W              | If *chance* is greater  |
| AGE](./DAMAGE.md) |                | than                    |
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
| ICK](./DCLICK.md) |                | with SRC as the source  |
|                         |                | of the event.           |
+-------------------------+----------------+-------------------------+
| [D                      | W              | Sets the decay timer    |
| ECAY](./DECAY.md) |                | (in tenths of a second) |
| *time*                  |                | for the item.           |
+-------------------------+----------------+-------------------------+
| [DESTR                  | W              | Deletes the object, not |
| OY](./DESTROY.md) |                | stopped by a return 1   |
|                         |                | in                      |
|                         |                | [\@Destro               |
|                         |                | y](./Destroy.md) |
+-------------------------+----------------+-------------------------+
| [DIALOG](DIALOG         | W              | Displays a dialog to    |
| _(Function) "wikilink") |                | SRC.                    |
| *dialog_id, page,       |                |                         |
| parameters*             |                |                         |
+-------------------------+----------------+-------------------------+
| [DIS                    | RW             | Gets or sets the ID     |
| PID](./DISPID.md) |                | that the item will      |
|                         |                | appear as to players.   |
+-------------------------+----------------+-------------------------+
| [DISPIDDEC              | RW             | Same as                 |
| ](./DISPIDDEC.md) |                | [DISP                   |
|                         |                | ID](./DISPID.md), |
|                         |                | except it returns the   |
|                         |                | ID as a decimal number. |
+-------------------------+----------------+-------------------------+
| [DISTANC                | R              | Gets the distance       |
| E](./DISTANCE.md) |                | between this object and |
| *point_or_uid*          |                | SRC. If *point_or_uid*  |
|                         |                | is used, SRC can be     |
|                         |                | replaced with a map     |
|                         |                | location or another     |
|                         |                | object.                 |
+-------------------------+----------------+-------------------------+
| [DMGCO                  | RW             | Gets or sets the amount |
| LD](./DMGCOLD.md) |                | of cold damage the      |
|                         |                | weapon will give.       |
+-------------------------+----------------+-------------------------+
| [DMGENERGY              | RW             | Gets or sets the amount |
| ](./DMGENERGY.md) |                | of energy damage the    |
|                         |                | weapon will give.       |
+-------------------------+----------------+-------------------------+
| [DMGFI                  | RW             | Gets or sets the amount |
| RE](./DMGFIRE.md) |                | of fire damage the      |
|                         |                | weapon will give.       |
+-------------------------+----------------+-------------------------+
| [DMGPOISON              | RW             | Gets or sets the amount |
| ](./DMGPOISON.md) |                | of poison damage the    |
|                         |                | weapon will give.       |
+-------------------------+----------------+-------------------------+
| [DROP](./DROP.md) | W              | Drops the item to the   |
|                         |                | ground.                 |
+-------------------------+----------------+-------------------------+
| [DUPE](./DUPE.md) | W              | Clones the item.        |
+-------------------------+----------------+-------------------------+
| [EDIT](./EDIT.md) | W              | Displays an editing     |
|                         |                | dialog for the item to  |
|                         |                | SRC.                    |
+-------------------------+----------------+-------------------------+
| [EFF                    | W              | Displays an effect to   |
| ECT](./EFFECT.md) |                | nearby clients.         |
| *type, item_id, speed,  |                |                         |
| loop, explode, colour,  |                |                         |
| rendermode*             |                |                         |
+-------------------------+----------------+-------------------------+
| [E                      | W              | Displays a \*You see\*  |
| MOTE](./EMOTE.md) |                | message to all nearby   |
| *message*               |                | clients.                |
+-------------------------+----------------+-------------------------+
| [E                      | W              | Equips the item to SRC. |
| QUIP](./EQUIP.md) |                |                         |
+-------------------------+----------------+-------------------------+
| [EVENTS](EVENTS         | RW             | Gets a list of events   |
| _(Property) "wikilink") |                | attached to the object, |
| *event_defname*         |                | or adds or removes an   |
|                         |                | event to or from the    |
|                         |                | object.                 |
+-------------------------+----------------+-------------------------+
| [FIX](./FIX.md)   | W              | Re-aligns the item or   |
|                         |                | character\'s Z level to |
|                         |                | ground level (if items  |
|                         |                | are on the ground, the  |
|                         |                | top item\'s *Z+HEIGHT*  |
|                         |                | is used).               |
+-------------------------+----------------+-------------------------+
| [FLIP](./FLIP.md) | W              | Rotates the item        |
|                         |                | clockwise.              |
+-------------------------+----------------+-------------------------+
| [F                      | RW             | Gets or sets the fruit  |
| RUIT](./FRUIT.md) |                | that will be produced   |
|                         |                | by the crops.           |
+-------------------------+----------------+-------------------------+
| [HEI                    | R              | Gets the height of the  |
| GHT](./HEIGHT.md) |                | item.                   |
+-------------------------+----------------+-------------------------+
| [HITS](./HITS.md) | RW             | Gets or sets the number |
|                         |                | of hitpoints the item   |
|                         |                | has.                    |
+-------------------------+----------------+-------------------------+
| [HITPOINTS              | RW             | Gets or sets the number |
| ](./HITPOINTS.md) |                | of hitpoints the item   |
|                         |                | has.                    |
+-------------------------+----------------+-------------------------+
| [ID](./ID.md)     | RW             | Gets or sets the ID of  |
|                         |                | the item.               |
+-------------------------+----------------+-------------------------+
| [INFO](./INFO.md) | W              | Displays an information |
|                         |                | dialog about the item   |
|                         |                | to SRC.                 |
+-------------------------+----------------+-------------------------+
| [ISARM                  | R              | Returns 1 if the object |
| OR](./ISARMOR.md) |                | is armour.              |
| *object_uid*            |                |                         |
+-------------------------+----------------+-------------------------+
| [ISC                    | R              | Returns 1 if the object |
| HAR](./ISCHAR.md) |                | is a character.         |
+-------------------------+----------------+-------------------------+
| [ISC                    | R              | Returns 1 if the object |
| ONT](./ISCONT.md) |                | is a container.         |
+-------------------------+----------------+-------------------------+
| [ISEVENT](ISEVENT "wik  | R              | Returns 1 if the object |
| ilink")*.event_defname* |                | has an event attached   |
|                         |                | to it.                  |
+-------------------------+----------------+-------------------------+
| [ISI                    | R              | Returns 1 if the object |
| TEM](./ISITEM.md) |                | is an item.             |
+-------------------------+----------------+-------------------------+
| [ISNEARTYPE]            | R              | Returns 1 if a nearby   |
| (ISNEARTYPE "wikilink") |                | item has the given TYPE |
| *type, distance, flags* |                | and is within           |
|                         |                | *distance*.             |
+-------------------------+----------------+-------------------------+
| [ISNEARTYPETOP](./IS_______R_______________Returns_a_nearby_world__
_NEARTYPETOP.md) |                | location of a nearby    |
| *type, distance, flags* |                | item which has the      |
|                         |                | given TYPE and is       |
|                         |                | within *distance*.      |
+-------------------------+----------------+-------------------------+
| [ISPLAYE                | R              | Returns 1 if the object |
| R](./ISPLAYER.md) |                | is a player character.  |
+-------------------------+----------------+-------------------------+
| [                       | R              | Returns 1 if the object |
| ISTEVENT](ISTEVENT "wik |                | has an event attached   |
| ilink")*.event_defname* |                | to its ITEMDEF.         |
+-------------------------+----------------+-------------------------+
| [ISTIMERF](./ISTIMERF______R_______________Returns_the_number_of.md)*.function* |                | seconds left on the     |
|                         |                | specified timerf if it  |
|                         |                | exists.                 |
+-------------------------+----------------+-------------------------+
| [ISWEAPO                | R              | Returns 1 if the object |
| N](./ISWEAPON.md) |                | is a weapon.            |
| *object_uid*            |                |                         |
+-------------------------+----------------+-------------------------+
| [L                      | RW             | Gets or sets the layer  |
| AYER](./LAYER.md) |                | that the item occupies  |
|                         |                | when equipped (possible |
|                         |                | layers are defined in   |
|                         |                | the sphere_defs.scp     |
|                         |                | file).                  |
+-------------------------+----------------+-------------------------+
| [MAP](./MAP.md)   | RW             | Gets or sets the map    |
|                         |                | that this object is     |
|                         |                | located.                |
+-------------------------+----------------+-------------------------+
| [MAXHI                  | RW             | Gets or sets the        |
| TS](./MAXHITS.md) |                | maximum number of       |
|                         |                | hitpoints the item can  |
|                         |                | have.                   |
+-------------------------+----------------+-------------------------+
| [MENU](MENU             | W              | Displays a menu to SRC. |
| _(Function) "wikilink") |                |                         |
| *menu_defname*          |                |                         |
+-------------------------+----------------+-------------------------+
| [MESSA                  | W              | Displays a message      |
| GE](./MESSAGE.md) |                | above this item to SRC. |
| *message*               |                |                         |
+-------------------------+----------------+-------------------------+
| [MESSAGEUA              | W              | Displays a UNICODE      |
| ](./MESSAGEUA.md) |                | message above this item |
| *colour, talkmode,      |                | to SRC.                 |
| font, lang_id, message* |                |                         |
+-------------------------+----------------+-------------------------+
| [M                      | RW             | Gets or sets a modifier |
| ODAR](./MODAR.md) |                | for the item\'s armour  |
|                         |                | rating if it is         |
|                         |                | clothing, armor, or a   |
|                         |                | shield. This gets or    |
|                         |                | sets a modifier for the |
|                         |                | item\'s damage if it is |
|                         |                | a weapon type.          |
+-------------------------+----------------+-------------------------+
| [M                      | RW             | Gets or sets the MORE1  |
| ORE1](./MORE1.md) |                | value for the item.     |
+-------------------------+----------------+-------------------------+
| [MOR                    | RW             | Gets or sets the upper  |
| E1H](./MORE1H.md) |                | 4 bytes of the item\'s  |
|                         |                | MORE1 value.            |
+-------------------------+----------------+-------------------------+
| [MOR                    | RW             | Gets or sets the lower  |
| E1L](./MORE1L.md) |                | 4 bytes of the item\'s  |
|                         |                | MORE1 value.            |
+-------------------------+----------------+-------------------------+
| [M                      | RW             | Gets or sets the MORE2  |
| ORE2](./MORE2.md) |                | value for the item.     |
+-------------------------+----------------+-------------------------+
| [MOR                    | RW             | Gets or sets the upper  |
| E2H](./MORE2H.md) |                | 4 bytes of the item\'s  |
|                         |                | MORE2 value.            |
+-------------------------+----------------+-------------------------+
| [MOR                    | RW             | Gets or sets the lower  |
| E2L](./MORE2L.md) |                | 4 bytes of the item\'s  |
|                         |                | MORE2 value.            |
+-------------------------+----------------+-------------------------+
| [M                      | RW             | Gets or sets the MOREM  |
| OREM](./MOREM.md) |                | value for the item.     |
+-------------------------+----------------+-------------------------+
| [M                      | RW             | Gets or sets the MOREX  |
| OREX](./MOREX.md) |                | value for the item.     |
+-------------------------+----------------+-------------------------+
| [M                      | RW             | Gets or sets the MOREY  |
| OREY](./MOREY.md) |                | value for the item.     |
+-------------------------+----------------+-------------------------+
| [M                      | RW             | Gets or sets the MOREZ  |
| OREZ](./MOREZ.md) |                | value for the item.     |
+-------------------------+----------------+-------------------------+
| [M                      | RW             | Gets or sets the MOREP  |
| OREP](./MOREP.md) |                | value for the item.     |
+-------------------------+----------------+-------------------------+
| [MOVE](./MOVE.md) | W              | Moves the object        |
| *direction amount*\     |                | relative to its current |
| [MOVE](./MOVE.md) |                | position. Possible      |
| *x y*                   |                | *direction* values are  |
|                         |                | N,S,W, or E. Note, you  |
|                         |                | can combine directions  |
|                         |                | (like: MOVE SW 1) but   |
|                         |                | nonsensical directions  |
|                         |                | (like: MOVE WE 2) have  |
|                         |                | the nonsense removed.   |
+-------------------------+----------------+-------------------------+
| [MOVENEA                | W              | Moves the object to a   |
| R](./MOVENEAR.md) |                | random location near    |
| *object_uid, distance*  |                | another object within a |
|                         |                | certain distance.       |
+-------------------------+----------------+-------------------------+
| [MOV                    | W              | Moves the object to a   |
| ETO](./MOVETO.md) |                | specific location       |
| *location*              |                | (note, the AREADEF or   |
|                         |                | ROOMDEF must have a P   |
|                         |                | defined).               |
+-------------------------+----------------+-------------------------+
| [NAME](./NAME.md) | RW             | Gets or sets the        |
|                         |                | object\'s name.         |
+-------------------------+----------------+-------------------------+
| [NUDGEDOWN              | W              | Decreases the object\'s |
| ](./NUDGEDOWN.md) |                | Z level.                |
| *amount*                |                |                         |
+-------------------------+----------------+-------------------------+
| [NUDGE                  | W              | Increases the object\'s |
| UP](./NUDGEUP.md) |                | Z level.                |
| *amount*                |                |                         |
+-------------------------+----------------+-------------------------+
| [PROMPTCONSOLE](./PR_______W_______________Displays_a_prompt_______
_OMPTCONSOLE.md) |                | message to SRC and      |
| *function,              |                | passes their response   |
| prompt_message*         |                | into a specified        |
|                         |                | function.               |
+-------------------------+----------------+-------------------------+
| [PROMPTCONSOLEU](./PRO_____W_______________Displays_a_prompt_______
_MPTCONSOLEU.md) |                | message to SRC and      |
| *function,              |                | passes their response   |
| prompt_message*         |                | into a specified        |
|                         |                | function, supporting    |
|                         |                | UNICODE response.       |
+-------------------------+----------------+-------------------------+
| [REM                    | W              | Deletes the object.     |
| OVE](./REMOVE.md) |                |                         |
+-------------------------+----------------+-------------------------+
| [REMOVEFROMVIEW](./REM_____W_______________Removes_the_object_from_
_OVEFROMVIEW.md) |                | nearby clients\'        |
|                         |                | screens.                |
+-------------------------+----------------+-------------------------+
| [RESCOUN                | R              | Returns the total       |
| T](./RESCOUNT.md) |                | amount of a specific    |
| *item_defname*          |                | item inside a           |
|                         |                | container.              |
+-------------------------+----------------+-------------------------+
| [RESENDTOOLTIP](./RE_______W_______________Forces_Sphere_to_update_
_SENDTOOLTIP.md) |                | the tooltips for nearby |
|                         |                | clients.                |
+-------------------------+----------------+-------------------------+
| [SAY](./SAY.md)   | W              | Makes the object speak  |
| *message*               |                | a message.              |
+-------------------------+----------------+-------------------------+
| [SAYU](./SAYU.md) | W              | Makes the object speak  |
| *message*               |                | a UTF-8 message         |
+-------------------------+----------------+-------------------------+
| [S                      | W              | Makes the object speak  |
| AYUA](./SAYUA.md) |                | a UNICODE message.      |
| *colour, talkmode,      |                |                         |
| font, lang_id, text*    |                |                         |
+-------------------------+----------------+-------------------------+
| [SDIAL                  | W              | Displays a dialog to    |
| OG](./SDIALOG.md) |                | SRC, providing that it  |
| *dialog_id, page,       |                | is not already open.    |
| parameters*             |                |                         |
+-------------------------+----------------+-------------------------+
| [SER                    | R              | Gets the item\'s unique |
| IAL](./SERIAL.md) |                | ID in the world.        |
+-------------------------+----------------+-------------------------+
| [SEXTANT                | R              | Converts the item\'s    |
| P](./SEXTANTP.md) |                | location or a specified |
| *location*              |                | location into sextant   |
|                         |                | coordinates.            |
+-------------------------+----------------+-------------------------+
| [S                      | W              | Plays a sound from this |
| OUND](./SOUND.md) |                | object.                 |
| *sound_id, repeat*      |                |                         |
+-------------------------+----------------+-------------------------+
| [SPELLEFFECT](./W_______________Causes_the_item_to_be___
_SPELLEFFECT.md) |                | affected by a spell.    |
| *spell_id, strength,    |                |                         |
| source_character_uid,   |                |                         |
| source_item_uid*        |                |                         |
+-------------------------+----------------+-------------------------+
| [TAG]                   | RW             | Gets or sets the value  |
| (TAG "wikilink")*.name* |                | of a TAG.               |
+-------------------------+----------------+-------------------------+
| [TAGAT](./TA_______________R_______________Gets_a_TAG_at_the_given_
_GAT.md)*.index* |                | zero-based index.       |
+-------------------------+----------------+-------------------------+
| [TAGAT](./TAGAT____________R_______________Gets_the_name_of_the.md)*.index*.KEY |                | TAG at the given        |
|                         |                | zero-based index.       |
+-------------------------+----------------+-------------------------+
| [TAGAT](./TAGAT____________R_______________Gets_the_value_of_the.md)*.index*.VAL |                | TAG at the given        |
|                         |                | zero-based index.       |
+-------------------------+----------------+-------------------------+
| [TAGCOUN                | R              | Gets the number of TAGs |
| T](./TAGCOUNT.md) |                | stored on the item.     |
+-------------------------+----------------+-------------------------+
| [TAGLI                  | W              | Outputs a list of the   |
| ST](./TAGLIST.md) |                | object\'s TAGs.         |
+-------------------------+----------------+-------------------------+
| [TARGET](./T_______________W_______________Displays_a_targeting____
_ARGET.md)*FGMW* |                | cursor to SRC. *F*      |
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
| IMER](./TIMER.md) |                | of time before the      |
|                         |                | item\'s timer expires,  |
|                         |                | in seconds.             |
+-------------------------+----------------+-------------------------+
| [TIM                    | RW             | Gets or sets the length |
| ERD](./TIMERD.md) |                | of time before the      |
|                         |                | item\'s timer expires,  |
|                         |                | in tenths of a second.  |
+-------------------------+----------------+-------------------------+
| [TIM                    | W              | Schedules a function to |
| ERF](./TIMERF.md) |                | be executed on this     |
| *time, function*        |                | object in *time*        |
|                         |                | seconds.                |
+-------------------------+----------------+-------------------------+
| [TIM                    | W              | Clears all scheduled    |
| ERF](./TIMERF.md) |                | functions from the      |
| *CLEAR*                 |                | object.                 |
+-------------------------+----------------+-------------------------+
| [TIM                    | W              | Stops the specified     |
| ERF](./TIMERF.md) |                | function from the item. |
| *STOP, function*        |                | (On X version wild      |
|                         |                | character \* is         |
|                         |                | available for defining  |
|                         |                | the function name or    |
|                         |                | the argument)           |
+-------------------------+----------------+-------------------------+
| [TRIGG                  | R              | Fires a custom trigger  |
| ER](./TRIGGER.md) |                | (trig_name), allowing   |
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
| [TYPE](./TYPE.md) | RW             | Gets or sets the item   |
|                         |                | type. You can use       |
|                         |                | built-in or custom      |
|                         |                | [TYPEDE                 |
|                         |                | Fs](./TYPEDEF.md) |
|                         |                | as a value.             |
+-------------------------+----------------+-------------------------+
| [UID](./UID.md)   | R              | Gets the item\'s unique |
|                         |                | ID in the world.        |
+-------------------------+----------------+-------------------------+
| [UNEQU                  | W              | Unequips the item and   |
| IP](./UNEQUIP.md) |                | places it in SRC\'s     |
|                         |                | backpack.               |
+-------------------------+----------------+-------------------------+
| [UPD                    | W              | Updates the state of    |
| ATE](./UPDATE.md) |                | the item to nearby      |
|                         |                | clients.                |
+-------------------------+----------------+-------------------------+
| [UPDAT                  | W              | Updates the state of    |
| EX](./UPDATEX.md) |                | the item to nearby      |
|                         |                | clients, removing it    |
|                         |                | from their view first   |
|                         |                | to ensure a full        |
|                         |                | refresh.                |
+-------------------------+----------------+-------------------------+
| [USESC                  | W              | X branch only. Gets or  |
| UR](./USESCUR.md) |                | sets the current uses   |
|                         |                | of an item. Only        |
|                         |                | partially supported.    |
+-------------------------+----------------+-------------------------+
| [USESM                  | W              | X branch only. Gets or  |
| AX](./USESMAX.md) |                | sets the maximum uses   |
|                         |                | of an item. Only        |
|                         |                | partially supported.    |
+-------------------------+----------------+-------------------------+
| [USE](./USE.md)   | W              | Uses the item, as if    |
| *check_los*             |                | SRC had double clicked  |
|                         |                | it.                     |
+-------------------------+----------------+-------------------------+
| [USEIT                  | W              | Double clicks the item, |
| EM](./USEITEM.md) |                | with SRC as the source  |
|                         |                | of the event, without   |
|                         |                | checking for line of    |
|                         |                | sight.                  |
+-------------------------+----------------+-------------------------+
| [WEI                    | R              | Gets the weight of the  |
| GHT](./WEIGHT.md) |                | item.                   |
+-------------------------+----------------+-------------------------+
| [Z](./Z.md)       | R              | Gets the Z position of  |
|                         |                | the item.               |
+-------------------------+----------------+-------------------------+

## Triggers

Here is a list of all item triggers. Click on the trigger name for more
detailed information such as arguments and examples.

  -------------------------------------------------------------- ---------------------------------------------------------------------------------------- --------------------
  **Name**                                                       **Description**                                                                          **Sphere X Only?**
  [\@AfterClick](./AfterClick.md)                         Fires when the object has been single-clicked, just before the overhead name is shown.   
  [\@Buy](./Buy.md)                                       Fires when the item is being bought from a vendor.                                       
  [\@Click](./Click.md)                                   Fires when the object has been single-clicked.                                           
  [\@ClientTooltip](./ClientTooltip.md)                   Fires when tooltips are about to be sent to a client.                                    
  [\@ContextMenuRequest](./ContextMenuRequest.md)         Fires when a client requests the context menu options for the object.                    
  [\@ContextMenuSelect](./ContextMenuSelect.md)           Fires when a client selects a context menu option for the object.                        
  [\@Carve](./Carve.md)                                   Fires when a corpse item is being carved.                                                X
  [\@Create](./Create.md)                                 Fires when the object is initially created, before it is placed in the world.            
  [\@Damage](./Damage.md)                                 Fires when the item receives damage.                                                     
  [\@DClick](./DClick.md)                                 Fires when the object is double-clicked.                                                 
  [\@Destroy](./Destroy.md)                               Fires when the object is being deleted.                                                  
  [\@DropOn_Char](./DropOn_Char.md)                       Fires when the item has been dropped on to a character.                                  
  [\@DropOn_Ground](./DropOn_Ground.md)                   Fires when the item has been dropped on to the ground.                                   
  [\@DropOn_Item](./DropOn_Item.md)                       Fires when the item is dropped on to another item.                                       
  [\@DropOn_Self](./DropOn_Self.md)                       Fires when an item has been dropped on to this item.                                     
  [\@DropOn_Trade](./DropOn_Trade.md)                     Fires when an item is being dropped on a Trade Window.                                   
  [\@Dye](./Dye.md)                                       Fires when an item is having its colored changed.                                        
  [\@Equip](./Equip.md)                                   Fires when the item has been equipped.                                                   
  [\@EquipTest](./EquipTest.md)                           Fires when the item is about to be equipped.                                             
  [\@HouseDesignBegin](./HouseDesignBegin.md)             A trigger for t_multi_custom, called when the player enters on design mode.              X
  [\@HouseDesignCommitItem](./HouseDesignCommitItem.md)   Fires for each commited item in house design system.                                     X
  [\@PickUp_Ground](./PickUp_Ground.md)                   Fires when the item ihas been picked up from the ground.                                 
  [\@PickUp_Pack](./PickUp_Pack.md)                       Fires when the item is picked up from inside a container.                                
  [\@PickUp_Self](./PickUp_Self.md)                       Fires when an item has been picked up from inside the item.                              
  [\@PickUp_Stack](./PickUp_Stack.md)                     Fires when the item is picked up from a stack.                                           
  [\@Redeed](./Redeed.md)                                 Fires when multi item is about to redeed (t_multi, t_ship, t_multi_custom, t_addon).     
  [\@Sell](./Sell.md)                                     Fires when the item is sold to a vendor.                                                 
  [\@Smelt](./Smelt.md)                                   Fires when the item is being smelt.                                                      X
  [\@SpellEffect](./SpellEffect.md)                       Fires when the object is hit by the effects of a spell.                                  
  [\@Step](./Step.md)                                     Fires when a character steps on the item.                                                
  [\@TargOn_Cancel](./TargOn_Cancel.md)                   Fires when a target is cancelled from the item.                                          
  [\@TargOn_Char](./TargOn_Char.md)                       Fires when a character is targeted from the item.                                        
  [\@TargOn_Ground](./TargOn_Ground.md)                   Fires when the ground is targeted from the item.                                         
  [\@TargOn_Item](./TargOn_Item.md)                       Fires when an item is targeted from this item.                                           
  [\@Timer](./Timer.md)                                   Fires when the item\'s timer expires.                                                    
  [\@ToolTip](./ToolTip.md)                               Fires when old-style tooltips are requested for the item.                                
  [\@UnEquip](./UnEquip.md)                               Fires when the item is unequipped.                                                       
  -------------------------------------------------------------- ---------------------------------------------------------------------------------------- --------------------

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Objects](./_Objects.md)
