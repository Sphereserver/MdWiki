\_\_FORCETOC\_\_ Type definitions are the equivalent of
[EVENTS](EVENTS "wikilink") that can be attached to
[items](Items "wikilink"). There are different properties that can be
used to attach a type block to an item or set of items:

- [item definitions](ITEMDEF "wikilink") via their
  [TYPE](TYPE "wikilink") and/or [TEVENTS](TEVENTS "wikilink") property.
- [items](Items "wikilink") via their [TYPE](TYPE "wikilink") and/or
  [EVENTS](EVENTS_(Property) "wikilink") property.

In addition to handling triggers, type definitions can also be used to
define different types of terrain. This can be used to affect the return
value of the [TYPE](TYPE "wikilink") property on [map
points](Map_points "wikilink"), or for some hardcoded types such as
t_rock it can be used to define which terrain IDs Sphere should consider
to be rock when the mining skill is used.

## Built-in Types

The built-in types are all listed in the sphere_defs.scp file. The table
below only lists some of the built-in types and it is VERY weak on
actual details...so use with care.

<table>
<thead>
<tr>
<th><p>DEFNAME</p></th>
<th><p>Number</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>t_normal</p></td>
<td><p>0</p></td>
<td><p>No built-in behavior.</p></td>
</tr>
<tr>
<td><p>t_container and t_container_locked</p></td>
<td><p>1 and 2</p></td>
<td><p>These types are used for containers. They leverage the following
properties:</p>
<ul>
<li>MORE1 = "ID" from the key that can unlock this item (If the MORE1 of
the key matches the MORE1 of the container then they are linked)</li>
<li>MORE2 = The lock complexity (how hard it is to pick the lock)</li>
<li>MOREX = The trap type (not used yet?)</li>
<li>TDATA2 = The gumpID of the container (this is not an ITEMDEF)</li>
<li>TDATA3/4: Defines rectangle, where you can place items (so they
won't end up out of gump)</li>
<li>TDATA3 = top left corner. Hexadecimal number, each position takes 4
bytes, XY (example: X = 10 (0a) and Y = 20 (014) will look like
TDATA3=000a0014</li>
<li>TDATA4 = bottom right corner.</li>
<li>LINK = UID of a secondary key?</li>
</ul></td>
</tr>
<tr>
<td><p>t_door or t_door_locked</p></td>
<td><p>3 or 4</p></td>
<td><p>This type is used for both unlocked and locked doors. They
leverage the following properties:</p>
<ul>
<li>MORE1 = UID of this door's key (if it has one)</li>
<li>TDATA1 = ID for the sound it makes when double clicked</li>
</ul></td>
</tr>
<tr>
<td><p>t_key</p></td>
<td><p>5</p></td>
<td><p>This type is used for keys. It leverages the following
properties:</p>
<ul>
<li>MORE1 = "ID" of the item(s) this key can unlock (if the MORE1 of the
key matches the MORE1 of the container/door then they are linked)</li>
<li>LINK = If this is set to the UID of a "multi" object (like a house)
the key can open all doors/containers in that multi?</li>
</ul>
<p><strong>Note:</strong> Keys, containers, and doors are interesting.
If both a key and a door/container contain the same arbitrary MORE1
value, the key can be used to lock or unlock the door/container. That
action changes the TYPE of the door/container to indicate whether it is
locked or not. It also seems like LINK on the key can be set to the UID
of a multi so that it can be used to open all doors/containers inside
that multi.</p></td>
</tr>
<tr>
<td><p>t_light_lit</p></td>
<td><p>6</p></td>
<td><p>This type is used for light sources that can be turned onIT_S or
off. It leverages the following properties:</p>
<ul>
<li>MOREY = Number of charges before the item is consumed</li>
<li>MOREZ = Type of light pattern it will cast</li>
</ul></td>
</tr>
<tr>
<td><p>t_light_out</p></td>
<td><p>7</p></td>
<td><p>This type is used for light sources that can be turned on or off.
It leverages the following properties:</p>
<ul>
<li>MOREY = Number of charges before the item is consumed</li>
<li>MOREZ = Type of light pattern it will cast</li>
</ul></td>
</tr>
<tr>
<td><p>t_food</p></td>
<td><p>8</p></td>
<td><p>This type is used for edible food. It leverages the following
properties:</p>
<ul>
<li>MORE2 = The ID of the creature that this came from</li>
<li>MOREM = Is the amount (0 to 127) of "food units" that will be gained
when the item is used (eaten)</li>
<li>MOREZ = Is the poison level of the food</li>
</ul>
<p><strong>Note:</strong> The following properties may also exist
depending on your server version:</p>
<ul>
<li>MOREX = The ID of a spell effect that will be gained when eaten</li>
<li>MOREY = The strength of the spell effect</li>
</ul></td>
</tr>
<tr>
<td><p>t_food_raw</p></td>
<td><p>9</p></td>
<td><p>This type is used for <em>raw</em> food. It leverages the
following properties:</p>
<ul>
<li>MORE1 = ID of the item it makes when cooked (the default is i_unused
and if defined, it will override TDATA1)</li>
<li>MORE2 = The ID of the creature that this came from</li>
<li>MOREM = Is the amount (0 to 127) of "food units" that will be gained
when the item is used (eaten)</li>
<li>MOREZ = Is the poison level of the food</li>
<li>TDATA1 = The item ID this cooks into</li>
</ul>
<p><strong>Note:</strong> The following properties may also exist
depending on your server version:</p>
<ul>
<li>MOREX = The ID of a spell effect that will be gained when eaten</li>
<li>MOREY = The strength of the spell effect</li>
<li>TDATA2 = The creature ID type that the food came from</li>
<li>TDATA3 = The amount of skill required to cook it (did this ever
work?)</li>
</ul></td>
</tr>
<tr>
<td><p>t_armor</p></td>
<td><p>10</p></td>
<td><p>This type is used for armor. It leverages the following
properties:</p>
<ul>
<li>MORE1L = Max hitpoints</li>
<li>MORE1H = Current hitpoints</li>
<li>MOREX = Spell effect when worn (for example, setting MOREX=1 causes
a permanent Clumsy effect)</li>
<li>MOREY = There are two possible effects of setting MOREY:
<ol>
<li>If MOREX is set, then MOREY is the power/effect of that spell</li>
<li>If the ATTR includes attr_magic, then there is an AR bonus (how is
this calculated?)</li>
</ol></li>
</ul>
<p><strong>Note:</strong> Old versions of sphere stored remaining
charges in MORE2, this is no longer true.</p></td>
</tr>
<tr>
<td><p>t_weapon_mace_smith</p></td>
<td><p>11</p></td>
<td><p>This type is used for macefighting weapons that can also be used
by blacksmiths to forge items. It leverages the following
properties:</p>
<ul>
<li>MORE1L = Max hitpoints</li>
<li>MORE1H = Current hitpoints</li>
<li>MOREY = Attack bonus (percentage), but only if ATTR &amp;
attr_magic</li>
</ul>
<p>The following overrides can be set on a per item basis:</p>
<ul>
<li>TAG.OVERRIDE.DAMAGETYPE = can be used on a per item basis to
override the types of damage this weapon does</li>
<li>TAG.OVERRIDE.SOUND_HIT = can be used on a per item basis to override
the sound this weapon makes when it hits</li>
<li>TAG.OVERRIDE.SOUND_MISS = can be used on a per item basis to
override the sound this weapon makes when it misses</li>
</ul></td>
</tr>
<tr>
<td><p>t_weapon_mace_sharp</p></td>
<td><p>12</p></td>
<td><p>This type is used for macefighting weapons that have sharp
cutting edges. It leverages the following properties:</p>
<ul>
<li>MORE1L = Max hitpoints</li>
<li>MORE1H = Current hitpoints</li>
<li>MOREY = Attack bonus (percentage), but only if ATTR &amp;
attr_magic</li>
</ul>
<p>The following overrides can be set on a per item basis:</p>
<ul>
<li>TAG.OVERRIDE.DAMAGETYPE = can be used on a per item basis to
override the types of damage this weapon does</li>
<li>TAG.OVERRIDE.SOUND_HIT = can be used on a per item basis to override
the sound this weapon makes when it hits</li>
<li>TAG.OVERRIDE.SOUND_MISS = can be used on a per item basis to
override the sound this weapon makes when it misses</li>
</ul></td>
</tr>
<tr>
<td><p>t_weapon_sword</p></td>
<td><p>13</p></td>
<td><p>This type is used for swordsmanship weapons. It leverages the
following properties:</p>
<ul>
<li>MORE1L = Max hitpoints</li>
<li>MORE1H = Current hitpoints</li>
<li>MOREY = Attack bonus (percentage), but only if ATTR &amp;
attr_magic</li>
</ul>
<p>The following overrides can be set on a per item basis:</p>
<ul>
<li>TAG.OVERRIDE.DAMAGETYPE = can be used on a per item basis to
override the types of damage this weapon does</li>
<li>TAG.OVERRIDE.SOUND_HIT = can be used on a per item basis to override
the sound this weapon makes when it hits</li>
<li>TAG.OVERRIDE.SOUND_MISS = can be used on a per item basis to
override the sound this weapon makes when it misses</li>
</ul></td>
</tr>
<tr>
<td><p>t_weapon_fence</p></td>
<td><p>14</p></td>
<td><p>This type is used for fencing weapons. It leverages the following
properties:</p>
<ul>
<li>MORE1L = Max hitpoints</li>
<li>MORE1H = Current hitpoints</li>
<li>MOREY = Attack bonus (percentage), but only if ATTR &amp;
attr_magic</li>
</ul>
<p>The following overrides can be set on a per item basis:</p>
<ul>
<li>TAG.OVERRIDE.DAMAGETYPE = can be used on a per item basis to
override the types of damage this weapon does</li>
<li>TAG.OVERRIDE.SOUND_HIT = can be used on a per item basis to override
the sound this weapon makes when it hits</li>
<li>TAG.OVERRIDE.SOUND_MISS = can be used on a per item basis to
override the sound this weapon makes when it misses</li>
</ul></td>
</tr>
<tr>
<td><p>t_weapon_bow</p></td>
<td><p>15</p></td>
<td><p>This type is used for archery weapons (bow or crossbow). It
leverages the following properties:</p>
<ul>
<li>MORE1L = Max hitpoints</li>
<li>MORE1H = Current hitpoints</li>
<li>MOREY = Attack bonus (percentage), but only if ATTR &amp;
attr_magic</li>
<li>TDATA1 = The sound effect the weapon makes when it shoots</li>
<li>TDATA2 = The required strength to wield the weapon</li>
<li>TDATA3 = ID of arrow item that will be fired (and must therefore be
on the player's person)</li>
<li>TDATA4 = ID of the arrow animation (for bows it is usually
i_arrow_x, for crossbows, i_xbow_x)</li>
</ul>
<p>The following overrides can be set on a per item basis:</p>
<ul>
<li>TAG.OVERRIDE.DAMAGETYPE = to override the types of damage this
weapon does</li>
<li>TAG.OVERRIDE.SOUND_HIT = to override the sound this weapon makes
when it hits</li>
<li>TAG.OVERRIDE.SOUND_MISS = to override the sound this weapon makes
when it misses</li>
<li>AMMOANIMRENDER = to override the rendermode of the ANIM this item
uses (yes, no TAGs)</li>
<li>AMMOTYPE = to override the type of ammo (TDATA3) this item uses
(yes, no TAGs)</li>
<li>AMMOANIM = to override the ammo animation (TDATA4) this item uses
(yes, no TAGs)</li>
<li>AMMOANIMHUE = to override the color of the ammo animation this item
uses (yes, no TAGs)</li>
</ul></td>
</tr>
<tr>
<td><p>t_wand</p></td>
<td><p>16</p></td>
<td><p>This type is used for magic wands. It leverages the following
properties:</p>
<ul>
<li>MORE1L = the current amount of hitpoints the item has</li>
<li>MORE1H = the maximum hitpoints for the item</li>
<li>MORE2 = the number of remaining charges (if magical)</li>
<li>MOREX = the spell type (if magical)</li>
<li>MOREY = the spell strength (0-1000)</li>
<li>MOREZ = the poison skill applied (0-100)</li>
<li>TDATA2 = Required Strength to equip the wand</li>
<li>TDATA3 = ID of the light pattern</li>
<li>TDATA4 = A flag to indicate what happens when the light burns out
(0=nothing, 1=delete the object).</li>
</ul></td>
</tr>
<tr>
<td><p>t_telepad</p></td>
<td><p>17</p></td>
<td><p>This type is used for teleport pads. It leverages the following
properties:</p>
<ul>
<li>MOREP = Coordinates of the point to which you will teleport when you
step on the item</li>
<li>MORE1 = If set to 1, the teleport pad will only work for players
(and their pets)</li>
<li>MORE2 = If set to 1, the teleport animation and sound will not be
shown to anyone witnessing the teleport</li>
</ul></td>
</tr>
<tr>
<td><p>t_switch</p></td>
<td><p>18</p></td>
<td><p>This type is used for switches. The way these things work is,
when used, they trigger @DCLICK on the LINK object. It leverages the
following properties:</p>
<ul>
<li>LINK = UID of item to trigger</li>
<li>MORE1 = The item ID of the next state of the switch</li>
<li>MOREX = A flag to indicate if this is activated by stepping on
it</li>
</ul></td>
</tr>
<tr>
<td><p>t_book</p></td>
<td><p>19</p></td>
<td><p>This type is used for books of static or dynamic text. The maximum number of pages has been extended to 255. It leverages the following properties:</p><ul>
<li>MORE1L = This can be set to an ID of a book (some default book text
is included in the sphere_books.scp file)</li>
<li>MORE1H = Some flags that determine book behavior:
<ul>
<li>0c00: Scripted book</li>
<li>0800: Editable book</li>
<li>08000: ? time stamp ?</li>
</ul></li>
<li>AUTHOR = The ID of the character that wrote the book</li>
<li>BODY.# = The text for each page of the book (starting with page
0)</li>
</ul>
<p><strong>Note:</strong> we need more information on those
flags...</p></td>
</tr>
<tr>
<td><p>t_rune</p></td>
<td><p>20</p></td>
<td><p>This type is used for recall runes. It leverages the following
properties:</p>
<ul>
<li>MORE1 = The number of uses left before it wears out</li>
<li>MOREP = The coordinates of the marked location</li>
</ul></td>
</tr>
<tr>
<td><p>t_booze</p></td>
<td><p>21</p></td>
<td><p>This type is used for alcohol (it causes a drunk effect when
double clicked.) It leverages the following properties:</p>
<ul>
<li>TDATA1 = A flag that indicates whether the container is empty or
not.</li>
</ul></td>
</tr>
<tr>
<td><p>t_potion</p></td>
<td><p>22</p></td>
<td><p>This type is used for potions. It leverages the following
properties:</p>
<ul>
<li>MORE1 = The potion spell effect that will result when the potion is
double clicked</li>
<li>MORE2 = The strength of the potion (This has a different effect
defending on the spell, usually between 0 and 1000)</li>
<li>MOREX = The countdown to explosion (for purple potions)</li>
<li>TDATA1 = A flag that indicates whether the container is empty or
not</li>
</ul></td>
</tr>
<tr>
<td><p>t_fire</p></td>
<td><p>23</p></td>
<td><p>This type is used for fires (and ovens?). These items can be used
to cook food, and they can burn you if stepped on. It leverages the
following properties:</p>
<ul>
<li>TIMER = time until it decays?</li>
<li>MORE1 (or MORE2?) = Amount of damage it will cause when stepped on
or dclicked</li>
<li>MOREZ = Type of light pattern it will cast</li>
</ul></td>
</tr>
<tr>
<td><p>t_clock</p></td>
<td><p>24</p></td>
<td><p>This type is used to tell time (game time, not real time) when
double clicked. The result comes out something like "half past eleven
o'clock at night". From what I can tell there are no MORE or TDATA
modifiers that affect the result.</p></td>
</tr>
<tr>
<td><p>t_trap and t_trap_active</p></td>
<td><p>25 and 26</p></td>
<td><p>These types are used for traps that are triggered when walked on.
They leverage the following properties:</p>
<ul>
<li>MORE1 = ID of the animation</li>
<li>MORE2 = The damage the trap will cause</li>
<li>MOREX = The length of time the animation will run</li>
<li>MOREY = The length of time the activated trap will idle until
reset</li>
<li>MOREZ = A flag that indicates if the trap must idle before changing
from active to inactive.</li>
</ul></td>
</tr>
<tr>
<td><p>t_musical</p></td>
<td><p>27</p></td>
<td><p>This type is used for musical instruments. It leverages the
following properties:</p>
<ul>
<li>TDATA1 = The sound ID to be played if successful</li>
<li>TDATA2 = The sound ID to be played if not successful</li>
</ul></td>
</tr>
<tr>
<td><p>t_spell</p></td>
<td><p>28</p></td>
<td><p>This type is used for magic spell effects. It leverages the
following properties:</p>
<ul>
<li>MORE1L = The polymorph effect on STR</li>
<li>MORE1H = The polymorph effect on DEX</li>
<li>MORE2 = The number of charges left</li>
<li>MOREX = The spell effect that will result when the item is stepped
on</li>
<li>MOREY = The strength of the spell (This has a different effect
defending on the spell, usually between 0 and 1000)</li>
<li>MOREZ = Type of light pattern it will cast</li>
</ul></td>
</tr>
<tr>
<td><p>t_gem</p></td>
<td><p>29</p></td>
<td><p>This type is used for gems, and from what I can tell there is no
built-in behavior for it.</p></td>
</tr>
<tr>
<td><p>t_water</p></td>
<td><p>30</p></td>
<td><p>This type is used for water, which means it can be fished in or
used to clean used bandages.</p>
<ul>
<li>MORE1 = The regiontype ID that determines what sorts of resources
(fish etc) that it can produce.</li>
</ul></td>
</tr>
<tr>
<td><p>t_clothing</p></td>
<td><p>31</p></td>
<td><p>This type is used for all cloth based equip-able items. It is
essentially identical to t_armor and t_armor_leather. It leverages the
following properties:</p>
<ul>
<li>MORE1L = Max hitpoints</li>
<li>MORE1H = Current hitpoints</li>
<li>MOREX = Spell effect when worn (for example, setting MOREX=1 causes
a permanent Clumsy effect)</li>
<li>MOREY = There are two possible effects of setting MOREY:
<ol>
<li>If MOREX is set, then MOREY is the power/effect of that spell</li>
<li>If the ATTR includes attr_magic, then there is an AR bonus (how is
this calculated?)</li>
</ol></li>
</ul>
<p><strong>Note:</strong> Old versions of sphere stored remaining
charges in MORE2, this is no longer true.</p></td>
</tr>
<tr>
<td><p>t_scroll</p></td>
<td><p>32</p></td>
<td><p>This type is used for scrolls. It leverages the following
properties:</p>
<ul>
<li>MOREX = ID of the spell to cast when double-clicked</li>
<li>MOREY = Power of the spell (equivalent to the EFFECT setting of the
spell itself?)</li>
</ul></td>
</tr>
<tr>
<td><p>t_carpentry</p></td>
<td><p>33</p></td>
<td><p>This type is used by carpenters to craft items, and from what I
can tell there is no built-in behavior for it.</p></td>
</tr>
<tr>
<td><p>t_spawn_char</p></td>
<td><p>34</p></td>
<td><p>This type is used to spawn NPCs. Once it spawns its first
creature, it will turn red and change its appearance to the ICON of the
creature (or appear as a wisp if the spawn is set to use a template.) It
leverages the following properties:</p>
<ul>
<li>AMOUNT = The maximum amount of NPCs the spawner should create</li>
<li>MORE1/SPAWNID* = The creature ID or spawn template ID for what you
want to spawn</li>
<li>MORE2/COUNT* = The current number of creatures spawned from this
point</li>
<li>MOREX/TIMELO* = The minimum time between spawns (in minutes)</li>
<li>MOREY/TIMEHI* = The maximum time between spawns (in minutes)</li>
<li>MOREZ/MAXDIST* = The maximum distance away from the spawn to create
the spawned NPC (this is also the maximum wander distance for the
NPC)</li>
<li>AT*(R/W) = Access the object in the N position and
reads/writes/executes the given text, eg: at.0.remove,
&lt;at.0.str&gt;...</li>
<li>ADDOBJ*(W) = Adds to the spawn an object with the given uid (must be
a valid uid)</li>
<li>DELOBJ*(W) = Deletes from the spawn an object with the given uid
(must be a valid uid)</li>
<li>START*(W) = Forces the spawn to start spawning</li>
<li>STOP*(W) = Stops the spawn and removes everything it created</li>
<li>RESET*(W) = Froces an STOP and then START it again</li>
</ul>
<p><code>  *X branch only</code></p>
<p><strong>Note:</strong> The spawn is considered active if the TIMER
has a positive value, and when the timer reaches zero, it is
automatically restarted using a random number between MOREX and
MOREY.</p></td>
</tr>
<tr>
<td><p>t_game_piece</p></td>
<td><p>35</p></td>
<td><p>This type is used for game board pieces (checkers, chess, etc).
They cannot be removed from the game, and they have no tile image
outside of the game board gump. It leverages the following
properties:</p>
<ul>
<li>TDATA1 = The starting x position for this piece</li>
<li>TDATA2 = The starting y position for this piece</li>
</ul></td>
</tr>
<tr>
<td><p>t_portculis</p></td>
<td><p>36</p></td>
<td><p>This type is used for portcullis doors that raise and lower when
double clicked. It leverages the following properties:</p>
<ul>
<li>MORE1 = The z height at the lowest setting</li>
<li>MORE2 = The z height at the highest setting</li>
</ul></td>
</tr>
<tr>
<td><p>t_figurine</p></td>
<td><p>37</p></td>
<td><p>This type is used for shrunk NPCs (essentially magic figurines),
that turn into a "pet" creature when double clicked. It leverages the
following properties:</p>
<ul>
<li>MORE1 = The creature ID that will spawn when the item is double
clicked.</li>
<li>MORE2 = The UID of the off-line creature (in "stable master"
inventory)</li>
<li>TDATA2 = The required strength to mount the creature (presumably
only if it is possible to mount it)</li>
<li>TDATA3 = The base creature ID.</li>
</ul></td>
</tr>
<tr>
<td><p>t_shrine</p></td>
<td><p>38</p></td>
<td><p>This type is used for shrines. They will resurrect a ghost when
double-clicked by a ghost.</p></td>
</tr>
<tr>
<td><p>t_moongate</p></td>
<td><p>39</p></td>
<td><p>This type is used for moongates. When stepped on they teleport
the player to another location. It leverages the following
properties:</p>
<ul>
<li>MOREP = The coordinates that the moongate leads to</li>
<li>MORE1 = If set to 1, the smoke and sound is supressed</li>
<li>MORE2 = If set to 1, NPCs (and pets?) cannot use it</li>
</ul></td>
</tr>
<tr>
<td><p>t_chair</p></td>
<td><p>40</p></td>
<td><p>This type is used for any sort of a chair item and it's only
purpose is to trigger a sitting animation.</p></td>
</tr>
<tr>
<td><p>t_forge</p></td>
<td><p>41</p></td>
<td><p>This type is used by blacksmiths to smelt ore....</p></td>
</tr>
<tr>
<td><p>t_ore</p></td>
<td><p>42</p></td>
<td><p>This type is harvested by miners, and converted by blacksmiths
(using a forge) into something else. It leverages the following
properties:</p>
<ul>
<li>TDATA1 = ID of item created when the ore is smelted (usually
ingots)</li>
</ul></td>
</tr>
<tr>
<td><p>t_log</p></td>
<td><p>43</p></td>
<td><p>This type is a raw material resource usually harvested from
trees.</p></td>
</tr>
<tr>
<td><p>t_tree</p></td>
<td><p>44</p></td>
<td><p>This type is chopped by lumberjacks to get logs. It leverages the
following properties:</p>
<ul>
<li>MORE1 = The regiontype ID that determines what sorts of resources
(fish etc) that it can produce.</li>
<li>FRUIT = ID of item gathered if double-clicked (usually logs)</li>
</ul></td>
</tr>
<tr>
<td><p>t_rock</p></td>
<td><p>45</p></td>
<td><p>This type can be mined for ore.</p>
<ul>
<li>MORE1 = The regiontype ID that determines what sorts of resources
(fish etc) that it can produce.</li>
</ul></td>
</tr>
<tr>
<td><p>t_carpentry_chop</p></td>
<td><p>46</p></td>
<td><p>A carpentry tool that can be used to craft carpentry objects as
well as used to "chop" trees (like a saw?)</p></td>
</tr>
<tr>
<td><p>t_multi</p></td>
<td><p>47</p></td>
<td><p>Multi part object like house or ship.</p>
<ul>
<li>MORE1 is the UID of the player that created/owns the multi</li>
</ul></td>
</tr>
<tr>
<td><p>t_reagent</p></td>
<td><p>48</p></td>
<td><p>Alchemy when clicked ?</p></td>
</tr>
<tr>
<td><p>t_ship</p></td>
<td><p>49</p></td>
<td><p>This is a ship multi.</p>
<ul>
<li>MORE1 is the UID of the player that created/owns the multi</li>
<li>MORE2 contains the speed, anchor flag, direction of movement, and
facing direction in each byte respectively</li>
</ul></td>
</tr>
<tr>
<td><p>t_ship_plank</p></td>
<td><p>50</p></td>
<td><p>Ship plank for players to get on a boat.</p>
<ul>
<li>TDATA1 = is the itemID of the next open/closed state.</li>
<li>MORE1 = the lock code. normally this is the same as the uid (magic
lock=non UID)</li>
<li>MORE2= 0-1000 = How hard to pick or magic unlock. (conflict with
door ?)</li>
<li>MOREX = type to become (IT_SHIP_SIDE or IT_SHIP_SIDE_LOCKED)</li>
</ul></td>
</tr>
<tr>
<td><p>t_ship_side</p></td>
<td><p>51</p></td>
<td><p>Should extend to make a plank TDATA1 is the itemID of the next
open/closed state.</p>
<ul>
<li>MORE1 = the lock code. normally this is the same as the uid (magic
lock=non UID)</li>
<li>MORE2= 0-1000 = How hard to pick or magic unlock. (conflict with
door ?)</li>
</ul></td>
</tr>
<tr>
<td><p>t_ship_side_locked</p></td>
<td><p>52</p></td>
<td><p>TDATA1 is the itemID of the next open/closed state.</p>
<ul>
<li>MORE1 = the lock code. normally this is the same as the uid (magic
lock=non UID)</li>
<li>MORE2= 0-1000 = How hard to pick or magic unlock. (conflict with
door ?)</li>
</ul></td>
</tr>
<tr>
<td><p>t_ship_tiller</p></td>
<td><p>53</p></td>
<td><p>Tiller man on the ship.</p>
<ul>
<li>MORE1 = the lock code. Normally this is the UID, except if uidLink
is set.</li>
<li>LINK = If this is set to the UID of a "multi" object (like a house)
the key can open all doors/containers in that multi?</li>
</ul>
<p><strong>Note:</strong> Keys, containers, and doors are interesting.
If both a key and a door/container contain the same arbitrary MORE1
value, the key can be used to lock or unlock the door/container. That
action changes the TYPE of the door/container to indicate whether it is
locked or not. It also seems like LINK on the key can be set to the UID
of a multi so that it can be used to open all doors/containers inside
that multi.</p></td>
</tr>
<tr>
<td><p>t_eq_trade_window</p></td>
<td><p>54</p></td>
<td><p>Container for the trade window.</p></td>
</tr>
<tr>
<td><p>t_fish</p></td>
<td><p>55</p></td>
<td><p>Fish can be cut up. Yields 4 * <Amount> when a bladed object is
used on it.</p></td>
</tr>
<tr>
<td><p>t_sign_gump</p></td>
<td><p>56</p></td>
<td><p>This type is used for simple signs (and things like grave
stones). It leverages the following properties:</p>
<ul>
<li>TDATA2 = The gumpID</li>
<li>TDATA3 = The minimum gump size</li>
<li>TDATA4 = The maximum gump size</li>
<li>MORE1 = the lock code. Normally this is the UID, except if uidLink
is set.</li>
<li>LINK = If this is set to the UID of a "multi" object (like a house)
the key can open all doors/containers in that multi?</li>
</ul>
<p><strong>Note:</strong> Keys, containers, and doors are interesting.
If both a key and a door/container contain the same arbitrary MORE1
value, the key can be used to lock or unlock the door/container. That
action changes the TYPE of the door/container to indicate whether it is
locked or not. It also seems like LINK on the key can be set to the UID
of a multi so that it can be used to open all doors/containers inside
that multi.</p></td>
</tr>
<tr>
<td><p>t_stone_guild</p></td>
<td><p>57</p></td>
<td><p>This type is used for guild stones. It leverages the following
properties:</p>
<ul>
<li>MORE1 = The alignment of the guild (chaos, neutral, order)</li>
<li>MORE2 = The amount of gold in the guild account</li>
</ul></td>
</tr>
<tr>
<td></td>
<td></td>
<td><p><code>t_anim_active            58   // = active anium that will recycle when done.</code><br />
<code>t_sand                   59   // = sand on the beach</code><br />
<code>t_cloth                  60   // = bolt or folded cloth</code><br />
<code>t_hair                   61   //</code><br />
<code>t_beard                  62   // = just for grouping purposes.</code></p></td>
</tr>
<tr>
<td><p>t_ingot</p></td>
<td><p>63</p></td>
<td><p>This type is used for ingots (when a blacksmith smelts ore, it
turns into ingots. It leverages the following properties:</p>
<ul>
<li>TDATA1 = The skill required to smelt this</li>
<li>TDATA2 = The skill required to get the maximum yield when
smelting</li>
</ul></td>
</tr>
<tr>
<td><p>t_coin</p></td>
<td><p>64</p></td>
<td><p>This types is used for coins, gold or otherwise.</p></td>
</tr>
<tr>
<td><p>t_crops</p></td>
<td><p>65</p></td>
<td><p>This type is used to grow plants that likely bear fruit. Double
clicking a t_crop item will harvest the fruit if it is ripe. It
leverages the following properties:</p>
<ul>
<li>MORE1 = Time in seconds before this item will grow to the next stage
(this overrides the default server defined number)</li>
<li>TDATA1 = Is the ID of the first stage of the crop (the sprout), it
is the ID that the crop will be reset to regrow from (0=nothing, which
means this plant will not regrow once harvested)</li>
<li>TDATA2 = Is the ID of the next stage of the crop (or zero if this is
the final mature crop which will bear the fruit)</li>
<li>TDATA3 = Is the ID of the fruit that this plant will grow and should
only be set on the <em>ripe</em> plant (0 means the plant is not
mature)</li>
</ul>
<p><strong>Note</strong> This type has unusual TIMER behavior in that
regardless of the ATTR flags, the timer will restart when it reaches
zero.</p></td>
</tr>
<tr>
<td><p>t_drink</p></td>
<td><p>66</p></td>
<td><p>This type is used for non-alcoholic drinks. It leverages the
following properties:</p>
<ul>
<li>TATA1 = A flag that indicates whether the container is empty or
not.</li>
</ul>
<p><strong>Note:</strong> There is an INI flag OF_DrinkIsFood (0x10000)
that, if set, will increase FOOD level when the drink is consumed (like
T_FOOD does)</p></td>
</tr>
<tr>
<td></td>
<td></td>
<td><p><code>t_anvil                  67   // = for repair.</code><br />
<code>t_port_locked            68   // = this portcullis must be triggered.</code></p></td>
</tr>
<tr>
<td><p>t_spawn_item</p></td>
<td><p>69</p></td>
<td><p>This type is used to spawn items. Once it spawns its first item,
it will turn red and change its appearance to the i_worldgem_lg ID item.
It leverages the following properties:</p>
<ul>
<li>AMOUNT = The maximum amount of items the spawner should create</li>
<li>MORE1/SPAWNID* = The item ID or spawn template ID for what you want
to spawn</li>
<li>MORE2/PILE* = The current number of items spawned from this
point</li>
<li>MOREX/TIMELO* = The minimum time between spawns (in minutes)</li>
<li>MOREY/TIMEHI* = The maximum time between spawns (in minutes)</li>
<li>MOREZ/MAXDIST* = The maximum distance away from the spawn to create
the spawned item (this is also the maximum wander distance for the
NPC)</li>
<li>AT*(R/W) = Access the object in the N position and
reads/writes/executes the given text, eg: at.0.remove,
&lt;at.0.str&gt;...</li>
<li>ADDOBJ*(W) = Adds to the spawn an object with the given uid (must be
a valid uid)</li>
<li>DELOBJ*(W) = Deletes from the spawn an object with the given uid
(must be a valid uid)</li>
<li>START*(W) = Forces the spawn to start spawning</li>
<li>STOP*(W) = Stops the spawn and removes everything it created</li>
<li>RESET*(W) = Froces an STOP and then START it again</li>
</ul>
<p><code>  *X branch only</code></p>
<p><strong>Note:</strong> The spawn is considered active if the TIMER
has a positive value, and when the timer reaches zero, it is
automatically restarted using a random number between MOREX and
MOREY.</p></td>
</tr>
<tr>
<td></td>
<td></td>
<td><p><code>t_telescope              70   // = big telescope pic.</code></p></td>
</tr>
<tr>
<td><p>t_bed</p></td>
<td><p>71</p></td>
<td><p>This type is used to indicate the item is a bed. I am not sure
how it is used exactly, but it leverages the following properties:</p>
<ul>
<li>TDATA1 = The direction it occupies</li>
</ul></td>
</tr>
<tr>
<td><p>t_gold</p></td>
<td><p>72</p></td>
<td><p>This type is used to indicate the object is a gold coin and can
be used to purchase stuff.</p></td>
</tr>
<tr>
<td><p>t_map</p></td>
<td><p>73</p></td>
<td><p>This type is used for cartography maps. It has the following
properties:</p>
<ul>
<li>MORE1L = The top coordinate.</li>
<li>MORE1H = The left coordinate.</li>
<li>MORE2L = The bottom coordinate.</li>
<li>MORE2H = The right coordinate.</li>
<li>MOREZ = A flag that indicates whether the map has pins or not.</li>
<li>MOREX and MOREY = The coordinates of the pin (I think).</li>
<li>TDATA1 = The map gump width.</li>
<li>TDATA2 = The map gump height.</li>
</ul></td>
</tr>
<tr>
<td><p>t_eq_memory_obj</p></td>
<td><p>74</p></td>
<td><p>This type is used for character memories, and it really depends
on the type of memory to know what each property really means, but here
is a relatively good guide:</p>
<ul>
<li>MORE1L = The action type this is a memory for</li>
<li>MORE1H = The skill involved</li>
<li>MORE2 = The start time of the memory</li>
<li>MOREP = The map coordinates at which the memory occurred.</li>
</ul></td>
</tr>
<tr>
<td></td>
<td></td>
<td><p><code>t_weapon_mace_staff      75   // = staff type of mace. or just other type of mace.</code></p></td>
</tr>
<tr>
<td><p>t_eq_horse</p></td>
<td><p>76</p></td>
<td><p>This type is used for equipped horse object. Essentially it
represents a riding horse to the client. It leverages the following
properties:</p>
<ul>
<li>MORE1 = The creature ID</li>
<li>MORE2 = The UID of the offline creature (in "stable master"
inventory)</li>
<li>TDATA2 = The required strength to mount it</li>
<li>TDATA3 = The base creature ID</li>
</ul></td>
</tr>
<tr>
<td><p>t_comm_crystal</p></td>
<td><p>77</p></td>
<td><p>This type is used for communication crystals.</p></td>
</tr>
<tr>
<td><p>t_game_board</p></td>
<td><p>78</p></td>
<td><p>This type is used as a container for game pieces (t_game_piece).
It leverages the following properties:</p>
<ul>
<li>MORE1 = The type of pieces to use (0=chess, 1=checkers, 2=none...
presumably this is hard-coded)</li>
<li>TDATA2 = The gumpID of the container (this is not an ITEMDEF)</li>
<li>TDATA3 = The minimum gump size</li>
<li>TDATA4 = The maximum gump size</li>
</ul></td>
</tr>
<tr>
<td><p>t_trash_can</p></td>
<td><p>79</p></td>
<td><p>This type is used as a trash can container, and it deletes any
object placed into it. It leverages the following properties:</p>
<ul>
<li>TDATA2 = The gumpID of the container (this is not an ITEMDEF)</li>
<li>TDATA3 = The minimum gump size</li>
<li>TDATA4 = The maximum gump size</li>
</ul></td>
</tr>
<tr>
<td><p>t_cannon_muzzle</p></td>
<td><p>80</p></td>
<td><p>This type is used for the business end of the cannon. It
leverages the following properties:</p>
<ul>
<li>MORE2 = A mask of what is currently loaded in it. (0 = none,
1=powder, 2=shot)</li>
</ul></td>
</tr>
<tr>
<td><p>t_cannon</p></td>
<td><p>81</p></td>
<td><p>This type is used for the cannon control.</p></td>
</tr>
<tr>
<td><p>t_cannon_ball</p></td>
<td><p>82</p></td>
<td><p>This is ammo for a t_cannon.</p></td>
</tr>
<tr>
<td></td>
<td></td>
<td><p><code>t_armor_leather          83   // = non metallic armor (t_clothing)</code></p></td>
</tr>
<tr>
<td><p>t_seed</p></td>
<td><p>84</p></td>
<td><p>This type is used for seeds. A seed can be created by using a
dagger on a fruit (assuming the fruit is setup to have a seed.) A seed
can be planted by double clicking it and targeting the ground
(specifically t_dirt items). It leverages the following properties:</p>
<ul>
<li>TDATA1 = The ID of a t_crop item that will grow the fruit that this
seed comes from. 0 is Nothing.</li>
<li>TDATA2 = The art asset to use as the seed art asset. A copper coin
is default.</li>
</ul></td>
</tr>
<tr>
<td></td>
<td></td>
<td><p><code>t_junk                   85   // = never used</code><br />
<code>t_crystal_ball           86   // = Has no internal use.</code><br />
<code>t_swamp                  87   // = swamp (smelly)</code></p></td>
</tr>
<tr>
<td><p>t_message</p></td>
<td><p>88</p></td>
<td><p>This type is used for bulletin board messages. It leverages the
following properties:</p>
<ul>
<li>TDATA2 = The gumpID</li>
<li>TDATA3 = The minimum gump size</li>
<li>TDATA4 = The maximum gump size</li>
</ul></td>
</tr>
<tr>
<td><p>t_reagent_raw</p></td>
<td><p>89</p></td>
<td><p>Freshly grown reagents...not processed yet. A seed can be created
by using a dagger on a raw reagent (assuming the raw reagent is setup to
have a seed.) A seed can be planted by double clicking it and targeting
the ground (specifically t_dirt items). It leverages the following
properties:</p>
<ul>
<li>TDATA1 = The ID of a t_crop item that will grow the fruit that this
seed comes from. 0 is Nothing.</li>
<li>TDATA2 = The art asset to use as the seed art asset. A copper coin
is default.</li>
</ul></td>
</tr>
<tr>
<td><p>t_eq_client_linger</p></td>
<td><p>90</p></td>
<td><p>Change player to npc for a while.</p></td>
</tr>
<tr>
<td><p>t_snow</p></td>
<td><p>91</p></td>
<td><p>Snow</p></td>
</tr>
<tr>
<td><p>t_it_stone</p></td>
<td><p>92</p></td>
<td><p>This type is an "item stone" that is used to generate items when
the object is double clicked. It has the following properties:</p>
<ul>
<li>MORE1 = The item or template ID to generate</li>
<li>MORE2 = The price (or Plotflags to set?)</li>
<li>MOREX = The regen time (0 = instant)</li>
<li>MOREY = The total amount to deliver (0 = infinite, 0xFFFF = none
left)</li>
</ul></td>
</tr>
<tr>
<td><p>t_unused_93</p></td>
<td><p>93</p></td>
<td><p>This has no use.</p></td>
</tr>
<tr>
<td><p>t_explosion</p></td>
<td><p>94</p></td>
<td><p>This type is used for explosion animations. It leverages the
following properties:</p>
<ul>
<li>MOREX = The damage that the explosion will cause</li>
<li>MOREY = The type of damage (fire, magic, etc)</li>
<li>MOREZ = The distance range for the damage</li>
</ul></td>
</tr>
<tr>
<td><p>t_eq_npc_script</p></td>
<td><p>95</p></td>
<td><p>This type is used to script NPC actions (in the form of a book).
The sphere_defs.scp file says "get rid of this in favor of waiting on
m_events" but it may still exist... if so, it leverages the following
properties:</p>
<ul>
<li>MORE1 = The same as for other books</li>
<li>MORE2L = The current script page</li>
<li>MORE2H = The current offset</li>
<li>MOREZ = The priority for this script (as a percent, this is the
chance they want to "do" this task)</li>
</ul></td>
</tr>
<tr>
<td><p>t_web</p></td>
<td><p>96</p></td>
<td><p>Walk on this and transform into some other object. MORE1 is the
amount of hits the web can take.</p></td>
</tr>
<tr>
<td><p>t_grass</p></td>
<td><p>97</p></td>
<td><p>Can be eaten by grazing animals</p>
<ul>
<li>MORE1 = The regiontype ID that determines what sorts of resources
(fish etc) that it can produce.</li>
</ul></td>
</tr>
<tr>
<td><p>t_arock</p></td>
<td><p>98</p></td>
<td><p>A rock or boulder. can be thrown by giants.</p></td>
</tr>
<tr>
<td><p>t_tracker</p></td>
<td><p>99</p></td>
<td><p>Points to a linked object.</p></td>
</tr>
<tr>
<td><p>t_sound</p></td>
<td><p>100</p></td>
<td><p>This type is used to play sounds. It uses the following
properties:</p>
<ul>
<li>MORE1 = The sound ID</li>
<li>MORE2 = A flag to indicate repetition</li>
</ul></td>
</tr>
<tr>
<td><p>t_stone_town</p></td>
<td><p>101</p></td>
<td><p>This type is used for town stones. It leverages the following
properties:</p>
<ul>
<li>MORE1 = The alignment of the town (chaos, neutral, order)</li>
<li>MORE2 = The amount of gold in the town bank account</li>
</ul></td>
</tr>
<tr>
<td></td>
<td></td>
<td><p><code>t_weapon_mace_crook     102   //</code><br />
<code>t_weapon_mace_pick      103   //</code><br />
<code>t_leather               104   // = leather or skins of some sort.(not wearable)</code><br />
<code>t_ship_other            105   // = some other part of a ship.</code></p></td>
</tr>
<tr>
<td><p>t_bboard</p></td>
<td><p>106</p></td>
<td><p>This type is a bulleting board container that holds t_message
items. It leverages the following properties:</p>
<ul>
<li>TDATA2 = The gumpID of the container</li>
<li>TDATA3 = The minimum gump size</li>
<li>TDATA4 = The maximum gump size</li>
</ul></td>
</tr>
<tr>
<td><p>t_spellbook</p></td>
<td><p>107</p></td>
<td><p>This type is used for the Magery spellbook. It leverages the
following properties:</p>
<ul>
<li>MORE1 = A bit mask of available spells in circles 0-4, so to add all
those spells: set MORE1=0ffffffff</li>
<li>MORE2 = A bit mask of available spells in circles 5-8, so to add all
those spells: set MORE2=0ffffffff</li>
</ul>
<p><strong>Note:</strong> In older sphere versions, MOREX, MOREY, and
MOREZ could be set to add additional spells (necro, etc), but recently
these concepts may have been removed... same with these TDATA
settings:</p>
<ul>
<li>TDATA2 = Required Strength to equip the book</li>
<li>TDATA3 = Type of light pattern it will cast</li>
<li>TDATA4 = A flag to indicate what happens when the light burns out
(0=nothing, 1=delete the object)</li>
</ul></td>
</tr>
<tr>
<td><p>t_corpse</p></td>
<td><p>108</p></td>
<td><p>This type is a container used for all dead corpses. It leverages
the following properties:</p>
<ul>
<li><s>MORE1 = The time of death</s> TIMESTAMP seems to hold the time of
death.</li>
<li>MORE1 = Corpse is already carved? (0=not carved, 1=carved)</li>
<li>MORE2 = The UID of the individual character that landed the killing
blow</li>
<li>MOREX &amp; MOREY = Combined, these make up a single DWORD which
specifies what type of creature this was</li>
<li>MOREZ = The direction it is facing</li>
<li>TDATA2 = The gumpID of the container</li>
<li>TDATA3 = The minimum gump size</li>
<li>TDATA4 = The maximum gump size</li>
</ul>
<p>There are two special TAGs for corpses:</p>
<ul>
<li>TAG.BLOOD = This is the number of times you can carve the corpse and
cause blood to come out (default 5)</li>
<li>TAG.MAXBLOOD = Not certain about this one, but it is likely
related... perhaps it is set on the CHARDEF?</li>
</ul></td>
</tr>
<tr>
<td></td>
<td></td>
<td><p><code>t_track_item            109   // - track a id or type of item.</code><br />
<code>t_track_char            110   // = track a char or range of char id's</code><br />
<code>t_weapon_arrow          111   //</code><br />
<code>t_weapon_bolt           112   //</code><br />
<code>t_eq_vendor_box         113   // = an equipped vendor box</code></p></td>
</tr>
<tr>
<td><p>t_eq_bank_box</p></td>
<td><p>114</p></td>
<td><p>This type is a container that is used for the character bank. It
leverages the following properties:</p>
<ul>
<li>MORE1 = The amount of gold in the account (is this still true?)</li>
<li>MORE2 = The amount to restock to (for NPCs vendors who can buy stuff
from players?)</li>
<li>MOREP = The location in the world (x, y, and z) where the bank box
was opened</li>
<li>TDATA2 = The gumpID for the bank box container</li>
<li>TDATA3 = The minimum gump size</li>
<li>TDATA4 = the maximum gump size</li>
</ul></td>
</tr>
<tr>
<td><p>t_deed</p></td>
<td><p>115</p></td>
<td><p>This type is used to create something else when double clicked.
It is perhaps the best solution for a player to place a <em>multi</em>
part item like a house. When double clicked, it will prompt for a target
location. It leverages the following properties:</p>
<ul>
<li>MORE1 = The ID of the item that will be created at the target
location</li>
<li>MORE2 = The previous key ID (ideally this is set when a house or
ship are re-deeded so that all the existing keys will still work)</li>
</ul></td>
</tr>
<tr>
<td><p>t_loom</p></td>
<td><p>116</p></td>
<td><p>This type of device is used by weavers who turn wool or thread
into bolts of cloth. It leverages the following properties:</p>
<ul>
<li>MORE1 = The ID of the currently loaded resource (wool or
cotton/flax) that is being woven</li>
<li>MORE2 = The amount of resources currently in the loom</li>
</ul></td>
</tr>
<tr>
<td><p>t_bee_hive</p></td>
<td><p>117</p></td>
<td><p>This type is used for beehives. It leverages the following
properties:</p>
<ul>
<li>MORE1 = The amount of honey which has accumulated in the hive</li>
</ul></td>
</tr>
<tr>
<td><p>t_archery_butte</p></td>
<td><p>118</p></td>
<td><p>This type is used for practice archery targets. When double
clicked, the target will first check if you have an archery weapon
equipped and if so, it will return some ammo. It leverages the following
properties:</p>
<ul>
<li>MORE1 = The ID for the type of ammo currently stuck in the
target</li>
<li>MORE2 = The amount of items stuck in the target</li>
</ul></td>
</tr>
<tr>
<td></td>
<td></td>
<td><p><code>t_eq_murder_count       119   // = my murder count flag.  MORE1 contains the amount of time before it expires. </code><br />
<code>t_eq_stuck              120   // we are stuck in a web</code><br />
<code>t_trap_inactive         121   //  = a safe trap.</code><br />
<code>//t_unused_122          122</code><br />
<code>t_bandage               123   //  = can be used for healing.</code><br />
<code>t_campfire              124   //  = this is a fire but a small one.</code><br />
<code>t_map_blank             125</code><br />
<code>t_spy_glass             126</code><br />
<code>t_sextant               127</code><br />
<code>t_scroll_blank          128</code></p></td>
</tr>
<tr>
<td><p>t_fruit</p></td>
<td><p>129</p></td>
<td><p>This type is used for fruit. When double clicked, fruit will be
eaten. Fruit can be grown from crops (t_crop). It leverages the
following properties:</p>
<ul>
<li>TDATA1 = The ID of a t_crop item that this fruit comes from (If not
set, this fruit may not have a seed, use zero to be certain)</li>
<li>MOREM = Is the amount (0 to 127) of "food units" that will be gained
when the item is used (eaten)</li>
<li>MOREZ = Is the poison level of the fruit</li>
</ul></td>
</tr>
<tr>
<td></td>
<td></td>
<td><p><code>t_water_wash            130   // water that will not contain fish. (for washing or drinking)  TDATA1 is a flag that indicates whether the container is empty or not </code><br />
<code>t_weapon_axe            131   // not the same as a sword. but uses swordsmanship skill</code></p></td>
</tr>
<tr>
<td><p>t_weapon_xbow</p></td>
<td><p>132</p></td>
<td><p>This type is used for crossbow weapons. It is essentially
identical to t_weapon_bow.</p></td>
</tr>
<tr>
<td></td>
<td></td>
<td><p><code>t_spellicon             133</code><br />
<code>t_door_open             134</code><br />
<code>t_meat_raw              135   // just a meaty part of a corpse. (uncooked meat)</code><br />
<code>t_garbage               136</code></p></td>
</tr>
<tr>
<td><p>t_keyring</p></td>
<td><p>137</p></td>
<td><p>This type is a container used to store keys. It leverages the
following properties:</p>
<ul>
<li>TDATA2 = The gumpID</li>
<li>TDATA3 = The minimum gump size</li>
<li>TDATA4 = The maximum gump size</li>
</ul></td>
</tr>
<tr>
<td><p>t_table</p></td>
<td><p>138</p></td>
<td><p>doesn't really do anything.</p></td>
</tr>
<tr>
<td><p>t_floor</p></td>
<td><p>139</p></td>
<td></td>
</tr>
<tr>
<td><p>t_roof</p></td>
<td><p>140</p></td>
<td></td>
</tr>
<tr>
<td><p>t_feather</p></td>
<td><p>141</p></td>
<td><p>a birds feather</p></td>
</tr>
<tr>
<td><p>t_wool</p></td>
<td><p>142</p></td>
<td><p>wool cut from a sheep.</p></td>
</tr>
<tr>
<td><p>t_fur</p></td>
<td><p>143</p></td>
<td></td>
</tr>
<tr>
<td><p>t_blood</p></td>
<td><p>144</p></td>
<td><p>blood of some creature</p></td>
</tr>
<tr>
<td><p>t_foliage</p></td>
<td><p>145</p></td>
<td><p>This type is very similar to t_crops, the difference being the
foliage does not disappear when the fruit is harvested. It leverages the
following properties:</p>
<ul>
<li>MORE1 = Time in seconds before this item will grow to the next stage
(this overrides the default server defined number)</li>
<li>TDATA1 = Is the ID of the first stage of the crop (the sprout)</li>
<li>TDATA2 = Is the ID of the next stage of the crop (or zero if this is
the final mature crop which will bear the fruit)</li>
<li>TDATA3 = Is the ID of the fruit that this plant will grow and should
only be set on the <em>ripe</em> plant</li>
</ul>
<p><strong>Note</strong> This type has unusual TIMER behavior in that
regardless of the ATTR flags, the timer will restart when it reaches
zero.</p></td>
</tr>
<tr>
<td></td>
<td></td>
<td><p><code>t_grain                 146</code><br />
<code>t_scissors              147</code><br />
<code>t_thread                148</code><br />
<code>t_yarn                  149</code><br />
<code>t_spinwheel             150</code><br />
<code>t_bandage_blood         151   //  = can't be used for healing.</code><br />
<code>t_fish_pole             152</code><br />
<code>t_shaft                 153   // bolt or arrow.</code><br />
<code>t_lockpick              154</code><br />
<code>t_kindling              155</code><br />
<code>t_train_dummy           156</code><br />
<code>t_train_pickpocket      157</code><br />
<code>t_bedroll               158</code><br />
<code>t_bellows               159</code></p></td>
</tr>
<tr>
<td><p>t_hide</p></td>
<td><p>160</p></td>
<td><p>Made into leather.</p>
<ul>
<li>TDATA1 = Hold ID or DEFNAME of custom cut leather (or any
item).</li>
</ul></td>
</tr>
<tr>
<td><p>t_cloth_bolt</p></td>
<td><p>161</p></td>
<td><p>A bolt of cloth.</p></td>
</tr>
<tr>
<td><p>t_board</p></td>
<td><p>162</p></td>
<td><p>Logs are plained into decent lumber</p></td>
</tr>
<tr>
<td><p>t_pitcher</p></td>
<td><p>163</p></td>
<td><p>A pitcher holding a liquid of some kind.</p>
<ul>
<li>TDATA1 is a flag that indicates whether the container is empty or
not.</li>
</ul></td>
</tr>
<tr>
<td><p>t_pitcher_empty</p></td>
<td><p>164</p></td>
<td><p>An empty pitcher that can or did hold a liquid.</p>
<ul>
<li>TDATA1 is a flag that indicates whether the container is empty or
not.</li>
</ul></td>
</tr>
<tr>
<td><p>t_dye_vat</p></td>
<td><p>165</p></td>
<td><p>For dyeing items with.</p></td>
</tr>
<tr>
<td><p>t_dye</p></td>
<td><p>166</p></td>
<td><p>Dyes to set colors on a t_dye_vat</p></td>
</tr>
<tr>
<td><p>t_potion_empty</p></td>
<td><p>167</p></td>
<td><p>Empty bottle.</p></td>
</tr>
<tr>
<td><p>t_mortar</p></td>
<td><p>168</p></td>
<td><p>Alchemists mortar and pestle.</p></td>
</tr>
<tr>
<td><p>t_hair_dye</p></td>
<td><p>169</p></td>
<td><p>Hair dye.</p></td>
</tr>
<tr>
<td><p>t_sewing_kit</p></td>
<td><p>170</p></td>
<td><p>Tailoring sewing kit.</p></td>
</tr>
<tr>
<td><p>t_tinker_tools</p></td>
<td><p>171</p></td>
<td><p>Tinker's tools.</p></td>
</tr>
<tr>
<td><p>t_wall</p></td>
<td><p>172</p></td>
<td><p>Wall of a structure.</p></td>
</tr>
<tr>
<td><p>t_window</p></td>
<td><p>173</p></td>
<td><p>Window for a structure. MOREZ is the light pattern</p></td>
</tr>
<tr>
<td><p>t_cotton</p></td>
<td><p>174</p></td>
<td><p>Cotton from the plant</p></td>
</tr>
<tr>
<td><p>t_bone</p></td>
<td><p>175</p></td>
<td><p>A bone from a corpse.</p></td>
</tr>
<tr>
<td><p>t_eq_script</p></td>
<td><p>176</p></td>
<td><p>This type can have tags and can be equipped. Possibly used for
memory objects that leverage @Equip and @UnEquip triggers.</p></td>
</tr>
<tr>
<td><p>t_ship_hold</p></td>
<td><p>177</p></td>
<td><p>A ships hold.</p>
<ul>
<li>TDATA2 is the gumpID</li>
<li>TDATA3 is the minimum gump size</li>
<li>TDATA4 is the maximum gump size</li>
<li>MORE1 = the lock code. normally this is the same as the uid (magic
lock=non UID)</li>
<li>MORE2= 0-1000 = How hard to pick or magic unlock. (conflict with
door ?)</li>
</ul></td>
</tr>
<tr>
<td><p>t_ship_hold_lock</p></td>
<td><p>178</p></td>
<td><p>A locked ship's hold.</p>
<ul>
<li>MORE1 = the lock code. normally this is the same as the uid (magic
lock=non UID)</li>
<li>MORE2= 0-1000 = How hard to pick or magic unlock. (conflict with
door ?)</li>
</ul></td>
</tr>
<tr>
<td><p>t_lava</p></td>
<td><p>179</p></td>
<td></td>
</tr>
<tr>
<td><p>t_shield</p></td>
<td><p>180</p></td>
<td><p>This type is used to indicate the object is an equipable shield.
It has the following properties:</p>
<ul>
<li>MORE1L = The current amount of hitpoints the item has</li>
<li>MORE1H = The maximum hitpoints for the item</li>
<li>MORE2 = The number of remaining charges (if magical)</li>
<li>MOREX = The spell type (if magical)</li>
<li>MOREY = The spell strength (0-1000)</li>
</ul></td>
</tr>
<tr>
<td><p>t_jewelry</p></td>
<td><p>181</p></td>
<td><p>This type is used for equpable jewelry. It leverages the
following properties:</p>
<ul>
<li>MORE1L = The current amount of hitpoints the item has</li>
<li>MORE1H = The maximum hitpoints for the item</li>
<li>MORE2 = The number of remaining charges (if magical)</li>
<li>MOREX = The spell type (if magical)</li>
<li>MOREY = The spell strength (0-1000)</li>
<li>TDATA2 = Required Strength to equip the item</li>
<li>TDATA3 = Light pattern</li>
<li>TDATA4 = A flag to indicate what happens when the light burns out
(0=nothing, 1=delete the object)</li>
</ul></td>
</tr>
<tr>
<td><p>t_dirt</p></td>
<td><p>182</p></td>
<td><p>This type is used to represent a patch of dirt where something
can be planted.</p></td>
</tr>
<tr>
<td><p>t_script</p></td>
<td><p>183</p></td>
<td><p>This type can have tags, but can NOT be equipped.</p></td>
</tr>
<tr>
<td><p>t_spellbook_necro</p></td>
<td><p>184</p></td>
<td><p>AOS Necromancy spellbook (should have MOREZ=100 by
default)</p></td>
</tr>
<tr>
<td><p>t_spellbook_pala</p></td>
<td><p>185</p></td>
<td><p>AOS Paladin spellbook (should have MOREZ=200 by default)</p></td>
</tr>
<tr>
<td><p>t_spellbook_extra</p></td>
<td><p>186</p></td>
<td><p>some spellbook for script purposes (MOREZ=basic offset)</p></td>
</tr>
<tr>
<td><p>t_spellbook_bushido</p></td>
<td><p>187</p></td>
<td><p>SE Bushido spellbook (should have MOREZ=400 by default)</p></td>
</tr>
<tr>
<td><p>t_spellbook_ninjitsu</p></td>
<td><p>188</p></td>
<td><p>SE Ninjitsu spellbook (should have MOREZ=500 by default)</p></td>
</tr>
<tr>
<td><p>t_spellbook_arcanist</p></td>
<td><p>189</p></td>
<td><p>ML Spellweaver spellbook (should have MOREZ=600 by
default)</p></td>
</tr>
<tr>
<td><p>t_multi_custom</p></td>
<td><p>190</p></td>
<td><p>Customisable multi</p></td>
</tr>
<tr>
<td><p>t_spellbook_mystic</p></td>
<td><p>191</p></td>
<td><p>SA Mysticism spellbook (should have MOREZ=677 by
default)</p></td>
</tr>
<tr>
<td><p>t_hoverover</p></td>
<td><p>192</p></td>
<td><p>Hover-over item (CAN_C_HOVER can hover over blocking
items)</p></td>
</tr>
<tr>
<td><p>t_spellbook_bard</p></td>
<td><p>193</p></td>
<td><p>SA Bard spellbook (should have MOREZ=700 by default)</p></td>
</tr>
</tbody>
</table>

## Scripted TYPEDEFs

| DEFNAME | File | Description |
|----|----|----|
| t_advance_gate | ??.scp \|\| MORE = ID of character to change into |  |

## Syntax

The syntax for defining a type is:

`[TYPEDEF `*`defname`*`]`  
`TERRAIN=`*`id`*  
`TERRAIN=`*`start_id`*`, `*`end_id`*  
  
`ON=`*`trigger_name`*  
`    `*`script`*  
  
`ON=`*`trigger_name`*  
`    `*`script`*  
  

Any number of triggers can be handled by one
[TYPEDEF](TYPEDEF "wikilink") definition, however it is not possible to
handle the same trigger twice without using multiple definitions.

The trigger name can be the name of any [item
trigger](Items#Triggers "wikilink"). The return value from the script
can affect Sphere's hardcoded behaviour in different ways. See the
documentation for the trigger to discover what parameters are passed in
to each trigger and what the return values do.

**Note:** If the *defname* matches any of Sphere's hardcoded types (see
'typedefs' block in sphere_defs.scp), then the
[TYPEDEF](TYPEDEF "wikilink") can be used to override the behaviours of
items of that type.

## Examples

<spherescript> // // Water definition from default script pack. //
\[TYPEDEF t_water\] TERRAIN = 0a8 0ab TERRAIN = 0136 0137
</spherescript>

<spherescript> // // Makes an item speak when double clicked. //
\[TYPEDEF t_exampletype\] ON=@DClick

` SAY I have been double clicked!`  
` RETURN 2`

</spherescript>

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Definitions](Category:_Definitions "wikilink")
