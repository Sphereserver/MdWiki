## Skill Menus

One of the most common requests by newbie admins is the ability to create new things via the craft skills. I've noticed that it is also one of the first things that players check out about a shard. If your shard has awesome craftable items, chances are the player will stick around longer and gain skill so he can see them. Craftable houses are the ultimate in cool. And this section will show you how to make one. First, we'll just look at how the crafting system works.

There are about 9 built-in section names, for each of the various crafting skills. This script is called from within the server, and if those sections don't exist, you will receive many scary errors. Here is the list, which I grabbed from the top of sphereskill.scp.

```
// Hard coded ref names: (called directly form server) //
```
sm_alchemy = dclick on alch tools // sm_summon // sm_polymorph = polymorph menus // sm_cartography = dclick on blank map // sm_bowcraft = knife on wood // sm_bolts = dclick on arrows or shafts // sm_blacksmith = dclick on tool // sm_carpentry = dclick on carp tool // sm_tailor_leather = dclick on sewing kit // sm_tailor_cloth // sm_tinker = dclick on tinker tools. // sm_inscription = dclick on blank scroll // sm_cook = ??? NOT USED YET

Here is the syntax of a SKILLMENU section, like every other section in a SPHERE script:

\[SKILLMENU sm_alchemy\]

Now, a skill menu is the little box that pops up that contains the pictures of the items that you can scroll through and select. There are several attributes of this box which obviously need defined. The first is the title. It goes immediately underneath the \[SKILLMENU\] `tag.`

\[SKILLMENU sm_alchemy\] What sort of potion do you want to make?

That line will be displayed across the top of the menu, as the title. In the case of the alchemy skill, we simply want to ask the user what type of potion he wishes to make. The next parts of the script are a little shaky, and contain some new constructs that you may or may not recognize. In reality, it's just a series of events, which occur depending on which menu item the user picks. Here's the part of the rest of the alchemy script:

\[SKILLMENU sm_alchemy\] What sort of potion do you want to make?

```
ON=i_potion_Agility <name> (<resmake>)
```

`   MAKEITEM=i_potion_Agility`

```
ON=i_potion_AgilityGreat <name> (<resmake>)
```

`   MAKEITEM=i_potion_AgilityGreat`

```
ON=i_potion_CureLess <name> (<resmake>)
```

`   MAKEITEM=i_potion_CureLess`

```
ON=i_potion_Cure <name> (<resmake>)
```

`   MAKEITEM=i_potion_Cure`

```
ON=i_potion_CureGreat <name> (<resmake>)
```

`   MAKEITEM=i_potion_CureGreat`

```
ON=i_potion_ExplosionLess <name> (<resmake>)
```

`   MAKEITEM=i_potion_ExplosionLess`

```
ON=i_potion_Explosion <name> (<resmake>)
```

`   MAKEITEM=i_potion_Explosion`

```
ON=i_potion_ExplosionGreat <name> (<resmake>)
```

`   MAKEITEM=i_potion_ExplosionGreat`

```
ON=i_potion_HealLess <name> (<resmake>)
```

`   MAKEITEM=i_potion_HealLess`

As you can see, we still use the `ON=` event construction for these menus as well. The different is what follows. Let's dissect it:

```
ON=i_potion_HealLess <name> (<resmake>)
```

This line tells the server a number of things. The first parameter, immediately following the = sign, is the ID of the item to display. So, what will be displayed here is the DISPID of the i_potion_HealLess item. It happens to be a yellow potion. As soon as you specify this item, it becomes the default item for the rest of that line. The server knows that `<NAME>` refers to the name of the potion item, and that `<RESMAKE>` is a string which tells what it takes to make that item. Both of those are specified in the script for i_potion_HealLess (whichis in sphere_item_provisions_potions.scp) and can easily be changed there (looks for NAME= to change the name and SKILLMAKE= to change theskill and difficulty).

```
MAKEITEM=i_potion_HealLess
```

Well if this isn't obvious, you shouldn't be reading this chapter. It simply begins the construction of the specific item. Wait, you may be asking, how does the server know which skill to use or how much skill is required, or even what to consume (1 empty bottle) when creating this item. Well, I'm glad you asked. To answer that, we need to look at the script for the item we're constructing. Ah, here it is....

\[ITEMDEF i_potion_HealLess\] NAME=Lesser Heal
```
ID=i_bottle_YELLOW RESOURCES=i_reag_ginseng, i_bottle_EMPTY SKILLMAKE=ALCHEMY 0.1 TYPE=T_POTION TDATA1=i_bottle_empty
```

```
ON=@Create
```

`   MORE1 = s_heal`
`   MORE2 = 50.0`

The two important lines are the **RESOURCES** and **SKILLMAKE** lines. These two lines work with the skill system to tell SPHERE what items are used to make this item. Basically, it says that when you create the item, you need 1 i_reag_ginseng and 1 i_bottle_empty. Incidentally, if you don't have the resources to make an item, it won't even appear on the list when you look at the SKILLMENU in-game. The next line tells the server which and how much skill is required to make this item. In this case, it says we need 0.1 in the alchemy skill. It IS just a lesser heal, after all.

Take your new i_potion_HealLess to a store and try to sell it. Magically, it seems to have a price. Where did that price come from? Well, it came from the RESOURCES. The value of a lesser heal potion is the combined value of the i_reag_ginseng and the i_bottle_EMPTY. Both of these are defined in sphere_item_resources.scp. This brings us to a point so important, I am going to put it in bold: **An item MUST have either a VALUE or resources with a VALUE, or it will not appear in a SKILLMENU!** Many newbie scripters ask on the boards about why their item is not appearing in an otherwise perfect SKILLMENU section. It has nothing to do with the SKILLMENU. Look at your item scripts before whining to us on the boards.

Another important point is this: You may have any number of lines between `ON=` events in a \[SKILLMENU\] section. It just happens that MAKEITEM does everything for us that we need it to do, so most scripts only have one line. However, you could print out a SYSMESSAGE or KILL a player within a SKILLMENU, just as easily as you could do it in any other event.

Now that we know this fact, let's build that craftable house I was referring to! First, we need to figure out what sort of RESOURCES we might want to use to craft a house. I would say a large amount of wood, maybe some metal for a doorknob, a deed to write on, and some magic just
```
for the heck of it. We'll take a resources like that looks like this:

RESOURCES=1000 i_board, 100 i_ingot_iron, 5 i_reag_garlic, i_deed

We also need a SKILLMAKE definition, and for this we'll use the Carpentry skill. Say, 95.0. Then we'll put those lines into the ITEMDEF for the deed we want to make craftable:

\[ITEMDEF i_craftable_deed\] ID=i_deed NAME=Deed to a Small Stone House RESOURCES=1000 i_board, 100 i_ingot_iron, 5 i_reag_garlic, i_deed SKILLMAKE=CARPENTRY 95.0

CATEGORY=Provisions - Deeds SUBSECTION=House Deeds DESCRIPTION=Small Stone House

ON=@Create

`   MORE1 = i_multi_house_stone_small`

This, if you haven't figured it out, is a copy of item 04202, which has been renamed and edited. You can find the original script in sphere_item_deed.scp. Now, our item has a SKILLMAKE definition, and a VALUE definition (through the RESOURCES). It is craftable. We need to stick it into one of the existing Carpentry \[SKILLMENU\] sections now. Let's look at one of them:

\[SKILLMENU sm_carpentry\] Carpentry

ON=i_board boards

`   MAKEITEM=i_board`

ON=i_chair_throne Chairs

`   SKILLMENU=sm_wood_chairs`

ON=i_chest_wooden_brass Containers & Shields

`   SKILLMENU=sm_wood_containers_shields`

ON=i_table_nightstand Table

`   SKILLMENU=sm_wood_tables`

ON=i_staff_gnarled Weapons & Tools

`   SKILLMENU=sm_wood_weapons_tools`

ON=i_armoir_dk Furniture

`   SKILLMENU=sm_wood_furniture`

ON=i_portrait_7 Paintings

`   SKILLMENU=sm_wood_paintings`

ON=i_trophy_deerhead Trophies

`   SKILLMENU=sm_wood_trophies`

ON=i_saddle Rancher Types

`   SKILLMENU=sm_wood_rancher`

ON=i_BED_9 Beds

`   SKILLMENU=sm_wood_beds`

ON=i_bulletin_board Miscellaneous

`   SKILLMENU=sm_wood_misc`

Like I said earlier, you can have any lines after an ON= section. In this case, it just happens to be a SKILLMENU line which opens up another menu. This is a hierarchical menu, because you choose from upper menu options like these, and go through lower menus, until you finally reach an item you can craft. Now, we're going to add the following two lines to the end of this script:

ON=i_craftable_deed <name> (<resmake>) MAKEITEM=i_craftable_deed

Guess what? We're done. That's all you need to do. Now, in most cases, you would make a new \[SKILLMENU sm_houses\] or something similar, and then add all of your items to that. In that case, the line you'd add to the main Carpentry menu (or one of the submenus) is the following:

ON=i_deed Craftable Houses

`   SKILLMENU=sm_houses`

That's all. Easy, isn't it? It's one of the easiest things to script, and one of the coolest. Unfortunately, it is so easy and repetitive that it takes FOREVER to make a good crafting system. If you are going to create one for your shard, start now. You should be finished in about a month. :)

```
## Menus
```

If you paid attention in the previous section, this section should be very simple for you. It is so much easier to make a simple menu than a skillmenu. And, when you see how to read from buttons in a GUMP, you will see how similar it is to this. Basically, in SPHERE, there are occasions when you may want to bring up a menu for the user to choose from. Say, when they choose the "Help Desk from Hell" option on your help menu.

Do that. Right now. See how a menu pops up and asks if the user really wants to go to the help desk from hell? He can choose Yes, or No, and something different will happen in each case. Here's what the script for that menu might look like:

\[MENU m_helpdesk\] Do you REALLY want to go to the Help Desk from Hell? You will be stuck until a GM comes to free you!

ON=0 Yes

`   SRC.GO Help Desk from Hell`

ON=0 No

`   SRC.SYSMESSAGE Help request cancelled.`

ON=0 I'm a monkey. Kill me.

`   SRC.KILL`

It looks awfully familiar, doesn't it? Here's what each part does. (I'llonly take the first four lines, because the next ones are self-explanatory if you understand the first four.

**\[MENU m_helpdesk\]**
This is rather obvious. In a script, you would call this menu like this:

MENU m_helpdesk

Difficult eh? :)

**Do you REALLY want**...
Like the skillmenu, this is the title of this section. The next thing I am about to discuss will determine where it is displayed.

**ON=0 Yes**
Aha, this is the new part. Remember what the first parameter to this section in a \[SKILLMENU\] was? Well, it's the same thing. That is the ITEM ID that the menu is supposed to display. However, we don't want a scrolling item-based menu, but rather a menu where we can select an option from a list. When you put a 0 for the ITEM ID, SPHERE will automatically assume that you want to create a text-based MENU. However, the catch is, you must put 0 for EVERY SINGLE OPTION in your menu, or else you will get a scrolling item menu like a SKILLMENU. In our case, we want to give the user options in text format, because our menu wouldn't make much sense with scrolling items for its purposes.

**SRC.GO Help Desk of Hell**
You know what this does. I just want to point out that the user of the menu is SRC, and the default object is whatever the MENU was called upon.

That's about all it takes to make a menu. Of course, you can put any commands you want after the *ON=* section, and there can be much more than one line. In fact, for most menus, there will be. That was easy, wasn't it? :)

```
## UOFiddler
```

UO comes with almost 4000 gumps. You aren't going to want to try each one in a script until you figure out which is which. You're going to need some sort of a program that shows you the gump. That program is UOFiddler, which has come to be as useful to SPHERE scripting as a sword to a warrior. Here's a link to download it:

[Download UOFiddler](http://uofiddler.polserver.com/)

It's a zip file so you need WinZip or a similar tool to extract it. Unzip it to your main SPHERE directory (where SphereSvr.exe is). If you are running a Linux server, just unzip it to somewhere on your Windows computer. It doesn't run in Linux, sorry. Now, when you run the program, you will need to enter the paths of your MUL files. In most cases, that's your the folder where you installed UO (hopefully). Go to the View menu and select File Paths. Sometimes, it will automatically detect the location of your files, in which case you don't have to do anything.

Now, click on the GUMPS button along the sidebar and wait for it to load the index file. It will have a huge list of gumps from 00000001 to some other large number. Look down through them, write some interesting ones down, because you won't want to search back through the list every time you need a specific gump ID.

Also, you're going to be needing backgrounds, which come in 9 parts. I'll explain that when we get there, but if you see a series of items, which look like they'd fit together, write that down, because it would make an excellent background.

One more thing to note before we move on to the next section: The gump IDs you see here are in HEXADECIMAL. SPHERE will only accept gump IDs in decimal. This is one of those times when you need to break out the Windows Calculator and do some conversions.

**Note:** UOFiddler is the most popular tool for viewing the contents of the UO files but it is not the only one out there. Check out the [Third Party Tools](Third_Party_Tools "wikilink") page for a list of other programs which you may want to use.

```
## Gumps
```

Congratulations. If you've made it this far, you're way past where many scripters reach. Unfortunately, this is also where many scripters hit a brick wall. Gump scripting, especially gump designing, is one of the hardest things for a scripter to do. Rather than easy-to-remember scripting commands such as REMOVE and NEWITEM, you get cryptic looking strings of letters and numbers, which are made even more complex when they use variables. Due to the difficulty, I've split the Gump Scripting 101 section into three parts. The first part shows the setup and syntax of some of the commands. The second part shows the rest of them. The third part will explain some more advanced techniques that can be used to create dynamic dialogs using relative coordinates, loops and dynamic buttons.

```
### Part 1
```

First, we need to look at the setup of a gump script, which is different than any script you've seen so far. The tag SPHERE uses to recognize a gump script is **DIALOG**. I will use the words dialog and gump interchangeably throughout these sections. Unfortunately, GUMPs come in three parts: The dialog itself, the strings that go into the dialog, and the button responses. Those couldn't all be in one section, so SPHERE has divided things up like this:

\[DIALOG d_test_dialog\] ... Code for the dialog layout goes here ...

\[DIALOG d_test_dialog TEXT\] ... The text that will be displayed in the dialog goes here ...

\[DIALOG d_test_dialog BUTTON\] ... The events that are triggered when buttons are pressed goes here ...

Now, dialogs are made up of a number of different types of objects. You can have text boxes, buttons, checkboxes, text entry boxes (which youcan change), and other various other things. They're each identified with a syntax that looks a lot like a function call. Here is the list of all the commands you can use with dialogs. I'll explain each of them in detail later.

**Dialog Objects**
resizepic <x> <y> <gumpback> <width> <height> // can come first if multi page. put up some background gump dorigin <x> <y> // Sets a dynamic origin point checkertrans <x> <y> <width> <height> // add a trasparent layer (only for clients \>= 3) gumppic <x> <y> <gump> <hue> // put gumps in the dlg. (hue only forclients \>= 3, otherwise ignored) gumppictiled <x> <y> <width> <height> <gump> // tile a gump tilepic <x> <y> <item> // put item tiles in the dlg. tilepichue <x> <y> <item> <hue> // put colored item tiles in the dlg. text <x> <y> <color> <stringindex> // put some text here. dtext <x> <y> <color> <text> // put some text here. croppedtext <x> <y> <width> <height> <color> <stringindex> dcroppedtext <x> <y> <width> <height> <color> <text> htmlgump <x> <y> <width> <height> <stringindex> <hasbackgroud> <hasscrollbar> // add an html gump that show a text dhtmlgump <x> <y> <width> <height> <hasbackgroud> <hasscrollbar> <text> // add an html gump that show a text xmfhtmlgump <x> <y> <width> <height> <clilocid> <hasbackgroud> <hasscrollbar> // add an html gump that show a cliloc text button <x> <y> <Down_gump> <Up_gump> \<pressable(1/0)\> <pagedest> <id> buttontileart <x> <y> <up_gump> <down_gump> <pressable> <page> <id> <tileid> <tilehue> <x offset> <y offset> // Add a button with tileart. textentry <x> <y> <width> <height> <color> <id> <startstringindex> // Height should be 20 dtextentry <x> <y> <width> <height> <color> <startstringindex> <text> // Height should be 20 textentrylimited <x> <y> <width> <height> <color> <id> <startstringindex> <limit> // Textentry with a limit of characters dtextentrylimited <x> <y> <width> <height> <color> <id> <limit> <text> // Textentry with a limit of characters tooltip <clilocid> // popup a tooltip over a gump object (only for clients \>= 4) radio <x> <y> <gump1> <gump2> <starting_state> <id> checkbox <x> <y> <gumpcheck> <gumpuncheck> <starting_state> <checkid> page <page_number> // for multi tab dialogs. group // used to group groups of radio buttons - Group 1, Group 2, etc. nomove // The gump cannot be moved around. noclose // The gump cannot be closed nodispose // not really used (modal?)Yes, those look complicated now, and if you want to stick with easier scripting for a while, I don't blame you. As you can see, we have all of the required objects to make a nice form, like on a website, or even to make a website-type interface. I'll show you in a later chapter how make hidden buttons and such things like that. It's not as hard as it seems.

Now, we have to discuss design. All gumps should start out like this:

\[DIALOG d_test_gump\] 0,0 page 0 ... Some objects here ... page 1 ... More objects here ...

0,0 is the position that the dialog will start on the screen. 0,0 means this dialog will appear with its upper left corner in the upper left corner of the game screen. It is possible to make a dialog start elsewhere, but it is really pointless unless the dialog is small.

Dialogs are divided into pages, and only one page can be displayed at a given time. I'll show you later how to switch between pages with buttons. However, page 0 is always displayed under the other pages. If you have something that you don't want to change between pages (like abackground or a title on top of the gump), you put it on page 0. Otherwise, it goes on another page. Page 1 is displayed by default when a dialog appears.

Now, let's add a background to our gump. Since it's something we want to stay, we'll put it in page 0. Open up your InsideUO and we'll find a good background. The piece that you're looking for is that top left corner piece. (Most things in gumps deal with the top left corner of anobject.) Find the one numbered A3C in the gump list of InsideUO. That's the background we're going to use. Actually this is a background you'll use a lot, because it's plain black with a gold border. Translating that number into hexadecimal, we get 2620. Remember that number, it's important.

The command used for backgrounds is resizepic. Look at the chart above, and you'll see what information we need to give it for a resizepic: an x coordinate, a y coordinate, a gump id, a width, and a height. We have all of those things. We'll put it at (0,0) for coordinates, and let's say we make it 500 width and 300 height. Here's the new script:

\[DIALOG d_test_gump\] 0,0 page 0 resizepic 0 0 2620 500 300 page 1

That's all. Now put that into a script and type <font color="darkred">.dialog d_test_gump</font> in-game. You'll see that we have a nice black background. It's good to be in-game while you're creating gumps, because you can test it after each new addition. Sometimes if you're off by as little as 25 in your coordinates, things will look strange. It's much easier to fix things one at a time than it is to type the entire gump script, then find out you screwed up somewhere.

Now, let's add some text to our gump. We'll say "Hello World" because that seems to be the standard for making new things in programming! There are two ways to store text, either inside the dialog or in the TEXT section. If your text is going to be used often, it's better to put it in the \[DIALOG d_test_gump TEXT\] section so you don't have to edit the same word every single time you want to change it. Otherwise, you can just add the text directly into the main dialog section. Here is an example of both:

**Using the TEXT section:**
\[DIALOG d_test_gump TEXT\] \<VAR.BLANKLINE\> Hello World

Each line has an index, starting with zero. For the first line, I always like to make a string that will evaluate to nothing, because sometimes you want empty text. I'll show you why later. Also, it makes it easier to think of your first line of text as 1 rather than 0. In our case, because Hello World is in position 1, we refer to it with text id 1. Here's what the whole script will look like now. Obviously, we're going to use that text object from the chart. We will put it at (50,50) and give it a color of 1152 (which happens to be white). We're also going to put it in page 1, because we don't want it to be there forever. Actually, I'll show you something else while we're at it.

**Using text inside the main gump:**
It's much simpler than adding it to the TEXT section. Just use the `dtext` object: dtext 50 50 1152 Hello World

Much simpler! I'll be using both examples from here on. Here's what our whole script looks like now:

\[DIALOG d_test_gump\] 0,0 page 0 resizepic 0 0 2620 500 300 page 1 dtext 50 50 1152 Hello World text 50 70 3 1

\[DIALOG d_test_gump TEXT\] \<LOCAL.BLANKLINE\> Hello World

\[DIALOG d_test_gump BUTTON\] // Nothing here yet!

See how easy it is to add text? You can also reuse text by using the same text id. If you look at this dialog in-game, you'll see that "Hello World" is written twice, because we have two text objects with Hello World. The second one is displayed 20 pixels (dots on the screen) below the first. As a general rule, all text should be assumed to be 20 pixels in height. (It's actually closer to 16, but some big letters take upmore space.)

You'll also see that they are in different colors. As a general rule, the color ID for dialog text is the color ID in-game minus 1. So black is 0, dark blue is 1, etc. New colors (like my hues.mul colors) will not display in any expected manner in a dialog, so stick to the default colors. Also, these colors are in DECIMAL, so you're going to need to convert things again. (Incidentally, color 1152 decimal is 0480hexadecimal which happens to be that ice-blue color on an item.)

Now that we've added text, we can experiment with a button. Obviously, we're going to use the button object to add a button to our gump. We need a lot of information for this button object, so I'll just copy the definition here for your reference. I'll go over each part in turn.

button <x> <y> \<gump id (down)\> \<gump id (up)\> <active> \<page \#\> <index>

Here is what each does:

```
|  |  |
|----|----|
| **\<x\> \<y\>** | This is the position of the top left corner (see?) of the button image. Try to keep dialog pieces off one another, because they will overlap in the order they are placed in the script. We're going to put our button at (50, 90), right below the second line of text. |
| **\<gump id\>** | When you press a button, it changes the picture to show that the button is in a "down" position. For our button IDs, we'll use 9A8 (2472) and 9A9 (2473). This is a red diamond shaped button that is rarely used. It has the same gold border as our background, so it'll look nice. Notice that the order is down, then up. The order of the images is up (2472), down (2473), so we'll have to switch the numbers in our script. |
| **\<active\>** | This is a switch determining whether or not the button will return an event (1) or switch pages (0). Until we discuss pages in a later section, this will always be 1. (Thanks Belgar!) |
| **\<page \#\>** | If the button will be used to switch pages, this is the page that will be displayed. Keep in mind that you should put something on the other page to switch back to the first one. You don't want to frustrate your users with a crappy interface. Put 0 if the button doesn't switch pages. |
| **\<index\>** | This is used in responding to events, as we'll see shortly. Make it a high number, probably starting in the thousands. Since this is our first button, we're going to call it button 1000. Index 0 is RESERVED, meaning you shouldn't use it for an ordinary button (we'll see why later). |
```

Here is the whole script now:

\[DIALOG d_test_gump\] 0,0 page 0 resizepic 0 0 2620 500 300 page 1 dtext 50 50 1152 Hello World text 50 70 3 1 button 50 90 2473 2472 1 0 1000

\[DIALOG d_test_gump TEXT\] \<LOCAL.BLANKLINE\> Hello World

\[DIALOG d_test_gump BUTTON\] ON=1000

`   SYSMESSAGE You pressed button 1000!`

Ooh! A new construct! The **ON=1000** you see in the button section of our dialog is how you respond to a button press. It acts just like any other ordinary event after that line. It means "When the button with ID 1000 is pressed, execute this event." In an ON event, SRC is the player operating the dialog and the default object is whatever the **DIALOG** command was used on. (On the sidenote, you can also use ONBUTTON=instead of ON=)

Thus ends the first section on gumps and dialogs (which are the samething). With this information you should be able to make just about any sort of gump you want, by playing with text and button positions. The possibilities are almost endless, and after you read Part 2, they will be endless. I have only used the information you will read in Part 2 twice in my entire long scripting career.

```
### Part 2
```

You've survived the first part of dialog scripting, and you're well on your way to designing some spectacular gumps I'm sure. OSI has provided us with a huge array of gumps, any of which you may use in your scripting. You might be surprised to see that all of the clothing and paperdoll type items are gumps and are listed with the others in InsideUO (at the bottom). There's even a leather dominatrix type uniform in there, and a whip, but that doesn't seem to have ever been used in UO as an item. Too bad.

As you know, no form would be complete without text-boxes to fill in, checkboxes to click, and radio buttons to select from. There is no shortage of gump IDs to use for these purposes, but most of them don't really fit on a normal gump (because they were made for other purposes). What I like to do is use a different background than the one we were using, and then stretch ANOTHER resizepic of the type we were using over top of the first one. Here, look at this example from my messaging system to see what I mean:

<font color="darkblue">`page 0`
`resizepic 0 0 5100 640 170`
`resizepic 15 155 5100 175 40`
`button 100 161 <eval g_btn_gray_apply> <eval g_btn_gray_apply_press> 1 0 901`
`button 20 161 5200 5201 1 0 900`
`text 5 10 1152 1`</font>
<font color="darkgreen">`resizepic 5 30 2620 600 35`
`textentry 15 36 600 20 1152 1 0 // 4 text fields now`</font>
<font color="darkred">`resizepic 5 57 2620 600 35`
`textentry 15 63 600 20 1152 2 0`</font>
<font color="yellow">`resizepic 5 84 2620 600 35`
`textentry 15 90 600 20 1152 3 0`</font>
<font color="orange">`resizepic 5 111 2620 600 35`
`textentry 15 117 600 20 1152 4 0`
</font>

Don't worry about the name or the TEXT and BUTTON sections. Notice that I have constructed a rather odd gump here. As you can see, for each textentry object, I have another resizepic object. Put this in a script (with the appropriate header tags) and look at it to see what it does.

Look carefully at the coordinates, widths, and heights of each highlighted part. If you're going to use this method, there is a particular place that you must position each so the text doesn't overlap other parts of the dialog when the player begins typing. That is called an offset. If one object is at (5, 30), and another is at (15, 36), that is an offset of (10, 6). I've discovered that the (10, 6) offset works well for space between the gold-bordered background and a textentry object.

textentry <x> <y> <gump width> <gump height> <color> <index> <text id>

Anyways, notice that the text id of each textentry field is 0. By default, the textentry field will be filled with whatever text id you give it. The player would then have to erase that to type something new, and that gets irritating. So, that's why I made the \<VAR.BLANKLINE\> be text id 0. There is nothing in the box when it appears, which is handy. See? There is rhyme to my reason, you just have to wait a while to get it.

You can also use `dtextentry`, which acts similar to dtext and doesn't require something under the TEXT section. See below for an example.

Now, when your gump returns, you're going to get a lot of data from each of those textboxes. Notice how each of them have an index? SPHERE has provided us with a nice variable array (yes, a REAL array) called ARGTXT which contains all of the text returned. You use `ARGTXT[x]` to refer to the text from textentry index x. Here is a full dialog example (actuallyit's the same one as above, but with some modifications).

\[DIALOG d_test_textentry\] page 0 resizepic 0 0 5100 640 170 resizepic 15 155 5100 175 40 button 100 161 <eval g_btn_gray_apply> <eval g_btn_gray_apply_press> 1 0 901 button 20 161 5200 5201 1 0 900 text 5 10 1152 1 resizepic 5 30 2620 600 35 textentry 15 36 600 20 1152 1 0 // 4 text fields now resizepic 5 57 2620 600 35 textentry 15 63 600 20 1152 2 0 resizepic 5 84 2620 600 35 textentry 15 90 600 20 1152 3 0 resizepic 5 111 2620 600 35 dtextentry 15 117 600 20 1152 4 // using dtextentry, you can ommit the text or add some as you wish.

\[DIALOG d_test_textentry TEXT\] \<VAR.BLANKLINE\> Enter the message you wish to send.

\[DIALOG d_test_textentry BUTTON\] ON=901 // The apply button

`   SRC.SYSMESSAGE You type <ARGTXT[1]> in textentry index 1!`
`   SRC.SYSMESSAGE You type <ARGTXT[2]> in textentry index 2!`
`   SRC.SYSMESSAGE You type <ARGTXT[3]> in textentry index 3!`
`   SRC.SYSMESSAGE You type <ARGTXT[4]> in textentry index 4!`
`   RETURN 0 // Yes, you can have RETURNs in a dialog`

This script should work fully. I did remember something while I was typing it, so I'll tell you now. The client depends on the information being sent by SPHERE, which you provide in your script, especially with the \[DIALOG TEXT\] section. If you refer to a text id that is not there, your client WILL crash. It is easier to crash a client with dialogs than anything else in the game. On my old server, if there was a player I didn't like, I would put an event on his character so a client-crashing gump would appear every time he logged in, no matter what. The GMs used to go crazy trying to fix that. :)

My example should help you understand the syntax of getting data from a textentry box. Now you can make forms rather than just still-life dialogs. Remember, you don't need the resizepic background, because a textentry will work no matter what. It just helps the player know where to type.

```
### Part 3
```

Here I'm going to add a few tips and tricks to make scripting your dialogs easier, as well as explaining some of the newer features.

```
#### Using DOrigin
```

DOrigin lets you set a dynamic origin point while still retaining your static origin which you set at the top of the dialog. When setting the x,y coordinates of other elements such as dtext you can specify them as offsets of dorigin rather than using fixed coordinates.

\[DIALOG d_test\] 50,50 // This is your static origin point Page 0

resizepic 0 0 9300 150 100 dtext 10 10 1152 This is a test dialog

dorigin 10 10 // this is your dynamic origin point dtext \*0 \*20 100 Test 1 // here I set this text to display at 10x 30y dtext +50 -0 100 Test 2 // now I offset this text by +50x and keep the same y as the last entry to use \*'s. It appears now at 60x 30y dtext \*0 \*20 100 Test 3 // here I set the text to display at 10x 50y dtext +50 -0 100 Test 4 // As with Test 2 it is offset by +50x and same y, so in theory it's really at 60x 50y dtext \*0 \*20 100 Test 5 // Same as Test 3 but now at 10x 70y dtext +50 -0 100 Test 5 // Same as Test 4 but now at 60x 70y

What makes this so powerful is that we can now simply copy and paste the last two lines over and over to add more rows without having to each time calculate the x's and y's. This gets especially usefull when you have more than two columns and will prove even more useful when using loops (more on that later). You can now also move the whole "block" of Test text left, right, up or down by simply changing the dorigin. Try it out for yourself, set dorigin to 50 30 and all your text will move 40 right.

There are three different ways that you can specify relative coordinates:

```
|  |  |
|----|----|
| **Syntax** | **Description** |
| -n | n is subtracted from the origin, the origin point does not change |
| +n | n is added to the origin, the origin point does not change |
| \*n | n is added to the origin, the origin is changed to the new position |
|  |  |
```

You can also mix and match different relative and fixed coordinates types. Here are some examples, assuming that DOrigin has been set to 50 50:

```
|                          |                       |                    |
|--------------------------|-----------------------|--------------------|
| **Example**              | **Line Result**       | **DOrigin Result** |
| dtext -10 -20 100 Text   | dtext 40 30 100 Text  | 50 50              |
| dtext +10 +20 100 Text   | dtext 60 70 100 Text  | 50 50              |
| dtext \*10 \*20 100 Text | dtext 60 70 100 Text  | 60 70              |
| dtext \*20 100 100 Text  | dtext 70 100 100 Text | 70 50              |
| dtext +30 \*20 100 Text  | dtext 80 70 100 Text  | 50 70              |
| dtext +0 \*20 100 Text   | dtext 50 70 100 Text  | 50 70              |
```

```
#### Dynamic Dialogs using Loops and Functions
```

Lets take the dialog above and see if you can make it shorter in the script but at the same time have 20 lines of Test text! Sounds impossible? Not at all, Sphere can use functions inside dialogs, so anything you can do in a script you can do in a dialog.

\[DIALOG d_test\] 50,50 page 0

resizepic 0 0 9300 150 440 dtext 10 10 1152 This is a test dialog

dorigin 10 10 FOR 20

`   dtext *0 *20 100 Test <dLOCAL._FOR>`
`   dtext +70 -0 100 Test <dLOCAL._FOR>.1`

ENDFOR

Now imagine that we have to use these FOR loops lots of times inside our whole dialog, or maybe even in more than one dialog. Isn't there an even easier way to do this? Yep there is, using a function:

\[FUNCTION f_test_text\] FOR 20

`   dtext *0 *20 100 Test <dLOCAL._FOR>`
`   dtext +70 -0 100 Test <dLOCAL._FOR>.1`

ENDFOR

Now we just add it to our dialog, but this time we're going to add a second set of text to the left by creating another dynamic origin point!

\[DIALOG d_test\] 50,50 page 0

resizepic 0 0 9300 350 460 dtext 10 10 1152 This is a test dialog

dorigin 10 10 dtext \*0 \*20 100 Left Columns F_TEST_TEXT

dorigin 100 10 dtext \*0 \*20 Right Columns F_TEST_TEXT

Pretty cool isn't it! This is just the beginning, the rest I'll leave to your scripting talent! :)

```
#### Dynamic Buttons
```

Lets take the same dialog and function as before and just modify it slightly so it all looks like this:

\[DIALOG d_test\] 50,50 page 0

resizepic 0 0 9300 350 460 dtext 10 10 1152 This is a test dialog

dorigin 10 10 dtext \*0 \*20 100 Left Columns F_TEST_TEXT 100

dorigin 200 10 dtext \*0 \*20 100 Right Columns F_TEST_TEXT 130

\[DIALOG d_test BUTTON\] ON=100 120 // handle button IDs 100 to 120

`   SRC.SYSMESSAGE You have pressed button <EVAL (`<ARGN1>` - 100)> from the left column!`
`   DIALOG d_test`

ON=130 150 // handle button IDs 130 to 150

`   SRC.SYSMESSAGE You have pressed button <EVAL (`<ARGN1>` - 100)> from the right column!`
`   DIALOG d_test`

\[FUNCTION f_test_text\] FOR 20

`   button *0 *20 5603 5607 1 0 <EVAL (<LOCAL._FOR> + `<ARGN1>`)>`
`   dtext +50 -0 100 Test <dLOCAL._FOR>`

ENDFOR
```

As you can see I have added a parameter (aka argument) to the `f_test_text` function. In this case it is to be the button starting range that I want for the button that is replacing one Test text column.

In the BUTTON part of the dialog I have regrouped the buttons, from 100-120 will be the 20 buttons of my left column and from 130-150 there will be the my 20 right column buttons. When pressing a button, `<ARGN1>` is the button number, hence using the EVAL in the BUTTON section to find out what the "virtual" button is (the real one remaining<ARGN1>).

It's pretty simple and with a bit of playing around you should get this to work easily. Good luck!

[Category:Tutorials](Category:Tutorials "wikilink")
