```{=mediawiki}
{{Languages|CHARDEF}}
```
\_\_FORCETOC\_\_

A CHARDEF block defines the basic properties of a
[character](./Characters.md).

## Properties

Here is a list of all character definition properties.

  --------------------------------------------------------------------------------- ---------------- --------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                                                                          **Read/Write**   **Override†**   **Description**
  [ANIM](./ANIM.md)                                                           RW               ??              Gets or sets a mask of animations that the character supports. The default value is 0ffffff.
  [ARMOR](./ARMOR.md)                                                         RW               ??              Gets or sets the character\'s base defense without armour.
  [AVERSIONS](./AVERSIONS.md)                                                 RW               ??              Gets or sets a list of things that the character does not like.
  [BASEID](./BASEID.md)                                                       R                ??              Gets the defname of the character if set, otherwise the ID.
  [BLOODCOLOR](./BLOODCOLOR.md)                                               RW               ??              Gets or sets the character\'s blood colour (a value of -1 prevents the creature from bleeding at all.)
  [CAN](./CAN.md)                                                             RW               ??              Gets or sets attributes for the character. See can_flags in sphere_defs.scp.
  [COLOR](./COLOR.md)                                                         RW               ??              Gets or sets the character colour.
  [DAM](./DAM.md) *min,max*                                                   RW               ??              Gets or sets the base damage that the character will deal without a weapon.
  [DAM](./DAM.md).LO                                                          R                ??              Gets the minimum base damage the character will deal without a weapon.
  [DAM](./DAM.md).HI                                                          R                ??              Gets the maximum base damage the character will deal without a weapon.
  [DEFNAME](./DEFNAME.md)                                                     RW               ??              Gets or sets defname of the character.
  [DESIRES](./DESIRES.md)                                                     RW               ??              Gets or sets a list of things that the character likes.
  [DEX](./DEX.md)                                                             RW               ??              Gets or sets the dexterity that is set when a character polymorphs into this character.
  [DISPID](./DISPID.md)                                                       R                ??              Gets the ID that the character displays as.
  [FOODTYPE](./FOODTYPE.md)                                                   RW               ??              Gets or sets a list of things that the character can eat.
  [HEIGHT](./HEIGHT.md)                                                       RW               ??              Gets or sets the height of the character.
  [HIREDAYWAGE](./HIREDAYWAGE.md)                                             RW               ??              Gets or sets how much gold is needed to hire the character for one day.
  [ICON](./ICON.md)                                                           RW               ??              Gets or sets the item that can be used to represent the character in figurine form.
  [ID](./ID.md)                                                               RW               ??              Gets or sets the ID of the character to inherit property values from.
  [INSTANCES](./INSTANCES.md)                                                 R                ??              Returns the number of this character that exist in the world.
  [INT](./INT.md)                                                             RW               ??              Gets or sets the intelligence that is set when a character polymorphs into this character.
  [JOB](./JOB.md)                                                             R                ??              Gets the character\'s job title.
  [MAXFOOD](./MAXFOOD.md)                                                     R                ??              Gets the maximum food level that the character can have.
  [MOVERATE](./MOVERATE.md)                                                   RW               Y               Boost or limit the movement speed (based on DEX) with the specified rate. The higher it is, the faster the NPC will be. 50 means 50% of speed, 200 means double speed.
  [NAME](./NAME.md)                                                           RW               ??              Gets or sets the name of the character.
  [RANGE](./RANGE.md) *min, max*                                              RW               Y               Gets or sets the attack range of the character.
  [RANGEH](./RANGEH.md)                                                       R                ??              Gets the maximum attack range of the character.
  [RANGEL](./RANGEL.md)                                                       R                ??              Gets the minimum attack range of the character.
  [RESDISPDNHUE](./RESDISPDNHUE.md)                                           RW               ??              Gets or sets the colour to display as to clients who don\'t have a high enough [RESDISP](./RESDISP.md) to see the character.
  [RESDISPNID](./RESDISPNID.md)                                               RW               ??              Gets or sets the character ID to display as to clients who don\'t have a high enough [RESDISP](./RESDISP.md) to see the character.
  [RESLEVEL](./RESLEVEL.md)                                                   RW               ??              Gets or sets the minimum [RESDISP](./RESDISP.md) required for a client to see the character.
  [RESOURCES](./RESOURCES.md)                                                 RW               ??              Gets or sets the resources that the character is made of.
  [RESOURCES](./RESOURCES.md)*.COUNT*                                         R                ??              Gets the number of different resources that the character is made of.
  [RESOURCES](./RESOURCES.md)*.n.KEY*                                         R                ??              Gets the [BASEID](./BASEID.md) of the nth resource that the character is made of. (zero-based)
  [RESOURCES](./RESOURCES.md)*.n.VAL*                                         R                ??              Gets the amount of the nth resource that the character is made of. (zero-based)
  [SOUND](./SOUND.md)                                                         RW               ??              Gets or sets the generic sound that the character makes. can be splitted into SOUNDHIT, SOUNDGETHIT, SOUNDDIE, SOUNDIDLE, SOUNDNOTICE, splitted values are optional, and when set it will have priority over default SOUND value.
  [SOUNDIDLE](./SOUNDIDLE.md)                                                 RW               ??              Gets or sets the iddle sound that the character makes. (can have -1 as value to prevent action-related sound to be played)
  [SOUNDNOTICE](./SOUNDNOTICE.md)                                             RW               ??              Gets or sets the notice sound that the character makes. (can have -1 as value to prevent action-related sound to be played)
  [SOUNDHIT](./SOUNDHIT.md)                                                   RW               ??              Gets or sets the hit sound that the character makes. (can have -1 as value to prevent action-related sound to be played)
  [SOUNDGETHIT](./SOUNDGETHIT.md)                                             RW               ??              Gets or sets the get hit sound that the character makes. (can have -1 as value to prevent action-related sound to be played)
  [SOUNDDIE](./SOUNDDIE.md)                                                   RW               ??              Gets or sets the die sound that the character makes. (can have -1 as value to prevent action-related sound to be played)
  [STR](./STR.md)                                                             RW               ??              Gets or sets the strength that is set when a character polymorphs into this character.
  [TAG](./TAG.md)*.name*                                                      RW               ??              Gets or sets the value of a TAG.
  [TAG.BARDING.DIFF (X branch only)](TAG.BARDING.DIFF_(X_branch_only) "wikilink")   RW               ??              determine the difficulty of Enticement, Peacemaking and Provocation skills. If this tag isn\'t set, the old behaviour is used.
  [THROWDAM](./THROWDAM.md) *min,max*                                         RW               y               Gets or sets a range of damage used for thrown objects.
  [THROWDAM](./THROWDAM.md) *dam*                                             RW               y               Gets or sets the constant damage used for thrown objects.
  [THROWDAMTYPE](./THROWDAMTYPE.md) *damage flags*                            RW               y               Gets or sets the damage flags used for thrown objects.
  [THROWOBJ](./THROWOBJ.md) *id*                                              RW               y               Gets or sets the ID of an object to be thrown by NPCs.
  [THROWRANGE](./THROWRANGE.md) *min,max*                                     RW               y               Gets or sets the range that an object can be thrown at.
  [THROWRANGE](./THROWRANGE.md) *max*                                         RW               y               Gets or sets the range that an object can be thrown at with a default min of 2.
  [TSPEECH](./TSPEECH.md) *speech_defname*                                    RW               ??              Gets a list of speech handlers for the character, or adds a speech handler to the character.
  [TEVENTS](./TEVENTS.md) *event_defname*                                     RW               ??              Gets a list of event handlers for the character, or adds an event handler to the character.
  --------------------------------------------------------------------------------- ---------------- --------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**†** Some properties can be overridden on a individual character basis.
For example, you can set TAG.OVERRIDE.MOVERATE on a specific NPC to
speed up or slow down the speed at which that one NPC will move.

## INI Overrides {#ini_overrides}

  **Name**                           **Description**
  ---------------------------------- ---------------------------------------------------------------------------------------
  TAG.OVERRIDE.RUNNINGPENALTY        This special tag overrides the INI setting of the same name on a per character basis.
  TAG.OVERRIDE.STAMINALOSSATWEIGHT   This special tag overrides the INI setting of the same name on a per character basis.

## Others

  **Name**         **Description**
  ---------------- ------------------------------------------------------------
  TAG.NoMoveTill   doesn\'t allow char to move if TAG.NoMoveTill \> SERV.Time
                   

## Examples

This first example shows a \"base\" CHARDEF\... these are identified by
the fact that the CHARDEF keyword is followed by a number:

`<spherescript>`{=html}\[CHARDEF 01\] // This is a \"base\" chardef for
character animation 01 (from the mul/uop files) // This is the start of
the \"base\" properties. // Values set in the base properties cannot
have a range (you cannot use {1 10}) DEFNAME=c_ogre // The DEFNAME is a
friendly name to reference this CHARDEF NAME=ogre // This is the
creature\'s name as seen in-game ICON=i_pet_ogre // If the creature is
shrunk, this is the item that will result SOUND=snd_monster_ogre1 //
This is the start of the sound entries for this creature
CAN=MT_WALK\|MT_USEHANDS\|MT_EQUIP // These flags are defined in the
can_flags area of sphere_defs.scp DAM=18,22 // This is the range of
damage they creature will cause when not using a weapon ARMOR=30 //
ARMOR is the physical damage resistance \*before\* additional armor is
equipped DESIRES=r_forests,t_gold,t_coin,t_gem,t_arock
AVERSIONS=t_trap,r_civilization FOODTYPE=35 t_meat_raw // This is the
maximum amount (and types) of food the creature eats RESOURCES=2
i_ribs_raw // If this creature\'s corpse is carved, these resources will
be created BLOODCOLOR=colors_blood // This is the color of this
creatures blood MOVERATE=100 TAG.Barding.Diff=48.8 // When a TAG is
added to the \"base properties\", all existing creatures are affected
TAG.SlayerGroup=OGRE,REPOND TEVENTS=e_carnivores2 // EVENTS are
collections of triggers used by CHARDEFs. Each TEVENT must be on its own
line. CATEGORY=Monsters // CATEGORY, SUBSECTION, and DESCRIPTION are
used by the GM tool \"Axis\" SUBSECTION=Giants DESCRIPTION=Ogre

// This is the end of the \"base\" properties, and the start of the
\"triggers\". // You can override \*most\* base properties in a trigger
if necessary.

ON=@Create // This is the \@Create trigger

`  NAME=#NAMES_OGRE               // #NAMES_OGRE is an array of names defined in sphere_names.scp`\
`  TITLE=the ogre`\
`  NPC=brain_monster              // The available "brains" are defined in sphere_defs.scp`\
`  FAME={1500 1999}               // The { } marks are used to set a range of possible values`\
`  KARMA={-1500 -1999}`\
`  STR={165 195}`\
`  MAXHITS={100 120}              // If MAXHITS is not set, the default value is the same as STR`\
`  DEX={45 65}`\
`  MAXSTAM={45 65}                // If MAXSTAM is not set, the default value is the same as DEX`\
`  INT={45 70}`\
`  MAXMANA={45 70}                // If MAXMANA is not set, the default value is the same as INT`\
`  MAGICRESISTANCE={55.0 70.0}`\
`  PARRYING={60.0 70.0}`\
`  TACTICS={60.0 70.0}`\
`  WRESTLING={70.0 80.0}`\
`  MODAR={0 5}                    // Setting MODAR in @Create lets us add o-5 more ARMOR to this creature`\
`  RESCOLD={15 25}`\
`  RESENERGY={15 25}`\
`  RESFIRE={15 25}`\
`  RESPOISON={15 25}`

ON=@NPCRestock

`  ITEM=loot_ogre                 // This references a TEMPLATE in the sphere_templates_loot.scp file`

`</spherescript>`{=html}

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Definitions](./_Definitions.md)
