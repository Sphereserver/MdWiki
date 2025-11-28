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
[UID](UID "wikilink") (1 for object types that don't have UIDs) of the
object or 0 if it doesn't exist, or by using *\<REFNAME.KEY\>* where KEY
is a valid property/function/reference for the *REFNAME* object. Click
on the name for more detailed information such as usage and examples.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [REGION](REGION "wikilink") | R | Gets the [region](Regions "wikilink") that contains the map point. |
| [ROOM](ROOM "wikilink") | R | Gets the [room](Rooms "wikilink") that contains the map point. |
| [SECTOR](SECTOR "wikilink") | R | Gets the [sector](Sectors "wikilink") that contains the map point. |

## Properties and Functions

Here is a list of all map point properties and functions. If a function
is marked as readable then it can return a value when used as <KEY>.
Click on the name for more detailed information such as usage and
examples.

<table>
<tbody>
<tr>
<td><p><strong>Name</strong></p></td>
<td><p><strong>Read/Write</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p><a href="COMPONENTS" title="wikilink">COMPONENTS</a></p></td>
<td><p>R</p></td>
<td><p>Gets the number of components of the <a href="MULTI"
title="wikilink">MULTI</a> at the location.</p></td>
</tr>
<tr>
<td><p><a href="COMPONENTS"
title="wikilink">COMPONENTS</a><em>.n.ID</em></p></td>
<td><p>R</p></td>
<td><p>Gets the ID of the nth component at the location.
(zero-based)</p></td>
</tr>
<tr>
<td><p><a href="COMPONENTS"
title="wikilink">COMPONENTS</a><em>.n.MULTI</em></p></td>
<td><p>R</p></td>
<td><p>Gets the UID of the MULTI item.</p></td>
</tr>
<tr>
<td><p><a href="COMPONENTS"
title="wikilink">COMPONENTS</a><em>.n.Z</em></p></td>
<td><p>R</p></td>
<td><p>Gets the Z level of the nth component at the location.
(zero-based)</p></td>
</tr>
<tr>
<td><p><a href="COMPONENTS"
title="wikilink">COMPONENTS</a><em>.n.KEY</em></p></td>
<td><p>R</p></td>
<td><p>Gets the <em>KEY</em> property from the <a href="ITEMDEF"
title="wikilink">ITEMDEF</a> of the nth component at the location.
(zero-based)</p></td>
</tr>
<tr>
<td><p><a href="ISNEARTYPE" title="wikilink">ISNEARTYPE</a> <em>type,
distance, check_multis</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if an item exists within <em>distance</em> tiles of the
location whose <a href="TYPE" title="wikilink">TYPE</a> matches a
specified type.</p></td>
</tr>
<tr>
<td><p><a href="M" title="wikilink">M</a><br />
<a href="MAP" title="wikilink">MAP</a></p></td>
<td><p>R</p></td>
<td><p>Gets the location's map number.</p></td>
</tr>
<tr>
<td><p><a href="STATICS" title="wikilink">STATICS</a></p></td>
<td><p>R</p></td>
<td><p>Gets the number of static items at the location.</p></td>
</tr>
<tr>
<td><p><a href="STATICS"
title="wikilink">STATICS</a><em>.n.ID</em></p></td>
<td><p>R</p></td>
<td><p>Gets the ID of the nth item at the location.
(zero-based)</p></td>
</tr>
<tr>
<td><p><a href="STATICS"
title="wikilink">STATICS</a><em>.n.COLOR</em></p></td>
<td><p>R</p></td>
<td><p>Gets the hue of the nth item at the location.
(zero-based)</p></td>
</tr>
<tr>
<td><p><a href="STATICS"
title="wikilink">STATICS</a><em>.n.Z</em></p></td>
<td><p>R</p></td>
<td><p>Gets the Z level of the nth item at the location.
(zero-based)</p></td>
</tr>
<tr>
<td><p><a href="STATICS"
title="wikilink">STATICS</a><em>.n.KEY</em></p></td>
<td><p>R</p></td>
<td><p>Gets the <em>KEY</em> property from the <a href="ITEMDEF"
title="wikilink">ITEMDEF</a> of the nth item at the location.
(zero-based)</p></td>
</tr>
<tr>
<td><p><a href="TERRAIN" title="wikilink">TERRAIN</a></p></td>
<td><p>R</p></td>
<td><p>Gets the terrain's ID at the location.</p></td>
</tr>
<tr>
<td><p><a href="TERRAIN" title="wikilink">TERRAIN</a>.Z</p></td>
<td><p>R</p></td>
<td><p>Gets the terrain's Z level at the location.</p></td>
</tr>
<tr>
<td><p><a href="TYPE" title="wikilink">TYPE</a></p></td>
<td><p>R</p></td>
<td><p>Gets the terrain's TYPE at the location.</p></td>
</tr>
<tr>
<td><p><a href="X" title="wikilink">X</a></p></td>
<td><p>R</p></td>
<td><p>Gets the X coordinate of the location.</p></td>
</tr>
<tr>
<td><p><a href="Y" title="wikilink">Y</a></p></td>
<td><p>R</p></td>
<td><p>Gets the Y coordinate of the location.</p></td>
</tr>
<tr>
<td><p><a href="Z" title="wikilink">Z</a></p></td>
<td><p>R</p></td>
<td><p>Gets the Z coordinate of the location.</p></td>
</tr>
</tbody>
</table>

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Objects](Category:_Objects "wikilink")
