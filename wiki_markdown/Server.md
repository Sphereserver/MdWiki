```{=mediawiki}
{{Languages|Server}}
```
\_\_FORCETOC\_\_ The server object is a global object that can be
accessed from any script, by using the SERV reference. The following
tables detail the various properties of the server in SphereServer:

## References

References return pointers to other objects (e.g. the CHAR.n reference
allows you to access the characters that are attached to the account).
These can either be accessed by using *\<REFNAME\>* to return the
[UID](./UID.md) (1 for object types that don\'t have UIDs) of the
object or 0 if it doesn\'t exist, or by using *\<REFNAME.KEY\>* where
KEY is a valid property/function/reference for the *REFNAME* object.
Click on the name for more detailed information such as usage and
examples.

+-------------------------+----------------+-------------------------+
| **Name**                | **Read/Write** | **Description**         |
+-------------------------+----------------+-------------------------+
| [ACCOUNT](./R_______________Gets_the_nth____________
_ACCOUNT.md)*.n* |                | [accoun                 |
|                         |                | t](./Accounts.md) |
|                         |                | on the server.          |
|                         |                | (zero-based)            |
+-------------------------+----------------+-------------------------+
| [ACCOUNT](./ACC____________R_______________Gets_the________________
_OUNT.md)*.name* |                | [accoun                 |
|                         |                | t](./Accounts.md) |
|                         |                | with the specified      |
|                         |                | name.                   |
+-------------------------+----------------+-------------------------+
| [AREA](./ARE_______________R_______________Gets_the________________
_A.md)*.defname* |                | [regi                   |
|                         |                | on](./Regions.md) |
|                         |                | with the specified      |
|                         |                | defname.                |
+-------------------------+----------------+-------------------------+
| [CHAR                   | R              | Gets the [character     |
| DEF](CHARDEF_(Reference |                | definiti                |
| ) "wikilink")*.defname* |                | on](CHARDEF "wikilink") |
|                         |                | for *defname*.          |
+-------------------------+----------------+-------------------------+
| [DEF](./DE_________________R_______________Gets_the_value_for______
_F.md)*.defname* |                | *defname*. Def0.defname |
|                         |                | can also be used        |
|                         |                | similar to tag0 and     |
|                         |                | ctag0.                  |
+-------------------------+----------------+-------------------------+
| [CLIENT]                | R              | Gets the nth            |
| (CLIENT "wikilink")*.n* |                | [client](./Charact________
__________________________________________ersClients.md) |
|                         |                | on the server.          |
|                         |                | (zero-based)\           |
|                         |                | **Note:** The nth       |
|                         |                | client may not be an    |
|                         |                | ingame player           |
|                         |                | character, check        |
|                         |                | \<CLIENT.n\> first as   |
|                         |                | it returns 1 for ingame |
|                         |                | clients and 0 for       |
|                         |                | non-player clients.     |
+-------------------------+----------------+-------------------------+
| [GMPAGE]                | R              | Gets the nth [GM        |
| (GMPAGE "wikilink")*.n* |                | pag                     |
|                         |                | e](./GM_Pages.md) |
|                         |                | on the server.          |
|                         |                | (zero-based)            |
+-------------------------+----------------+-------------------------+
| [GUILDSTONES](./GUIL_______R_______________Gets_the_nth_guild_____
_DSTONES.md)*.n* |                | stone]                  |
|                         |                | (Special_Items#Guild.2F |
|                         |                | Town_Stones "wikilink") |
|                         |                | on the server.          |
|                         |                | (zero-based)            |
+-------------------------+----------------+-------------------------+
| [ITEM                   | R              | Gets the [item          |
| DEF](ITEMDEF_(Reference |                | definiti                |
| ) "wikilink")*.defname* |                | on](ITEMDEF "wikilink") |
|                         |                | for *defname*.          |
+-------------------------+----------------+-------------------------+
| [LASTNEWCHAR](./R_______________Gets_the_last___________
_LASTNEWCHAR.md) |                | [character]             |
|                         |                | (Characters "wikilink") |
|                         |                | created on the server.  |
+-------------------------+----------------+-------------------------+
| [LASTNEWITEM](./R_______________Gets_the_last___________
_LASTNEWITEM.md) |                | [                       |
|                         |                | item](./Items.md) |
|                         |                | created on the server.  |
+-------------------------+----------------+-------------------------+
| [M                      | R              | Gets the [map           |
| AP](./MAP.md)*(x, |                | point]                  |
| y, map)*\               |                | (Map_Points "wikilink") |
| [M                      |                | for a specified         |
| AP](./MAP.md)*(x, |                | location.               |
| y, z, map)*             |                |                         |
+-------------------------+----------------+-------------------------+
| [REGIONRESOURCE](RE     | R              | Gets the [region        |
| GIONRESOURCE_(Reference |                | resource                |
| ) "wikilink")*.defname* |                | definition](./REG_________
__________________________________________IONRESOURCE.md) |
|                         |                | for *defname*.          |
+-------------------------+----------------+-------------------------+
| [REGIONTYPE             | R              | Gets the [region type   |
| ](REGIONTYPE_(Reference |                | definition]             |
| ) "wikilink")*.defname* |                | (REGIONTYPE "wikilink") |
|                         |                | for *defname*.          |
+-------------------------+----------------+-------------------------+
| [ROOM](ROOM_(Reference  | R              | Gets the                |
| ) "wikilink")*.defname* |                | [                       |
|                         |                | room](./Rooms.md) |
|                         |                | with the specified      |
|                         |                | defname.                |
+-------------------------+----------------+-------------------------+
| [                       | R              | Gets the [skill         |
| SKILL](SKILL_(Reference |                | defini                  |
| ) "wikilink")*.defname* |                | tion](SKILL "wikilink") |
|                         |                | for *defname*.          |
+-------------------------+----------------+-------------------------+
| [SKILLCLASS             | R              | Gets the                |
| ](SKILLCLASS_(Reference |                | [skillclass]            |
| ) "wikilink")*.defname* |                | (SKILLCLASS "wikilink") |
|                         |                | for *defname*.          |
+-------------------------+----------------+-------------------------+
| [                       | R              | Gets the [spawn         |
| SPAWN](SPAWN_(Reference |                | g                       |
| ) "wikilink")*.defname* |                | roup](SPAWN "wikilink") |
|                         |                | for *defname*.          |
+-------------------------+----------------+-------------------------+
| [                       | R              | Gets the [spell         |
| SPELL](SPELL_(Reference |                | defini                  |
| ) "wikilink")*.defname* |                | tion](SPELL "wikilink") |
|                         |                | for *defname*.          |
+-------------------------+----------------+-------------------------+
| [SPELL](SPELL_(Ref      | R              | Gets the nth [spell     |
| erence) "wikilink")*.n* |                | definit                 |
|                         |                | ion](./SPELL.md), |
|                         |                | ordered by skill        |
|                         |                | requirements (1-based,  |
|                         |                | ascending).             |
+-------------------------+----------------+-------------------------+
| (X                      | R              | Gets the tiledata       |
| only)                   |                | *attribute* of *id*     |
| [TILEDATA](TILEDATA_(Re |                | terrain. *attribute*    |
| ference) "wikilink").TE |                | can be one of:          |
| RRAIN(*id*).*attribute* |                | FLAGS,UNK,INDEX,NAME.   |
+-------------------------+----------------+-------------------------+
| (X                      | R              | Gets the tiledata       |
| on                      |                | *attribute* of *id*     |
| ly)[TILEDATA](TILEDATA_ |                | item. *attribute* can   |
| (Reference) "wikilink") |                | be one of:              |
| .ITEM(*id*).*attribute* |                | FLAGS,                  |
|                         |                | WEIGHT,LAYER,UNK11,ANIM |
|                         |                | ,HUE,LIGHT,HEIGHT,NAME. |
+-------------------------+----------------+-------------------------+
| [TOWNSTONES](./TOW_________R_______________Gets_the_nth_town______
_NSTONES.md)*.n* |                | stone]                  |
|                         |                | (Special_Items#Guild.2F |
|                         |                | Town_Stones "wikilink") |
|                         |                | on the server.          |
|                         |                | (zero-based)            |
+-------------------------+----------------+-------------------------+

## Properties and Functions {#properties_and_functions}

Here is a list of all item properties and functions. If a function is
marked as readable then it can return a value when used as
`<KEY>`{=html}. Click on the name for more detailed information such as
usage and examples. Settings from Sphere.ini can also be accessed from
the server object, but they are not listed in this table.

  --------------------------------------------------------------------------------- ---------------- -----------------------------------------------------------------------------------------------------------------------------------
  **Name**                                                                          **Read/Write**   **Description**
  [ACCOUNT](./ACCOUNT.md) ADD *name password*                                 W                Creates an account with the specified name and password.
  [ACCOUNT](./ACCOUNT.md) ADDMD5 *name hash*                                  W                Creates an account with the specified name and MD5 password hash.
  [ACCOUNT](./ACCOUNT.md) BLOCKED *days command*                              W                Executes *command* on all accounts that have been unused for *days* days and are currently blocked.
  [ACCOUNT](./ACCOUNT.md) JAILED *days command*                               W                Executes *command* on all accounts that have been unused for *days* days and are currently jailed.
  [ACCOUNT](./ACCOUNT.md) UNUSED *days command*                               W                Executes *command* on all accounts that have been unused for *days* days.
  [ACCOUNT](./ACCOUNT.md) UPDATE                                              W                Saves the accounts to file.
  [ACCOUNT](./ACCOUNT.md) *name command*                                      W                Executes *command* on the account with the specified name.
  [ACCOUNTS](./ACCOUNTS.md)                                                   RW               Gets or sets the number of accounts on the server.
  [ALLCLIENTS](./ALLCLIENTS.md) *command*                                     W                Executes *command* on all online player characters.
  [B](./B.md) *message*                                                       W                Broadcasts *message* to all clients on the server.
  [BLOCKIP](./BLOCKIP.md) *address, time*                                     W                Blocks an IP address for *time*, in tenths of a second (-1 = permanent).
  [CHARS](./CHARS.md)                                                         RW               Gets or sets the number of characters on the server.
  [CLEARLISTS](./CLEARLISTS.md) *mask*                                        W                Removes all LISTs whose name contains *mask*.
  [CLEARVARS](./CLEARVARS.md) *prefix*                                        W                Removes all VARs that start with the given prefix.
  [CLIENTS](./CLIENTS.md)                                                     R                Gets the total number of connected clients.
  [CONSOLE](./CONSOLE.md) *command*                                           W                Executes *command* as if it had been typed directly into the server console.
  [EXPORT](./EXPORT.md) *file, flags, distance*                               W                Exports all objects within *distance* tiles of SRC to a file. (Flags: 1 = Items, 2 = Characters, 3 = Both)
  [GARBAGE](./GARBAGE.md)                                                     W                Forces an immediate garbage collection (checks for invalid objects and fixes them if possible, or else removes them).
  [GMPAGES](./GMPAGES.md)                                                     R                Returns the total number of GM pages.
  [GUILDS](./GUILDS.md)                                                       R                Returns the total number of guild *and* town stones.
  [GUILDSTONES](./GUILDSTONES.md).COUNT                                       R                Returns the total number of guild stones on the server.
  [HEARALL](./HEARALL.md)                                                     RW               Gets or sets whether player speech is logged to server console and log file.
  [IMPORT](./IMPORT.md) *file, flags, distance*                               W                Imports previously exported items that were within *distance* tiles. (Flags: 1 = Items, 2 = Characters, 3 = Both)
  [INFORMATION](./INFORMATION.md)                                             W                Displays server information to SRC.
  [ITEMS](./ITEMS.md)                                                         RW               Gets or sets the number of items on the server.
  [LOAD](./LOAD.md) *file*                                                    W                Loads a script file.
  [LOG](./LOG.md) *message*                                                   W                Logs *message* to server console and logs.
  [LOOKUPSKILL](./LOOKUPSKILL.md) *skill_name*                                R                Looks up a skill name or key, and returns its skill number.
  [MAP](./MAP.md)*.map_num.*ALLSECTORS *command*                              W                Executes *command* on all sectors of a map.
  [MAP](./MAP.md)*.map_num.*SECTOR.*sector_num command*                       RW               Executes *command* on sector *sector_num* of a map.
  [MAPLIST](./MAPLIST.md)*.map_num*                                           R                Returns 1 if *map_num* is a valid map number.
  [MAPLIST](./MAPLIST.md)*.map_num*.BOUND.X                                   R                Returns the maximum X coordinate for a map.
  [MAPLIST](./MAPLIST.md)*.map_num*.BOUND.Y                                   R                Returns the maximum Y coordinate for a map.
  [MAPLIST](./MAPLIST.md)*.map_num*.CENTER.X                                  R                Returns the central X coordinate of a map.
  [MAPLIST](./MAPLIST.md)*.map_num*.CENTER.Y                                  R                Returns the central Y coordinate of a map.
  [MAPLIST](./MAPLIST.md)*.map_num*.SECTOR.COLS                               R                Returns the number of sector columns on a map.
  [MAPLIST](./MAPLIST.md)*.map_num*.SECTOR.QTY                                R                Returns the number of sectors on a map.
  [MAPLIST](./MAPLIST.md)*.map_num*.SECTOR.ROWs                               R                Returns the number of sector rows on a map.
  [MAPLIST](./MAPLIST.md)*.map_num*.SECTOR.SIZE                               R                Returns the size of the sectors on a map.
  [MEM](./MEM.md)                                                             R                Returns the total amount of memory being used, in kilobytes.
  [PRINTLISTS](./PRINTLISTS.md) *LOG*                                         W                Displays a list of all LISTs to SRC, or the server console.
  [REGEN](./REGEN.md)0                                                        RW               Gets or sets the length of time it takes for characters to regenerate 1 health point, in seconds.
  [REGEN](./REGEN.md)1                                                        RW               Gets or sets the length of time it takes for characters to regenerate 1 mana point, in seconds.
  [REGEN](./REGEN.md)2                                                        RW               Gets or sets the length of time it takes for characters to regenerate 1 stamina point, in seconds.
  [REGEN](./REGEN.md)3                                                        RW               Gets or sets the length of time it takes for characters to lose 1 food point, in seconds.
  [RESPAWN](./RESPAWN.md)                                                     W                Respawns all dead NPCs (not corpses) in the world.
  [RESTOCK](./RESTOCK.md)                                                     W                Restocks all NPCs in the world.
  [RESTORE](./RESTORE.md) *file, account_name, character_name*                W                Restores a player character from a backup save.
  [RESYNC](./RESYNC.md)                                                       W                Checks all script files for any changes made since they were last loaded.
  [RTICKS](./RTICKS.md)                                                       R                Returns the real-world time, as a timestamp.
  [RTICKS](./RTICKS.md).FORMAT *timestamp, format*                            R                Returns the real-world timestamp as a formatted datetime string.
  [RTICKS](./RTICKS.md).FROMTIME *year, month, day, hour, minutes, seconds*   R                Returns the specified real-world time, as a timestamp.
  [RTIME](./RTIME.md)                                                         R                Returns the real-world time, as a formatted string.
  [RTIME](./RTIME.md).FORMAT *format*                                         R                Returns the real-world time, as a formatted string. More information : [Serv.rtime.format](./Servrtimeformat.md)
  [SAVE](./SAVE.md) *force_immediate*                                         W                Begins a world save. If background saving is enabled, *force_immediate* can be used to force a foreground save.
  [SAVECOUNT](./SAVECOUNT.md)                                                 R                Returns the number of world saves that have taken place.
  [SAVESTATICS](./SAVESTATICS.md)                                             W                Performs a statics save.
  [SHRINKMEM](./SHRINKMEM.md)                                                 W                Temporarily reduces memory usage.
  [SHUTDOWN](./SHUTDOWN.md) *time*                                            W                Schedules a server shutdown in *time* minutes.
  [SYSCMD](./SYSCMD.md) *cmd*                                                 W                Executes *cmd* and waits for it to finish executing. Returns \<0 if an error occurred. Requires OF_FileCommands.
  [SYSSPAWN](./SYSSPAWN.md) *cmd*                                             W                Executes *cmd* and does not wait for the program to finish executing. Returns \<0 if an error occurred. Requires OF_FileCommands.
  [TICKPERIOD](./TICKPERIOD.md)                                               R                Returns how much server ticks are in a real-world second.
  [TIME](./TIME.md)                                                           R                Returns the total server uptime, in tenths of a second.
  [TIMEHIRES](./TIMEHIRES.md)                                                 R                X branch only. Returns the internal timer in milliseconds.
  [TIMEUP](./TIMEUP.md)                                                       R                Returns the server uptime, as second.
  [TOWNSTONES](./TOWNSTONES.md).COUNT                                         R                Returns the total number of town stones on the server.
  [UNBLOCKIP](./UNBLOCKIP.md) *address*                                       W                Unblocks a previously blocked IP address.
  [VARLIST](./VARLIST.md) *LOG*                                               W                Displays a list of all VARs to SRC, or the server console.
  [VERSION](./VERSION.md)                                                     R                Returns the SphereServer version.
  --------------------------------------------------------------------------------- ---------------- -----------------------------------------------------------------------------------------------------------------------------------

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Objects](./_Objects.md)
