```{=mediawiki}
{{Languages|Map_Points}}
```
\_\_FORCETOC\_\_ A map point is a specific location on a world map,
defined by X, Y, Z and M coordinates. Map point references, such as *P*
from the [character](Characters "wikilink")/[item](Items "wikilink")
object and *MAP(x,y,map)* from the [server](Server "wikilink") object
can be used to access additional information about a map point such as
what static items exist at the location. The following tables detail the
various properties of map points in SphereServer:

## References

References return pointers to other objects (e.g. the REGION reference
allows you to access the region that contains the map point). These can
either be accessed by using *\<REFNAME\>* to return the
[UID](UID "wikilink") (1 for object types that don\'t have UIDs) of the
object or 0 if it doesn\'t exist, or by using *\<REFNAME.KEY\>* where
KEY is a valid property/function/reference for the *REFNAME* object.
Click on the name for more detailed information such as usage and
examples.

  ----------------------------- ---------------- --------------------------------------------------------------------
  **Name**                      **Read/Write**   **Description**
  [REGION](REGION "wikilink")   R                Gets the [region](Regions "wikilink") that contains the map point.
  [ROOM](ROOM "wikilink")       R                Gets the [room](Rooms "wikilink") that contains the map point.
  [SECTOR](SECTOR "wikilink")   R                Gets the [sector](Sectors "wikilink") that contains the map point.
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
|                         |                | ULTI](MULTI "wikilink") |
|                         |                | at the location.        |
+-------------------------+----------------+-------------------------+
| [COMPONENTS](COMPON     | R              | Gets the ID of the nth  |
| ENTS "wikilink")*.n.ID* |                | component at the        |
|                         |                | location. (zero-based)  |
+-------------------------+----------------+-------------------------+
| [COMPONENTS](COMPONENT  | R              | Gets the UID of the     |
| S "wikilink")*.n.MULTI* |                | MULTI item.             |
+-------------------------+----------------+-------------------------+
| [COMPONENTS](COMPO      | R              | Gets the Z level of the |
| NENTS "wikilink")*.n.Z* |                | nth component at the    |
|                         |                | location. (zero-based)  |
+-------------------------+----------------+-------------------------+
| [COMPONENTS](COMPONE    | R              | Gets the *KEY* property |
| NTS "wikilink")*.n.KEY* |                | from the                |
|                         |                | [ITEMD                  |
|                         |                | EF](ITEMDEF "wikilink") |
|                         |                | of the nth component at |
|                         |                | the location.           |
|                         |                | (zero-based)            |
+-------------------------+----------------+-------------------------+
| [ISNEARTYPE]            | R              | Returns 1 if an item    |
| (ISNEARTYPE "wikilink") |                | exists within           |
| *type, distance,        |                | *distance* tiles of the |
| check_multis*           |                | location whose          |
|                         |                | [TYPE](TYPE "wikilink") |
|                         |                | matches a specified     |
|                         |                | type.                   |
+-------------------------+----------------+-------------------------+
| [M](M "wikilink")\      | R              | Gets the location\'s    |
| [MAP](MAP "wikilink")   |                | map number.             |
+-------------------------+----------------+-------------------------+
| [STATI                  | R              | Gets the number of      |
| CS](STATICS "wikilink") |                | static items at the     |
|                         |                | location.               |
+-------------------------+----------------+-------------------------+
| [STATICS](STA           | R              | Gets the ID of the nth  |
| TICS "wikilink")*.n.ID* |                | item at the location.   |
|                         |                | (zero-based)            |
+-------------------------+----------------+-------------------------+
| [STATICS](STATIC        | R              | Gets the hue of the nth |
| S "wikilink")*.n.COLOR* |                | item at the location.   |
|                         |                | (zero-based)            |
+-------------------------+----------------+-------------------------+
| [STATICS](ST            | R              | Gets the Z level of the |
| ATICS "wikilink")*.n.Z* |                | nth item at the         |
|                         |                | location. (zero-based)  |
+-------------------------+----------------+-------------------------+
| [STATICS](STAT          | R              | Gets the *KEY* property |
| ICS "wikilink")*.n.KEY* |                | from the                |
|                         |                | [ITEMD                  |
|                         |                | EF](ITEMDEF "wikilink") |
|                         |                | of the nth item at the  |
|                         |                | location. (zero-based)  |
+-------------------------+----------------+-------------------------+
| [TERRA                  | R              | Gets the terrain\'s ID  |
| IN](TERRAIN "wikilink") |                | at the location.        |
+-------------------------+----------------+-------------------------+
| [TERRAIN                | R              | Gets the terrain\'s Z   |
| ](TERRAIN "wikilink").Z |                | level at the location.  |
+-------------------------+----------------+-------------------------+
| [TYPE](TYPE "wikilink") | R              | Gets the terrain\'s     |
|                         |                | TYPE at the location.   |
+-------------------------+----------------+-------------------------+
| [X](X "wikilink")       | R              | Gets the X coordinate   |
|                         |                | of the location.        |
+-------------------------+----------------+-------------------------+
| [Y](Y "wikilink")       | R              | Gets the Y coordinate   |
|                         |                | of the location.        |
+-------------------------+----------------+-------------------------+
| [Z](Z "wikilink")       | R              | Gets the Z coordinate   |
|                         |                | of the location.        |
+-------------------------+----------------+-------------------------+

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Objects](Category:_Objects "wikilink")
