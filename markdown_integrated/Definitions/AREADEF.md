\_\_FORCETOC\_\_ Areas in the world, such as dungeons and cities are
defined by regions. Regions are constructed from one or more
"rectangles" on the map.

The basic syntax for definining a region is as follows:

`[AREADEF `*`defname`*`]`  
`RECT=`*`left, top, right, bottom, map`*  
`RECT=`*`left, top, right, bottom, map`*  
`RECT=`*`left, top, right, bottom, map`*  

## Properties

Within the region definition the following properties are also available
to customise the behaviour of the area.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [ANNOUNCE](ANNOUNCE "wikilink") | RW | Gets or sets whether or not there will be an announcement when someone enters or exits the region. |
| [ARENA](ARENA "wikilink") | RW | Gets or sets whether or not the region is considered to be an arena. |
| [BUILDABLE](BUILDABLE "wikilink") | RW | Gets or sets whether or not players can place buildings and ships in the region. |
| [EVENTS](EVENTS_(Property) "wikilink") *regiontype_defname* | W | Adds a region event to the region. |
| [FLAGS](FLAGS "wikilink") | RW | Gets or sets the region's attributes. |
| [GATE](GATE "wikilink") | RW | Gets or sets whether or not casting the gate travel spell is allowed in the region. |
| [GROUP](GROUP "wikilink") | RW | Gets or sets a group name for the region. |
| [GUARDED](GUARDED "wikilink") | RW | Gets or sets whether or not guards can be called within the region. |
| [MAGIC](MAGIC "wikilink") | RW | Gets or sets whether or not there is an anti-magic field in the region. |
| [MARK](MARK "wikilink") | RW | Gets or sets whether or not casting the mark spell is allowed in the region. |
| [NAME](NAME "wikilink") | RW | Gets or sets the name of the region. |
| [NOBUILD](NOBUILD "wikilink") | RW | Gets or sets whether or not players can place buildings in the region. |
| [NODECAY](NODECAY "wikilink") | RW | Gets or sets whether or not items will decay in the region. |
| [NOPVP](NOPVP "wikilink") | RW | Gets or sets whether or not PvP combat is allowed in the region. |
| [P](P "wikilink") | RW | Gets or sets the location of the region (used when using the [GO](GO "wikilink") command). |
| [RECALL](RECALL "wikilink") | RW | Gets or sets whether or not casting the recall spell is allowed in the region. |
| [RECALLIN](RECALLIN "wikilink") | RW | Gets or sets whether or not it is possible to use the recall spell to enter the region. |
| [RECALLOUT](RECALLOUT "wikilink") | RW | Gets or sets whether players can recall out of the region. |
| [RECT](RECT "wikilink") *left, top, right, bottom, map* | W | Adds a rectangle to the region definition. |
| [RESOURCES](RESOURCES "wikilink") *regiontype_defname* | W | Adds a region event to the region. |
| [SAFE](SAFE "wikilink") | RW | Gets or sets whether or not the region is a safe zone. |
| [TAG](TAG "wikilink")*.name* | RW | Gets or sets the value of a TAG. |
| [UNDERGROUND](UNDERGROUND "wikilink") | RW | Gets or sets whether or not the region is considered to be underground. |

## Examples

<spherescript> // // The world region from the default script pack. //
\[AREADEF a_world\]
EVENTS=r_default,r_default_rock,r_default_water,r_default_tree,r_default_grass
NAME=Felucca GROUP=ALLMAP P=1323,1624,55,0 RECT=0,0,7168,4096,0
</spherescript>

<spherescript> // // Lord British's Castle from the default script pack.
// \[AREADEF a_lord_britishs_castle_1\]
EVENTS=r_default,r_default_rock,r_default_water,r_default_tree,r_default_grass
NAME=Lord British's Castle GROUP=Britain FLAGS=0648e P=1392,1625,30,0
RECT=1294,1679,1411,1697,0 RECT=1295,1559,1313,1577,0
RECT=1392,1559,1410,1577,0 RECT=1302,1577,1410,1680,0
RECT=1313,1563,1392,1577,0 EVENTS=r_brit_castle TAG.GUARDOWNER=Lord
British's Personal </spherescript>

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Definitions](Category:_Definitions "wikilink")
