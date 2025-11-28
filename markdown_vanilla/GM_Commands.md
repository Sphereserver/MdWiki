GM Commands

ADD \# - GM & COUNSELOR Adds an item to the world. If the itemnumber (#)
is left out, a gump menu will be displayed with different menu options
of what can be created. The current gump this command produces is
limited. Item numbers are listed in the items.scp file. In X branch, the
command accepts a second parameter to set the amount of the item about
to be created.

.ADMIN - GM & COUNSELOR This will display a menu that allows you to do a
variety of things without having to enter the commands by hand. Most of
the commands listed below are included in this menu.

.ADDNPC \# - GM Adds an NPC to the world. NOTE: This method of adding
NPCs will result in an NPC which is not associated with a spawn point.
The added NPC will respawn after death at the point of creation. The
only way to remove an NPC created by this method is to .REMOVE it while
it's alive.

.ALLMOVE - GM This makes it possible for the you to move items not
normally movable, i.e. items whose properties have been set to make them
non moveable.

.ALLCLIENTS - GM This command brings all clients to your location in the
game. This is a dangerous command on large shards as it may crash
clients in heavily populated servers when used. Syntax: .SERV.ALLCLIENTS
GO x VERIFY: where x is the x,y,z location?

.ANIM \# - GM & COUNSELOR Performs the selected (#) animation. Refer to
Inside UO to see Animation Numbers.

.BANK or .BANK \# - GM If no \# is supplied, it opens the bankbox of the
selected character. (A target cursor appears after the command is
entered.) For the \# command, use 1A,1B or 1C for vendor storage areas.
1A is the main vendor stock. Items put in here are periodically
restocked. Use the SETZ command to set the restock count. 1B is the area
vendors store things they have bought from players. 1C is the list of
items that vendors will buy from players but not actually stock.

.BANKSELF - GM This will open your personal bank box.

.BLOCKIP \#.#.#.# - ADMIN Block an IP. Only blocks full IP's, not ranges
See also: UNBLOCKIP

.CAST \# - GM Attempts to cast spell \#.

.CLOCK - ADMIN Displays timing/clock information. Usable for debugging.

.COLDCHANCE \# - GM Set the % chance of snow in a 64x64 map tile area.
Settings are saved in the worldfile.

.RAINCHANCE \# - GM Set the % chance of rain a 64x64 map tile area.
Settings are saved in the worldfile.

.CONTROL - GM Gain possession of the PC/NPC selected. WARNING: .CONTROL
is very useful for on the fly quests, but be warned! Your original body
will assume the characteristics (NPC BRAIN) of the new body you intend
to inhabit. Your original body may wander off. To prevent this use the
.set flags 4 command on your original body to keep it paralyzed while
you inhabit the new body. If your old body was a ghost, the ghost is
deleted. All newbie items are carried with you as you move. Create a
newbie backpack inside your main pack and all items in the pack will be
carried with you.

.CLIENTIS3D - ADMIN Returns 1 if client is 3D.

.CLIENTISENHANCED - ADMIN Returns 1 if client is enhanced.

.CLIENTISKR - ADMIN Returns 1 if client is Kingdom Reborn.

.CLIENTS - GM Lists all the clients currently connected to the server.

.xCRIMINAL - GM Sets a character as criminal, more useful when used in a
script trigger. Leave the x off if you wish yourself to be the target.

.DEBUG - GM Toggles debug mode of the invoking client. All objects look
like visible worldgems. All creatures look like white humans and do not
animate. all objects will appear at the same Z level as the viewer. This
is a good way to remove a house or a ship, enter .DEBUG mode and .REMOVE
the structure or ship object gem.

.DETAIL - GM & COUNSELOR Toggles detail level on system messages.
Defaults to ON, and it gives you information when people log on and off
the server.

.xDISCONNECT - GM Will disconnect a client character without blocking
the account. Great for characters that are stuck in-game after a crash.
Leaving off the x will disconnect your client.

.DRY - GM Turn off rain and snow in this quadrant of the world.

.DUPE - GM Duplicates the selected object.

.xEDIT - GM Allows you to edit the contents of any container, including
NPC and Player Characters

.EXPORT- filename.scp <boolean> \# ADMIN Exports the whole or a part of
the world to a file. Syntax: .EXPORT filename.scp exportchar
pacesfromyou Comment: exportchar is 1 or 0 ; pacesfromyou is \# of
paces. Example: .EXPORT tailorshop.scp 1 10

.EXTRACT - filename ADMIN Extracts multi items out of the MULTI.MUL
file. Syntax: .EXTRACT multi.txt Comment: This will create the multi.txt
file, after which you need to edit the file and change the header Sample
Header: XXX template id change the XXX to 1 and import with /MULTI 1

.FIX - GM & COUNSELOR Attempt to set the Z coordinates after a teleport.

.FIXWEIGHT - GM Recalculates the weight of the selected character. For
use when weight gets outside of normal range due to scripting errors or
resync problems.

.xFLIP - GM & COUNSELOR Attempt to flip the item to it's directionally
different equivalent. (ex. right and left handed stacks of hides or
change the facing direction of a creature.), as allowed by the game art.
This will rotate characters or corpses as well as change the shape of
light sources. Not all settings for the flips are correct. If you find
an error, please report it in our bug forum including the base ID of the
flipped item.

.xFOLLOWED - GM Allows a GM to follow any targeted char. Toggle war mode
to cancel

.x FORGIVE - GM & COUNSELOR Release someone who has been jailed using
the /jail command. Leave off the X if you wish to target yourself

.GM - GM Toggle GM mode for testing as player. Also handy for wandering
around incognito.

.GMPAGE - GM Enter a page request into the page que.

.GO X Y Z - GM & COUNSELOR Teleports to the selected X, Y, Z
coordinates.

.GOCHAR \# - GM & COUNSELOR Teleport to the selected (#) character. Good
mostly for random player checking. If there are 5 characters in the
game, valid values for \# are 0, 1, 2, 3 or 4.

.GOCLI \# - GM & COUNSELOR Teleport to the selected (#) client on the
server. If there are 5 clients connected to the server, valid values for
\# are 0, 1, 2, 3 or 4.

.GOPLACE <string> - GM Teleport to the location, as named in
SPHEREmap.scp. Town names are used as default. Example: .GOPLACE Yew

.GOSOCK \# - GM & COUNSELOR Teleport to the client connected to the
selected (#) socket. If there are 5 sockets in use, valid values for \#
are 0, 1, 2, 3 or 4. The socketcodes are obtained on the console or from
the .CLIENTS list.

.GOUID \# - GM & COUNSELOR Teleports to the selected (#) UID
(gameobject). Every object in the game has a UID number as listed in the
world file. Going to a key code (MORE) will allow you to locate to
house, ship or container the key belongs to.

.HEARALL - GM Gives you the ability to hear all that is said in the
world.

.HUNGRY - GM & COUNSELOR Reports your current hunger level.

.IMPORT \#CHAR \#RANGE ADMIN - Imports an area from another server's
save file or from an UOX WSC-file. Syntax: /IMPORT FILENAME .(WSC or
SCP) \#CHAR \#RANGE Some fields are lost during conversion of UOX files,
type=x is sometimes not translated correctly. Remeber that the files to
be imported must end with \*.WSC or \*.SCP.

1.  CHAR - 1 = include characters in conversion, 0 = exclude characters.
2.  RANGE - This is a distance limit from the current location to
    import.

.INFO - GM & COUNSELOR Brings up an in game dialog for viewing and
modifying object attributes. A councilor may view, but not modify.

.INFORMATION - GM Displays information about the server.

.INVIS - GM This toggles the invisibility flag of the invoking client.
When the invisibility flag is set, you will not show up on .CLIENTS or
on tracking. You will however show up on the console Client list. You
will produce no words of power when you cast a spell. You can talk
normally.

.INVULNERABLE - GM This toggles the invulnerability flag of the invoking
client. This command makes the invoker invulnerable. NPC's wont attack
an invulnerable client (they aren't that stupid you know). When used on
a regular player, the player cannot do harm or be harmed.

.xJAIL \# or .xJAIL - GM & COUNSELOR Moves the selected player to a jail
cell. Leave the x off if you wish yourself to be the target. Valid cell
numbers are 1-10, if the number is left out, the selected player will be
moved to jailcell number 10.

.xKICK - GM Kicks the selected player off the server.

.KILL - GM Kills the selected PC/NPC.

.LAST - GM & COUNSELOR When the client is in target mode (cursor), this
command targets the invoking players last selected target. When a client
creates an object or a npc, the npc/object is automatically set to last
target. VERIFY: THIS FEATURE MAY HAVE BEEN REMOVED IN RECENT VERSIONS.

.LIGHT \# - GM Sets light level for a 64x64 map tile area. It is saved
in the world file. The lightlevels (#) range from 1 (brightest) to 19
(darkest). In T2A light levels range from 1 - 30.

.LINK - GM Links two objects together. This command is most commonly
used to link two doors in the same doorframe together so that with a
single click they both open. This command may also be used to link a key
to a door.

.LISTEN - GM See HEARALL.

.MOVE X,Y - GM Move your (or a target's) x or y position. Example: .MOVE
0,10 will move your character 10 paces along the y axis (south)

.MOVE - 10,0 will move your character 10 paces along the x axis (east)
Use negative numbers for moving north and west.

.MULTI \# - ADMIN Places a multi object into the world. The .MULTI
command is used with the multi.txt file which lists large items made up
of multiple images like the telescope or shrines.

.MUSIC \# - GM & COUNSELOR Plays the music code supplied.

.NUDGEDOWN - GM Shift the Z level of an item down by one.

.NUDGEUP - GM Shift the Z level of an item up by one.

.NUKE - GM Deletes the items in a selected area. This is the opposite of
the TILE command. When you invoke this command you will be prompted for
two points (via targeting cursor) that should reflect the
rectangle/square you want deleted. WARNING: If you are standing on the
roof of a tower and delete a range of objects, all objects in all Z
levels of the building will be deleted within the selected range.

.NUKECHAR - ADMIN Deletes the character(s) in a selected area. When you
invoke this comment you will be prompted for two points (via
targetingcursor) that should reflect the rectangle/square you want the
NPC's deleted from. WARNING: If you are standing on the roof of a tower
and delete a range of objects, all objects in all Z levels of the
building will be deleted within the selected range.

.PAGE <letter> - GM & COUNSELOR Displays the GM page queue. The page
command have several flags, below are listed the most common.

.PAGE D - Disposes the current page.

.PAGE L - Lists the page queue.

.PAGE O - Go to the Origin point of the page.

.PAGE P - Go to the current location of the calling Player.

.PAGE Q - Send page back to Queue.

.PAGE CURRENT or

.PAGE ? - Displays information about the Current selected page.

.PAGE K - .Kick the player who made the page. Only works if they are
online.

.PAGE BAN - Ban the player who made the page and lock their account.

.PAGE JAIL - Send the calling player to jail. Only works if they are
online.

.PAGE OFF - Turns of intrusive page notify messages.

.PAGE ON - Turns on intrusive page notify messages.

.PASSWORD - GM & COUNSELOR Changes your account password. This command
clears your current password, you will then need to log out and log in
using your new choice of password.

.PRIVSHOW - GM Turn on or off the privilege label showing on the
paperdoll. For example GM Joe becomes simply Joe. The privs remain
intact but players cannot see the GM tag.

.PRIVSET \# or .SETPRIV \# - ADMIN Sets a characters privilege level.
LEVEL 0 PLEVEL_Guest Restricted Guest Account, ie. can't PK LEVEL1
PLEVEL_Player Player or NPC LEVEL2 PLEVEL_Counsel Can travel (teleport)
LEVEL3 PLEVEL_Seer Can add items and NPC's but cannot directly affect
players \<\<-- broken LEVEL 4 PLEVEL_GM GM Command Clearance LEVEL 5
PLEVEL_Dev Developement Clearence, not bothered by GM LEVEL 6
PLEVEL_Admin Can Switch into and out of GM mode

.POLY \#### - GM Polymorph into the selected NPC, by ID hex number

.PROPS- GM See INFO.

.RAIN - GM Make it rain in the immediate 64 x 64 map tile area of the
world.

.RAINCHANCE \# - GM Set the % chance of rain in a 64x64 map tile area.
Settings are saved in the world file.

.REGION \# <binary> - GM Change the default map settings for the area
you are currently in. Options are defined on the SPHEREmap.scp file.

.REMOVE - GM Permanently remove the item or character from the game.
This cannot be used on players. It will also remove all the contents of
a container or corpse so be careful.

.REPAIR - GM Attempt to repair the selected item

.RESEND - GM & COUNSELOR Reload all objects and chars on screen for the
client. Used to fix some sorts of display problems.

. RESPAWN - GM Respawns all dead monsters in the world, ahead of their
regular schedule on the spawn bit timer.

.RESTOCK - GM Restocks the monster spawns and the vendors in the current
quadrant of the world.

.RESTOCK ALL - GM Restocks the monster spawns and the vendors in the
whole world.

.RESYNC - GM See RESEND.

.SAVE

or

.SAVE \# - GM Force an immediate world save.

.SAVE - If background save is enabled, .SAVE 1 forces a fast foreground
save .

.SELF - GM & COUNSELOR When the client is in target mode (cursor), this
command targets the invoking player. VERIFY: THIS FEATURE MAY HAVE BEEN
REMOVED IN RECENT VERSIONS.

.SEND \# - ADMIN Sends a string of bytes to the client. DANGEROUS! The
\# represents the string of bytes you want to send to the client.

.SET \#PROP \#VAL - GM Modify any property of an item or character.
There are many many properties. This is probably the most useful in game
command in the server. See the Properties explanation in the Customizing
your SPHERE area of the SPHERE Support menu. Syntax: /SET \#PROP \#VAL

1.  PROP = The property to be changed.
2.  VAL = The new value.

.SETZ - GM Sets the Z coordinate of the selected object. This is also
used for setting the restock count for items in vendor vaults. See the
BANK command for this.

.SHOW - GM Command to show specific properties that may or may not be
listed in the .info dialogue.

.SFX \# - GM Plays the selected sound code.

.SHRINK - GM Turns the selected creature into a TYPE_FIGURINE object.
This does not work on players. For further help on what this command
actually does, summon a horse and use SHRINK on it, then play around
with the figurine. If you want to turn it back into a real horse again,
doubleclick the figurine.

.SERV.SHUTDOWN \# - GM & COUNSELOR Shuts down the server in \# minutes.
VERIFY .SHUTDOWN \# or .SERV.SHUTDOWN \#

.SNOW - GM Make it snow is in this quadrant of the world.

.SPLIT - GM Allows you to separate from your body to become a ghost. It
leaves your current body behind as an NPC.

.STATIC - GM Sets the targeted item as unmovable. Also may be used
instead of /ADD to add items preset to static.

.SUICIDE - GM & COUNSELOR Mostly used in triggers but may be used in
game.

.SYNC - GM & COUNSELOR See .RESEND.

.SYSMESSAGE <text> - GM Sends a system message. Example:

.SYSMESSAGE - This SPHERE is shutting down in 10 minutes.

.TELE - GM & COUNSELOR Teleport to selected location.

.TILE - GM Lay a blanket of tiles (objects) on the selected area and at
the selected Z-coordinate. Syntax: /TILE \#Z \# The \#Z is the height
(Z-coordinate) at which height you want your area fill to appear. The
item number (#) is what item from the SPHEREITEM.SCP file you want the
area filled with. When you invoke this comment you will be prompted for
two points (via targeting cursor) that should reflect the
rectangle/square you want filled.

.TWEAK - GM See .INFO.

.TYPEDEF - GM This will allow access to the base class information like
SELLVALUE and BUYVALUE. This information will not be saved as it exists
only in the SPHEREITEM.SCP file but it will allow you to play with this
a bit.

.UNBLOCKIP ADMIN - Unblock the IP that was previously blocked See also:
BLOCKIP VERIFY USAGE: .UNBLOCKIP \#.#.#.#

.UNDERWEAR - GM & COUNSELOR For removing the default underwear from PC
and NPC chars.

.VERSION - GM Displays current server version.

.WEBLINK - GM Launches your system's browser and loads the SPHERE page.

.WHERE - GM & COUNSELOR This command tells you your current X Y and Z
coordinates in the world.

.XGO - GM Teleports a PC/NPC or an object to the selected coordinates.
Syntax: .GO \#X \#Y \#Z
