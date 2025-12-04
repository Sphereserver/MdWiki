 Within [regions](Regions "wikilink") you can also define rooms, which are basically 'sub-regions' that exist inside the area which may represent buildings within a town or a boss room within a dungeon. Rooms are almost identical to region.

**Sphere 56b**

`ROOMDEF  cannot possess events, triggers or tags.`

**Since Sphere56c (20 July 2013)**

`ROOMDEF can have events, triggers and tags.`

The syntax for defining a room is as follows:

`[ROOMDEF `*`defname`*`]`
`RECT=`*`left, top, right, bottom, map`*
`RECT=`*`left, top, right, bottom, map`*
`RECT=`*`left, top, right, bottom, map`*

## Properties

Within the room definition the following properties are also available to customise the behaviour of the area.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [ANNOUNCE](ANNOUNCE "wikilink") | RW | Gets or sets whether or not there will be an announcement when someone enters or exits the room. |
| [ARENA](ARENA "wikilink") | RW | Gets or sets whether or not the room is considered to be an arena. |
| [BUILDABLE](BUILDABLE "wikilink") | RW | Gets or sets whether or not players can place buildings and ships in the room. |
| [EVENTS](EVENTS_(Property) "wikilink") *regiontype_defname* | W | Adds a region event to the region. |
| [FLAGS](FLAGS "wikilink") | RW | Gets or sets the room's attributes. |
| [GATE](GATE "wikilink") | RW | Gets or sets whether or not casting the gate travel spell is allowed in the room. |
| [GROUP](GROUP "wikilink") | RW | Gets or sets a group name for the room. |
| [GUARDED](GUARDED "wikilink") | RW | Gets or sets whether or not guards can be called within the room. |
| [MAGIC](MAGIC "wikilink") | RW | Gets or sets whether or not there is an anti-magic field in the room. |
| [MARK](MARK "wikilink") | RW | Gets or sets whether or not casting the mark spell is allowed in the room. |
| [NAME](NAME "wikilink") | RW | Gets or sets the name of the room. |
| [NOBUILD](NOBUILD "wikilink") | RW | Gets or sets whether or not players can place buildings in the room. |
| [NODECAY](NODECAY "wikilink") | RW | Gets or sets whether or not items will decay in the room. |
| [NOPVP](NOPVP "wikilink") | RW | Gets or sets whether or not PvP combat is allowed in the room. |
| [P](P "wikilink") | RW | Gets or sets the location of the room (used when using the [GO](GO "wikilink") command). |
| [RECALL](RECALL "wikilink") | RW | Gets or sets whether or not casting the recall spell is allowed in the room. |
| [RECALLIN](RECALLIN "wikilink") | RW | Gets or sets whether or not it is possible to use the recall spell to enter the room. |
| [RECALLOUT](RECALLOUT "wikilink") | RW | Gets or sets whether players can recall out of the room. |
| [SAFE](SAFE "wikilink") | RW | Gets or sets whether or not the room is a safe zone. |
| [TAG](TAG "wikilink")*.name* | RW | Gets or sets the value of a TAG. |
| [UNDERGROUND](UNDERGROUND "wikilink") | RW | Gets or sets whether or not the room is considered to be underground. |

## Triggers

Within the room definition the following properties are also available to customise the behaviour of the area.

|  |  |
|----|----|
| **Trigger** | **Description** |
| [@Enter](@Enter "wikilink") | Fires when a room is entered (56c) |
| [@Exit](@Exit "wikilink") | Fires when a room is exited (56c) |
| [@Step](@Step "wikilink") | Fires when a step is taken inside a room (56c) |

## Examples

```
 // // A House in Minoc, from the default script pack. //
```
\[ROOMDEF a_house_1\] NAME=House GROUP=Minoc FLAGS=04000 P=2484,472,0,0
```
RECT=2479,463,2489,481,0 RECT=2489,471,2497,481,0
```

```
 // // A Secret Cave, from the default script pack. //
```
\[ROOMDEF a_secret_cave_1\] NAME=Secret Cave GROUP=Hidden Valley
```
P=1653,2967,0,0 RECT=1648,2957,1658,2977,0
```

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Definitions](Category:_Definitions "wikilink")
