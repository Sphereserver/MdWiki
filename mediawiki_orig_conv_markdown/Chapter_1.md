```{=mediawiki}
{{Languages|Chapter_1}}
```
## Numbers

The first thing you\'ll notice while looking through SPHERE scripts is
the wide variety of ways to write numbers. Since numbers are insanely
important to a SPHERE scripter, this is the first lesson in the series.
By the end of the lesson, I hope that you have a general understanding
of hexadecimal, decimal and binary numbering systems, and SPHERE\'s ways
of identifying each. You will also know how to generate random numbers
either from a series or from a list of choices.

The first thing you need to understand is that the way we count is not
the only way to count. Our numbering system contains ten digits (0, 1,
2, 3, 4, 5, 6, 7, 8, and 9). Therefore, at the tenth number, we have to
add an extra column to the number, and reset the first column to zero
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10). That\'s why our numbering system works
the way it does.

In the decimal system, without realizing it, we write our numbers to
mean powers of ten. For example, if you take the number 17282 (which I
just made up), and divide it down we get this:

  ------------------- ------- ------ ----- ---- ---
  Power of ten        4       3      2     1    0
  Ten to that power   10000   1000   100   10   1
  Digit               1       7      2     8    2
  ------------------- ------- ------ ----- ---- ---

To reach the number 17282 from here, we simply take ten to the power of
the number in the top row, multiply it by the number in the bottom row,
and then add all those numbers together. We get 10000 + 7000 + 200 +
80 + 2. Obviously, this is simplistic, and we do it without even
realizing we\'re doing it. You\'re probably thinking \"Riiight, what
does Taran think he\'s getting at?\" Well, we aren\'t so special that
our counting system is the only way to count.

Now, there is another numbering system that is used almost solely by
computers. It only contains two numbers (1 and 0) and is therefore
called the binary (meaning two) system. Binary numbers look like this:
101011101101, and you often see them in ads for computers and other
electronic equipment (oftentimes they are shown streaming out of a CD
player on television commercials). Digits in the binary system are
called bits (short for BInary digiT)Binary numbers are almost impossible
to translate to decimal directly, and so some math must be done.

Binary works in the same way, by adding powers of a number. In the case
of binary, since there are two numbers in the whole system, that number
is naturally two. Here are some examples of powers of two. These numbers
might look familiar to some people.

  ------------ --------------- ----------------
  Power of 2   Binary number   Decimal number
  0            1               1
  1            10              2
  2            100             4
  3            1000            8
  4            10000           16
  5            100000          32
  6            1000000         64
  7            10000000        128
  8            100000000       256
  9            1000000000      512
  10           10000000000     1024
  ------------ --------------- ----------------

Ridiculous eh? :)

We need a better system! The reason we get such strange results is
because 10 is not a power of two. We need to find a system where the
number base IS a power of two. The most commonly used system used is
base-16, or hexadecimal. I\'m sure if you\'ve perused the SPHERE boards,
you\'ve seen the word hex floating around. No, this isn\'t a curse or
evil spell, it\'s a short way of saying \"hexadecimal\".

  -------- --------- -------------
  Binary   Decimal   Hexadecimal
  1        1         1
  10       2         2
  11       3         3
  100      4         4
  101      5         5
  110      6         6
  111      7         7
  1000     8         8
  1001     9         9
  1010     10        A
  1011     11        B
  1100     12        C
  1101     13        D
  1110     14        E
  1111     15        F
  10000    16        10
  -------- --------- -------------

See how it works? There are an extra six numbers added onto the end of
the system, represented by the first six letters of the alphabet.

Now, in SPHERE scripting, you are almost NEVER going to be dealing with
binary numbers that are NOT powers of two, and if you do, you can simply
use any scientific calculator to figure it out. But it\'s a lot easier
in hexadecimal.

(This is the last table, I promise!!)

  --------------- -------------
  Binary          Hexadecimal
  000000001 (1)   01
  000000010 (2)   02
  000000100 (3)   04
  000001000 (4)   08
  000010000 (5)   010
  000100000 (6)   020
  001000000 (7)   040
  010000000 (8)   080
  100000000 (9)   0100
  --------------- -------------

As you can see, there\'s a bit of a pattern in the hexadecimal column.
You might be thinking, there seems to be some sort of pattern of the
numbers 1, 2, 4 and 8. And you would be right. Another detail you may
notice is the zeros in front of the hexadecimal numbers (like 0100,
rather than just 100). In SPHERE, that 0 tells the script \"Hey, this
number is HEX!\" 0100 and 100 are very different numbers.

Let\'s say, for a SPHERE script, you need to set the 13th bit of a
number (FLAGS, for example), you could write something like this:

**SRC.FLAGS \|= 8192**

But would you really remember that 8192 is 2 to the 13th power? I
didn\'t think so. What would be easier is to go down through your list
in your head, until you reach the 13th number. (Remember, START AT ZERO
when you\'re counting!)

  ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------- ------- ------- -------
  01     02     04     08     010    020    040    080    0100   0200   0400    0800    01000   02000
  2\^0   2\^1   2\^2   2\^3   2\^4   2\^5   2\^6   2\^7   2\^8   2\^9   2\^10   2\^11   2\^12   2\^13
  ------ ------ ------ ------ ------ ------ ------ ------ ------ ------ ------- ------- ------- -------

And there you have it. The first 14 powers of two in hexademical.

**SRC.FLAGS \|= 02000**

The above code is identical to the previous example. 8192 (decimal) is
EQUAL to 02000 (hexadecimal)

**8192 = 02000**

You may be saying, \"How do I know he\'s just not making all of this
up?\" Well, our wonderful friends at Microsoft have provided us with a
nice tool that converters from decimal to hexadecimal to binary to octal
(ANOTHER numbering system that is useless in SPHERE, so we will not deal
with it). It\'s called the Calculator. You may find it by clicking your
start button, going to Programs, then Accessories. Calculator should be
sitting there looking pretty. Once in the calculator program, go to the
View menu, and click Scientific. You\'ll see the display drastically
change. To convert a number between numbering systems, simply click on
the original system (Dec), type a number (8192), then click on the
button for the other system (Hex). Automagically, Windows will convert
your decimal number to hexadecimal. Stick a zero on the front, and
SPHERE will be perfectly happy with it.

This is probably the hardest thing in all of SPHERE scripting to
understand. Luckily, because of the next section, you won\'t have to
deal with scary numbers most of the time. If I still have you at the end
of this lesson, I know you\'re going to do great!

Onward to some SPHERE scripting!

## Defnames

Here\'s a list of scary numbers you might encounter while programming in
SPHERE.

  ------------------ ----------------------------
  The Scary Number   What it means
  0eed               ID of a gold coin
  0dda               ID of a red moongate
  1650,1440          Coordinates of Britain
  021                The code number for red
  04000              The invisible color
  04000efad          An item\'s serial number
  4                  The PLEVEL of a GM
  2048 (or 0800)     Flag for incognito spell
  010 (or 16)        Memory type for aggressors
  ------------------ ----------------------------

Obviously, no one is going to want to remember those numbers. Back in
the old days, before SPHERE and TUS (pre-.50 SPHERE) and even into the
mists of Grayworld (pre-.41 TUS), we all had to remember those numbers.
I know all of those numbers I just said (except the serial number which
I just made up), plus a couple dozen more, by heart. Luckily for those
of you who don\'t like to sit around remembering numbers all day, SPHERE
has developed a system whereby things can be identified by names instead
of numbers.

Actually, the things are still identified by numbers. It\'s the numbers
which are identified by the name.

In the game, type .add 0eed and press enter. A target will come up and
you\'ll create a single gold piece.

Now type .add i_gold and press enter. You will create the same single
gold piece.

Now which is easier to remember, 0eed or i_gold. I would say that i_gold
wins by a long shot. But how does this magic happen? Let\'s take a look
at the script definition for a piece of gold. Don\'t worry about
understanding it. I\'ll explain item scripts in full in the next
section! You can find this script in the file sphere_item_resources.scp.

`<font color="darkgreen">`{=html}`[ITEMDEF 0eed]`\
`//gold coin`\
`<font color="ff0000">`{=html}`DEFNAME=i_gold``</font>`{=html}\
`TYPE=T_GOLD`\
`VALUE=1`\
`CATEGORY=Provisions - Miscellaneous`\
`SUBSECTION=Coins`\
`DESCRIPTION=Gold Coin`\
`DUPELIST=0eee,0eef``</font>`{=html}\

I have highlighted in red the line that really matters for the purposes
of this lesson. Take note of the 0eed in the top line of the script, and
then ignore the rest of it. That 0eed is the real item number of this
item. We\'ll cover item numbers more in the next section.

But the real line we want to see the
`<font color="ff0000">`{=html}DEFNAME=i_gold`</font>`{=html} line. This
is where the script tells the server, \"I want item 0eed to be
identified by the text i_gold from here on.\" If you tried to refer to
i_gold before the server read this script (more on reordering scripts in
[Chapter 2](Chapter_2 "wikilink"), the server would spit out an error,
but now it knows what that refers to, so you can use it in the game or
in another script.

You should ALWAYS give items you create a DEFNAME that fits the item.
Usually the defname will be defined in the \[ITEMDEF\] identifier itself
(again, more on this later), but if you insist upon using numbers, be
sure you give it an easy-to-remember name (not golden_gulash for a
viking sword). It makes it easier to remember names than numbers.

A second way to define a DEFNAME is by using the \[DEFNAME\] tag in a
script. Here is an example of that:

`<font color="darkgreen">`{=html}`[DEFNAME colors]`\
`color_blue 02`\
`color_red 021`\
`color_green 041``</font>`{=html}\

You\'ll find a script similar to this in spheredefs.scp, another file
that should be loaded before any other file.

Here\'s the rundown on this script, line by line:

**Line 1**: This is where the type of script and the defname (yes colors
is the defname of this script) is defined. This tells the server what
type of script to expect between this and the next identifier
(identifiers are the lines contained in square brackets). All
identifiers have this format. The first parameter is the script type.
These are numerous, and I will go over them as we get to them. The
second parameter is either an ID number or a defname. In most cases, in
the scripts you write, it will be a defname. The only exceptions to this
I can think of would be if you used a program to insert a new item into
the client files.

**Lines 2-4**: These set up your individual DEFNAME pieces. It says that
color_blue is equal to 02, color_red is equal to 021, and color_green is
equal to 041. You may have any number of spaces between the name and the
value. The definitions contained in spheredefs.scp are among the most
useful you will encounter, as they prevent you from writing the long
scary numbers we went over in the previous section. These include things
like names for flags, names for item attributes, names for the built-in
MIDI or MP3 music, names for memory types, and many other things. Look
through the file to see what it offers you.

That\'s about it for DEFNAMEs. You\'ll see more of these later as we
cover other types of scripts.

Now go on to learn about items.

## ITEMDEF

Or, how to make a mountain from a molehill, SPHERE style

Most people make item scripting much harder than it needs to be. For the
purposes of this tutorial, since there is a more advanced one later, we
will simply go over the basics of an ITEM script, line by line. We\'ll
be using the gold script from the previous lesson, provided I can find
it again\....

Ah, here it is, conveniently color coded for your viewing pleasure!

`<spherescript>`{=html}\[ITEMDEF 0eed\] //gold coin DEFNAME=i_gold
TYPE=T_GOLD VALUE=1 CATEGORY=Provisions - Miscellaneous SUBSECTION=Coins
DESCRIPTION=Gold Coin DUPELIST=0eee,0eef`</spherescript>`{=html}

This is the simplest of item scripts, since it has no additional
behaviors beyond existing. I will go through this line by line,
describing to you what each line does, and how it affects the end
result.

**Line 1**: \[ITEMDEF 0eed\]

The first lines of an item script are frequently the most important.
Basically, this line tells the server \"Hey this is an item and I want
it to be called 0eed!\" The server then looks through one of the client
files (specifically art.idx), and identifies whether or not this item is
one of the built-in items. I think all items below 04500 are defined as
built-in items, so never define a new item in that range. By typing this
line, you tell the server that an item script is following. You also
define 0eed as a valid item, which will definitely help later on when
you try to give gold to players!

**Line 2**: // gold coin

This is the SPHERE version of comment. C programmers will recognize the
format immediately. If you type // on any line of code, everything
beyond that is ignored by the script reader. This can be on a line by
itself, or at the end of a line to explain what the specific line does.
In all cases, it won\'t affect your program, just make it easier to
read.

**Line 3**: DEFNAME=i_gold

You should know by now what this does! If you don\'t, go back and read
the previous lesson! It tells the server that i_gold and 0eed mean the
same thing. In item scripts, all parameters are defined in that format:

variable=value

You will see later on, when we get into scripting, how that format will
help you more than you would believe. Items have a good number of
variables that you can define, including:

-   DEFNAME
-   ID
-   TYPE
-   VALUE
-   RESOURCES

Other variables depend on the value of the TYPE. Which leads us right
into\...

**Line 4**: TYPE=t_gold

The first thing you might say is \"What the heck is t_gold?\" Well it\'s
a DEFNAME. Actually it\'s a number. And that number is 72. If you want
to check me on this, look in spheredefs.scp, it\'s there! Writing
TYPE=72 would have the exact same effect.

There are, currently, 183 built-in item types. These are hardcoded item
types that contain predefined actions for an item. If an item has no
type, when you click it, you get the \"You cannot think of a way to use
that item\" message. There is a complete list of types, and how to set
them up, here . All you need to know for now is that setting the type of
this item to t_gold has no effect other than to make the item act like a
gold coin (i.e. you can buy stuff with it!) Setting another item to type
t_gold would probably make the server think that you can buy stuff with
that item too. I\'ve never tried this. It might be an interesting way to
have unique currencies\...

**Line 5**: VALUE=1

This defines how much the item costs when purchased, in gold. Of course,
this is one gold piece, which is worth, well, one gold piece. So the
value of the item is one.

**Lines 6-8**: CATEGORY, SUBSECTION, DESCRIPTION

These are lines used only by SPHERE\'s GM tool, Axis, which actually
saves you a lot of work by typing \".add i_gold\" for you. More
importantly, it types \".add 01737\" and things like that for you, for
items that were not important enough to get their own separate DEFNAME.

**Line 9**: DUPEITEM

It would be a ton of work for the SPHERE team to define all 8000 items
that came with the game, especially when many of them are the same. (For
an example of this, use the .xflip command on a door or sign. It cycles
through all of the DUPEITEMs for that the item being flipped.) The
numbers listed here are item numbers, which probably have not been
defined yet. Here is the script for item 0eee:

`<spherescript>`{=html}\[ITEMDEF 0eee\] //gold coins DUPEITEM=0eed
CATEGORY=Provisions - Miscellaneous SUBSECTION=Coins DESCRIPTION=Gold
Coins`</spherescript>`{=html}

As you can see, there is only one parameter for this whole item. It
reiterates the DUPEITEM and sends the server looking to our 0eed (or
i_gold) item for more information, such as TYPE and VALUE. DUPEITEM only
exists to save typing. You probably won\'t use it.

## CHARDEF

Or, what it takes to make a naked man who can stand around and say
\"Huh?\"

NPCs\... They make the world go around. They are what makes UO a unique
multiplayer game. The monsters and NPCs you create make your server
unique from any other. This section of chapter one will cover how to
create a simple naked man who walks around and says little more than
\"Huh?\" (or \"Stop thief!\" if you tell him to!).

First of all, we\'ll look at the script for a simple naked man. I\'m
pulling this out of spherechar_human.scp.

`<spherescript>`{=html}\[CHARDEF 0190\] DEFNAME=c_man Name=Man
ICON=i_pet_MAN CAN=MT_EQUIP\|MT_WALK\|MT_RUN\|MT_USEHANDS
RESOURCES=i_flesh_head, i_flesh_torso, i_flesh_right_arm,
i_flesh_left_arm FOODTYPE=15 t_food, t_fruit DESIRES=i_gold,e_notoriety
AVERSIONS=t_TRAP,t_eerie_stuff SHELTER=r_house BLOODCOLOR=0

TSPEECH=spk_human_prime TSPEECH=spk_human_default
TEVENTS=e_Human_HearUnk DESCRIPTION=Man SUBSECTION=Miscellaneous
CATEGORY=Civilized`</spherescript>`{=html}

As you can see, it doesn\'t look a lot different than the item scripts
we examined in the previous section. There are a lot of variables set
that are the same, including DEFNAME, DESCRIPTION, and the other Axis
variables.

But, there are a lot of new things here that we will again go over, one
line at a time! And it\'s longer this time! Let the good times roll!
(Sorry if you\'re not American.. All my American clichés are probably
growing irritating!)

**Line 1**: \[CHARDEF 0190\]

Surprise surprise! It\'s an identifier, telling the server that we are
going to be defined a character between this and the next
\[identifier\]. And we also tell it that our character, or NPC, will
have the ID 0190. The server knows that this ID is one of the built-in
IDs. In fact, it\'s the ID of a naked man. You also know that 0190 is
hexadecimal is 400 in decimal right? :) Well why didn\'t you know that!
Oh I\'m just kidding, you don\'t need to know things like that.

**Line 2**: DEFNAME=c_man

Nothing new here. c_man is now the same as 0190. Most character DEFNAMEs
will begin with C and then an underscore (c\_) like you see above.

**Line 3**: Name=Man

Oh oh! Something new! Items come with default names, built in to the
server. Characters don\'t. So we have to assign him a name. We can give
him any name we want, but since this isn\'t a specific man, we just give
him a name telling us what he is. In this case \"Man\".

**Line 4**: ICON=i_pet_man

It took me a while to figure this one out. ICON defines what little
picture you see when you\'re using the Tracking skill and all those
little miniature creatures appear in the window. Those are actually
items, all the i_pet items. To find out what the i_pet item for your
creature should be, create him in the game using .addnpc, then use the
.shrink command on him. The ID of the item that he becomes is your i_pet
item.

**Line 5**: CAN=mt\_\*

(In case you don\'t know, \* means \"anything\" for those who use
Linux.)

This is one of the most important lines of your character script, next
to the ID we give him in the first line. First, because it allows us to
tell the game what our NPC can do and what he can\'t do. There are only
a few mt\_\* items, all of which are defined in spheredefs.scp. For the
purpose of the lesson, I am going to copy them here. (The purple
comments are mine.)

`<spherescript>`{=html}MT_NONMOVER 0 // We can\'t move at all MT_GHOST
01 // We can walk through doors and such, like a ghost MT_SWIM 02 // I
can swim! (Water elementals, dolphins, etc) MT_WALK 04 // I can move.
Set this if you want your creature to move. MT_FLY 010 // Moves through
(supposed to be over) trees MT_FIRE_IMMUNE 020 // Immune to damage by
fire. Setting this on a player is bad. :) MT_EQUIP 00100 // Can equip
things MT_USEHANDS 00200 // Can use his hands to carry things (or open
doors) MT_MALE 0 // Is a male MT_FEMALE 00800 // Is a female MT_NONHUM
01000 // Non-human. I\'m not sure what this does. MT_RUN 02000 // Can
move really fast!`</spherescript>`{=html}

According to this chart, we can see that if we don\'t give a creature a
CAN flag, it will be an MT_MALE and an MT_NONMOVER (the two zeros). You
can see from the example that by putting a \| (found by pressing
shift+backslash) between two CAN flags, we can give him more than one.
In this case, we allow our man to equip things, walk, run, and use his
hands. (An interesting fact is, even creatures that don\'t have hands
can be set to use their hands, thus allowing them to carry light
sources. Fire elementals do this. That\'s how they glow.)

**Line 6**: RESOURCES

Resources is a very morbid name for this setting. Especially for a
person. These are the items that you get whenever you chop up this
creature\'s corpse. Scary eh? :)

**Line 7-10**: FOODTYPE, DESIRES, AVERSIONS

**FOODTYPE**: Defines what kind of food the npc will eat and if
NPC_AI_FOOD is on it\'ll make the npc look for this food + grass when
he\'s hunger.

**DESIRES**: Defines what kind of items will the npc be interested in,
if NPC_AI_EXTRA is on it\'ll show what items the npc will loot of
players corpses or walk towards when it\'s on the ground.

**AVERSIONS**: No idea, but I think it tells the npc what sort of NPCs
he\'ll try to fight, for example: I have a horse with e_horse as an
event, and an imp without any events, if the npc has AVERSIONS=e_horse
it\'ll prefer to fight the horse.

**Line 11**: BLOODCOLOR

Ever wanted to make your players have green blood? This is where you do
it! A color number or a color defname will work fine. (Try to learn the
numbers for common colors, it makes it so much easier.)

The rest of it: TSPEECH and TEVENTS

We\'re going to cover these in sections of their own. They are probably
the most complex topics in scripting! (How many times do you suppose
I\'m going to say that before it\'s actually true?)

*`<font color="darkblue">`{=html}Some other things:`</font>`{=html}*

On 56B we have some other fields like MOVERATE,RESLEVEL,RESDISPDNID and
RESDISPDNHUE. They sound some difficult and strange thing but they
aren\'t. Here\'s the explanation for them:

**MOVERATE**: This setting (that can only be writed at the npc chardef)
controls how fast the npc moves. The smaller the value, the faster the
npc is. For example, if I have a horse chardef with default moverate
(100) and another with moverate=60, the one with 60 will walk and run a
lot faster than the other horse. This is great for making really
difficult monsters to kill.

**RESLEVEL**: This tells sphere what version of uo this monster is from,
for example, a Wanderer of the Void will have RESLEVEL=3 (3=AOS) (see
sphere_defs.scp for a complete list), so only accounts with RESDISP 3 or
bigger can see this monster as he really is.

*NOTE*: If you set a lower value for RESLEVEL, if the player doesn\'t
have this npc anim he\'ll crash.

**RESDISPDNID**: As you probably have seen, I used a lot of \"as he
really\" is, exactly because of this setting, this tells the client what
monster will the player see instead of the correct one. For example,
this Wanderer of the Void will show as Wanderer of the Void for those
who has ACCOUNT.RESDISP=3 or bigger, but for those who has smaller
values it\'ll show as a c_spectre (if you so define).

**RESDISPDNHUE**: This defines what color will the player see the
monster if the RESDISPDNID id is shown to him (have an account.resdisp
lower than the reslevel of this char)

Here\'s an example for those new settings:

`<spherescript>`{=html}\[CHARDEF 310\] DEFNAME=c_Wailing_Banshee
NAME=Wailing Banshee SOUND=snd_monster_zombie1 ICON=i_pet_wailingbanshee
DAM=11,16 RESDISPDNID=c_spectre RESLEVEL=3 RESDISPDNHUE=01 ARMOR=20
CAN=MT_WALK\|MT_FLY
DESIRES=i_gold,e_notoriety,e_horses,c_man,c_woman,t_corpse CATEGORY=New
Monsters SUBSECTION=AOS DESCRIPTION=Wailing Banshee

ON=@Create

`   NPC = brain_monster`\
`   FAME = {100 3000}`\
`   KARMA = {-5000 -6999}`\
`   STR = {126 166}`\
`   INT = {86 115}`\
`   DEX = {41 75}`\
`   MAGICRESISTANCE = {75.0 95.0}`\
`   TACTICS = {45.0 75.0}`\
`   WRESTLING = {50.0 70.0}`

ON=@NpcRestock

`   ITEM = i_gold, {50 100}`\
`   ITEM = i_reag_daemon_bone, {2 6}``</spherescript>`{=html}

And there you have it. A simple character script and some new things.
Read the chapter that is all about making NPCs later in the tutorial.

## TEMPLATE

Or, how to put great laggy quantities of items into one unlaggy
container.

You\'ve all seen it. Those shards out there that don\'t use TEMPLATEs.
When you kill, say, a dragon, on those shards, and go to loot him, you
find that rather than neatly organized containers, there are 100 potions
scattered about the loot window. Not only that, but all your magical
weapons are buried neatly beneath them!

How do we solve this problem? Well, SPHERE has given us the handy tool
of TEMPLATEs. These allow you to define a container item, AND the items
inside of it, AT THE SAME TIME. Isn\'t that neat? I thought so too, when
I first figured out what they were. Let\'s do our traditional
take-apart-the-script section. I\'ll place a nice TEMPLATE from the file
spheretemp_loot.scp.

`<font color="darkblue">`{=html}`[TEMPLATE 101505]`\
`DEFNAME=backpack_poor`\
`CATEGORY=Item Templates`\
`SUBSECTION=Loot Templates`\
`DESCRIPTION=Poor Backpack`\
`CONTAINER=i_backpack`\
`ITEM={ random_food 1 0 3 },{ 1 3 }`\
`ITEM={ random_bottle 1 0 8 }`\
`ITEM={ random_light 1 0 8 }`\
`ITEM={ random_male_tops 1 0 4 }`\
`COLOR=colors_all`\
`ITEM={ random_male_pants 1 0 4 }`\
`COLOR=colors_all`\
`ITEM=POOR_GOLD_PILE`\
`</font>`{=html}

Wow, that looks confusing. But don\'t worry, by the time we\'re done,
you\'ll know exactly what it means!

`<font color="darkblue">`{=html}\[TEMPLATE 101505\]`</font>`{=html}:
First of all, we look at the header for our template. An interesting
thing about templates is that the item name cannot be a DEFNAME like all
other scripts. It must be a ridiculously high number like 101505.
`<font color="darkblue">`{=html}DEFNAME=backpack_poor`</font>`{=html}:
Of course, SPHERE developers are not entirely evil, and have provided us
with the ability to give these scary numbers a DEFNAME for easier
access. You tell me, which would you rather type? \".add 101505\" or
\".add backpack_poor\"? I thought so.

**Note:** Since .56c, move DEFNAME to \[TEMPLATE \...\], e.g. \[TEMPLATE
backpack_poor\]

`<font color="darkblue">`{=html}CATEGORY, SUBSECTION,
DESCRIPTION`</font>`{=html}: Axis crap. Optional. See the previous
sections for a description of what these do.

`<font color="darkblue">`{=html}CONTAINER=i_backpack`</font>`{=html}:
Ahh, now we\'re getting down to the meat of this thing. This specifies
the holding container that all other items in this template will be in.
When you add the item in game, you will see this container. In this
case, it\'s a backpack. Simple enough. This can be any valid item with a
TYPE of t_container or t_container_locked.

`<font color="darkblue">`{=html}ITEM={ random_food 1 0 3},{1
3}`</font>`{=html} Well, that\'s certainly cryptic. I think we need to
break this line down even further.

But first, we\'re going to cover RANDOM SELECTORS! Sounds like fun
doesn\'t it? Nah, it doesn\'t sound fun to me either, but it\'s
absolutely necessary to a good shard.

Basically, they are an easy way to get different numbers with one
command. What fun would a shard be where you killed a dragon and got a
Platemail of Magic Stuff and a Super Duper Sword of Power every single
time? Everyone would be running around with them. What we need is some
variety!

There are two types of random selectors: weighted random and ranged
random. Weighted random makes a statement like this: \"Ok, 1 out of 10
times pick Number A, 3 out of 10 times pick Number B, and 6 out of 10
times pick number C\". Ranged random makes a statement like this: \"Pick
any number between the two numbers I give you\".

Our example actually has an example of both ranged random and weighted
random. We\'ll cover them in the order they appear:

{ random_food 1 0 3}

This is a weighted random selector. The way to interpret these is to
take the numbers that appear between the parentheses and divide them
into sets of two:

random_food 1\
0 3

Add up the second numbers in both sets, and we get 4. This tells SPHERE,
\"Ok, 1 out of four times, I want you to pick random_food, and 3 out of
four times, I want you to pick zero.\" You can even have random sets
within random sets, but then it just gets confusing.

{ { random_food 1 0 3} 1 random_clothing 1}

Can you figure it out?

random_clothing 1 { random_food 1 0 3} 1

2 is our magic number in this case. One out of two times, SPHERE will
pick random_clothing, and one out of two times, SPHERE will pick our
previous random selector, which will then select one of its own options.
If you\'re confused at this point, don\'t worry. This is extremely rare,
and we\'ll see in a moment how templates help us to solve this problem.

I did mention, though, that there is another type of random selector,
and you can probably see what it is:

{1 3}

NOTE: Spacing here is important. There must be ZERO spaces between the {
and the first number, or the } and the last number. It will behave
strangely otherwise.

This tells SPHERE \"Pick a number between 1 and 3, inclusive\".
Inclusive means that SPHERE can pick 1, 3, or any number in between. In
this case, the range is rather limited. SPHERE will give you a 1, 2 or 3
here. Ranged random selectors are actually more often used inside of
weighted random selectors.

{ {1 3} 3 {4 9} 1}

\"One out of four times, pick a number between 4 and 9. Three out of
four times, pick a number between 1 and 3.\"

And with that out of the way, we\'re going to analyze the actual line of
the script from above. The Piece What the Line does ITEM= This tells the
script \"Ok, we\'re going to add an item to this container. Anything
after the = tells the script exactly what it is we\'re adding and in
what amounts. You could easily say ITEM=i_platemail_chest, or something
like that, without the mysterious { } sections, but the reason templates
are interesting is because they can vary greatly.

`<font color="darkblue">`{=html}{ random_food 1 0 3}`</font>`{=html}

This is the item you will be creating. As we can see from our weighted
random selector lesson, 1 out of 4 times, it will be random_food, and 3
out of 4 times, it will be zero. If an ITEM is zero, nothing will be
created this time. Basically this is saying \"There will be a one in
four chance of getting random_food in this container.\" What is
random_food you ask? Well, it happens to be another TEMPLATE, defined in
spheretemplate.scp, I believe.

{1 3} This is the amount of the item that will be created. You should
recognize this as a ranged random selector. This tells SPHERE to put
between 1 and 3 of this item into the container. Of course, if the item
is zero as selected above, this has no effect since one nothing and
three nothings are still nothing.

So basically, that is a template script. You then fill it with as many
items as you want. You may also notice the following construction:

ITEM=i_sword_long,R11

This is a shorthand way of writing this:

ITEM={ i_sword_long 1 0 10 }

R11 means \"one out of 11 chance of finding this item\". And you can add
an amount selector to the end of that as well, which makes it look long
and scary:

ITEM=i_sword_long,R11,{4 5}

But why would you want 4 or 5 long swords in one item? That would be
bizzare. :)

And that\'s about it for templates. Congratulations, you\'re finished
with chapter 1. Now you should be able to understand the examples to
follow on the next section. You may also have some questions which are
addressed in the common questions area. If you have a question which is
not addressed there, perhaps it is too advanced of a topic for
chapter 1. I assure you almost every aspect of SPHERE scripting will be
covered in later chapters.

*(A template example by Belgar)*

`<font color="darkblue">`{=html}`[TEMPLATE tm_necromancer]`\
`CONTAINER=i_bag`\
`ITEM=random_necro_scroll`\
`ITEM=random_necro_scroll`\
`ITEM=random_necro_reagent, {5 12}`\
`ITEM=random_reagent, {5 12}`\
`ITEM=random_necro_reagent, {5 12}`\
`</font>`{=html}

## Examples

Or, um. Well I guess there really isn\'t another way to say
\"Examples\".

This shall be my attempt to create the most basic new items available.
You will see things in these examples that are NOT mentioned in the
tutorials. The major factor will be ON=@Create, which is the primary
topic of Chapter 2. Just know for now that things you can change in game
(color, etc) must go under ON=@Create.

**Example 1**: A Red Sword

`<tt>`{=html}`<font color="darkblue">`{=html}\[ITEMDEF i_sword_red\]\
ID=i_sword_viking\
TYPE=t_weapon_sword\
NAME=The Red Sword\
CATEGORY=Weapons\
SUBSECTION=New Swords\
DESCRIPTION=Red Sword\
ON=@Create

:   COLOR=colors_red // This is a comment. Comments are ignored by
    SPHERE.\
    `</font>`{=html}`</tt>`{=html}

Wait, what is this weird
`<font color="darkblue">`{=html}//`</font>`{=html} thing we\'ve got
going here? That\'s called a comment. It\'s completely ignored by
SPHERE, so you can write whatever you want to the end of the line after
//. You cannot have multi-line comments in SPHERE unless you use a new
//, so don\'t even try it. SPHERE will give funky errors and then
you\'ll have fun finding them.

**Example 2**: A blue ettin

`<font color="darkblue">`{=html}`[CHARDEF c_ettin_blue]`\
`ID=02 // You could just as easily use c_ettin here.`\
`NAME=My Blue Ettin`\
\
\
`ON=@Create`\
`:COLOR=02 // This is a dark blue color. It's often used for Counselor robes. Remember it.`\
`</font>`{=html}

**Example 3**: A template from the file, since I\'m too lazy to write
one myself

`<font color="darkblue">`{=html}`[TEMPLATE 101521]`\
`DEFNAME=goodie_meager_1`\
`CATEGORY=Item Templates`\
`SUBSECTION=Loot Templates`\
`DESCRIPTION=Meager Goodie 1`\
`ITEM={ meager_gold_pile 1 backpack_meager 1 pouch_meager 1 }`\
`ITEM={ random_boots 1 0 4 }`\
`ITEM={ random_gorget 1 0 4 }`\
`ITEM={ random_staff 1 0 4 }`\
`ITEM={ random_necklace 1 0 4 }`\
`ITEM={ i_cape 1 0 9 }`\
`<font color="darkred">`{=html}`COLOR=colors_all``</font>`{=html}\
`</font>`{=html}

You may notice something new here (especially since I highlighted it in
red), and yes, it is legal. Any lines between ITEM= lines will affect
the previously created item. The COLOR= line here affects the ITEM
created by the line

ITEM={ i_cape 1 0 9 }

Remember, the best way to learn this type of scripts is to read the
scripts provided for you in files like sphereitem_colorarm.scp and
sphereitem_beers.scp.

[Category:Tutorials](Category:Tutorials "wikilink")
