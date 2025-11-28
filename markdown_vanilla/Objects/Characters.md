\_\_FORCETOC\_\_ A character can be either a player or an NPC.

## References

References return pointers to other objects (e.g. the REGION reference
allows you to access the REGION that an object is in). These can either
be accessed by using *\<REFNAME\>* to return the [UID](UID "wikilink")
(1 for object types that don't have UIDs) of the object or 0 if it
doesn't exist, or by using *\<REFNAME.KEY\>* where KEY is a valid
property/function/reference for the *REFNAME* object. Click on the name
for more detailed information such as usage and examples.

|  |  |  |  |
|----|----|----|----|
| **Name** | **Read/Write** | **Description** | **Sphere X only?** |
| [ACCOUNT](Accounts "wikilink") | RW | Gets or sets the [account](Accounts "wikilink") that the character belongs to. |  |
| [ACT](ACT "wikilink") | RW | Gets or sets the [character](Characters "wikilink") or [item](Items "wikilink") that is related to the action the character is performing. |  |
| [FINDCONT](FINDCONT "wikilink")*.n* | R | Gets the nth [item](Items "wikilink") equipped to the character. (zero-based) |  |
| [FINDID](FINDID "wikilink")*.item_id* | R | Gets the first [item](Items "wikilink") found equipped to the character or inside their backpack, with the matching [BASEID](BASEID "wikilink"). |  |
| [FINDLAYER](FINDLAYER "wikilink")*.layer* | R | Gets the [item](Items "wikilink") that the character has equipped in a specified layer. |  |
| [FINDTYPE](FINDTYPE "wikilink")*.type* | R | Gets the first [item](Items "wikilink") found equipped to the character or inside their backpack, with the matching [TYPE](TYPE "wikilink"). |  |
| [MEMORYFINDTYPE](MEMORYFINDTYPE "wikilink")*.memory_flags* | R | Gets a [memory item](Items "wikilink") with the specified flags. |  |
| [MEMORYFIND](MEMORYFIND "wikilink").*object_uid* | R | Gets a [memory item](Items "wikilink") that is linked to the given object. |  |
| [OWNER](OWNER "wikilink") | R | Gets the character that owns this character. (RW in SphereServer-X Build) |  |
| [SPAWNITEM](SPAWNITEM "wikilink") | R | Gets the [spawn item](Items "wikilink") (t_spawn_char) that this character originated from. |  |
| [WEAPON](WEAPON "wikilink") | R | Gets the [weapon](Items "wikilink") that the character currently has equipped. |  |
| [P](P "wikilink") | RW | Gets or sets the [position](Map_Points "wikilink") that the character is at. |  |
| [REGION](Regions "wikilink") | R | Gets the [region](Regions "wikilink") that the character is currently located in. |  |
| [ROOM](Rooms "wikilink") | R | Gets the [room](Rooms "wikilink") that the character is in. |  |
| [SECTOR](Sectors "wikilink") | R | Gets the [sector](Sectors "wikilink") that the character is in. |  |
| [TOPOBJ](TOPOBJ "wikilink") | R | Gets the top-most [character](Characters "wikilink") or [item](Items "wikilink") in the world that contains the character. |  |
| [TYPEDEF](TYPEDEF_(Reference) "wikilink") | R | Gets the [CHARDEF](CHARDEF "wikilink") that defines the character. |  |

## Properties and Functions

Here is a list of all character properties and functions. If a function
is marked as readable then it can return a value when used as <KEY>.
Click on the name for more detailed information such as usage and
examples. If an attempt is made to access a property that does not exist
on the character, the property from the [CHARDEF](CHARDEF "wikilink")
will be accessed instead.

<table>
<tbody>
<tr>
<td><p><strong>Name</strong></p></td>
<td><p><strong>Read/Write</strong></p></td>
<td><p><strong>Description</strong></p></td>
<td><p><strong>Sphere X only?</strong></p></td>
</tr>
<tr>
<td><p><a href="AC" title="wikilink">AC</a></p></td>
<td><p>R</p></td>
<td><p>Returns the character's total defense.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ACTARG1" title="wikilink">ACTARG1</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's ACTARG1 value. X branch only: for
skills Enticement, Peacemaking and Provocation, if ACTARG1 is set to the
UID of the instrument to play, it will be played the sound of that
instrument.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ACTARG2" title="wikilink">ACTARG2</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's ACTARG2 value.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ACTARG3" title="wikilink">ACTARG3</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's ACTARG3 value.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ACTDIFF" title="wikilink">ACTDIFF</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the difficulty of the character's current
action.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ACTION" title="wikilink">ACTION</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the skill that the character is currently
using.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ACTP" title="wikilink">ACTP</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's ACTP value. Can get x,y,z,position
of the point in X branch.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ACTPRV" title="wikilink">ACTPRV</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's ACTPRV value.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ADDHOUSE_uid" title="wikilink">ADDHOUSE uid</a></p></td>
<td><p>W</p></td>
<td><p>X branch only. Adds the given uid to the player's house. If the
player current count of houses is greater than the limit he has, the
house will be redeeded.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ADDSHIP_uid" title="wikilink">ADDSHIP uid</a></p></td>
<td><p>W</p></td>
<td><p>X branch only. Adds the given uid to the player's ship. If the
player current count of ships is greater than the limit he has, the ship
will be redeeded.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="AFK" title="wikilink">AFK</a></p></td>
<td><p>W</p></td>
<td><p>Gets or sets whether or not the character is in AFK
mode.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="AGE" title="wikilink">AGE</a></p></td>
<td><p>R</p></td>
<td><p>Returns the age of the character since its creation, in
seconds.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ALLSKILLS" title="wikilink">ALLSKILLS</a>
<em>amount</em></p></td>
<td><p>W</p></td>
<td><p>Sets all of the character's skills to the specified
amount.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ANIM" title="wikilink">ANIM</a>
<em>anim_id</em></p></td>
<td><p>W</p></td>
<td><p>Plays the specified animation on the character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ATTACKER"
title="wikilink">ATTACKER</a><em>.properties</em></p></td>
<td><p>R</p></td>
<td><p>Gets the number of opponents who have damaged the
character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="BANK" title="wikilink">BANK</a> <em>layer</em></p></td>
<td><p>W</p></td>
<td><p>Opens the character's bank (or the container at the specified
layer) for SRC to view.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="BANKBALANCE" title="wikilink">BANKBALANCE</a></p></td>
<td><p>R</p></td>
<td><p>Returns the total amount of gold in the character's
bankbox.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="BARK" title="wikilink">BARK</a>
<em>sound_id</em></p></td>
<td><p>W</p></td>
<td><p>Plays the specified sound (or the character's generic sound if
not specified) to nearby clients from this character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="BODY" title="wikilink">BODY</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's body.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="BOUNCE" title="wikilink">BOUNCE</a>
<em>item_uid</em></p></td>
<td><p>W</p></td>
<td><p>Places a specified item in the character's backpack.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="BOW" title="wikilink">BOW</a></p></td>
<td><p>W</p></td>
<td><p>Makes the character bow to SRC.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="CAN_(Characters)" title="wikilink">CAN</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or Sets the Can flags for this chardef. Only readable in X
branch.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="CANCAST" title="wikilink">CANCAST</a> <em>spell_id,
check_antimagic</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the character can cast a given spell, bypassing
anti-magic field tests if <em>check_antimagic</em> set to 0.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="CANMAKE" title="wikilink">CANMAKE</a>
<em>item_id</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the character has the skills and resources to craft
a certain item.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="CANMAKESKILL" title="wikilink">CANMAKESKILL</a>
<em>item_id</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the character has the skills to craft a certain
item.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="CANMASK_(Characters)"
title="wikilink">CANMASK</a></p></td>
<td><p>RW</p></td>
<td><p>X branch only. Stores the CAN flags to be dynamically switched on
or off from the base CAN property.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="CANMOVE" title="wikilink">CANMOVE</a>
<em>direction</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the character can move in the given
direction.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="CANSEE" title="wikilink">CANSEE</a></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if SRC can see the character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="CANSEELOS" title="wikilink">CANSEELOS</a></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if SRC has line of sight to the character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="CANSEELOSFLAG" title="wikilink">CANSEELOSFLAG</a>
<em>flags</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if SRC has line of sight to the character, with flags
to modify what tests take place.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="COLOR" title="wikilink">COLOR</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's hue.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="CONSUME" title="wikilink">CONSUME</a>
<em>resource_list</em></p></td>
<td><p>W</p></td>
<td><p>Removes specified resources from SRC's backpack.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="COUNT" title="wikilink">COUNT</a></p></td>
<td><p>R</p></td>
<td><p>Returns the number of items equipped to the character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="CREATE" title="wikilink">CREATE</a></p></td>
<td><p>RW (R only on X)</p></td>
<td><p>Gets or sets the character's age since creation, in seconds
(Tenth of seconds on X).</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="CRIMINAL" title="wikilink">CRIMINAL</a></p></td>
<td><p>W</p></td>
<td><p>Sets whether or not the character is a criminal.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="CURFOLLOWER" title="wikilink">CURFOLLOWER</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the number of current followers the character
has,</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DAMAGE" title="wikilink">DAMAGE</a> <em>amount, type,
source</em></p></td>
<td><p>W</p></td>
<td><p>Inflicts damage upon the character.</p>
<p><code>When using COMBAT_ELEMENTAL_ENGINE add the following parameters after </code><em><code>source</code></em><code>: </code><em><code>physical</code></em><code>,</code><em><code>fire</code></em><code>,</code><em><code>cold</code></em><code>,</code><em><code>poison</code></em><code>,</code><em><code>energy</code></em><code>. All the values are in %.</code></p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DELHOUSE_uid" title="wikilink">DELHOUSE uid</a></p></td>
<td><p>W</p></td>
<td><p>X branch only. Deletes the given uid from the player's list (Will
not delete the house)(-1 clears the whole list).</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DELSHIP_uid" title="wikilink">DELSHIP uid</a></p></td>
<td><p>W</p></td>
<td><p>X branch only. Deletes the given uid from the player's list (Will
not delete the ship)(-1 clears the whole list).</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DESTROY" title="wikilink">DESTROY</a></p></td>
<td><p>W</p></td>
<td><p>Deletes the object, not stopped by a return 1 in <a
href="@Destroy" title="wikilink">@Destroy</a></p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DEX" title="wikilink">DEX</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's total dexterity.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DIALOG_(Function)" title="wikilink">DIALOG</a>
<em>dialog_id, page, parameters</em></p></td>
<td><p>W</p></td>
<td><p>Displays a dialog to SRC.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DIALOGCLOSE" title="wikilink">DIALOGCLOSE</a>
<em>dialog_id button</em></p></td>
<td><p>W</p></td>
<td><p>Closes a dialog that SRC has open, simulating a button
press.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DIALOGLIST"
title="wikilink">DIALOGLIST</a><em>.COUNT</em></p></td>
<td><p>R</p></td>
<td><p>Gets the number of number of dialogs currently considered to be
visible on SRC's screen.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DIALOGLIST"
title="wikilink">DIALOGLIST</a><em>.n.ID</em></p></td>
<td><p>R</p></td>
<td><p>Gets the ID of the nth dialog that SRC has open
(zero-based).</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DIALOGLIST"
title="wikilink">DIALOGLIST</a><em>.n.COUNT</em></p></td>
<td><p>R</p></td>
<td><p>Gets the number of instances of nth dialog SRC has open
(zero-based).</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DIR" title="wikilink">DIR</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or setes the direction that the character is
facing.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DISCONNECT" title="wikilink">DISCONNECT</a></p></td>
<td><p>W</p></td>
<td><p>Disconnects the character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DISMOUNT" title="wikilink">DISMOUNT</a></p></td>
<td><p>W</p></td>
<td><p>Dismounts the character from their ride.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DISPIDDEC" title="wikilink">DISPIDDEC</a></p></td>
<td><p>R</p></td>
<td><p>Gets the ID of the character as a decimal number.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DISTANCE" title="wikilink">DISTANCE</a>
<em>point_or_uid</em></p></td>
<td><p>R</p></td>
<td><p>Gets the distance between this object and either SRC, a map
location or another object.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DCLICK" title="wikilink">DCLICK</a></p></td>
<td><p>W</p></td>
<td><p>Double clicks the character, with SRC as the source of the
event.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DCLICK" title="wikilink">DCLICK</a>
<em>object_uid</em></p></td>
<td><p>W</p></td>
<td><p>Double clicks an object, with the character as SRC.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DRAWMAP" title="wikilink">DRAWMAP</a>
<em>radius</em></p></td>
<td><p>W</p></td>
<td><p>Starts the cartography skill, drawing a map of the local area up
to <em>radius</em> tiles.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DROP" title="wikilink">DROP</a>
<em>item_uid</em></p></td>
<td><p>W</p></td>
<td><p>Drops a specified item at the character's feet.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="DUPE" title="wikilink">DUPE</a></p></td>
<td><p>W</p></td>
<td><p>Creates a clone of the character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="EDIT" title="wikilink">EDIT</a></p></td>
<td><p>W</p></td>
<td><p>Displays an editing dialog for the character to SRC.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="EFFECT" title="wikilink">EFFECT</a> <em>type, item_id,
speed, loop, explode, color, rendermode</em></p></td>
<td><p>W</p></td>
<td><p>Displays an effect to nearby clients.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="EFFECTLOCATION" title="wikilink">EFFECTLOCATION</a>
<em>x,y,z,type,itemid,speed,loop,explode,color,render</em></p></td>
<td><p>W</p></td>
<td><p>Similar to the EFFECT command but instead of an object it takes a
terrain location as a target.</p></td>
<td><p>X</p></td>
</tr>
<tr>
<td><p><a href="EMOTE" title="wikilink">EMOTE</a>
<em>message</em></p></td>
<td><p>W</p></td>
<td><p>Displays a *You see* message to all nearby clients.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="EMOTEACT" title="wikilink">EMOTEACT</a></p></td>
<td><p>RW</p></td>
<td><p>Gets, sets or toggles whether or not the character will emote all
of its actions.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="EQUIP" title="wikilink">EQUIP</a>
<em>item_uid</em></p></td>
<td><p>W</p></td>
<td><p>Equips an item to the character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="EQUIPARMOR" title="wikilink">EQUIPARMOR</a></p></td>
<td><p>W</p></td>
<td><p>Equips the character with the best armour in their
backpack.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="EQUIPHALO" title="wikilink">EQUIPHALO</a>
<em>timeout</em></p></td>
<td><p>W</p></td>
<td><p>Equips a halo light to the character, lasting for
<em>timeout</em> tenths of a second.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="EQUIPWEAPON" title="wikilink">EQUIPWEAPON</a></p></td>
<td><p>W</p></td>
<td><p>Equips the character with the best weapon in their
backpack.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="EVENTS_(Property)" title="wikilink">EVENTS</a>
<em>event_defname</em></p></td>
<td><p>RW</p></td>
<td><p>Gets a list of events attached to the object, or adds or removes
an event to or from the object.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="EXP" title="wikilink">EXP</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's experience points.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="FACE" title="wikilink">FACE</a> <em>object_uid</em> (P
coords in X branch)</p></td>
<td><p>W</p></td>
<td><p>Turns the character to face a specified object or SRC. Admits
coordinates instead uid in X branch.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="FAME" title="wikilink">FAME</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's fame.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="FAME"
title="wikilink">FAME</a><em>.fame_group</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the character's fame falls within the specified fame
group.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="FCOUNT" title="wikilink">FCOUNT</a></p></td>
<td><p>R</p></td>
<td><p>Returns the total number of items equipped to the character,
including subitems</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="FLAGS" title="wikilink">FLAGS</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's flags.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="FIX" title="wikilink">FIX</a></p></td>
<td><p>W</p></td>
<td><p>Re-aligns the character's Z level to ground level.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="FIXWEIGHT" title="wikilink">FIXWEIGHT</a></p></td>
<td><p>W</p></td>
<td><p>Recalculates the character's total weight.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="FLIP" title="wikilink">FLIP</a></p></td>
<td><p>W</p></td>
<td><p>Rotates the character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="FONT" title="wikilink">FONT</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's speech font.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="FOOD" title="wikilink">FOOD</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's food level.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="FORGIVE" title="wikilink">FORGIVE</a></p></td>
<td><p>W</p></td>
<td><p>Revokes the character's jailed status.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="GETHOUSEPOS_uid" title="wikilink">GETHOUSEPOS
uid</a></p></td>
<td><p>R</p></td>
<td><p>Returns the position of the given UID on the houses list (-1 if
not found).</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="GETSHIPPOS_uid" title="wikilink">GETSHIPPOS
uid</a></p></td>
<td><p>R</p></td>
<td><p>Returns the position of the given UID on the ships list (-1 if
not found).</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="GO" title="wikilink">GO</a> <em>location</em></p></td>
<td><p>W</p></td>
<td><p>Teleports the character to the specified location.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="GOCHAR" title="wikilink">GOCHAR</a> <em>n</em></p></td>
<td><p>W</p></td>
<td><p>Teleports the character to the nth character in the
world.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="GOCHARID" title="wikilink">GOCHARID</a>
<em>character_defname</em></p></td>
<td><p>W</p></td>
<td><p>Teleports the character to the next characer in the world with
the specified <a href="BASEID" title="wikilink">BASEID</a></p></td>
<td></td>
</tr>
<tr>
<td><p><a href="GOCLI" title="wikilink">GOCLI</a> <em>n</em></p></td>
<td><p>W</p></td>
<td><p>Teleports the character to the nth online player.
(zero-based)</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="GOITEMID" title="wikilink">GOITEMID</a>
<em>item_defname</em></p></td>
<td><p>W</p></td>
<td><p>Teleports the character to the next item in the world with the
specified <a href="BASEID" title="wikilink">BASEID</a>.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="GOLD" title="wikilink">GOLD</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the amount of gold the character has.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="GONAME" title="wikilink">GONAME</a>
<em>name</em></p></td>
<td><p>W</p></td>
<td><p>Teleports the character to the next character or item in the
world with the specified name, accepts wildcards (*).</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="GOSOCK" title="wikilink">GOSOCK</a>
<em>socket</em></p></td>
<td><p>W</p></td>
<td><p>Teleports the character to the online player with the specified
socket number.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="GOTYPE" title="wikilink">GOTYPE</a>
<em>item_type</em></p></td>
<td><p>W</p></td>
<td><p>Teleports the character to the next item in the world with the
specified <a href="TYPE" title="wikilink">TYPE</a>.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="GOUID" title="wikilink">GOUID</a>
<em>object_uid</em></p></td>
<td><p>W</p></td>
<td><p>Teleports the character to the object with the specified <a
href="UID" title="wikilink">UID</a>.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="GUILDABBREV" title="wikilink">GUILDABBREV</a></p></td>
<td><p>R</p></td>
<td><p>Returns the character's guild abbreviation.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="HEAR" title="wikilink">HEAR</a> <em>text</em></p></td>
<td><p>W</p></td>
<td><p>For NPCs, acts as if SRC had spoken the specified <em>text</em>.
For players, displays <em>text</em> as a system message.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="HEIGHT" title="wikilink">HEIGHT</a></p></td>
<td><p>R</p></td>
<td><p>Gets the character's height.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="HITS" title="wikilink">HITS</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's hitpoints.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="HOME" title="wikilink">HOME</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's home location.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="HOUSE.n" title="wikilink">HOUSE.n</a></p></td>
<td><p>R</p></td>
<td><p>X branch only.Access the house in the Nth position, eg:
house.3.Redeed</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="HOUSES" title="wikilink">HOUSES</a></p></td>
<td><p>R</p></td>
<td><p>X branch only. Returns the number of houses on the player's
list.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="HUNGRY" title="wikilink">HUNGRY</a></p></td>
<td><p>W</p></td>
<td><p>Displays this character's hunger level to SRC.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ID" title="wikilink">ID</a></p></td>
<td><p>R</p></td>
<td><p>Gets the character's ID.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="INFO" title="wikilink">INFO</a></p></td>
<td><p>W</p></td>
<td><p>Displays an information dialog about the character to
SRC.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="INT" title="wikilink">INT</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's total intelligence.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="INVIS" title="wikilink">INVIS</a></p></td>
<td><p>W</p></td>
<td><p>Sets whether or not the character is invisible.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="INVUL" title="wikilink">INVUL</a></p></td>
<td><p>W</p></td>
<td><p>Sets whether or not the character is invulnerable.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISARMOR" title="wikilink">ISARMOR</a>
<em>object_uid</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the object is armour.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISCHAR" title="wikilink">ISCHAR</a></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the object is a character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISCONT" title="wikilink">ISCONT</a></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the object is a container.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISDIALOGOPEN" title="wikilink">ISDIALOGOPEN</a>
<em>dialog_id</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if SRC has the specified dialog visible on their
screen.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISEVENT"
title="wikilink">ISEVENT</a><em>.event_defname</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the object has an event attached to it.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISGM" title="wikilink">ISGM</a></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the character is in GM mode.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISINPARTY" title="wikilink">ISINPARTY</a></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the player is in a <a href="party"
title="wikilink">party</a>.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISITEM" title="wikilink">ISITEM</a></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the object is an item.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISMYPET" title="wikilink">ISMYPET</a></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the character belongs to SRC.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISNEARTYPE" title="wikilink">ISNEARTYPE</a> <em>type,
distance, flags</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if a nearby item has the given TYPE.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISNEARTYPETOP" title="wikilink">ISNEARTYPETOP</a>
<em>type, distance, flags</em></p></td>
<td><p>R</p></td>
<td><p>Returns a nearby world location of a nearby item which has the
given TYPE.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISONLINE" title="wikilink">ISONLINE</a></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the character is considered to be online.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISPLAYER" title="wikilink">ISPLAYER</a></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the object is a player.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISSTUCK" title="wikilink">ISSTUCK</a></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the character cannot walk in any direction.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISTEVENT"
title="wikilink">ISTEVENT</a><em>.event_defname</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the object has an event attached to its <a
href="CHARDEF" title="wikilink">CHARDEF</a>.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISTIMERF"
title="wikilink">ISTIMERF</a><em>.function</em></p></td>
<td><p>R</p></td>
<td><p>Returns the number of seconds left on the specified timerf if it
exists.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISVENDOR" title="wikilink">ISVENDOR</a></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the character is a vendor.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISVERTICALSPACE" title="wikilink">ISVERTICALSPACE</a>
<em>location</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the ceiling at the given location is high enough for
the character to fit under.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ISWEAPON" title="wikilink">ISWEAPON</a>
<em>object_uid</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the object is a weapon.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="JAIL" title="wikilink">JAIL</a> <em>cell</em></p></td>
<td><p>W</p></td>
<td><p>Sends the character to jail, to a specified jail cell.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="KARMA" title="wikilink">KARMA</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's karma.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="KARMA"
title="wikilink">KARMA</a><em>.karma_group</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the character's karma falls within the specified
karma group.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="KILL" title="wikilink">KILL</a></p></td>
<td><p>W</p></td>
<td><p>Kills the character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="LEVEL" title="wikilink">LEVEL</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's experience level.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="LIGHT" title="wikilink">LIGHT</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's personal light level.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="LUCK" title="wikilink">LUCK</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the luck value for the character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MAKEITEM" title="wikilink">MAKEITEM</a>
<em>item_defname, amount</em></p></td>
<td><p>| W</p></td>
<td><p>Begins an attempt to craft the specified quantity of the given
item.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MANA" title="wikilink">MANA</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's mana.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MAP" title="wikilink">MAP</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the map that this object is located.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MAPWAYPOINT" title="wikilink">MAPWAYPOINT</a>
"ObjectUID, WaypointType"</p></td>
<td><p>W</p></td>
<td><p>Add/remove waypoints on client radar map (enhanced clients
only).</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MAXFOLLOWER" title="wikilink">MAXFOLLOWER</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the maximum number of followers the character can
have.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MAXHITS" title="wikilink">MAXHITS</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's maximum hitpoints.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MAXHOUSES" title="wikilink">MAXHOUSES</a></p></td>
<td><p>RW</p></td>
<td><p>Added to Accounts and Chars, when created they read this setting
from the sphere.ini (if values on sphere.ini change, they will not
reflect on already created accounts/chars).</p></td>
<td><p>X</p></td>
</tr>
<tr>
<td><p><a href="MAXMANA" title="wikilink">MAXMANA</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's maximum mana.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MAXSHIPS" title="wikilink">MAXSHIPS</a></p></td>
<td><p>RW</p></td>
<td><p>Added Accounts and Chars, when created they read this new setting
from the sphere.ini (if values on sphere.ini change, they will not
reflect on already created accounts/chars).</p></td>
<td><p>X</p></td>
</tr>
<tr>
<td><p><a href="MAXSTAM" title="wikilink">MAXSTAM</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's maximum stamina.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MAXWEIGHT" title="wikilink">MAXWEIGHT</a></p></td>
<td><p>R</p></td>
<td><p>Returns the maximum weight that the character can carry.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MEMORY"
title="wikilink">MEMORY</a><em>.object_uid</em></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the memory flags the character has for the given
object.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MENU_(Function)" title="wikilink">MENU</a>
<em>menu_defname</em></p></td>
<td><p>W</p></td>
<td><p>Displays a menu to SRC.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MESSAGE" title="wikilink">MESSAGE</a>
<em>message</em></p></td>
<td><p>W</p></td>
<td><p>Displays a message above this character to SRC.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MESSAGEUA" title="wikilink">MESSAGEUA</a> <em>colour,
talkmode, font, lang_id, message</em></p></td>
<td><p>W</p></td>
<td><p>Displays a UNICODE message above this character to SRC.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MODAR" title="wikilink">MODAR</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets a modifier for the character's armour
rating.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MODDEX" title="wikilink">MODDEX</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's dexterity modifier.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MODINT" title="wikilink">MODINT</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's intelligence modifier.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MODMAXWEIGHT" title="wikilink">MODMAXWEIGHT</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's maximum weight modifier.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MODSTR" title="wikilink">MODSTR</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's strength modifier.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MOUNT" title="wikilink">MOUNT</a></p></td>
<td><p>R</p></td>
<td><p>Gets the UID of the character's mount.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MOUNT" title="wikilink">MOUNT</a>
<em>mount_uid</em></p></td>
<td><p>W</p></td>
<td><p>Attempts to mount the character on to the specified
mount.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MOVE" title="wikilink">MOVE</a>
<em>direction</em></p></td>
<td><p>R</p></td>
<td><p>Returns the movement flags for the tile in the given direction
(see can_flags in sphere_defs.scp).</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MOVE" title="wikilink">MOVE</a> <em>direction,
amount</em><br />
<a href="MOVE" title="wikilink">MOVE</a> <em>x y</em></p></td>
<td><p>W</p></td>
<td><p>Moves the object relative to its current position.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MOVENEAR" title="wikilink">MOVENEAR</a> <em>object_uid,
distance</em></p></td>
<td><p>W</p></td>
<td><p>Moves the character to a random location near another object
within a certain distance.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="MOVETO" title="wikilink">MOVETO</a>
<em>location</em></p></td>
<td><p>W</p></td>
<td><p>Moves the character to a specific location.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="NAME" title="wikilink">NAME</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's name.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="NEWBIESKILL" title="wikilink">NEWBIESKILL</a>
<em>skill_id</em></p></td>
<td><p>W</p></td>
<td><p>Distributes items that are associated with the specified skill,
to the character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="NEWGOLD" title="wikilink">NEWGOLD</a>
<em>amount</em></p></td>
<td><p>W</p></td>
<td><p>Generates <em>amount</em> gold in the character's
backpack.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="NEWLOOT" title="wikilink">NEWLOOT</a>
<em>item_or_template_defname</em></p></td>
<td><p>W</p></td>
<td><p>Generates the specified item or template into the character's
backpack, providing that they are an NPC that hasn't been
summoned.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="NIGHTSIGHT" title="wikilink">NIGHTSIGHT</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets whether or not the character has nightsight
enabled.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="NOTOGETFLAG" title="wikilink">NOTOGETFLAG</a>
<em>viewer_uid, allow_incognito</em></p></td>
<td><p>RW</p></td>
<td><p>Gets the character's notoriety flags as seen by the specified
viewer.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="NPC" title="wikilink">NPC</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's AI type.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="NUDGEDOWN" title="wikilink">NUDGEDOWN</a>
<em>amount</em></p></td>
<td><p>W</p></td>
<td><p>Decreases the character's Z level.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="NUDGEUP" title="wikilink">NUDGEUP</a>
<em>amount</em></p></td>
<td><p>W</p></td>
<td><p>Increases the characer's Z level.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="OBODY" title="wikilink">OBODY</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's original body.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="OPENPAPERDOLL"
title="wikilink">OPENPAPERDOLL</a></p></td>
<td><p>W</p></td>
<td><p>Displays the character's paperdoll to SRC.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="OPENPAPERDOLL" title="wikilink">OPENPAPERDOLL</a>
<em>character_uid</em></p></td>
<td><p>W</p></td>
<td><p>Displays a specified character's paperdoll to this
character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="OSKIN" title="wikilink">OSKIN</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's original colour.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="ODEX" title="wikilink">ODEX</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's base dexterity (without
modifiers).</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="OINT" title="wikilink">OINT</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's base intelligence (without
modifiers).</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="OSTR" title="wikilink">OSTR</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's base strength (without
modifiers).</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="PACK" title="wikilink">PACK</a></p></td>
<td><p>W</p></td>
<td><p>Opens the character's backpack for SRC to view.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="POISON" title="wikilink">POISON</a>
<em>strength</em></p></td>
<td><p>W</p></td>
<td><p>Poisons the character, with the specified poison
strength.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="POLY" title="wikilink">POLY</a>
<em>character_id</em></p></td>
<td><p>W</p></td>
<td><p>Begins casting the polymorph spell, with <em>character_id</em>
being the character to turn into.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="PROMPTCONSOLE" title="wikilink">PROMPTCONSOLE</a>
<em>function, prompt_message</em></p></td>
<td><p>W</p></td>
<td><p>Displays a prompt message to SRC and passes their response into a
specified function.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="PROMPTCONSOLEU" title="wikilink">PROMPTCONSOLEU</a>
<em>function, prompt_message</em></p></td>
<td><p>W</p></td>
<td><p>Displays a prompt message to SRC and passes their response into a
specified function, supporting UNICODE response.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="PRIVSET" title="wikilink">PRIVSET</a>
<em>plevel</em></p></td>
<td><p>W</p></td>
<td><p>Sets the PLEVEL of the character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="RANGE" title="wikilink">RANGE</a></p></td>
<td><p>R</p></td>
<td><p>Gets the combat range of the character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="RELEASE" title="wikilink">RELEASE</a></p></td>
<td><p>W</p></td>
<td><p>Clears the character's owners.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="REMOVE" title="wikilink">REMOVE</a>
<em>allow_player_removal</em></p></td>
<td><p>W</p></td>
<td><p>Deletes the character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="REMOVEFROMVIEW"
title="wikilink">REMOVEFROMVIEW</a></p></td>
<td><p>W</p></td>
<td><p>Removes the object from nearby clients' screens.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="RESCOLD" title="wikilink">RESCOLD</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's resistance to cold.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="RESCOLDMAX" title="wikilink">RESCOLDMAX</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's maximum resistance to cold.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="RESCOUNT" title="wikilink">RESCOUNT</a>
<em>item_defname</em></p></td>
<td><p>R</p></td>
<td><p>Returns the total amount of a specific item equipped to the
character or inside their baackpack.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="RESENDTOOLTIP" title="wikilink">RESENDTOOLTIP</a>
<em>sendfull</em>,<em>usecache</em></p></td>
<td><p>W</p></td>
<td><p>Forces Sphere to update the tooltips for nearby clients. If
sendfull is 1 the entire tooltip is sent and if 0 then just the header
is sent. If usecache is 1 then the cached version (if found) will be
sent and if 0 then the cached version (if found) will be replaced and
sent</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="RESENERGY" title="wikilink">RESENERGY</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's resistance to energy.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="RESENERGYMAX" title="wikilink">RESENERGYMAX</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's maximum resistance to
energy.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="RESFIRE" title="wikilink">RESFIRE</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's resistance to fire.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="RESFIREMAX" title="wikilink">RESFIREMAX</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's maximum resistance to fire.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="RESPOISON" title="wikilink">RESPOISON</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's resistance to poison.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="RESPOISONMAX" title="wikilink">RESPOISONMAX</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's maximum resistance to
poison.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="RESTEST" title="wikilink">RESTEST</a>
<em>item_list</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if all of the items in the list can be found equipped
to the character or inside their backpack.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="RESURRECT" title="wikilink">RESURRECT</a>
<em>force</em></p></td>
<td><p>W</p></td>
<td><p>Resurrects the character. If <em>force</em> is 1 then usual
anti-magic checks are bypasses.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SALUTE" title="wikilink">SALUTE</a>
<em>object_uid</em></p></td>
<td><p>W</p></td>
<td><p>Makes the character salute a specified object or SRC.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SAY" title="wikilink">SAY</a> <em>message</em></p></td>
<td><p>W</p></td>
<td><p>Makes the character speak a message.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SAYU" title="wikilink">SAYU</a>
<em>message</em></p></td>
<td><p>W</p></td>
<td><p>Makes the character speak a UTF-8 message</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SAYUA" title="wikilink">SAYUA</a> <em>colour, talkmode,
font, lang_id, text</em></p></td>
<td><p>W</p></td>
<td><p>MAkes the character speak a UNICODE message.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SDIALOG" title="wikilink">SDIALOG</a> <em>dialog_id,
page, parameters</em></p></td>
<td><p>W</p></td>
<td><p>Displays a dialog to SRC, providing that it is not already
open.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SERIAL" title="wikilink">SERIAL</a></p></td>
<td><p>R</p></td>
<td><p>Gets the item's unique ID in the world.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SEX" title="wikilink">SEX</a>
<em>value_male:value_female</em></p></td>
<td><p>R</p></td>
<td><p>Returns <em>value_male</em> or <em>value_female</em> depending on
the character's gender.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SEXTANTP" title="wikilink">SEXTANTP</a>
<em>location</em></p></td>
<td><p>R</p></td>
<td><p>Converts the character's location or a specified location into
sextant coordinates.</p></td>
<td></td>
</tr>
<tr>
<td><p><em>skill_name</em></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's skill level in
<em>skill_name</em>.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SHIP.n" title="wikilink">SHIP.n</a></p></td>
<td><p>R</p></td>
<td><p>X branch only. Added to access the ship in the Nth position, eg:
ship.3.Redeed</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SHIPS" title="wikilink">SHIPS</a></p></td>
<td><p>R</p></td>
<td><p>X branch only. Return the ships on the player's list.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SKILL_(Function)" title="wikilink">SKILL</a></p></td>
<td><p>W</p></td>
<td><p>Begins using a skill.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SKILLADJUSTED"
title="wikilink">SKILLADJUSTED</a>."number or skill_name" (X branch
only)</p></td>
<td><p>R</p></td>
<td><p>Returns the skill value adjusted by the stat bonus. Example
“SkillAdjusted.1” or “SkillAdjusted.Anatomy”.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SKILLCHECK" title="wikilink">SKILLCHECK</a>
<em>skill_id, difficulty</em></p></td>
<td><p>R</p></td>
<td><p>Performs a check for skill success, returning 1 if the attempt
was successful.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SKILLBEST"
title="wikilink">SKILLBEST</a><em>.n</em></p></td>
<td><p>R</p></td>
<td><p>Returns the ID of the character's nth highest skill (0 =
Highest)</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SKILLGAIN" title="wikilink">SKILLGAIN</a> <em>skill,
difficulty</em></p></td>
<td><p>W</p></td>
<td><p>Invokes Sphere's skill gain for the specified skill, with the
given difficulty (0-100)</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SKILLTEST" title="wikilink">SKILLTEST</a>
<em>skill_list</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if the character possess all of the skills in the
list.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SKILLTOTAL" title="wikilink">SKILLTOTAL</a></p></td>
<td><p>R</p></td>
<td><p>Returns the total value of all the character's skills.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SKILLTOTAL" title="wikilink">SKILLTOTAL</a>
<em>skill_group</em></p></td>
<td><p>R</p></td>
<td><p>Returns the total value of all the character's skills with the
specified group flag(s).</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SKILLTOTAL" title="wikilink">SKILLTOTAL</a>
<em>-amount</em></p></td>
<td><p>R</p></td>
<td><p>Returns the total value of all the character's skills that are
under <em>amount</em>.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SKILLTOTAL" title="wikilink">SKILLTOTAL</a>
<em>+amount</em></p></td>
<td><p>R</p></td>
<td><p>Returns the total value of all the character's skills that are
over <em>amount</em>.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SKILLUSEQUICK" title="wikilink">SKILLUSEQUICK</a>
<em>skill_id, difficulty</em></p></td>
<td><p>R</p></td>
<td><p>Quickly uses a skill, returning 1 if the attempt was
successful.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SLEEP" title="wikilink">SLEEP</a>
<em>fall_forwards</em></p></td>
<td><p>W</p></td>
<td><p>Makes the character appear to sleep.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SOUND" title="wikilink">SOUND</a> <em>sound_id,
repeat</em></p></td>
<td><p>W</p></td>
<td><p>Plays a sound from this character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SPELLEFFECT" title="wikilink">SPELLEFFECT</a>
<em>spell_id, strength, source_character_uid,
source_item_uid</em></p></td>
<td><p>W</p></td>
<td><p>Causes the character to be affected by a spell.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SPEECHCOLOROVERRIDE"
title="wikilink">SPEECHCOLOROVERRIDE</a> <em>value</em></p></td>
<td><p>RW</p></td>
<td><p>Override client speech hue.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="STAM" title="wikilink">STAM</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's stamina.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="STEPSTEALTH" title="wikilink">STEPSTEALTH</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the amount of steps a character can do while using
the Stealth skill.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="STONE" title="wikilink">STONE</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets whether or not the character is trapped in
stone.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="STR" title="wikilink">STR</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's total strength.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SUICIDE" title="wikilink">SUICIDE</a></p></td>
<td><p>W</p></td>
<td><p>Forces the character to commit suicide.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SUMMONCAGE" title="wikilink">SUMMONCAGE</a></p></td>
<td><p>W</p></td>
<td><p>Teleports the character to SRC's, surrounded by a cage
multi.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="SUMMONTO" title="wikilink">SUMMONTO</a></p></td>
<td><p>W</p></td>
<td><p>Teleports the character to SRC's position.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="TAG" title="wikilink">TAG</a><em>.name</em></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the value of a TAG.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="TAGAT"
title="wikilink">TAGAT</a><em>.index</em></p></td>
<td><p>R</p></td>
<td><p>Gets a TAG at the given zero-based index.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="TAGAT"
title="wikilink">TAGAT</a><em>.index</em>.KEY</p></td>
<td><p>R</p></td>
<td><p>Gets the name of the TAG at the given zero-based index.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="TAGAT"
title="wikilink">TAGAT</a><em>.index</em>.VAL</p></td>
<td><p>R</p></td>
<td><p>Gets the value of the TAG at the given zero-based index.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="TAGCOUNT" title="wikilink">TAGCOUNT</a></p></td>
<td><p>R</p></td>
<td><p>Gets the number of TAGs stored on the item.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="TAGLIST" title="wikilink">TAGLIST</a></p></td>
<td><p>W</p></td>
<td><p>Outputs a list of the object's TAGs.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="TARGET" title="wikilink">TARGET</a><em>FGMW</em>
<em>function</em></p></td>
<td><p>W</p></td>
<td><p>Displays a targeting cursor to SRC.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="TIMER" title="wikilink">TIMER</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the length of time before the item's timer expires,
in seconds.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="TIMERD" title="wikilink">TIMERD</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the length of time before the item's timer expires,
in tenths of a second.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="TIMERF" title="wikilink">TIMERF</a> <em>time,
function</em></p></td>
<td><p>W</p></td>
<td><p>Scheduled a function to be executed on this object in
<em>time</em> seconds.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="TIMERF" title="wikilink">TIMERF</a>
<em>CLEAR</em></p></td>
<td><p>W</p></td>
<td><p>Clears all scheduled functions from the character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="TIMERF" title="wikilink">TIMERF</a> <em>STOP,
function</em></p></td>
<td><p>W</p></td>
<td><p>Stops the specified function from the character. (On X version
wild character * is available for defining the function name or the
argument)</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="TIMERMS" title="wikilink">TIMERMS</a></p></td>
<td><p>W</p></td>
<td><p>Set an object timer to elapse after the given number of
milliseconds.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="TITHING" title="wikilink">TITHING</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the number of tithing points the character
has.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="TITLE" title="wikilink">TITLE</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's title.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="TOWNABBREV" title="wikilink">TOWNABBREV</a></p></td>
<td><p>R</p></td>
<td><p>Returns the character's town abbreviation.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="TRIGGER" title="wikilink">TRIGGER</a> <em>trig_name,
trig_type</em></p></td>
<td><p>R</p></td>
<td><p>Fires a custom trigger and returns the RETURN value.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="UID" title="wikilink">UID</a></p></td>
<td><p>R</p></td>
<td><p>Gets the item's unique ID in the world.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="UNDERWEAR" title="wikilink">UNDERWEAR</a></p></td>
<td><p>W</p></td>
<td><p>Toggles the display of underwear on the character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="UNEQUIP" title="wikilink">UNEQUIP</a>
<em>item_uid</em></p></td>
<td><p>W</p></td>
<td><p>Unequips an item from the character, placing it in their
backpack.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="UPDATE" title="wikilink">UPDATE</a></p></td>
<td><p>W</p></td>
<td><p>Updates the state of the character to nearby clients.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="UPDATEX" title="wikilink">UPDATEX</a></p></td>
<td><p>W</p></td>
<td><p>Updates the state of the character to nearby clients, removing it
from their view first to ensure a full refresh.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="USEITEM" title="wikilink">USEITEM</a></p></td>
<td><p>W</p></td>
<td><p>Double clicks the character, with SRC as the source of the event,
without checking for line of sight.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="USEITEM" title="wikilink">USEITEM</a>
<em>object_uid</em></p></td>
<td><p>W</p></td>
<td><p>Double clicks an object, with the character as SRC.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="VISUALRANGE" title="wikilink">VISUALRANGE</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the character's sight range.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="WEIGHT" title="wikilink">WEIGHT</a></p></td>
<td><p>R</p></td>
<td><p>Gets the weight of the character.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="WHERE" title="wikilink">WHERE</a></p></td>
<td><p>W</p></td>
<td><p>Describes the character's location to SRC.</p></td>
<td></td>
</tr>
<tr>
<td><p><a href="Z" title="wikilink">Z</a></p></td>
<td><p>R</p></td>
<td><p>Gets the Z position of the character.</p></td>
<td></td>
</tr>
</tbody>
</table>

## Triggers

Here is a list of all character triggers. Click on the trigger name for
more detailed information such as arguments and examples.

|  |  |  |
|----|----|----|
| **Name** | **Description** | **Sphere X only?** |
| [@AfterClick](@AfterClick "wikilink") | Fires when the object has been single-clicked, just before the overhead name is shown. |  |
| [@Attack](@Attack "wikilink") | Fires when the character begins attacking another. |  |
| [@CallGuards](@CallGuards "wikilink") | Fires when the character calls for guards. |  |
| [@CharAttack](@CharAttack "wikilink") | Fires when the character is attacked by another character. |  |
| [@CharClick](@CharClick "wikilink") | Fires when the character is clicked by another character. |  |
| [@CharClientTooltip](@CharClientTooltip "wikilink") | Fires when the tooltips are about to be sent to the character. |  |
| [@CharDClick](@CharDClick "wikilink") | Fires when the character double clicks another character. |  |
| [@CharTradeAccepted](@CharTradeAccepted "wikilink") | Fires when another character accepts trade with the character. |  |
| [@Click](@Click "wikilink") | Fires when the object has been single-clicked. |  |
| [@ClientTooltip](@ClientTooltip "wikilink") | Fires when tooltips for this character are about to be sent to a client. |  |
| [@CombatAdd](@CombatAdd "wikilink") | Fires when someone is being added to my attacker list. |  |
| [@CombatDelete](@CombatDelete "wikilink") | Fires when someone is deleted from my attacker list. |  |
| [@CombatEnd](@CombatEnd "wikilink") | Fires when someone is being deleted from my attacker list and I don't have any more viable targets. |  |
| [@CombatStart](@CombatStart "wikilink") | Fires when adding first attacker to my list. |  |
| [@ContextMenuRequest](@ContextMenuRequest "wikilink") | Fires when a client requests the context menu options for the object. |  |
| [@ContextMenuSelect](@ContextMenuSelect "wikilink") | Fires when a client selects a context menu option for the object. |  |
| [@Create](@Create "wikilink") | Fires when the object is initially created, before it is placed in the world. |  |
| [@Criminal](@Criminal "wikilink") | Fires when the character becomes a criminal. |  |
| [@DClick](@DClick "wikilink") | Fires when the object is double-clicked. |  |
| [@Death](@Death "wikilink") | Fires when the character's hitpoints reaches zero. |  |
| [@DeathCorpse](@DeathCorpse "wikilink") | Fires when a corpse is created for the character. |  |
| [@Destroy](@Destroy "wikilink") | Fires when the object is being deleted. |  |
| [@Dismount](@Dismount "wikilink") | Fires when the character dismounts their ride. |  |
| [@Dye](@Dye "wikilink") | Fires when the character is about to change their color or the color of an object. |  |
| [@Eat](@Eat "wikilink") | Fires when the character eats something. |  |
| [@EnvironChange](@EnvironChange "wikilink") | Fires when the environment changes for the character. |  |
| [@ExpChange](@ExpChange "wikilink") | Fires when the character's experience points change. |  |
| [@ExpLevelChange](@ExpLevelChange "wikilink") | Fires when the character's experience level changes. |  |
| [@FameChange](@FameChange "wikilink") | Fires when the character's fame changes. |  |
| [@GetHit](@GetHit "wikilink") | Fires when the character receives damage. |  |
| [@Hit](@Hit "wikilink") | Fires when the character hits another in combat. |  |
| [@HitMiss](@HitMiss "wikilink") | Fires when the character fails to hit another in combat. |  |
| [@HitParry](@HitParry "wikilink") | X branch only. Fires when the character is attempting to parry a hit. | X |
| [@HitTry](@HitTry "wikilink") | Fires when the character tries to hit another in combat. |  |
| [@HouseDesignCommit](@HouseDesignCommit "wikilink") | Fires when the character commits a new house design. |  |
| [@HouseDesignExit](@HouseDesignExit "wikilink") | Fires when the character exits house design mode. |  |
| [@Hunger](@Hunger "wikilink") | Fires when the character's food level decreases. |  |
| [@ItemAfterClick](@ItemAfterClick "wikilink") | Fires when the character single-clicks an item, just before the overhead name is shown. |  |
| [@ItemBuy](@ItemBuy "wikilink") | Fires when the character buys an item from a vendor. |  |
| [@ItemClick](@ItemClick "wikilink") | Fires when the character single-clicks an item. |  |
| [@ItemClientTooltip](@ItemClientTooltip "wikilink") | Fires when the tooltips are about to be sent to the client for an item. |  |
| [@ItemContextMenuRequest](@ItemContextMenuRequest "wikilink") | Fires when the character requests the context menu options for an item. |  |
| [@ItemContextMenuSelect](@ItemContextMenuSelect "wikilink") | Fires when the character selects a context menu option for an item. |  |
| [@ItemCreate](@ItemCreate "wikilink") | Fires when an item is initially created, before it is placed in the world, and the character is in some way responsible for it. |  |
| [@ItemDamage](@ItemDamage "wikilink") | Fires when the character damages an item. |  |
| [@ItemDClick](@ItemDClick "wikilink") | Fires when the character double-clicks an item. |  |
| [@ItemDropOn_Char](@ItemDropOn_Char "wikilink") | Fires when the character drops an item on to a character. |  |
| [@ItemDropOn_Ground](@ItemDropOn_Ground "wikilink") | Fires when the character drops an item on to the ground. |  |
| [@ItemDropOn_Item](@ItemDropOn_Item "wikilink") | Fires when the character drops an item on to another item. |  |
| [@ItemDropOn_Self](@ItemDropOn_Self "wikilink") | Fires when the character drops an item inside another item. |  |
| [@ItemEquip](@ItemEquip "wikilink") | Fires when the character equips an item. |  |
| [@ItemEquipTest](@ItemEquipTest "wikilink") | Fires when the characer is about to equip an item. |  |
| [@ItemPickUp_Ground](@ItemPickUp_Ground "wikilink") | Fires when the character picks an item up from the ground. |  |
| [@ItemPickUp_Pack](@ItemPickUp_Pack "wikilink") | Fires when the character picks an item up from inside a container. |  |
| [@ItemPickUp_Self](@ItemPickUp_Self "wikilink") | Fires when the character picks an item up from inside another item. |  |
| [@ItemPickUp_Stack](@ItemPickUp_Stack "wikilink") | Fires when the character picks up an item from a stack. |  |
| [@ItemSell](@ItemSell "wikilink") | Fires when the character sells an item to a vendor. |  |
| [@ItemSmelt](@ItemSmelt "wikilink") | Fires when the character smelt an item. | X |
| [@ItemSpellEffect](@ItemSpellEffect "wikilink") | Fires when the character hits an item with a spell. |  |
| [@ItemStep](@ItemStep "wikilink") | Fires when the character steps on an item. |  |
| [@ItemTargOn_Cancel](@ItemTargOn_Cancel "wikilink") | Fires when the character cancels an item's target cursor. |  |
| [@ItemTargOn_Char](@ItemTargOn_Char "wikilink") | Fires when the character targets a character with an item's target cursor. |  |
| [@ItemTargOn_Ground](@ItemTargOn_Ground "wikilink") | Fires when the character targets the ground with an item's target cursor. |  |
| [@ItemTargOn_Item](@ItemTargOn_Item "wikilink") | Fires when the character targets an item with an item's target cursor. |  |
| [@ItemToolTip](@ItemToolTip "wikilink") | Fires when the character requests old-style tooltips for an item. |  |
| [@ItemUnEquip](@ItemUnEquip "wikilink") | Fires when the character unequips an item. |  |
| [@Jailed](@Jailed "wikilink") | Fires when the character is sent to jail. |  |
| [@KarmaChange](@KarmaChange "wikilink") | Fires when the character's karma changes. |  |
| [@Kill](@Kill "wikilink") | Fires when the character kills another character. |  |
| [@Login](@Login "wikilink") | Fires when the character logs in. |  |
| [@Logout](@Logout "wikilink") | Fires when the character logs out. |  |
| [@Mount](@Mount "wikilink") | Fires when the character mounts a ride. |  |
| [@MurderDecay](@MurderDecay "wikilink") | Fires when one of the character's kills is about to decay. |  |
| [@MurderMark](@MurderMark "wikilink") | Fires when the character is about to gain a kill. |  |
| [@NotoSend](@NotoSend "wikilink") | Fires the status bar/character notoriety color is sent to another players. |  |
| [@NPCAcceptItem](@NPCAcceptItem "wikilink") | Fires when the NPC receives an item. |  |
| [@NpcActCast](@NpcActCast "wikilink") | Fires when the NPC is selecting the spell to cast. | X |
| [@NPCActFight](@NPCActFight "wikilink") | Fires when the NPC makes a combat decision. |  |
| [@NPCActFollow](@NPCActFollow "wikilink") | Fires when the NPC follows another character. |  |
| [@NPCAction](@NPCAction "wikilink") | Fires when the NPC is about to perform an AI action. |  |
| [@NPCActWander](@NPCActWander "wikilink") | X branch only. Fires each step an NPC does while wandering. |  |
| [@NPCHearGreeting](@NPCHearGreeting "wikilink") | Fires when the NPC hears a character for the first time. |  |
| [@NPCHearUnknown](@NPCHearUnknown "wikilink") | Fires when the NPC hears something they don't understand. |  |
| [@NPCLookAtChar](@NPCLookAtChar "wikilink") | Fires then the NPC looks at a character. |  |
| [@NPCLookAtItem](@NPCLookAtItem "wikilink") | Fires when the NPC looks at an item. |  |
| [@NPCLostTeleport](@NPCLostTeleport "wikilink") | Fires when the NPC is lost and is about to be teleported back to their [HOME](HOME "wikilink"). |  |
| [@NPCRefuseItem](@NPCRefuseItem "wikilink") | Fires when the NPC refuses an item being given to them. |  |
| [@NPCRestock](@NPCRestock "wikilink") | Fires when the NPC is having their items restocked. |  |
| [@NPCSeeNewPlayer](@NPCSeeNewPlayer "wikilink") | Fires when the NPC first sees a player. |  |
| [@NPCSeeWantItem](@NPCSeeWantItem "wikilink") | Fires when the NPC sees an item they want. |  |
| [@NPCSpecialAction](@NPCSpecialAction "wikilink") | Fires when the NPC is about to perform a special action (leaving fire trail, dropping web). |  |
| [@PayGold](@PayGold "wikilink") | Fires when the character receives a payment. (Experimental Build Only) |  |
| [@PersonalSpace](@PersonalSpace "wikilink") | Fires when the character is stepped on. |  |
| [@PetDesert](@PetDesert "wikilink") | Fires when the character deserts its owner. |  |
| [@Profile](@Profile "wikilink") | Fires when a player attempts to read the character's profile from the paperdoll. |  |
| [@ReceiveItem](@ReceiveItem "wikilink") | Fires when the NPC receives an item from another character, before they decide if they want it or not. |  |
| [@RegenStat](@RegenStat "wikilink") | Fires when a character is going to regenerate any stat point. |  |
| [@RegionEnter](@RegionEnter "wikilink") | Fires when the character enters a region. |  |
| [@RegionLeave](@RegionLeave "wikilink") | Fires when the character leaves a region. |  |
| [@RegionResourceFound](@RegionResourceFound "wikilink") | Fires after a resource has been selected and the resource bit has been created. |  |
| [@Rename](@Rename "wikilink") | Fires when the character renames another. |  |
| [@Resurrect](@Resurrect "wikilink") | Fires when the character is being resurrected. |  |
| [@SeeCrime](@SeeCrime "wikilink") | Fires when the character sees a crime take place. |  |
| [@SeeHidden](@SeeHidden "wikilink") | Fires when this character is about to see a hidden character. |  |
| [@SkillAbort](@SkillAbort "wikilink") | Fires when the character aborts a skill. |  |
| [@SkillChange](@SkillChange "wikilink") | Fires when the character's skill level changes. |  |
| [@SkillFail](@SkillFail "wikilink") | Fires when the character fails a skill. |  |
| [@SkillGain](@SkillGain "wikilink") | Fires when the character has a chance to gain in a skill. |  |
| [@SkillMakeItem](@SkillMakeItem "wikilink") | Fires when the character crafts an item. |  |
| [@SkillMenu](@SkillMenu "wikilink") | Fires when a skill menu is shown to the character. |  |
| [@SkillPreStart](@SkillPreStart "wikilink") | Fires when the character starts a skill, before any hardcoded action takes place. |  |
| [@SkillSelect](@SkillSelect "wikilink") | Fires when the character selects a skill on their skill menu. |  |
| [@SkillStart](@SkillStart "wikilink") | Fires when the character starts a skill. |  |
| [@SkillSuccess](@SkillSuccess "wikilink") | Fires when the character succeeds at a skill. |  |
| [@SkillUseQuick](@SkillUseQuick "wikilink") | Fires when the character quickly uses a skill. |  |
| [@SkillWait](@SkillWait "wikilink") | Fires when Sphere wants to check if a character must wait before starting a skill. |  |
| [@SpellBook](@SpellBook "wikilink") | Fires when the character opens their spellbook. |  |
| [@SpellCast](@SpellCast "wikilink") | Fires when the character casts a spell. |  |
| [@SpellEffect](@SpellEffect "wikilink") | Fires when the character is hit by the effects of a spell. |  |
| [@SpellEffectAdd](@SpellEffectAdd "wikilink") | Fires when a spell memory is added to the character. | X |
| [@SpellEffectRemove](@SpellEffectRemove "wikilink") | Fires the spell memory is removed from the character. | X |
| [@SpellEffectTick](@SpellEffectTick "wikilink") | Fires when the character is hit the effect of a periodic spell (like Poison spell). | X |
| [@SpellFail](@SpellFail "wikilink") | Fires when the character fails to cast a spell. |  |
| [@SpellSelect](@SpellSelect "wikilink") | Fires when the character selects a spell to cast. |  |
| [@SpellSuccess](@SpellSuccess "wikilink") | Fires when the character successfully casts a spell. |  |
| [@SpellTargetCancel](@SpellTargetCancel "wikilink") | Fires when the character cancels target selection for a spell they have just cast. |  |
| [@StatChange](@StatChange "wikilink") | Fires when the character's STR, DEX or INT is changed through skill gain. |  |
| [@StepStealth](@StepStealth "wikilink") | Fires when the character takes a step whilst hidden. |  |
| [@ToggleFlying](@ToggleFlying "wikilink") | Fires when a Gargoyle Player is going to Fly or to Land. |  |
| [@ToolTip](@ToolTip "wikilink") | Fires when a player requests old-style tooltips for this character. |  |
| [@TradeAccepted](@TradeAccepted "wikilink") | Fires when the character accepts a trade with another player. |  |
| [@TradeClose](@TradeClose "wikilink") | Fires when a trade window is closed. |  |
| [@TradeCreate](@TradeCreate "wikilink") | Fires when a player begins a trade with another player. |  |
| [@UserBugReport](@UserBugReport "wikilink") | Fires when the player submits a bug report. |  |
| [@UserChatButton](@UserChatButton "wikilink") | Fires when the player presses the Chat button on the paperdoll. |  |
| [@UserExtCmd](@UserExtCmd "wikilink") | Fires when the player sends an extended command packet. (used by some macros) |  |
| [@UserExWalkLimit](@UserExWalkLimit "wikilink") | Fires when the player's movement is restricted by the movement speed settings in Sphere.ini |  |
| [@UserGuildButton](@UserGuildButton "wikilink") | Fires when the player presses the Guild button on the paperdoll. |  |
| [@UserKRToolbar](@UserKRToolbar "wikilink") | Fires when the player presses a button on the toolbar. |  |
| [@UserMailBag](@UserMailBag "wikilink") | Fires when the player drags the mail bag on to another character. |  |
| [@UserQuestArrowClick](@UserQuestArrowClick "wikilink") | Fires when the player clicks the quest arrow. |  |
| [@UserQuestButton](@UserQuestButton "wikilink") | Fires when the player presses the Quest button on the paperdoll. |  |
| [@UserSkills](@UserSkills "wikilink") | Fires when the player opens their skill menu, or a skill update is sent to the player. |  |
| [@UserSpecialMove](@UserSpecialMove "wikilink") | Fires when the player uses a special move. |  |
| [@UserStats](@UserStats "wikilink") | Fires when the player opens the status window. |  |
| [@UserUltimaStoreButton](@UserUltimaStoreButton "wikilink") | Fires when click on 'Ultima Store' button on new clients 7.0.62+ |  |
| [@UserVirtue](@UserVirtue "wikilink") | Fires when the player presses on the Virtue button. |  |
| [@UserVirtueInvoke](@UserVirtueInvoke "wikilink") | Fires when the player invokes a virtue through macros. |  |
| [@UserWarmode](@UserWarmode "wikilink") | Fires when the player switches between war and peace mode. |  |

## Players

Characters that are attached to an account become Player Characters. In
addition to the basic character references, properties and functions
they also receive the following:

### References

References return pointers to other objects (e.g. the REGION reference
allows you to access the REGION that an object is in). These can either
be accessed by using *\<REFNAME\>* to return the [UID](UID "wikilink")
(1 for object types that don't have UIDs) of the object or 0 if it
doesn't exist, or by using *\<REFNAME.KEY\>* where KEY is a valid
property/function/reference for the *REFNAME* object. Click on the name
for more detailed information such as usage and examples.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [GUILD](GUILD "wikilink") | R | Gets the [guild stone](Special_Items#Guild.2FTown_Stones "wikilink") that the player belongs to. |
| [SKILLCLASS](SKILLCLASS_(Reference) "wikilink") | RW | Gets or sets the player's [skillclass](SKILLCLASS "wikilink"). |
| [TOWN](TOWN "wikilink") | R | Gets the [town stone](Special_Items#Guild.2FTown_Stones "wikilink") that the player belongs to. |

### Properties and Functions

Here is a list of all player properties and functions. If a function is
marked as readable then it can return a value when used as <KEY>. Click
on the name for more detailed information such as usage and examples.

|  |  |  |  |
|----|----|----|----|
| **Name** | **Read/Write** | **Description** | **Sphere X only?** |
| [DEATHS](DEATHS "wikilink") | RW | Gets or sets the number of times the player has died. |  |
| [DSPEECH](DSPEECH "wikilink") *+/-speech_id* | RW | Gets a list of attached speech handlers, or adds or removes a speech handler to or from the player. |  |
| [GMPAGE](GMPAGE "wikilink")*.n.DELETE* | W | Deletes the nth GM page. (zero-based) |  |
| [GMPAGE](GMPAGE "wikilink")*.n.HANDLE* | W | Sets the player as the handler for the nth GM page. (zero-based) |  |
| [GMPAGE](GMPAGE "wikilink")*.n.key* | W | Executes the .page command with *key* as the arguments. |  |
| [ISDSPEECH](ISDSPEECH "wikilink")*.speech_id* | R | Returns 1 if the player has the given speech handler attached. |  |
| [KICK](KICK "wikilink") | W | Disconnects and blocks the player's account. |  |
| [KILLS](KILLS "wikilink") | RW | Gets the number of murders the player has committed. |  |
| [KRTOOLBARSTATUS](KRTOOLBARSTATUS "wikilink") | RW | Gets or sets whether or not the KR toolbar is enabled for this player. |  |
| [LASTUSED](LASTUSED "wikilink") | RW | Gets the length of time since the player was last attached to a client, in seconds. |  |
| [PASSWORD](PASSWORD "wikilink") | W | Sets or clears the player's password. |  |
| [PFLAG](PFLAG "wikilink") | RW | Gets or sets the player's PFLAG value. |  |
| [PROFILE](PROFILE "wikilink") | RW | Gets or sets the text to display on the player's profile. |  |
| [SKILLLOCK](SKILLLOCK "wikilink")*.skill_id* | RW | Gets or sets the lock state of the player's skill. 0 is Up. 1 is Down. 2 is Locked. |  |
| [SPEEDMODE](SPEEDMODE "wikilink") | RW | Gets or sets the speed that the player moves at. (0=Normal, 1=Double Speed on Foot, 2=Always walk, 3=Always Run on Foot/Always Walk on Mount, 4=Can not Walk or Run) |  |
| [STATLOCK](STATLOCK "wikilink")''.stat_id | RW | Gets or sets the lock state of the player's STR (0), DEX (2) or INT (1). \[0 = up, 1 = down, 2 = locked\] |  |

## NPCs

Characters that are not attached to an account are NPCs and are
controlled by Sphere's AI. In addition to the basic character
references, properties and functions they also receive the following:

### Properties and Functions

Here is a list of all NPC properties and functions. If a function is
marked as readable then it can return a value when used as <KEY>. Click
on the name for more detailed information such as usage and examples.

|  |  |  |  |
|----|----|----|----|
| **Name** | **Read/Write** | **Description** | **Sphere X only?** |
| [ACTPRI](ACTPRI "wikilink") | RW | Gets or sets the NPC's motivation towards their current action. |  |
| [BUY](BUY "wikilink") | W | Displays the shop window to SRC, in buy mode. |  |
| [BYE](BYE "wikilink") | W | Ends the NPC's current action. |  |
| [FLEE](FLEE "wikilink") *distance* | W | Begins moving the NPC away from its current location. |  |
| [GOTO](GOTO "wikilink") *location* | W | Begins moving the NPC towards the specified location. |  |
| [HIRE](HIRE "wikilink") | W | Begins the hiring process between the NPC and SRC. |  |
| [LEAVE](LEAVE "wikilink") *distance* | W | Begins moving the NPC away from its current location. |  |
| [NPC](NPC "wikilink") | RW | Gets or sets the NPC's AI type. |  |
| [HOMEDIST](HOMEDIST "wikilink") | RW | Gets or sets the distance that the NPC can wander from its [HOME](HOME "wikilink") position. |  |
| [PETRETRIEVE](PETRETRIEVE "wikilink") | W | Enables SRC to retrieve their stabled pets from the NPC. |  |
| [PETSTABLE](PETSTABLE "wikilink") | W | Enables SRC to stable their pet with the NPC. |  |
| [RESTOCK](RESTOCK "wikilink") *force* | W | Clears all of the NPC's stock, repopulating it when it is next accessed (or immediately if *force*=1) |  |
| [RUN](RUN "wikilink") *direction* | W | Forces the NPC to run one tile in the specified direction. |  |
| [SELL](SELL "wikilink") | W | Displays the shop window to SRC, in sell mode. |  |
| [SHRINK](SHRINK "wikilink") | W | Shrinks the NPC into a figurine item. |  |
| [SPEECH](SPEECH "wikilink") *+/-speech_id* | RW | Gets the list of speech handlers attached to the NPC, or adds or removes a speech handler to or from the NPC. |  |
| [SPEECHCOLOR](SPEECHCOLOR "wikilink") | RW | Gets or sets the colour of the NPC's speech. |  |
| [THROWDAM](THROWDAM "wikilink") *min,max* | RW | Gets or sets a range of damage used for thrown objects. (overrides chardef property) |  |
| [THROWDAM](THROWDAM "wikilink") *dam* | RW | Gets or sets the constant damage used for thrown objects. (overrides chardef property) |  |
| [THROWDAMTYPE](THROWDAMTYPE "wikilink") *damage flags* | RW | y | Gets or sets the damage flags used for thrown objects. (overrides chardef property) |
| [THROWOBJ](THROWOBJ "wikilink") *id* | RW | Gets or sets the ID of an object to be thrown by NPCs. (overrides chardef property) |  |
| [THROWRANGE](THROWRANGE "wikilink") *min,max* | RW | Gets or sets the range that an object can be thrown at. (overrides chardef property) |  |
| [THROWRANGE](THROWRANGE "wikilink") *max* | RW | Gets or sets the range that an object can be thrown at with a default min of 2. (overrides chardef property) |  |
| [TRAIN](TRAIN "wikilink") *skill* | W | Initiates training between the NPC and SRC. |  |
| [VENDCAP](VENDCAP "wikilink") | RW | Gets or sets the amount of gold a vendor will restock to. |  |
| [VENDGOLD](VENDGOLD "wikilink") | RW | Gets or sets the amount of gold a vendor has. |  |
| [WALK](WALK "wikilink") *direction* | W | Forces the NPC to walk one tile in the specified direction. |  |

## Clients

When a client is controlling a character, the following references,
properties and functions will be available:

### References

References return pointers to other objects (e.g. the REGION reference
allows you to access the REGION that an object is in). These can either
be accessed by using *\<REFNAME\>* to return the [UID](UID "wikilink")
(1 for object types that don't have UIDs) of the object or 0 if it
doesn't exist, or by using *\<REFNAME.KEY\>* where KEY is a valid
property/function/reference for the *REFNAME* object. Click on the name
for more detailed information such as usage and examples.

|  |  |  |  |
|----|----|----|----|
| **Name** | **Read/Write** | **Description** | **Sphere X only?** |
| [GMPAGEP](GMPAGEP "wikilink") | R | Gets the [GM page](GM_Pages "wikilink") that the client is currently handling. |  |
| [HOUSEDESIGN](HOUSEDESIGN "wikilink") | R | Gets the [building](Special_Items#Customizable_Multis "wikilink") that is currently being designed by the client. |  |
| [PARTY](PARTY "wikilink") | R | Gets the [party](Parties "wikilink") that the client is a member of. |  |
| [TARG](TARG "wikilink") | RW | Gets or sets the [character](Characters "wikilink") or [item](Items "wikilink") that the client has targeted. |  |
| [TARGP](TARGP "wikilink") | RW | Gets or sets the [location](Map_Points "wikilink") that the client has targeted. |  |
| [TARGPROP](TARGPROP "wikilink") | RW | Gets or sets the character whose skills are shown in the client's skill menu. |  |
| [TARGPRV](TARGPRV "wikilink") | RW | Gets or sets the [character](Characters "wikilink") or [item](Items "wikilink") that the client previously targeted. |  |

### Properties and Functions

Here is a list of all client properties and functions. If a function is
marked as readable then it can return a value when used as <KEY>. Click
on the name for more detailed information such as usage and examples.

|  |  |  |  |
|----|----|----|----|
| **Name** | **Read/Write** | **Description** | **Sphere X only?** |
| [ADD](ADD "wikilink") *item_defname* | W | Prompts the client to target a location to add the specified item at. |  |
| [ADDBUFF](ADDBUFF "wikilink") *icon, cliloc1, cliloc2, time, arg1, arg2, arg3* | W | Displays a buff icon in the client's buff icon bar. |  |
| [ADDCLILOC](ADDCLILOC "wikilink") *cliloc, args* | W | Adds a cliloc to the tooltip being sent to the client. Only valid in @ClientTooltip triggers. |  |
| [ADDCONTEXTENTRY](ADDCONTEXTENTRY "wikilink") *entry_id, cliloc, flags, colour* | W | Adds an entry to the context menu being sent to the client. Only valid in @ContextMenuRequest triggers. |  |
| [ALLMOVE](ALLMOVE "wikilink") | RW | Gets or sets whether or not the client has ALLMOVE privileges. |  |
| [ALLSHOW](ALLSHOW "wikilink") | RW | Gets or sets whether or not the client is able to see disconnected characters. |  |
| [ARROWQUEST](ARROWQUEST "wikilink") *x, y, id* | W | Displays an arrow on the client's screen that points to the specified world coordinates. If id is supplied multiple arrows can be displayed on the client at once (Newer clients only - 3.x+ clients confirm?). You can cancel the arrow by passing 0 for x and y and your id. Using ARROWQUEST without any arguments will cancel arrow with id 0 if present. |  |
| [BADSPAWN](BADSPAWN "wikilink") | W | Teleports the client to the first invalid spawn point in the world. |  |
| [BANKSELF](BANKSELF "wikilink") | W | Opens up the client's bankbox. |  |
| [CAST](CAST "wikilink") ''spell_id' | W | Begins casting a spell. |  |
| [CHARLIST](CHARLIST "wikilink") | W | Displays the client's character list screen. |  |
| [CLEARCTAGS](CLEARCTAGS "wikilink") | W | Removes all of the client's CTAGs. |  |
| [CLIENTIS3D](CLIENTIS3D "wikilink") | R | Returns 1 if the client is using the 3D client. |  |
| [CLIENTISKR](CLIENTISKR "wikilink") | R | Returns 1 if the client is using the KR client. |  |
| [CLIENTVERSION](CLIENTVERSION "wikilink") | R | Gets the client version the client is using, based on the encryption keys being used (unencrypted clients return 0). |  |
| [CTAG](CTAG "wikilink") | RW | Gets or sets the value of a CTAG. |  |
| [CTAGCOUNT](CTAGCOUNT "wikilink") | R | Gets the number of CTAGs stored on the client. |  |
| [CTAGLIST](CTAGLIST "wikilink") | W | Displays a list of the client's CTAGs to SRC. |  |
| [CTAGLIST](CTAGLIST "wikilink") LOG | W | Displays a list of the client's CTAGs on the server console. |  |
| [DEBUG](DEBUG "wikilink") | RW | Gets or sets whether or not the client is in debug mode. |  |
| [DETAIL](DETAIL "wikilink") | RW | Gets or sets whether or not the client receives additional detail, such as combat messages. |  |
| [EVERBTARG](EVERBTARG "wikilink") *command* | W | Prompts the client to enter a command, or arguments to the command if specified. The complete command with arguments is then executed on TARG. |  |
| [EXTRACT](EXTRACT "wikilink") *file, template_id* | W | Extracts static items from a targeted area on the map and saves them into the specified file. |  |
| [FLUSH](FLUSH "wikilink") | W | Forces queued network data to be immediately sent to the client. |  |
| [GM](GM "wikilink") | RW | Gets or sets whether or not the client is in GM mode. |  |
| [GMPAGE](GMPAGE "wikilink") *ADD message* | W | Sends a GM page from the client with the specified message, or if no arguments provided will prompt the client for a message. |  |
| [GOTARG](GOTARG "wikilink") | W | Teleports the client to their targeted item. |  |
| [HEARALL](HEARALL "wikilink") | RW | Gets or sets whether or not the client can hear all player speech regardless of location. |  |
| [INFO](INFO "wikilink") | W | Displays an information dialog to the client for an object they target. |  |
| [INFORMATION](INFORMATION "wikilink") | W | Displays server information to the client. |  |
| [LAST](LAST "wikilink") | W | Forces the client to target the object referenced by [ACT](ACT "wikilink"). |  |
| [LASTEVENT](LASTEVENT "wikilink") | RW | Returns the time when data was last received from the client. |  |
| [LINK](LINK "wikilink") | W | Allows the client to target two objects to link them together. |  |
| [MENU](MENU_(Function) "wikilink") *menu_id* | W | Displays a menu to the client. |  |
| [MIDILIST](MIDILIST "wikilink") *music1, music2, ...* | W | Selects a random music id from the given list and tells the client to play it. |  |
| [NUDGE](NUDGE "wikilink") *dx, dy, dz* | W | Allows the client to nudge an area of items by the given coordinates, relative to the items' position. |  |
| [NUKE](NUKE "wikilink") *command* | W | Allows the client to execute *command* on all items in a targeted area. |  |
| [NUKECHAR](NUKECHAR "wikilink") *command* | W | Allows the client to execute *command* on all NPCs in a targeted area. |  |
| [PAGE](PAGE "wikilink") | W | Displays the GM page menu to the client. |  |
| [PRIVSHOW](PRIVSHOW "wikilink") | W | Gets or sets whether or not the client's privilege level should show in their name. |  |
| [REMOVEBUFF](REMOVEBUFF "wikilink") *icon* | W | Removes a buff icon from the client's buff icon bar. |  |
| [REPAIR](REPAIR "wikilink") | W | Prompts the client to target an item for them to repair. |  |
| [REPORTEDCLIVER](REPORTEDCLIVER "wikilink") | R | Gets the client version the client is using, based on what it has identified itself as to the server. |  |
| [REPORTEDCLIVER](REPORTEDCLIVER "wikilink").FULL | R | Gets the client version the client is using, based on what it has identified itself as to the server, including the 4th digit. |  |
| [RESEND](RESEND "wikilink") | W | Forces a full refresh of the client's screen. |  |
| [SAVE](SAVE "wikilink") *immediate* | W | Begins a world save. If background saving is enabled then *[SAVE](SAVE "wikilink") 1* will force a foreground save. |  |
| [SCREENSIZE](SCREENSIZE "wikilink") | R | Gets the client's screen size. (width,height) |  |
| [SCREENSIZE](SCREENSIZE "wikilink").X | R | Gets the width of the client's screen size. |  |
| [SCREENSIZE](SCREENSIZE "wikilink").Y | R | Gets the height of the client's screen size. |  |
| [SCROLL](SCROLL "wikilink") *scroll_id* | W | Displays a message scroll to the client. |  |
| [SELF](SELF "wikilink") | W | Forces the client to target itself. |  |
| [SENDPACKET](SENDPACKET "wikilink") *data* | W | Sends a raw data packet to the client. |  |
| [SET](SET "wikilink") *command* | W | Prompts the client to target an object to execute *command* on. |  |
| [SHOWSKILLS](SHOWSKILLS "wikilink") | W | Refreshes the client's skills for the skill menu. |  |
| [SKILLMENU](SKILLMENU_(Function) "wikilink") *skillmenu_id* | W | Displays a skillmenu to the client. |  |
| [SKILLSELECT](SKILLSELECT "wikilink") *skill_id* | W | Simulates the client selecting a skill from their skill menu. |  |
| [SUMMON](SUMMON "wikilink") *character_id* | W | Casts the summon spell, with ''character_id'; being the character to summon. |  |
| [SYSMESSAGE](SYSMESSAGE "wikilink") *text* | W | Displays a system message to the client. |  |
| [SYSMESSAGELOC](SYSMESSAGELOC "wikilink") *hue, cliloc, args* | W | Displays a localized system message to the client. |  |
| [SYSMESSAGELOCEX](SYSMESSAGELOCEX "wikilink") *hue, cliloc, flags, affix, args* | W | Displays a localized system message to the client with affixed text. |  |
| [SYSMESSAGEUA](SYSMESSAGEUA "wikilink") *hue, font, mode, language, text* | W | Displays a UNICODE system message to the client. |  |
| [TARGETTEXT](TARGETTEXT "wikilink") | RW | Gets or sets the client's target text. |  |
| [TELE](TELE "wikilink") | W | Casts the teleport spell. |  |
| [TILE](TILE "wikilink") *z, item1, item2, ...* | W | Tiles the ground within a targeted area with the listed items, at the given Z level. |  |
| [UNEXTRACT](UNEXTRACT "wikilink") *file* | W | Unextracts previously extracted statics, as dynamic items at a targeted location. |  |
| [VERSION](VERSION "wikilink") | W | Displays the server description to the client. |  |
| [WEBLINK](WEBLINK "wikilink") *url* | W | Opens the client's web browser to send them to the specified url. |  |
| [X](X "wikilink")*command* | W | Prompts the client to target an object to execute *command* on. |  |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Objects](Category:_Objects "wikilink")
