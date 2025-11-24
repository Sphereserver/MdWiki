```{=mediawiki}
{{Languages|Map_Points}}
```
\_\_FORCETOC\_\_ A map point is a specific location on a world map,
defined by X, Y, Z and M coordinates. Map point references, such as *P*
from the [character](./Characters.md)/[item](./Items.md)
object and *MAP(x,y,map)* from the [server](./Server.md) object
can be used to access additional information about a map point such as
what static items exist at the location. The following tables detail the
various properties of map points in SphereServer:

## References

References return pointers to other objects (e.g. the REGION reference
allows you to access the region that contains the map point). These can
either be accessed by using *\<REFNAME\>* to return the
[UID](./UID.md) (1 for object types that don\'t have UIDs) of the
object or 0 if it doesn\'t exist, or by using *\<REFNAME.KEY\>* where
KEY is a valid property/function/reference for the *REFNAME* object.
Click on the name for more detailed information such as usage and
examples.

  ----------------------------- ---------------- --------------------------------------------------------------------
  **Name**                      **Read/Write**   **Description**
  [REGION](./REGION.md)   R                Gets the [region](./Regions.md) that contains the map point.
  [ROOM](./ROOM.md)       R                Gets the [room](./Rooms.md) that contains the map point.
  [SECTOR](./SECTOR.md)   R                Gets the [sector](./Sectors.md) that contains the map point.
  ----------------------------- ---------------- --------------------------------------------------------------------

## Properties and Functions {#properties_and_functions}

Here is a list of all map point properties and functions. If a function
is marked as readable then it can return a value when used as
`<KEY>`{=html}. Click on the name for more detailed information such as
usage and examples.

+-------------------------+----------------+-------------------------+
| **Name**                | **Read/Write** | **Description**         |
+-------------------------+----------------+-------------------------+
| [COMPONENTS]            | R              | Gets the number of      |
| (COMPONENTS "wikilink") |                | components of the       |
|                         |                | [M                      |
|                         |                | ULTI](./MULTI.md) |
|                         |                | at the location.        |
+-------------------------+----------------+-------------------------+
| [COMPONENTS](./COMPON______R_______________Gets_the_ID_of_the_nth__
_ENTS.md)*.n.ID* |                | component at the        |
|                         |                | location. (zero-based)  |
+-------------------------+----------------+-------------------------+
| [COMPONENTS](./COMPONENT___R_______________Gets_the_UID_of_the_____
_S.md)*.n.MULTI* |                | MULTI item.             |
+-------------------------+----------------+-------------------------+
| [COMPONENTS](./COMPO_______R_______________Gets_the_Z_level_of_the_
_NENTS.md)*.n.Z* |                | nth component at the    |
|                         |                | location. (zero-based)  |
+-------------------------+----------------+-------------------------+
| [COMPONENTS](./COMPONE_____R_______________Gets_the_KEY_property_
_NTS.md)*.n.KEY* |                | from the                |
|                         |                | [ITEMD                  |
|                         |                | EF](./ITEMDEF.md) |
|                         |                | of the nth component at |
|                         |                | the location.           |
|                         |                | (zero-based)            |
+-------------------------+----------------+-------------------------+
| [ISNEARTYPE]            | R              | Returns 1 if an item    |
| (ISNEARTYPE "wikilink") |                | exists within           |
| *type, distance,        |                | *distance* tiles of the |
| check_multis*           |                | location whose          |
|                         |                | [TYPE](./TYPE.md) |
|                         |                | matches a specified     |
|                         |                | type.                   |
+-------------------------+----------------+-------------------------+
| [M](./M.md)\      | R              | Gets the location\'s    |
| [MAP](./MAP.md)   |                | map number.             |
+-------------------------+----------------+-------------------------+
| [STATI                  | R              | Gets the number of      |
| CS](./STATICS.md) |                | static items at the     |
|                         |                | location.               |
+-------------------------+----------------+-------------------------+
| [STATICS](./STA____________R_______________Gets_the_ID_of_the_nth__
_TICS.md)*.n.ID* |                | item at the location.   |
|                         |                | (zero-based)            |
+-------------------------+----------------+-------------------------+
| [STATICS](./STATIC_________R_______________Gets_the_hue_of_the_nth_
_S.md)*.n.COLOR* |                | item at the location.   |
|                         |                | (zero-based)            |
+-------------------------+----------------+-------------------------+
| [STATICS](./ST_____________R_______________Gets_the_Z_level_of_the_
_ATICS.md)*.n.Z* |                | nth item at the         |
|                         |                | location. (zero-based)  |
+-------------------------+----------------+-------------------------+
| [STATICS](./STAT___________R_______________Gets_the_KEY_property_
_ICS.md)*.n.KEY* |                | from the                |
|                         |                | [ITEMD                  |
|                         |                | EF](./ITEMDEF.md) |
|                         |                | of the nth item at the  |
|                         |                | location. (zero-based)  |
+-------------------------+----------------+-------------------------+
| [TERRA                  | R              | Gets the terrain\'s ID  |
| IN](./TERRAIN.md) |                | at the location.        |
+-------------------------+----------------+-------------------------+
| [TERRAIN                | R              | Gets the terrain\'s Z   |
| ](./TERRAIN.md).Z |                | level at the location.  |
+-------------------------+----------------+-------------------------+
| [TYPE](./TYPE.md) | R              | Gets the terrain\'s     |
|                         |                | TYPE at the location.   |
+-------------------------+----------------+-------------------------+
| [X](./X.md)       | R              | Gets the X coordinate   |
|                         |                | of the location.        |
+-------------------------+----------------+-------------------------+
| [Y](./Y.md)       | R              | Gets the Y coordinate   |
|                         |                | of the location.        |
+-------------------------+----------------+-------------------------+
| [Z](./Z.md)       | R              | Gets the Z coordinate   |
|                         |                | of the location.        |
+-------------------------+----------------+-------------------------+

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Objects](./_Objects.md)
