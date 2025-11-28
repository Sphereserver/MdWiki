\_\_FORCETOC\_\_ The server object is a global object that can be
accessed from any script, by using the SERV reference. The following
tables detail the various properties of the server in SphereServer:

## References

References return pointers to other objects (e.g. the CHAR.n reference
allows you to access the characters that are attached to the account).
These can either be accessed by using *\<REFNAME\>* to return the
[UID](UID "wikilink") (1 for object types that don't have UIDs) of the
object or 0 if it doesn't exist, or by using *\<REFNAME.KEY\>* where KEY
is a valid property/function/reference for the *REFNAME* object. Click
on the name for more detailed information such as usage and examples.

<table>
<tbody>
<tr>
<td><p><strong>Name</strong></p></td>
<td><p><strong>Read/Write</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p><a href="ACCOUNT"
title="wikilink">ACCOUNT</a><em>.n</em></p></td>
<td><p>R</p></td>
<td><p>Gets the nth <a href="Accounts" title="wikilink">account</a> on
the server. (zero-based)</p></td>
</tr>
<tr>
<td><p><a href="ACCOUNT"
title="wikilink">ACCOUNT</a><em>.name</em></p></td>
<td><p>R</p></td>
<td><p>Gets the <a href="Accounts" title="wikilink">account</a> with the
specified name.</p></td>
</tr>
<tr>
<td><p><a href="AREA"
title="wikilink">AREA</a><em>.defname</em></p></td>
<td><p>R</p></td>
<td><p>Gets the <a href="Regions" title="wikilink">region</a> with the
specified defname.</p></td>
</tr>
<tr>
<td><p><a href="CHARDEF_(Reference)"
title="wikilink">CHARDEF</a><em>.defname</em></p></td>
<td><p>R</p></td>
<td><p>Gets the <a href="CHARDEF" title="wikilink">character
definition</a> for <em>defname</em>.</p></td>
</tr>
<tr>
<td><p><a href="DEF" title="wikilink">DEF</a><em>.defname</em></p></td>
<td><p>R</p></td>
<td><p>Gets the value for <em>defname</em>. Def0.defname can also be
used similar to tag0 and ctag0.</p></td>
</tr>
<tr>
<td><p><a href="CLIENT" title="wikilink">CLIENT</a><em>.n</em></p></td>
<td><p>R</p></td>
<td><p>Gets the nth <a href="Characters#Clients"
title="wikilink">client</a> on the server. (zero-based)<br />
<strong>Note:</strong> The nth client may not be an ingame player
character, check &lt;CLIENT.n&gt; first as it returns 1 for ingame
clients and 0 for non-player clients.</p></td>
</tr>
<tr>
<td><p><a href="GMPAGE" title="wikilink">GMPAGE</a><em>.n</em></p></td>
<td><p>R</p></td>
<td><p>Gets the nth <a href="GM_Pages" title="wikilink">GM page</a> on
the server. (zero-based)</p></td>
</tr>
<tr>
<td><p><a href="GUILDSTONES"
title="wikilink">GUILDSTONES</a><em>.n</em></p></td>
<td><p>R</p></td>
<td><p>Gets the nth <a href="Special_Items#Guild.2FTown_Stones"
title="wikilink">guild stone</a> on the server. (zero-based)</p></td>
</tr>
<tr>
<td><p><a href="ITEMDEF_(Reference)"
title="wikilink">ITEMDEF</a><em>.defname</em></p></td>
<td><p>R</p></td>
<td><p>Gets the <a href="ITEMDEF" title="wikilink">item definition</a>
for <em>defname</em>.</p></td>
</tr>
<tr>
<td><p><a href="LASTNEWCHAR" title="wikilink">LASTNEWCHAR</a></p></td>
<td><p>R</p></td>
<td><p>Gets the last <a href="Characters" title="wikilink">character</a>
created on the server.</p></td>
</tr>
<tr>
<td><p><a href="LASTNEWITEM" title="wikilink">LASTNEWITEM</a></p></td>
<td><p>R</p></td>
<td><p>Gets the last <a href="Items" title="wikilink">item</a> created
on the server.</p></td>
</tr>
<tr>
<td><p><a href="MAP" title="wikilink">MAP</a><em>(x, y, map)</em><br />
<a href="MAP" title="wikilink">MAP</a><em>(x, y, z, map)</em></p></td>
<td><p>R</p></td>
<td><p>Gets the <a href="Map_Points" title="wikilink">map point</a> for
a specified location.</p></td>
</tr>
<tr>
<td><p><a href="REGIONRESOURCE_(Reference)"
title="wikilink">REGIONRESOURCE</a><em>.defname</em></p></td>
<td><p>R</p></td>
<td><p>Gets the <a href="REGIONRESOURCE" title="wikilink">region
resource definition</a> for <em>defname</em>.</p></td>
</tr>
<tr>
<td><p><a href="REGIONTYPE_(Reference)"
title="wikilink">REGIONTYPE</a><em>.defname</em></p></td>
<td><p>R</p></td>
<td><p>Gets the <a href="REGIONTYPE" title="wikilink">region type
definition</a> for <em>defname</em>.</p></td>
</tr>
<tr>
<td><p><a href="ROOM_(Reference)"
title="wikilink">ROOM</a><em>.defname</em></p></td>
<td><p>R</p></td>
<td><p>Gets the <a href="Rooms" title="wikilink">room</a> with the
specified defname.</p></td>
</tr>
<tr>
<td><p><a href="SKILL_(Reference)"
title="wikilink">SKILL</a><em>.defname</em></p></td>
<td><p>R</p></td>
<td><p>Gets the <a href="SKILL" title="wikilink">skill definition</a>
for <em>defname</em>.</p></td>
</tr>
<tr>
<td><p><a href="SKILLCLASS_(Reference)"
title="wikilink">SKILLCLASS</a><em>.defname</em></p></td>
<td><p>R</p></td>
<td><p>Gets the <a href="SKILLCLASS" title="wikilink">skillclass</a> for
<em>defname</em>.</p></td>
</tr>
<tr>
<td><p><a href="SPAWN_(Reference)"
title="wikilink">SPAWN</a><em>.defname</em></p></td>
<td><p>R</p></td>
<td><p>Gets the <a href="SPAWN" title="wikilink">spawn group</a> for
<em>defname</em>.</p></td>
</tr>
<tr>
<td><p><a href="SPELL_(Reference)"
title="wikilink">SPELL</a><em>.defname</em></p></td>
<td><p>R</p></td>
<td><p>Gets the <a href="SPELL" title="wikilink">spell definition</a>
for <em>defname</em>.</p></td>
</tr>
<tr>
<td><p><a href="SPELL_(Reference)"
title="wikilink">SPELL</a><em>.n</em></p></td>
<td><p>R</p></td>
<td><p>Gets the nth <a href="SPELL" title="wikilink">spell
definition</a>, ordered by skill requirements (1-based,
ascending).</p></td>
</tr>
<tr>
<td><p>(X only)<a href="TILEDATA_(Reference)"
title="wikilink">TILEDATA</a>.TERRAIN(<em>id</em>).<em>attribute</em></p></td>
<td><p>R</p></td>
<td><p>Gets the tiledata <em>attribute</em> of <em>id</em> terrain.
<em>attribute</em> can be one of: FLAGS,UNK,INDEX,NAME.</p></td>
</tr>
<tr>
<td><p>(X only)<a href="TILEDATA_(Reference)"
title="wikilink">TILEDATA</a>.ITEM(<em>id</em>).<em>attribute</em></p></td>
<td><p>R</p></td>
<td><p>Gets the tiledata <em>attribute</em> of <em>id</em> item.
<em>attribute</em> can be one of:
FLAGS,WEIGHT,LAYER,UNK11,ANIM,HUE,LIGHT,HEIGHT,NAME.</p></td>
</tr>
<tr>
<td><p><a href="TOWNSTONES"
title="wikilink">TOWNSTONES</a><em>.n</em></p></td>
<td><p>R</p></td>
<td><p>Gets the nth <a href="Special_Items#Guild.2FTown_Stones"
title="wikilink">town stone</a> on the server. (zero-based)</p></td>
</tr>
</tbody>
</table>

## Properties and Functions

Here is a list of all item properties and functions. If a function is
marked as readable then it can return a value when used as <KEY>. Click
on the name for more detailed information such as usage and examples.
Settings from Sphere.ini can also be accessed from the server object,
but they are not listed in this table.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [ACCOUNT](ACCOUNT "wikilink") ADD *name password* | W | Creates an account with the specified name and password. |
| [ACCOUNT](ACCOUNT "wikilink") ADDMD5 *name hash* | W | Creates an account with the specified name and MD5 password hash. |
| [ACCOUNT](ACCOUNT "wikilink") BLOCKED *days command* | W | Executes *command* on all accounts that have been unused for *days* days and are currently blocked. |
| [ACCOUNT](ACCOUNT "wikilink") JAILED *days command* | W | Executes *command* on all accounts that have been unused for *days* days and are currently jailed. |
| [ACCOUNT](ACCOUNT "wikilink") UNUSED *days command* | W | Executes *command* on all accounts that have been unused for *days* days. |
| [ACCOUNT](ACCOUNT "wikilink") UPDATE | W | Saves the accounts to file. |
| [ACCOUNT](ACCOUNT "wikilink") *name command* | W | Executes *command* on the account with the specified name. |
| [ACCOUNTS](ACCOUNTS "wikilink") | RW | Gets or sets the number of accounts on the server. |
| [ALLCLIENTS](ALLCLIENTS "wikilink") *command* | W | Executes *command* on all online player characters. |
| [B](B "wikilink") *message* | W | Broadcasts *message* to all clients on the server. |
| [BLOCKIP](BLOCKIP "wikilink") *address, time* | W | Blocks an IP address for *time*, in tenths of a second (-1 = permanent). |
| [CHARS](CHARS "wikilink") | RW | Gets or sets the number of characters on the server. |
| [CLEARLISTS](CLEARLISTS "wikilink") *mask* | W | Removes all LISTs whose name contains *mask*. |
| [CLEARVARS](CLEARVARS "wikilink") *prefix* | W | Removes all VARs that start with the given prefix. |
| [CLIENTS](CLIENTS "wikilink") | R | Gets the total number of connected clients. |
| [CONSOLE](CONSOLE "wikilink") *command* | W | Executes *command* as if it had been typed directly into the server console. |
| [EXPORT](EXPORT "wikilink") *file, flags, distance* | W | Exports all objects within *distance* tiles of SRC to a file. (Flags: 1 = Items, 2 = Characters, 3 = Both) |
| [GARBAGE](GARBAGE "wikilink") | W | Forces an immediate garbage collection (checks for invalid objects and fixes them if possible, or else removes them). |
| [GMPAGES](GMPAGES "wikilink") | R | Returns the total number of GM pages. |
| [GUILDS](GUILDS "wikilink") | R | Returns the total number of guild *and* town stones. |
| [GUILDSTONES](GUILDSTONES "wikilink").COUNT | R | Returns the total number of guild stones on the server. |
| [HEARALL](HEARALL "wikilink") | RW | Gets or sets whether player speech is logged to server console and log file. |
| [IMPORT](IMPORT "wikilink") *file, flags, distance* | W | Imports previously exported items that were within *distance* tiles. (Flags: 1 = Items, 2 = Characters, 3 = Both) |
| [INFORMATION](INFORMATION "wikilink") | W | Displays server information to SRC. |
| [ITEMS](ITEMS "wikilink") | RW | Gets or sets the number of items on the server. |
| [LOAD](LOAD "wikilink") *file* | W | Loads a script file. |
| [LOG](LOG "wikilink") *message* | W | Logs *message* to server console and logs. |
| [LOOKUPSKILL](LOOKUPSKILL "wikilink") *skill_name* | R | Looks up a skill name or key, and returns its skill number. |
| [MAP](MAP "wikilink")*.map_num.*ALLSECTORS *command* | W | Executes *command* on all sectors of a map. |
| [MAP](MAP "wikilink")*.map_num.*SECTOR.*sector_num command* | RW | Executes *command* on sector *sector_num* of a map. |
| [MAPLIST](MAPLIST "wikilink")*.map_num* | R | Returns 1 if *map_num* is a valid map number. |
| [MAPLIST](MAPLIST "wikilink")*.map_num*.BOUND.X | R | Returns the maximum X coordinate for a map. |
| [MAPLIST](MAPLIST "wikilink")*.map_num*.BOUND.Y | R | Returns the maximum Y coordinate for a map. |
| [MAPLIST](MAPLIST "wikilink")*.map_num*.CENTER.X | R | Returns the central X coordinate of a map. |
| [MAPLIST](MAPLIST "wikilink")*.map_num*.CENTER.Y | R | Returns the central Y coordinate of a map. |
| [MAPLIST](MAPLIST "wikilink")*.map_num*.SECTOR.COLS | R | Returns the number of sector columns on a map. |
| [MAPLIST](MAPLIST "wikilink")*.map_num*.SECTOR.QTY | R | Returns the number of sectors on a map. |
| [MAPLIST](MAPLIST "wikilink")*.map_num*.SECTOR.ROWs | R | Returns the number of sector rows on a map. |
| [MAPLIST](MAPLIST "wikilink")*.map_num*.SECTOR.SIZE | R | Returns the size of the sectors on a map. |
| [MEM](MEM "wikilink") | R | Returns the total amount of memory being used, in kilobytes. |
| [PRINTLISTS](PRINTLISTS "wikilink") *LOG* | W | Displays a list of all LISTs to SRC, or the server console. |
| [REGEN](REGEN "wikilink")0 | RW | Gets or sets the length of time it takes for characters to regenerate 1 health point, in seconds. |
| [REGEN](REGEN "wikilink")1 | RW | Gets or sets the length of time it takes for characters to regenerate 1 mana point, in seconds. |
| [REGEN](REGEN "wikilink")2 | RW | Gets or sets the length of time it takes for characters to regenerate 1 stamina point, in seconds. |
| [REGEN](REGEN "wikilink")3 | RW | Gets or sets the length of time it takes for characters to lose 1 food point, in seconds. |
| [RESPAWN](RESPAWN "wikilink") | W | Respawns all dead NPCs (not corpses) in the world. |
| [RESTOCK](RESTOCK "wikilink") | W | Restocks all NPCs in the world. |
| [RESTORE](RESTORE "wikilink") *file, account_name, character_name* | W | Restores a player character from a backup save. |
| [RESYNC](RESYNC "wikilink") | W | Checks all script files for any changes made since they were last loaded. |
| [RTICKS](RTICKS "wikilink") | R | Returns the real-world time, as a timestamp. |
| [RTICKS](RTICKS "wikilink").FORMAT *timestamp, format* | R | Returns the real-world timestamp as a formatted datetime string. |
| [RTICKS](RTICKS "wikilink").FROMTIME *year, month, day, hour, minutes, seconds* | R | Returns the specified real-world time, as a timestamp. |
| [RTIME](RTIME "wikilink") | R | Returns the real-world time, as a formatted string. |
| [RTIME](RTIME "wikilink").FORMAT *format* | R | Returns the real-world time, as a formatted string. More information : [Serv.rtime.format](Serv.rtime.format "wikilink") |
| [SAVE](SAVE "wikilink") *force_immediate* | W | Begins a world save. If background saving is enabled, *force_immediate* can be used to force a foreground save. |
| [SAVECOUNT](SAVECOUNT "wikilink") | R | Returns the number of world saves that have taken place. |
| [SAVESTATICS](SAVESTATICS "wikilink") | W | Performs a statics save. |
| [SHRINKMEM](SHRINKMEM "wikilink") | W | Temporarily reduces memory usage. |
| [SHUTDOWN](SHUTDOWN "wikilink") *time* | W | Schedules a server shutdown in *time* minutes. |
| [SYSCMD](SYSCMD "wikilink") *cmd* | W | Executes *cmd* and waits for it to finish executing. Returns \<0 if an error occurred. Requires OF_FileCommands. |
| [SYSSPAWN](SYSSPAWN "wikilink") *cmd* | W | Executes *cmd* and does not wait for the program to finish executing. Returns \<0 if an error occurred. Requires OF_FileCommands. |
| [TICKPERIOD](TICKPERIOD "wikilink") | R | Returns how much server ticks are in a real-world second. |
| [TIME](TIME "wikilink") | R | Returns the total server uptime, in tenths of a second. |
| [TIMEHIRES](TIMEHIRES "wikilink") | R | X branch only. Returns the internal timer in milliseconds. |
| [TIMEUP](TIMEUP "wikilink") | R | Returns the server uptime, as second. |
| [TOWNSTONES](TOWNSTONES "wikilink").COUNT | R | Returns the total number of town stones on the server. |
| [UNBLOCKIP](UNBLOCKIP "wikilink") *address* | W | Unblocks a previously blocked IP address. |
| [VARLIST](VARLIST "wikilink") *LOG* | W | Displays a list of all VARs to SRC, or the server console. |
| [VERSION](VERSION "wikilink") | R | Returns the SphereServer version. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Objects](Category:_Objects "wikilink")
