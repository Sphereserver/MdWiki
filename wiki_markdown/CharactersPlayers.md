```{=mediawiki}
{{Languages|Characters}}
```
\_\_FORCETOC\_\_ A character can be either a player or an NPC.

## References

References return pointers to other objects (e.g. the REGION reference
allows you to access the REGION that an object is in). These can either
be accessed by using *\<REFNAME\>* to return the [UID](UID "wikilink")
(1 for object types that don\'t have UIDs) of the object or 0 if it
doesn\'t exist, or by using *\<REFNAME.KEY\>* where KEY is a valid
property/function/reference for the *REFNAME* object. Click on the name
for more detailed information such as usage and examples.

  ------------------------------------------------------------ ---------------- -------------------------------------------------------------------------------------------------------------------------------------------------- --------------------
  **Name**                                                     **Read/Write**   **Description**                                                                                                                                    **Sphere X only?**
  [ACCOUNT](Accounts "wikilink")                               RW               Gets or sets the [account](Accounts "wikilink") that the character belongs to.                                                                     
  [ACT](ACT "wikilink")                                        RW               Gets or sets the [character](Characters "wikilink") or [item](Items "wikilink") that is related to the action the character is performing.         
  [FINDCONT](FINDCONT "wikilink")*.n*                          R                Gets the nth [item](Items "wikilink") equipped to the character. (zero-based)                                                                      
  [FINDID](FINDID "wikilink")*.item_id*                        R                Gets the first [item](Items "wikilink") found equipped to the character or inside their backpack, with the matching [BASEID](BASEID "wikilink").   
  [FINDLAYER](FINDLAYER "wikilink")*.layer*                    R                Gets the [item](Items "wikilink") that the character has equipped in a specified layer.                                                            
  [FINDTYPE](FINDTYPE "wikilink")*.type*                       R                Gets the first [item](Items "wikilink") found equipped to the character or inside their backpack, with the matching [TYPE](TYPE "wikilink").       
  [MEMORYFINDTYPE](MEMORYFINDTYPE "wikilink")*.memory_flags*   R                Gets a [memory item](Items "wikilink") with the specified flags.                                                                                   
  [MEMORYFIND](MEMORYFIND "wikilink").*object_uid*             R                Gets a [memory item](Items "wikilink") that is linked to the given object.                                                                         
  [OWNER](OWNER "wikilink")                                    R                Gets the character that owns this character. (RW in SphereServer-X Build)                                                                          
  [SPAWNITEM](SPAWNITEM "wikilink")                            R                Gets the [spawn item](Items "wikilink") (t_spawn_char) that this character originated from.                                                        
  [WEAPON](WEAPON "wikilink")                                  R                Gets the [weapon](Items "wikilink") that the character currently has equipped.                                                                     
  [P](P "wikilink")                                            RW               Gets or sets the [position](Map_Points "wikilink") that the character is at.                                                                       
  [REGION](Regions "wikilink")                                 R                Gets the [region](Regions "wikilink") that the character is currently located in.                                                                  
  [ROOM](Rooms "wikilink")                                     R                Gets the [room](Rooms "wikilink") that the character is in.                                                                                        
  [SECTOR](Sectors "wikilink")                                 R                Gets the [sector](Sectors "wikilink") that the character is in.                                                                                    
  [TOPOBJ](TOPOBJ "wikilink")                                  R                Gets the top-most [character](Characters "wikilink") or [item](Items "wikilink") in the world that contains the character.                         
  [TYPEDEF](TYPEDEF_(Reference) "wikilink")                    R                Gets the [CHARDEF](CHARDEF "wikilink") that defines the character.                                                                                 
  ------------------------------------------------------------ ---------------- -------------------------------------------------------------------------------------------------------------------------------------------------- --------------------

## Properties and Functions {#properties_and_functions}

Here is a list of all character properties and functions. If a function
is marked as readable then it can return a value when used as
`<KEY>`{=html}. Click on the name for more detailed information such as
usage and examples. If an attempt is made to access a property that does
not exist on the character, the property from the
[CHARDEF](CHARDEF "wikilink") will be accessed instead.

+----------------+----------------+----------------+----------------+
| **Name**       | **Read/Write** | *              | **Sphere X     |
|                |                | *Description** | only?**        |
+----------------+----------------+----------------+----------------+
| [AC](          | R              | Returns the    |                |
| AC "wikilink") |                | character\'s   |                |
|                |                | total defense. |                |
+----------------+----------------+----------------+----------------+
| [              | RW             | Gets or sets   |                |
| ACTARG1](ACTAR |                | the            |                |
| G1 "wikilink") |                | character\'s   |                |
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
| ACTARG2](ACTAR |                | the            |                |
| G2 "wikilink") |                | character\'s   |                |
|                |                | ACTARG2 value. |                |
+----------------+----------------+----------------+----------------+
| [              | RW             | Gets or sets   |                |
| ACTARG3](ACTAR |                | the            |                |
| G3 "wikilink") |                | character\'s   |                |
|                |                | ACTARG3 value. |                |
+----------------+----------------+----------------+----------------+
| [              | RW             | Gets or sets   |                |
| ACTDIFF](ACTDI |                | the difficulty |                |
| FF "wikilink") |                | of the         |                |
|                |                | character\'s   |                |
|                |                | current        |                |
|                |                | action.        |                |
+----------------+----------------+----------------+----------------+
| [ACTION](ACTI  | RW             | Gets or sets   |                |
| ON "wikilink") |                | the skill that |                |
|                |                | the character  |                |
|                |                | is currently   |                |
|                |                | using.         |                |
+----------------+----------------+----------------+----------------+
| [ACTP](AC      | RW             | Gets or sets   |                |
| TP "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | ACTP value.    |                |
|                |                | Can get        |                |
|                |                | x,y,z,position |                |
|                |                | of the point   |                |
|                |                | in X branch.   |                |
+----------------+----------------+----------------+----------------+
| [ACTPRV](ACTP  | RW             | Gets or sets   |                |
| RV "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | ACTPRV value.  |                |
+----------------+----------------+----------------+----------------+
| [ADDHOUSE      | W              | X branch only. |                |
| u              |                | Adds the given |                |
| id](ADDHOUSE_u |                | uid to the     |                |
| id "wikilink") |                | player\'s      |                |
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
| uid](ADDSHIP_u |                | Adds the given |                |
| id "wikilink") |                | uid to the     |                |
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
| [AFK](A        | W              | Gets or sets   |                |
| FK "wikilink") |                | whether or not |                |
|                |                | the character  |                |
|                |                | is in AFK      |                |
|                |                | mode.          |                |
+----------------+----------------+----------------+----------------+
| [AGE](A        | R              | Returns the    |                |
| GE "wikilink") |                | age of the     |                |
|                |                | character      |                |
|                |                | since its      |                |
|                |                | creation, in   |                |
|                |                | seconds.       |                |
+----------------+----------------+----------------+----------------+
| [ALLS          | W              | Sets all of    |                |
| KILLS](ALLSKIL |                | the            |                |
| LS "wikilink") |                | character\'s   |                |
| *amount*       |                | skills to the  |                |
|                |                | specified      |                |
|                |                | amount.        |                |
+----------------+----------------+----------------+----------------+
| [ANIM](AN      | W              | Plays the      |                |
| IM "wikilink") |                | specified      |                |
| *anim_id*      |                | animation on   |                |
|                |                | the character. |                |
+----------------+----------------+----------------+----------------+
| [A             | R              | Gets the       |                |
| TTACKER](ATTAC |                | number of      |                |
| KER "wikilink" |                | opponents who  |                |
| )*.properties* |                | have damaged   |                |
|                |                | the character. |                |
+----------------+----------------+----------------+----------------+
| [BANK](BA      | W              | Opens the      |                |
| NK "wikilink") |                | character\'s   |                |
| *layer*        |                | bank (or the   |                |
|                |                | container at   |                |
|                |                | the specified  |                |
|                |                | layer) for SRC |                |
|                |                | to view.       |                |
+----------------+----------------+----------------+----------------+
| [BANKBALA      | R              | Returns the    |                |
| NCE](BANKBALAN |                | total amount   |                |
| CE "wikilink") |                | of gold in the |                |
|                |                | character\'s   |                |
|                |                | bankbox.       |                |
+----------------+----------------+----------------+----------------+
| [BARK](BA      | W              | Plays the      |                |
| RK "wikilink") |                | specified      |                |
| *sound_id*     |                | sound (or the  |                |
|                |                | character\'s   |                |
|                |                | generic sound  |                |
|                |                | if not         |                |
|                |                | specified) to  |                |
|                |                | nearby clients |                |
|                |                | from this      |                |
|                |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [BODY](BO      | RW             | Gets or sets   |                |
| DY "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | body.          |                |
+----------------+----------------+----------------+----------------+
| [BOUNCE](BOUN  | W              | Places a       |                |
| CE "wikilink") |                | specified item |                |
| *item_uid*     |                | in the         |                |
|                |                | character\'s   |                |
|                |                | backpack.      |                |
+----------------+----------------+----------------+----------------+
| [BOW](B        | W              | Makes the      |                |
| OW "wikilink") |                | character bow  |                |
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
| CANCAST](CANCA |                | the character  |                |
| ST "wikilink") |                | can cast a     |                |
| *spell_id,     |                | given spell,   |                |
| ch             |                | bypassing      |                |
| eck_antimagic* |                | anti-magic     |                |
|                |                | field tests if |                |
|                |                | *ch            |                |
|                |                | eck_antimagic* |                |
|                |                | set to 0.      |                |
+----------------+----------------+----------------+----------------+
| [              | R              | Returns 1 if   |                |
| CANMAKE](CANMA |                | the character  |                |
| KE "wikilink") |                | has the skills |                |
| *item_id*      |                | and resources  |                |
|                |                | to craft a     |                |
|                |                | certain item.  |                |
+----------------+----------------+----------------+----------------+
| [CANMAKESKI    | R              | Returns 1 if   |                |
| LL](CANMAKESKI |                | the character  |                |
| LL "wikilink") |                | has the skills |                |
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
| CANMOVE](CANMO |                | the character  |                |
| VE "wikilink") |                | can move in    |                |
| *direction*    |                | the given      |                |
|                |                | direction.     |                |
+----------------+----------------+----------------+----------------+
| [CANSEE](CANS  | R              | Returns 1 if   |                |
| EE "wikilink") |                | SRC can see    |                |
|                |                | the character. |                |
+----------------+----------------+----------------+----------------+
| [CANS          | R              | Returns 1 if   |                |
| EELOS](CANSEEL |                | SRC has line   |                |
| OS "wikilink") |                | of sight to    |                |
|                |                | the character. |                |
+----------------+----------------+----------------+----------------+
| [CANSEELOSFLA  | R              | Returns 1 if   |                |
| G](CANSEELOSFL |                | SRC has line   |                |
| AG "wikilink") |                | of sight to    |                |
| *flags*        |                | the character, |                |
|                |                | with flags to  |                |
|                |                | modify what    |                |
|                |                | tests take     |                |
|                |                | place.         |                |
+----------------+----------------+----------------+----------------+
| [COLOR](COL    | RW             | Gets or sets   |                |
| OR "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | hue.           |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Removes        |                |
| CONSUME](CONSU |                | specified      |                |
| ME "wikilink") |                | resources from |                |
| *              |                | SRC\'s         |                |
| resource_list* |                | backpack.      |                |
+----------------+----------------+----------------+----------------+
| [COUNT](COU    | R              | Returns the    |                |
| NT "wikilink") |                | number of      |                |
|                |                | items equipped |                |
|                |                | to the         |                |
|                |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [CREATE](CREA  | RW (R only on  | Gets or sets   |                |
| TE "wikilink") | X)             | the            |                |
|                |                | character\'s   |                |
|                |                | age since      |                |
|                |                | creation, in   |                |
|                |                | seconds (Tenth |                |
|                |                | of seconds on  |                |
|                |                | X).            |                |
+----------------+----------------+----------------+----------------+
| [CR            | W              | Sets whether   |                |
| IMINAL](CRIMIN |                | or not the     |                |
| AL "wikilink") |                | character is a |                |
|                |                | criminal.      |                |
+----------------+----------------+----------------+----------------+
| [CURFOLLO      | RW             | Gets or sets   |                |
| WER](CURFOLLOW |                | the number of  |                |
| ER "wikilink") |                | current        |                |
|                |                | followers the  |                |
|                |                | character has, |                |
+----------------+----------------+----------------+----------------+
| [DAMAGE](DAMA  | W              | Inflicts       |                |
| GE "wikilink") |                | damage upon    |                |
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
| id](DELHOUSE_u |                | given uid from |                |
| id "wikilink") |                | the player\'s  |                |
|                |                | list (Will not |                |
|                |                | delete the     |                |
|                |                | house)(-1      |                |
|                |                | clears the     |                |
|                |                | whole list).   |                |
+----------------+----------------+----------------+----------------+
| [DELSHIP       | W              | X branch only. |                |
| uid](DELSHIP_u |                | Deletes the    |                |
| id "wikilink") |                | given uid from |                |
|                |                | the player\'s  |                |
|                |                | list (Will not |                |
|                |                | delete the     |                |
|                |                | ship)(-1       |                |
|                |                | clears the     |                |
|                |                | whole list).   |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Deletes the    |                |
| DESTROY](DESTR |                | object, not    |                |
| OY "wikilink") |                | stopped by a   |                |
|                |                | return 1 in    |                |
|                |                | [\@D           |                |
|                |                | estroy](@Destr |                |
|                |                | oy "wikilink") |                |
+----------------+----------------+----------------+----------------+
| [DEX](D        | RW             | Gets or sets   |                |
| EX "wikilink") |                | the            |                |
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
| OSE](DIALOGCLO |                | dialog that    |                |
| SE "wikilink") |                | SRC has open,  |                |
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
| [DIR](D        | RW             | Gets or setes  |                |
| IR "wikilink") |                | the direction  |                |
|                |                | that the       |                |
|                |                | character is   |                |
|                |                | facing.        |                |
+----------------+----------------+----------------+----------------+
| [DISCON        | W              | Disconnects    |                |
| NECT](DISCONNE |                | the character. |                |
| CT "wikilink") |                |                |                |
+----------------+----------------+----------------+----------------+
| [DI            | W              | Dismounts the  |                |
| SMOUNT](DISMOU |                | character from |                |
| NT "wikilink") |                | their ride.    |                |
+----------------+----------------+----------------+----------------+
| [DISP          | R              | Gets the ID of |                |
| IDDEC](DISPIDD |                | the character  |                |
| EC "wikilink") |                | as a decimal   |                |
|                |                | number.        |                |
+----------------+----------------+----------------+----------------+
| [DI            | R              | Gets the       |                |
| STANCE](DISTAN |                | distance       |                |
| CE "wikilink") |                | between this   |                |
| *point_or_uid* |                | object and     |                |
|                |                | either SRC, a  |                |
|                |                | map location   |                |
|                |                | or another     |                |
|                |                | object.        |                |
+----------------+----------------+----------------+----------------+
| [DCLICK](DCLI  | W              | Double clicks  |                |
| CK "wikilink") |                | the character, |                |
|                |                | with SRC as    |                |
|                |                | the source of  |                |
|                |                | the event.     |                |
+----------------+----------------+----------------+----------------+
| [DCLICK](DCLI  | W              | Double clicks  |                |
| CK "wikilink") |                | an object,     |                |
| *object_uid*   |                | with the       |                |
|                |                | character as   |                |
|                |                | SRC.           |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Starts the     |                |
| DRAWMAP](DRAWM |                | cartography    |                |
| AP "wikilink") |                | skill, drawing |                |
| *radius*       |                | a map of the   |                |
|                |                | local area up  |                |
|                |                | to *radius*    |                |
|                |                | tiles.         |                |
+----------------+----------------+----------------+----------------+
| [DROP](DR      | W              | Drops a        |                |
| OP "wikilink") |                | specified item |                |
| *item_uid*     |                | at the         |                |
|                |                | character\'s   |                |
|                |                | feet.          |                |
+----------------+----------------+----------------+----------------+
| [DUPE](DU      | W              | Creates a      |                |
| PE "wikilink") |                | clone of the   |                |
|                |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [EDIT](ED      | W              | Displays an    |                |
| IT "wikilink") |                | editing dialog |                |
|                |                | for the        |                |
|                |                | character to   |                |
|                |                | SRC.           |                |
+----------------+----------------+----------------+----------------+
| [EFFECT](EFFE  | W              | Displays an    |                |
| CT "wikilink") |                | effect to      |                |
| *type,         |                | nearby         |                |
| item_id,       |                | clients.       |                |
| speed, loop,   |                |                |                |
| explode,       |                |                |                |
| color,         |                |                |                |
| rendermode*    |                |                |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Similar to the | X              |
| EFFECTLOCATION |                | EFFECT command |                |
| ](EFFECTLOCATI |                | but instead of |                |
| ON "wikilink") |                | an object it   |                |
| *x,y,z,ty      |                | takes a        |                |
| pe,itemid,spee |                | terrain        |                |
| d,loop,explode |                | location as a  |                |
| ,color,render* |                | target.        |                |
+----------------+----------------+----------------+----------------+
| [EMOTE](EMO    | W              | Displays a     |                |
| TE "wikilink") |                | \*You see\*    |                |
| *message*      |                | message to all |                |
|                |                | nearby         |                |
|                |                | clients.       |                |
+----------------+----------------+----------------+----------------+
| [EM            | RW             | Gets, sets or  |                |
| OTEACT](EMOTEA |                | toggles        |                |
| CT "wikilink") |                | whether or not |                |
|                |                | the character  |                |
|                |                | will emote all |                |
|                |                | of its         |                |
|                |                | actions.       |                |
+----------------+----------------+----------------+----------------+
| [EQUIP](EQU    | W              | Equips an item |                |
| IP "wikilink") |                | to the         |                |
| *item_uid*     |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [EQUIPA        | W              | Equips the     |                |
| RMOR](EQUIPARM |                | character with |                |
| OR "wikilink") |                | the best       |                |
|                |                | armour in      |                |
|                |                | their          |                |
|                |                | backpack.      |                |
+----------------+----------------+----------------+----------------+
| [EQUI          | W              | Equips a halo  |                |
| PHALO](EQUIPHA |                | light to the   |                |
| LO "wikilink") |                | character,     |                |
| *timeout*      |                | lasting for    |                |
|                |                | *timeout*      |                |
|                |                | tenths of a    |                |
|                |                | second.        |                |
+----------------+----------------+----------------+----------------+
| [EQUIPWEA      | W              | Equips the     |                |
| PON](EQUIPWEAP |                | character with |                |
| ON "wikilink") |                | the best       |                |
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
| [EXP](E        | RW             | Gets or sets   |                |
| XP "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | experience     |                |
|                |                | points.        |                |
+----------------+----------------+----------------+----------------+
| [FACE](FA      | W              | Turns the      |                |
| CE "wikilink") |                | character to   |                |
| *object_uid*   |                | face a         |                |
| (P coords in X |                | specified      |                |
| branch)        |                | object or SRC. |                |
|                |                | Admits         |                |
|                |                | coordinates    |                |
|                |                | instead uid in |                |
|                |                | X branch.      |                |
+----------------+----------------+----------------+----------------+
| [FAME](FA      | RW             | Gets or sets   |                |
| ME "wikilink") |                | the            |                |
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
| [FCOUNT](FCOU  | R              | Returns the    |                |
| NT "wikilink") |                | total number   |                |
|                |                | of items       |                |
|                |                | equipped to    |                |
|                |                | the character, |                |
|                |                | including      |                |
|                |                | subitems       |                |
+----------------+----------------+----------------+----------------+
| [FLAGS](FLA    | RW             | Gets or sets   |                |
| GS "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | flags.         |                |
+----------------+----------------+----------------+----------------+
| [FIX](F        | W              | Re-aligns the  |                |
| IX "wikilink") |                | character\'s Z |                |
|                |                | level to       |                |
|                |                | ground level.  |                |
+----------------+----------------+----------------+----------------+
| [FIXW          | W              | Recalculates   |                |
| EIGHT](FIXWEIG |                | the            |                |
| HT "wikilink") |                | character\'s   |                |
|                |                | total weight.  |                |
+----------------+----------------+----------------+----------------+
| [FLIP](FL      | W              | Rotates the    |                |
| IP "wikilink") |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [FONT](FO      | RW             | Gets or sets   |                |
| NT "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | speech font.   |                |
+----------------+----------------+----------------+----------------+
| [FOOD](FO      | RW             | Gets or sets   |                |
| OD "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | food level.    |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Revokes the    |                |
| FORGIVE](FORGI |                | character\'s   |                |
| VE "wikilink") |                | jailed status. |                |
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
| ](GETSHIPPOS_u |                | the given UID  |                |
| id "wikilink") |                | on the ships   |                |
|                |                | list (-1 if    |                |
|                |                | not found).    |                |
+----------------+----------------+----------------+----------------+
| [GO](          | W              | Teleports the  |                |
| GO "wikilink") |                | character to   |                |
| *location*     |                | the specified  |                |
|                |                | location.      |                |
+----------------+----------------+----------------+----------------+
| [GOCHAR](GOCH  | W              | Teleports the  |                |
| AR "wikilink") |                | character to   |                |
| *n*            |                | the nth        |                |
|                |                | character in   |                |
|                |                | the world.     |                |
+----------------+----------------+----------------+----------------+
| [GO            | W              | Teleports the  |                |
| CHARID](GOCHAR |                | character to   |                |
| ID "wikilink") |                | the next       |                |
| *char          |                | characer in    |                |
| acter_defname* |                | the world with |                |
|                |                | the specified  |                |
|                |                | [BASEID](BASE  |                |
|                |                | ID "wikilink") |                |
+----------------+----------------+----------------+----------------+
| [GOCLI](GOC    | W              | Teleports the  |                |
| LI "wikilink") |                | character to   |                |
| *n*            |                | the nth online |                |
|                |                | player.        |                |
|                |                | (zero-based)   |                |
+----------------+----------------+----------------+----------------+
| [GO            | W              | Teleports the  |                |
| ITEMID](GOITEM |                | character to   |                |
| ID "wikilink") |                | the next item  |                |
| *item_defname* |                | in the world   |                |
|                |                | with the       |                |
|                |                | specified      |                |
|                |                | [BASEID](BASEI |                |
|                |                | D "wikilink"). |                |
+----------------+----------------+----------------+----------------+
| [GOLD](GO      | RW             | Gets or sets   |                |
| LD "wikilink") |                | the amount of  |                |
|                |                | gold the       |                |
|                |                | character has. |                |
+----------------+----------------+----------------+----------------+
| [GONAME](GONA  | W              | Teleports the  |                |
| ME "wikilink") |                | character to   |                |
| *name*         |                | the next       |                |
|                |                | character or   |                |
|                |                | item in the    |                |
|                |                | world with the |                |
|                |                | specified      |                |
|                |                | name, accepts  |                |
|                |                | wildcards      |                |
|                |                | (\*).          |                |
+----------------+----------------+----------------+----------------+
| [GOSOCK](GOSO  | W              | Teleports the  |                |
| CK "wikilink") |                | character to   |                |
| *socket*       |                | the online     |                |
|                |                | player with    |                |
|                |                | the specified  |                |
|                |                | socket number. |                |
+----------------+----------------+----------------+----------------+
| [GOTYPE](GOTY  | W              | Teleports the  |                |
| PE "wikilink") |                | character to   |                |
| *item_type*    |                | the next item  |                |
|                |                | in the world   |                |
|                |                | with the       |                |
|                |                | specified      |                |
|                |                | [TYPE](TYP     |                |
|                |                | E "wikilink"). |                |
+----------------+----------------+----------------+----------------+
| [GOUID](GOU    | W              | Teleports the  |                |
| ID "wikilink") |                | character to   |                |
| *object_uid*   |                | the object     |                |
|                |                | with the       |                |
|                |                | specified      |                |
|                |                | [UID](UI       |                |
|                |                | D "wikilink"). |                |
+----------------+----------------+----------------+----------------+
| [GUILDABB      | R              | Returns the    |                |
| REV](GUILDABBR |                | character\'s   |                |
| EV "wikilink") |                | guild          |                |
|                |                | abbreviation.  |                |
+----------------+----------------+----------------+----------------+
| [HEAR](HE      | W              | For NPCs, acts |                |
| AR "wikilink") |                | as if SRC had  |                |
| *text*         |                | spoken the     |                |
|                |                | specified      |                |
|                |                | *text*. For    |                |
|                |                | players,       |                |
|                |                | displays       |                |
|                |                | *text* as a    |                |
|                |                | system         |                |
|                |                | message.       |                |
+----------------+----------------+----------------+----------------+
| [HEIGHT](HEIG  | R              | Gets the       |                |
| HT "wikilink") |                | character\'s   |                |
|                |                | height.        |                |
+----------------+----------------+----------------+----------------+
| [HITS](HI      | RW             | Gets or sets   |                |
| TS "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | hitpoints.     |                |
+----------------+----------------+----------------+----------------+
| [HOME](HO      | RW             | Gets or sets   |                |
| ME "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | home location. |                |
+----------------+----------------+----------------+----------------+
| [              | R              | X branch       |                |
| HOUSE.n](HOUSE |                | only.Access    |                |
| .n "wikilink") |                | the house in   |                |
|                |                | the Nth        |                |
|                |                | position, eg:  |                |
|                |                | house.3.Redeed |                |
+----------------+----------------+----------------+----------------+
| [HOUSES](HOUS  | R              | X branch only. |                |
| ES "wikilink") |                | Returns the    |                |
|                |                | number of      |                |
|                |                | houses on the  |                |
|                |                | player\'s      |                |
|                |                | list.          |                |
+----------------+----------------+----------------+----------------+
| [HUNGRY](HUNG  | W              | Displays this  |                |
| RY "wikilink") |                | character\'s   |                |
|                |                | hunger level   |                |
|                |                | to SRC.        |                |
+----------------+----------------+----------------+----------------+
| [ID](          | R              | Gets the       |                |
| ID "wikilink") |                | character\'s   |                |
|                |                | ID.            |                |
+----------------+----------------+----------------+----------------+
| [INFO](IN      | W              | Displays an    |                |
| FO "wikilink") |                | information    |                |
|                |                | dialog about   |                |
|                |                | the character  |                |
|                |                | to SRC.        |                |
+----------------+----------------+----------------+----------------+
| [INT](I        | RW             | Gets or sets   |                |
| NT "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | total          |                |
|                |                | intelligence.  |                |
+----------------+----------------+----------------+----------------+
| [INVIS](INV    | W              | Sets whether   |                |
| IS "wikilink") |                | or not the     |                |
|                |                | character is   |                |
|                |                | invisible.     |                |
+----------------+----------------+----------------+----------------+
| [INVUL](INV    | W              | Sets whether   |                |
| UL "wikilink") |                | or not the     |                |
|                |                | character is   |                |
|                |                | invulnerable.  |                |
+----------------+----------------+----------------+----------------+
| [              | R              | Returns 1 if   |                |
| ISARMOR](ISARM |                | the object is  |                |
| OR "wikilink") |                | armour.        |                |
| *object_uid*   |                |                |                |
+----------------+----------------+----------------+----------------+
| [ISCHAR](ISCH  | R              | Returns 1 if   |                |
| AR "wikilink") |                | the object is  |                |
|                |                | a character.   |                |
+----------------+----------------+----------------+----------------+
| [ISCONT](ISCO  | R              | Returns 1 if   |                |
| NT "wikilink") |                | the object is  |                |
|                |                | a container.   |                |
+----------------+----------------+----------------+----------------+
| [ISDIALOGOP    | R              | Returns 1 if   |                |
| EN](ISDIALOGOP |                | SRC has the    |                |
| EN "wikilink") |                | specified      |                |
| *dialog_id*    |                | dialog visible |                |
|                |                | on their       |                |
|                |                | screen.        |                |
+----------------+----------------+----------------+----------------+
| [IS            | R              | Returns 1 if   |                |
| EVENT](ISEVENT |                | the object has |                |
|  "wikilink")*. |                | an event       |                |
| event_defname* |                | attached to    |                |
|                |                | it.            |                |
+----------------+----------------+----------------+----------------+
| [ISGM](IS      | R              | Returns 1 if   |                |
| GM "wikilink") |                | the character  |                |
|                |                | is in GM mode. |                |
+----------------+----------------+----------------+----------------+
| [ISIN          | R              | Returns 1 if   |                |
| PARTY](ISINPAR |                | the player is  |                |
| TY "wikilink") |                | in a           |                |
|                |                | [party](part   |                |
|                |                | y "wikilink"). |                |
+----------------+----------------+----------------+----------------+
| [ISITEM](ISIT  | R              | Returns 1 if   |                |
| EM "wikilink") |                | the object is  |                |
|                |                | an item.       |                |
+----------------+----------------+----------------+----------------+
| [              | R              | Returns 1 if   |                |
| ISMYPET](ISMYP |                | the character  |                |
| ET "wikilink") |                | belongs to     |                |
|                |                | SRC.           |                |
+----------------+----------------+----------------+----------------+
| [ISNEAR        | R              | Returns 1 if a |                |
| TYPE](ISNEARTY |                | nearby item    |                |
| PE "wikilink") |                | has the given  |                |
| *type,         |                | TYPE.          |                |
| distance,      |                |                |                |
| flags*         |                |                |                |
+----------------+----------------+----------------+----------------+
| [ISNEARTYPETO  | R              | Returns a      |                |
| P](ISNEARTYPET |                | nearby world   |                |
| OP "wikilink") |                | location of a  |                |
| *type,         |                | nearby item    |                |
| distance,      |                | which has the  |                |
| flags*         |                | given TYPE.    |                |
+----------------+----------------+----------------+----------------+
| [IS            | R              | Returns 1 if   |                |
| ONLINE](ISONLI |                | the character  |                |
| NE "wikilink") |                | is considered  |                |
|                |                | to be online.  |                |
+----------------+----------------+----------------+----------------+
| [IS            | R              | Returns 1 if   |                |
| PLAYER](ISPLAY |                | the object is  |                |
| ER "wikilink") |                | a player.      |                |
+----------------+----------------+----------------+----------------+
| [              | R              | Returns 1 if   |                |
| ISSTUCK](ISSTU |                | the character  |                |
| CK "wikilink") |                | cannot walk in |                |
|                |                | any direction. |                |
+----------------+----------------+----------------+----------------+
| [ISTE          | R              | Returns 1 if   |                |
| VENT](ISTEVENT |                | the object has |                |
|  "wikilink")*. |                | an event       |                |
| event_defname* |                | attached to    |                |
|                |                | its            |                |
|                |                | [C             |                |
|                |                | HARDEF](CHARDE |                |
|                |                | F "wikilink"). |                |
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
| VENDOR](ISVEND |                | the character  |                |
| OR "wikilink") |                | is a vendor.   |                |
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
| WEAPON](ISWEAP |                | the object is  |                |
| ON "wikilink") |                | a weapon.      |                |
| *object_uid*   |                |                |                |
+----------------+----------------+----------------+----------------+
| [JAIL](JA      | W              | Sends the      |                |
| IL "wikilink") |                | character to   |                |
| *cell*         |                | jail, to a     |                |
|                |                | specified jail |                |
|                |                | cell.          |                |
+----------------+----------------+----------------+----------------+
| [KARMA](KAR    | RW             | Gets or sets   |                |
| MA "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | karma.         |                |
+----------------+----------------+----------------+----------------+
| [KARMA](KAR    | R              | Returns 1 if   |                |
| MA "wikilink") |                | the            |                |
| *.karma_group* |                | character\'s   |                |
|                |                | karma falls    |                |
|                |                | within the     |                |
|                |                | specified      |                |
|                |                | karma group.   |                |
+----------------+----------------+----------------+----------------+
| [KILL](KI      | W              | Kills the      |                |
| LL "wikilink") |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [LEVEL](LEV    | RW             | Gets or sets   |                |
| EL "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | experience     |                |
|                |                | level.         |                |
+----------------+----------------+----------------+----------------+
| [LIGHT](LIG    | RW             | Gets or sets   |                |
| HT "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | personal light |                |
|                |                | level.         |                |
+----------------+----------------+----------------+----------------+
| [LUCK](LU      | RW             | Gets or sets   |                |
| CK "wikilink") |                | the luck value |                |
|                |                | for the        |                |
|                |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [MA            | \| W           | Begins an      |                |
| KEITEM](MAKEIT |                | attempt to     |                |
| EM "wikilink") |                | craft the      |                |
| *item_defname, |                | specified      |                |
| amount*        |                | quantity of    |                |
|                |                | the given      |                |
|                |                | item.          |                |
+----------------+----------------+----------------+----------------+
| [MANA](MA      | RW             | Gets or sets   |                |
| NA "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | mana.          |                |
+----------------+----------------+----------------+----------------+
| [MAP](M        | RW             | Gets or sets   |                |
| AP "wikilink") |                | the map that   |                |
|                |                | this object is |                |
|                |                | located.       |                |
+----------------+----------------+----------------+----------------+
| [MAPWAYPO      | W              | Add/remove     |                |
| INT](MAPWAYPOI |                | waypoints on   |                |
| NT "wikilink") |                | client radar   |                |
| \"ObjectUID,   |                | map (enhanced  |                |
| WaypointType\" |                | clients only). |                |
+----------------+----------------+----------------+----------------+
| [MAXFOLLO      | RW             | Gets or sets   |                |
| WER](MAXFOLLOW |                | the maximum    |                |
| ER "wikilink") |                | number of      |                |
|                |                | followers the  |                |
|                |                | character can  |                |
|                |                | have.          |                |
+----------------+----------------+----------------+----------------+
| [              | RW             | Gets or sets   |                |
| MAXHITS](MAXHI |                | the            |                |
| TS "wikilink") |                | character\'s   |                |
|                |                | maximum        |                |
|                |                | hitpoints.     |                |
+----------------+----------------+----------------+----------------+
| [MAXH          | RW             | Added to       | X              |
| OUSES](MAXHOUS |                | Accounts and   |                |
| ES "wikilink") |                | Chars, when    |                |
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
| MAXMANA](MAXMA |                | the            |                |
| NA "wikilink") |                | character\'s   |                |
|                |                | maximum mana.  |                |
+----------------+----------------+----------------+----------------+
| [MA            | RW             | Added Accounts | X              |
| XSHIPS](MAXSHI |                | and Chars,     |                |
| PS "wikilink") |                | when created   |                |
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
| MAXSTAM](MAXST |                | the            |                |
| AM "wikilink") |                | character\'s   |                |
|                |                | maximum        |                |
|                |                | stamina.       |                |
+----------------+----------------+----------------+----------------+
| [MAXW          | R              | Returns the    |                |
| EIGHT](MAXWEIG |                | maximum weight |                |
| HT "wikilink") |                | that the       |                |
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
| MESSAGE](MESSA |                | message above  |                |
| GE "wikilink") |                | this character |                |
| *message*      |                | to SRC.        |                |
+----------------+----------------+----------------+----------------+
| [MESS          | W              | Displays a     |                |
| AGEUA](MESSAGE |                | UNICODE        |                |
| UA "wikilink") |                | message above  |                |
| *colour,       |                | this character |                |
| talkmode,      |                | to SRC.        |                |
| font, lang_id, |                |                |                |
| message*       |                |                |                |
+----------------+----------------+----------------+----------------+
| [MODAR](MOD    | RW             | Gets or sets a |                |
| AR "wikilink") |                | modifier for   |                |
|                |                | the            |                |
|                |                | character\'s   |                |
|                |                | armour rating. |                |
+----------------+----------------+----------------+----------------+
| [MODDEX](MODD  | RW             | Gets or sets   |                |
| EX "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | dexterity      |                |
|                |                | modifier.      |                |
+----------------+----------------+----------------+----------------+
| [MODINT](MODI  | RW             | Gets or sets   |                |
| NT "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | intelligence   |                |
|                |                | modifier.      |                |
+----------------+----------------+----------------+----------------+
| [MODMAXWEIG    | RW             | Gets or sets   |                |
| HT](MODMAXWEIG |                | the            |                |
| HT "wikilink") |                | character\'s   |                |
|                |                | maximum weight |                |
|                |                | modifier.      |                |
+----------------+----------------+----------------+----------------+
| [MODSTR](MODS  | RW             | Gets or sets   |                |
| TR "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | strength       |                |
|                |                | modifier.      |                |
+----------------+----------------+----------------+----------------+
| [MOUNT](MOU    | R              | Gets the UID   |                |
| NT "wikilink") |                | of the         |                |
|                |                | character\'s   |                |
|                |                | mount.         |                |
+----------------+----------------+----------------+----------------+
| [MOUNT](MOU    | W              | Attempts to    |                |
| NT "wikilink") |                | mount the      |                |
| *mount_uid*    |                | character on   |                |
|                |                | to the         |                |
|                |                | specified      |                |
|                |                | mount.         |                |
+----------------+----------------+----------------+----------------+
| [MOVE](MO      | R              | Returns the    |                |
| VE "wikilink") |                | movement flags |                |
| *direction*    |                | for the tile   |                |
|                |                | in the given   |                |
|                |                | direction (see |                |
|                |                | can_flags in   |                |
|                |                | sph            |                |
|                |                | ere_defs.scp). |                |
+----------------+----------------+----------------+----------------+
| [MOVE](MO      | W              | Moves the      |                |
| VE "wikilink") |                | object         |                |
| *direction,    |                | relative to    |                |
| amount*\       |                | its current    |                |
| [MOVE](MO      |                | position.      |                |
| VE "wikilink") |                |                |                |
| *x y*          |                |                |                |
+----------------+----------------+----------------+----------------+
| [MO            | W              | Moves the      |                |
| VENEAR](MOVENE |                | character to a |                |
| AR "wikilink") |                | random         |                |
| *object_uid,   |                | location near  |                |
| distance*      |                | another object |                |
|                |                | within a       |                |
|                |                | certain        |                |
|                |                | distance.      |                |
+----------------+----------------+----------------+----------------+
| [MOVETO](MOVE  | W              | Moves the      |                |
| TO "wikilink") |                | character to a |                |
| *location*     |                | specific       |                |
|                |                | location.      |                |
+----------------+----------------+----------------+----------------+
| [NAME](NA      | RW             | Gets or sets   |                |
| ME "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | name.          |                |
+----------------+----------------+----------------+----------------+
| [NEWBIESK      | W              | Distributes    |                |
| ILL](NEWBIESKI |                | items that are |                |
| LL "wikilink") |                | associated     |                |
| *skill_id*     |                | with the       |                |
|                |                | specified      |                |
|                |                | skill, to the  |                |
|                |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Generates      |                |
| NEWGOLD](NEWGO |                | *amount* gold  |                |
| LD "wikilink") |                | in the         |                |
| *amount*       |                | character\'s   |                |
|                |                | backpack.      |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Generates the  |                |
| NEWLOOT](NEWLO |                | specified item |                |
| OT "wikilink") |                | or template    |                |
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
| IGHT](NIGHTSIG |                | whether or not |                |
| HT "wikilink") |                | the character  |                |
|                |                | has nightsight |                |
|                |                | enabled.       |                |
+----------------+----------------+----------------+----------------+
| [NOTOGETF      | RW             | Gets the       |                |
| LAG](NOTOGETFL |                | character\'s   |                |
| AG "wikilink") |                | notoriety      |                |
| *viewer_uid,   |                | flags as seen  |                |
| al             |                | by the         |                |
| low_incognito* |                | specified      |                |
|                |                | viewer.        |                |
+----------------+----------------+----------------+----------------+
| [NPC](N        | RW             | Gets or sets   |                |
| PC "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | AI type.       |                |
+----------------+----------------+----------------+----------------+
| [NUDG          | W              | Decreases the  |                |
| EDOWN](NUDGEDO |                | character\'s Z |                |
| WN "wikilink") |                | level.         |                |
| *amount*       |                |                |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Increases the  |                |
| NUDGEUP](NUDGE |                | characer\'s Z  |                |
| UP "wikilink") |                | level.         |                |
| *amount*       |                |                |                |
+----------------+----------------+----------------+----------------+
| [OBODY](OBO    | RW             | Gets or sets   |                |
| DY "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | original body. |                |
+----------------+----------------+----------------+----------------+
| [OPENPAPERDOL  | W              | Displays the   |                |
| L](OPENPAPERDO |                | character\'s   |                |
| LL "wikilink") |                | paperdoll to   |                |
|                |                | SRC.           |                |
+----------------+----------------+----------------+----------------+
| [OPENPAPERDOL  | W              | Displays a     |                |
| L](OPENPAPERDO |                | specified      |                |
| LL "wikilink") |                | character\'s   |                |
| *              |                | paperdoll to   |                |
| character_uid* |                | this           |                |
|                |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [OSKIN](OSK    | RW             | Gets or sets   |                |
| IN "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | original       |                |
|                |                | colour.        |                |
+----------------+----------------+----------------+----------------+
| [ODEX](OD      | RW             | Gets or sets   |                |
| EX "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | base dexterity |                |
|                |                | (without       |                |
|                |                | modifiers).    |                |
+----------------+----------------+----------------+----------------+
| [OINT](OI      | RW             | Gets or sets   |                |
| NT "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | base           |                |
|                |                | intelligence   |                |
|                |                | (without       |                |
|                |                | modifiers).    |                |
+----------------+----------------+----------------+----------------+
| [OSTR](OS      | RW             | Gets or sets   |                |
| TR "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | base strength  |                |
|                |                | (without       |                |
|                |                | modifiers).    |                |
+----------------+----------------+----------------+----------------+
| [PACK](PA      | W              | Opens the      |                |
| CK "wikilink") |                | character\'s   |                |
|                |                | backpack for   |                |
|                |                | SRC to view.   |                |
+----------------+----------------+----------------+----------------+
| [POISON](POIS  | W              | Poisons the    |                |
| ON "wikilink") |                | character,     |                |
| *strength*     |                | with the       |                |
|                |                | specified      |                |
|                |                | poison         |                |
|                |                | strength.      |                |
+----------------+----------------+----------------+----------------+
| [POLY](PO      | W              | Begins casting |                |
| LY "wikilink") |                | the polymorph  |                |
| *character_id* |                | spell, with    |                |
|                |                | *character_id* |                |
|                |                | being the      |                |
|                |                | character to   |                |
|                |                | turn into.     |                |
+----------------+----------------+----------------+----------------+
| [PROMPTCONSOL  | W              | Displays a     |                |
| E](PROMPTCONSO |                | prompt message |                |
| LE "wikilink") |                | to SRC and     |                |
| *function,     |                | passes their   |                |
| p              |                | response into  |                |
| rompt_message* |                | a specified    |                |
|                |                | function.      |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Displays a     |                |
| PROMPTCONSOLEU |                | prompt message |                |
| ](PROMPTCONSOL |                | to SRC and     |                |
| EU "wikilink") |                | passes their   |                |
| *function,     |                | response into  |                |
| p              |                | a specified    |                |
| rompt_message* |                | function,      |                |
|                |                | supporting     |                |
|                |                | UNICODE        |                |
|                |                | response.      |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Sets the       |                |
| PRIVSET](PRIVS |                | PLEVEL of the  |                |
| ET "wikilink") |                | character.     |                |
| *plevel*       |                |                |                |
+----------------+----------------+----------------+----------------+
| [RANGE](RAN    | R              | Gets the       |                |
| GE "wikilink") |                | combat range   |                |
|                |                | of the         |                |
|                |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Clears the     |                |
| RELEASE](RELEA |                | character\'s   |                |
| SE "wikilink") |                | owners.        |                |
+----------------+----------------+----------------+----------------+
| [REMOVE](REMO  | W              | Deletes the    |                |
| VE "wikilink") |                | character.     |                |
| *allow_p       |                |                |                |
| layer_removal* |                |                |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Removes the    |                |
| REMOVEFROMVIEW |                | object from    |                |
| ](REMOVEFROMVI |                | nearby         |                |
| EW "wikilink") |                | clients\'      |                |
|                |                | screens.       |                |
+----------------+----------------+----------------+----------------+
| [              | RW             | Gets or sets   |                |
| RESCOLD](RESCO |                | the            |                |
| LD "wikilink") |                | character\'s   |                |
|                |                | resistance to  |                |
|                |                | cold.          |                |
+----------------+----------------+----------------+----------------+
| [RESCOL        | RW             | Gets or sets   |                |
| DMAX](RESCOLDM |                | the            |                |
| AX "wikilink") |                | character\'s   |                |
|                |                | maximum        |                |
|                |                | resistance to  |                |
|                |                | cold.          |                |
+----------------+----------------+----------------+----------------+
| [RE            | R              | Returns the    |                |
| SCOUNT](RESCOU |                | total amount   |                |
| NT "wikilink") |                | of a specific  |                |
| *item_defname* |                | item equipped  |                |
|                |                | to the         |                |
|                |                | character or   |                |
|                |                | inside their   |                |
|                |                | baackpack.     |                |
+----------------+----------------+----------------+----------------+
| [RESENDTOOLTI  | W              | Forces Sphere  |                |
| P](RESENDTOOLT |                | to update the  |                |
| IP "wikilink") |                | tooltips for   |                |
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
| NERGY](RESENER |                | the            |                |
| GY "wikilink") |                | character\'s   |                |
|                |                | resistance to  |                |
|                |                | energy.        |                |
+----------------+----------------+----------------+----------------+
| [RESENERGYM    | RW             | Gets or sets   |                |
| AX](RESENERGYM |                | the            |                |
| AX "wikilink") |                | character\'s   |                |
|                |                | maximum        |                |
|                |                | resistance to  |                |
|                |                | energy.        |                |
+----------------+----------------+----------------+----------------+
| [              | RW             | Gets or sets   |                |
| RESFIRE](RESFI |                | the            |                |
| RE "wikilink") |                | character\'s   |                |
|                |                | resistance to  |                |
|                |                | fire.          |                |
+----------------+----------------+----------------+----------------+
| [RESFIR        | RW             | Gets or sets   |                |
| EMAX](RESFIREM |                | the            |                |
| AX "wikilink") |                | character\'s   |                |
|                |                | maximum        |                |
|                |                | resistance to  |                |
|                |                | fire.          |                |
+----------------+----------------+----------------+----------------+
| [RESP          | RW             | Gets or sets   |                |
| OISON](RESPOIS |                | the            |                |
| ON "wikilink") |                | character\'s   |                |
|                |                | resistance to  |                |
|                |                | poison.        |                |
+----------------+----------------+----------------+----------------+
| [RESPOISONM    | RW             | Gets or sets   |                |
| AX](RESPOISONM |                | the            |                |
| AX "wikilink") |                | character\'s   |                |
|                |                | maximum        |                |
|                |                | resistance to  |                |
|                |                | poison.        |                |
+----------------+----------------+----------------+----------------+
| [              | R              | Returns 1 if   |                |
| RESTEST](RESTE |                | all of the     |                |
| ST "wikilink") |                | items in the   |                |
| *item_list*    |                | list can be    |                |
|                |                | found equipped |                |
|                |                | to the         |                |
|                |                | character or   |                |
|                |                | inside their   |                |
|                |                | backpack.      |                |
+----------------+----------------+----------------+----------------+
| [RESU          | W              | Resurrects the |                |
| RRECT](RESURRE |                | character. If  |                |
| CT "wikilink") |                | *force* is 1   |                |
| *force*        |                | then usual     |                |
|                |                | anti-magic     |                |
|                |                | checks are     |                |
|                |                | bypasses.      |                |
+----------------+----------------+----------------+----------------+
| [SALUTE](SALU  | W              | Makes the      |                |
| TE "wikilink") |                | character      |                |
| *object_uid*   |                | salute a       |                |
|                |                | specified      |                |
|                |                | object or SRC. |                |
+----------------+----------------+----------------+----------------+
| [SAY](S        | W              | Makes the      |                |
| AY "wikilink") |                | character      |                |
| *message*      |                | speak a        |                |
|                |                | message.       |                |
+----------------+----------------+----------------+----------------+
| [SAYU](SA      | W              | Makes the      |                |
| YU "wikilink") |                | character      |                |
| *message*      |                | speak a UTF-8  |                |
|                |                | message        |                |
+----------------+----------------+----------------+----------------+
| [SAYUA](SAY    | W              | MAkes the      |                |
| UA "wikilink") |                | character      |                |
| *colour,       |                | speak a        |                |
| talkmode,      |                | UNICODE        |                |
| font, lang_id, |                | message.       |                |
| text*          |                |                |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Displays a     |                |
| SDIALOG](SDIAL |                | dialog to SRC, |                |
| OG "wikilink") |                | providing that |                |
| *dialog_id,    |                | it is not      |                |
| page,          |                | already open.  |                |
| parameters*    |                |                |                |
+----------------+----------------+----------------+----------------+
| [SERIAL](SERI  | R              | Gets the       |                |
| AL "wikilink") |                | item\'s unique |                |
|                |                | ID in the      |                |
|                |                | world.         |                |
+----------------+----------------+----------------+----------------+
| [SEX](S        | R              | Returns        |                |
| EX "wikilink") |                | *value_male*   |                |
| *value_male    |                | or             |                |
| :value_female* |                | *value_female* |                |
|                |                | depending on   |                |
|                |                | the            |                |
|                |                | character\'s   |                |
|                |                | gender.        |                |
+----------------+----------------+----------------+----------------+
| [SE            | R              | Converts the   |                |
| XTANTP](SEXTAN |                | character\'s   |                |
| TP "wikilink") |                | location or a  |                |
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
| [SHIP.n](SHIP  | R              | X branch only. |                |
| .n "wikilink") |                | Added to       |                |
|                |                | access the     |                |
|                |                | ship in the    |                |
|                |                | Nth position,  |                |
|                |                | eg:            |                |
|                |                | ship.3.Redeed  |                |
+----------------+----------------+----------------+----------------+
| [SHIPS](SHI    | R              | X branch only. |                |
| PS "wikilink") |                | Return the     |                |
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
| HECK](SKILLCHE |                | check for      |                |
| CK "wikilink") |                | skill success, |                |
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
| LGAIN](SKILLGA |                | Sphere\'s      |                |
| IN "wikilink") |                | skill gain for |                |
| *skill,        |                | the specified  |                |
| difficulty*    |                | skill, with    |                |
|                |                | the given      |                |
|                |                | difficulty     |                |
|                |                | (0-100)        |                |
+----------------+----------------+----------------+----------------+
| [SKIL          | R              | Returns 1 if   |                |
| LTEST](SKILLTE |                | the character  |                |
| ST "wikilink") |                | possess all of |                |
| *skill_list*   |                | the skills in  |                |
|                |                | the list.      |                |
+----------------+----------------+----------------+----------------+
| [SKILLT        | R              | Returns the    |                |
| OTAL](SKILLTOT |                | total value of |                |
| AL "wikilink") |                | all the        |                |
|                |                | character\'s   |                |
|                |                | skills.        |                |
+----------------+----------------+----------------+----------------+
| [SKILLT        | R              | Returns the    |                |
| OTAL](SKILLTOT |                | total value of |                |
| AL "wikilink") |                | all the        |                |
| *skill_group*  |                | character\'s   |                |
|                |                | skills with    |                |
|                |                | the specified  |                |
|                |                | group flag(s). |                |
+----------------+----------------+----------------+----------------+
| [SKILLT        | R              | Returns the    |                |
| OTAL](SKILLTOT |                | total value of |                |
| AL "wikilink") |                | all the        |                |
| *-amount*      |                | character\'s   |                |
|                |                | skills that    |                |
|                |                | are under      |                |
|                |                | *amount*.      |                |
+----------------+----------------+----------------+----------------+
| [SKILLT        | R              | Returns the    |                |
| OTAL](SKILLTOT |                | total value of |                |
| AL "wikilink") |                | all the        |                |
| *+amount*      |                | character\'s   |                |
|                |                | skills that    |                |
|                |                | are over       |                |
|                |                | *amount*.      |                |
+----------------+----------------+----------------+----------------+
| [SKILLUSEQUIC  | R              | Quickly uses a |                |
| K](SKILLUSEQUI |                | skill,         |                |
| CK "wikilink") |                | returning 1 if |                |
| *skill_id,     |                | the attempt    |                |
| difficulty*    |                | was            |                |
|                |                | successful.    |                |
+----------------+----------------+----------------+----------------+
| [SLEEP](SLE    | W              | Makes the      |                |
| EP "wikilink") |                | character      |                |
| *              |                | appear to      |                |
| fall_forwards* |                | sleep.         |                |
+----------------+----------------+----------------+----------------+
| [SOUND](SOU    | W              | Plays a sound  |                |
| ND "wikilink") |                | from this      |                |
| *sound_id,     |                | character.     |                |
| repeat*        |                |                |                |
+----------------+----------------+----------------+----------------+
| [SPELLEFF      | W              | Causes the     |                |
| ECT](SPELLEFFE |                | character to   |                |
| CT "wikilink") |                | be affected by |                |
| *spell_id,     |                | a spell.       |                |
| strength,      |                |                |                |
| source_        |                |                |                |
| character_uid, |                |                |                |
| so             |                |                |                |
| urce_item_uid* |                |                |                |
+----------------+----------------+----------------+----------------+
| [SPEECHCOLO    | RW             | Override       |                |
| ROVERRIDE](SPE |                | client speech  |                |
| ECHCOLOROVERRI |                | hue.           |                |
| DE "wikilink") |                |                |                |
| *value*        |                |                |                |
+----------------+----------------+----------------+----------------+
| [STAM](ST      | RW             | Gets or sets   |                |
| AM "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | stamina.       |                |
+----------------+----------------+----------------+----------------+
| [STEPSTEA      | RW             | Gets or sets   |                |
| LTH](STEPSTEAL |                | the amount of  |                |
| TH "wikilink") |                | steps a        |                |
|                |                | character can  |                |
|                |                | do while using |                |
|                |                | the Stealth    |                |
|                |                | skill.         |                |
+----------------+----------------+----------------+----------------+
| [STONE](STO    | RW             | Gets or sets   |                |
| NE "wikilink") |                | whether or not |                |
|                |                | the character  |                |
|                |                | is trapped in  |                |
|                |                | stone.         |                |
+----------------+----------------+----------------+----------------+
| [STR](S        | RW             | Gets or sets   |                |
| TR "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | total          |                |
|                |                | strength.      |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Forces the     |                |
| SUICIDE](SUICI |                | character to   |                |
| DE "wikilink") |                | commit         |                |
|                |                | suicide.       |                |
+----------------+----------------+----------------+----------------+
| [SUMMON        | W              | Teleports the  |                |
| CAGE](SUMMONCA |                | character to   |                |
| GE "wikilink") |                | SRC\'s,        |                |
|                |                | surrounded by  |                |
|                |                | a cage multi.  |                |
+----------------+----------------+----------------+----------------+
| [SU            | W              | Teleports the  |                |
| MMONTO](SUMMON |                | character to   |                |
| TO "wikilink") |                | SRC\'s         |                |
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
| GCOUNT](TAGCOU |                | number of TAGs |                |
| NT "wikilink") |                | stored on the  |                |
|                |                | item.          |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Outputs a list |                |
| TAGLIST](TAGLI |                | of the         |                |
| ST "wikilink") |                | object\'s      |                |
|                |                | TAGs.          |                |
+----------------+----------------+----------------+----------------+
| [TARG          | W              | Displays a     |                |
| ET](TARGET "wi |                | targeting      |                |
| kilink")*FGMW* |                | cursor to SRC. |                |
| *function*     |                |                |                |
+----------------+----------------+----------------+----------------+
| [TIMER](TIM    | RW             | Gets or sets   |                |
| ER "wikilink") |                | the length of  |                |
|                |                | time before    |                |
|                |                | the item\'s    |                |
|                |                | timer expires, |                |
|                |                | in seconds.    |                |
+----------------+----------------+----------------+----------------+
| [TIMERD](TIME  | RW             | Gets or sets   |                |
| RD "wikilink") |                | the length of  |                |
|                |                | time before    |                |
|                |                | the item\'s    |                |
|                |                | timer expires, |                |
|                |                | in tenths of a |                |
|                |                | second.        |                |
+----------------+----------------+----------------+----------------+
| [TIMERF](TIME  | W              | Scheduled a    |                |
| RF "wikilink") |                | function to be |                |
| *time,         |                | executed on    |                |
| function*      |                | this object in |                |
|                |                | *time*         |                |
|                |                | seconds.       |                |
+----------------+----------------+----------------+----------------+
| [TIMERF](TIME  | W              | Clears all     |                |
| RF "wikilink") |                | scheduled      |                |
| *CLEAR*        |                | functions from |                |
|                |                | the character. |                |
+----------------+----------------+----------------+----------------+
| [TIMERF](TIME  | W              | Stops the      |                |
| RF "wikilink") |                | specified      |                |
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
| TIMERMS](TIMER |                | timer to       |                |
| MS "wikilink") |                | elapse after   |                |
|                |                | the given      |                |
|                |                | number of      |                |
|                |                | milliseconds.  |                |
+----------------+----------------+----------------+----------------+
| [              | RW             | Gets or sets   |                |
| TITHING](TITHI |                | the number of  |                |
| NG "wikilink") |                | tithing points |                |
|                |                | the character  |                |
|                |                | has.           |                |
+----------------+----------------+----------------+----------------+
| [TITLE](TIT    | RW             | Gets or sets   |                |
| LE "wikilink") |                | the            |                |
|                |                | character\'s   |                |
|                |                | title.         |                |
+----------------+----------------+----------------+----------------+
| [TOWNAB        | R              | Returns the    |                |
| BREV](TOWNABBR |                | character\'s   |                |
| EV "wikilink") |                | town           |                |
|                |                | abbreviation.  |                |
+----------------+----------------+----------------+----------------+
| [              | R              | Fires a custom |                |
| TRIGGER](TRIGG |                | trigger and    |                |
| ER "wikilink") |                | returns the    |                |
| *trig_name,    |                | RETURN value.  |                |
| trig_type*     |                |                |                |
+----------------+----------------+----------------+----------------+
| [UID](U        | R              | Gets the       |                |
| ID "wikilink") |                | item\'s unique |                |
|                |                | ID in the      |                |
|                |                | world.         |                |
+----------------+----------------+----------------+----------------+
| [UNDE          | W              | Toggles the    |                |
| RWEAR](UNDERWE |                | display of     |                |
| AR "wikilink") |                | underwear on   |                |
|                |                | the character. |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Unequips an    |                |
| UNEQUIP](UNEQU |                | item from the  |                |
| IP "wikilink") |                | character,     |                |
| *item_uid*     |                | placing it in  |                |
|                |                | their          |                |
|                |                | backpack.      |                |
+----------------+----------------+----------------+----------------+
| [UPDATE](UPDA  | W              | Updates the    |                |
| TE "wikilink") |                | state of the   |                |
|                |                | character to   |                |
|                |                | nearby         |                |
|                |                | clients.       |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Updates the    |                |
| UPDATEX](UPDAT |                | state of the   |                |
| EX "wikilink") |                | character to   |                |
|                |                | nearby         |                |
|                |                | clients,       |                |
|                |                | removing it    |                |
|                |                | from their     |                |
|                |                | view first to  |                |
|                |                | ensure a full  |                |
|                |                | refresh.       |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Double clicks  |                |
| USEITEM](USEIT |                | the character, |                |
| EM "wikilink") |                | with SRC as    |                |
|                |                | the source of  |                |
|                |                | the event,     |                |
|                |                | without        |                |
|                |                | checking for   |                |
|                |                | line of sight. |                |
+----------------+----------------+----------------+----------------+
| [              | W              | Double clicks  |                |
| USEITEM](USEIT |                | an object,     |                |
| EM "wikilink") |                | with the       |                |
| *object_uid*   |                | character as   |                |
|                |                | SRC.           |                |
+----------------+----------------+----------------+----------------+
| [VISUALRA      | RW             | Gets or sets   |                |
| NGE](VISUALRAN |                | the            |                |
| GE "wikilink") |                | character\'s   |                |
|                |                | sight range.   |                |
+----------------+----------------+----------------+----------------+
| [WEIGHT](WEIG  | R              | Gets the       |                |
| HT "wikilink") |                | weight of the  |                |
|                |                | character.     |                |
+----------------+----------------+----------------+----------------+
| [WHERE](WHE    | W              | Describes the  |                |
| RE "wikilink") |                | character\'s   |                |
|                |                | location to    |                |
|                |                | SRC.           |                |
+----------------+----------------+----------------+----------------+
| [Z]            | R              | Gets the Z     |                |
| (Z "wikilink") |                | position of    |                |
|                |                | the character. |                |
+----------------+----------------+----------------+----------------+

## Triggers

Here is a list of all character triggers. Click on the trigger name for
more detailed information such as arguments and examples.

  ---------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------- --------------------
  **Name**                                                         **Description**                                                                                                                   **Sphere X only?**
  [\@AfterClick](@AfterClick "wikilink")                           Fires when the object has been single-clicked, just before the overhead name is shown.                                            
  [\@Attack](@Attack "wikilink")                                   Fires when the character begins attacking another.                                                                                
  [\@CallGuards](@CallGuards "wikilink")                           Fires when the character calls for guards.                                                                                        
  [\@CharAttack](@CharAttack "wikilink")                           Fires when the character is attacked by another character.                                                                        
  [\@CharClick](@CharClick "wikilink")                             Fires when the character is clicked by another character.                                                                         
  [\@CharClientTooltip](@CharClientTooltip "wikilink")             Fires when the tooltips are about to be sent to the character.                                                                    
  [\@CharDClick](@CharDClick "wikilink")                           Fires when the character double clicks another character.                                                                         
  [\@CharTradeAccepted](@CharTradeAccepted "wikilink")             Fires when another character accepts trade with the character.                                                                    
  [\@Click](@Click "wikilink")                                     Fires when the object has been single-clicked.                                                                                    
  [\@ClientTooltip](@ClientTooltip "wikilink")                     Fires when tooltips for this character are about to be sent to a client.                                                          
  [\@CombatAdd](@CombatAdd "wikilink")                             Fires when someone is being added to my attacker list.                                                                            
  [\@CombatDelete](@CombatDelete "wikilink")                       Fires when someone is deleted from my attacker list.                                                                              
  [\@CombatEnd](@CombatEnd "wikilink")                             Fires when someone is being deleted from my attacker list and I don\'t have any more viable targets.                              
  [\@CombatStart](@CombatStart "wikilink")                         Fires when adding first attacker to my list.                                                                                      
  [\@ContextMenuRequest](@ContextMenuRequest "wikilink")           Fires when a client requests the context menu options for the object.                                                             
  [\@ContextMenuSelect](@ContextMenuSelect "wikilink")             Fires when a client selects a context menu option for the object.                                                                 
  [\@Create](@Create "wikilink")                                   Fires when the object is initially created, before it is placed in the world.                                                     
  [\@Criminal](@Criminal "wikilink")                               Fires when the character becomes a criminal.                                                                                      
  [\@DClick](@DClick "wikilink")                                   Fires when the object is double-clicked.                                                                                          
  [\@Death](@Death "wikilink")                                     Fires when the character\'s hitpoints reaches zero.                                                                               
  [\@DeathCorpse](@DeathCorpse "wikilink")                         Fires when a corpse is created for the character.                                                                                 
  [\@Destroy](@Destroy "wikilink")                                 Fires when the object is being deleted.                                                                                           
  [\@Dismount](@Dismount "wikilink")                               Fires when the character dismounts their ride.                                                                                    
  [\@Dye](@Dye "wikilink")                                         Fires when the character is about to change their color or the color of an object.                                                
  [\@Eat](@Eat "wikilink")                                         Fires when the character eats something.                                                                                          
  [\@EnvironChange](@EnvironChange "wikilink")                     Fires when the environment changes for the character.                                                                             
  [\@ExpChange](@ExpChange "wikilink")                             Fires when the character\'s experience points change.                                                                             
  [\@ExpLevelChange](@ExpLevelChange "wikilink")                   Fires when the character\'s experience level changes.                                                                             
  [\@FameChange](@FameChange "wikilink")                           Fires when the character\'s fame changes.                                                                                         
  [\@GetHit](@GetHit "wikilink")                                   Fires when the character receives damage.                                                                                         
  [\@Hit](@Hit "wikilink")                                         Fires when the character hits another in combat.                                                                                  
  [\@HitMiss](@HitMiss "wikilink")                                 Fires when the character fails to hit another in combat.                                                                          
  [\@HitParry](@HitParry "wikilink")                               X branch only. Fires when the character is attempting to parry a hit.                                                             X
  [\@HitTry](@HitTry "wikilink")                                   Fires when the character tries to hit another in combat.                                                                          
  [\@HouseDesignCommit](@HouseDesignCommit "wikilink")             Fires when the character commits a new house design.                                                                              
  [\@HouseDesignExit](@HouseDesignExit "wikilink")                 Fires when the character exits house design mode.                                                                                 
  [\@Hunger](@Hunger "wikilink")                                   Fires when the character\'s food level decreases.                                                                                 
  [\@ItemAfterClick](@ItemAfterClick "wikilink")                   Fires when the character single-clicks an item, just before the overhead name is shown.                                           
  [\@ItemBuy](@ItemBuy "wikilink")                                 Fires when the character buys an item from a vendor.                                                                              
  [\@ItemClick](@ItemClick "wikilink")                             Fires when the character single-clicks an item.                                                                                   
  [\@ItemClientTooltip](@ItemClientTooltip "wikilink")             Fires when the tooltips are about to be sent to the client for an item.                                                           
  [\@ItemContextMenuRequest](@ItemContextMenuRequest "wikilink")   Fires when the character requests the context menu options for an item.                                                           
  [\@ItemContextMenuSelect](@ItemContextMenuSelect "wikilink")     Fires when the character selects a context menu option for an item.                                                               
  [\@ItemCreate](@ItemCreate "wikilink")                           Fires when an item is initially created, before it is placed in the world, and the character is in some way responsible for it.   
  [\@ItemDamage](@ItemDamage "wikilink")                           Fires when the character damages an item.                                                                                         
  [\@ItemDClick](@ItemDClick "wikilink")                           Fires when the character double-clicks an item.                                                                                   
  [\@ItemDropOn_Char](@ItemDropOn_Char "wikilink")                 Fires when the character drops an item on to a character.                                                                         
  [\@ItemDropOn_Ground](@ItemDropOn_Ground "wikilink")             Fires when the character drops an item on to the ground.                                                                          
  [\@ItemDropOn_Item](@ItemDropOn_Item "wikilink")                 Fires when the character drops an item on to another item.                                                                        
  [\@ItemDropOn_Self](@ItemDropOn_Self "wikilink")                 Fires when the character drops an item inside another item.                                                                       
  [\@ItemEquip](@ItemEquip "wikilink")                             Fires when the character equips an item.                                                                                          
  [\@ItemEquipTest](@ItemEquipTest "wikilink")                     Fires when the characer is about to equip an item.                                                                                
  [\@ItemPickUp_Ground](@ItemPickUp_Ground "wikilink")             Fires when the character picks an item up from the ground.                                                                        
  [\@ItemPickUp_Pack](@ItemPickUp_Pack "wikilink")                 Fires when the character picks an item up from inside a container.                                                                
  [\@ItemPickUp_Self](@ItemPickUp_Self "wikilink")                 Fires when the character picks an item up from inside another item.                                                               
  [\@ItemPickUp_Stack](@ItemPickUp_Stack "wikilink")               Fires when the character picks up an item from a stack.                                                                           
  [\@ItemSell](@ItemSell "wikilink")                               Fires when the character sells an item to a vendor.                                                                               
  [\@ItemSmelt](@ItemSmelt "wikilink")                             Fires when the character smelt an item.                                                                                           X
  [\@ItemSpellEffect](@ItemSpellEffect "wikilink")                 Fires when the character hits an item with a spell.                                                                               
  [\@ItemStep](@ItemStep "wikilink")                               Fires when the character steps on an item.                                                                                        
  [\@ItemTargOn_Cancel](@ItemTargOn_Cancel "wikilink")             Fires when the character cancels an item\'s target cursor.                                                                        
  [\@ItemTargOn_Char](@ItemTargOn_Char "wikilink")                 Fires when the character targets a character with an item\'s target cursor.                                                       
  [\@ItemTargOn_Ground](@ItemTargOn_Ground "wikilink")             Fires when the character targets the ground with an item\'s target cursor.                                                        
  [\@ItemTargOn_Item](@ItemTargOn_Item "wikilink")                 Fires when the character targets an item with an item\'s target cursor.                                                           
  [\@ItemToolTip](@ItemToolTip "wikilink")                         Fires when the character requests old-style tooltips for an item.                                                                 
  [\@ItemUnEquip](@ItemUnEquip "wikilink")                         Fires when the character unequips an item.                                                                                        
  [\@Jailed](@Jailed "wikilink")                                   Fires when the character is sent to jail.                                                                                         
  [\@KarmaChange](@KarmaChange "wikilink")                         Fires when the character\'s karma changes.                                                                                        
  [\@Kill](@Kill "wikilink")                                       Fires when the character kills another character.                                                                                 
  [\@Login](@Login "wikilink")                                     Fires when the character logs in.                                                                                                 
  [\@Logout](@Logout "wikilink")                                   Fires when the character logs out.                                                                                                
  [\@Mount](@Mount "wikilink")                                     Fires when the character mounts a ride.                                                                                           
  [\@MurderDecay](@MurderDecay "wikilink")                         Fires when one of the character\'s kills is about to decay.                                                                       
  [\@MurderMark](@MurderMark "wikilink")                           Fires when the character is about to gain a kill.                                                                                 
  [\@NotoSend](@NotoSend "wikilink")                               Fires the status bar/character notoriety color is sent to another players.                                                        
  [\@NPCAcceptItem](@NPCAcceptItem "wikilink")                     Fires when the NPC receives an item.                                                                                              
  [\@NpcActCast](@NpcActCast "wikilink")                           Fires when the NPC is selecting the spell to cast.                                                                                X
  [\@NPCActFight](@NPCActFight "wikilink")                         Fires when the NPC makes a combat decision.                                                                                       
  [\@NPCActFollow](@NPCActFollow "wikilink")                       Fires when the NPC follows another character.                                                                                     
  [\@NPCAction](@NPCAction "wikilink")                             Fires when the NPC is about to perform an AI action.                                                                              
  [\@NPCActWander](@NPCActWander "wikilink")                       X branch only. Fires each step an NPC does while wandering.                                                                       
  [\@NPCHearGreeting](@NPCHearGreeting "wikilink")                 Fires when the NPC hears a character for the first time.                                                                          
  [\@NPCHearUnknown](@NPCHearUnknown "wikilink")                   Fires when the NPC hears something they don\'t understand.                                                                        
  [\@NPCLookAtChar](@NPCLookAtChar "wikilink")                     Fires then the NPC looks at a character.                                                                                          
  [\@NPCLookAtItem](@NPCLookAtItem "wikilink")                     Fires when the NPC looks at an item.                                                                                              
  [\@NPCLostTeleport](@NPCLostTeleport "wikilink")                 Fires when the NPC is lost and is about to be teleported back to their [HOME](HOME "wikilink").                                   
  [\@NPCRefuseItem](@NPCRefuseItem "wikilink")                     Fires when the NPC refuses an item being given to them.                                                                           
  [\@NPCRestock](@NPCRestock "wikilink")                           Fires when the NPC is having their items restocked.                                                                               
  [\@NPCSeeNewPlayer](@NPCSeeNewPlayer "wikilink")                 Fires when the NPC first sees a player.                                                                                           
  [\@NPCSeeWantItem](@NPCSeeWantItem "wikilink")                   Fires when the NPC sees an item they want.                                                                                        
  [\@NPCSpecialAction](@NPCSpecialAction "wikilink")               Fires when the NPC is about to perform a special action (leaving fire trail, dropping web).                                       
  [\@PayGold](@PayGold "wikilink")                                 Fires when the character receives a payment. (Experimental Build Only)                                                            
  [\@PersonalSpace](@PersonalSpace "wikilink")                     Fires when the character is stepped on.                                                                                           
  [\@PetDesert](@PetDesert "wikilink")                             Fires when the character deserts its owner.                                                                                       
  [\@Profile](@Profile "wikilink")                                 Fires when a player attempts to read the character\'s profile from the paperdoll.                                                 
  [\@ReceiveItem](@ReceiveItem "wikilink")                         Fires when the NPC receives an item from another character, before they decide if they want it or not.                            
  [\@RegenStat](@RegenStat "wikilink")                             Fires when a character is going to regenerate any stat point.                                                                     
  [\@RegionEnter](@RegionEnter "wikilink")                         Fires when the character enters a region.                                                                                         
  [\@RegionLeave](@RegionLeave "wikilink")                         Fires when the character leaves a region.                                                                                         
  [\@RegionResourceFound](@RegionResourceFound "wikilink")         Fires after a resource has been selected and the resource bit has been created.                                                   
  [\@Rename](@Rename "wikilink")                                   Fires when the character renames another.                                                                                         
  [\@Resurrect](@Resurrect "wikilink")                             Fires when the character is being resurrected.                                                                                    
  [\@SeeCrime](@SeeCrime "wikilink")                               Fires when the character sees a crime take place.                                                                                 
  [\@SeeHidden](@SeeHidden "wikilink")                             Fires when this character is about to see a hidden character.                                                                     
  [\@SkillAbort](@SkillAbort "wikilink")                           Fires when the character aborts a skill.                                                                                          
  [\@SkillChange](@SkillChange "wikilink")                         Fires when the character\'s skill level changes.                                                                                  
  [\@SkillFail](@SkillFail "wikilink")                             Fires when the character fails a skill.                                                                                           
  [\@SkillGain](@SkillGain "wikilink")                             Fires when the character has a chance to gain in a skill.                                                                         
  [\@SkillMakeItem](@SkillMakeItem "wikilink")                     Fires when the character crafts an item.                                                                                          
  [\@SkillMenu](@SkillMenu "wikilink")                             Fires when a skill menu is shown to the character.                                                                                
  [\@SkillPreStart](@SkillPreStart "wikilink")                     Fires when the character starts a skill, before any hardcoded action takes place.                                                 
  [\@SkillSelect](@SkillSelect "wikilink")                         Fires when the character selects a skill on their skill menu.                                                                     
  [\@SkillStart](@SkillStart "wikilink")                           Fires when the character starts a skill.                                                                                          
  [\@SkillSuccess](@SkillSuccess "wikilink")                       Fires when the character succeeds at a skill.                                                                                     
  [\@SkillUseQuick](@SkillUseQuick "wikilink")                     Fires when the character quickly uses a skill.                                                                                    
  [\@SkillWait](@SkillWait "wikilink")                             Fires when Sphere wants to check if a character must wait before starting a skill.                                                
  [\@SpellBook](@SpellBook "wikilink")                             Fires when the character opens their spellbook.                                                                                   
  [\@SpellCast](@SpellCast "wikilink")                             Fires when the character casts a spell.                                                                                           
  [\@SpellEffect](@SpellEffect "wikilink")                         Fires when the character is hit by the effects of a spell.                                                                        
  [\@SpellEffectAdd](@SpellEffectAdd "wikilink")                   Fires when a spell memory is added to the character.                                                                              X
  [\@SpellEffectRemove](@SpellEffectRemove "wikilink")             Fires the spell memory is removed from the character.                                                                             X
  [\@SpellEffectTick](@SpellEffectTick "wikilink")                 Fires when the character is hit the effect of a periodic spell (like Poison spell).                                               X
  [\@SpellFail](@SpellFail "wikilink")                             Fires when the character fails to cast a spell.                                                                                   
  [\@SpellSelect](@SpellSelect "wikilink")                         Fires when the character selects a spell to cast.                                                                                 
  [\@SpellSuccess](@SpellSuccess "wikilink")                       Fires when the character successfully casts a spell.                                                                              
  [\@SpellTargetCancel](@SpellTargetCancel "wikilink")             Fires when the character cancels target selection for a spell they have just cast.                                                
  [\@StatChange](@StatChange "wikilink")                           Fires when the character\'s STR, DEX or INT is changed through skill gain.                                                        
  [\@StepStealth](@StepStealth "wikilink")                         Fires when the character takes a step whilst hidden.                                                                              
  [\@ToggleFlying](@ToggleFlying "wikilink")                       Fires when a Gargoyle Player is going to Fly or to Land.                                                                          
  [\@ToolTip](@ToolTip "wikilink")                                 Fires when a player requests old-style tooltips for this character.                                                               
  [\@TradeAccepted](@TradeAccepted "wikilink")                     Fires when the character accepts a trade with another player.                                                                     
  [\@TradeClose](@TradeClose "wikilink")                           Fires when a trade window is closed.                                                                                              
  [\@TradeCreate](@TradeCreate "wikilink")                         Fires when a player begins a trade with another player.                                                                           
  [\@UserBugReport](@UserBugReport "wikilink")                     Fires when the player submits a bug report.                                                                                       
  [\@UserChatButton](@UserChatButton "wikilink")                   Fires when the player presses the Chat button on the paperdoll.                                                                   
  [\@UserExtCmd](@UserExtCmd "wikilink")                           Fires when the player sends an extended command packet. (used by some macros)                                                     
  [\@UserExWalkLimit](@UserExWalkLimit "wikilink")                 Fires when the player\'s movement is restricted by the movement speed settings in Sphere.ini                                      
  [\@UserGuildButton](@UserGuildButton "wikilink")                 Fires when the player presses the Guild button on the paperdoll.                                                                  
  [\@UserKRToolbar](@UserKRToolbar "wikilink")                     Fires when the player presses a button on the toolbar.                                                                            
  [\@UserMailBag](@UserMailBag "wikilink")                         Fires when the player drags the mail bag on to another character.                                                                 
  [\@UserQuestArrowClick](@UserQuestArrowClick "wikilink")         Fires when the player clicks the quest arrow.                                                                                     
  [\@UserQuestButton](@UserQuestButton "wikilink")                 Fires when the player presses the Quest button on the paperdoll.                                                                  
  [\@UserSkills](@UserSkills "wikilink")                           Fires when the player opens their skill menu, or a skill update is sent to the player.                                            
  [\@UserSpecialMove](@UserSpecialMove "wikilink")                 Fires when the player uses a special move.                                                                                        
  [\@UserStats](@UserStats "wikilink")                             Fires when the player opens the status window.                                                                                    
  [\@UserUltimaStoreButton](@UserUltimaStoreButton "wikilink")     Fires when click on \'Ultima Store\' button on new clients 7.0.62+                                                                
  [\@UserVirtue](@UserVirtue "wikilink")                           Fires when the player presses on the Virtue button.                                                                               
  [\@UserVirtueInvoke](@UserVirtueInvoke "wikilink")               Fires when the player invokes a virtue through macros.                                                                            
  [\@UserWarmode](@UserWarmode "wikilink")                         Fires when the player switches between war and peace mode.                                                                        
  ---------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------- --------------------

## Players

Characters that are attached to an account become Player Characters. In
addition to the basic character references, properties and functions
they also receive the following:

### References {#references_1}

References return pointers to other objects (e.g. the REGION reference
allows you to access the REGION that an object is in). These can either
be accessed by using *\<REFNAME\>* to return the [UID](UID "wikilink")
(1 for object types that don\'t have UIDs) of the object or 0 if it
doesn\'t exist, or by using *\<REFNAME.KEY\>* where KEY is a valid
property/function/reference for the *REFNAME* object. Click on the name
for more detailed information such as usage and examples.

  ------------------------------------------------- ---------------- --------------------------------------------------------------------------------------------------
  **Name**                                          **Read/Write**   **Description**
  [GUILD](GUILD "wikilink")                         R                Gets the [guild stone](Special_Items#Guild.2FTown_Stones "wikilink") that the player belongs to.
  [SKILLCLASS](SKILLCLASS_(Reference) "wikilink")   RW               Gets or sets the player\'s [skillclass](SKILLCLASS "wikilink").
  [TOWN](TOWN "wikilink")                           R                Gets the [town stone](Special_Items#Guild.2FTown_Stones "wikilink") that the player belongs to.
  ------------------------------------------------- ---------------- --------------------------------------------------------------------------------------------------

### Properties and Functions {#properties_and_functions_1}

Here is a list of all player properties and functions. If a function is
marked as readable then it can return a value when used as
`<KEY>`{=html}. Click on the name for more detailed information such as
usage and examples.

  ----------------------------------------------- ---------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------
  **Name**                                        **Read/Write**   **Description**                                                                                                                                                        **Sphere X only?**
  [DEATHS](DEATHS "wikilink")                     RW               Gets or sets the number of times the player has died.                                                                                                                  
  [DSPEECH](DSPEECH "wikilink") *+/-speech_id*    RW               Gets a list of attached speech handlers, or adds or removes a speech handler to or from the player.                                                                    
  [GMPAGE](GMPAGE "wikilink")*.n.DELETE*          W                Deletes the nth GM page. (zero-based)                                                                                                                                  
  [GMPAGE](GMPAGE "wikilink")*.n.HANDLE*          W                Sets the player as the handler for the nth GM page. (zero-based)                                                                                                       
  [GMPAGE](GMPAGE "wikilink")*.n.key*             W                Executes the .page command with *key* as the arguments.                                                                                                                
  [ISDSPEECH](ISDSPEECH "wikilink")*.speech_id*   R                Returns 1 if the player has the given speech handler attached.                                                                                                         
  [KICK](KICK "wikilink")                         W                Disconnects and blocks the player\'s account.                                                                                                                          
  [KILLS](KILLS "wikilink")                       RW               Gets the number of murders the player has committed.                                                                                                                   
  [KRTOOLBARSTATUS](KRTOOLBARSTATUS "wikilink")   RW               Gets or sets whether or not the KR toolbar is enabled for this player.                                                                                                 
  [LASTUSED](LASTUSED "wikilink")                 RW               Gets the length of time since the player was last attached to a client, in seconds.                                                                                    
  [PASSWORD](PASSWORD "wikilink")                 W                Sets or clears the player\'s password.                                                                                                                                 
  [PFLAG](PFLAG "wikilink")                       RW               Gets or sets the player\'s PFLAG value.                                                                                                                                
  [PROFILE](PROFILE "wikilink")                   RW               Gets or sets the text to display on the player\'s profile.                                                                                                             
  [SKILLLOCK](SKILLLOCK "wikilink")*.skill_id*    RW               Gets or sets the lock state of the player\'s skill. 0 is Up. 1 is Down. 2 is Locked.                                                                                   
  [SPEEDMODE](SPEEDMODE "wikilink")               RW               Gets or sets the speed that the player moves at. (0=Normal, 1=Double Speed on Foot, 2=Always walk, 3=Always Run on Foot/Always Walk on Mount, 4=Can not Walk or Run)   
  [STATLOCK](STATLOCK "wikilink")\'\'.stat_id     RW               Gets or sets the lock state of the player\'s STR (0), DEX (2) or INT (1). \[0 = up, 1 = down, 2 = locked\]                                                             
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
  [ACTPRI](ACTPRI "wikilink")                              RW               Gets or sets the NPC\'s motivation towards their current action.                                                
  [BUY](BUY "wikilink")                                    W                Displays the shop window to SRC, in buy mode.                                                                   
  [BYE](BYE "wikilink")                                    W                Ends the NPC\'s current action.                                                                                 
  [FLEE](FLEE "wikilink") *distance*                       W                Begins moving the NPC away from its current location.                                                           
  [GOTO](GOTO "wikilink") *location*                       W                Begins moving the NPC towards the specified location.                                                           
  [HIRE](HIRE "wikilink")                                  W                Begins the hiring process between the NPC and SRC.                                                              
  [LEAVE](LEAVE "wikilink") *distance*                     W                Begins moving the NPC away from its current location.                                                           
  [NPC](NPC "wikilink")                                    RW               Gets or sets the NPC\'s AI type.                                                                                
  [HOMEDIST](HOMEDIST "wikilink")                          RW               Gets or sets the distance that the NPC can wander from its [HOME](HOME "wikilink") position.                    
  [PETRETRIEVE](PETRETRIEVE "wikilink")                    W                Enables SRC to retrieve their stabled pets from the NPC.                                                        
  [PETSTABLE](PETSTABLE "wikilink")                        W                Enables SRC to stable their pet with the NPC.                                                                   
  [RESTOCK](RESTOCK "wikilink") *force*                    W                Clears all of the NPC\'s stock, repopulating it when it is next accessed (or immediately if *force*=1)          
  [RUN](RUN "wikilink") *direction*                        W                Forces the NPC to run one tile in the specified direction.                                                      
  [SELL](SELL "wikilink")                                  W                Displays the shop window to SRC, in sell mode.                                                                  
  [SHRINK](SHRINK "wikilink")                              W                Shrinks the NPC into a figurine item.                                                                           
  [SPEECH](SPEECH "wikilink") *+/-speech_id*               RW               Gets the list of speech handlers attached to the NPC, or adds or removes a speech handler to or from the NPC.   
  [SPEECHCOLOR](SPEECHCOLOR "wikilink")                    RW               Gets or sets the colour of the NPC\'s speech.                                                                   
  [THROWDAM](THROWDAM "wikilink") *min,max*                RW               Gets or sets a range of damage used for thrown objects. (overrides chardef property)                            
  [THROWDAM](THROWDAM "wikilink") *dam*                    RW               Gets or sets the constant damage used for thrown objects. (overrides chardef property)                          
  [THROWDAMTYPE](THROWDAMTYPE "wikilink") *damage flags*   RW               y                                                                                                               Gets or sets the damage flags used for thrown objects. (overrides chardef property)
  [THROWOBJ](THROWOBJ "wikilink") *id*                     RW               Gets or sets the ID of an object to be thrown by NPCs. (overrides chardef property)                             
  [THROWRANGE](THROWRANGE "wikilink") *min,max*            RW               Gets or sets the range that an object can be thrown at. (overrides chardef property)                            
  [THROWRANGE](THROWRANGE "wikilink") *max*                RW               Gets or sets the range that an object can be thrown at with a default min of 2. (overrides chardef property)    
  [TRAIN](TRAIN "wikilink") *skill*                        W                Initiates training between the NPC and SRC.                                                                     
  [VENDCAP](VENDCAP "wikilink")                            RW               Gets or sets the amount of gold a vendor will restock to.                                                       
  [VENDGOLD](VENDGOLD "wikilink")                          RW               Gets or sets the amount of gold a vendor has.                                                                   
  [WALK](WALK "wikilink") *direction*                      W                Forces the NPC to walk one tile in the specified direction.                                                     
  -------------------------------------------------------- ---------------- --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------

## Clients

When a client is controlling a character, the following references,
properties and functions will be available:

### References {#references_2}

References return pointers to other objects (e.g. the REGION reference
allows you to access the REGION that an object is in). These can either
be accessed by using *\<REFNAME\>* to return the [UID](UID "wikilink")
(1 for object types that don\'t have UIDs) of the object or 0 if it
doesn\'t exist, or by using *\<REFNAME.KEY\>* where KEY is a valid
property/function/reference for the *REFNAME* object. Click on the name
for more detailed information such as usage and examples.

  --------------------------------------- ---------------- ---------------------------------------------------------------------------------------------------------------------- --------------------
  **Name**                                **Read/Write**   **Description**                                                                                                        **Sphere X only?**
  [GMPAGEP](GMPAGEP "wikilink")           R                Gets the [GM page](GM_Pages "wikilink") that the client is currently handling.                                         
  [HOUSEDESIGN](HOUSEDESIGN "wikilink")   R                Gets the [building](Special_Items#Customizable_Multis "wikilink") that is currently being designed by the client.      
  [PARTY](PARTY "wikilink")               R                Gets the [party](Parties "wikilink") that the client is a member of.                                                   
  [TARG](TARG "wikilink")                 RW               Gets or sets the [character](Characters "wikilink") or [item](Items "wikilink") that the client has targeted.          
  [TARGP](TARGP "wikilink")               RW               Gets or sets the [location](Map_Points "wikilink") that the client has targeted.                                       
  [TARGPROP](TARGPROP "wikilink")         RW               Gets or sets the character whose skills are shown in the client\'s skill menu.                                         
  [TARGPRV](TARGPRV "wikilink")           RW               Gets or sets the [character](Characters "wikilink") or [item](Items "wikilink") that the client previously targeted.   
  --------------------------------------- ---------------- ---------------------------------------------------------------------------------------------------------------------- --------------------

### Properties and Functions {#properties_and_functions_3}

Here is a list of all client properties and functions. If a function is
marked as readable then it can return a value when used as
`<KEY>`{=html}. Click on the name for more detailed information such as
usage and examples.

  --------------------------------------------------------------------------------- ---------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------
  **Name**                                                                          **Read/Write**   **Description**                                                                                                                                                                                                                                                                                                                                                  **Sphere X only?**
  [ADD](ADD "wikilink") *item_defname*                                              W                Prompts the client to target a location to add the specified item at.                                                                                                                                                                                                                                                                                            
  [ADDBUFF](ADDBUFF "wikilink") *icon, cliloc1, cliloc2, time, arg1, arg2, arg3*    W                Displays a buff icon in the client\'s buff icon bar.                                                                                                                                                                                                                                                                                                             
  [ADDCLILOC](ADDCLILOC "wikilink") *cliloc, args*                                  W                Adds a cliloc to the tooltip being sent to the client. Only valid in \@ClientTooltip triggers.                                                                                                                                                                                                                                                                   
  [ADDCONTEXTENTRY](ADDCONTEXTENTRY "wikilink") *entry_id, cliloc, flags, colour*   W                Adds an entry to the context menu being sent to the client. Only valid in \@ContextMenuRequest triggers.                                                                                                                                                                                                                                                         
  [ALLMOVE](ALLMOVE "wikilink")                                                     RW               Gets or sets whether or not the client has ALLMOVE privileges.                                                                                                                                                                                                                                                                                                   
  [ALLSHOW](ALLSHOW "wikilink")                                                     RW               Gets or sets whether or not the client is able to see disconnected characters.                                                                                                                                                                                                                                                                                   
  [ARROWQUEST](ARROWQUEST "wikilink") *x, y, id*                                    W                Displays an arrow on the client\'s screen that points to the specified world coordinates. If id is supplied multiple arrows can be displayed on the client at once (Newer clients only - 3.x+ clients confirm?). You can cancel the arrow by passing 0 for x and y and your id. Using ARROWQUEST without any arguments will cancel arrow with id 0 if present.   
  [BADSPAWN](BADSPAWN "wikilink")                                                   W                Teleports the client to the first invalid spawn point in the world.                                                                                                                                                                                                                                                                                              
  [BANKSELF](BANKSELF "wikilink")                                                   W                Opens up the client\'s bankbox.                                                                                                                                                                                                                                                                                                                                  
  [CAST](CAST "wikilink") \'\'spell_id\'                                            W                Begins casting a spell.                                                                                                                                                                                                                                                                                                                                          
  [CHARLIST](CHARLIST "wikilink")                                                   W                Displays the client\'s character list screen.                                                                                                                                                                                                                                                                                                                    
  [CLEARCTAGS](CLEARCTAGS "wikilink")                                               W                Removes all of the client\'s CTAGs.                                                                                                                                                                                                                                                                                                                              
  [CLIENTIS3D](CLIENTIS3D "wikilink")                                               R                Returns 1 if the client is using the 3D client.                                                                                                                                                                                                                                                                                                                  
  [CLIENTISKR](CLIENTISKR "wikilink")                                               R                Returns 1 if the client is using the KR client.                                                                                                                                                                                                                                                                                                                  
  [CLIENTVERSION](CLIENTVERSION "wikilink")                                         R                Gets the client version the client is using, based on the encryption keys being used (unencrypted clients return 0).                                                                                                                                                                                                                                             
  [CTAG](CTAG "wikilink")                                                           RW               Gets or sets the value of a CTAG.                                                                                                                                                                                                                                                                                                                                
  [CTAGCOUNT](CTAGCOUNT "wikilink")                                                 R                Gets the number of CTAGs stored on the client.                                                                                                                                                                                                                                                                                                                   
  [CTAGLIST](CTAGLIST "wikilink")                                                   W                Displays a list of the client\'s CTAGs to SRC.                                                                                                                                                                                                                                                                                                                   
  [CTAGLIST](CTAGLIST "wikilink") LOG                                               W                Displays a list of the client\'s CTAGs on the server console.                                                                                                                                                                                                                                                                                                    
  [DEBUG](DEBUG "wikilink")                                                         RW               Gets or sets whether or not the client is in debug mode.                                                                                                                                                                                                                                                                                                         
  [DETAIL](DETAIL "wikilink")                                                       RW               Gets or sets whether or not the client receives additional detail, such as combat messages.                                                                                                                                                                                                                                                                      
  [EVERBTARG](EVERBTARG "wikilink") *command*                                       W                Prompts the client to enter a command, or arguments to the command if specified. The complete command with arguments is then executed on TARG.                                                                                                                                                                                                                   
  [EXTRACT](EXTRACT "wikilink") *file, template_id*                                 W                Extracts static items from a targeted area on the map and saves them into the specified file.                                                                                                                                                                                                                                                                    
  [FLUSH](FLUSH "wikilink")                                                         W                Forces queued network data to be immediately sent to the client.                                                                                                                                                                                                                                                                                                 
  [GM](GM "wikilink")                                                               RW               Gets or sets whether or not the client is in GM mode.                                                                                                                                                                                                                                                                                                            
  [GMPAGE](GMPAGE "wikilink") *ADD message*                                         W                Sends a GM page from the client with the specified message, or if no arguments provided will prompt the client for a message.                                                                                                                                                                                                                                    
  [GOTARG](GOTARG "wikilink")                                                       W                Teleports the client to their targeted item.                                                                                                                                                                                                                                                                                                                     
  [HEARALL](HEARALL "wikilink")                                                     RW               Gets or sets whether or not the client can hear all player speech regardless of location.                                                                                                                                                                                                                                                                        
  [INFO](INFO "wikilink")                                                           W                Displays an information dialog to the client for an object they target.                                                                                                                                                                                                                                                                                          
  [INFORMATION](INFORMATION "wikilink")                                             W                Displays server information to the client.                                                                                                                                                                                                                                                                                                                       
  [LAST](LAST "wikilink")                                                           W                Forces the client to target the object referenced by [ACT](ACT "wikilink").                                                                                                                                                                                                                                                                                      
  [LASTEVENT](LASTEVENT "wikilink")                                                 RW               Returns the time when data was last received from the client.                                                                                                                                                                                                                                                                                                    
  [LINK](LINK "wikilink")                                                           W                Allows the client to target two objects to link them together.                                                                                                                                                                                                                                                                                                   
  [MENU](MENU_(Function) "wikilink") *menu_id*                                      W                Displays a menu to the client.                                                                                                                                                                                                                                                                                                                                   
  [MIDILIST](MIDILIST "wikilink") *music1, music2, \...*                            W                Selects a random music id from the given list and tells the client to play it.                                                                                                                                                                                                                                                                                   
  [NUDGE](NUDGE "wikilink") *dx, dy, dz*                                            W                Allows the client to nudge an area of items by the given coordinates, relative to the items\' position.                                                                                                                                                                                                                                                          
  [NUKE](NUKE "wikilink") *command*                                                 W                Allows the client to execute *command* on all items in a targeted area.                                                                                                                                                                                                                                                                                          
  [NUKECHAR](NUKECHAR "wikilink") *command*                                         W                Allows the client to execute *command* on all NPCs in a targeted area.                                                                                                                                                                                                                                                                                           
  [PAGE](PAGE "wikilink")                                                           W                Displays the GM page menu to the client.                                                                                                                                                                                                                                                                                                                         
  [PRIVSHOW](PRIVSHOW "wikilink")                                                   W                Gets or sets whether or not the client\'s privilege level should show in their name.                                                                                                                                                                                                                                                                             
  [REMOVEBUFF](REMOVEBUFF "wikilink") *icon*                                        W                Removes a buff icon from the client\'s buff icon bar.                                                                                                                                                                                                                                                                                                            
  [REPAIR](REPAIR "wikilink")                                                       W                Prompts the client to target an item for them to repair.                                                                                                                                                                                                                                                                                                         
  [REPORTEDCLIVER](REPORTEDCLIVER "wikilink")                                       R                Gets the client version the client is using, based on what it has identified itself as to the server.                                                                                                                                                                                                                                                            
  [REPORTEDCLIVER](REPORTEDCLIVER "wikilink").FULL                                  R                Gets the client version the client is using, based on what it has identified itself as to the server, including the 4th digit.                                                                                                                                                                                                                                   
  [RESEND](RESEND "wikilink")                                                       W                Forces a full refresh of the client\'s screen.                                                                                                                                                                                                                                                                                                                   
  [SAVE](SAVE "wikilink") *immediate*                                               W                Begins a world save. If background saving is enabled then *[SAVE](SAVE "wikilink") 1* will force a foreground save.                                                                                                                                                                                                                                              
  [SCREENSIZE](SCREENSIZE "wikilink")                                               R                Gets the client\'s screen size. (width,height)                                                                                                                                                                                                                                                                                                                   
  [SCREENSIZE](SCREENSIZE "wikilink").X                                             R                Gets the width of the client\'s screen size.                                                                                                                                                                                                                                                                                                                     
  [SCREENSIZE](SCREENSIZE "wikilink").Y                                             R                Gets the height of the client\'s screen size.                                                                                                                                                                                                                                                                                                                    
  [SCROLL](SCROLL "wikilink") *scroll_id*                                           W                Displays a message scroll to the client.                                                                                                                                                                                                                                                                                                                         
  [SELF](SELF "wikilink")                                                           W                Forces the client to target itself.                                                                                                                                                                                                                                                                                                                              
  [SENDPACKET](SENDPACKET "wikilink") *data*                                        W                Sends a raw data packet to the client.                                                                                                                                                                                                                                                                                                                           
  [SET](SET "wikilink") *command*                                                   W                Prompts the client to target an object to execute *command* on.                                                                                                                                                                                                                                                                                                  
  [SHOWSKILLS](SHOWSKILLS "wikilink")                                               W                Refreshes the client\'s skills for the skill menu.                                                                                                                                                                                                                                                                                                               
  [SKILLMENU](SKILLMENU_(Function) "wikilink") *skillmenu_id*                       W                Displays a skillmenu to the client.                                                                                                                                                                                                                                                                                                                              
  [SKILLSELECT](SKILLSELECT "wikilink") *skill_id*                                  W                Simulates the client selecting a skill from their skill menu.                                                                                                                                                                                                                                                                                                    
  [SUMMON](SUMMON "wikilink") *character_id*                                        W                Casts the summon spell, with \'\'character_id\'; being the character to summon.                                                                                                                                                                                                                                                                                  
  [SYSMESSAGE](SYSMESSAGE "wikilink") *text*                                        W                Displays a system message to the client.                                                                                                                                                                                                                                                                                                                         
  [SYSMESSAGELOC](SYSMESSAGELOC "wikilink") *hue, cliloc, args*                     W                Displays a localized system message to the client.                                                                                                                                                                                                                                                                                                               
  [SYSMESSAGELOCEX](SYSMESSAGELOCEX "wikilink") *hue, cliloc, flags, affix, args*   W                Displays a localized system message to the client with affixed text.                                                                                                                                                                                                                                                                                             
  [SYSMESSAGEUA](SYSMESSAGEUA "wikilink") *hue, font, mode, language, text*         W                Displays a UNICODE system message to the client.                                                                                                                                                                                                                                                                                                                 
  [TARGETTEXT](TARGETTEXT "wikilink")                                               RW               Gets or sets the client\'s target text.                                                                                                                                                                                                                                                                                                                          
  [TELE](TELE "wikilink")                                                           W                Casts the teleport spell.                                                                                                                                                                                                                                                                                                                                        
  [TILE](TILE "wikilink") *z, item1, item2, \...*                                   W                Tiles the ground within a targeted area with the listed items, at the given Z level.                                                                                                                                                                                                                                                                             
  [UNEXTRACT](UNEXTRACT "wikilink") *file*                                          W                Unextracts previously extracted statics, as dynamic items at a targeted location.                                                                                                                                                                                                                                                                                
  [VERSION](VERSION "wikilink")                                                     W                Displays the server description to the client.                                                                                                                                                                                                                                                                                                                   
  [WEBLINK](WEBLINK "wikilink") *url*                                               W                Opens the client\'s web browser to send them to the specified url.                                                                                                                                                                                                                                                                                               
  [X](X "wikilink")*command*                                                        W                Prompts the client to target an object to execute *command* on.                                                                                                                                                                                                                                                                                                  
  --------------------------------------------------------------------------------- ---------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Objects](Category:_Objects "wikilink")
