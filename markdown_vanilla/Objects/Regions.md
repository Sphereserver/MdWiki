\_\_FORCETOC\_\_ Areas in the world, such as dungeons and cities are
defined by regions. Accessing regions in scripts can be accomplished
using the REGION reference from a [character](Characters "wikilink"),
[item](Items "wikilink") or [map point](Map_Points "wikilink") object,
or the AREA.region_id reference from the [server](Server "wikilink")
object. The following tables detail the various properties of the region
object in SphereServer:

## References

References return pointers to other objects (e.g. the CHAR.n reference
allows you to access the characters that are attached to the account).
These can either be accessed by using *\<REFNAME\>* to return the
[UID](UID "wikilink") (1 for object types that don't have UIDs) of the
object or 0 if it doesn't exist, or by using *\<REFNAME.KEY\>* where KEY
is a valid property/function/reference for the *REFNAME* object. Click
on the name for more detailed information such as usage and examples.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [REGION](REGION "wikilink") | R | For regions linked to a multi, gets the region that contains the multi region. Only valid for reading values. |

## Properties and Functions

Here is a list of all region properties and functions. If a function is
marked as readable then it can return a value when used as <KEY>. Click
on the name for more detailed information such as usage and examples.
Properties from the [region definition](AREADEF "wikilink") can also be
accessed from the region object. If an attempt is made to execute (not
read) a command that does not exist on the region or its definition,
then the command will be called on all sectors that touch the region
area.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [ALLCLIENTS](ALLCLIENTS "wikilink") *command* | W | Executes *command* on all clients inside the region boundaries. |
| [CLEARTAGS](CLEARTAGS "wikilink") *prefix* | W | Removes all TAGs from the region that start with the given prefix. |
| [CLIENTS](CLIENTS "wikilink") | R | Gets the total number of clients that are inside the sectors that touch the region. |
| [COLDCHANCE](COLDCHANCE "wikilink") | W | Set the ColdChance to all sectors in this Region. |
| [DEFNAME](DEFNAME "wikilink") | R | Gets the region's defname. |
| [EVENTS](EVENTS_(Property) "wikilink") *+/-regiontype_defname* | RW | Gets a list of attached region events, or adds or removes a region event to or from the region. |
| [GUARDED](GUARDED "wikilink") | RW | Set the region to be Guarded or not. |
| [ISEVENT](ISEVENT "wikilink")*.regiontype_defname* | R | Returns 1 if the region has a specified region event attached. |
| [MAGIC](MAGIC "wikilink") | RW | Enables or Disables Region_Antimagic_All flag. |
| [MAP](MAP "wikilink") | R | Gets the map that the region exists on. |
| [MARK](MARK "wikilink") | RW | Same as RecallIn. |
| [NOBUILD](NOBUILD "wikilink") | RW | Enables or disables Building in this area (only affects futures houses). |
| [NOPVP](NOPVP "wikilink") | RW | Enables or disables PvP in this region. |
| [P](P "wikilink") | RW | Gets or Sets the P coordinates for this area. |
| [RECALLIN](RECALLIN "wikilink") | RW | Enables or disables Mark & RecallIn flags. |
| [RECT](RECT "wikilink") | R | Gets the number of rectangles that this region is made from. |
| [RECT](RECT "wikilink")*.n* | R | Gets the nth rectangle that this region is made from. |
| [RAINCHANCE](RAINCHANCE "wikilink") | W | Sets the RainChance for all sectors inside this region. |
| [RESOURCES](RESOURCES "wikilink") *+/-regiontype_defname* | RW | Gets a list of attached region events, or adds or removes a region event to or from the region. |
| [SAFE](SAFE "wikilink") | RW | Get or Set Safe flag for this region. |
| [TAGAT](TAGAT "wikilink")*.index* | R | Gets a TAG at the given zero-based index. |
| [TAGAT](TAGAT "wikilink")*.index*.KEY | R | Gets the name of the TAG at the given zero-based index. |
| [TAGAT](TAGAT "wikilink")*.index*.VAL | R | Gets the value of the TAG at the given zero-based index. |
| [TAGCOUNT](TAGCOUNT "wikilink") | R | Gets the number of TAGs stored on the region. |
| [TAGLIST](TAGLIST "wikilink") | W | Outputs a list of the region's TAGs. |
| [TYPE](TYPE "wikilink") | R | If the region is linked to a multi, returns the multi's [BASEID](BASEID "wikilink") property. |
| [UID](UID "wikilink") | R | Gets the region's unique ID in the world. |
| [UNDERGROUND](UNDERGROUND "wikilink") | RW | Gets or sets Underground flag for this region. |

## Triggers

Here is a list of all region triggers. Click on the trigger name for
more detailed information such as arguments and examples.

|  |  |
|----|----|
| **Name** | **Description** |
| [@CliPeriodic](@CliPeriodic "wikilink") | Fires multiple times approximately every 30 seconds, for each client in the region. |
| [@Enter](@Enter "wikilink") | Fires when a character enters the region. |
| [@Exit](@Exit "wikilink") | Fires when a character exits the region. |
| [@RegPeriodic](@RegPeriodic "wikilink") | Fires once approximately every 30 seconds, as long as there is at least one client in the region. |
| [@ResourceFound](@ResourceFound "wikilink") | Fires after a resource has been selected and the resource bit has been created. |
| [@ResourceGather](@ResourceGather "wikilink") | Fires before finishing the gathering skill. |
| [@ResourceTest](@ResourceTest "wikilink") | Fires once for every resource listed in a REGIONTYPE, to check if the player (SRC) can get it. It is called only if the player meets the SKILLMAKE requirements for the item set in REAP. |
| [@Step](@Step "wikilink") | Fires whenever a character takes a step within the region. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Objects](Category:_Objects "wikilink")
