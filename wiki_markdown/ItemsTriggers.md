\_\_FORCETOC\_\_ Generally speaking, there are two types of "things" in
the game; characters and items. Compared to characters, items are very
complex. Items have a number of different uses, for example a sword is
an item that players can see and equip to increase the damage they can
do in combat. Some items in the game can not be seen by the players, but
they have as much impact on the player as their sword, for example, a
memory item is equipped every time a player is under the effects of a
spell. Some [special types of item](./Special_Items.md) also have
additional properties that can be accessed via scripts. The following
tables detail the various properties of items in SphereServer:

## References

References return pointers to other objects (e.g. the REGION reference
allows you to access the REGION that an object is in). These can either
be accessed by using *\<REFNAME\>* to return the [UID](./UID.md)
(1 for object types that don't have UIDs) of the object or 0 if it
doesn't exist, or by using *\<REFNAME.KEY\>* where KEY is a valid
property/function/reference for the *REFNAME* object. Click on the name
for more detailed information such as usage and examples.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [CONT](./CONT.md) | RW | Gets or sets the [character](./Characters.md) or [container item](./Special_ItemsContainers.md) that the object is inside. When an item's CONT is changed, it bypasses the typical behavior (for example, you can force an item to be "in" a container and bypass @dropon triggers, or force an item to be equipped to a player and bypass @equiptest and @equip triggers -- but be careful, because in this second scenario it may end up in an invalid layer.) |
| [LINK](./LINK.md) | RW | Gets or sets the [character](./Characters.md) or [item](./Items.md) that the item is linked to. Note, you can make circular LINK's, but a single item cannot be linked to more than one other item. |
| [REGION](./Regions.md) | R | Gets the [region](./Regions.md) that the object is in. |
| [ROOM](./ROOM.md) | R | Gets the [room](./Rooms.md) that the object is in. |
| [P](./P.md) | RW | Gets or sets the [position](./Map_Points.md) that the object is at. |
| [SECTOR](./Sectors.md) | R | Gets the [sector](./Sectors.md) that the object is in. |
| [TOPOBJ](./TOPOBJ.md) | R | Gets the top-most [character](./Characters.md) or [item](./Items.md) in the world that contains the item. |
| [TYPEDEF](TYPEDEF_(Reference) "wikilink") | R | Gets the [ITEMDEF](./ITEMDEF.md) that defines the item. |

## Properties and Functions

Here is a list of all item properties and functions. If a function is
marked as readable then it can return a value when used as <KEY>. Click
on the name for more detailed information such as usage and examples. If
an attempt is made to access a property that does not exist on the item,
the property from the [ITEMDEF](./ITEMDEF.md) will be accessed
instead.

<table>
<thead>
<tr>
<th><p>Name</p></th>
<th><p><strong>Read/Write</strong></p></th>
<th><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><a href="ADDCIRCLE" title="wikilink">ADDCIRCLE</a>
<em>spell_circle</em></p></td>
<td><p>W</p></td>
<td><p>Adds all of the spells in the given Magery circle to the
spellbook.</p></td>
</tr>
<tr>
<td><p><a href="ADDSPELL" title="wikilink">ADDSPELL</a>
<em>spell_id</em></p></td>
<td><p>RW</p></td>
<td><p>Gets whether or not a spell exists in the spellbook, or adds a
spell to the spellbook.</p></td>
</tr>
<tr>
<td><p><a href="AMMOANIM" title="wikilink">AMMOANIM</a></p></td>
<td><p>RW</p></td>
<td><p>Overrides TDATA4 for bow/crossbow type weapons.</p></td>
</tr>
<tr>
<td><p><a href="AMMOANIMHUE" title="wikilink">AMMOANIMHUE</a></p></td>
<td><p>RW</p></td>
<td><p>Sets the color of the effect when firing bow/crossbow type
weapons.</p></td>
</tr>
<tr>
<td><p><a href="AMMOANIMRENDER"
title="wikilink">AMMOANIMRENDER</a></p></td>
<td><p>RW</p></td>
<td><p>Sets the render mode of the effect when firing bow/crossbow type
weapons.</p></td>
</tr>
<tr>
<td><p><a href="AMMOCONT" title="wikilink">AMMOCONT</a></p></td>
<td><p>RW</p></td>
<td><p>Sets the container UID or ID where to search for ammos for
bow/crossbow type weapons.</p></td>
</tr>
<tr>
<td><p><a href="AMMOSOUNDHIT" title="wikilink">AMMOSOUNDHIT</a></p></td>
<td><p>RW</p></td>
<td><p>Overrides the hit sound on weapons.</p></td>
</tr>
<tr>
<td><p><a href="AMMOSOUNDMISS"
title="wikilink">AMMOSOUNDMISS</a></p></td>
<td><p>RW</p></td>
<td><p>Overrides the miss sound on weapons.</p></td>
</tr>
<tr>
<td><p><a href="AMMOTYPE" title="wikilink">AMMOTYPE</a></p></td>
<td><p>RW</p></td>
<td><p>Overrides TDATA3 for bow/crossbow type weapons.</p></td>
</tr>
<tr>
<td><p><a href="AMOUNT" title="wikilink">AMOUNT</a></p></td>
<td><p>RW</p></td>
<td><p>Gets the amount of items this icon represents (e.g. a pile of
gold or any stacked item).</p></td>
</tr>
<tr>
<td><p><a href="ATTR" title="wikilink">ATTR</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the item's attribute flags.</p></td>
</tr>
<tr>
<td><p><a href="BOUNCE" title="wikilink">BOUNCE</a></p></td>
<td><p>W</p></td>
<td><p>Moves the item to SRC's backpack (triggering the <em>you put the
item in your pack</em> message.</p></td>
</tr>
<tr>
<td><p><a href="CAN" title="wikilink">CAN</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or Sets the can_flags (Setting can be only done in the
Itemdef itself). Only readable in X branch.</p></td>
</tr>
<tr>
<td><p><a href="CANMASK" title="wikilink">CANMASK</a></p></td>
<td><p>RW</p></td>
<td><p>Stores the CAN flags to be dynamically switched on or off from
the base CAN property.</p></td>
</tr>
<tr>
<td><p><a href="CANSEE" title="wikilink">CANSEE</a></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if SRC can see the item.</p></td>
</tr>
<tr>
<td><p><a href="CANSEELOS" title="wikilink">CANSEELOS</a>
<em>point_or_uid</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if SRC has line of sight to the item or character (uid)
or point (location).</p></td>
</tr>
<tr>
<td><p><a href="CANSEELOSFLAG" title="wikilink">CANSEELOSFLAG</a>
<em>flags,point_or_uid</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if SRC has line of sight to the item. The
<em>flags</em> are defined in the los_flags section of the
sphere_defs.scp file and can be used to modify what tests take place.
The <em>point_or_uid</em> is an object or position that can be used to
test line of sight to something other than SRC. Note, the delimiter for
FLAG values is ;</p></td>
</tr>
<tr>
<td><p><a href="CLEARTAGS" title="wikilink">CLEARTAGS</a>
<em>prefix</em></p></td>
<td><p>W</p></td>
<td><p>Removes all TAGs from the item that start with the given
prefix.</p></td>
</tr>
<tr>
<td><p><a href="COLOR" title="wikilink">COLOR</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the object's hue.</p></td>
</tr>
<tr>
<td><p><a href="CONSUME" title="wikilink">CONSUME</a>
<em>amount</em></p></td>
<td><p>W</p></td>
<td><p>Deducts an amount from the item, deleting it at 0.</p></td>
</tr>
<tr>
<td><p><a href="CONTCONSUME" title="wikilink">CONTCONSUME</a>
<em>resource_list</em></p></td>
<td><p>W</p></td>
<td><p>Deletes items from inside the container.</p></td>
</tr>
<tr>
<td><p><a href="CONTGRID" title="wikilink">CONTGRID</a></p></td>
<td><p>RW</p></td>
<td><p>If in a container, gets or sets the grid number that the item
occupies (in KR's grid view)</p></td>
</tr>
<tr>
<td><p><a href="CONTP" title="wikilink">CONTP</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the position of the item within its
container.</p></td>
</tr>
<tr>
<td><p><a href="DAMAGE" title="wikilink">DAMAGE</a> <em>chance, type,
source</em></p></td>
<td><p>W</p></td>
<td><p>If <em>chance</em> is greater than (Rand(maxhits*16)), inflicts
damage of <em>type</em> (the damage type flags are defined in the
sphere_defs.scp file) upon the item. You can optionally specify the
<em>source</em> of the damage.</p></td>
</tr>
<tr>
<td><p><a href="DCLICK" title="wikilink">DCLICK</a></p></td>
<td><p>W</p></td>
<td><p>Double clicks the item, with SRC as the source of the
event.</p></td>
</tr>
<tr>
<td><p><a href="DECAY" title="wikilink">DECAY</a> <em>time</em></p></td>
<td><p>W</p></td>
<td><p>Sets the decay timer (in tenths of a second) for the
item.</p></td>
</tr>
<tr>
<td><p><a href="DESTROY" title="wikilink">DESTROY</a></p></td>
<td><p>W</p></td>
<td><p>Deletes the object, not stopped by a return 1 in <a
href="@Destroy" title="wikilink">@Destroy</a></p></td>
</tr>
<tr>
<td><p><a href="DIALOG_(Function)" title="wikilink">DIALOG</a>
<em>dialog_id, page, parameters</em></p></td>
<td><p>W</p></td>
<td><p>Displays a dialog to SRC.</p></td>
</tr>
<tr>
<td><p><a href="DISPID" title="wikilink">DISPID</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the ID that the item will appear as to
players.</p></td>
</tr>
<tr>
<td><p><a href="DISPIDDEC" title="wikilink">DISPIDDEC</a></p></td>
<td><p>RW</p></td>
<td><p>Same as <a href="DISPID" title="wikilink">DISPID</a>, except it
returns the ID as a decimal number.</p></td>
</tr>
<tr>
<td><p><a href="DISTANCE" title="wikilink">DISTANCE</a>
<em>point_or_uid</em></p></td>
<td><p>R</p></td>
<td><p>Gets the distance between this object and SRC. If
<em>point_or_uid</em> is used, SRC can be replaced with a map location
or another object.</p></td>
</tr>
<tr>
<td><p><a href="DMGCOLD" title="wikilink">DMGCOLD</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the amount of cold damage the weapon will
give.</p></td>
</tr>
<tr>
<td><p><a href="DMGENERGY" title="wikilink">DMGENERGY</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the amount of energy damage the weapon will
give.</p></td>
</tr>
<tr>
<td><p><a href="DMGFIRE" title="wikilink">DMGFIRE</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the amount of fire damage the weapon will
give.</p></td>
</tr>
<tr>
<td><p><a href="DMGPOISON" title="wikilink">DMGPOISON</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the amount of poison damage the weapon will
give.</p></td>
</tr>
<tr>
<td><p><a href="DROP" title="wikilink">DROP</a></p></td>
<td><p>W</p></td>
<td><p>Drops the item to the ground.</p></td>
</tr>
<tr>
<td><p><a href="DUPE" title="wikilink">DUPE</a></p></td>
<td><p>W</p></td>
<td><p>Clones the item.</p></td>
</tr>
<tr>
<td><p><a href="EDIT" title="wikilink">EDIT</a></p></td>
<td><p>W</p></td>
<td><p>Displays an editing dialog for the item to SRC.</p></td>
</tr>
<tr>
<td><p><a href="EFFECT" title="wikilink">EFFECT</a> <em>type, item_id,
speed, loop, explode, colour, rendermode</em></p></td>
<td><p>W</p></td>
<td><p>Displays an effect to nearby clients.</p></td>
</tr>
<tr>
<td><p><a href="EMOTE" title="wikilink">EMOTE</a>
<em>message</em></p></td>
<td><p>W</p></td>
<td><p>Displays a *You see* message to all nearby clients.</p></td>
</tr>
<tr>
<td><p><a href="EQUIP" title="wikilink">EQUIP</a></p></td>
<td><p>W</p></td>
<td><p>Equips the item to SRC.</p></td>
</tr>
<tr>
<td><p><a href="EVENTS_(Property)" title="wikilink">EVENTS</a>
<em>event_defname</em></p></td>
<td><p>RW</p></td>
<td><p>Gets a list of events attached to the object, or adds or removes
an event to or from the object.</p></td>
</tr>
<tr>
<td><p><a href="FIX" title="wikilink">FIX</a></p></td>
<td><p>W</p></td>
<td><p>Re-aligns the item or character's Z level to ground level (if
items are on the ground, the top item's <em>Z+HEIGHT</em> is
used).</p></td>
</tr>
<tr>
<td><p><a href="FLIP" title="wikilink">FLIP</a></p></td>
<td><p>W</p></td>
<td><p>Rotates the item clockwise.</p></td>
</tr>
<tr>
<td><p><a href="FRUIT" title="wikilink">FRUIT</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the fruit that will be produced by the
crops.</p></td>
</tr>
<tr>
<td><p><a href="HEIGHT" title="wikilink">HEIGHT</a></p></td>
<td><p>R</p></td>
<td><p>Gets the height of the item.</p></td>
</tr>
<tr>
<td><p><a href="HITS" title="wikilink">HITS</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the number of hitpoints the item has.</p></td>
</tr>
<tr>
<td><p><a href="HITPOINTS" title="wikilink">HITPOINTS</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the number of hitpoints the item has.</p></td>
</tr>
<tr>
<td><p><a href="ID" title="wikilink">ID</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the ID of the item.</p></td>
</tr>
<tr>
<td><p><a href="INFO" title="wikilink">INFO</a></p></td>
<td><p>W</p></td>
<td><p>Displays an information dialog about the item to SRC.</p></td>
</tr>
<tr>
<td><p><a href="ISARMOR" title="wikilink">ISARMOR</a>
<em>object_uid</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the object is armour.</p></td>
</tr>
<tr>
<td><p><a href="ISCHAR" title="wikilink">ISCHAR</a></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the object is a character.</p></td>
</tr>
<tr>
<td><p><a href="ISCONT" title="wikilink">ISCONT</a></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the object is a container.</p></td>
</tr>
<tr>
<td><p><a href="ISEVENT"
title="wikilink">ISEVENT</a><em>.event_defname</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the object has an event attached to it.</p></td>
</tr>
<tr>
<td><p><a href="ISITEM" title="wikilink">ISITEM</a></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the object is an item.</p></td>
</tr>
<tr>
<td><p><a href="ISNEARTYPE" title="wikilink">ISNEARTYPE</a> <em>type,
distance, flags</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if a nearby item has the given TYPE and is within
<em>distance</em>.</p></td>
</tr>
<tr>
<td><p><a href="ISNEARTYPETOP" title="wikilink">ISNEARTYPETOP</a>
<em>type, distance, flags</em></p></td>
<td><p>R</p></td>
<td><p>Returns a nearby world location of a nearby item which has the
given TYPE and is within <em>distance</em>.</p></td>
</tr>
<tr>
<td><p><a href="ISPLAYER" title="wikilink">ISPLAYER</a></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the object is a player character.</p></td>
</tr>
<tr>
<td><p><a href="ISTEVENT"
title="wikilink">ISTEVENT</a><em>.event_defname</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the object has an event attached to its
ITEMDEF.</p></td>
</tr>
<tr>
<td><p><a href="ISTIMERF"
title="wikilink">ISTIMERF</a><em>.function</em></p></td>
<td><p>R</p></td>
<td><p>Returns the number of seconds left on the specified timerf if it
exists.</p></td>
</tr>
<tr>
<td><p><a href="ISWEAPON" title="wikilink">ISWEAPON</a>
<em>object_uid</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the object is a weapon.</p></td>
</tr>
<tr>
<td><p><a href="LAYER" title="wikilink">LAYER</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the layer that the item occupies when equipped
(possible layers are defined in the sphere_defs.scp file).</p></td>
</tr>
<tr>
<td><p><a href="MAP" title="wikilink">MAP</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the map that this object is located.</p></td>
</tr>
<tr>
<td><p><a href="MAXHITS" title="wikilink">MAXHITS</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the maximum number of hitpoints the item can
have.</p></td>
</tr>
<tr>
<td><p><a href="MENU_(Function)" title="wikilink">MENU</a>
<em>menu_defname</em></p></td>
<td><p>W</p></td>
<td><p>Displays a menu to SRC.</p></td>
</tr>
<tr>
<td><p><a href="MESSAGE" title="wikilink">MESSAGE</a>
<em>message</em></p></td>
<td><p>W</p></td>
<td><p>Displays a message above this item to SRC.</p></td>
</tr>
<tr>
<td><p><a href="MESSAGEUA" title="wikilink">MESSAGEUA</a> <em>colour,
talkmode, font, lang_id, message</em></p></td>
<td><p>W</p></td>
<td><p>Displays a UNICODE message above this item to SRC.</p></td>
</tr>
<tr>
<td><p><a href="MODAR" title="wikilink">MODAR</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets a modifier for the item's armour rating if it is
clothing, armor, or a shield. This gets or sets a modifier for the
item's damage if it is a weapon type.</p></td>
</tr>
<tr>
<td><p><a href="MORE1" title="wikilink">MORE1</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the MORE1 value for the item.</p></td>
</tr>
<tr>
<td><p><a href="MORE1H" title="wikilink">MORE1H</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the upper 4 bytes of the item's MORE1
value.</p></td>
</tr>
<tr>
<td><p><a href="MORE1L" title="wikilink">MORE1L</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the lower 4 bytes of the item's MORE1
value.</p></td>
</tr>
<tr>
<td><p><a href="MORE2" title="wikilink">MORE2</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the MORE2 value for the item.</p></td>
</tr>
<tr>
<td><p><a href="MORE2H" title="wikilink">MORE2H</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the upper 4 bytes of the item's MORE2
value.</p></td>
</tr>
<tr>
<td><p><a href="MORE2L" title="wikilink">MORE2L</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the lower 4 bytes of the item's MORE2
value.</p></td>
</tr>
<tr>
<td><p><a href="MOREM" title="wikilink">MOREM</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the MOREM value for the item.</p></td>
</tr>
<tr>
<td><p><a href="MOREX" title="wikilink">MOREX</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the MOREX value for the item.</p></td>
</tr>
<tr>
<td><p><a href="MOREY" title="wikilink">MOREY</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the MOREY value for the item.</p></td>
</tr>
<tr>
<td><p><a href="MOREZ" title="wikilink">MOREZ</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the MOREZ value for the item.</p></td>
</tr>
<tr>
<td><p><a href="MOREP" title="wikilink">MOREP</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the MOREP value for the item.</p></td>
</tr>
<tr>
<td><p><a href="MOVE" title="wikilink">MOVE</a> <em>direction
amount</em><br />
<a href="MOVE" title="wikilink">MOVE</a> <em>x y</em></p></td>
<td><p>W</p></td>
<td><p>Moves the object relative to its current position. Possible
<em>direction</em> values are N,S,W, or E. Note, you can combine
directions (like: MOVE SW 1) but nonsensical directions (like: MOVE WE
2) have the nonsense removed.</p></td>
</tr>
<tr>
<td><p><a href="MOVENEAR" title="wikilink">MOVENEAR</a> <em>object_uid,
distance</em></p></td>
<td><p>W</p></td>
<td><p>Moves the object to a random location near another object within
a certain distance.</p></td>
</tr>
<tr>
<td><p><a href="MOVETO" title="wikilink">MOVETO</a>
<em>location</em></p></td>
<td><p>W</p></td>
<td><p>Moves the object to a specific location (note, the AREADEF or
ROOMDEF must have a P defined).</p></td>
</tr>
<tr>
<td><p><a href="NAME" title="wikilink">NAME</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the object's name.</p></td>
</tr>
<tr>
<td><p><a href="NUDGEDOWN" title="wikilink">NUDGEDOWN</a>
<em>amount</em></p></td>
<td><p>W</p></td>
<td><p>Decreases the object's Z level.</p></td>
</tr>
<tr>
<td><p><a href="NUDGEUP" title="wikilink">NUDGEUP</a>
<em>amount</em></p></td>
<td><p>W</p></td>
<td><p>Increases the object's Z level.</p></td>
</tr>
<tr>
<td><p><a href="PROMPTCONSOLE" title="wikilink">PROMPTCONSOLE</a>
<em>function, prompt_message</em></p></td>
<td><p>W</p></td>
<td><p>Displays a prompt message to SRC and passes their response into a
specified function.</p></td>
</tr>
<tr>
<td><p><a href="PROMPTCONSOLEU" title="wikilink">PROMPTCONSOLEU</a>
<em>function, prompt_message</em></p></td>
<td><p>W</p></td>
<td><p>Displays a prompt message to SRC and passes their response into a
specified function, supporting UNICODE response.</p></td>
</tr>
<tr>
<td><p><a href="REMOVE" title="wikilink">REMOVE</a></p></td>
<td><p>W</p></td>
<td><p>Deletes the object.</p></td>
</tr>
<tr>
<td><p><a href="REMOVEFROMVIEW"
title="wikilink">REMOVEFROMVIEW</a></p></td>
<td><p>W</p></td>
<td><p>Removes the object from nearby clients' screens.</p></td>
</tr>
<tr>
<td><p><a href="RESCOUNT" title="wikilink">RESCOUNT</a>
<em>item_defname</em></p></td>
<td><p>R</p></td>
<td><p>Returns the total amount of a specific item inside a
container.</p></td>
</tr>
<tr>
<td><p><a href="RESENDTOOLTIP"
title="wikilink">RESENDTOOLTIP</a></p></td>
<td><p>W</p></td>
<td><p>Forces Sphere to update the tooltips for nearby clients.</p></td>
</tr>
<tr>
<td><p><a href="SAY" title="wikilink">SAY</a> <em>message</em></p></td>
<td><p>W</p></td>
<td><p>Makes the object speak a message.</p></td>
</tr>
<tr>
<td><p><a href="SAYU" title="wikilink">SAYU</a>
<em>message</em></p></td>
<td><p>W</p></td>
<td><p>Makes the object speak a UTF-8 message</p></td>
</tr>
<tr>
<td><p><a href="SAYUA" title="wikilink">SAYUA</a> <em>colour, talkmode,
font, lang_id, text</em></p></td>
<td><p>W</p></td>
<td><p>Makes the object speak a UNICODE message.</p></td>
</tr>
<tr>
<td><p><a href="SDIALOG" title="wikilink">SDIALOG</a> <em>dialog_id,
page, parameters</em></p></td>
<td><p>W</p></td>
<td><p>Displays a dialog to SRC, providing that it is not already
open.</p></td>
</tr>
<tr>
<td><p><a href="SERIAL" title="wikilink">SERIAL</a></p></td>
<td><p>R</p></td>
<td><p>Gets the item's unique ID in the world.</p></td>
</tr>
<tr>
<td><p><a href="SEXTANTP" title="wikilink">SEXTANTP</a>
<em>location</em></p></td>
<td><p>R</p></td>
<td><p>Converts the item's location or a specified location into sextant
coordinates.</p></td>
</tr>
<tr>
<td><p><a href="SOUND" title="wikilink">SOUND</a> <em>sound_id,
repeat</em></p></td>
<td><p>W</p></td>
<td><p>Plays a sound from this object.</p></td>
</tr>
<tr>
<td><p><a href="SPELLEFFECT" title="wikilink">SPELLEFFECT</a>
<em>spell_id, strength, source_character_uid,
source_item_uid</em></p></td>
<td><p>W</p></td>
<td><p>Causes the item to be affected by a spell.</p></td>
</tr>
<tr>
<td><p><a href="TAG" title="wikilink">TAG</a><em>.name</em></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the value of a TAG.</p></td>
</tr>
<tr>
<td><p><a href="TAGAT"
title="wikilink">TAGAT</a><em>.index</em></p></td>
<td><p>R</p></td>
<td><p>Gets a TAG at the given zero-based index.</p></td>
</tr>
<tr>
<td><p><a href="TAGAT"
title="wikilink">TAGAT</a><em>.index</em>.KEY</p></td>
<td><p>R</p></td>
<td><p>Gets the name of the TAG at the given zero-based index.</p></td>
</tr>
<tr>
<td><p><a href="TAGAT"
title="wikilink">TAGAT</a><em>.index</em>.VAL</p></td>
<td><p>R</p></td>
<td><p>Gets the value of the TAG at the given zero-based index.</p></td>
</tr>
<tr>
<td><p><a href="TAGCOUNT" title="wikilink">TAGCOUNT</a></p></td>
<td><p>R</p></td>
<td><p>Gets the number of TAGs stored on the item.</p></td>
</tr>
<tr>
<td><p><a href="TAGLIST" title="wikilink">TAGLIST</a></p></td>
<td><p>W</p></td>
<td><p>Outputs a list of the object's TAGs.</p></td>
</tr>
<tr>
<td><p><a href="TARGET" title="wikilink">TARGET</a><em>FGMW</em>
<em>function</em></p></td>
<td><p>W</p></td>
<td><p>Displays a targeting cursor to SRC. <em>F</em> makes the
<em>function</em> available, and when added, the function name must be
the 1st argument. <em>M</em> allows you to place a <em>multi</em> item,
in which case the multi number must be passed as an argument. <em>G</em>
forces the target to only be the ground. <em>W</em> checks the criminal
status of the player before (or after?) the target selection is
made.</p></td>
</tr>
<tr>
<td><p><a href="TIMER" title="wikilink">TIMER</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the length of time before the item's timer expires,
in seconds.</p></td>
</tr>
<tr>
<td><p><a href="TIMERD" title="wikilink">TIMERD</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the length of time before the item's timer expires,
in tenths of a second.</p></td>
</tr>
<tr>
<td><p><a href="TIMERF" title="wikilink">TIMERF</a> <em>time,
function</em></p></td>
<td><p>W</p></td>
<td><p>Schedules a function to be executed on this object in
<em>time</em> seconds.</p></td>
</tr>
<tr>
<td><p><a href="TIMERF" title="wikilink">TIMERF</a>
<em>CLEAR</em></p></td>
<td><p>W</p></td>
<td><p>Clears all scheduled functions from the object.</p></td>
</tr>
<tr>
<td><p><a href="TIMERF" title="wikilink">TIMERF</a> <em>STOP,
function</em></p></td>
<td><p>W</p></td>
<td><p>Stops the specified function from the item. (On X version wild
character * is available for defining the function name or the
argument)</p></td>
</tr>
<tr>
<td><p><a href="TRIGGER" title="wikilink">TRIGGER</a> <em>trig_name,
trigger_argtype, argument1, argument2, ...</em></p></td>
<td><p>R</p></td>
<td><p>Fires a custom trigger (trig_name), allowing you to define the
behavior of the arguments (the types are defined under trigger_argtype
in the sphere_defs.scp file). The result of the trigger's RETURN value
is returned. For example:</p>
<p><code>LOCAL.result=&lt;TRIGGER @CustomTrigger,&lt;DEF.tat_as_argn&gt;,1,2,3&gt;</code></p></td>
</tr>
<tr>
<td><p><a href="TYPE" title="wikilink">TYPE</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the item type. You can use built-in or custom <a
href="TYPEDEF" title="wikilink">TYPEDEFs</a> as a value.</p></td>
</tr>
<tr>
<td><p><a href="UID" title="wikilink">UID</a></p></td>
<td><p>R</p></td>
<td><p>Gets the item's unique ID in the world.</p></td>
</tr>
<tr>
<td><p><a href="UNEQUIP" title="wikilink">UNEQUIP</a></p></td>
<td><p>W</p></td>
<td><p>Unequips the item and places it in SRC's backpack.</p></td>
</tr>
<tr>
<td><p><a href="UPDATE" title="wikilink">UPDATE</a></p></td>
<td><p>W</p></td>
<td><p>Updates the state of the item to nearby clients.</p></td>
</tr>
<tr>
<td><p><a href="UPDATEX" title="wikilink">UPDATEX</a></p></td>
<td><p>W</p></td>
<td><p>Updates the state of the item to nearby clients, removing it from
their view first to ensure a full refresh.</p></td>
</tr>
<tr>
<td><p><a href="USESCUR" title="wikilink">USESCUR</a></p></td>
<td><p>W</p></td>
<td><p>X branch only. Gets or sets the current uses of an item. Only
partially supported.</p></td>
</tr>
<tr>
<td><p><a href="USESMAX" title="wikilink">USESMAX</a></p></td>
<td><p>W</p></td>
<td><p>X branch only. Gets or sets the maximum uses of an item. Only
partially supported.</p></td>
</tr>
<tr>
<td><p><a href="USE" title="wikilink">USE</a>
<em>check_los</em></p></td>
<td><p>W</p></td>
<td><p>Uses the item, as if SRC had double clicked it.</p></td>
</tr>
<tr>
<td><p><a href="USEITEM" title="wikilink">USEITEM</a></p></td>
<td><p>W</p></td>
<td><p>Double clicks the item, with SRC as the source of the event,
without checking for line of sight.</p></td>
</tr>
<tr>
<td><p><a href="WEIGHT" title="wikilink">WEIGHT</a></p></td>
<td><p>R</p></td>
<td><p>Gets the weight of the item.</p></td>
</tr>
<tr>
<td><p><a href="Z" title="wikilink">Z</a></p></td>
<td><p>R</p></td>
<td><p>Gets the Z position of the item.</p></td>
</tr>
</tbody>
</table>

## Triggers

Here is a list of all item triggers. Click on the trigger name for more
detailed information such as arguments and examples.

|  |  |  |
|----|----|----|
| **Name** | **Description** | **Sphere X Only?** |
| [@AfterClick](./AfterClick.md) | Fires when the object has been single-clicked, just before the overhead name is shown. |  |
| [@Buy](./Buy.md) | Fires when the item is being bought from a vendor. |  |
| [@Click](./Click.md) | Fires when the object has been single-clicked. |  |
| [@ClientTooltip](./ClientTooltip.md) | Fires when tooltips are about to be sent to a client. |  |
| [@ContextMenuRequest](./ContextMenuRequest.md) | Fires when a client requests the context menu options for the object. |  |
| [@ContextMenuSelect](./ContextMenuSelect.md) | Fires when a client selects a context menu option for the object. |  |
| [@Carve](./Carve.md) | Fires when a corpse item is being carved. | X |
| [@Create](./Create.md) | Fires when the object is initially created, before it is placed in the world. |  |
| [@Damage](./Damage.md) | Fires when the item receives damage. |  |
| [@DClick](./DClick.md) | Fires when the object is double-clicked. |  |
| [@Destroy](./Destroy.md) | Fires when the object is being deleted. |  |
| [@DropOn_Char](./DropOn_Char.md) | Fires when the item has been dropped on to a character. |  |
| [@DropOn_Ground](./DropOn_Ground.md) | Fires when the item has been dropped on to the ground. |  |
| [@DropOn_Item](./DropOn_Item.md) | Fires when the item is dropped on to another item. |  |
| [@DropOn_Self](./DropOn_Self.md) | Fires when an item has been dropped on to this item. |  |
| [@DropOn_Trade](./DropOn_Trade.md) | Fires when an item is being dropped on a Trade Window. |  |
| [@Dye](./Dye.md) | Fires when an item is having its colored changed. |  |
| [@Equip](./Equip.md) | Fires when the item has been equipped. |  |
| [@EquipTest](./EquipTest.md) | Fires when the item is about to be equipped. |  |
| [@HouseDesignBegin](./HouseDesignBegin.md) | A trigger for t_multi_custom, called when the player enters on design mode. | X |
| [@HouseDesignCommitItem](./HouseDesignCommitItem.md) | Fires for each commited item in house design system. | X |
| [@PickUp_Ground](./PickUp_Ground.md) | Fires when the item ihas been picked up from the ground. |  |
| [@PickUp_Pack](./PickUp_Pack.md) | Fires when the item is picked up from inside a container. |  |
| [@PickUp_Self](./PickUp_Self.md) | Fires when an item has been picked up from inside the item. |  |
| [@PickUp_Stack](./PickUp_Stack.md) | Fires when the item is picked up from a stack. |  |
| [@Redeed](./Redeed.md) | Fires when multi item is about to redeed (t_multi, t_ship, t_multi_custom, t_addon). |  |
| [@Sell](./Sell.md) | Fires when the item is sold to a vendor. |  |
| [@Smelt](./Smelt.md) | Fires when the item is being smelt. | X |
| [@SpellEffect](./SpellEffect.md) | Fires when the object is hit by the effects of a spell. |  |
| [@Step](./Step.md) | Fires when a character steps on the item. |  |
| [@TargOn_Cancel](./TargOn_Cancel.md) | Fires when a target is cancelled from the item. |  |
| [@TargOn_Char](./TargOn_Char.md) | Fires when a character is targeted from the item. |  |
| [@TargOn_Ground](./TargOn_Ground.md) | Fires when the ground is targeted from the item. |  |
| [@TargOn_Item](./TargOn_Item.md) | Fires when an item is targeted from this item. |  |
| [@Timer](./Timer.md) | Fires when the item's timer expires. |  |
| [@ToolTip](./ToolTip.md) | Fires when old-style tooltips are requested for the item. |  |
| [@UnEquip](./UnEquip.md) | Fires when the item is unequipped. |  |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Objects](./_Objects.md)
