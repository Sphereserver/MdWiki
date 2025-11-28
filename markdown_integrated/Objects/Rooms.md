\_\_FORCETOC\_\_ Within [regions](Regions "wikilink") you can also
define rooms, which are basically 'sub-regions' that exist inside the
area which may represent buildings within a town or a boss room within a
dungeon. Accessing rooms in scripts can be accomplished using the ROOM
reference from a [character](Characters "wikilink"),
[item](Items "wikilink") or [map point](Map_Points "wikilink") object,
or the ROOM.room_id reference from the [server](Server "wikilink")
object. The following table details the various properties of the room
object in SphereServer:

## Properties and Functions

Here is a list of all room properties and functions. If a function is
marked as readable then it can return a value when used as <KEY>. Click
on the name for more detailed information such as usage and examples.
The properties from the [room definition](ROOMDEF "wikilink") can also
be accessed from the room object. If an attempt is made to execute (not
read) a command that does not exist on the room, then the command will
be called on all sectors that touch the room area.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [ALLCLIENTS](ALLCLIENTS "wikilink") *command* | W | Executes *command* on all clients inside the room boundaries. |
| [CLEARTAGS](CLEARTAGS "wikilink") *prefix* | W | Removes all TAGs from the room that start with the given prefix. |
| [CLIENTS](CLIENTS "wikilink") | R | Gets the total number of clients that are inside the sectors that touch the room. |
| [EVENTS](EVENTS_(Property) "wikilink") *+/-regiontype_defname* | RW | Gets a list of attached room events, or adds or removes a room event to or from the room. |
| [ISEVENT](ISEVENT "wikilink")*.regiontype_defname* | R | Returns 1 if the room has a specified room event attached. |
| [MAP](MAP "wikilink") | R | Gets the map that the room exists on. |
| [RECT](RECT "wikilink") | R | Gets the number of rectangles that this room is made from. |
| [RECT](RECT "wikilink")*.n* | R | Gets the nth rectangle that this room is made from. |
| [TAGAT](TAGAT "wikilink")*.index* | R | Gets a TAG at the given zero-based index. |
| [TAGAT](TAGAT "wikilink")*.index*.KEY | R | Gets the name of the TAG at the given zero-based index. |
| [TAGAT](TAGAT "wikilink")*.index*.VAL | R | Gets the value of the TAG at the given zero-based index. |
| [TAGCOUNT](TAGCOUNT "wikilink") | R | Gets the number of TAGs stored on the room. |
| [TAGLIST](TAGLIST "wikilink") | W | Outputs a list of the room's TAGs. |
| [UID](UID "wikilink") | R | Gets the room's unique ID in the world. |

## Triggers

Here is a list of all room triggers. Click on the trigger name for more
detailed information such as arguments and examples.

|  |  |
|----|----|
| **Name** | **Description** |
| [@Enter](@Enter "wikilink") | Fires when a character enters the room. |
| [@Exit](@Exit "wikilink") | Fires when a character exits the room. |
| [@Step](@Step "wikilink") | Fires whenever a character takes a step within the room. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Objects](Category:_Objects "wikilink")
