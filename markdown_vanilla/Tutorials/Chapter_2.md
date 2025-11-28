## spheretables.scp

Spheretables.scp is the very first file read by SPHERE after SPHERE.ini,
and therefore it is the most important. Almost all of the secondary
settings are contained within this file, wich makes this very important.
Now, let's talk about this very important file in topics:

== <font color="darkred">\[RESOURCES\]</font> ==

The first thing you'll see when you open this file is a list of
resources. This is marked by (SURPRISE!) a \[RESOURCE\] tag. It looks
something like this:

<font color="darkblue">`[RESOURCES]`  
`scripts/sphere_defs.scp`  
`scripts/sphere_book.scp`  
`scripts/sphere_backward_compatibility.scp`  
`scripts/sphere_events_human.scp`  
`scripts/sphere_events_npcs.scp`  
`scripts/npcs/`  
`...`  
</font>

This tells sphere what files to load and in what order to do so. You
must change it carefully sometimes, put scripts with a lot of DEFNAMES,
REGIONS, and other global used settings first, to avoid errors when
sphere starts (although those errors won't harm your server). For
example, we looked at a gold script in Chapter 1 that had a line like
this:

<font color="darkred">TYPE=t_gold</font>

Now, unless SPHERE loads sphere_defs.scp before the script containing
the gold, it will have no idea what t_gold means, and will give you an
error. This is because t_gold is defined within sphere_defs.scp.

Item files should be loaded before template files, and finally character
files. Other files may come after this, but these particular files must
load in that order. The loot on monsters is comprised of items and
templates, and unless SPHERE has already loaded the file containing
these items and templates, you will get hundreds of fun errors to track
down and correct. Actually, it isn't very hard to correct, but it's
irritating to start up the program and have a thousand errors scroll up
your screen.

**Note**: *You can make sphere load a full folder instead of putting
each file, that's why we have this <font color="darkred">scripts/</font>
as the last file on the \[RESOURCES\] tag, so sphere loads all other
scripts that might have been out of the list.*

== <font color="darkred">\[OBSCENE\]</font> ==

The next section is self-explanatory, \[OBSCENE\]. This defines "illegal
names". If a player creates a character with a name on this list, it
will tell him that the name is unavailable and to pick another. If you
are a punk who enjoys cussing at others, this list might be a good place
to expand your knowledge of obscenities.

== <font color="darkred">\[NOTOTITLES\]</font> ==

This defines the title that will be shown related to the player's karma.
Do not touch this section. If you remove a line inadvertently, your
server WILL NOT RUN. Only change them.

== <font color="darkred">\[PLEVEL X\]</font> ==

These sections define the commands available to the various account
plevels. Any command not listed is automatically assumed to be in the
plevel 4 category. This includes self-defined functions (see [Chapter
6](Chapter_6 "wikilink")). As you can see, there is quite an extensive
list of functions and commands.

**Note**: *You don't have to put every function you make in this section
as you can have various sections in different scripts, although I
recommend that you put them here just for organization purposes.*

== <font color="darkred">\[RUNES\]</font> ==

This is the list of those words you say when casting a spell (An, Lor,
In, etc). You can play with them, but it'll become very confusing. =P

## Sphere.ini

Sphere.ini contains all of the internal options for the Sphere emulator.
In order to configure your shard, this is the file you will start with.
In order to explain this better, I'm just going to add more explanatory
comments throughout the file. My comments and additions/changes will be
in **bold text**.

<font color="darkred">`//****************************************************************************`  
`// SPHERE by : Menasoft 1997-2003`  
`// www.sphereserver.com`  
`// All SPHERE script files and formats are copyright Menasoft & Partners.`  
`// This file may be freely edited for personal use, but may not be distributed`  
`// in whole or in part, in any format without express written permission from`  
`// Menasoft & Partners. All donations and contributions`  
`// become the property of Menasoft & Partners.`  
`//****************************************************************************`  
</font>  
<font color="darkblue">`///////////////////////////////////////////////////////////////`  
`//////// General Information`  
`///////////////////////////////////////////////////////////////`  
</font>  
`[SPHERE]`  
`// Name of your Sphere shard`  
`ServName=`**`WarAngel's Test Centre`**  
`// The IP of your server, this will be 127.0.0.1 almost always`  
`ServIP=127.0.0.1`  
`// The port of your server, this is 2593 by default`  
`ServPort=2593`  
  
`// Admin's contact email`  
`AdminEmail=`**`warangel999@msn.com`**  
`// Web page for this server`  
`URL=www.myshard.com Replace www.myshard.com with your shard's URL'`  
`// GMT offset, from -12 to +12 [London=0, EST=5, etc]`  
`TimeZone=`**`-5 Eastern Time (US & Canada). Change this to fit your timezone`**  
  
`// Official staff language`  
`Lang=English`  
`// Start this as a system service on Win2000, XP, NT`  
`NTService=0 `**`Enabling this removes the ability to use the console.`**  
  
`// MySql configuration.`  
`//MYSQL=0 `**`Set this to =1 to enable MySQL`**  
`//MySqlHost=`**`localhost This will almost always be localhost if the MYSQL host is located on the same computer as your shard`**  
`//MySqlUser=`  
`//MySqlPassword=`  
`//MySqlDatabase=`  
  
<font color="darkblue">`///////////////////////////////////////////////////////////////`  
`//////// File Locations`  
`///////////////////////////////////////////////////////////////`  
</font>` // Directory where spheretables.scp is located, from there we will`  
`// load any additional scripts`  
`ScpFiles=scripts/`  
  
`// Where your sphereworld.scp and spherechars.scp are located`  
`WorldSave=save/`  
  
`// Where your sphereaccu.scp and sphereacct.scp is located`  
`AcctFiles=accounts/`  
  
`// Where your UO installation is located. This need: map0.mul, statics0.mul,`  
`// staidx0.mul, multi.mul, multi.idx, hues.mul, tiledata.mul.`  
`// Optional files: verdata.mul, mapX.mul/staticsX.mul/staidxX.mul for higher`  
`// maps support (Malas, etc).`  
`//`  
`// Note that if not set, sphere will scan windows registry to auto-detect it`  
`//MulFiles=mul/`  
  
`// Where your log files will be saved by sphere`  
`Log=logs/`  
  
<font color="darkblue">`///////////////////////////////////////////////////////////////`  
`//////// World Save Information`  
`///////////////////////////////////////////////////////////////`  
</font>` // How often for Sphere to save your world (minutes)`  
`SavePeriod=20`  
  
`// How many backup levels to keep. Each level means 7 backups done for it.`  
`// So, 10*7 = 70 backup saves will be storied.`  
`BackupLevels=10`  
  
`// On would save in the background quietly over a longer period of time, and not interrupt the game`  
`// Off would notify "World save has been initiated" and save faster, but pause the game momentarily`  
`SaveBackground=0`  
  
<font color="darkblue">`///////////////////////////////////////////////////////////////`  
`//////// Account Management`  
`///////////////////////////////////////////////////////////////`  
</font>` //Code for servers account application process`  
`// 0=Closed, // Closed. Not accepting more.`  
`// 2=Free, // Anyone can just log in and create a full account.`  
`// 3=GuestAuto, // You get to be a guest and are automatically sent email with u're new password.`  
`// 4=GuestTrial, // You get to be a guest til u're accepted for full by an Admin.`  
`// 6=Unspecified, // Not specified.`  
`// To enable auto account you must set this to 2`  
`AccApp=0`  
  
`// Store password hashed with MD5 `**`MD5 is a safer encryption method for saving passwords. More information on it `[`here`](http://en.wikipedia.org/wiki/MD5)**  
`Md5Passwords=0`  
  
`// local ip is assumed to be the admin`  
`LocalIPAdmin=1`  
  
`// Number of chars allowed per account`  
`MaxCharsPerAccount=5`  
  
`// Min time for a char to exist before delete allowed (in seconds)`  
`MinCharDeleteTime=3*24*60`  
  
`// Max number of Guest accounts allowed`  
`GuestsMax=0`  
  
<font color="darkblue">`///////////////////////////////////////////////////////////////`  
`//////// Client Management`  
`///////////////////////////////////////////////////////////////`  
</font>` // What client protocol version used`  
`// Comment out the ClientVersion line to allow any client that is supported.`  
`//ClientVersion=2.0.3`  
  
`// Set this to 0 to block login to encrypted clients `**`Default client uses encryption`**  
`UseCrypt=1`  
  
`// Set this to 1 to allow login to unencrypted clients `**`You can use tools such as `[`UO Rice`](http://stud4.tuwien.ac.at/~e9425109/UO_RICE.htm)` and `[`UOGateway`](http://www.uogateway.com/)` to remove encryption on a client`**  
`UseNoCrypt=0`  
  
`// Maximum total open connections to server`  
`ClientMax=256`  
  
`// Maximum open connections to server per IP`  
`ClientMaxIP=16`  
  
`// Maximum total (not-in-game) connections to server`  
`ConnectingMax=32`  
  
`// Maximum total simultaneous (not-in-game) connections to server per IP`  
`ConnectingMax=8`  
  
`// How long logged out clients linger in seconds`  
`ClientLinger=15`  
  
`// Walk limiting code: buffer size (in tenths of second)`  
`WalkBuffer=75`  
  
`// Walk limiting code: regen speed (%)`  
`WalkRegen=25`  
  
`// Only commands issued by this plevel and higher will be logged`  
`CommandLog=0 `**`0 means that all commands will be logged`**  
  
`// Prefix for ingame commands`  
`CommandPrefix=.`  
  
`// Use the built in http server`  
`UseHttp=1`  
  
`// Use the built in god port`  
`UseGodPort=0 `**`This is for use with the God client`**  
  
`// Default setting for all accounts specifying default resdisp. Recommended`  
`// specifying at least 1 (T2A) here.`  
`//AutoResDisp=0 `**`0=automatic detect, 1=T2A, 2=LBR, 3=AoS, 4=SE, 5=ML`**  
  
`// Default setting for new accounts specifying default priv level`  
`//AutoPrivFlags=010`  
  
<font color="darkblue">`///////////////////////////////////////////////////////////////`  
`//////// Game Mechanics`  
`///////////////////////////////////////////////////////////////`  
</font>` // Do not allow entering under roof being on horse?`  
`MountHeight=0`  
  
`// Archery does not work if too close (0 = not checked)`  
`ArcheryMinDist=2`  
  
`// Maximum Distance for Archery`  
`ArcheryMaxDist=15`  
  
`// Speed scale factor for weapons `**`Formula is now DELAY = SPEEDSCALEFACTOR /((DEX + 100) * SPEED)`**  
`SpeedScaleFactor=15000`  
  
`// This is the percent of max weight at which stamina is lost half the time`  
`// (200 = no effect)`  
`StaminaLossAtWeight=150`  
  
`// Weight penalty for running +N% of max carry weight (0 = no effect)`  
`RunningPenalty=50`  
  
`// Show people joining/leaving the server`  
`ArriveDepartMsg=1`  
  
`// Are house and boat keys newbied automatically`  
`AutoNewbieKeys=1`  
  
`// Maximum number of items allowed in bank`  
`BankMaxItems=1000`  
  
`// Maximum weight in stones allowed in bank`  
`BankMaxWeight=1000`  
  
`// If 1 vendors will take gold only from backpack`  
`PayFromPackOnly=0 `**`If set to 0, vendors also take gold from the bank`**  
  
`// Disable weather effects?`  
`NoWeather=1`  
  
`// Default light level in dungeons`  
`DungeonLight=27 `**`0 is brightest, 30 is darkest`**  
  
`// Day light level 0-30 `**`0 is brightest, 30 is darkest`**  
`LightDay=0`  
  
`// Night light level 0-30`  
`LightNight=25`  
  
`// Wool Regen Time (in minutes)`  
`WoolGrowthTime=30`  
  
`// Suppress player speech with 75% of capital letters`  
`SuppressCapitals=0`  
  
`// Extra combat flags to control the fight (default:0, 0.55i compatible)`  
`// COMBAT_NODIRCHANGE 00001 // not rotate player when fighting (like was in 0.51a)`  
`// COMBAT_FACECOMBAT 00002 // allow faced combat only (recommended)`  
`//CombatFlags=0 `**`If both of these are enabled, it means the player has to keep turning to face his opponent in order to strike`**  
  
<font color="darkblue">`///////////////////////////////////////////////////////////////`  
`//////// NPC/Item/Player Management`  
`///////////////////////////////////////////////////////////////`  
</font>` // Distance in tiles before an NPC that's wandered too far from it's home will teleport back`  
`LostNPCTeleport=50`  
  
`// Wether PCs get a resurrection robe when they get resurrected.`  
`NoResRobe=0`  
  
`// Time for a NPC corpse to decay mins`  
`CorpseNPCDecay=10`  
  
`// Time for a playercorpse to decay mins`  
`CorpsePlayerDecay=15`  
  
`// Base decay time in minutes for items`  
`DecayTimer=30`  
  
`// Put [NPC] tags over chars `**`or [TAME], if the creature is tamed`**  
`CharTags=0`  
  
`// Flip dropped items`  
`FlipDroppedItems=0`  
  
`// Monsters run when scared of death`  
`MonsterFear=0`  
  
`// Monsters may fight each other`  
`MonsterFight=0`  
  
`// Percent setting of the all NPC move rate, default 100`  
`MoveRate=100`  
  
`// Do players receive sounds`  
`GenericSounds=1`  
  
`// Max number of items to sell to one person at once`  
`VendorMaxSell=255`  
  
`// Max level npc trainers can go`  
`NPCTrainMax=300 `**`300 is 30.0 skill`**  
  
`// Percent of own ability npcs can train to`  
`NPCTrainPercent=30`  
  
`// Max level of skill trainable on dummies, archery butte ect..`  
`SkillPracticeMax=300 `**`300 is 30.0 skill`**  
  
`// Max skill player's will start with on skills they haven't chosen during char create`  
`MaxBaseSkill=200 `**`Set this to 0 for players to start with no skills other than the selected ones`**  
  
`// Time in seconds for hitpoint regeneration`  
`Regen0=40`  
  
`// Time in seconds for mana regeneration`  
`Regen1=20`  
  
`// Time in seconds for stamina regeneration`  
`Regen2=10`  
  
`// Time in seconds for food degeneration`  
`// 60*60*24 = 1 day of real life time`  
`Regen3=60*60*24`  
  
`// Speech block associated to players`  
`SpeechSelf=spk_player`  
  
`// Speech block associated to pets`  
`SpeechPet=spk_pet`  
  
`// When player skills/stats goes this times more than skillclass allowed, drop`  
`// them to skillclass level. Setting this to 0 disables the action.`  
`OverSkillMultiply=2`  
  
`// NPC AI settings`  
`// NPC_AI_PATH 0001 NPC pathfinding`  
`// NPC_AI_FOOD 0002 NPC food search (objects + grass) `**`This makes npcs look for food (specified on their FOODTYPE sections) and grass to eat`**  
`// NPC_AI_EXTRA 0004 NPC magics, combat, etc`  
`//NPCAI=0`  
  
<font color="darkblue">`///////////////////////////////////////////////////////////////`  
`//////// Crime/Murder/Karma/Fame/Guard Settings`  
`///////////////////////////////////////////////////////////////`  
</font>` // Karma when player goes from good to neutral (from -10000 to 10000)`  
`PlayerNeutral=-2000`  
  
`// How many minutes are criminals flagged for`  
`CriminalTimer=3`  
  
`// Times a player can snoop before becoming a criminal`  
`SnoopCriminal=20`  
  
`// Seconds time to decay a murder count (default 8*60*60 is 8 hours)`  
`MurderDecayTime=8*60*60`  
  
`// Amount of murders before we get title`  
`MurderMinCount=1`  
  
`// Looting or carving a blue player is a crime`  
`LootingIsaCrime=1`  
  
`// Flag players criminal for helping criminals?`  
`HelpingCriminalsIsaCrime=1`  
  
`// How long do guards linger about in minutes`  
`GuardLinger=3`  
  
`// Will guards kill instantly or follow normal combat rules`  
`GuardsInstantKill=1`  
  
`// Limits the MAXHITS/MAXMANA/MAXSTAM changes`  
`// STAT_FLAG_NORMAL 0x00 // MAX* status allowed (default)`  
`// STAT_FLAG_DENYMAX 0x01 // MAX* denied`  
`// STAT_FLAG_DENYMAXP 0x02 // .. for players`  
`// STAT_FLAG_DENYMAXN 0x04 // .. for npcs`  
`StatsFlags=0`  
  
<font color="darkblue">`///////////////////////////////////////////////////////////////`  
`//////// Server Mechanics`  
`///////////////////////////////////////////////////////////////`  
</font>` // Experimental flags`  
`// Flags for options that affect server behaviour and which might affect compatibility`  
`// See the revisions.txt file for more details on this`  
`// EF_DiagonalWalkCheck = 00000001`  
`// EF_UNICODE = 00000002 // No on Linux `**`Enables new Unicode fixes`**  
`// EF_Scripts_Ret_Strings = 00000004`  
`// EF_New_Triggers = 00000008`  
`// EF_Scripts_Parse_Verbs = 00000010`  
`// EF_Intrinsic_Locals = 00000020 //`**`Allows locals to be referenced differently. For example: <local.X> can be referenced as just `<X>**  
`// EF_Item_Strict_Comparison = 00000040 //`**`Disables similars items being compared instead of specific items, such as cloth, leather, hides, log, boards, arrow, bolt being compared when the server tries to find an arrow.`**  
`// EF_WalkCheck = 00000100 `**`//Fixes a lot of house looting bugs, and other walkchecking related problems.`**  
`// EF_Script_Profiler = 00000400`  
`// EF_Size_Optimise = 00000800`  
`// EF_Minimize_Triggers = 00001000 //Minimize trigger calls (use only 0.51 triggers)`  
`Experimental=00000`  
  
`// Option flags`  
`// Flags for options that affect server behaviour but not compatibility`  
`// See the revisions.txt file for more details on this`  
`// OF_Magic_IgnoreAR = 00000001 //`**`Does magic ignore a players armor statistics?`**  
`// OF_Magic_CanHarmSelf = 00000002 //`**`Can a player harm himself with magic? (using Magic Arrow to unparalyze oneself, for example)`**  
`// OF_Magic_StackStats = 00000004`  
`// OF_Archery_CanMove = 00000010 //`**`Can a player move and shoot at the same time?`**  
`// OF_Magic_PreCast = 00000020 //`**`Allow pre-casting of spells, or freeze a player in place while they cast?`**  
`// OF_Items_AutoName = 00000040`  
`// OF_FileCommands = 00000080 //`**`This enables all file commands, such as writefile, etc.`**  
`// OF_NoItemNaming = 00000100 //`**`If enabled, prevents Sphere from naming crafted items such as "sword craft by Player`**  
`// OF_NoHouseMuteSpeech = 00000200 //`**`Can players inside a house hear players outside, and vice-versa?`**  
`// OF_Multithreaded = 00000400 //`**`Do not set while server is running !!! (Make *Nix server unstable) Puts account handling in a second thread`**  
`// OF_Advanced_LOS = 00000800`  
`// OF_Flood_Protection = 00001000`  
`OptionFlags=0200`  
  
`// FeatureT2A, used to control T2A expansion features ( default 03 )`  
`// FEATURE_T2A_UPDATE 01 // Monster and Lost lands`  
`// FEATURE_T2A_CHAT 02 // In game chat`  
`FeatureT2A = 03`  
  
`// FeatureLBR, used to control LBR expansion features ( default 0 )`  
`// FEATURE_LBR_UPDATE 01 // Lbr Monsters`  
`// FEATURE_LBR_SOUND 02 // MP3 instead of MIDI`  
`FeatureLBR = 0`  
  
`// FeatureAOS, used to control AOS expansion features ( default 0 )`  
`// Enabling one of them automagically enables AoS basic features`  
`// FEATURE_AOS_UPDATE 01 // Basic AoS feature`  
`// FEATURE_AOS_POPUP 02 // Popup infos`  
`// FEATURE_AOS_DAMAGE 04 // Damage shown on hit`  
`// FEATURE_AOS_PALNECRO 08 // Fightbook and Paladin/Necro on char creation`  
`// FEATURE_AOS_TOOLTIP 010 // Tooltips`  
`FeatureAOS = 0`  
  
`// FeatureSE, used to control SE expansion features ( default 0 )`  
`// FEATURE_SE_UPDATE 01 // Basic SE features`  
`// FEATURE_SE_NINJASAM 02 // Ninja and Samurai`  
`FeatureSE = 0`  
  
`// FeatureML, used to control ML expansion features ( default 0 )`  
`// FEATURE_ML_UPDATE 01 // Basic ML features`  
`FeatureML = 0`  
  
`// In game effects to turn on and off`  
`// Messages echoed to the server console while in debug mode`  
`// DEBUGF_NPC_EMOTE = 0x0001`  
`// DEBUGF_ADVANCE_STATS = 0x0002`  
`// DEBUGF_WALKCODES = 0x0080 // try the new walk code checking stuff`  
`// DEBUGF_NPCAI = 0x0100 // some NPC AI debugging`  
`// DEBUGF_EXP = 0x0200 // experience gain/loss`  
`// DEBUGF_LEVEL = 0x0400 // experience level changes`  
`DebugFlags=0`  
  
`// Console Hears all that is said on the server`  
`HearAll=1`  
  
`// Secure mode attempts to ignore errors, protect from accidently shutdowns`  
`Secure=1`  
  
`// Value from 1 to 32, set sectors inactive when unused to conserve resources`  
`SectorSleep=10`  
  
`// Disconnect inactive socket in x min`  
`DeadSocketTime=5`  
  
`// Always force a full garbage collection on save`  
`ForceGarbageCollect=1`  
  
`// Time before restarting when server appears hung (in seconds)`  
`FreezeRestartTime=60`  
  
`// Length of the game world minute in real world in seconds`  
`GameMinuteLength=60`  
  
`// Bit Mask of the subjects you want to log when logging is on`  
`// LOGM_ACCOUNTS 0x00080`  
`// LOGM_SAVE 0x00200 // world save status.`  
`// LOGM_CLIENTS_LOG 0x00400 // all clients as they log in and out.`  
`// LOGM_GM_PAGE 0x00800 // player gm pages.`  
`// LOGM_PLAYER_SPEAK 0x01000 // All that the players say.`  
`// LOGM_GM_CMDS 0x02000 // Log all GM commands.`  
`// LOGM_CHEAT 0x04000 // Probably an exploit !`  
`// LOGM_KILLS 0x08000 // Log player combat results.`  
`// LOGM_HTTP 0x10000`  
`// 01ffff log everything`  
`LogMask=01ec80`  
  
`// Amount of time to keep map data cached in sec`  
`MapCacheTime=120`  
  
`// Max NPC chars for a sector to prevent lag`  
`MaxComplexity=32`  
  
`// Amount of items in one tile so start showing "too many items here"`  
`MaxItemComplexity=25`  
  
`// Amount of items in one sector to start showing "x items too complex"`  
`MaxSectorComplexity=1024`  
  
`// Limit the number of cycles the while/for loop can proceed. Setting this to`  
`// zero disables the limitation`  
`MaxLoopTimes=0`  
  
<font color="darkblue">`///////////////////////////////////////////////////////////////`  
`//////// Magic/Effects Settings`  
`///////////////////////////////////////////////////////////////`  
</font>  
`// Allow casting while equipped`  
`EquippedCast=1`  
  
`// Words of power for player using magic`  
`WOPPlayer=1`  
  
`// Words of power for staff using magic`  
`WOPStaff=0`  
  
`// Reagents lost if magic fails`  
`ReagentLossFail=0`  
  
`// Magic requires reagents`  
`ReagentsRequired=0`  
  
`// What % of hitpoints players will resurrect with. Note, that if you set this`  
`// too low, people with little STR will have problems resurrecting.`  
`HitPointPercentOnRez=33`  
  
`// How many % of hits will the character loose when starving. 0 disables`  
`//HitsHungerLoss=0`  
  
`// Amount of skill of lock picking needed to unlock a magically locked door`  
`MagicUnlockDoor=900`  
  
`// Teleport effect for GMs and players. Setting 0 disables the effect`  
`TeleportEffectStaff=03709`  
`TeleportEffectPlayers=0372a`  
  
<font color="darkblue">`///////////////////////////////////////////////////////////////`  
`//////// Experience and Level system`  
`///////////////////////////////////////////////////////////////`  
</font>  
`// Enable experience system`  
`//ExperienceSystem=0`  
  
`// Experience system settings:`  
`// 0001 gain experience in combat`  
`// 0002 gain experience in crafts`  
`// 0004 allow experience to go down`  
`// 0008 limit experience decrease by a range witheen a current level`  
`// 0010 auto-init EXP/LEVEL for NPCs if not set in @Create`  
`// 0020 allow trigger @ExpChange`  
`// 0040 allow trigger @ExpLevelChange`  
`//ExperienceMode=0`  
  
`// If combat experience gain is allowed, use these percents for gaining exp in`  
`// Player versus Monster and Player versus Player combats. Value 0 disables gain.`  
`//ExperienceKoefPVM=100`  
`//ExperienceKoefPVP=100`  
  
`// Enable levels system (as a part of experience system)`  
`//LevelSystem=0`  
  
`// Level system settings:`  
`// linear = 0 (each NextLevelAt exp will give a level up)`  
`// double = 1 (you need (NextLevelAt * (level+1)) to get a level up)`  
`//LevelMode=1`  
  
`// Amount of experience to raise to the next level`  
`//LevelNextAt=0`  
  
<font color="darkblue">`///////////////////////////////////////////////////////////////`  
`//////// Webpage Settings`  
`///////////////////////////////////////////////////////////////`  
</font>  
`// Note, that you can catch error codes by creating sphere404.htm and so on`  
`// for all HTTP error codes sphere support.`  
  
`[WEBPAGE 1]`  
`// Determines what html file is used as base for the status page`  
`WebPageSrc=scripts\web\spherestatusbase.html`  
`// Determines where the status page is saved`  
`WebPageFile=scripts\web\status.html`  
`// In seconds, how often the status file is updated`  
`WebPageUpdate=60`  
`// Required PLevel to view this page (0 = anyone, 6 = admins only)`  
`PLevel=0`  
  
<font color="darkblue">`///////////////////////////////////////////////////////////////`  
`//////// Abuse Control`  
`///////////////////////////////////////////////////////////////`  
</font>  
`// Block these ips from the server`  
`// 255 is a wildcard, so 255.255.255.255 disables anyone connecting.`  
`[BlockIP]`  
`//123.34.45.56`  
`//123.45.56.78`  
  
<font color="darkblue">`///////////////////////////////////////////////////////////////`  
`//////// Connection Information`  
`///////////////////////////////////////////////////////////////`  
</font>  
`//First line should be the name of your shard (this is what people see when they connect)`  
`//Second line should be the IP of your shard (this is almost always 127.0.0.1)`  
`//Third line should be the port of your shard (this should be whatever ServPort is set to)`  
  
`//Uncomment next 3 lines below this if you have a router`  
`//First line should be a name different than your shard name above this`  
`//Second line should be your real/external IP (www.whatismyip.com)`  
`//Third line should be the shard port (this should be whatever ServPort is set to)`  
`[SERVERS]`  
**`WarAngel's Test Centre`**  
`127.0.0.1`  
`2593`  
  
`//External`  
`//my.ip.goes.here`  
`//2593`  
  
`[EOF]`  

**MAPx** It isn't present in sphere.ini, but it can be used (just check
REVISIONS.txt). You use it like that:

MAPx=max_x,max_y,sector_size,real_map_number.

For example: MAP1=7168,4096,512,-1

will change map 1 size to 7168,4096, the sector sizes of map 1 to 512
tiles and the -1 means it'll call the default mul file for that map.

Another example:

MAP50=7168,4096,64,3

Will activate a map number 50 that has 7168,4096 as size, 64 as sector
size and loads map3.mul, statics3.mul and staidx3.mul as it's map file.

## sphere_region.scp

This script deals with the caracteristics of the places, like what you
can mine or lumber, what happens when you enter that place and that kind
of things. It also contains most of the resources sections. Let's start
by explaining those:

`[REGIONRESOURCE x]`

This section contains the the skill needed to gather that resource, what
resource it gives to the player and the time for it to regen. Let's take
a look at this example (you'll see a commented text "//t_tree" if you
have read the previous chapter you'll surelly know what this is, it's a
defname)

<font color="darkgreen">`[REGIONRESOURCE mr_tree]`</font>  
`// lumberjacking default`  
`// t_tree`  
`SKILL=1.0,80.0`  
`AMOUNT=9,30`  
`REAP=i_log`  
`REGEN=60*60*10`  

Basically this section defines a resource, something that you can gather
from the landscape. It compares skill and amount. This particular one
says that you may gather a maximum of 9 logs at 1.0 skill and a maximum
of 30 logs at 80.0 skill. Anything after that simply increases your
chances of getting 30 logs. See that SKILL line? The syntax is
SKILL=lower,high. And the AMOUNT line sets the AMOUNT=min,max. How does
it know what to give you? This line:
<font color="darkred">REAP=i_log</font>. This tells the server to create
an i_log item if this resource is taken. So you can put anything you
want to be gatherable in this REAP setting. The next line, REGEN,
defines how long this resource will take to reappear, in seconds. As we
can see here, it's 60\*60\*10 seconds, or 10 hours. As a GM, if you walk
around where players have been chopping wood or mining, you'll see
little worldgem bits all over the ground. They look like spawnpoints,
but are really resource markers. They mark where a specific resource has
been gathered, how much has been gathered, and what type of resource it
is. They also have a <font color="darkgreen">TIMER</font> which counts
down from this very high number (36000) and then decay when it reaches
zero.

<font color="darkgreen">`[REGIONTYPE r_default_rock t_rock]`</font>  
`//Random rocks`  
`RESOURCES=100.0 mr_nothing`  
`RESOURCES=500.0 mr_iron`  
`//RESOURCES=6.0 mr_rusty`  
`//RESOURCES=6.0 mr_old_copper`  
`//RESOURCES=6.0 mr_dull_copper`  
`//RESOURCES=4.5 mr_bronze`  
`RESOURCES=5.0 mr_copper`  
`RESOURCES=2.0 mr_gold`  
`RESOURCES=1.0 mr_rose`  
`RESOURCES=2.0 mr_agapite`  
`RESOURCES=1.0 mr_bloodrock`  
`RESOURCES=1.0 mr_silver`  
`RESOURCES=0.5 mr_verite`  
`RESOURCES=0.2 mr_Valorite`  
`RESOURCES=0.1 mr_mytheril`  
`RESOURCES=0.1 mr_blackrock`  
`RESOURCES=0.1 mr_diamond`  

Wow, you must be saying. What are all these things? mr_iron? mr_agapite?
I don't see those anywhere in the file. Now, I bet you'll go to
sphere_defs.scp to see if they are DEFNAMEs for something else. And the
truth is, they are, but the definitions can be found in
sphereitem_ore.scp.

`RESOURCES=50.0 mr_iron`

This should look slightly familiar. Would it look even more familiar if
the whole thing looked like this?

<font color="darkred">`RESOURCES={ mr_iron 50 mr_copper 5 mr_gold 2 mr_rose 2 ...etc... }`</font>

I bet it would, if you were paying attention during the earlier lessons
in Chapter 1. This is a weighted list of resources, in a slightly
different format than you're used to. But it works exactly the same way.
It's also one of the ONLY places in SPHERE scripting that you can use
fractional numbers like 0.1 or 0.2. Actually you can't use them here
either, but SPHERE successfully hides this as long as you use them in
ALL of the <font color="darkgreen">RESOURCES</font>. (By the way, do not
try to script a <font color="darkgreen">RESOURCES</font> identifier as a
random selector. SPHERE wont like that. Use the format provided to you.)

<font color="darkgreen">\[REGIONTYPE r_default_rock t_rock\]</font>
*Understanding:* That r_dafault_rock defines the defname of that
<font color="darkgreen">REGIONTYPE</font>, which is how you'll access it
in other scripts (wait for next section =P). The t_rock is the defname
(see <font color="darkblue">sphere_defs.scp</font> for it) of the type
of a rock, which shows sphere where your players can gather that
resource (you could change it to t_water so they could mine ores on
water, which isn't a good idea actually :P)

Hopefully that clears up the sphere_region.scp file for you. We'll tell
you in the next section how to use these REGIONTYPE settings to make
resources actually available in game.

## sphere_mapX.scp

Welcome to one of the easiest files in all of SPHERE. This is the
spheremap.scp file. It's also the only file that's almost completely
done for you. It is a very rare occasion that you need to change this
file.

Actually, on that note, I might as well say it from the start. If you
change this file, you must restart your server for the changes to take
effect. If you do a resync, you'll get over 1000 "Conflicting region"
errors.

This section will tell you how to make new regions, like that you go
with the .go command.

There are currently 5 files in the default scripts pack, one for each
map (Fellucca, Trammel, Ilshenar, Malas and Tokuno) being each one
enumerated from 0 to 4 (sphere_map0,sphere_map1,and so on).

I'll use the region of Fellucca as an example for this part of the
tutorial, and now here's the script:

<font color="darkgreen">`[AREADEF a_world]`</font>  
`NAME=Felucca`  
`EVENTS=r_default,r_default_rock,r_default_water,r_default_tree,r_default_grass`  
`GROUP=ALLMAP`  
`P=1323,1624,55,0`  
`RECT=0,0,6144,4096,0`  

Let's understand those lines now:

**\[AREADEF somedef\]**: As you have probably noticed a_world is a
defname which defines the region for the server so it can be processed.

**Name**: This line contains the name of the region, which is shown when
you do .where inside the region and it also makes you go to that place
when doing .go "region name" (do not make 2 regions with the same name,
the last that has been loaded will replace the first when you do .go
command (which can fuck up a lot of things)).

**Events**: This defines what will happen in that region and what
resources are gatherable here (remember the REGIONTYPE section? It can
be used as an event here.). Besides the resources gatherable it'll also
show sphere what triggers to call from the events (you've probably
realized now that the REGIONTYPE section is an event for regions :P),
like the @Enter trigger and the others (see
[Triggers](Triggers "wikilink")).

**Group**: This is just an axis setting, this separates the regions in
groups (duh) when you go to the Travel Menu.

**P**: This is the place you go when you do .go "region name". Almost
all regions will have a P value and it's usually a convenient location
in the region to teleport to, or else it's the center of the region. If
you are making your own new region, be sure to pick a place you'd like
to teleport to.

**RainChance**: This defines the chance to rain on that region when a
weather is called (RainChance=50 means 50% chance of raining), the
others 50% means it'll snow.

**Rect**: This describes the exact boundaries of this region, by
coordinates. The first two numbers are the coordinate of the upper left
corner of the region, and the second two are the coordinates of the
lower right. In the case of Fellucca it stretches from 0,0 to 6144,4096
(RECT=0,0,6144,4096). Since 56B you also need to add a fith argument,
the map this region uses so it's RECT=0,0,6144,4096,0 (if the map is 0
you can leave it empty, otherwise you MUST NOT leave it empty or you'll
have conflicting regions.

**Flags**: The region flags allow you to control what goes on in a
particular region. They describe whether or not a region is to be
guarded, what types of magic are allowed to be cast there, who can be
harmed here, or whether or not it is allowed to rain there. Basically
anything you could ever want. Here's how you use them:

Just add this line to a region script:

FLAGS=#

Of course you're going to want to replace that \# with an actual number!
Where do we get those numbers? They're predefined in the game, but they
give us a nice handy list. I just showed it to you.

Say we want to make a region that is guarded and safe from harm. We
would simply add the two numbers together:

<tt>

  
  
region_flag_safe (02000)  

\+  
:region_flag_guarded (04000)  

=  
:06000  
</tt>

There you go. Your <font color="darkgreen">FLAGS</font> would be set to
06000. "But.. but.." you're saying. "Didn't you tell me that
<font color="darkgreen">DEFNAMEs</font> were supposed to prevent me from
working with scary numbers?" (See [Chapter 1](Chapter_1 "wikilink").) Of
course I did! And there's a way to do this without using any scary
number at all. Here it is:

<font color="darkblue">`FLAGS=region_flag_safe|region_flag_guarded`</font>

That's it. Now your region is both safe and guarded.

Which, as you may learn quickly as a new admin, is a big mistake. Making
a region safe and guarded at the same time prevents the guards from
actually killing anything, so they pile up and call each other, and soon
you have a huge laggy mess of guards hacking at something that can't be
killed (because it's a safe region). Just take my word for it and don't
make a region safe and guarded.

Here's a quick list for the region flags (you should check you
sphere_defs.scp for more, cause they may be changed):

<font color="darkblue">`[DEFNAME region_flags]`  
`region_antimagic_all 00001 // `<font color="darkred">`all magic banned here.`</font>  
`region_antimagic_recall_in 00002 // `<font color="darkred">`teleport,recall in to this, and mark`</font>  
`region_antimagic_recall_out 00004 // `<font color="darkred">`can't recall out of here.`</font>  
`region_antimagic_gate 00008 // `<font color="darkred">`can't open gates from or to this place.`</font>  
`region_antimagic_teleport 00010 // `<font color="darkred">`can't teleport into here.`</font>  
`region_antimagic_damage 00020 // `<font color="darkred">`just no bad magic here`</font>  
`region_flag_ship 00040 // `<font color="darkred">`this is a ship region. ship commands`</font>  
`region_flag_nobuilding 00080 // `<font color="darkred">`no building in this area`</font>  
`region_flag_globalname 00100 // `<font color="darkred">`make sure the name is avail globally.`</font>  
`region_flag_announce 00200 // `<font color="darkred">`announce to all who enter.`</font>  
`region_flag_insta_logout 00400 // `<font color="darkred">`instant log out is allowed here. (hotel)`</font>  
`region_flag_underground 00800 // `<font color="darkred">`dungeon type area. (no weather)`</font>  
`region_flag_nodecay 01000 // `<font color="darkred">`things on the ground don't decay here.`</font>  
`region_flag_safe 02000 // `<font color="darkred">`this region is safe from all harm.`</font>  
`region_flag_guarded 04000 // `<font color="darkred">`try tag.guardowner`</font>  
`region_flag_no_pvp 08000 // `<font color="darkred">`players cannot directly harm each other here.`</font>  
</font>

And that's about it for the
<font color="darkblue">sphere_mapX.scp</font> files.

## sphere_book.scp

Spherebook.scp is one of the most pointless files you will ever
encounter. How many times, when you logged onto a shard, did you
actually stop to READ those tips, or to READ the updates screen that
comes up every time? I know most of my players refused to. But, in any
case, that is what's in this file. And books. Did I mention books? Those
impossible-to-write-correctly, rarely-used items that waste RAM in-game?

**`[SCROLL SCROLL_MOTD]`**  
**`[SCROLL SCROLL_NEWBIE]`**  
**`[SCROLL SCROLL_GUEST]`**  

These are the sections that define the messages that pop up when you log
in. Anything written after these tags will appear in the appropriate
message. You'll have to figure out exactly what spacing is best for
those little info boxes. It does take some time, and there's really no
way to explain it. Just do it and you'll figure it out. Remember, there
is no wordwrap. Or at least there wasn't in the past.

**`[TIP X]`**  

You guessed it. These are the tips that pop up on startup. "War is
unhealthy for children and other living things." is one of them. Very
appropriate right now, I would say.

**`[BOOK title]`**  
**`[BOOK title x]`**  

Creates a book with a DEFNAME of title. Putting a page number x after
the DEFNAME will add your text to that particular page. Look at the
example books for clues on how to do this. The major difficulty with
books is that the game uses a variable-width font, so you don't know an
exact number of letters you can have on one line. For example, you can
fit more i's on one line than w's or M's, since those letters are
bigger. You can start a paragraph by typing a TAB text (clicking yout
TAB button :P)

## sphere_name.scp

This is an easy file. It's just lists of names under sections with
various <font color="darkgreen">DEFNAMEs</font>. It's these names that
are important, not the contents, since you will almost NEVER write your
own list of names. I've been using this emulator for two years now, and
I have never modified this file once.

To access this list of names, you write this in a script:

**NAME=#NAMES_HUMANMALE**

It will automatically replace it with a random name from the
<font color="darkgreen">**NAMES_HUMANMALE**</font> list.

To make a list of names, it'll look like that:

<font color="darkgreen">`[NAMES A_DEFNAME_YOU_WANT]`  
`NUMBER_OF_NAMES`  
`NAMES`  
</font>

for example:

<font color="darkgreen">`[NAMES NAMES_SPECIAL]`  
`2`  
`Hil`  
`Hol`  
</font>

Difficult file huh? I almost didn't give it a section to itself.

## sphere_newb.scp

There! I did it! No vain attempt at humor under the title! :)

In any case, this is another file that a lot of questions are asked
about. "How do I make players start with 10000 gold?" people ask. Or,
"How do I give all blacksmiths 800 ingots?" Now, I'm not saying I would
like to play on a shard where you start with 10000 gold or blacksmiths
start with 800 ingots. But this file would be the place to do it.

<font color="darkblue">`[NEWBIE MALE_DEFAULT]`  
`// Male Generic Starting Clothes`  
`ITEMNEWBIE=i_shirt_plain`  
`COLOR=colors_all`  
`ITEMNEWBIE=random_pants`  
`COLOR=colors_neutral`  
`ITEMNEWBIE=random_shoes`  
`COLOR=colors_neutral`  
`ITEMNEWBIE=i_dagger`  
`ITEMNEWBIE=i_candle`  
`ITEMNEWBIE=i_book_sm`  
`ITEMNEWBIE=i_gold,100`  
</font>

This is what a typical script looks like. It looks kinda like a template
doesn't it? Well there's a good reason for that. It really is a
template. It just uses the <font color="darkgreen">**ITEMNEWBIE**</font>
tag rather than the <font color="darkgreen">**ITEM**</font> tag. Look at
the section in Chapter 1 on Templates for more information on how to
structure this file!

The only real item of note is that these sections MUST have specific
names that the server looks for. You cannot add a new newbie section, no
matter how much you'd like to. Sorry!

## sphere_skill.scp (SKILLCLASSES)

Skill classes are what defines how much you can train at each skill/stat
and you can also add triggers to it. A SkillClass script would look like
this:

<font color="darkblue">`[SKILLCLASS 0]`  
`// undeclared class.`  
`// max skills for players of this skill class.`  
`// might want this to be all 50.0 to make people declare a class?`  
`DEFNAME=Class_undeclared`  
`NAME=undeclared`  
`// EVENTS=e_ClassUndeclared`  
`STATSUM=300`  
`SKILLSUM=10000.0`  
`STR=100`  
`INT=100`  
`DEX=100`  
`ALCHEMY=100.0`  
`ANATOMY=100.0`  
`ITEMID=100.0`  
`ARMSLORE=100.0`  
`and so on...`  
</font>

Now let's understand it:

<font color="darkgreen">**EVENTS**</font>: It means everyone with this
skillclass will also call the events specified in this field (to add
more events just use a ",", for example: EVENTS=e_1,e_2,and so on)

<font color="darkgreen">**STATSUM**</font>: This is how much the som of
your players stats can be, for example, if I have 100 str, 100 dex and
100 int, I've reached 300 stats, so I've reached STATSUM and can't have
more (except for magic items and such things)

<font color="darkgreen">**SKILLSUM**</font>: The same thing as STATSUM
but for skills.

<font color="darkgreen">**STR/DEX/INT**</font>: This is how much can the
player have at this specific stat (except for magic items and such)

<font color="darkgreen">**ALCHEMY**</font>: The same thing as the STR,
DEX and INT fields, but for skills (in this case alchemy, but of course
you can change to any other)

## sphere_serv_triggers.scp

This file hold special trigger "functions" that are fired by the server
its self at certain times depending on the function, below are a list of
the functions found in this file and a breif explain of what the
function will do for you.

**f_onaccount_login**

This function is called after the client has entered the password.

  
ARGS --\> username of the client logging in

ARGO --\> the client logging in

RETURN 0 --\> normal action (login)

RETURN 1 --\> disconnect the client

**f_onaccount_delete**

This function is called before an account is being deleted.

  
ARGS --\> username of the account being deleted.

RETURN 0 --\> normal action (delete)

RETURN 1 --\> account not deleted

**f_onchar_create**

**f_onchar_delete**

**f_onserver_start**

**f_onserver_save**

**f_onserver_save_ok**

**f_onserver_save_fail**

**f_onserver_save_finished**

**f_onserver_exit**

**f_onserver_blockip**

[Chapter 3](Chapter_3 "wikilink")

[Category:Tutorials](Category:Tutorials "wikilink")
