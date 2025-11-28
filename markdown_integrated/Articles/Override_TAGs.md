## Override Common Data

Ever wondered why you can't change for example 'TDATA' values on a
per-item basis? Or some default values from Sphere.ini?

The reason is simple: The majority of items, characters and situation
will not need individual values there and are working fine with the
default ones (either hardcoded or set in the INI or the \*DEF sections),
so it simply would be a waste of memory to store them again on each game
object. Therefore for example a single crossbow in the world reads what
items it needs as ammunition not from it's "WORLDITEM" data object, but
from it's ITEMDEF (the TDATA property).

Alas, as time goes by for some stuff it showed reasonable to allow
overriding the default values for a single item, character or even
region. Nevertheless it still would be a waste of resources to give all
crossbows an "ammunition" property what on almost all of them will read:
"default". So the Sphere developers decided to store the respective
individual changes in TAGs: If the TAG exists it will be used, if not,
the default is used.

Common to most overrides is the syntax of the TAG's name:
**TAG.OVERRIDE.\*** - where "**\***" denotes the name of the respective
tag. But there are also some others what were named before this naming
scheme was established.

## Item-based Override TAGs

|  |  |
|----|----|
| **TAG.ALWAYSSEND** | When optional flag OF_OsiMultiSight is on, all items inside a multi are not sent until entering the multi. If you want an item to be always sent, set TAG.ALWYASSEND to 1. This tag also can also go under the ITEMDEF section of an item. |
| **TAG.NOSAVE** | If set to 1 the object will NOT be saved. |
| **TAG.OVERRIDE.DAMAGETYPE** | Sets the damage type for a weapon (ARGN2 in @GetHit trigger). |
| **TAG.OVERRIDE.DROPSOUND** | Overrides the sound that will be played when the item is dropped somewhere. |
| **TAG.OVERRIDE_LIGHTID** | Overrides TDATA3 for lights (T_LIGHT_LIT, T_LIGHT_OUT). Take notice that there is an underscore in this TAG's name. |
| **TAG.OVERRIDE.MAXITEMS** | Overrides the maximum number of items that can be placed into a container (default: 255) |
| **ModMaxWeight** | Overrides the maximum total weight that can be placed into a container. |
| **TAG.OVERRIDE.PRACTICEMAX.SKILL\_\$skillid** | Overrides SKILLPRACTICEMAX setting from Sphere.ini for a particular skill. \$skillid is the numeric ID of the skill. |
| **TAG.OVERRIDE.SKILL** | Overrides the SKILL property of the ITEMDEF for a weapon. |
| **TAG.OVERRIDE.SPEED** | Overrides the SPEED for a weapon. |
| **TAG.OVERRIDE.SOUND_HIT** | Overrides the hit sound for a weapon. Take notice that there is an underscore in this TAG's name. (Removed in newer versions and is just AMMOSOUNDHIT=<Val> without the use of Tag.Override.<String>=<Val>) |
| **TAG.OVERRIDE.SOUND_MISS** | Overrides the miss sound for a weapon. Take notice that there is an underscore in this TAG's name. (Removed in newer versions and is just AMMOSOUNDMISS=<Val> without the use of Tag.Override.<String>=<Val>) |

## Character-based Override TAGs

|  |  |
|----|----|
| **TAG.DEATHFLAGS** | Changes some death related behaviour. The list of supported flags are in sphere_defs.scp. |
| **TAG.MAXPLAYERPETS** | Overrides the maximum number of pets that a player can stable. Default is 10. |
| **TAG.NAME.ALT** | Sets an alternative name, useful for incognito effects. |
| **TAG.NAME.HUE** | Changes the colour of the name displayed above a character. |
| **TAG.NAME.PREFIX** | Sets some text to display before the character's name. |
| **TAG.NAME.SUFFIX** | Sets some text to display after the character's name. |
| **TAG.NOSKILLMSG** | When set to 1, character will receive the "gainradius_not_met" defmessage (sphere_msgs.scp) when skillgain is aborted due to the GAINRADIUS on a skill. |
| **TAG.OVERRIDE.MOVERATE** | Overrides the MOVERATE property of the CHARDEF. |
| **TAG.OVERRIDE.MOVEDELAY** | Overrides completely the moverate checks and setting the next movement to the given timer, eg 'tag.override.moverate=250' makes the npc move each 250 milliseconds when walking. WARNING:\* Setting this tag completelly overrides default moverate checks, TAG.OVERRIDE.MOVERATE gets ignored too. |
| **TAG.OVERRIDE.RUNNINGPENALTY** | Overrides RUNNINGPENALTY from Sphere.ini |
| **TAG.OVERRIDE.SKILLCAP\_\$skillid** | Overrides skill settings from the character's SKILLCLASS. \$skillid is the numeric ID of the skill. |
| **TAG.OVERRIDE.SKILLSUM** | Overrides SKILLSUM setting from the character's SKILLCLASS. |
| '''TAG.OVERRIDE.SPIDERWEB | When set to 1, NPC will be able to drop spider webs (for a giant spider, if this set to 1 then it will stop it from dropping webs) |
| **TAG.OVERRIDE.STAMINALOSSATWEIGHT** | Overrides STAMINALOSSATWEIGHT from Sphere.ini |
| **TAG.OVERRIDE.STATCAP\_\$statid** | Overrides STR/DEX/INT settings from the character's SKILLCLASS. (0=STR, 1=INT, 2=DEX) |
| '''TAG.OVERRIDE.STATSUM | Overrides STATSUM setting from the character's SKILLCLASS. |
| **TAG.OVERRIDE.TRAINSKILLMAX** | Overrides NPCTRAINMAX setting from Sphere.ini |
| **TAG.OVERRIDE.TRAINSKILLMAXPERCENT** | Overrides NPCTRAINPERCENT setting from Sphere.ini |
| **TAG.PARTY_AUTODECLINEINVITE** | When set to 1, character will automatically decline party invitations. |
| **TAG.PARTY_CANLOOTME** | When set to 1, party members will be allow to loot this character without it being counted as a criminal action (linked to the option in the party menu). |
| **TAG.VENDORMARKUP** | This value is added to the markup percentage that vendors apply to their buy and sell prices. Since the default markup is 15%, this means that a vendor will sell something worth 100gp at 115gp and buy it back for 85gp. If you set this tag to -15 the markup will be cancelled out to 0%, or you can raise/lower it if you want your vendor to sell things at a higher/lower price. |

## Region-based Override TAGs

|  |  |
|----|----|
| **TAG.ANNOUNCEMENT** | Sets a message to be announced to all who enters the region if REGION_FLAG_ANNOUNCE is set. |
| **TAG.GUARDOWNER** | Specifies the owner of the region's guards (ex: "The City") |
| **TAG.OVERRIDE.GUARDS** | Specifies the character that will be summoned when guards are called in the region, overriding the `guards {c_h_guard 1 c_h_guard_f 1}` defname in sphere_defs.scp |
| **TAG.RED** | Sets the region as a safe place for evil. Murders are considered normal here. If region is guarded, guards will be red and protect evil players. |
| **TAG.VENDORMARKUP** | This value is added to the markup percentage that vendors apply to their buy and sell prices. Since the default markup is 15%, this means that a vendor will sell something worth 100gp at 115gp and buy it back for 85gp. If you set this tag to -15 the markup will be cancelled out to 0%, or you can raise/lower it if you want your vendor to sell things at a higher/lower price. If the vendor has this tag set directly on them then this region TAG will not be used. |

## Removed Override TAGs

|  |  |  |
|----|----|----|
| **OLD TAG** | **NEW Variable** | **Description** |
| '''TAG.BREATH.DAM | Breath.Dam | Overrides Damage done from fire breathing. |
| '''TAG.RANGE | Range | Range is now writable for both characters and items. |
| '''TAG.OVERRIDE.SHIPSPEED.PERIOD | ShipSpeed.Period | Overrides SHIPSPEED.PERIOD for a ship (the length of time it takes for the ship to move one step, in tenths of a second). |
| '''TAG.OVERRIDE.SHIPSPEED.TILES | ShipSpeed.Tiles | Overrides the amount of tiles moved in each tick. |
| '''TAG.OVERRIDE.DOORSOUND_CLOSE | DOORCLOSESOUND | Overrides the sound that will be played for a door when it is being closed. |
| '''TAG.OVERRIDE.DOORSOUND_OPEN | DOOROPENSOUND | Overrides the sound that will be played for a door when it is being opened. |
| '''TAG.OVERRIDE.PORTCULISSOUND | PORTCULISSOUND | Overrides the sound that will be played for a portcullis when it is used. |

[Category: Articles](Category:_Articles "wikilink")
