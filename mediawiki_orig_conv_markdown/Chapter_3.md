```{=mediawiki}
{{Languages|Chapter_3}}
```
## NPC Evolution {#npc_evolution}

Remember in Chapter 1 when we looked at that basic NPC script? It was a
generic script to create a naked man (or a naked player). And it looked
something like this:

`<font color="darkblue">`{=html}`[CHARDEF 0190]`\
`DEFNAME=c_man`\
`Name=Man`\
`ICON=i_pet_MAN`\
`CAN=MT_EQUIP|MT_WALK|MT_RUN|MT_USEHANDS`\
`RESOURCES=i_flesh_head, i_flesh_torso, i_flesh_right_arm, i_flesh_left_arm`\
`FOODTYPE=15 t_food, t_fruit`\
`DESIRES=i_gold,e_notoriety`\
`AVERSIONS=t_TRAP,t_eerie_stuff`\
`SHELTER=r_house`\
`BLOODCOLOR=0`\
\
`TSPEECH=spk_human_prime`\
`TSPEECH=spk_human_default`\
`TEVENTS=e_Human_HearUnk`\
`DESCRIPTION=Man`\
`SUBSECTION=Miscellaneous`\
`CATEGORY=Civilized`\
`</font>`{=html}

As you can see, this is a rather incomplete script. It\'s actually one
of the least complete of any of the scripts available in the
spherechar\_\*.scp files. Here is a more complete example of an NPC
script:

`<font color="darkblue">`{=html}`[CHARDEF 0490]`\
`DEFNAME=C_H_ALCHEMIST`\
`NAME=#NAMES_HUMANMALE the Alchemist`\
`ID=C_MAN`\
\
`DESIRES=i_gold,e_notoriety,t_magic`\
`AVERSIONS=t_TRAP,t_eerie_stuff`\
\
`TSPEECH=spk_human_prime`\
`TSPEECH=jobalchemist`\
`TSPEECH=spk_shopkeep`\
`TSPEECH=spk_needs`\
`TSPEECH=spk_rehello`\
`TSPEECH=spk_human_default`\
\
`TEVENTS=e_Human_HearUnk`\
`TEVENTS=e_Human_ConvInit`\
`TEVENTS=e_Human_Greet`\
`TEVENTS=e_Human_Space`\
`TEVENTS=e_Human_Needs`\
`TEVENTS=e_Human_Refuse`\
`TEVENTS=e_Human_Environ`\
\
`CATEGORY=Civilized`\
`SUBSECTION=Tradesmen`\
`DESCRIPTION=Alchemist (male)`\
\
`<font color="darkred">`{=html}`ON=@Create`\
`:NPC=brain_vendor`\
`:COLOR=colors_skin`\
`:STR={36 50}`\
`:DEX={36 50}`\
`:INT={51 65}`\
\
`:ALCHEMY={55.0 78.0}`\
`:TASTEID={55.0 78.0}`\
`:WRESTLING={15.0 38.0}`\
`:MAGICRESISTANCE={25.0 48.0}`\
`:TACTICS={15.0 38.0}`\
`:POISONING={35.0 55.0}`\
\
`:ITEMNEWBIE=random_male_hair`\
`:COLOR=colors_hair`\
`:ITEMNEWBIE=random_facial_hair`\
`:COLOR=match_hair``</font>`{=html}\
\
`ON=@NPCRestock`\
`:ITEM=i_expcoin,3`\
\
`:ITEM=i_shirt_plain`\
`:COLOR=colors_all`\
`:ITEM=random_pants`\
`:COLOR=colors_all`\
`:ITEM=i_robe`\
`:COLOR=colors_red`\
`:ITEM=random_shoes`\
`:COLOR=colors_neutral`\
`:ITEM=random_coin_purse`\
\
`:SELL=VENDOR_S_ALCHEMIST`\
`:BUY=VENDOR_B_ALCHEMIST`\
`</font>`{=html}

**\[CHARDEF 0490\]** We\'ve seen this before. It says \"Hey SPHERE!
Everything after this line until the next header is going to define a
character!\" What is this character going to be? Well, right now we have
no idea, it\'s just 0490 to SPHERE. The 0490 also shows the client what
anim to show (except for monsters with the ID field, which will show the
ID field anim). You can also use the char defname in the \[CHARDEF x\]
field instead of a number (which is better for new npcs), for example:
\[CHARDEF c_new_monster\]

**DEFNAME=C_H_ALCHEMIST** This is the
`<font color="darkgreen">`{=html}**defname**`</font>`{=html} for this
script, obviously. We\'ve seen things like this so many times, I don\'t
believe I need to go over it. But now at least we have a more memorable
name for this script. It\'s obviously a character (C), a human (H), and
an alchemist
(`<font color="yellow">`{=html}**C_H_ALCHEMIST**`</font>`{=html}). Try
to make your
`<font color="darkgreen">`{=html}**DEFNAMEs**`</font>`{=html} make sense
based on what the character is. Calling this c_robed_man would have
absolutely no memorable qualities. :)

**NAME=#NAMES_HUMANMALE the Alchemist** This is where SPHERE does some
funky stuff. First of all, if you remember from the
`<font color="darkblue">`{=html}SPHERE_NAME.SCP`</font>`{=html} lesson
in [Chapter 2](Chapter_2 "wikilink"), it is going to replace
#NAMES_HUMANMALE with an actual name for this NPC, such as \"Fritz\",
\"Bob\" or the ever popular \"Roderick\". The second thing it is going
to do is divide this name into a
`<font color="darkblue">`{=html}NAME`</font>`{=html} and a
`<font color="darkblue">`{=html}TITLE`</font>`{=html}. Where does it do
this division? At the word \"the\". So writing this line is equivalent
to:

*`NAME=#NAMES_HUMANMALE`*\
*`TITLE=the Alchemist`*\

**ID=C_MAN** Here is where we actually tell SPHERE what this thing is.
What is C_MAN? It\'s a **DEFNAME** obviously, but for what? Look up
toward the top of this file, and you\'ll see the definition of the
*C_MAN* character.

And so on. As you can see, we\'re just duplicating what we\'ve written
in the previous section. But with the newer versions of SPHERE we don\'t
need to do that. Our character 0490 automatically gets everything that
comes default on a C_MAN, including abilities, icons, and sounds, UNLESS
WE SAY OTHERWISE. In programming, this is called inheritance. The new,
more specific character inherits the properties of the less specific
one.

You\'ll notice that we respecify
`<font color="darkgreen">`{=html}DESIRES`</font>`{=html} and
`<font color="darkgreen">`{=html}AVERSIONS`</font>`{=html}. Why do we do
this if `<font color="yellow">`{=html}**C_MAN**`</font>`{=html} has
already told us what this type of character wants and doesn\'t want?
Well I\'m not sure in the case of AVERSIONS, because, well, they\'re the
same. But the DESIRES of an alchemist are different than the DESIRES of
a generic man, so we tell SPHERE, \"Hey, replace the
`<font color="yellow">`{=html}**C_MAN**`</font>`{=html} desires with our
new ones!\"

**TSPEECH=** What do you suppose those cryptic names are following this
statement? Of course, they\'re DEFNAMEs, but for what? If you look
through your files, chances are you won\'t find those defined anywhere..
But what\'s this? We have a folder called speech that comes
preconstructed in the zip file. Looking through those files reveals a
wealth of
`<font color="darkgreen">`{=html}**\[SPEECH\]**`</font>`{=html} block
definitions. The default ones can be found at the SPEECH folder on your
scripts folder.

We\'ll look at a very simple speech script right now. I am not taking
this from any file.

`<font color="darkblue">`{=html}*`[SPEECH spk_human_test]`*\
*`ON=*hello*`*\
*`SAY Cheese!`*\
`</font>`{=html}

In our script, if we were to write
`<font color="darkred">`{=html}**TSPEECH=spk_human_test**`</font>`{=html},
our NPC would respond with \"Cheese!\" any time we said \"hello\" to
him. You might be wondering why I have surrounded this word with stars
**(\*)**. In programming lingo, a star means *\"ANYTHING\"*. So you
could say \"I want to eat you hello goodbye\" and the NPC would still
respond with \"Cheese!\", because the word \"hello\" was present.

Of course, SPEECH is much more complicated than that and we\'ll look at
it again when we reach the chapter on basic event scripting. Just know
for now that you can have as many TSPEECH lines as you wish in a CHARDEF
section.

**TEVENTS=** We\'ve already covered this in a very very tiny amount of
detail in Chapter 1. This is where events for the creature are defined.
As you can see, this creature contains a great deal of events. They
define everything from what he says when he hears an unknown word
(\"Huh?\"), to what he does when he sees a new player. We\'ll look at an
event script in Chapter 8. You should learn the basics of item scripting
before you try NPC event scripting. For now just know that you can
retrieve all the TEVENTS of a npc by using \<\[REF\].TEVENTS\>.

**ON=@Create** Actually, I lied. \@Create is an event, and we\'re going
to talk about it right now. But it\'s a special event, as is the next
one we\'re going to discuss. Basically, \@Create causes every line after
it to be processed (the entire section highlighted in red) when an
object is Created. Creative eh? (Ha, ha.) In this case, I\'m not going
to concentrate on most of the lines following, as they should all make
sense to you now. All you need to know at this point about \@Create is
that things you can change IN GAME go under this section. This includes
stats, skills, unlootable items, colors, brain types, and TAGs (Although
tags can be defined on CHARDEF too, it\'s a great way to set a tag to
all npcs with that chardef without needing to do a restock or change one
by one) (You don\'t know what a TAG is? Good, I haven\'t taught you
yet.).

**ALCHEMY={55.0 77.0}** This line is very deceiving, and the reason for
the deception is the way that SPHERE processes numbers. SPHERE cannot,
ever, read a decimal number. 55.0 means nothing to SPHERE, and it simply
strips out the decimal point. Now, isn\'t it convenient that internally,
skills are stored as big numbers? Look at your skills menu in-game right
now. Find a skill that isn\'t zero, obviously, and look at the value.

It looks like this: 42.0

Now, in-game again, type this command: .set \[skillname\] 42 (Of course,
replacing \[skillname\] with the skill of your choice. Refer to
spheretables.scp if the name you\'re typing doesn\'t work.) What
happened? Your skill suddenly went to 4.2!! Is this an error in the
game? No, actually it\'s because skills are stored by removing the
decimal point. If you have 100.0 in blacksmithing, your skill is
actually set to 1000. If you have 75.2 in a skill, that skill is 752.

This may seem like a simple concept, but it also applies to the REST of
scripting as well. Any time you type a number like 55.0, SPHERE
eliminates the decimal. So our example line above is actually this:

`ALCHEMY={550 770}`

Isn\'t that sneaky?

One of the times you might want to remember this is later, if you are
multiplying numbers:

4 \* 0.5

Sphere translates this as \"4 times 5\" and you get 20, rather than the
2 you were expecting. As you can see, this may cause serious problems.
I\'ll show in later chapters how to get around this problem. I just
wanted to point out here that it exists. (Look back at the resource
tables in sphereregion.scp for another example of where sneaky decimal
points are used.)

**NPC=brain_vendor** Ok, so I\'m out of order. Deal with it.

All NPCs in the game are controlled by specific intelligences, which
direct the way they act in certain situations. For instance, this
alchemist is a brain_vendor, which means he responds to commands like
\"buy\" and \"sell\" by opening up a trade window. It also means that he
is allowed to have extra storage space for information dealing with the
items he can buy and sell. (Actually they are additional containers
stored on the vendor, but we shall see that later.) Here is a list of
the other intelligences available (I bet you can\'t guess which file I
pulled this from):

`<font color="darkblue">`{=html}`[DEFNAME brains]`\
`BRAIN_NONE 0 // Players: No brain. Convenient eh? :)`\
`BRAIN_ANIMAL 1 // Animals: wander, attack only if attacked`\
`BRAIN_HUMAN 2 // Human: wander and speak`\
`BRAIN_HEALER 3 // Healer: heal ghosts in proximity`\
`BRAIN_GUARD 4 // Guard: attack bad guys I see`\
`BRAIN_BANKER 5 // Banker: you can access your bank through him`\
`BRAIN_VENDOR 6 // Vendor: buys and sells things`\
`BRAIN_BEGGAR 7 // Beggar: follows players around asking irritating questions`\
`BRAIN_ANIMAL_TRAINER 8 // Trainer: can stable animals`\
`BRAIN_THIEF 9 // Thief: no effect right now`\
`BRAIN_MONSTER 10 // Evil: attack all players we see`\
`BRAIN_BERSERK 11 // Crazy: attack anything we see`\
`BRAIN_UNDEAD 12 // Undead: same as evil, just used for identification`\
`BRAIN_DRAGON 13 // Dragon: breathes fire (set this on a rabbit)`\
`BRAIN_VENDOR_OFFDUTY 14 // No idea what the difference is here`\
`BRAIN_TOWNCRIER 2 // Same number as brain_human, same effect`\
`brain_beserk brain_berserk //Same thing as brain_berserk, just to avoid some errors by typos`\
`</font>`{=html}

**ITEMNEWBIE=** This creates the specified item with the attr_newbie on
the char.

**ON=@NPCRestock** I lied twice! This is the SECOND event you\'re going
to learn in this script. This event is triggered when a \"restock\"
happens in-game. This occurs once every few real-time hours, or if a
staff member types
\"`<font color="darkred">`{=html}.sector.restock`</font>`{=html}\". What
you should put here is anything lootable from this NPC, along with the
definitions of things they buy and sell. Once again, this is just a
template in most cases, so you should know how to deal with it. I\'m
going to examine two lines though:

**SELL=VENDOR_S_ALCHEMIST**\
**BUY=VENDOR_B_ALCHEMIST**

This defines what the vendor buys and sells? But where are these
mysterious lists of items coming from? Actually, they\'re templates, in
the file
`<font color="darkblue">`{=html}spheretemp_vend.scp`</font>`{=html}.
(Templates for vendors. Those developers are so creative.) Actually
it\'s a good thing to name files after what\'s inside of them. :)

Price is not defined anywhere on these BUY and SELL lines. Price is
defined in a VALUE= line in an individual item script. If an item script
does not have a VALUE= line, price is determined by multiplying the
value of the resources in that item by the number of resources required.
For example, if an item takes 8 iron ingots to make, and each ingot has
a VALUE of 8 gold pieces, the entire item is going to be worth 64 gold.
By default, things sell for half of the price you can buy them for.

I think that\'s all you need to know for now about scripting a new NPC.
Right now, with your abilities, you can create new vendors, new
monsters, and new animals that wander your world. But they don\'t do
anything unique yet. They just behave like stronger or weaker versions
of the same monsters. And they\'re probably pretty colors, too, judging
from the recent use of my hues.mul file for colors 077a and 07a1. (I
really should release a DEFNAME script for those.)

Now that you know how to make a decent NPC, let\'s explore ways to make
unique items to put on him as loot. In the next section, we\'re going to
make a SUPER DUPER BOW OF FIRE AND BRIMSTONE! \*trumpet fanfare\*

## Advanced Item Scripting {#advanced_item_scripting}

The Super Duper Wand of Fire and Brimstone!

`<font color="darkblue">`{=html}`[ITEMDEF i_wand_sdwfb]`\
`NAME=Super Duper Wand of Fire and Brimstone`\
`ID=i_wand_1`\
`TYPE=t_wand`\
`RESOURCES=i_wand,10 i_scroll_flamestrike`\
\
`ON=@Create`\
`:ATTR=attr_magic`\
`:MOREX=s_flamestrike`\
`:MOREY=50.0`\
`:MORE2=10`\
`</font>`{=html}

I tricked you that time! We STARTED with the script. No funny
introductions. No livening up the article. Just a script. And a very
interesting script it is too. You won\'t find it in any of your files.
(In case you\'re wondering, SDBFB stands for \"Super Duper Wand of Fire
and Brimstone\").

Now, what does this thing do? Well it\'s one of those handy predefined
types that makes it do what it\'s supposed to do. Actually, it\'s not
the only thing here that makes it do what it\'s supposed to do, but
we\'ll see that in a moment!

**\[ITEMDEF i_wand_sdwfb\]** You should be able to tell me what this
does by now. We\'re making a new item with DEFNAME i_wand_sdwfb.

Notice that we don\'t explicitly declare the DEFNAME, but put it in the
ITEMDEF. It\'s the same thing.

**NAME=**

Duh. :)

**ID=i_wand_1**

Once again, we\'re inheriting some properties here, including animation,
skill type (macefighting oddly enough), etc from the definition of
i_wand_1.

**TYPE=t_wand**

Remember in our NPC script, I said that the different brain types caused
the NPCs to act different ways in certain situations. Well, in items,
TYPE does the same thing. Only there are more of them. A lot more. Here
are the specifications of the \"t_wand\" type. As you can see, we use
all of them in the \@Create section. Note: this line wouldn\'t be
necessary since we\'re getting type=t_wand from the itemdef i_wand_1
too.

**MOREX** = the spell this wand will cast **MOREY** = the skill with
which the spell will be cast **MORE2** = the number of charges this wand
has left

Every item does something different with the MOREs. Actually this is a
good time to go through the variables available to you on an item. In a
simple list:

-   MORE1 (or MORE)
-   MORE2
-   MOREP
-   COLOR
-   TYPE
-   CREATE
-   LAYER
-   ATTR
-   LINK
-   CONT
-   TOPOBJ
-   LINK

As we\'ll see, a few of these have special functions that will allow us
to do a lot more. But that doesn\'t come until advanced scripting. And
there are also a lot more things which you\'ll know in future chapters.

One of these properties (MOREP) has the weirdness that it can hold a
coordinate of the form (x, y, z, m). Which means that it can be broken
down into MOREX, MOREY, MOREZ, and MOREM. For example, if you write this
line:

`<font color="darkblue">`{=html}`MOREP=1,2,3,4`\
`</font>`{=html}

It is exactly the same as writing:

`<font color="darkblue">`{=html}`MOREX=1`\
`MOREY=2`\
`MOREZ=3`\
`MOREM=4`\
`</font>`{=html}

This is what you call in C++ programming a \"union\", basically meaning
there are going to be restrictions on the amount of data you can store
in each of these variables. MOREX and MOREY can both hold numbers up to
0FFFF. MOREZ can hold numbers from -128 to 127, and is always displayed
in decimal. MOREM can hold numbers from 0 to 255, and is also always
displayed in decimal.

Be sure that when you\'re writing a script, or an item, you don\'t use
both MOREP and one of the other MOREP pieces (MOREX, etc). It won\'t
work together, since one will overwrite the other.

`<font color="darkblue">`{=html}`MOREP=10,42,51,53`\
`MOREX=78`\
`MOREY=89`\
`MOREM=56`\
`</font>`{=html}

MOREP now is equal to 78,89,51,56.

So you see, it doesn\'t work to use these together.

Another strangeness of SPHERE is that they have given us the properties
MORE1L, MORE1H, MORE2L, and MORE2H. These are not entirely visible to
you, but just know that they are pieces of the MORE1 and MORE2
properties. As such, you should not be using both MORE1 and either of
the MORE1 properties, or the same for the MORE2 properties, on a single
item.

`<font color="darkblue">`{=html}`MORE1=0FFFFFFFF`\
`MORE1L=01234`\
`MORE1H=0F0`\
`</font>`{=html}

Now MORE1 is 000F01234. Which would totally screw up any script you were
writing involving the MORE1 property. So don\'t use both in the same
script. (If you don\'t understand where that number came from, don\'t
worry about it. I\'ve never used MORE1L and MORE1H in a script, and
chances are neither will you.)

We\'ll also see later how to use the ATTR property to give your item
special properties (like being unmovable, or magical, or blessed). I\'ll
put that in my massive chart that\'s going in the next section, which
lists all the TYPEs and all of the ATTR values.

From what I\'ve just explained to you, the rest of the item script,
after the \@Create event, should be obvious. We\'re setting the pieces
of MOREP to be what we need them to be so our wand functions properly.
And if you create this item in the game, and double-click it, you\'ll
get a target to cast Flamestrike. That\'s all you need to do.

By the way, you could just as easily have written:

`<font color="darkblue">`{=html}`MOREP=s_flamestrike,50.0`\
`MORE2L=10`\
`</font>`{=html}

Think about it. :)

(Anyone know why the developers decided to have 10 variables named MORE?
Standing for \"MORE information about an item\" perhaps?)

**Understanding the \@Create trigger**

You\'re probably wandering why I didn\'t set the item properties (such
as the mores) directly on the itemdef, that\'s because not everything
can be set there, only general properties for the items with that id.

\"But hey, I can set different names for an item with the same id\"

Yes you can, but mostly you won\'t, another thing that can be set there
but you can also change are TAGs (you\'ll see more on other chapters).

Things that you can\'t change for example are WEIGHT, VALUE, RESOURCES
and of course the DEFNAME. There are more, but just to make you get the
idea.

## TYPEs

This section explains how you can use [built-in item
types](TYPEDEF "wikilink"), how to override the built-in types, and how
you can make your own.

If you want to override a built-in typedef, that is indeed possible,
just define its new behavior it in a script and since the scripts are
loaded after the server starts, your new definition will take
precedence.

A TYPEDEF is essentially a collection of triggers, and can be written to
reference other aspects of the ITEMDEF, CHARDEF, or REGION that it is
assigned to. To assign a TYPEDEF to an item, you can simply set
TYPE=t_mytype in the ITEMDEF (Note: An item can only have one TYPE.)

Here is an example TYPEDEF:

`[TYPEDEF t_horseshoes]`\
`ON=@DClick`\
`   TARGET What animal needs this item?`\
`   RETURN 1`\
`ON=@Targon_Char`\
`   IF (<SRC.TARG.DEX> > 100)`\
`      SRC.SYSMESSAGE @032 That animal does not need this item.`\
`      RETURN 1`\
`   ENDIF`\
`   IF (<SRC.TARG.OBODY>==(c_horse_pack|c_llama_pack|c_horse_gray|c_horse_brown_dk|c_horse_brown_lt|c_llama))`\
`      SRC.SYSMESSAGE @032 Now the animal is faster.`\
`      SRC.TARG.MODDEX += ``<MORE1>`{=html}\
`      SRC.EFFECT=3,0374a,6,15,1`\
`      REMOVE`\
`   ELSE`\
`      SRC.SYSMESSAGE @032 That animal can not wear this item.`\
`   ENDIF`\
`   RETURN 1`

Here is an example item that uses the t_horseshoes TYPEDEF shown above:

`[ITEMDEF i_horse_shoes_magic]`\
`ID=0fb6`\
`NAME=magic horseshoes`\
`TYPE=t_horseshoes`\
`VALUE=35`\
`WEIGHT=8.0`\
`RESOURCES=8 i_ingot_iron`\
`SKILLMAKE=Blacksmithing 30.0`\
`CATEGORY=Items by Professions`\
`SUBSECTION=Blacksmiths`\
`DESCRIPTION=Magic Horse Shoes`\
`ON=@Create`\
`   MORE1={10 15}`\
`   ATTR=attr_magic`

## ATTRs

This is a list of the ATTR flags available and what they do. I pulled it
right out of
`<font color="darkblue">`{=html}spheredefs.scp`</font>`{=html}

+---+---+---+
| V | D | D |
| a | E | e |
| l | F | s |
| u | N | c |
| e | A | r |
|   | M | i |
|   | E | p |
|   |   | t |
|   |   | i |
|   |   | o |
|   |   | n |
+===+===+===+
| 0 | a | S |
| 1 | t | o |
|   | t | m |
|   | r | e |
|   | _ | o |
|   | i | n |
|   | d | e |
|   | e | h |
|   | n | a |
|   | t | s |
|   | i | u |
|   | f | s |
|   | i | e |
|   | e | d |
|   | d | t |
|   |   | h |
|   |   | e |
|   |   | I |
|   |   | t |
|   |   | e |
|   |   | m |
|   |   | I |
|   |   | D |
|   |   | s |
|   |   | k |
|   |   | i |
|   |   | l |
|   |   | l |
|   |   | o |
|   |   | n |
|   |   | t |
|   |   | h |
|   |   | i |
|   |   | s |
|   |   | i |
|   |   | t |
|   |   | e |
|   |   | m |
|   |   | s |
|   |   | o |
|   |   | i |
|   |   | t |
|   |   | w |
|   |   | i |
|   |   | l |
|   |   | l |
|   |   | d |
|   |   | i |
|   |   | s |
|   |   | p |
|   |   | l |
|   |   | a |
|   |   | y |
|   |   | t |
|   |   | h |
|   |   | e |
|   |   | f |
|   |   | u |
|   |   | l |
|   |   | l |
|   |   | m |
|   |   | a |
|   |   | g |
|   |   | i |
|   |   | c |
|   |   | n |
|   |   | a |
|   |   | m |
|   |   | e |
|   |   | \ |
|   |   | " |
|   |   | + |
|   |   | 7 |
|   |   | S |
|   |   | w |
|   |   | o |
|   |   | r |
|   |   | d |
|   |   | o |
|   |   | f |
|   |   | R |
|   |   | u |
|   |   | i |
|   |   | n |
|   |   | o |
|   |   | f |
|   |   | F |
|   |   | l |
|   |   | a |
|   |   | m |
|   |   | e |
|   |   | s |
|   |   | t |
|   |   | r |
|   |   | i |
|   |   | k |
|   |   | e |
|   |   | \ |
|   |   | " |
|   |   | . |
+---+---+---+
| 0 | a | T |
| 2 | t | h |
|   | t | e |
|   | r | i |
|   | _ | t |
|   | d | e |
|   | e | m |
|   | c | w |
|   | a | i |
|   | y | l |
|   |   | l |
|   |   | d |
|   |   | e |
|   |   | c |
|   |   | a |
|   |   | y |
|   |   | w |
|   |   | h |
|   |   | e |
|   |   | n |
|   |   | t |
|   |   | h |
|   |   | e |
|   |   | i |
|   |   | n |
|   |   | t |
|   |   | e |
|   |   | r |
|   |   | n |
|   |   | a |
|   |   | l |
|   |   | d |
|   |   | e |
|   |   | c |
|   |   | a |
|   |   | y |
|   |   | t |
|   |   | i |
|   |   | m |
|   |   | e |
|   |   | r |
|   |   | , |
|   |   | o |
|   |   | r |
|   |   | t |
|   |   | h |
|   |   | e |
|   |   | i |
|   |   | t |
|   |   | e |
|   |   | m |
|   |   | \ |
|   |   | ' |
|   |   | s |
|   |   | T |
|   |   | I |
|   |   | M |
|   |   | E |
|   |   | R |
|   |   | r |
|   |   | e |
|   |   | a |
|   |   | c |
|   |   | h |
|   |   | e |
|   |   | s |
|   |   | z |
|   |   | e |
|   |   | r |
|   |   | o |
|   |   | . |
+---+---+---+
| 0 | a | T |
| 4 | t | h |
|   | t | e |
|   | r | i |
|   | _ | t |
|   | n | e |
|   | e | m |
|   | w | w |
|   | b | i |
|   | i | l |
|   | e | l |
|   |   | n |
|   |   | o |
|   |   | t |
|   |   | b |
|   |   | e |
|   |   | p |
|   |   | l |
|   |   | a |
|   |   | c |
|   |   | e |
|   |   | d |
|   |   | i |
|   |   | n |
|   |   | a |
|   |   | c |
|   |   | o |
|   |   | r |
|   |   | p |
|   |   | s |
|   |   | e |
|   |   | u |
|   |   | p |
|   |   | o |
|   |   | n |
|   |   | d |
|   |   | e |
|   |   | a |
|   |   | t |
|   |   | h |
|   |   | . |
+---+---+---+
| 0 | a | A |
| 8 | t | n |
|   | t | y |
|   | r | o |
|   | _ | n |
|   | m | e |
|   | o | c |
|   | v | a |
|   | e | n |
|   | _ | p |
|   | a | i |
|   | l | c |
|   | w | k |
|   | a | t |
|   | y | h |
|   | s | i |
|   |   | s |
|   |   | u |
|   |   | p |
|   |   | , |
|   |   | e |
|   |   | v |
|   |   | e |
|   |   | n |
|   |   | i |
|   |   | f |
|   |   | t |
|   |   | h |
|   |   | e |
|   |   | y |
|   |   | s |
|   |   | h |
|   |   | o |
|   |   | u |
|   |   | l |
|   |   | d |
|   |   | n |
|   |   | \ |
|   |   | ' |
|   |   | t |
|   |   | b |
|   |   | e |
|   |   | a |
|   |   | b |
|   |   | l |
|   |   | e |
|   |   | t |
|   |   | o |
|   |   | n |
|   |   | o |
|   |   | r |
|   |   | m |
|   |   | a |
|   |   | l |
|   |   | l |
|   |   | y |
|   |   | . |
|   |   | T |
|   |   | h |
|   |   | e |
|   |   | i |
|   |   | t |
|   |   | e |
|   |   | m |
|   |   | w |
|   |   | i |
|   |   | l |
|   |   | l |
|   |   | n |
|   |   | o |
|   |   | t |
|   |   | d |
|   |   | e |
|   |   | c |
|   |   | a |
|   |   | y |
|   |   | u |
|   |   | n |
|   |   | l |
|   |   | e |
|   |   | s |
|   |   | s |
|   |   | t |
|   |   | h |
|   |   | e |
|   |   | d |
|   |   | e |
|   |   | c |
|   |   | a |
|   |   | y |
|   |   | f |
|   |   | l |
|   |   | a |
|   |   | g |
|   |   | i |
|   |   | s |
|   |   | a |
|   |   | l |
|   |   | s |
|   |   | o |
|   |   | s |
|   |   | e |
|   |   | t |
|   |   | . |
+---+---+---+
| 0 | a | L |
| 1 | t | o |
| 0 | t | c |
|   | r | k |
|   | _ | e |
|   | m | d |
|   | o | d |
|   | v | o |
|   | e | w |
|   | _ | n |
|   | n | . |
|   | e | P |
|   | v | r |
|   | e | o |
|   | r | b |
|   |   | a |
|   |   | b |
|   |   | l |
|   |   | y |
|   |   | t |
|   |   | h |
|   |   | e |
|   |   | o |
|   |   | n |
|   |   | e |
|   |   | y |
|   |   | o |
|   |   | u |
|   |   | \ |
|   |   | ' |
|   |   | l |
|   |   | l |
|   |   | u |
|   |   | s |
|   |   | e |
|   |   | m |
|   |   | o |
|   |   | s |
|   |   | t |
|   |   | o |
|   |   | f |
|   |   | t |
|   |   | e |
|   |   | n |
|   |   | . |
|   |   | I |
|   |   | t |
|   |   | w |
|   |   | i |
|   |   | l |
|   |   | l |
|   |   | n |
|   |   | e |
|   |   | v |
|   |   | e |
|   |   | r |
|   |   | d |
|   |   | e |
|   |   | c |
|   |   | a |
|   |   | y |
|   |   | , |
|   |   | e |
|   |   | v |
|   |   | e |
|   |   | n |
|   |   | i |
|   |   | f |
|   |   | t |
|   |   | h |
|   |   | e |
|   |   | d |
|   |   | e |
|   |   | c |
|   |   | a |
|   |   | y |
|   |   | f |
|   |   | l |
|   |   | a |
|   |   | g |
|   |   | i |
|   |   | s |
|   |   | s |
|   |   | e |
|   |   | t |
|   |   | . |
+---+---+---+
| 0 | a | T |
| 2 | t | h |
| 0 | t | i |
|   | r | s |
|   | _ | i |
|   | m | t |
|   | a | e |
|   | g | m |
|   | i | h |
|   | c | a |
|   |   | s |
|   |   | b |
|   |   | e |
|   |   | e |
|   |   | n |
|   |   | e |
|   |   | n |
|   |   | c |
|   |   | h |
|   |   | a |
|   |   | n |
|   |   | t |
|   |   | e |
|   |   | d |
+---+---+---+
| 0 | a | T |
| 4 | t | h |
| 0 | t | i |
|   | r | s |
|   | _ | i |
|   | o | s |
|   | w | o |
|   | n | w |
|   | e | n |
|   | d | e |
|   |   | d |
|   |   | b |
|   |   | y |
|   |   | t |
|   |   | h |
|   |   | e |
|   |   | t |
|   |   | o |
|   |   | w |
|   |   | n |
|   |   | , |
|   |   | a |
|   |   | n |
|   |   | d |
|   |   | t |
|   |   | r |
|   |   | y |
|   |   | i |
|   |   | n |
|   |   | g |
|   |   | t |
|   |   | o |
|   |   | p |
|   |   | i |
|   |   | c |
|   |   | k |
|   |   | i |
|   |   | t |
|   |   | u |
|   |   | p |
|   |   | w |
|   |   | i |
|   |   | l |
|   |   | l |
|   |   | c |
|   |   | o |
|   |   | u |
|   |   | n |
|   |   | t |
|   |   | a |
|   |   | s |
|   |   | s |
|   |   | t |
|   |   | e |
|   |   | a |
|   |   | l |
|   |   | i |
|   |   | n |
|   |   | g |
|   |   | . |
|   |   | Y |
|   |   | o |
|   |   | u |
|   |   | w |
|   |   | i |
|   |   | l |
|   |   | l |
|   |   | b |
|   |   | e |
|   |   | f |
|   |   | l |
|   |   | a |
|   |   | g |
|   |   | g |
|   |   | e |
|   |   | d |
|   |   | c |
|   |   | r |
|   |   | i |
|   |   | m |
|   |   | i |
|   |   | n |
|   |   | a |
|   |   | l |
|   |   | i |
|   |   | f |
|   |   | y |
|   |   | o |
|   |   | u |
|   |   | t |
|   |   | r |
|   |   | y |
|   |   | t |
|   |   | o |
|   |   | u |
|   |   | s |
|   |   | e |
|   |   | t |
|   |   | h |
|   |   | e |
|   |   | S |
|   |   | t |
|   |   | e |
|   |   | a |
|   |   | l |
|   |   | i |
|   |   | n |
|   |   | g |
|   |   | s |
|   |   | k |
|   |   | i |
|   |   | l |
|   |   | l |
|   |   | o |
|   |   | n |
|   |   | t |
|   |   | h |
|   |   | i |
|   |   | s |
|   |   | i |
|   |   | t |
|   |   | e |
|   |   | m |
|   |   | . |
|   |   | I |
|   |   | t |
|   |   | w |
|   |   | i |
|   |   | l |
|   |   | l |
|   |   | n |
|   |   | e |
|   |   | v |
|   |   | e |
|   |   | r |
|   |   | d |
|   |   | e |
|   |   | c |
|   |   | a |
|   |   | y |
|   |   | . |
+---+---+---+
| 0 | a | I |
| 8 | t | n |
| 0 | t | v |
|   | r | i |
|   | _ | s |
|   | i | i |
|   | n | b |
|   | v | l |
|   | i | e |
|   | s | t |
|   |   | o |
|   |   | n |
|   |   | o |
|   |   | n |
|   |   | - |
|   |   | G |
|   |   | M |
|   |   | c |
|   |   | l |
|   |   | i |
|   |   | e |
|   |   | n |
|   |   | t |
|   |   | s |
+---+---+---+
| 0 | a | C |
| 1 | t | u |
| 0 | t | r |
| 0 | r | s |
|   | _ | e |
|   | c | d |
|   | u | i |
|   | r | t |
|   | s | e |
|   | e | m |
|   | d | , |
|   |   | c |
|   |   | a |
|   |   | s |
|   |   | t |
|   |   | s |
|   |   | c |
|   |   | u |
|   |   | r |
|   |   | s |
|   |   | e |
|   |   | o |
|   |   | n |
|   |   | t |
|   |   | h |
|   |   | e |
|   |   | w |
|   |   | e |
|   |   | a |
|   |   | r |
|   |   | e |
|   |   | r |
|   |   | w |
|   |   | h |
|   |   | i |
|   |   | l |
|   |   | e |
|   |   | i |
|   |   | t |
|   |   | \ |
|   |   | ' |
|   |   | s |
|   |   | e |
|   |   | q |
|   |   | u |
|   |   | i |
|   |   | p |
|   |   | p |
|   |   | e |
|   |   | d |
+---+---+---+
| 0 | a | I |
| 2 | t | h |
| 0 | t | a |
| 0 | r | v |
|   | _ | e |
|   | c | n |
|   | u | o |
|   | r | i |
|   | s | d |
|   | e | e |
|   | d | a |
|   | 2 | w |
|   |   | h |
|   |   | a |
|   |   | t |
|   |   | t |
|   |   | h |
|   |   | e |
|   |   | d |
|   |   | i |
|   |   | f |
|   |   | f |
|   |   | e |
|   |   | r |
|   |   | e |
|   |   | n |
|   |   | c |
|   |   | e |
|   |   | i |
|   |   | s |
|   |   | . |
|   |   | . |
|   |   | s |
|   |   | t |
|   |   | r |
|   |   | e |
|   |   | n |
|   |   | g |
|   |   | t |
|   |   | h |
|   |   | m |
|   |   | a |
|   |   | y |
|   |   | b |
|   |   | e |
|   |   | ? |
+---+---+---+
| 0 | a | C |
| 4 | t | a |
| 0 | t | s |
| 0 | r | t |
|   | _ | s |
|   | b | b |
|   | l | l |
|   | e | e |
|   | s | s |
|   | s | s |
|   | e | o |
|   | d | n |
|   |   | t |
|   |   | h |
|   |   | e |
|   |   | p |
|   |   | e |
|   |   | r |
|   |   | s |
|   |   | o |
|   |   | n |
|   |   | w |
|   |   | h |
|   |   | o |
|   |   | i |
|   |   | s |
|   |   | e |
|   |   | q |
|   |   | u |
|   |   | i |
|   |   | p |
|   |   | p |
|   |   | i |
|   |   | n |
|   |   | g |
|   |   | i |
|   |   | t |
|   |   | ( |
|   |   | s |
|   |   | t |
|   |   | a |
|   |   | t |
|   |   | g |
|   |   | a |
|   |   | i |
|   |   | n |
|   |   | ) |
+---+---+---+
| 0 | a | ? |
| 8 | t |   |
| 0 | t |   |
| 0 | r |   |
|   | _ |   |
|   | b |   |
|   | l |   |
|   | e |   |
|   | s |   |
|   | s |   |
|   | e |   |
|   | d |   |
|   | 2 |   |
+---+---+---+
| 0 | a | I |
| 1 | t | n |
| 0 | t | a |
| 0 | r | v |
| 0 | _ | e |
|   | f | n |
|   | o | d |
|   | r | o |
|   | s | r |
|   | a | \ |
|   | l | ' |
|   | e | s |
|   |   | s |
|   |   | e |
|   |   | l |
|   |   | l |
|   |   | - |
|   |   | b |
|   |   | o |
|   |   | x |
|   |   | o |
|   |   | r |
|   |   | b |
|   |   | u |
|   |   | y |
|   |   | - |
|   |   | b |
|   |   | o |
|   |   | x |
|   |   | . |
+---+---+---+
| 0 | a | T |
| 2 | t | h |
| 0 | t | i |
| 0 | r | s |
| 0 | _ | i |
|   | s | t |
|   | t | e |
|   | o | m |
|   | l | h |
|   | e | a |
|   | n | s |
|   |   | b |
|   |   | e |
|   |   | e |
|   |   | n |
|   |   | s |
|   |   | t |
|   |   | o |
|   |   | l |
|   |   | e |
|   |   | n |
|   |   | ( |
|   |   | f |
|   |   | r |
|   |   | o |
|   |   | m |
|   |   | t |
|   |   | h |
|   |   | e |
|   |   | t |
|   |   | o |
|   |   | w |
|   |   | n |
|   |   | p |
|   |   | r |
|   |   | o |
|   |   | b |
|   |   | a |
|   |   | b |
|   |   | l |
|   |   | y |
|   |   | ) |
+---+---+---+
| 0 | a | I |
| 4 | t | t |
| 0 | t | h |
| 0 | r | i |
| 0 | _ | n |
|   | c | k |
|   | a | t |
|   | n | h |
|   | _ | i |
|   | d | s |
|   | e | i |
|   | c | s |
|   | a | u |
|   | y | s |
|   |   | e |
|   |   | d |
|   |   | t |
|   |   | o |
|   |   | g |
|   |   | e |
|   |   | t |
|   |   | r |
|   |   | i |
|   |   | d |
|   |   | o |
|   |   | f |
|   |   | t |
|   |   | h |
|   |   | o |
|   |   | s |
|   |   | e |
|   |   | i |
|   |   | r |
|   |   | r |
|   |   | i |
|   |   | t |
|   |   | a |
|   |   | t |
|   |   | i |
|   |   | n |
|   |   | g |
|   |   | e |
|   |   | r |
|   |   | r |
|   |   | o |
|   |   | r |
|   |   | s |
|   |   | \ |
|   |   | " |
|   |   | T |
|   |   | I |
|   |   | M |
|   |   | E |
|   |   | R |
|   |   | h |
|   |   | a |
|   |   | s |
|   |   | e |
|   |   | x |
|   |   | p |
|   |   | i |
|   |   | r |
|   |   | e |
|   |   | d |
|   |   | w |
|   |   | i |
|   |   | t |
|   |   | h |
|   |   | o |
|   |   | u |
|   |   | t |
|   |   | d |
|   |   | e |
|   |   | c |
|   |   | a |
|   |   | y |
|   |   | f |
|   |   | l |
|   |   | a |
|   |   | g |
|   |   | \ |
|   |   | " |
|   |   | . |
+---+---+---+
| 0 | a | M |
| 8 | t | a |
| 0 | t | k |
| 0 | r | e |
| 0 | _ | s |
|   | s | i |
|   | t | t |
|   | a | s |
|   | t | o |
|   | i | a |
|   | c | n |
|   |   | i |
|   |   | t |
|   |   | e |
|   |   | m |
|   |   | d |
|   |   | o |
|   |   | e |
|   |   | s |
|   |   | n |
|   |   | \ |
|   |   | ' |
|   |   | t |
|   |   | h |
|   |   | i |
|   |   | g |
|   |   | h |
|   |   | l |
|   |   | i |
|   |   | g |
|   |   | h |
|   |   | t |
|   |   | w |
|   |   | h |
|   |   | e |
|   |   | n |
|   |   | a |
|   |   | p |
|   |   | l |
|   |   | a |
|   |   | y |
|   |   | e |
|   |   | r |
|   |   | p |
|   |   | a |
|   |   | s |
|   |   | s |
|   |   | e |
|   |   | s |
|   |   | t |
|   |   | h |
|   |   | e |
|   |   | m |
|   |   | o |
|   |   | u |
|   |   | s |
|   |   | e |
|   |   | o |
|   |   | v |
|   |   | e |
|   |   | r |
|   |   | i |
|   |   | t |
|   |   | . |
|   |   | ( |
|   |   | I |
|   |   | t |
|   |   | e |
|   |   | m |
|   |   | s |
|   |   | w |
|   |   | i |
|   |   | l |
|   |   | l |
|   |   | s |
|   |   | t |
|   |   | i |
|   |   | l |
|   |   | l |
|   |   | h |
|   |   | i |
|   |   | g |
|   |   | h |
|   |   | l |
|   |   | i |
|   |   | g |
|   |   | h |
|   |   | t |
|   |   | f |
|   |   | o |
|   |   | r |
|   |   | G |
|   |   | M |
|   |   | s |
|   |   | n |
|   |   | o |
|   |   | m |
|   |   | a |
|   |   | t |
|   |   | t |
|   |   | e |
|   |   | r |
|   |   | w |
|   |   | h |
|   |   | a |
|   |   | t |
|   |   | . |
|   |   | ) |
+---+---+---+

You can, of course, have multiple ATTRs on a single item like this:

`<font color="darkblue">`{=html}`ATTR=attr_magic|attr_decay|attr_move_never`\
`</font>`{=html}

If you have a \@Timer script on an item, you must have an attr_decay on
that item. Otherwise you will get scary errors. You can always RETURN 1
from the \@Timer script to prevent decay, but the flag must still be
there.

## Cool Commands {#cool_commands}

Or, how to make a huge number of NPCs die at once

There are a few often overlooked commands in the SPHERE scripting
language, and the in-game command set. These are:

-   .nuke
-   .nukechar
-   .region.sectors restock

You may not understand the format of the last command yet, but I will
tell you how to use it anyway.

One thing that make SPHERE scripters do not realize is that the
`<font color="darkred">`{=html}.nuke`</font>`{=html} and
`<font color="darkred">`{=html}.nukechar`</font>`{=html} commands can
take parameters, and that those parameters will be applied to any items
within the targetted area.

Type `<font color="darkred">`{=html}.nuke`</font>`{=html} and target a
box. All the items disappear.

Now type `<font color="darkred">`{=html}.nuke color 02`</font>`{=html}
and target a box. All the items in the box turn blue.

`<font color="darkred">`{=html}.nuke dupe`</font>`{=html} is an
interesting command that creates a duplicate of any item in the box.

`<font color="darkred">`{=html}.nukechar`</font>`{=html} works the same
way:

`<font color="darkred">`{=html}.nukechar kill`</font>`{=html} will kill
any NPC you target inside of the box.

`<font color="darkgreen">`{=html}**Note:**`</font>`{=html} BOX can mean
the world too, but if you target the ground it\'ll ask for a second
targetting and will peform the actions in all chars/items in the area
you selected)

Now, after you have spawned your world, if you make massive changes to
your Vendor files, the changes WILL NOT take effect on already-spawned
NPCs. And I\'m sure you don\'t want to go around the world resetting
every single vendor. But there\'s an easier way. Do these two commands
in order:

`<font color="darkred">`{=html}.go 11 11 .region.sectors
restock`</font>`{=html} or just
`<font color="darkred">`{=html}.region.restock`</font>`{=html}

(since from 56b region.X will automatically access all the sectors of
this region too)

Magically, all your Vendors will be restocked!

NOTE TO VETERANS: **NEVER, EVER TYPE**
`<font color="darkred">`{=html}.region.restock all`</font>`{=html}!!! It
will freeze the server!

`<font color="darkred">`{=html}Extra:`</font>`{=html} If you want to
respawn all of your npcs across all maps you need to create a function
to do that, here\'s an example:

`<font color="darkblue">`{=html}`[FUNCTION redospawns]`\
`GO 1,1`\
`FOR 0 4 //make loop through all 5 maps`\
`    MAP = <LOCAL._FOR> //set the map`\
`    FORCHARS 8000 //loop through all chars in the world (unless EA makes a map bigger than 8000x8000 squares)`\
`        REF1 = <MEMORYFINDTYPE.memory_ispawned.LINK> //set REF1 to the spawngem of that npc`\
`        IF (``<REF1>`{=html}`) //checks if the npc has the spawn memory`\
`            REF1.TIMER = <EVAL {<REF1.MOREX> <REF1.MOREY>} * 60> //set the spawn memory timer to the values specified when creating it`\
`        ENDIF`\
`    ENDFOR`\
`ENDFOR`\
`</font>`{=html}

[Category:Tutorials](Category:Tutorials "wikilink")
