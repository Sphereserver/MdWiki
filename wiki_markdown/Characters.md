```{=mediawiki}
{{Languages|Characters}}
```
\_\_FORCETOC\_\_ A character can be either a player or an NPC. Safety checks and warnings are now in place to prevent setting invalid skill or stat values.

## References

References return pointers to other objects (e.g. the REGION reference
allows you to access the REGION that an object is in). These can either
be accessed by using *\<REFNAME\>* to return the [UID](./UID.md)
(1 for object types that don\'t have UIDs) of the object or 0 if it
doesn\'t exist, or by using *\<REFNAME.KEY\>* where KEY is a valid
property/function/reference for the *REFNAME* object. Click on the name
for more detailed information such as usage and examples.

  ------------------------------------------------------------ ---------------- -------------------------------------------------------------------------------------------------------------------------------------------------- --------------------
  **Name**                                                     **Read/Write**   **Description**                                                                                                                                    **Sphere X only?**
  [ACCOUNT](./Accounts.md)                               RW               Gets or sets the [account](./Accounts.md) that the character belongs to.                                                                     
  [ACT](./ACT.md)                                        RW               Gets or sets the [character](./Characters.md) or [item](./Items.md) that is related to the action the character is performing.         
  [FINDCONT](./FINDCONT.md)*.n*                          R                Gets the nth [item](./Items.md) equipped to the character. (zero-based)                                                                      
  [FINDID](./FINDID.md)*.item_id*                        R                Gets the first [item](./Items.md) found equipped to the character or inside their backpack, with the matching [BASEID](./BASEID.md).   
  [FINDLAYER](./FINDLAYER.md)*.layer*                    R                Gets the [item](./Items.md) that the character has equipped in a specified layer.                                                            
  [FINDTYPE](./FINDTYPE.md)*.type*                       R                Gets the first [item](./Items.md) found equipped to the character or inside their backpack, with the matching [TYPE](./TYPE.md).       
  [MEMORYFINDTYPE](./MEMORYFINDTYPE.md)*.memory_flags*   R                Gets a [memory item](./Items.md) with the specified flags.                                                                                   
  [MEMORYFIND](./MEMORYFIND.md).*object_uid*             R                Gets a [memory item](./Items.md) that is linked to the given object.                                                                         
  [OWNER](./Owner.md)                                    R                Gets the character that owns this character. (RW in SphereServer-X Build)                                                                          
  [COOWNER.x](./Coowners.md)                             R                Gets the Coowner in the Xth position.
  [FRIEND.x](./Friends.md)                               R                Gets the Friend in the Xth position.
  [BAN.x](./Bans.md)                                     R                Gets the Banned character in the Xth position.
  [LOCKDOWN.x](./Lockdowns.md)                           R                Gets the locked down item in the Xth position.
  [VENDOR.x](./Vendors.md)                               R                Gets the vendor in the Xth position.
  [COMPONENT.x](./Comps.md)                         R                Gets the comp in the Xth position.
  [SPAWNITEM](./SPAWNITEM.md)                            R                Gets the [spawn item](./Items.md) (t_spawn_char) that this character originated from.                                                        
  [WEAPON](./WEAPON.md)                                  R                Gets the [weapon](./Items.md) that the character currently has equipped.                                                                     
  [P](./P.md)                                            RW               Gets or sets the [position](./Map_Points.md) that the character is at.                                                                       
  [REGION](./Regions.md)                                 R                Gets the [region](./Regions.md) that the character is currently located in.                                                                  
  [ROOM](./Rooms.md)                                     R                Gets the [room](./Rooms.md) that the character is in.                                                                                        
  [SECTOR](./Sectors.md)                                 R                Gets the [sector](./Sectors.md) that the character is in.                                                                                    
  [TOPOBJ](./TOPOBJ.md)                                  R                Gets the top-most [character](./Characters.md) or [item](./Items.md) in the world that contains the character.                         
  [TYPEDEF](TYPEDEF_(Reference) "wikilink")                    R                Gets the [CHARDEF](./CHARDEF.md) that defines the character.                                                                                 
  ------------------------------------------------------------ ---------------- -------------------------------------------------------------------------------------------------------------------------------------------------- --------------------

## Properties and Functions {#properties_and_functions}

Here is a list of all character properties and functions. If a function
is marked as readable then it can return a value when used as
`<KEY>`{=html}. Click on the name for more detailed information such as
usage and examples. If an attempt is made to access a property that does
not exist on the character, the property from the
[CHARDEF](./CHARDEF.md) will be accessed instead.

+----------------+----------------+----------------+----------------+
| **Name**       | **Read/Write** | *              | **Sphere X     |
|                |                | *Description** | only?**        |
+----------------+----------------+----------------+----------------+
| [AC](./R_______________Returns_the____________________
_AC.md) |                | character\'s   |                |
|                |                | total defense. |                |
+----------------+----------------+----------------+----------------+
| [              | RW             | Gets or sets   |                |
| ACTARG1](./ACTAR__________________the____________________________
_G1.md) |                | character\'s   |                |
|                |                | ACTARG1 value. |                |
|                |                | X branch only: |                |
|                |                | for skills     |                |
|                |                | Enticement,    |                |
|                |                | Peacemaking    |                |
|                |                | and            |                |
|                |                | Provocation,   |                |
|                |                | if ACTARG1 is  |                |
|                |                | set to the UID |                |
|                |                | of the         |                |
|                |                | instrument to  |                |
|                |                | play, it will  |                |
|                |                | be played the  |                |
|                |                | sound of that  |                |
|                |                | instrument.    |                |
+----------------+----------------+----------------+----------------+
| [              | RW             | Gets or sets   |                |
| ACTARG2](./ACTAR__________________the____________________________
_G2.md) |                | character\'s   |                |
|                |                | ACTARG2 value. |                |
+----------------+----------------+----------------+----------------+
| [              | RW             | Gets or sets   |                |
| ACTARG3](./ACTAR__________________the____________________________
_G3.md) |                | character\'s   |                |
|                |                | ACTARG3 value. |                |
+----------------+----------------+----------------+----------------+
| [              | RW             | Gets or sets   |                |
| ACTDIFF](./ACTDI__________________the_difficulty_________________
_FF.md) |                | of the         |                |
|                |                | character\'s   |                |
|                |                | current        |                |
|                |                | action.        |                |
+----------------+----------------+----------------+----------------+
| [ACTION](./ACTI___RW______________Gets_or_sets___________________
_ON.md) |                | the skill that |                |
|                |                | the character  |                |
|                |                | is currently   |                |
|                |                | using.         |                |
+----------------+----------------+----------------+----------------+
| [ACTP](./AC_______RW______________Gets_or_sets___________________
_TP.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | ACTP value.    |                |
|                |                | Can get        |                |
|                |                | x,y,z,position |                |
|                |                | of the point   |                |
|                |                | in X branch.   |                |
+----------------+----------------+----------------+----------------+
| [ACTPRV](./ACTP___RW______________Gets_or_sets___________________
_RV.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | ACTPRV value.  |                |
+----------------+----------------+----------------+----------------+
| [ADDHOUSE      | W              | X branch only. |                |
| u              |                | Adds the given |                |
| id](./ADDHOUSE_u__________________uid_to_the_____________________
_id.md) |                | player\'s      |                |
|                |                | house. If the  |                |
|                |                | player current |                |
|                |                | count of       |                |
|                |                | houses is      |                |
|                |                | greater than   |                |
|                |                | the limit he   |                |
|                |                | has, the house |                |
|                |                | will be        |                |
|                |                | redeeded.      |                |
+----------------+----------------+----------------+----------------+
| [ADDSHIP       | W              | X branch only. |                |
| uid](./ADDSHIP_u__________________Adds_the_given_________________
_id.md) |                | uid to the     |                |
|                |                | player\'s      |                |
|                |                | ship. If the   |                |
|                |                | player current |                |
|                |                | count of ships |                |
|                |                | is greater     |                |
|                |                | than the limit |                |
|                |                | he has, the    |                |
|                |                | ship will be   |                |
|                |                | redeeded.      |                |
+----------------+----------------+----------------+----------------+
| [AFK](./A_________W_______________Gets_or_sets___________________
_FK.md) |                | whether or not |                |
|                |                | the character  |                |
|                |                | is in AFK      |                |
|                |                | mode.          |                |
+----------------+----------------+----------------+----------------+
| [AGE](./A_________R_______________Returns_the____________________
_GE.md) |                | age of the     |                |
|                |                | character      |                |
|                |                | since its      |                |
|                |                | creation, in   |                |
|                |                | seconds.       |                |
+----------------+----------------+----------------+----------------+
| [ALLS          | W              | Sets all of    |                |
| KILLS](./ALLSKIL__________________the____________________________
_LS.md) |                | character\'s   |                |
| *amount*       |                | skills to the  |                |
|                |                | specified      |                |
|                |                | amount.        |                |
+----------------+----------------+----------------+----------------+
| [ANIM](./AN_______W_______________Plays_the______________________
_IM.md) |                | specified      |                |
| *anim_id*      |                | animation on   |                |
|                |                | the character. |                |
+----------------+----------------+----------------+----------------+
| [A             | R              | Gets the       |                |
| TTACKER](ATTAC |                | number of      |                |
| KER "wikilink" |                | opponents who  |                |
| )*.properties* |                | have damaged   |                |
|                |                | the character. |                |
+----------------+----------------+----------------+----------------+
| [BANK](./BA_______W_______________Opens_the______________________
_NK.md) |                | character\'s   |                |
| *layer*        |                | bank (or the   |                |
|                |                | container at   |                |
|                |                | the specified  |                |
|                |                | layer) for SRC |                |
|                |                | to view.       |                |
+----------------+----------------+----------------+----------------+
| [BANKBALA      | R              | Returns the    |                |
| NCE](./BANKBALAN__________________total_amount___________________
_CE.md) |                | of gold in the |                |
|                |                | character\'s   |                |
|                |                | bankbox.       |                |
+----------------+----------------+----------------+----------------+
| [BARK](./BA_______W_______________Plays_the______________________
_RK.md) |                | specified      |                |
| *sound_id*     |                | sound (or the  |                |
|                |                | character\'s   |                |
|                |                | generic sound  |                |
|                |                | if not         |                |
|                |                | specified) to  |                |
|                |                | nearby clients |                |
|                |                | from this      |                |
|                |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [BODY](./BO_______RW______________Gets_or_sets___________________
_DY.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | body.          |                |
+----------------+----------------+----------------+----------------+
| [BOUNCE](./BOUN___W_______________Places_a_______________________
_CE.md) |                | specified item |                |
| *item_uid*     |                | in the         |                |
|                |                | character\'s   |                |
|                |                | backpack.      |                |
+----------------+----------------+----------------+----------------+
| [BOW](./B_________W_______________Makes_the______________________
_OW.md) |                | character bow  |                |
|                |                | to SRC.        |                |
+----------------+----------------+----------------+----------------+
| [CAN](         | RW             | Gets or Sets   |                |
| CAN_(Character |                | the Can flags  |                |
| s) "wikilink") |                | for this       |                |
|                |                | chardef. Only  |                |
|                |                | readable in X  |                |
|                |                | branch.        |                |
+----------------+----------------+----------------+----------------+
| [              | R              | Returns 1 if   |                |
| CANCAST](./CANCA__________________the_character__________________
_ST.md) |                | can cast a     |                |
| *spell_id,     |                | given spell,   |                |
| ch             |                | bypassing      |                |
| eck_antimagic* |                | anti-magic     |                |
|                |                | field tests if |                |
|                |                | *ch            |                |
|                |                | eck_antimagic* |                |
|                |                | set to 0.      |                |
+----------------+----------------+----------------+----------------+
| [              | R              | Returns 1 if   |                |
| CANMAKE](./CANMA__________________the_character__________________
_KE.md) |                | has the skills |                |
| *item_id*      |                | and resources  |                |
|                |                | to craft a     |                |
|                |                | certain item.  |                |
+----------------+----------------+----------------+----------------+
| [CANMAKESKI    | R              | Returns 1 if   |                |
| LL](./CANMAKESKI__________________the_character__________________
_LL.md) |                | has the skills |                |
| *item_id*      |                | to craft a     |                |
|                |                | certain item.  |                |
+----------------+----------------+----------------+----------------+
| [CANMASK](CANM | RW             | X branch only. |                |
| ASK_(Character |                | Stores the CAN |                |
| s) "wikilink") |                | flags to be    |                |
|                |                | dynamically    |                |
|                |                | switched on or |                |
|                |                | off from the   |                |
|                |                | base CAN       |                |
|                |                | property.      |                |
+----------------+----------------+----------------+----------------+
| [              | R              | Returns 1 if   |                |
| CANMOVE](./CANMO__________________the_character__________________
_VE.md) |                | can move in    |                |
| *direction*    |                | the given      |                |
|                |                | direction.     |                |
+----------------+----------------+----------------+----------------+
| [CANSEE](./CANS___R_______________Returns_1_if___________________
_EE.md) |                | SRC can see    |                |
|                |                | the character. |                |
+----------------+----------------+----------------+----------------+
| [CANS          | R              | Returns 1 if   |                |
| EELOS](./CANSEEL__________________SRC_has_line___________________
_OS.md) |                | of sight to    |                |
|                |                | the character. |                |
+----------------+----------------+----------------+----------------+
| [CANSEELOSFLA  | R              | Returns 1 if   |                |
| G](./CANSEELOSFL__________________SRC_has_line___________________
_AG.md) |                | of sight to    |                |
| *flags*        |                | the character, |                |
|                |                | with flags to  |                |
|                |                | modify what    |                |
|                |                | tests take     |                |
|                |                | place.         |                |
+----------------+----------------+----------------+----------------+
| [COLOR](./COL_____RW______________Gets_or_sets___________________
_OR.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | hue.           |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Removes        |                |
| CONSUME](./CONSU__________________specified______________________
_ME.md) |                | resources from |                |
| *              |                | SRC\'s         |                |
| resource_list* |                | backpack.      |                |
+----------------+----------------+----------------+----------------+
| [COUNT](./COU_____R_______________Returns_the____________________
_NT.md) |                | number of      |                |
|                |                | items equipped |                |
|                |                | to the         |                |
|                |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [CREATE](./CREA___RW_R_only_on___Gets_or_sets___________________
_TE.md) | X)             | the            |                |
|                |                | character\'s   |                |
|                |                | age since      |                |
|                |                | creation, in   |                |
|                |                | seconds (Tenth |                |
|                |                | of seconds on  |                |
|                |                | X).            |                |
+----------------+----------------+----------------+----------------+
| [CR            | W              | Sets whether   |                |
| IMINAL](./CRIMIN__________________or_not_the_____________________
_AL.md) |                | character is a |                |
|                |                | criminal.      |                |
+----------------+----------------+----------------+----------------+
| [CURFOLLO      | RW             | Gets or sets   |                |
| WER](./CURFOLLOW__________________the_number_of__________________
_ER.md) |                | current        |                |
|                |                | followers the  |                |
|                |                | character has, |                |
+----------------+----------------+----------------+----------------+
| [DAMAGE](./DAMA___W_______________Inflicts_______________________
_GE.md) |                | damage upon    |                |
| *amount, type, |                | the character. |                |
| source*        |                |                |                |
|                |                | `When          |                |
|                |                | using COMBAT_E |                |
|                |                | LEMENTAL_ENGIN |                |
|                |                | E add the foll |                |
|                |                | owing paramete |                |
|                |                | rs after `*`so |                |
|                |                | urce`*`: `*`ph |                |
|                |                | ysical`*`,`*`f |                |
|                |                | ire`*`,`*`cold |                |
|                |                | `*`,`*`poison` |                |
|                |                | *`,`*`energy`* |                |
|                |                | `. All the val |                |
|                |                | ues are in %.` |                |
+----------------+----------------+----------------+----------------+
| [DELHOUSE      | W              | X branch only. |                |
| u              |                | Deletes the    |                |
| id](./DELHOUSE_u__________________given_uid_from_________________
_id.md) |                | the player\'s  |                |
|                |                | list (Will not |                |
|                |                | delete the     |                |
|                |                | house)(-1      |                |
|                |                | clears the     |                |
|                |                | whole list).   |                |
+----------------+----------------+----------------+----------------+
| [DELSHIP       | W              | X branch only. |                |
| uid](./DELSHIP_u__________________Deletes_the____________________
_id.md) |                | given uid from |                |
|                |                | the player\'s  |                |
|                |                | list (Will not |                |
|                |                | delete the     |                |
|                |                | ship)(-1       |                |
|                |                | clears the     |                |
|                |                | whole list).   |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Deletes the    |                |
| DESTROY](./DESTR__________________object_not____________________
_OY.md) |                | stopped by a   |                |
|                |                | return 1 in    |                |
|                |                | [\@D           |                |
|                |                | estroy](./Destr_________________
_________________________________oy.md) |                |
+----------------+----------------+----------------+----------------+
| [DEX](./D_________RW______________Gets_or_sets___________________
_EX.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | total          |                |
|                |                | dexterity.     |                |
+----------------+----------------+----------------+----------------+
| [DIALOG](D     | W              | Displays a     |                |
| IALOG_(Functio |                | dialog to SRC. |                |
| n) "wikilink") |                |                |                |
| *dialog_id,    |                |                |                |
| page,          |                |                |                |
| parameters*    |                |                |                |
+----------------+----------------+----------------+----------------+
| [DIALOGCL      | W              | Closes a       |                |
| OSE](./DIALOGCLO__________________dialog_that____________________
_SE.md) |                | SRC has open,  |                |
| *dialog_id     |                | simulating a   |                |
| button*        |                | button press.  |                |
+----------------+----------------+----------------+----------------+
| [              | R              | Gets the       |                |
| DIALOGLIST](DI |                | number of      |                |
| ALOGLIST "wiki |                | number of      |                |
| link")*.COUNT* |                | dialogs        |                |
|                |                | currently      |                |
|                |                | considered to  |                |
|                |                | be visible on  |                |
|                |                | SRC\'s screen. |                |
+----------------+----------------+----------------+----------------+
| [DIALOGLIST](D | R              | Gets the ID of |                |
| IALOGLIST "wik |                | the nth dialog |                |
| ilink")*.n.ID* |                | that SRC has   |                |
|                |                | open           |                |
|                |                | (zero-based).  |                |
+----------------+----------------+----------------+----------------+
| [DI            | R              | Gets the       |                |
| ALOGLIST](DIAL |                | number of      |                |
| OGLIST "wikili |                | instances of   |                |
| nk")*.n.COUNT* |                | nth dialog SRC |                |
|                |                | has open       |                |
|                |                | (zero-based).  |                |
+----------------+----------------+----------------+----------------+
| [DIR](./D_________RW______________Gets_or_setes__________________
_IR.md) |                | the direction  |                |
|                |                | that the       |                |
|                |                | character is   |                |
|                |                | facing.        |                |
+----------------+----------------+----------------+----------------+
| [DISCON        | W              | Disconnects    |                |
| NECT](./DISCONNE__________________the_character_________________
_CT.md) |                |                |                |
+----------------+----------------+----------------+----------------+
| [DI            | W              | Dismounts the  |                |
| SMOUNT](./DISMOU__________________character_from_________________
_NT.md) |                | their ride.    |                |
+----------------+----------------+----------------+----------------+
| [DISP          | R              | Gets the ID of |                |
| IDDEC](./DISPIDD__________________the_character__________________
_EC.md) |                | as a decimal   |                |
|                |                | number.        |                |
+----------------+----------------+----------------+----------------+
| [DI            | R              | Gets the       |                |
| STANCE](./DISTAN__________________distance_______________________
_CE.md) |                | between this   |                |
| *point_or_uid* |                | object and     |                |
|                |                | either SRC, a  |                |
|                |                | map location   |                |
|                |                | or another     |                |
|                |                | object.        |                |
+----------------+----------------+----------------+----------------+
| [DCLICK](./DCLI___W_______________Double_clicks__________________
_CK.md) |                | the character, |                |
|                |                | with SRC as    |                |
|                |                | the source of  |                |
|                |                | the event.     |                |
+----------------+----------------+----------------+----------------+
| [DCLICK](./DCLI___W_______________Double_clicks__________________
_CK.md) |                | an object,     |                |
| *object_uid*   |                | with the       |                |
|                |                | character as   |                |
|                |                | SRC.           |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Starts the     |                |
| DRAWMAP](./DRAWM__________________cartography____________________
_AP.md) |                | skill, drawing |                |
| *radius*       |                | a map of the   |                |
|                |                | local area up  |                |
|                |                | to *radius*    |                |
|                |                | tiles.         |                |
+----------------+----------------+----------------+----------------+
| [DROP](./DR_______W_______________Drops_a________________________
_OP.md) |                | specified item |                |
| *item_uid*     |                | at the         |                |
|                |                | character\'s   |                |
|                |                | feet.          |                |
+----------------+----------------+----------------+----------------+
| [DUPE](./DU_______W_______________Creates_a______________________
_PE.md) |                | clone of the   |                |
|                |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [EDIT](./ED_______W_______________Displays_an____________________
_IT.md) |                | editing dialog |                |
|                |                | for the        |                |
|                |                | character to   |                |
|                |                | SRC.           |                |
+----------------+----------------+----------------+----------------+
| [EFFECT](./EFFE___W_______________Displays_an____________________
_CT.md) |                | effect to      |                |
| *type,         |                | nearby         |                |
| item_id,       |                | clients.       |                |
| speed, loop,   |                |                |                |
| explode,       |                |                |                |
| color,         |                |                |                |
| rendermode*    |                |                |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Similar to the | X              |
| EFFECTLOCATION |                | EFFECT command |                |
| ](./EFFECTLOCATI__________________but_instead_of_________________
_ON.md) |                | an object it   |                |
| *x,y,z,ty      |                | takes a        |                |
| pe,itemid,spee |                | terrain        |                |
| d,loop,explode |                | location as a  |                |
| ,color,render* |                | target.        |                |
+----------------+----------------+----------------+----------------+
| [EMOTE](./EMO_____W_______________Displays_a_____________________
_TE.md) |                | \*You see\*    |                |
| *message*      |                | message to all |                |
|                |                | nearby         |                |
|                |                | clients.       |                |
+----------------+----------------+----------------+----------------+
| [EM            | RW             | Gets, sets or  |                |
| OTEACT](./EMOTEA__________________toggles________________________
_CT.md) |                | whether or not |                |
|                |                | the character  |                |
|                |                | will emote all |                |
|                |                | of its         |                |
|                |                | actions.       |                |
+----------------+----------------+----------------+----------------+
| [EQUIP](./EQU_____W_______________Equips_an_item_________________
_IP.md) |                | to the         |                |
| *item_uid*     |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [EQUIPA        | W              | Equips the     |                |
| RMOR](./EQUIPARM__________________character_with_________________
_OR.md) |                | the best       |                |
|                |                | armour in      |                |
|                |                | their          |                |
|                |                | backpack.      |                |
+----------------+----------------+----------------+----------------+
| [EQUI          | W              | Equips a halo  |                |
| PHALO](./EQUIPHA__________________light_to_the___________________
_LO.md) |                | character,     |                |
| *timeout*      |                | lasting for    |                |
|                |                | *timeout*      |                |
|                |                | tenths of a    |                |
|                |                | second.        |                |
+----------------+----------------+----------------+----------------+
| [EQUIPWEA      | W              | Equips the     |                |
| PON](./EQUIPWEAP__________________character_with_________________
_ON.md) |                | the best       |                |
|                |                | weapon in      |                |
|                |                | their          |                |
|                |                | backpack.      |                |
+----------------+----------------+----------------+----------------+
| [EVENTS](E     | RW             | Gets a list of |                |
| VENTS_(Propert |                | events         |                |
| y) "wikilink") |                | attached to    |                |
| *              |                | the object, or |                |
| event_defname* |                | adds or        |                |
|                |                | removes an     |                |
|                |                | event to or    |                |
|                |                | from the       |                |
|                |                | object.        |                |
+----------------+----------------+----------------+----------------+
| [EXP](./E_________RW______________Gets_or_sets___________________
_XP.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | experience     |                |
|                |                | points.        |                |
+----------------+----------------+----------------+----------------+
| [FACE](./FA_______W_______________Turns_the______________________
_CE.md) |                | character to   |                |
| *object_uid*   |                | face a         |                |
| (P coords in X |                | specified      |                |
| branch)        |                | object or SRC. |                |
|                |                | Admits         |                |
|                |                | coordinates    |                |
|                |                | instead uid in |                |
|                |                | X branch.      |                |
+----------------+----------------+----------------+----------------+
| [FAME](./FA_______RW______________Gets_or_sets___________________
_ME.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | fame.          |                |
+----------------+----------------+----------------+----------------+
| [FAME](F       | R              | Returns 1 if   |                |
| AME "wikilink" |                | the            |                |
| )*.fame_group* |                | character\'s   |                |
|                |                | fame falls     |                |
|                |                | within the     |                |
|                |                | specified fame |                |
|                |                | group.         |                |
+----------------+----------------+----------------+----------------+
| [FCOUNT](./FCOU___R_______________Returns_the____________________
_NT.md) |                | total number   |                |
|                |                | of items       |                |
|                |                | equipped to    |                |
|                |                | the character, |                |
|                |                | including      |                |
|                |                | subitems       |                |
+----------------+----------------+----------------+----------------+
| [FLAGS](./FLA_____RW______________Gets_or_sets___________________
_GS.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | flags.         |                |
+----------------+----------------+----------------+----------------+
| [FIX](./F_________W_______________Re-aligns_the__________________
_IX.md) |                | character\'s Z |                |
|                |                | level to       |                |
|                |                | ground level.  |                |
+----------------+----------------+----------------+----------------+
| [FIXW          | W              | Recalculates   |                |
| EIGHT](./FIXWEIG__________________the____________________________
_HT.md) |                | character\'s   |                |
|                |                | total weight.  |                |
+----------------+----------------+----------------+----------------+
| [FLIP](./FL_______W_______________Rotates_the____________________
_IP.md) |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [FONT](./FO_______RW______________Gets_or_sets___________________
_NT.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | speech font.   |                |
+----------------+----------------+----------------+----------------+
| [FOOD](./FO_______RW______________Gets_or_sets___________________
_OD.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | food level.    |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Revokes the    |                |
| FORGIVE](./FORGI__________________characters___________________
_VE.md) |                | jailed status. |                |
+----------------+----------------+----------------+----------------+
| [GETHOUSEPOS   | R              | Returns the    |                |
| uid]           |                | position of    |                |
| (GETHOUSEPOS_u |                | the given UID  |                |
| id "wikilink") |                | on the houses  |                |
|                |                | list (-1 if    |                |
|                |                | not found).    |                |
+----------------+----------------+----------------+----------------+
| [GETSHIPPOS    | R              | Returns the    |                |
| uid            |                | position of    |                |
| ](./GETSHIPPOS_u__________________the_given_UID__________________
_id.md) |                | on the ships   |                |
|                |                | list (-1 if    |                |
|                |                | not found).    |                |
+----------------+----------------+----------------+----------------+
| [GO](./W_______________Teleports_the__________________
_GO.md) |                | character to   |                |
| *location*     |                | the specified  |                |
|                |                | location.      |                |
+----------------+----------------+----------------+----------------+
| [GOCHAR](./GOCH___W_______________Teleports_the__________________
_AR.md) |                | character to   |                |
| *n*            |                | the nth        |                |
|                |                | character in   |                |
|                |                | the world.     |                |
+----------------+----------------+----------------+----------------+
| [GO            | W              | Teleports the  |                |
| CHARID](./GOCHAR__________________character_to___________________
_ID.md) |                | the next       |                |
| *char          |                | characer in    |                |
| acter_defname* |                | the world with |                |
|                |                | the specified  |                |
|                |                | [BASEID](./BASE__________________
_________________________________ID.md) |                |
+----------------+----------------+----------------+----------------+
| [GOCLI](./GOC_____W_______________Teleports_the__________________
_LI.md) |                | character to   |                |
| *n*            |                | the nth online |                |
|                |                | player.        |                |
|                |                | (zero-based)   |                |
+----------------+----------------+----------------+----------------+
| [GO            | W              | Teleports the  |                |
| ITEMID](./GOITEM__________________character_to___________________
_ID.md) |                | the next item  |                |
| *item_defname* |                | in the world   |                |
|                |                | with the       |                |
|                |                | specified      |                |
|                |                | [BASEID](./BASEI_________________
_________________________________D.md). |                |
+----------------+----------------+----------------+----------------+
| [GOLD](./GO_______RW______________Gets_or_sets___________________
_LD.md) |                | the amount of  |                |
|                |                | gold the       |                |
|                |                | character has. |                |
+----------------+----------------+----------------+----------------+
| [GONAME](./GONA___W_______________Teleports_the__________________
_ME.md) |                | character to   |                |
| *name*         |                | the next       |                |
|                |                | character or   |                |
|                |                | item in the    |                |
|                |                | world with the |                |
|                |                | specified      |                |
|                |                | name, accepts  |                |
|                |                | wildcards      |                |
|                |                | (\*).          |                |
+----------------+----------------+----------------+----------------+
| [GOSOCK](./GOSO___W_______________Teleports_the__________________
_CK.md) |                | character to   |                |
| *socket*       |                | the online     |                |
|                |                | player with    |                |
|                |                | the specified  |                |
|                |                | socket number. |                |
+----------------+----------------+----------------+----------------+
| [GOTYPE](./GOTY___W_______________Teleports_the__________________
_PE.md) |                | character to   |                |
| *item_type*    |                | the next item  |                |
|                |                | in the world   |                |
|                |                | with the       |                |
|                |                | specified      |                |
|                |                | [TYPE](./TYP_____________________
_________________________________E.md). |                |
+----------------+----------------+----------------+----------------+
| [GOUID](./GOU_____W_______________Teleports_the__________________
_ID.md) |                | character to   |                |
| *object_uid*   |                | the object     |                |
|                |                | with the       |                |
|                |                | specified      |                |
|                |                | [UID](./UI_______________________
_________________________________D.md). |                |
+----------------+----------------+----------------+----------------+
| [GUILDABB      | R              | Returns the    |                |
| REV](./GUILDABBR__________________characters___________________
_EV.md) |                | guild          |                |
|                |                | abbreviation.  |                |
+----------------+----------------+----------------+----------------+
| [HEAR](./HE_______W_______________For_NPCs_acts_________________
_AR.md) |                | as if SRC had  |                |
| *text*         |                | spoken the     |                |
|                |                | specified      |                |
|                |                | *text*. For    |                |
|                |                | players,       |                |
|                |                | displays       |                |
|                |                | *text* as a    |                |
|                |                | system         |                |
|                |                | message.       |                |
+----------------+----------------+----------------+----------------+
| [HEIGHT](./HEIG___R_______________Gets_the_______________________
_HT.md) |                | character\'s   |                |
|                |                | height.        |                |
+----------------+----------------+----------------+----------------+
| [HITS](./HI_______RW______________Gets_or_sets___________________
_TS.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | hitpoints.     |                |
+----------------+----------------+----------------+----------------+
| [HOME](./HO_______RW______________Gets_or_sets___________________
_ME.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | home location. |                |
+----------------+----------------+----------------+----------------+
| [              | R              | X branch       |                |
| HOUSE.n](./HOUSE__________________onlyAccess____________________
_n.md) |                | the house in   |                |
|                |                | the Nth        |                |
|                |                | position, eg:  |                |
|                |                | house.3.Redeed |                |
+----------------+----------------+----------------+----------------+
| [HOUSES](./HOUS___R_______________X_branch_only_________________
_ES.md) |                | Returns the    |                |
|                |                | number of      |                |
|                |                | houses on the  |                |
|                |                | player\'s      |                |
|                |                | list.          |                |
+----------------+----------------+----------------+----------------+
| [HUNGRY](./HUNG___W_______________Displays_this__________________
_RY.md) |                | character\'s   |                |
|                |                | hunger level   |                |
|                |                | to SRC.        |                |
+----------------+----------------+----------------+----------------+
| [ID](./R_______________Gets_the_______________________
_ID.md) |                | character\'s   |                |
|                |                | ID.            |                |
+----------------+----------------+----------------+----------------+
| [INFO](./IN_______W_______________Displays_an____________________
_FO.md) |                | information    |                |
|                |                | dialog about   |                |
|                |                | the character  |                |
|                |                | to SRC.        |                |
+----------------+----------------+----------------+----------------+
| [INT](./I_________RW______________Gets_or_sets___________________
_NT.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | total          |                |
|                |                | intelligence.  |                |
+----------------+----------------+----------------+----------------+
| [INVIS](./INV_____W_______________Sets_whether___________________
_IS.md) |                | or not the     |                |
|                |                | character is   |                |
|                |                | invisible.     |                |
+----------------+----------------+----------------+----------------+
| [INVUL](./INV_____W_______________Sets_whether___________________
_UL.md) |                | or not the     |                |
|                |                | character is   |                |
|                |                | invulnerable.  |                |
+----------------+----------------+----------------+----------------+
| [              | R              | Returns 1 if   |                |
| ISARMOR](./ISARM__________________the_object_is__________________
_OR.md) |                | armour.        |                |
| *object_uid*   |                |                |                |
+----------------+----------------+----------------+----------------+
| [ISCHAR](./ISCH___R_______________Returns_1_if___________________
_AR.md) |                | the object is  |                |
|                |                | a character.   |                |
+----------------+----------------+----------------+----------------+
| [ISCONT](./ISCO___R_______________Returns_1_if___________________
_NT.md) |                | the object is  |                |
|                |                | a container.   |                |
+----------------+----------------+----------------+----------------+
| [ISDIALOGOP    | R              | Returns 1 if   |                |
| EN](./ISDIALOGOP__________________SRC_has_the____________________
_EN.md) |                | specified      |                |
| *dialog_id*    |                | dialog visible |                |
|                |                | on their       |                |
|                |                | screen.        |                |
+----------------+----------------+----------------+----------------+
| [IS            | R              | Returns 1 if   |                |
| EVENT](./ISEVENT__________________the_object_has.md)*. |                | an event       |                |
| event_defname* |                | attached to    |                |
|                |                | it.            |                |
+----------------+----------------+----------------+----------------+
| [ISGM](./IS_______R_______________Returns_1_if___________________
_GM.md) |                | the character  |                |
|                |                | is in GM mode. |                |
+----------------+----------------+----------------+----------------+
| [ISIN          | R              | Returns 1 if   |                |
| PARTY](./ISINPAR__________________the_player_is__________________
_TY.md) |                | in a           |                |
|                |                | [party](./part___________________
_________________________________y.md). |                |
+----------------+----------------+----------------+----------------+
| [ISITEM](./ISIT___R_______________Returns_1_if___________________
_EM.md) |                | the object is  |                |
|                |                | an item.       |                |
+----------------+----------------+----------------+----------------+
| [              | R              | Returns 1 if   |                |
| ISMYPET](./ISMYP__________________the_character__________________
_ET.md) |                | belongs to     |                |
|                |                | SRC.           |                |
+----------------+----------------+----------------+----------------+
| [ISNEAR        | R              | Returns 1 if a |                |
| TYPE](./ISNEARTY__________________nearby_item____________________
_PE.md) |                | has the given  |                |
| *type,         |                | TYPE.          |                |
| distance,      |                |                |                |
| flags*         |                |                |                |
+----------------+----------------+----------------+----------------+
| [ISNEARTYPETO  | R              | Returns a      |                |
| P](./ISNEARTYPET__________________nearby_world___________________
_OP.md) |                | location of a  |                |
| *type,         |                | nearby item    |                |
| distance,      |                | which has the  |                |
| flags*         |                | given TYPE.    |                |
+----------------+----------------+----------------+----------------+
| [IS            | R              | Returns 1 if   |                |
| ONLINE](./ISONLI__________________the_character__________________
_NE.md) |                | is considered  |                |
|                |                | to be online.  |                |
+----------------+----------------+----------------+----------------+
| [IS            | R              | Returns 1 if   |                |
| PLAYER](./ISPLAY__________________the_object_is__________________
_ER.md) |                | a player.      |                |
+----------------+----------------+----------------+----------------+
| [              | R              | Returns 1 if   |                |
| ISSTUCK](./ISSTU__________________the_character__________________
_CK.md) |                | cannot walk in |                |
|                |                | any direction. |                |
+----------------+----------------+----------------+----------------+
| [ISTE          | R              | Returns 1 if   |                |
| VENT](./ISTEVENT__________________the_object_has.md)*. |                | an event       |                |
| event_defname* |                | attached to    |                |
|                |                | its            |                |
|                |                | [C             |                |
|                |                | HARDEF](./CHARDE_________________
_________________________________F.md). |                |
+----------------+----------------+----------------+----------------+
| [ISTIMERF](IST | R              | Returns the    |                |
| IMERF "wikilin |                | number of      |                |
| k")*.function* |                | seconds left   |                |
|                |                | on the         |                |
|                |                | specified      |                |
|                |                | timerf if it   |                |
|                |                | exists.        |                |
+----------------+----------------+----------------+----------------+
| [IS            | R              | Returns 1 if   |                |
| VENDOR](./ISVEND__________________the_character__________________
_OR.md) |                | is a vendor.   |                |
+----------------+----------------+----------------+----------------+
| [IS            | R              | Returns 1 if   |                |
| VERTICALSPACE] |                | the ceiling at |                |
| (ISVERTICALSPA |                | the given      |                |
| CE "wikilink") |                | location is    |                |
| *location*     |                | high enough    |                |
|                |                | for the        |                |
|                |                | character to   |                |
|                |                | fit under.     |                |
+----------------+----------------+----------------+----------------+
| [IS            | R              | Returns 1 if   |                |
| WEAPON](./ISWEAP__________________the_object_is__________________
_ON.md) |                | a weapon.      |                |
| *object_uid*   |                |                |                |
+----------------+----------------+----------------+----------------+
| [JAIL](./JA_______W_______________Sends_the______________________
_IL.md) |                | character to   |                |
| *cell*         |                | jail, to a     |                |
|                |                | specified jail |                |
|                |                | cell.          |                |
+----------------+----------------+----------------+----------------+
| [KARMA](./KAR_____RW______________Gets_or_sets___________________
_MA.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | karma.         |                |
+----------------+----------------+----------------+----------------+
| [KARMA](./KAR_____R_______________Returns_1_if___________________
_MA.md) |                | the            |                |
| *.karma_group* |                | character\'s   |                |
|                |                | karma falls    |                |
|                |                | within the     |                |
|                |                | specified      |                |
|                |                | karma group.   |                |
+----------------+----------------+----------------+----------------+
| [KILL](./KI_______W_______________Kills_the______________________
_LL.md) |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [LEVEL](./LEV_____RW______________Gets_or_sets___________________
_EL.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | experience     |                |
|                |                | level.         |                |
+----------------+----------------+----------------+----------------+
| [LIGHT](./LIG_____RW______________Gets_or_sets___________________
_HT.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | personal light |                |
|                |                | level.         |                |
+----------------+----------------+----------------+----------------+
| [LUCK](./LU_______RW______________Gets_or_sets___________________
_CK.md) |                | the luck value |                |
|                |                | for the        |                |
|                |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [MA            | \| W           | Begins an      |                |
| KEITEM](./MAKEIT__________________attempt_to_____________________
_EM.md) |                | craft the      |                |
| *item_defname, |                | specified      |                |
| amount*        |                | quantity of    |                |
|                |                | the given      |                |
|                |                | item.          |                |
+----------------+----------------+----------------+----------------+
| [MANA](./MA_______RW______________Gets_or_sets___________________
_NA.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | mana.          |                |
+----------------+----------------+----------------+----------------+
| [MAP](./M_________RW______________Gets_or_sets___________________
_AP.md) |                | the map that   |                |
|                |                | this object is |                |
|                |                | located.       |                |
+----------------+----------------+----------------+----------------+
| [MAPWAYPO      | W              | Add/remove     |                |
| INT](./MAPWAYPOI__________________waypoints_on___________________
_NT.md) |                | client radar   |                |
| \"ObjectUID,   |                | map (enhanced  |                |
| WaypointType\" |                | clients only). |                |
+----------------+----------------+----------------+----------------+
| [MAXFOLLO      | RW             | Gets or sets   |                |
| WER](./MAXFOLLOW__________________the_maximum____________________
_ER.md) |                | number of      |                |
|                |                | followers the  |                |
|                |                | character can  |                |
|                |                | have.          |                |
+----------------+----------------+----------------+----------------+
| [              | RW             | Gets or sets   |                |
| MAXHITS](./MAXHI__________________the____________________________
_TS.md) |                | character\'s   |                |
|                |                | maximum        |                |
|                |                | hitpoints.     |                |
+----------------+----------------+----------------+----------------+
| [MAXH          | RW             | Added to       | X              |
| OUSES](./MAXHOUS__________________Accounts_and___________________
_ES.md) |                | Chars, when    |                |
|                |                | created they   |                |
|                |                | read this      |                |
|                |                | setting from   |                |
|                |                | the sphere.ini |                |
|                |                | (if values on  |                |
|                |                | sphere.ini     |                |
|                |                | change, they   |                |
|                |                | will not       |                |
|                |                | reflect on     |                |
|                |                | already        |                |
|                |                | created        |                |
|                |                | ac             |                |
|                |                | counts/chars). |                |
+----------------+----------------+----------------+----------------+
| [              | RW             | Gets or sets   |                |
| MAXMANA](./MAXMA__________________the____________________________
_NA.md) |                | character\'s   |                |
|                |                | maximum mana.  |                |
+----------------+----------------+----------------+----------------+
| [MA            | RW             | Added Accounts | X              |
| XSHIPS](./MAXSHI__________________and_Chars_____________________
_PS.md) |                | when created   |                |
|                |                | they read this |                |
|                |                | new setting    |                |
|                |                | from the       |                |
|                |                | sphere.ini (if |                |
|                |                | values on      |                |
|                |                | sphere.ini     |                |
|                |                | change, they   |                |
|                |                | will not       |                |
|                |                | reflect on     |                |
|                |                | already        |                |
|                |                | created        |                |
|                |                | ac             |                |
|                |                | counts/chars). |                |
+----------------+----------------+----------------+----------------+
| [              | RW             | Gets or sets   |                |
| MAXSTAM](./MAXST__________________the____________________________
_AM.md) |                | character\'s   |                |
|                |                | maximum        |                |
|                |                | stamina.       |                |
+----------------+----------------+----------------+----------------+
| [MAXW          | R              | Returns the    |                |
| EIGHT](./MAXWEIG__________________maximum_weight_________________
_HT.md) |                | that the       |                |
|                |                | character can  |                |
|                |                | carry.         |                |
+----------------+----------------+----------------+----------------+
| [MEMORY](MEM   | RW             | Gets or sets   |                |
| ORY "wikilink" |                | the memory     |                |
| )*.object_uid* |                | flags the      |                |
|                |                | character has  |                |
|                |                | for the given  |                |
|                |                | object.        |                |
+----------------+----------------+----------------+----------------+
| [MENU]         | W              | Displays a     |                |
| (MENU_(Functio |                | menu to SRC.   |                |
| n) "wikilink") |                |                |                |
| *menu_defname* |                |                |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Displays a     |                |
| MESSAGE](./MESSA__________________message_above__________________
_GE.md) |                | this character |                |
| *message*      |                | to SRC.        |                |
+----------------+----------------+----------------+----------------+
| [MESS          | W              | Displays a     |                |
| AGEUA](./MESSAGE__________________UNICODE________________________
_UA.md) |                | message above  |                |
| *colour,       |                | this character |                |
| talkmode,      |                | to SRC.        |                |
| font, lang_id, |                |                |                |
| message*       |                |                |                |
+----------------+----------------+----------------+----------------+
| [MODAR](./MOD_____RW______________Gets_or_sets_a_________________
_AR.md) |                | modifier for   |                |
|                |                | the            |                |
|                |                | character\'s   |                |
|                |                | armour rating. |                |
+----------------+----------------+----------------+----------------+
| [MODDEX](./MODD___RW______________Gets_or_sets___________________
_EX.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | dexterity      |                |
|                |                | modifier.      |                |
+----------------+----------------+----------------+----------------+
| [MODINT](./MODI___RW______________Gets_or_sets___________________
_NT.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | intelligence   |                |
|                |                | modifier.      |                |
+----------------+----------------+----------------+----------------+
| [MODMAXWEIG    | RW             | Gets or sets   |                |
| HT](./MODMAXWEIG__________________the____________________________
_HT.md) |                | character\'s   |                |
|                |                | maximum weight |                |
|                |                | modifier.      |                |
+----------------+----------------+----------------+----------------+
| [MODSTR](./MODS___RW______________Gets_or_sets___________________
_TR.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | strength       |                |
|                |                | modifier.      |                |
+----------------+----------------+----------------+----------------+
| [MOUNT](./MOU_____R_______________Gets_the_UID___________________
_NT.md) |                | of the         |                |
|                |                | character\'s   |                |
|                |                | mount.         |                |
+----------------+----------------+----------------+----------------+
| [MOUNT](./MOU_____W_______________Attempts_to____________________
_NT.md) |                | mount the      |                |
| *mount_uid*    |                | character on   |                |
|                |                | to the         |                |
|                |                | specified      |                |
|                |                | mount.         |                |
+----------------+----------------+----------------+----------------+
| [MOVE](./MO_______R_______________Returns_the____________________
_VE.md) |                | movement flags |                |
| *direction*    |                | for the tile   |                |
|                |                | in the given   |                |
|                |                | direction (see |                |
|                |                | can_flags in   |                |
|                |                | sph            |                |
|                |                | ere_defs.scp). |                |
+----------------+----------------+----------------+----------------+
| [MOVE](./MO_______W_______________Moves_the______________________
_VE.md) |                | object         |                |
| *direction,    |                | relative to    |                |
| amount*\       |                | its current    |                |
| [MOVE](./MO_______________________position______________________
_VE.md) |                |                |                |
| *x y*          |                |                |                |
+----------------+----------------+----------------+----------------+
| [MO            | W              | Moves the      |                |
| VENEAR](./MOVENE__________________character_to_a_________________
_AR.md) |                | random         |                |
| *object_uid,   |                | location near  |                |
| distance*      |                | another object |                |
|                |                | within a       |                |
|                |                | certain        |                |
|                |                | distance.      |                |
+----------------+----------------+----------------+----------------+
| [MOVETO](./MOVE___W_______________Moves_the______________________
_TO.md) |                | character to a |                |
| *location*     |                | specific       |                |
|                |                | location.      |                |
+----------------+----------------+----------------+----------------+
| [NAME](./NA_______RW______________Gets_or_sets___________________
_ME.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | name.          |                |
+----------------+----------------+----------------+----------------+
| [NEWBIESK      | W              | Distributes    |                |
| ILL](./NEWBIESKI__________________items_that_are_________________
_LL.md) |                | associated     |                |
| *skill_id*     |                | with the       |                |
|                |                | specified      |                |
|                |                | skill, to the  |                |
|                |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Generates      |                |
| NEWGOLD](./NEWGO__________________amount_gold__________________
_LD.md) |                | in the         |                |
| *amount*       |                | character\'s   |                |
|                |                | backpack.      |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Generates the  |                |
| NEWLOOT](./NEWLO__________________specified_item_________________
_OT.md) |                | or template    |                |
| *item_or_tem   |                | into the       |                |
| plate_defname* |                | character\'s   |                |
|                |                | backpack,      |                |
|                |                | providing that |                |
|                |                | they are an    |                |
|                |                | NPC that       |                |
|                |                | hasn\'t been   |                |
|                |                | summoned.      |                |
+----------------+----------------+----------------+----------------+
| [NIGHTS        | RW             | Gets or sets   |                |
| IGHT](./NIGHTSIG__________________whether_or_not_________________
_HT.md) |                | the character  |                |
|                |                | has nightsight |                |
|                |                | enabled.       |                |
+----------------+----------------+----------------+----------------+
| [NOTOGETF      | RW             | Gets the       |                |
| LAG](./NOTOGETFL__________________characters___________________
_AG.md) |                | notoriety      |                |
| *viewer_uid,   |                | flags as seen  |                |
| al             |                | by the         |                |
| low_incognito* |                | specified      |                |
|                |                | viewer.        |                |
+----------------+----------------+----------------+----------------+
| [NPC](./N_________RW______________Gets_or_sets___________________
_PC.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | AI type.       |                |
+----------------+----------------+----------------+----------------+
| [NUDG          | W              | Decreases the  |                |
| EDOWN](./NUDGEDO__________________characters_Z_________________
_WN.md) |                | level.         |                |
| *amount*       |                |                |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Increases the  |                |
| NUDGEUP](./NUDGE__________________characers_Z__________________
_UP.md) |                | level.         |                |
| *amount*       |                |                |                |
+----------------+----------------+----------------+----------------+
| [OBODY](./OBO_____RW______________Gets_or_sets___________________
_DY.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | original body. |                |
+----------------+----------------+----------------+----------------+
| [OPENPAPERDOL  | W              | Displays the   |                |
| L](./OPENPAPERDO__________________characters___________________
_LL.md) |                | paperdoll to   |                |
|                |                | SRC.           |                |
+----------------+----------------+----------------+----------------+
| [OPENPAPERDOL  | W              | Displays a     |                |
| L](./OPENPAPERDO__________________specified______________________
_LL.md) |                | character\'s   |                |
| *              |                | paperdoll to   |                |
| character_uid* |                | this           |                |
|                |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [OSKIN](./OSK_____RW______________Gets_or_sets___________________
_IN.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | original       |                |
|                |                | colour.        |                |
+----------------+----------------+----------------+----------------+
| [ODEX](./OD_______RW______________Gets_or_sets___________________
_EX.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | base dexterity |                |
|                |                | (without       |                |
|                |                | modifiers).    |                |
+----------------+----------------+----------------+----------------+
| [OINT](./OI_______RW______________Gets_or_sets___________________
_NT.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | base           |                |
|                |                | intelligence   |                |
|                |                | (without       |                |
|                |                | modifiers).    |                |
+----------------+----------------+----------------+----------------+
| [OSTR](./OS_______RW______________Gets_or_sets___________________
_TR.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | base strength  |                |
|                |                | (without       |                |
|                |                | modifiers).    |                |
+----------------+----------------+----------------+----------------+
| [PACK](./PA_______W_______________Opens_the______________________
_CK.md) |                | character\'s   |                |
|                |                | backpack for   |                |
|                |                | SRC to view.   |                |
+----------------+----------------+----------------+----------------+
| [POISON](./POIS___W_______________Poisons_the____________________
_ON.md) |                | character,     |                |
| *strength*     |                | with the       |                |
|                |                | specified      |                |
|                |                | poison         |                |
|                |                | strength.      |                |
+----------------+----------------+----------------+----------------+
| [POLY](./PO_______W_______________Begins_casting_________________
_LY.md) |                | the polymorph  |                |
| *character_id* |                | spell, with    |                |
|                |                | *character_id* |                |
|                |                | being the      |                |
|                |                | character to   |                |
|                |                | turn into.     |                |
+----------------+----------------+----------------+----------------+
| [PROMPTCONSOL  | W              | Displays a     |                |
| E](./PROMPTCONSO__________________prompt_message_________________
_LE.md) |                | to SRC and     |                |
| *function,     |                | passes their   |                |
| p              |                | response into  |                |
| rompt_message* |                | a specified    |                |
|                |                | function.      |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Displays a     |                |
| PROMPTCONSOLEU |                | prompt message |                |
| ](./PROMPTCONSOL__________________to_SRC_and_____________________
_EU.md) |                | passes their   |                |
| *function,     |                | response into  |                |
| p              |                | a specified    |                |
| rompt_message* |                | function,      |                |
|                |                | supporting     |                |
|                |                | UNICODE        |                |
|                |                | response.      |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Sets the       |                |
| PRIVSET](./PRIVS__________________PLEVEL_of_the__________________
_ET.md) |                | character.     |                |
| *plevel*       |                |                |                |
+----------------+----------------+----------------+----------------+
| [RANGE](./RAN_____R_______________Gets_the_______________________
_GE.md) |                | combat range   |                |
|                |                | of the         |                |
|                |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Clears the     |                |
| RELEASE](./RELEA__________________characters___________________
_SE.md) |                | owners.        |                |
+----------------+----------------+----------------+----------------+
| [REMOVE](./REMO___W_______________Deletes_the____________________
_VE.md) |                | character.     |                |
| *allow_p       |                |                |                |
| layer_removal* |                |                |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Removes the    |                |
| REMOVEFROMVIEW |                | object from    |                |
| ](./REMOVEFROMVI__________________nearby_________________________
_EW.md) |                | clients\'      |                |
|                |                | screens.       |                |
+----------------+----------------+----------------+----------------+
| [              | RW             | Gets or sets   |                |
| RESCOLD](./RESCO__________________the____________________________
_LD.md) |                | character\'s   |                |
|                |                | resistance to  |                |
|                |                | cold.          |                |
+----------------+----------------+----------------+----------------+
| [RESCOL        | RW             | Gets or sets   |                |
| DMAX](./RESCOLDM__________________the____________________________
_AX.md) |                | character\'s   |                |
|                |                | maximum        |                |
|                |                | resistance to  |                |
|                |                | cold.          |                |
+----------------+----------------+----------------+----------------+
| [RE            | R              | Returns the    |                |
| SCOUNT](./RESCOU__________________total_amount___________________
_NT.md) |                | of a specific  |                |
| *item_defname* |                | item equipped  |                |
|                |                | to the         |                |
|                |                | character or   |                |
|                |                | inside their   |                |
|                |                | baackpack.     |                |
+----------------+----------------+----------------+----------------+
| [RESENDTOOLTI  | W              | Forces Sphere  |                |
| P](./RESENDTOOLT__________________to_update_the__________________
_IP.md) |                | tooltips for   |                |
| *sendfu        |                | nearby         |                |
| ll*,*usecache* |                | clients. If    |                |
|                |                | sendfull is 1  |                |
|                |                | the entire     |                |
|                |                | tooltip is     |                |
|                |                | sent and if 0  |                |
|                |                | then just the  |                |
|                |                | header is      |                |
|                |                | sent. If       |                |
|                |                | usecache is 1  |                |
|                |                | then the       |                |
|                |                | cached version |                |
|                |                | (if found)     |                |
|                |                | will be sent   |                |
|                |                | and if 0 then  |                |
|                |                | the cached     |                |
|                |                | version (if    |                |
|                |                | found) will be |                |
|                |                | replaced and   |                |
|                |                | sent           |                |
+----------------+----------------+----------------+----------------+
| [RESE          | RW             | Gets or sets   |                |
| NERGY](./RESENER__________________the____________________________
_GY.md) |                | character\'s   |                |
|                |                | resistance to  |                |
|                |                | energy.        |                |
+----------------+----------------+----------------+----------------+
| [RESENERGYM    | RW             | Gets or sets   |                |
| AX](./RESENERGYM__________________the____________________________
_AX.md) |                | character\'s   |                |
|                |                | maximum        |                |
|                |                | resistance to  |                |
|                |                | energy.        |                |
+----------------+----------------+----------------+----------------+
| [              | RW             | Gets or sets   |                |
| RESFIRE](./RESFI__________________the____________________________
_RE.md) |                | character\'s   |                |
|                |                | resistance to  |                |
|                |                | fire.          |                |
+----------------+----------------+----------------+----------------+
| [RESFIR        | RW             | Gets or sets   |                |
| EMAX](./RESFIREM__________________the____________________________
_AX.md) |                | character\'s   |                |
|                |                | maximum        |                |
|                |                | resistance to  |                |
|                |                | fire.          |                |
+----------------+----------------+----------------+----------------+
| [RESP          | RW             | Gets or sets   |                |
| OISON](./RESPOIS__________________the____________________________
_ON.md) |                | character\'s   |                |
|                |                | resistance to  |                |
|                |                | poison.        |                |
+----------------+----------------+----------------+----------------+
| [RESPOISONM    | RW             | Gets or sets   |                |
| AX](./RESPOISONM__________________the____________________________
_AX.md) |                | character\'s   |                |
|                |                | maximum        |                |
|                |                | resistance to  |                |
|                |                | poison.        |                |
+----------------+----------------+----------------+----------------+
| [              | R              | Returns 1 if   |                |
| RESTEST](./RESTE__________________all_of_the_____________________
_ST.md) |                | items in the   |                |
| *item_list*    |                | list can be    |                |
|                |                | found equipped |                |
|                |                | to the         |                |
|                |                | character or   |                |
|                |                | inside their   |                |
|                |                | backpack.      |                |
+----------------+----------------+----------------+----------------+
| [RESU          | W              | Resurrects the |                |
| RRECT](./RESURRE__________________character_If__________________
_CT.md) |                | *force* is 1   |                |
| *force*        |                | then usual     |                |
|                |                | anti-magic     |                |
|                |                | checks are     |                |
|                |                | bypasses.      |                |
+----------------+----------------+----------------+----------------+
| [SALUTE](./SALU___W_______________Makes_the______________________
_TE.md) |                | character      |                |
| *object_uid*   |                | salute a       |                |
|                |                | specified      |                |
|                |                | object or SRC. |                |
+----------------+----------------+----------------+----------------+
| [SAY](./S_________W_______________Makes_the______________________
_AY.md) |                | character      |                |
| *message*      |                | speak a        |                |
|                |                | message.       |                |
+----------------+----------------+----------------+----------------+
| [SAYU](./SA_______W_______________Makes_the______________________
_YU.md) |                | character      |                |
| *message*      |                | speak a UTF-8  |                |
|                |                | message        |                |
+----------------+----------------+----------------+----------------+
| [SAYUA](./SAY_____W_______________MAkes_the______________________
_UA.md) |                | character      |                |
| *colour,       |                | speak a        |                |
| talkmode,      |                | UNICODE        |                |
| font, lang_id, |                | message.       |                |
| text*          |                |                |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Displays a     |                |
| SDIALOG](./SDIAL__________________dialog_to_SRC_________________
_OG.md) |                | providing that |                |
| *dialog_id,    |                | it is not      |                |
| page,          |                | already open.  |                |
| parameters*    |                |                |                |
+----------------+----------------+----------------+----------------+
| [SERIAL](./SERI___R_______________Gets_the_______________________
_AL.md) |                | item\'s unique |                |
|                |                | ID in the      |                |
|                |                | world.         |                |
+----------------+----------------+----------------+----------------+
| [SEX](./S_________R_______________Returns________________________
_EX.md) |                | *value_male*   |                |
| *value_male    |                | or             |                |
| :value_female* |                | *value_female* |                |
|                |                | depending on   |                |
|                |                | the            |                |
|                |                | character\'s   |                |
|                |                | gender.        |                |
+----------------+----------------+----------------+----------------+
| [SE            | R              | Converts the   |                |
| XTANTP](./SEXTAN__________________characters___________________
_TP.md) |                | location or a  |                |
| *location*     |                | specified      |                |
|                |                | location into  |                |
|                |                | sextant        |                |
|                |                | coordinates.   |                |
+----------------+----------------+----------------+----------------+
| *skill_name*   | RW             | Gets or sets   |                |
|                |                | the            |                |
|                |                | character\'s   |                |
|                |                | skill level in |                |
|                |                | *skill_name*.  |                |
+----------------+----------------+----------------+----------------+
| [SHIP.n](./SHIP___R_______________X_branch_only_________________
_n.md) |                | Added to       |                |
|                |                | access the     |                |
|                |                | ship in the    |                |
|                |                | Nth position,  |                |
|                |                | eg:            |                |
|                |                | ship.3.Redeed  |                |
+----------------+----------------+----------------+----------------+
| [SHIPS](./SHI_____R_______________X_branch_only_________________
_PS.md) |                | Return the     |                |
|                |                | ships on the   |                |
|                |                | player\'s      |                |
|                |                | list.          |                |
+----------------+----------------+----------------+----------------+
| [SKILL](       | W              | Begins using a |                |
| SKILL_(Functio |                | skill.         |                |
| n) "wikilink") |                |                |                |
+----------------+----------------+----------------+----------------+
| [SKILLAD       | R              | Returns the    |                |
| JUSTED](SKILLA |                | skill value    |                |
| DJUSTED "wikil |                | adjusted by    |                |
| ink").\"number |                | the stat       |                |
| or             |                | bonus. Example |                |
| skill_name\"   |                | "Sk            |                |
| (X branch      |                | illAdjusted.1" |                |
| only)          |                | or             |                |
|                |                | "SkillAdju     |                |
|                |                | sted.Anatomy". |                |
+----------------+----------------+----------------+----------------+
| [SKILLC        | R              | Performs a     |                |
| HECK](./SKILLCHE__________________check_for______________________
_CK.md) |                | skill success, |                |
| *skill_id,     |                | returning 1 if |                |
| difficulty*    |                | the attempt    |                |
|                |                | was            |                |
|                |                | successful.    |                |
+----------------+----------------+----------------+----------------+
| [SKILLBES      | R              | Returns the ID |                |
| T](SKILLBEST " |                | of the         |                |
| wikilink")*.n* |                | character\'s   |                |
|                |                | nth highest    |                |
|                |                | skill (0 =     |                |
|                |                | Highest)       |                |
+----------------+----------------+----------------+----------------+
| [SKIL          | W              | Invokes        |                |
| LGAIN](./SKILLGA__________________Spheres______________________
_IN.md) |                | skill gain for |                |
| *skill,        |                | the specified  |                |
| difficulty*    |                | skill, with    |                |
|                |                | the given      |                |
|                |                | difficulty     |                |
|                |                | (0-100)        |                |
+----------------+----------------+----------------+----------------+
| [SKIL          | R              | Returns 1 if   |                |
| LTEST](./SKILLTE__________________the_character__________________
_ST.md) |                | possess all of |                |
| *skill_list*   |                | the skills in  |                |
|                |                | the list.      |                |
+----------------+----------------+----------------+----------------+
| [SKILLT        | R              | Returns the    |                |
| OTAL](./SKILLTOT__________________total_value_of_________________
_AL.md) |                | all the        |                |
|                |                | character\'s   |                |
|                |                | skills.        |                |
+----------------+----------------+----------------+----------------+
| [SKILLT        | R              | Returns the    |                |
| OTAL](./SKILLTOT__________________total_value_of_________________
_AL.md) |                | all the        |                |
| *skill_group*  |                | character\'s   |                |
|                |                | skills with    |                |
|                |                | the specified  |                |
|                |                | group flag(s). |                |
+----------------+----------------+----------------+----------------+
| [SKILLT        | R              | Returns the    |                |
| OTAL](./SKILLTOT__________________total_value_of_________________
_AL.md) |                | all the        |                |
| *-amount*      |                | character\'s   |                |
|                |                | skills that    |                |
|                |                | are under      |                |
|                |                | *amount*.      |                |
+----------------+----------------+----------------+----------------+
| [SKILLT        | R              | Returns the    |                |
| OTAL](./SKILLTOT__________________total_value_of_________________
_AL.md) |                | all the        |                |
| *+amount*      |                | character\'s   |                |
|                |                | skills that    |                |
|                |                | are over       |                |
|                |                | *amount*.      |                |
+----------------+----------------+----------------+----------------+
| [SKILLUSEQUICK](./SKILLUSEQUICK.md) | R | Quickly uses a skill with optional parameters to control the check formula and script execution. It accepts: `skill_id` (the ID of the skill), `difficulty` (the difficulty of the skill attempt). The `linearcheck` parameter, when set to 1, makes Sphere perform a linear skill check (typically for combat-related checks, where a higher difficulty value makes it easier to pass). The `forcecheck` parameter, when set to 1, allows the execution of the Skill_UseQuick method by a skill with the SKF_SCRIPTED flag. Sphere internally utilizes quick checks for various actions including Camping, Mining, Musicianship, Parrying, Repairing Items, Resisting Spells, Tinkering, Training Dummies, and Tracking. |
| *skill_id, difficulty, linearcheck, forcecheck* | | |
+----------------+----------------+----------------+----------------+
| [SLEEP](./SLE_____W_______________Makes_the______________________
_EP.md) |                | character      |                |
| *              |                | appear to      |                |
| fall_forwards* |                | sleep.         |                |
+----------------+----------------+----------------+----------------+
| [SOUND](./SOU_____W_______________Plays_a_sound__________________
_ND.md) |                | from this      |                |
| *sound_id,     |                | character.     |                |
| repeat*        |                |                |                |
+----------------+----------------+----------------+----------------+
| [SPELLEFF      | W              | Causes the     |                |
| ECT](./SPELLEFFE__________________character_to___________________
_CT.md) |                | be affected by |                |
| *spell_id,     |                | a spell.       |                |
| strength,      |                |                |                |
| source_        |                |                |                |
| character_uid, |                |                |                |
| so             |                |                |                |
| urce_item_uid* |                |                |                |
+----------------+----------------+----------------+----------------+
| [SPEECHCOLO    | RW             | Override       |                |
| ROVERRIDE](./SPE__________________client_speech__________________
_ECHCOLOROVERRI__________________hue___________.md) |                |                |                |
| *value*        |                |                |                |
+----------------+----------------+----------------+----------------+
| [STAM](./ST_______RW______________Gets_or_sets___________________
_AM.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | stamina.       |                |
+----------------+----------------+----------------+----------------+
| [STEPSTEA      | RW             | Gets or sets   |                |
| LTH](./STEPSTEAL__________________the_amount_of__________________
_TH.md) |                | steps a        |                |
|                |                | character can  |                |
|                |                | do while using |                |
|                |                | the Stealth    |                |
|                |                | skill.         |                |
+----------------+----------------+----------------+----------------+
| [STONE](./STO_____RW______________Gets_or_sets___________________
_NE.md) |                | whether or not |                |
|                |                | the character  |                |
|                |                | is trapped in  |                |
|                |                | stone.         |                |
+----------------+----------------+----------------+----------------+
| [STR](./S_________RW______________Gets_or_sets___________________
_TR.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | total          |                |
|                |                | strength.      |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Forces the     |                |
| SUICIDE](./SUICI__________________character_to___________________
_DE.md) |                | commit         |                |
|                |                | suicide.       |                |
+----------------+----------------+----------------+----------------+
| [SUMMON        | W              | Teleports the  |                |
| CAGE](./SUMMONCA__________________character_to___________________
_GE.md) |                | SRC\'s,        |                |
|                |                | surrounded by  |                |
|                |                | a cage multi.  |                |
+----------------+----------------+----------------+----------------+
| [SU            | W              | Teleports the  |                |
| MMONTO](./SUMMON__________________character_to___________________
_TO.md) |                | SRC\'s         |                |
|                |                | position.      |                |
+----------------+----------------+----------------+----------------+
| [TAG](TAG "wik | RW             | Gets or sets   |                |
| ilink")*.name* |                | the value of a |                |
|                |                | TAG.           |                |
+----------------+----------------+----------------+----------------+
| [TAGA          | R              | Gets a TAG at  |                |
| T](TAGAT "wiki |                | the given      |                |
| link")*.index* |                | zero-based     |                |
|                |                | index.         |                |
+----------------+----------------+----------------+----------------+
| [TAGAT](T      | R              | Gets the name  |                |
| AGAT "wikilink |                | of the TAG at  |                |
| ")*.index*.KEY |                | the given      |                |
|                |                | zero-based     |                |
|                |                | index.         |                |
+----------------+----------------+----------------+----------------+
| [TAGAT](T      | R              | Gets the value |                |
| AGAT "wikilink |                | of the TAG at  |                |
| ")*.index*.VAL |                | the given      |                |
|                |                | zero-based     |                |
|                |                | index.         |                |
+----------------+----------------+----------------+----------------+
| [TA            | R              | Gets the       |                |
| GCOUNT](./TAGCOU__________________number_of_TAGs_________________
_NT.md) |                | stored on the  |                |
|                |                | item.          |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Outputs a list |                |
| TAGLIST](./TAGLI__________________of_the_________________________
_ST.md) |                | object\'s      |                |
|                |                | TAGs.          |                |
+----------------+----------------+----------------+----------------+
| [TARG          | W              | Displays a     |                |
| ET](TARGET "wi |                | targeting      |                |
| kilink")*FGMW* |                | cursor to SRC. |                |
| *function*     |                |                |                |
+----------------+----------------+----------------+----------------+
| [TIMER](./TIM_____RW______________Gets_or_sets___________________
_ER.md) |                | the length of  |                |
|                |                | time before    |                |
|                |                | the item\'s    |                |
|                |                | timer expires, |                |
|                |                | in seconds.    |                |
+----------------+----------------+----------------+----------------+
| [TIMERD](./TIME___RW______________Gets_or_sets___________________
_RD.md) |                | the length of  |                |
|                |                | time before    |                |
|                |                | the item\'s    |                |
|                |                | timer expires, |                |
|                |                | in tenths of a |                |
|                |                | second.        |                |
+----------------+----------------+----------------+----------------+
| [TIMERF](./TIME___W_______________Scheduled_a____________________
_RF.md) |                | function to be |                |
| *time,         |                | executed on    |                |
| function*      |                | this object in |                |
|                |                | *time*         |                |
|                |                | seconds.       |                |
+----------------+----------------+----------------+----------------+
| [TIMERF](./TIME___W_______________Clears_all_____________________
_RF.md) |                | scheduled      |                |
| *CLEAR*        |                | functions from |                |
|                |                | the character. |                |
+----------------+----------------+----------------+----------------+
| [TIMERF](./TIME___W_______________Stops_the______________________
_RF.md) |                | specified      |                |
| *STOP,         |                | function from  |                |
| function*      |                | the character. |                |
|                |                | (On X version  |                |
|                |                | wild character |                |
|                |                | \* is          |                |
|                |                | available for  |                |
|                |                | defining the   |                |
|                |                | function name  |                |
|                |                | or the         |                |
|                |                | argument)      |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Set an object  |                |
| TIMERMS](./TIMER__________________timer_to_______________________
_MS.md) |                | elapse after   |                |
|                |                | the given      |                |
|                |                | number of      |                |
|                |                | milliseconds.  |                |
+----------------+----------------+----------------+----------------+
| [              | RW             | Gets or sets   |                |
| TITHING](./TITHI__________________the_number_of__________________
_NG.md) |                | tithing points |                |
|                |                | the character  |                |
|                |                | has.           |                |
+----------------+----------------+----------------+----------------+
| [TITLE](./TIT_____RW______________Gets_or_sets___________________
_LE.md) |                | the            |                |
|                |                | character\'s   |                |
|                |                | title.         |                |
+----------------+----------------+----------------+----------------+
| [TOWNAB        | R              | Returns the    |                |
| BREV](./TOWNABBR__________________characters___________________
_EV.md) |                | town           |                |
|                |                | abbreviation.  |                |
+----------------+----------------+----------------+----------------+
| [              | R              | Fires a custom |                |
| TRIGGER](./TRIGG__________________trigger_and____________________
_ER.md) |                | returns the    |                |
| *trig_name,    |                | RETURN value.  |                |
| trig_type*     |                |                |                |
+----------------+----------------+----------------+----------------+
| [UID](./U_________R_______________Gets_the_______________________
_ID.md) |                | item\'s unique |                |
|                |                | ID in the      |                |
|                |                | world.         |                |
+----------------+----------------+----------------+----------------+
| [UNDE          | W              | Toggles the    |                |
| RWEAR](./UNDERWE__________________display_of_____________________
_AR.md) |                | underwear on   |                |
|                |                | the character. |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Unequips an    |                |
| UNEQUIP](./UNEQU__________________item_from_the__________________
_IP.md) |                | character,     |                |
| *item_uid*     |                | placing it in  |                |
|                |                | their          |                |
|                |                | backpack.      |                |
+----------------+----------------+----------------+----------------+
| [UPDATE](./UPDA___W_______________Updates_the____________________
_TE.md) |                | state of the   |                |
|                |                | character to   |                |
|                |                | nearby         |                |
|                |                | clients.       |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Updates the    |                |
| UPDATEX](./UPDAT__________________state_of_the___________________
_EX.md) |                | character to   |                |
|                |                | nearby         |                |
|                |                | clients,       |                |
|                |                | removing it    |                |
|                |                | from their     |                |
|                |                | view first to  |                |
|                |                | ensure a full  |                |
|                |                | refresh.       |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Double clicks  |                |
| USEITEM](./USEIT__________________the_character_________________
_EM.md) |                | with SRC as    |                |
|                |                | the source of  |                |
|                |                | the event,     |                |
|                |                | without        |                |
|                |                | checking for   |                |
|                |                | line of sight. |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Double clicks  |                |
| USEITEM](./USEIT__________________an_object_____________________
_EM.md) |                | with the       |                |
| *object_uid*   |                | character as   |                |
|                |                | SRC.           |                |
+----------------+----------------+----------------+----------------+
| [VISUALRA      | RW             | Gets or sets   |                |
| NGE](./VISUALRAN__________________the____________________________
_GE.md) |                | character\'s   |                |
|                |                | sight range.   |                |
+----------------+----------------+----------------+----------------+
| [WEIGHT](./WEIG___R_______________Gets_the_______________________
_HT.md) |                | weight of the  |                |
|                |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [WHERE](./WHE_____W_______________Describes_the__________________
_RE.md) |                | character\'s   |                |
|                |                | location to    |                |
|                |                | SRC.           |                |
+----------------+----------------+----------------+----------------+
| [Z]            | R              | Gets the Z     |                |
| (Z "wikilink") |                | position of    |                |
|                |                | the character. |                |
| [ISLEEPING](./SECTOR.md) | R          | Returns 1 if the char is sleeping, 0 otherwise. | X |
| [SLEEP](./SECTOR.md) | W          | Puts the char to sleep. | X |
| [AWAKE](./SECTOR.md) | W          | Wakes the char up.      | X |
+----------------+----------------+----------------+----------------+

## Triggers

Here is a list of all character triggers. Click on the trigger name for
more detailed information such as arguments and examples.

  ---------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------- --------------------
  **Name**                                                         **Description**                                                                                                                   **Sphere X only?**
  [\@AfterClick](./AfterClick.md)                           Fires when the object has been single-clicked, just before the overhead name is shown.                                            
  [\@Attack](./Attack.md)                                   Fires when the character begins attacking another.                                                                                
  [\@CallGuards](./CallGuards.md)                           Fires when the character calls for guards.                                                                                        
  [\@CharAttack](./CharAttack.md)                           Fires when the character is attacked by another character.                                                                        
  [\@CharClick](./CharClick.md)                             Fires when the character is clicked by another character.                                                                         
  [\@CharClientTooltip](./CharClientTooltip.md)             Fires when the tooltips are about to be sent to the character.                                                                    
  [\@CharDClick](./CharDClick.md)                           Fires when the character double clicks another character.                                                                         
  [\@CharTradeAccepted](./CharTradeAccepted.md)             Fires when another character accepts trade with the character.                                                                    
  [\@Click](./Click.md)                                     Fires when the object has been single-clicked.                                                                                    
  [\@ClientTooltip](./ClientTooltip.md)                     Fires when tooltips for this character are about to be sent to a client.                                                          
  [\@CombatAdd](./CombatAdd.md)                             Fires when someone is being added to my attacker list.                                                                            
  [\@CombatDelete](./CombatDelete.md)                       Fires when someone is deleted from my attacker list.                                                                              
  [\@CombatEnd](./CombatEnd.md)                             Fires when someone is being deleted from my attacker list and I don\'t have any more viable targets.                              
  [\@CombatStart](./CombatStart.md)                         Fires when adding first attacker to my list.                                                                                      
  [\@ContextMenuRequest](./ContextMenuRequest.md)           Fires when a client requests the context menu options for the object.                                                             
  [\@ContextMenuSelect](./ContextMenuSelect.md)             Fires when a client selects a context menu option for the object.                                                                 
  [\@Create](./Create.md)                                   Fires when the object is initially created, before it is placed in the world.                                                     
  [\@Criminal](./Criminal.md)                               Fires when the character becomes a criminal.                                                                                      
  [\@DClick](./DClick.md)                                   Fires when the object is double-clicked.                                                                                          
  [\@Death](./Death.md)                                     Fires when the character\'s hitpoints reaches zero.                                                                               
  [\@DeathCorpse](./DeathCorpse.md)                         Fires when a corpse is created for the character.                                                                                 
  [\@Destroy](./Destroy.md)                                 Fires when the object is being deleted.                                                                                           
  [\@Dismount](./Dismount.md)                               Fires when the character dismounts their ride.                                                                                    
  [\@Dye](./Dye.md)                                         Fires when the character is about to change their color or the color of an object.                                                
  [\@Eat](./Eat.md)                                         Fires when the character eats something.                                                                                          
  [\@EnvironChange](./EnvironChange.md)                     Fires when the environment changes for the character.                                                                             
  [\@ExpChange](./ExpChange.md)                             Fires when the character\'s experience points change.                                                                             
  [\@ExpLevelChange](./ExpLevelChange.md)                   Fires when the character\'s experience level changes.                                                                             
  [\@FameChange](./FameChange.md)                           Fires when the character\'s fame changes.                                                                                         
  [\@GetHit](./GetHit.md)                                   Fires when the character receives damage.                                                                                         
  [\@Hit](./Hit.md)                                         Fires when the character hits another in combat.                                                                                  
  [\@HitMiss](./HitMiss.md)                                 Fires when the character fails to hit another in combat.                                                                          
  [\@HitParry](./HitParry.md)                               X branch only. Fires when the character is attempting to parry a hit.                                                             X
  [\@HitTry](./HitTry.md)                                   Fires when the character tries to hit another in combat.                                                                          
  [\@HouseDesignCommit](./HouseDesignCommit.md)             Fires when the character commits a new house design.                                                                              
  [\@HouseDesignExit](./HouseDesignExit.md)                 Fires when the character exits house design mode.                                                                                 
  [\@Hunger](./Hunger.md)                                   Fires when the character\'s food level decreases.                                                                                 
  [\@ItemAfterClick](./ItemAfterClick.md)                   Fires when the character single-clicks an item, just before the overhead name is shown.                                           
  [\@ItemBuy](./ItemBuy.md)                                 Fires when the character buys an item from a vendor.                                                                              
  [\@ItemClick](./ItemClick.md)                             Fires when the character single-clicks an item.                                                                                   
  [\@ItemClientTooltip](./ItemClientTooltip.md)             Fires when the tooltips are about to be sent to the client for an item.                                                           
  [\@ItemContextMenuRequest](./ItemContextMenuRequest.md)   Fires when the character requests the context menu options for an item.                                                           
  [\@ItemContextMenuSelect](./ItemContextMenuSelect.md)     Fires when the character selects a context menu option for an item.                                                               
  [\@ItemCreate](./ItemCreate.md)                           Fires when an item is initially created, before it is placed in the world, and the character is in some way responsible for it.   
  [\@ItemDamage](./ItemDamage.md)                           Fires when the character damages an item.                                                                                         
  [\@ItemDClick](./ItemDClick.md)                           Fires when the character double-clicks an item.                                                                                   
  [\@ItemDropOn_Char](./ItemDropOn_Char.md)                 Fires when the character drops an item on to a character.                                                                         
  [\@ItemDropOn_Ground](./ItemDropOn_Ground.md)             Fires when the character drops an item on to the ground.                                                                          
  [\@ItemDropOn_Item](./ItemDropOn_Item.md)                 Fires when the character drops an item on to another item.                                                                        
  [\@ItemDropOn_Self](./ItemDropOn_Self.md)                 Fires when the character drops an item inside another item.                                                                       
  [\@ItemEquip](./ItemEquip.md)                             Fires when the character equips an item.                                                                                          
  [\@ItemEquipTest](./ItemEquipTest.md)                     Fires when the characer is about to equip an item.                                                                                
  [\@ItemPickUp_Ground](./ItemPickUp_Ground.md)             Fires when the character picks an item up from the ground.                                                                        
  [\@ItemPickUp_Pack](./ItemPickUp_Pack.md)                 Fires when the character picks an item up from inside a container.                                                                
  [\@ItemPickUp_Self](./ItemPickUp_Self.md)                 Fires when the character picks an item up from inside another item.                                                               
  [\@ItemPickUp_Stack](./ItemPickUp_Stack.md)               Fires when the character picks up an item from a stack.                                                                           
  [\@ItemSell](./ItemSell.md)                               Fires when the character sells an item to a vendor.                                                                               
  [\@ItemSmelt](./ItemSmelt.md)                             Fires when the character smelt an item.                                                                                           X
  [\@ItemSpellEffect](./ItemSpellEffect.md)                 Fires when the character hits an item with a spell.                                                                               
  [\@ItemStep](./ItemStep.md)                               Fires when the character steps on an item.                                                                                        
  [\@ItemTargOn_Cancel](./ItemTargOn_Cancel.md)             Fires when the character cancels an item\'s target cursor.                                                                        
  [\@ItemTargOn_Char](./ItemTargOn_Char.md)                 Fires when the character targets a character with an item\'s target cursor.                                                       
  [\@ItemTargOn_Ground](./ItemTargOn_Ground.md)             Fires when the character targets the ground with an item\'s target cursor.                                                        
  [\@ItemTargOn_Item](./ItemTargOn_Item.md)                 Fires when the character targets an item with an item\'s target cursor.                                                           
  [\@ItemToolTip](./ItemToolTip.md)                         Fires when the character requests old-style tooltips for an item.                                                                 
  [\@ItemUnEquip](./ItemUnEquip.md)                         Fires when the character unequips an item.                                                                                        
  [\@Jailed](./Jailed.md)                                   Fires when the character is sent to jail.                                                                                         
  [\@KarmaChange](./KarmaChange.md)                         Fires when the character\'s karma changes.                                                                                        
  [\@Kill](./Kill.md)                                       Fires when the character kills another character.                                                                                 
  [\@Login](./Login.md)                                     Fires when the character logs in.                                                                                                 
  [\@Logout](./Logout.md)                                   Fires when the character logs out.                                                                                                
  [\@Mount](./Mount.md)                                     Fires when the character mounts a ride.                                                                                           
  [\@MurderDecay](./MurderDecay.md)                         Fires when one of the character\'s kills is about to decay.                                                                       
  [\@MurderMark](./MurderMark.md)                           Fires when the character is about to gain a kill.                                                                                 
  [\@NotoSend](./NotoSend.md)                               Fires the status bar/character notoriety color is sent to another players.                                                        
  [\@NPCAcceptItem](./NPCAcceptItem.md)                     Fires when the NPC receives an item.                                                                                              
  [\@NpcActCast](./NpcActCast.md)                           Fires when the NPC is selecting the spell to cast.                                                                                X
  [\@NPCActFight](./NPCActFight.md)                         Fires when the NPC makes a combat decision.                                                                                       
  [\@NPCActFollow](./NPCActFollow.md)                       Fires when the NPC follows another character.                                                                                     
  [\@NPCAction](./NPCAction.md)                             Fires when the NPC is about to perform an AI action.                                                                              
  [\@NPCActWander](./NPCActWander.md)                       X branch only. Fires each step an NPC does while wandering.                                                                       
  [\@NPCHearGreeting](./NPCHearGreeting.md)                 Fires when the NPC hears a character for the first time.                                                                          
  [\@NPCHearUnknown](./NPCHearUnknown.md)                   Fires when the NPC hears something they don\'t understand.                                                                        
  [\@NPCLookAtChar](./NPCLookAtChar.md)                     Fires then the NPC looks at a character.                                                                                          
  [\@NPCLookAtItem](./NPCLookAtItem.md)                     Fires when the NPC looks at an item.                                                                                              
  [\@NPCLostTeleport](./NPCLostTeleport.md)                 Fires when the NPC is lost and is about to be teleported back to their [HOME](./HOME.md).                                   
  [\@NPCRefuseItem](./NPCRefuseItem.md)                     Fires when the NPC refuses an item being given to them.                                                                           
  [\@NPCRestock](./NPCRestock.md)                           Fires when the NPC is having their items restocked.                                                                               
  [\@NPCSeeNewPlayer](./NPCSeeNewPlayer.md)                 Fires when the NPC first sees a player.                                                                                           
  [\@NPCSeeWantItem](./NPCSeeWantItem.md)                   Fires when the NPC sees an item they want.                                                                                        
  [\@NPCSpecialAction](./NPCSpecialAction.md)               Fires when the NPC is about to perform a special action (leaving fire trail, dropping web).                                       
  [\@PayGold](./PayGold.md)                                 Fires when the character receives a payment. (Experimental Build Only)                                                            
  [\@PersonalSpace](./PersonalSpace.md)                     Fires when the character is stepped on.                                                                                           
  [\@PetDesert](./PetDesert.md)                             Fires when the character deserts its owner.                                                                                       
  [\@Profile](./Profile.md)                                 Fires when a player attempts to read the character\'s profile from the paperdoll.                                                 
  [\@ReceiveItem](./ReceiveItem.md)                         Fires when the NPC receives an item from another character, before they decide if they want it or not.                            
  [\@RegenStat](./RegenStat.md)                             Fires when a character is going to regenerate any stat point.                                                                     
  [\@RegionEnter](./RegionEnter.md)                         Fires when the character enters a region.                                                                                         
  [\@RegionLeave](./RegionLeave.md)                         Fires when the character leaves a region.                                                                                         
  [\@RegionResourceFound](./RegionResourceFound.md)         Fires after a resource has been selected and the resource bit has been created.                                                   
  [\@Rename](./Rename.md)                                   Fires when the character renames another.                                                                                         
  [\@Resurrect](./Resurrect.md)                             Fires when the character is being resurrected.                                                                                    
  [\@SeeCrime](./SeeCrime.md)                               Fires when the character sees a crime take place.                                                                                 
  [\@SeeHidden](./SeeHidden.md)                             Fires when this character is about to see a hidden character.                                                                     
  [\@SkillAbort](./SkillAbort.md)                           Fires when the character aborts a skill.                                                                                          
  [\@SkillChange](./SkillChange.md)                         Fires when the character\'s skill level changes.                                                                                  
  [\@SkillFail](./SkillFail.md)                             Fires when the character fails a skill.                                                                                           
  [\@SkillGain](./SkillGain.md)                             Fires when the character has a chance to gain in a skill.                                                                         
  [\@SkillMakeItem](./SkillMakeItem.md)                     Fires when the character crafts an item.                                                                                          
  [\@SkillMenu](./SkillMenu.md)                             Fires when a skill menu is shown to the character.                                                                                
  [\@SkillPreStart](./SkillPreStart.md)                     Fires when the character starts a skill, before any hardcoded action takes place.                                                 
  [\@SkillSelect](./SkillSelect.md)                         Fires when the character selects a skill on their skill menu.                                                                     
  [\@SkillStart](./SkillStart.md)                           Fires when the character starts a skill.                                                                                          
  [\@SkillSuccess](./SkillSuccess.md)                       Fires when the character succeeds at a skill.                                                                                     
  [\@SkillUseQuick](./SkillUseQuick.md)                     Fires when the character quickly uses a skill.                                                                                    
  [\@SkillWait](./SkillWait.md)                             Fires when Sphere wants to check if a character must wait before starting a skill.                                                
  [\@SpellBook](./SpellBook.md)                             Fires when the character opens their spellbook.                                                                                   
  [\@SpellCast](./SpellCast.md)                             Fires when the character casts a spell.                                                                                           
  [\@SpellEffect](./SpellEffect.md)                         Fires when the character is hit by the effects of a spell.                                                                        
  [\@SpellEffectAdd](./SpellEffectAdd.md)                   Fires when a spell memory is added to the character.                                                                              X
  [\@SpellEffectRemove](./SpellEffectRemove.md)             Fires the spell memory is removed from the character.                                                                             X
  [\@SpellEffectTick](./SpellEffectTick.md)                 Fires when the character is hit the effect of a periodic spell (like Poison spell).                                               X
  [\@SpellFail](./SpellFail.md)                             Fires when the character fails to cast a spell.                                                                                   
  [\@SpellSelect](./SpellSelect.md)                         Fires when the character selects a spell to cast.                                                                                 
  [\@SpellSuccess](./SpellSuccess.md)                       Fires when the character successfully casts a spell.                                                                              
  [\@SpellTargetCancel](./SpellTargetCancel.md)             Fires when the character cancels target selection for a spell they have just cast.                                                
  [\@StatChange](./StatChange.md)                           Fires when the character\'s STR, DEX or INT is changed through skill gain.                                                        
  [\@StepStealth](./StepStealth.md)                         Fires when the character takes a step whilst hidden.                                                                              
  [\@ToggleFlying](./ToggleFlying.md)                       Fires when a Gargoyle Player is going to Fly or to Land.                                                                          
  [\@ToolTip](./ToolTip.md)                                 Fires when a player requests old-style tooltips for this character.                                                               
  [\@TradeAccepted](./TradeAccepted.md)                     Fires when the character accepts a trade with another player.                                                                     
  [\@TradeClose](./TradeClose.md)                           Fires when a trade window is closed.                                                                                              
  [\@TradeCreate](./TradeCreate.md)                         Fires when a player begins a trade with another player.                                                                           
  [\@UserBugReport](./UserBugReport.md)                     Fires when the player submits a bug report.                                                                                       
  [\@UserChatButton](./UserChatButton.md)                   Fires when the player presses the Chat button on the paperdoll.                                                                   
  [\@UserExtCmd](./UserExtCmd.md)                           Fires when the player sends an extended command packet. (used by some macros)                                                     
  [\@UserExWalkLimit](./UserExWalkLimit.md)                 Fires when the player\'s movement is restricted by the movement speed settings in Sphere.ini                                      
  [\@UserGuildButton](./UserGuildButton.md)                 Fires when the player presses the Guild button on the paperdoll.                                                                  
  [\@UserKRToolbar](./UserKRToolbar.md)                     Fires when the player presses a button on the toolbar.                                                                            
  [\@UserMailBag](./UserMailBag.md)                         Fires when the player drags the mail bag on to another character.                                                                 
  [\@UserQuestArrowClick](./UserQuestArrowClick.md)         Fires when the player clicks the quest arrow.                                                                                     
  [\@UserQuestButton](./UserQuestButton.md)                 Fires when the player presses the Quest button on the paperdoll.                                                                  
  [\@UserSkills](./UserSkills.md)                           Fires when the player opens their skill menu, or a skill update is sent to the player.                                            
  [\@UserSpecialMove](./UserSpecialMove.md)                 Fires when the player uses a special move.                                                                                        
  [\@UserStats](./UserStats.md)                             Fires when the player opens the status window.                                                                                    
  [\@UserUltimaStoreButton](./UserUltimaStoreButton.md)     Fires when click on \'Ultima Store\' button on new clients 7.0.62+                                                                
  [\@UserVirtue](./UserVirtue.md)                           Fires when the player presses on the Virtue button.                                                                               
  [\@UserVirtueInvoke](./UserVirtueInvoke.md)               Fires when the player invokes a virtue through macros.                                                                            
  [\@UserWarmode](./UserWarmode.md)                         Fires when the player switches between war and peace mode.                                                                        
  ---------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------- --------------------

## Players

Characters that are attached to an account become Player Characters. In
addition to the basic character references, properties and functions
they also receive the following:

### References {#references_1}

References return pointers to other objects (e.g. the REGION reference
allows you to access the REGION that an object is in). These can either
be accessed by using *\<REFNAME\>* to return the [UID](./UID.md)
(1 for object types that don\'t have UIDs) of the object or 0 if it
doesn\'t exist, or by using *\<REFNAME.KEY\>* where KEY is a valid
property/function/reference for the *REFNAME* object. Click on the name
for more detailed information such as usage and examples.

  ------------------------------------------------- ---------------- --------------------------------------------------------------------------------------------------
  **Name**                                          **Read/Write**   **Description**
  [GUILD](./GUILD.md)                         R                Gets the [guild stone](./Special_ItemsGuild2FTown_Stones.md) that the player belongs to.
  [SKILLCLASS](SKILLCLASS_(Reference) "wikilink")   RW               Gets or sets the player\'s [skillclass](./SKILLCLASS.md).
  [TOWN](./TOWN.md)                           R                Gets the [town stone](./Special_ItemsGuild2FTown_Stones.md) that the player belongs to.
  ------------------------------------------------- ---------------- --------------------------------------------------------------------------------------------------

### Properties and Functions {#properties_and_functions_1}

Here is a list of all player properties and functions. If a function is
marked as readable then it can return a value when used as
`<KEY>`{=html}. Click on the name for more detailed information such as
usage and examples.

  ----------------------------------------------- ---------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------
  **Name**                                        **Read/Write**   **Description**                                                                                                                                                        **Sphere X only?**
  [DEATHS](./DEATHS.md)                     RW               Gets or sets the number of times the player has died.                                                                                                                  
  [DSPEECH](./DSPEECH.md) *+/-speech_id*    RW               Gets a list of attached speech handlers, or adds or removes a speech handler to or from the player.                                                                    
  [GMPAGE](./GMPAGE.md)*.n.DELETE*          W                Deletes the nth GM page. (zero-based)                                                                                                                                  
  [GMPAGE](./GMPAGE.md)*.n.HANDLE*          W                Sets the player as the handler for the nth GM page. (zero-based)                                                                                                       
  [GMPAGE](./GMPAGE.md)*.n.key*             W                Executes the .page command with *key* as the arguments.                                                                                                                
  [ISDSPEECH](./ISDSPEECH.md)*.speech_id*   R                Returns 1 if the player has the given speech handler attached.                                                                                                         
  [KICK](./KICK.md)                         W                Disconnects and blocks the player\'s account.                                                                                                                          
  [KILLS](./KILLS.md)                       RW               Gets the number of murders the player has committed.                                                                                                                   
  [KRTOOLBARSTATUS](./KRTOOLBARSTATUS.md)   RW               Gets or sets whether or not the KR toolbar is enabled for this player.                                                                                                 
  [LASTUSED](./LASTUSED.md)                 RW               Gets the length of time since the player was last attached to a client, in seconds.                                                                                    
  [PASSWORD](./PASSWORD.md)                 W                Sets or clears the player\'s password.                                                                                                                                 
  [PFLAG](./PFLAG.md)                       RW               Gets or sets the player\'s PFLAG value.                                                                                                                                
  [PROFILE](./PROFILE.md)                   RW               Gets or sets the text to display on the player\'s profile.                                                                                                             
  [SKILLLOCK](./SKILLLOCK.md)*.skill_id*    RW               Gets or sets the lock state of the player\'s skill. 0 is Up. 1 is Down. 2 is Locked.                                                                                   
  [SPEEDMODE](./SPEEDMODE.md)               RW               Gets or sets the speed that the player moves at. (0=Normal, 1=Double Speed on Foot, 2=Always walk, 3=Always Run on Foot/Always Walk on Mount, 4=Can not Walk or Run)   
  [STATLOCK](./STATLOCK.md)\'\'.stat_id     RW               Gets or sets the lock state of the player\'s STR (0), DEX (2) or INT (1). \[0 = up, 1 = down, 2 = locked\]                                                             
  ----------------------------------------------- ---------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------

## NPCs

Characters that are not attached to an account are NPCs and are
controlled by Sphere\'s AI. In addition to the basic character
references, properties and functions they also receive the following:

### Properties and Functions {#properties_and_functions_2}

Here is a list of all NPC properties and functions. If a function is
marked as readable then it can return a value when used as
`<KEY>`{=html}. Click on the name for more detailed information such as
usage and examples.

  -------------------------------------------------------- ---------------- --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------
  **Name**                                                 **Read/Write**   **Description**                                                                                                 **Sphere X only?**
  [ACTPRI](./ACTPRI.md)                              RW               Gets or sets the NPC\'s motivation towards their current action.                                                
  [BUY](./BUY.md)                                    W                Displays the shop window to SRC, in buy mode.                                                                   
  [BYE](./BYE.md)                                    W                Ends the NPC\'s current action.                                                                                 
  [FLEE](./FLEE.md) *distance*                       W                Begins moving the NPC away from its current location.                                                           
  [GOTO](./GOTO.md) *location*                       W                Begins moving the NPC towards the specified location.                                                           
  [HIRE](./HIRE.md)                                  W                Begins the hiring process between the NPC and SRC.                                                              
  [LEAVE](./LEAVE.md) *distance*                     W                Begins moving the NPC away from its current location.                                                           
  [NPC](./NPC.md)                                    RW               Gets or sets the NPC\'s AI type.                                                                                
  [HOMEDIST](./HOMEDIST.md)                          RW               Gets or sets the distance that the NPC can wander from its [HOME](./HOME.md) position.                    
  [PETRETRIEVE](./PETRETRIEVE.md)                    W                Enables SRC to retrieve their stabled pets from the NPC.                                                        
  [PETSTABLE](./PETSTABLE.md)                        W                Enables SRC to stable their pet with the NPC.                                                                   
  [RESTOCK](./RESTOCK.md) *force*                    W                Clears all of the NPC\'s stock, repopulating it when it is next accessed (or immediately if *force*=1)          
  [RUN](./RUN.md) *direction*                        W                Forces the NPC to run one tile in the specified direction.                                                      
  [SELL](./SELL.md)                                  W                Displays the shop window to SRC, in sell mode.                                                                  
  [SHRINK](./SHRINK.md)                              W                Shrinks the NPC into a figurine item.                                                                           
  [SPEECH](./SPEECH.md) *+/-speech_id*               RW               Gets the list of speech handlers attached to the NPC, or adds or removes a speech handler to or from the NPC.   
| [SPEECHCOLOR](./SPEECHCOLOR.md)                    | RW             | For NPCs, gets or sets the colour of their speech. For players, it is read-only and contains the last speech hue sent by the client. This can be overridden by SPEECHCOLOROVERRIDE. |                |
| [SPEECHCOLOROVERRIDE](./SPEECHCOLOROVERRIDE.md) | RW | Overrides the speech color for both NPCs and players. | X |
| EMOTECOLOROVERRIDE | RW | Overrides the default emote color for the character. |                                                                   
  [THROWDAM](./THROWDAM.md) *min,max*                RW               Gets or sets a range of damage used for thrown objects. (overrides chardef property)                            
  [THROWDAM](./THROWDAM.md) *dam*                    RW               Gets or sets the constant damage used for thrown objects. (overrides chardef property)                          
  [THROWDAMTYPE](./THROWDAMTYPE.md) *damage flags*   RW               y                                                                                                               Gets or sets the damage flags used for thrown objects. (overrides chardef property)
  [THROWOBJ](./THROWOBJ.md) *id*                     RW               Gets or sets the ID of an object to be thrown by NPCs. (overrides chardef property)                             
  [THROWRANGE](./THROWRANGE.md) *min,max*            RW               Gets or sets the range that an object can be thrown at. (overrides chardef property)                            
  [THROWRANGE](./THROWRANGE.md) *max*                RW               Gets or sets the range that an object can be thrown at with a default min of 2. (overrides chardef property)    
  [TRAIN](./TRAIN.md) *skill*                        W                Initiates training between the NPC and SRC.                                                                     
  [VENDCAP](./VENDCAP.md)                            RW               Gets or sets the amount of gold a vendor will restock to.                                                       
  [VENDGOLD](./VENDGOLD.md)                          RW               Gets or sets the amount of gold a vendor has.                                                                   
  [WALK](./WALK.md) *direction*                      W                Forces the NPC to walk one tile in the specified direction.                                                     
  -------------------------------------------------------- ---------------- --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------

## Clients

When a client is controlling a character, the following references,
properties and functions will be available:

### References {#references_2}

References return pointers to other objects (e.g. the REGION reference
allows you to access the REGION that an object is in). These can either
be accessed by using *\<REFNAME\>* to return the [UID](./UID.md)
(1 for object types that don\'t have UIDs) of the object or 0 if it
doesn\'t exist, or by using *\<REFNAME.KEY\>* where KEY is a valid
property/function/reference for the *REFNAME* object. Click on the name
for more detailed information such as usage and examples.

  --------------------------------------- ---------------- ---------------------------------------------------------------------------------------------------------------------- --------------------
  **Name**                                **Read/Write**   **Description**                                                                                                        **Sphere X only?**
  [GMPAGEP](./GMPAGEP.md)           R                Gets the [GM page](./GM_Pages.md) that the client is currently handling.                                         
  [HOUSEDESIGN](./HOUSEDESIGN.md)   R                Gets the [building](./Special_ItemsCustomizable_Multis.md) that is currently being designed by the client.      
  [PARTY](./PARTY.md)               R                Gets the [party](./Parties.md) that the client is a member of.                                                   
  [TARG](./TARG.md)                 RW               Gets or sets the [character](./Characters.md) or [item](./Items.md) that the client has targeted.          
  [TARGP](./TARGP.md)               RW               Gets or sets the [location](./Map_Points.md) that the client has targeted.                                       
  [TARGPROP](./TARGPROP.md)         RW               Gets or sets the character whose skills are shown in the client\'s skill menu.                                         
  [TARGPRV](./TARGPRV.md)           RW               Gets or sets the [character](./Characters.md) or [item](./Items.md) that the client previously targeted.   
  --------------------------------------- ---------------- ---------------------------------------------------------------------------------------------------------------------- --------------------

### Properties and Functions {#properties_and_functions_3}

Here is a list of all client properties and functions. If a function is
marked as readable then it can return a value when used as
`<KEY>`{=html}. Click on the name for more detailed information such as
usage and examples.

  --------------------------------------------------------------------------------- ---------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------
  **Name**                                                                          **Read/Write**   **Description**                                                                                                                                                                                                                                                                                                                                                  **Sphere X only?**
  [ADD](./ADD.md) *item_defname*                                              W                Prompts the client to target a location to add the specified item at.                                                                                                                                                                                                                                                                                            
  [ADDBUFF](./ADDBUFF.md) *icon, cliloc1, cliloc2, time, arg1, arg2, arg3*    W                Displays a buff icon in the client\'s buff icon bar.                                                                                                                                                                                                                                                                                                             
  [ADDCLILOC](./ADDCLILOC.md) *cliloc, args*                                  W                Adds a cliloc to the tooltip being sent to the client. Only valid in \@ClientTooltip triggers.                                                                                                                                                                                                                                                                   
  [ADDCONTEXTENTRY](./ADDCONTEXTENTRY.md) *entry_id, cliloc, flags, colour*   W                Adds an entry to the context menu being sent to the client. Only valid in \@ContextMenuRequest triggers.                                                                                                                                                                                                                                                         
  [ALLMOVE](./ALLMOVE.md)                                                     RW               Gets or sets whether or not the client has ALLMOVE privileges.                                                                                                                                                                                                                                                                                                   
  [ALLSHOW](./ALLSHOW.md)                                                     RW               Gets or sets whether or not the client is able to see disconnected characters.                                                                                                                                                                                                                                                                                   
  [ARROWQUEST](./ARROWQUEST.md) *x, y, id*                                    W                Displays an arrow on the client\'s screen that points to the specified world coordinates. If id is supplied multiple arrows can be displayed on the client at once (Newer clients only - 3.x+ clients confirm?). You can cancel the arrow by passing 0 for x and y and your id. Using ARROWQUEST without any arguments will cancel arrow with id 0 if present.   
  [BADSPAWN](./BADSPAWN.md)                                                   W                Teleports the client to the first invalid spawn point in the world.                                                                                                                                                                                                                                                                                              
  [BANKSELF](./BANKSELF.md)                                                   W                Opens up the client\'s bankbox.                                                                                                                                                                                                                                                                                                                                  
  [CAST](./CAST.md) \'\'spell_id\'                                            W                Begins casting a spell.                                                                                                                                                                                                                                                                                                                                          
  [CHARLIST](./CHARLIST.md)                                                   W                Displays the client\'s character list screen.                                                                                                                                                                                                                                                                                                                    
  [CLEARCTAGS](./CLEARCTAGS.md)                                               W                Removes all of the client\'s CTAGs.                                                                                                                                                                                                                                                                                                                              
  [CLIENTIS3D](./CLIENTIS3D.md)                                               R                Returns 1 if the client is using the 3D client.                                                                                                                                                                                                                                                                                                                  
  [CLIENTISKR](./CLIENTISKR.md)                                               R                Returns 1 if the client is using the KR client.                                                                                                                                                                                                                                                                                                                  
  [CLIENTVERSION](./CLIENTVERSION.md)                                         R                Gets the client version the client is using, based on the encryption keys being used (unencrypted clients return 0).                                                                                                                                                                                                                                             
  [CTAG](./CTAG.md)                                                           RW               Gets or sets the value of a CTAG.                                                                                                                                                                                                                                                                                                                                
  [CTAGCOUNT](./CTAGCOUNT.md)                                                 R                Gets the number of CTAGs stored on the client.                                                                                                                                                                                                                                                                                                                   
  [CTAGLIST](./CTAGLIST.md)                                                   W                Displays a list of the client\'s CTAGs to SRC.                                                                                                                                                                                                                                                                                                                   
  [CTAGLIST](./CTAGLIST.md) LOG                                               W                Displays a list of the client\'s CTAGs on the server console.                                                                                                                                                                                                                                                                                                    
  [DEBUG](./DEBUG.md)                                                         RW               Gets or sets whether or not the client is in debug mode.                                                                                                                                                                                                                                                                                                         
  [DETAIL](./DETAIL.md)                                                       RW               Gets or sets whether or not the client receives additional detail, such as combat messages.                                                                                                                                                                                                                                                                      
  [EVERBTARG](./EVERBTARG.md) *command*                                       W                Prompts the client to enter a command, or arguments to the command if specified. The complete command with arguments is then executed on TARG.                                                                                                                                                                                                                   
  [EXTRACT](./EXTRACT.md) *file, template_id*                                 W                Extracts static items from a targeted area on the map and saves them into the specified file.                                                                                                                                                                                                                                                                    
  [FLUSH](./FLUSH.md)                                                         W                Forces queued network data to be immediately sent to the client.                                                                                                                                                                                                                                                                                                 
  [GM](./GM.md)                                                               RW               Gets or sets whether or not the client is in GM mode.                                                                                                                                                                                                                                                                                                            
  [GMPAGE](./GMPAGE.md) *ADD message*                                         W                Sends a GM page from the client with the specified message, or if no arguments provided will prompt the client for a message.                                                                                                                                                                                                                                    
  [GOTARG](./GOTARG.md)                                                       W                Teleports the client to their targeted item.                                                                                                                                                                                                                                                                                                                     
  [HEARALL](./HEARALL.md)                                                     RW               Gets or sets whether or not the client can hear all player speech regardless of location.                                                                                                                                                                                                                                                                        
  [INFO](./INFO.md)                                                           W                Displays an information dialog to the client for an object they target.                                                                                                                                                                                                                                                                                          
  [INFORMATION](./INFORMATION.md)                                             W                Displays server information to the client.                                                                                                                                                                                                                                                                                                                       
  [LAST](./LAST.md)                                                           W                Forces the client to target the object referenced by [ACT](./ACT.md).                                                                                                                                                                                                                                                                                      
  [LASTEVENT](./LASTEVENT.md)                                                 RW               Returns the time when data was last received from the client.                                                                                                                                                                                                                                                                                                    
  [LINK](./LINK.md)                                                           W                Allows the client to target two objects to link them together.                                                                                                                                                                                                                                                                                                   
  [MENU](MENU_(Function) "wikilink") *menu_id*                                      W                Displays a menu to the client.                                                                                                                                                                                                                                                                                                                                   
  [MIDILIST](./MIDILIST.md) *music1, music2, \...*                            W                Selects a random music id from the given list and tells the client to play it.                                                                                                                                                                                                                                                                                   
  [NUDGE](./NUDGE.md) *dx, dy, dz*                                            W                Allows the client to nudge an area of items by the given coordinates, relative to the items\' position.                                                                                                                                                                                                                                                          
  [NUKE](./NUKE.md) *command*                                                 W                Allows the client to execute *command* on all items in a targeted area.                                                                                                                                                                                                                                                                                          
  [NUKECHAR](./NUKECHAR.md) *command*                                         W                Allows the client to execute *command* on all NPCs in a targeted area.                                                                                                                                                                                                                                                                                           
  [PAGE](./PAGE.md)                                                           W                Displays the GM page menu to the client.                                                                                                                                                                                                                                                                                                                         
  [PRIVSHOW](./PRIVSHOW.md)                                                   W                Gets or sets whether or not the client\'s privilege level should show in their name.                                                                                                                                                                                                                                                                             
  [REMOVEBUFF](./REMOVEBUFF.md) *icon*                                        W                Removes a buff icon from the client\'s buff icon bar.                                                                                                                                                                                                                                                                                                            
  [REPAIR](./REPAIR.md)                                                       W                Prompts the client to target an item for them to repair.                                                                                                                                                                                                                                                                                                         
  [REPORTEDCLIVER](./REPORTEDCLIVER.md)                                       R                Gets the client version the client is using, based on what it has identified itself as to the server.                                                                                                                                                                                                                                                            
  [REPORTEDCLIVER](./REPORTEDCLIVER.md).FULL                                  R                Gets the client version the client is using, based on what it has identified itself as to the server, including the 4th digit.                                                                                                                                                                                                                                   
  [RESEND](./RESEND.md)                                                       W                Forces a full refresh of the client\'s screen.                                                                                                                                                                                                                                                                                                                   
  [SAVE](./SAVE.md) *immediate*                                               W                Begins a world save. If background saving is enabled then *[SAVE](./SAVE.md) 1* will force a foreground save.                                                                                                                                                                                                                                              
  [SCREENSIZE](./SCREENSIZE.md)                                               R                Gets the client\'s screen size. (width,height)                                                                                                                                                                                                                                                                                                                   
  [SCREENSIZE](./SCREENSIZE.md).X                                             R                Gets the width of the client\'s screen size.                                                                                                                                                                                                                                                                                                                     
  [SCREENSIZE](./SCREENSIZE.md).Y                                             R                Gets the height of the client\'s screen size.                                                                                                                                                                                                                                                                                                                    
  [SCROLL](./SCROLL.md) *scroll_id*                                           W                Displays a message scroll to the client.                                                                                                                                                                                                                                                                                                                         
  [SELF](./SELF.md)                                                           W                Forces the client to target itself.                                                                                                                                                                                                                                                                                                                              
  [SENDPACKET](./SENDPACKET.md) *data*                                        W                Sends a raw data packet to the client.                                                                                                                                                                                                                                                                                                                           
  [SET](./SET.md) *command*                                                   W                Prompts the client to target an object to execute *command* on.                                                                                                                                                                                                                                                                                                  
  [SHOWSKILLS](./SHOWSKILLS.md)                                               W                Refreshes the client\'s skills for the skill menu.                                                                                                                                                                                                                                                                                                               
  [SKILLMENU](SKILLMENU_(Function) "wikilink") *skillmenu_id*                       W                Displays a skillmenu to the client.                                                                                                                                                                                                                                                                                                                              
  [SKILLSELECT](./SKILLSELECT.md) *skill_id*                                  W                Simulates the client selecting a skill from their skill menu.                                                                                                                                                                                                                                                                                                    
  [SUMMON](./SUMMON.md) *character_id*                                        W                Casts the summon spell, with \'\'character_id\'; being the character to summon.                                                                                                                                                                                                                                                                                  
  [SYSMESSAGE](./SYSMESSAGE.md) *text*                                        W                Displays a system message to the client.                                                                                                                                                                                                                                                                                                                         
  [SYSMESSAGELOC](./SYSMESSAGELOC.md) *hue, cliloc, args*                     W                Displays a localized system message to the client.                                                                                                                                                                                                                                                                                                               
  [SYSMESSAGELOCEX](./SYSMESSAGELOCEX.md) *hue, cliloc, flags, affix, args*   W                Displays a localized system message to the client with affixed text.                                                                                                                                                                                                                                                                                             
  [SYSMESSAGEUA](./SYSMESSAGEUA.md) *hue, font, mode, language, text*         W                Displays a UNICODE system message to the client.                                                                                                                                                                                                                                                                                                                 
  [TARGETTEXT](./TARGETTEXT.md)                                               RW               Gets or sets the client\'s target text.                                                                                                                                                                                                                                                                                                                          
  [TELE](./TELE.md)                                                           W                Casts the teleport spell.                                                                                                                                                                                                                                                                                                                                        
  [TILE](./TILE.md) *z, item1, item2, \...*                                   W                Tiles the ground within a targeted area with the listed items, at the given Z level.                                                                                                                                                                                                                                                                             
  [UNEXTRACT](./UNEXTRACT.md) *file*                                          W                Unextracts previously extracted statics, as dynamic items at a targeted location.                                                                                                                                                                                                                                                                                
  [VERSION](./VERSION.md)                                                     W                Displays the server description to the client.                                                                                                                                                                                                                                                                                                                   
  [WEBLINK](./WEBLINK.md) *url*                                               W                Opens the client\'s web browser to send them to the specified url.                                                                                                                                                                                                                                                                                               
  [X](./X.md)*command*                                                        W                Prompts the client to target an object to execute *command* on.                                                                                                                                                                                                                                                                                                  
  --------------------------------------------------------------------------------- ---------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Objects](./_Objects.md)
