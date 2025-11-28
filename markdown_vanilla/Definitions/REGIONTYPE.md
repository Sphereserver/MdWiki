\_\_FORCETOC\_\_ A REGIONTYPE definition contains a set of trigger
scripts which can be attached to [regions](Regions "wikilink"). A region
type can also define which resources can be found inside the region.
There are different properties that can be used to attach an region type
block to a region or set of regions:

- [Region definitions](AREADEF "wikilink") via their
  [EVENTS](EVENTS "wikilink") or [RESOURCES](RESOURCES "wikilink")
  property.
- [Region objects](Regions "wikilink") via their
  [EVENTS](EVENTS "wikilink") or [RESOURCES](RESOURCES "wikilink")
  property.
- All [regions](Regions "wikilink") via the
  [EVENTSREGION](EVENTSREGION "wikilink") setting in Sphere.ini
  (triggers only).

## Syntax

The syntax for defining an region type for triggers is:

`[REGIONTYPE `*`defname`*`]`  
`ON=`*`trigger_name`*  
`    `*`script`*  
  
`ON=`*`trigger_name`*  
`    `*`script`*  
  

Any number of triggers can be handled by one
[REGIONTYPE](REGIONTYPE "wikilink") definition, however it is not
possible to handle the same trigger twice without using multiple
definitions.

The trigger name can be the name of any [region
trigger](Regions#Triggers "wikilink"). The return value from the script
can affect Sphere's hardcoded behaviour in different ways. See the
documentation for the trigger to discover what parameters are passed in
to each trigger and what the return values do.

A region type can also define which resources can be gathered from a
region. This syntax for this is:

`[REGIONTYPE `*`defname`*` `*`item_type`*`]`  
`RESOURCES=`*`weight`*` `*`resource`*  
`RESOURCES=`*`weight`*` `*`resource`*  
`RESOURCES=`*`weight`*` `*`resource`*  
  

The *item_type* parameter should be the item or terrain
[TYPE](TYPE "wikilink") that the resources can be gathered from.

## Properties

The following properties are available when defining a region type:

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [CALCMEMBERINDEX](CALCMEMBERINDEX "wikilink") | R | Selects a resource from the region type at random, and returns its zero-based index. |
| [CALCMEMBERINDEX](CALCMEMBERINDEX "wikilink") *character_uid* | R | Selects a resource from the region type at random based on the resource available to the specified character, and returns its zero-based index. |
| [DEFNAME](DEFNAME "wikilink") | W | Sets the region type's defname. |
| [RESOURCES](RESOURCES "wikilink") *weight* *resource_defname* | W | Adds a region resource to the region type. Accepts a comma-separated list of resources. |
| [RESOURCES](RESOURCES "wikilink") | R | Gets a list of resources attached to the region type. |
| [RESOURCES](RESOURCES "wikilink").COUNT | R | Gets the number of different resources attached to the region type. |
| [RESOURCES](RESOURCES "wikilink")*.n*.KEY | R | Gets the defname of the *nth* resource attached to the region type. *(1-based)* |
| [RESOURCES](RESOURCES "wikilink")*.n*.VAL | R | Gets the weight of the *nth* resource attached to the region type. *(1-based)* |
| [WEIGHT](WEIGHT "wikilink") | W | Sets the weight of the last resource added to the region type. |

## Examples

<spherescript> // // Default region type from default script pack. //
\[REGIONTYPE r_default\] ON=@Enter

`   SRC.MUSIC = midi_britain1,midi_ForestA,midi_JungleA,midi_MountainA,midi_Plains,midi_Victory`

ON=@CliPeriodic

`   SRC.MUSIC = midi_britain1,midi_ForestA,midi_JungleA,midi_MountainA,midi_Plains,midi_Victory`

</spherescript>

<spherescript> // // Default rock resources from default script pack. //
\[REGIONTYPE r_default_rock t_rock\] // Random rocks RESOURCES=420.0
mr_iron RESOURCES=8.5 mr_copper RESOURCES=8.0 mr_bronze RESOURCES=7.5
mr_stagmite RESOURCES=7.0 mr_arcanium RESOURCES=6.5 mr_gold
RESOURCES=6.0 mr_shadow RESOURCES=5.5 mr_phoenix RESOURCES=5.0
mr_argonite RESOURCES=4.5 mr_bronzealloy RESOURCES=4.0 mr_myriad
RESOURCES=3.5 mr_chromecopper RESOURCES=3.0 mr_nixalite RESOURCES=2.5
mr_crimson RESOURCES=2.0 mr_agapite RESOURCES=1.9 mr_daedric
RESOURCES=1.8 mr_omniate RESOURCES=1.7 mr_alumina RESOURCES=1.6 mr_rose
RESOURCES=1.5 mr_silver RESOURCES=1.4 mr_elven RESOURCES=1.3
mr_bloodrock RESOURCES=1.2 mr_solarite RESOURCES=1.1 mr_cyruss
RESOURCES=1.0 mr_verite RESOURCES=1.0 mr_stone RESOURCES=1.0 mr_lunar
RESOURCES=1.0 mr_ice RESOURCES=0.9 mr_demonic RESOURCES=0.8 mr_mystic
RESOURCES=0.7 mr_aqualis RESOURCES=0.6 mr_Valorite RESOURCES=0.5
mr_kryptonite RESOURCES=0.4 mr_lavan RESOURCES=0.3 mr_ancientsteel
RESOURCES=0.2 mr_sandrock RESOURCES=0.1 mr_mytheril RESOURCES=0.1
mr_vulcan RESOURCES=0.1 mr_titanium RESOURCES=0.1 mr_dragon
RESOURCES=0.1 mr_bloodsteel RESOURCES=0.1 mr_sacratus RESOURCES=0.1
mr_blackrock RESOURCES=0.1 mr_lothlorien RESOURCES=0.1 mr_diamond
</spherescript>

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Definitions](Category:_Definitions "wikilink")
