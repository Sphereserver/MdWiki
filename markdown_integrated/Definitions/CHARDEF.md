

A CHARDEF block defines the basic properties of a [character](Characters "wikilink").

## Properties

Here is a list of all character definition properties.

|  |  |  |  |
|----|----|----|----|
| **Name** | **Read/Write** | **Override†** | **Description** |
| [ANIM](ANIM "wikilink") | RW | ?? | Gets or sets a mask of animations that the character supports. The default value is 0ffffff. |
| [ARMOR](ARMOR "wikilink") | RW | ?? | Gets or sets the character's base defense without armour. |
| [AVERSIONS](AVERSIONS "wikilink") | RW | ?? | Gets or sets a list of things that the character does not like. |
| [BASEID](BASEID "wikilink") | R | ?? | Gets the defname of the character if set, otherwise the ID. |
| [BLOODCOLOR](BLOODCOLOR "wikilink") | RW | ?? | Gets or sets the character's blood colour (a value of -1 prevents the creature from bleeding at all.) |
| [CAN](CAN "wikilink") | RW | ?? | Gets or sets attributes for the character. See can_flags in sphere_defs.scp. |
| [COLOR](COLOR "wikilink") | RW | ?? | Gets or sets the character colour. |
| [DAM](DAM "wikilink") *min,max* | RW | ?? | Gets or sets the base damage that the character will deal without a weapon. |
| [DAM](DAM "wikilink").LO | R | ?? | Gets the minimum base damage the character will deal without a weapon. |
| [DAM](DAM "wikilink").HI | R | ?? | Gets the maximum base damage the character will deal without a weapon. |
| [DEFNAME](DEFNAME "wikilink") | RW | ?? | Gets or sets defname of the character. |
| [DESIRES](DESIRES "wikilink") | RW | ?? | Gets or sets a list of things that the character likes. |
| [DEX](DEX "wikilink") | RW | ?? | Gets or sets the dexterity that is set when a character polymorphs into this character. |
| [DISPID](DISPID "wikilink") | R | ?? | Gets the ID that the character displays as. |
| [FOODTYPE](FOODTYPE "wikilink") | RW | ?? | Gets or sets a list of things that the character can eat. |
| [HEIGHT](HEIGHT "wikilink") | RW | ?? | Gets or sets the height of the character. |
| [HIREDAYWAGE](HIREDAYWAGE "wikilink") | RW | ?? | Gets or sets how much gold is needed to hire the character for one day. |
| [ICON](ICON "wikilink") | RW | ?? | Gets or sets the item that can be used to represent the character in figurine form. |
| [ID](ID "wikilink") | RW | ?? | Gets or sets the ID of the character to inherit property values from. |
| [INSTANCES](INSTANCES "wikilink") | R | ?? | Returns the number of this character that exist in the world. |
| [INT](INT "wikilink") | RW | ?? | Gets or sets the intelligence that is set when a character polymorphs into this character. |
| [JOB](JOB "wikilink") | R | ?? | Gets the character's job title. |
| [MAXFOOD](MAXFOOD "wikilink") | R | ?? | Gets the maximum food level that the character can have. |
| [MOVERATE](MOVERATE "wikilink") | RW | Y | Boost or limit the movement speed (based on DEX) with the specified rate. The higher it is, the faster the NPC will be. 50 means 50% of speed, 200 means double speed. |
| [NAME](NAME "wikilink") | RW | ?? | Gets or sets the name of the character. |
| [RANGE](RANGE "wikilink") *min, max* | RW | Y | Gets or sets the attack range of the character. |
| [RANGEH](RANGEH "wikilink") | R | ?? | Gets the maximum attack range of the character. |
| [RANGEL](RANGEL "wikilink") | R | ?? | Gets the minimum attack range of the character. |
| [RESDISPDNHUE](RESDISPDNHUE "wikilink") | RW | ?? | Gets or sets the colour to display as to clients who don't have a high enough [RESDISP](RESDISP "wikilink") to see the character. |
| [RESDISPNID](RESDISPNID "wikilink") | RW | ?? | Gets or sets the character ID to display as to clients who don't have a high enough [RESDISP](RESDISP "wikilink") to see the character. |
| [RESLEVEL](RESLEVEL "wikilink") | RW | ?? | Gets or sets the minimum [RESDISP](RESDISP "wikilink") required for a client to see the character. |
| [RESOURCES](RESOURCES "wikilink") | RW | ?? | Gets or sets the resources that the character is made of. |
| [RESOURCES](RESOURCES "wikilink")*.COUNT* | R | ?? | Gets the number of different resources that the character is made of. |
| [RESOURCES](RESOURCES "wikilink")*.n.KEY* | R | ?? | Gets the [BASEID](BASEID "wikilink") of the nth resource that the character is made of. (zero-based) |
| [RESOURCES](RESOURCES "wikilink")*.n.VAL* | R | ?? | Gets the amount of the nth resource that the character is made of. (zero-based) |
| [SOUND](SOUND "wikilink") | RW | ?? | Gets or sets the generic sound that the character makes. can be splitted into SOUNDHIT, SOUNDGETHIT, SOUNDDIE, SOUNDIDLE, SOUNDNOTICE, splitted values are optional, and when set it will have priority over default SOUND value. |
| [SOUNDIDLE](SOUNDIDLE "wikilink") | RW | ?? | Gets or sets the iddle sound that the character makes. (can have -1 as value to prevent action-related sound to be played) |
| [SOUNDNOTICE](SOUNDNOTICE "wikilink") | RW | ?? | Gets or sets the notice sound that the character makes. (can have -1 as value to prevent action-related sound to be played) |
| [SOUNDHIT](SOUNDHIT "wikilink") | RW | ?? | Gets or sets the hit sound that the character makes. (can have -1 as value to prevent action-related sound to be played) |
| [SOUNDGETHIT](SOUNDGETHIT "wikilink") | RW | ?? | Gets or sets the get hit sound that the character makes. (can have -1 as value to prevent action-related sound to be played) |
| [SOUNDDIE](SOUNDDIE "wikilink") | RW | ?? | Gets or sets the die sound that the character makes. (can have -1 as value to prevent action-related sound to be played) |
| [STR](STR "wikilink") | RW | ?? | Gets or sets the strength that is set when a character polymorphs into this character. |
| [TAG](TAG "wikilink")*.name* | RW | ?? | Gets or sets the value of a TAG. |
| [TAG.BARDING.DIFF (X branch only)](TAG.BARDING.DIFF_(X_branch_only) "wikilink") | RW | ?? | determine the difficulty of Enticement, Peacemaking and Provocation skills. If this tag isn't set, the old behaviour is used. |
| [THROWDAM](THROWDAM "wikilink") *min,max* | RW | y | Gets or sets a range of damage used for thrown objects. |
| [THROWDAM](THROWDAM "wikilink") *dam* | RW | y | Gets or sets the constant damage used for thrown objects. |
| [THROWDAMTYPE](THROWDAMTYPE "wikilink") *damage flags* | RW | y | Gets or sets the damage flags used for thrown objects. |
| [THROWOBJ](THROWOBJ "wikilink") *id* | RW | y | Gets or sets the ID of an object to be thrown by NPCs. |
| [THROWRANGE](THROWRANGE "wikilink") *min,max* | RW | y | Gets or sets the range that an object can be thrown at. |
| [THROWRANGE](THROWRANGE "wikilink") *max* | RW | y | Gets or sets the range that an object can be thrown at with a default min of 2. |
| [TSPEECH](TSPEECH "wikilink") *speech_defname* | RW | ?? | Gets a list of speech handlers for the character, or adds a speech handler to the character. |
| [TEVENTS](TEVENTS "wikilink") *event_defname* | RW | ?? | Gets a list of event handlers for the character, or adds an event handler to the character. |

**†** Some properties can be overridden on a individual character basis.
```
For example, you can set TAG.OVERRIDE.MOVERATE on a specific NPC to speed up or slow down the speed at which that one NPC will move.

```
## INI Overrides
```

```
| **Name** | **Description** |
|----|----|
| TAG.OVERRIDE.RUNNINGPENALTY | This special tag overrides the INI setting of the same name on a per character basis. |
| TAG.OVERRIDE.STAMINALOSSATWEIGHT | This special tag overrides the INI setting of the same name on a per character basis. |
```

```
## Others
```

```
| **Name**       | **Description**                                           |
|----------------|-----------------------------------------------------------|
| TAG.NoMoveTill | doesn't allow char to move if TAG.NoMoveTill \> SERV.Time |
|                |                                                           |
```

```
## Examples
```

This first example shows a "base" CHARDEF... these are identified by the fact that the CHARDEF keyword is followed by a number:

\[CHARDEF 01\] // This is a "base" chardef for character animation 01 (from the mul/uop files) // This is the start of the "base" properties. // Values set in the base properties cannot have a range (you cannot use {1 10}) DEFNAME=c_ogre // The DEFNAME is a friendly name to reference this CHARDEF NAME=ogre // This is the creature's name as seen in-game ICON=i_pet_ogre // If the creature is shrunk, this is the item that will result SOUND=snd_monster_ogre1 // This is the start of the sound entries for this creature CAN=MT_WALK\|MT_USEHANDS\|MT_EQUIP // These flags are defined in the can_flags area of sphere_defs.scp DAM=18,22 // This is the range of damage they creature will cause when not using a weapon ARMOR=30 // ARMOR is the physical damage resistance \*before\* additional armor is equipped DESIRES=r_forests,t_gold,t_coin,t_gem,t_arock AVERSIONS=t_trap,r_civilization FOODTYPE=35 t_meat_raw // This is the maximum amount (and types) of food the creature eats RESOURCES=2 i_ribs_raw // If this creature's corpse is carved, these resources will be created BLOODCOLOR=colors_blood // This is the color of this creatures blood MOVERATE=100 TAG.Barding.Diff=48.8 // When a TAG is added to the "base properties", all existing creatures are affected TAG.SlayerGroup=OGRE,REPOND TEVENTS=e_carnivores2 // EVENTS are collections of triggers used by CHARDEFs. Each TEVENT must be on its own line. CATEGORY=Monsters // CATEGORY, SUBSECTION, and DESCRIPTION are used by the GM tool "Axis" SUBSECTION=Giants DESCRIPTION=Ogre

// This is the end of the "base" properties, and the start of the "triggers". // You can override \*most\* base properties in a trigger if necessary.

ON=@Create // This is the @Create trigger

`  NAME=#NAMES_OGRE               // #NAMES_OGRE is an array of names defined in sphere_names.scp`
`  TITLE=the ogre`
`  NPC=brain_monster              // The available "brains" are defined in sphere_defs.scp`
`  FAME={1500 1999}               // The { } marks are used to set a range of possible values`
`  KARMA={-1500 -1999}`
`  STR={165 195}`
`  MAXHITS={100 120}              // If MAXHITS is not set, the default value is the same as STR`
`  DEX={45 65}`
`  MAXSTAM={45 65}                // If MAXSTAM is not set, the default value is the same as DEX`
`  INT={45 70}`
`  MAXMANA={45 70}                // If MAXMANA is not set, the default value is the same as INT`
`  MAGICRESISTANCE={55.0 70.0}`
`  PARRYING={60.0 70.0}`
`  TACTICS={60.0 70.0}`
`  WRESTLING={70.0 80.0}`
`  MODAR={0 5}                    // Setting MODAR in @Create lets us add o-5 more ARMOR to this creature`
`  RESCOLD={15 25}`
`  RESENERGY={15 25}`
`  RESFIRE={15 25}`
`  RESPOISON={15 25}`

ON=@NPCRestock

`  ITEM=loot_ogre                 // This references a TEMPLATE in the sphere_templates_loot.scp file`


[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Definitions](Category:_Definitions "wikilink")
```
