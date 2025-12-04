 A map point is a specific location on a world map, defined by X, Y, Z and M coordinates. Map point references, such as *P* from the [character](Characters "wikilink")/[item](Items "wikilink") object and *MAP(x,y,map)* from the [server](Server "wikilink") object can be used to access additional information about a map point such as what static items exist at the location. The following tables detail the various properties of map points in SphereServer:

## References

References return pointers to other objects (e.g. the REGION referenceallows you to access the region that contains the map point). These can either be accessed by using *\<REFNAME\>* to return the [UID](UID "wikilink") (1 for object types that don't have UIDs) of the object or 0 if it doesn't exist, or by using *\<REFNAME.KEY\>* where KEY is a valid property/function/reference for the *REFNAME* object. Click on the name for more detailed information such as usage and examples.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [REGION](REGION "wikilink") | R | Gets the [region](Regions "wikilink") that contains the map point. |
| [ROOM](ROOM "wikilink") | R | Gets the [room](Rooms "wikilink") that contains the map point. |
| [SECTOR](SECTOR "wikilink") | R | Gets the [sector](Sectors "wikilink") that contains the map point. |

## Properties and Functions

Here is a list of all map point properties and functions. If a function is marked as readable then it can return a value when used as <KEY>. Click on the name for more detailed information such as usage and examples.

| **Name** | **Read/Write** | **Description** |
| --- | --- | --- |
| [COMPONENTS](COMPONENTS) | R | Gets the number of components of the [MULTI](MULTI) at the location. |
| [COMPONENTS](COMPONENTS)*.n.ID* | R | Gets the ID of the nth component at the location. (zero-based) |
| [COMPONENTS](COMPONENTS)*.n.MULTI* | R | Gets the UID of the MULTI item. |
| [COMPONENTS](COMPONENTS)*.n.Z* | R | Gets the Z level of the nth component at the location. (zero-based) |
| [COMPONENTS](COMPONENTS)*.n.KEY* | R | Gets the *KEY* property from the [ITEMDEF](ITEMDEF) of the nth component at the location. (zero-based) |
| [ISNEARTYPE](ISNEARTYPE) *type, distance, check_multis* | R | Returns 1 if an item exists within *distance* tiles of the location whose [TYPE](TYPE) matches a specified type. |
| [M](M) [MAP](MAP) | R | Gets the location's map number. |
| [STATICS](STATICS) | R | Gets the number of static items at the location. |
| [STATICS](STATICS)*.n.ID* | R | Gets the ID of the nth item at the location. (zero-based) |
| [STATICS](STATICS)*.n.COLOR* | R | Gets the hue of the nth item at the location. (zero-based) |
| [STATICS](STATICS)*.n.Z* | R | Gets the Z level of the nth item at the location. (zero-based) |
| [STATICS](STATICS)*.n.KEY* | R | Gets the *KEY* property from the [ITEMDEF](ITEMDEF) of the nth item at the location. (zero-based) |
| [TERRAIN](TERRAIN) | R | Gets the terrain's ID at the location. |
| [TERRAIN](TERRAIN).Z | R | Gets the terrain's Z level at the location. |
| [TYPE](TYPE) | R | Gets the terrain's TYPE at the location. |
| [X](X) | R | Gets the X coordinate of the location. |
| [Y](Y) | R | Gets the Y coordinate of the location. |
| [Z](Z) | R | Gets the Z coordinate of the location. |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Objects](Category:_Objects "wikilink")
