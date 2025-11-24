```{=mediawiki}
{{Languages|Chapter_7}}
```
## Recursive Functions {#recursive_functions}

I discovered this very seldom explored extension of SPHERE scripting
while reading messages on the boards. Someone was trying to create a
function that counted the number of items in a container using this sort
of thing, and it worked for the most part. I was very amazed, because
before that, no one had even thought of using functions that looped back
upon themselves.

Which is what a recursive function is. I\'ll say it one more time.

A recursive function is one that calls itself, or recurs. Surprise!

So how do we do this? It\'s as simple as calling a function:

`<spherescript>`{=html}\[FUNCTION recursive_test\]
recursive_test`</spherescript>`{=html}

This very small piece of code in fact IS a recursive function. As you
can see, the function will call itself and start over from the
beginning, which will proceed to call the function again, and again, and
again, and on and on. In this case, we don\'t have any way to stop it.
This is called an infinite loop, one that will continue forever without
stopping. Your server will die a flaming death.

**Lesson 1: How to NOT create an infinite loop**

Let me tell you right now. You will write a script that implements an
infinite loop. You will test it. Your server will die. It\'s guaranteed.
No programmer can say that they have never accidentally written an
infinite loop. (RANDOM NOTE: All windows programs are in fact infinite
loops. Your SPHERE server is an infinite loop.) In a SPHERE script,
however, here\'s what happens:

1.  The function is called.
2.  Some stuff takes place
3.  The function is called from within itself. Being a good scripting
    language, it records where it left off so it can go back later. This
    is called the stack.
4.  Go back to number 1.

This \"stack\" builds up very very quickly, and soon the server cannot
allocate any more memory for it, and will crash when it tries. Fun
stuff, I tell you.

Anyways, here is one way to avoid creating an infinite loop. Let\'s say
we want to make a function that executes SRC.SYSMESSAGE Hello World 35
times. Here would be an example of how one could do this:

`<spherescript>`{=html}\[FUNCTION recurse_hello\] IF (`<ARGN1>`{=html}
\< 1)

`   RETURN 1`

ENDIF SYSMESSAGE Hello World RECURSE_HELLO \<EVAL `<ARGN1>`{=html} - 1\>
RETURN 1`</spherescript>`{=html}

Then, in another script, we would execute this command:
`<font color="darkred">`{=html}SRC.RECURSE_HELLO 35`</font>`{=html}

Remember what ARGN is from the previous chapter? It\'s the argument to
the function stored as a number. Initially, as you can see, it\'s 25
because we made it be that way. However, every time the function calls
itself, or \"recurses\", it sets ARGN1 to be one less than itself.
Here\'s the step-by-step analysis of this:

1.  The function is called. ARGN1 is 35 because we said so.
2.  It checks to see if ARGN1 is less than one. If it is, we immediately
    RETURN 1 and set off the chain reaction that stops the recursive
    function.
3.  The next part should be fairly obvious. We\'re sending a SYSMESSAGE
    to the default object. Because we used SRC when we initially called
    the function, the default object is SRC.
4.  This is where the recursion takes place. The function calls itself
    with an argument ONE LESS than the current one. This starts the
    whole thing over at step 1. This is a NEW FUNCTION CALL, remember.
    The original function call STILL EXISTS and the program will
    \"rewind\" back down the stack to that location later. That is why I
    have a RETURN 1 after the function call.

That\'s your example of a recursive function. It isn\'t very practical.
Let\'s look at a more practical example. See if you can figure it out
for yourself. This is courtesy of Belgar, for the most part:

`<spherescript>`{=html}\[FUNCTION pack_to_bank\] IF
(\<FINDLAYER.21.FINDCONT.0.UID\> == 0)

`   RETURN 1`

ENDIF FINDLAYER.21.FINDCONT.0.CONT = \<FINDLAYER.layer_bankbox.UID\>
PACK_TO_BANK RETURN 1`</spherescript>`{=html}

(As you can see, we don\'t always need an ARGS to make a function loop.
In this case, we use a backpack with an unknown number of items inside
and only stop when the pack no longer contains items.)

Recursive functions are very useful. Be sure you don\'t overuse them,
though! Remember, while a script is running, YOUR SERVER IS FROZEN. If a
recursive function takes too long to complete, your server will lag. A
good method is to make sure that no function should be looping more than
about 500 times. (Actually other server emulators such as POL have a
mechanism to catch \"runaway scripts\" like this and halt them in their
tracks.)

## FOR

### FOR {#for_1}

FOR is a powerful way to create a recursive function, and it allows a
simpler level of control over your recursions.

Usage:

`<spherescript>`{=html}\[FUNCTION for_display\] FOR X 1 20

`   SYSMESSAGE <LOCAL.X> //Will sysmessage the current for count.`

ENDFOR`</spherescript>`{=html}

The loop will loop through 20 times, starting at 1 and ending at 20. X
is the variable containing the current FOR count. If no variable is
declared, the count can be accessed using \<LOCAL.\_FOR\>

Changing LOCAL.\_FOR or whatever you declared as count, will not change
the loop\'s behaviour. But be aware that if you \"stack\" FOR loops
without giving them different loop variables, the innermost loop will
overwrite the loop variables of its successors, usually leading towards
a completely messup of the whole loop stuff.

### FORCHARLAYER

FORCHARLAYER is another type of FOR loop. Basically it allows you to
loop through each item that is stored on the specified layer of a
character. This can be useful for when you want to manipulate all of the
spell runes or memory items on a character as an alternative to using
FINDLAYER.x in a loop.

Something to be aware of here is that whilst inside the loop, the
default object will be temporarily changed to the item in the loop. As
you can see in the following example, we must store a reference to the
original default object (the character) so that we can still reference
it from within the loop:

`<spherescript>`{=html}\[FUNCTION get_mitems_names\] REF1 =
`<UID>`{=html} // store the default object in REF1 FORCHARLAYER 30

`   REF1.SYSMESSAGE ``<NAME>`{=html}` is a memory item in layer ``<LAYER>`{=html}

ENDFOR`</spherescript>`{=html}

### FORCHARMEMORYTYPE

FORCHARMEMORYTYPE is a very useful type of FOR loop. You may want to use
it for experience systems, and some player and NPC killing systems. It
loops through every memory item on a character that has a specified
flag.

For example, a character has 4 memory items with the following names and
flags:

  ----------- -------
  Ellessar    02000
  Sorea       022bc
  Introvert   0740d
  Enrath      0c40d
  ----------- -------

**Script:**\
`<spherescript>`{=html}\[FUNCTION get_harmedby_mems\] REF1 =
`<UID>`{=html} // As with FORCHARLAYER, the default object changes
within the loop FORCHARMEMORYTYPE memory_harmedby // Loop through memory
items with flag 00010=memory_harmedby

`   REF1.SYSMESSAGE There is a memory item with name ``<NAME>`{=html}`, uid ``<UID>`{=html}`, flags ``<COLOR>`{=html}` and one of its flag is also 00010.`

ENDFOR`</spherescript>`{=html}

**Result:**\
On your screen you would see:

*There is a memory item with name Ellessar, uid 04f000001, flags 02000
and one of its flag is also 02000.*\
*There is a memory item with name Sorea, uid 04f000002, flags 022bc and
one of its flag is also 02000.*\
*There is a memory item with name Introvert, uid 04f000003, flags 0740d
and one of its flag is also 02000.*\
`</tt>`{=html}

**Note that there are only three messages, because the memory item
\"Enrath\" does not have the flag 02000.**

### FORCHARS

FORCHARS is a FOR loop that you can use to check all mobiles (online
player and NPC) within a set radius of an object.

The correct syntax being *FORCHARS x* where *x* is the radius in tiles
the loop will cover.

-   **FORCHARS 2** would check any mobile within a 2 tile radius
-   **FORCHARS 18** would check the area inside your screen
-   **FORCHARS 6144** would check the entire world map

One example of a function using FORCHARS

`<spherescript>`{=html}\[FUNCTION kill_vendors\] FORCHARS 6144 // checks
entire map

`   IF (``<BRAIN>`{=html}` == brain_vendor) //argument for what will be acted upon within this function`\
`       KILL // action`\
`   ENDIF `

ENDFOR`</spherescript>`{=html}

As with all FOR loops you have to stipulate inside the loop what it is
to act upon, if you are restricting it to certian players/npcs (or in
the case of FORITEMS, items) otherwise it will perform the action upon
all online players/npcs within the radius of the loop.

In this case the loop checks for any Vendor npc\'s and kills them.

### FORCLIENTS, FORPLAYERS {#forclients_forplayers}

FORCLIENTS and FORPLAYERS are FOR loops, both are used to affect a
clients/players in certain radius. If you do not set the radius, radius
18 is used as default. While FORCLIENTS only acts on player characters
who are logged in, FORPLAYERS acts on each and every player character,
even if logged off.

**Usage:**\
`<spherescript>`{=html}\[FUNCTION radius_players\] FORCLIENTS 25

`   IF (<ACCOUNT.PLEVEL> <= 1) // Affects only logged in players, not staff`\
`       SAY I am here!`\
`   ENDIF`

ENDFOR`</spherescript>`{=html}

### FORCONT

FORCONT is a type of FOR loop. It loops through every item in a
container. The default object inside the loop will be the item currently
being looped over.

**Usage:**\
`<spherescript>`{=html}\[FUNCTION rem_spellbooks\] FORCONT
\<FINDLAYER.21.UID\> 10 // \<FINDLAYER.21.UID\> - UID of a container,
10 - how many subcontainers the function goes through, if set 0, it
affects only items in container with UID

`   IF (``<BASEID>`{=html}` == i_spellbook)`\
`       REMOVE`\
`   ENDIF`

ENDFOR`</spherescript>`{=html}

### FORCONTID

FORCONTID is a FOR loop that works in a similar way to FORCONT, except
that it will only cycle through items that have a specific BASEID. You
can set the amount of subcontainers to loop through, like the FORCONT
example.

**Usage:**\
`<spherescript>`{=html}\[FUNCTION rem_spellbooks2\] FORCONTID
i_spellbook 10

`   REMOVE`

ENDFOR`</spherescript>`{=html}

### FORCONTTYPE

This is another FOR loop that is almost identical to FORCONTYPE. The
only difference is that instead of looping through items with a specific
BASEID, it will loop through items with a specific TYPE. Following the
spellbooks remover example:

**Usage:**\
`<spherescript>`{=html}\[FUNCTION rem_spellbook3\] FORCONTTYPE
t_spellbook

`   REMOVE`

ENDFOR`</spherescript>`{=html}

### FORINSTANCES

You may have seen scripts that do something like the following:

`<spherescript>`{=html}\[FUNCTION removespawns\] FORITEMS 9999

`   IF (``<BASEID>`{=html}` == i_worldgem_bit)`\
`       REMOVE`\
`   ENDIF`

ENDFOR`</spherescript>`{=html}

At a glance this script looks like a fairly useful script that can be
used to remove all of your i_worldgem_bit (spawn) items from the server.
If you attempt to run it you will most certainly notice that your server
pauses for a signicantly long time (on a well-populated server you may
even end up waiting a whole minute for the script to run), even if you
only have several instances of the item on the server! The reason that
this happens is because *FORITEMS 9999* will loop through *every* item
within the 9999 tile radius, so the code will be looping hundreds or
thousands of times when you only wanted to affect a handful of items!

To resolve this issue we have FORINSTANCES. This is a special loop which
will loop through all instances of a given character or item BASEID that
exist on the server. This offers the following advantages over using
*FORITEMS/FORCHARS 9999*:

-   Sphere will only run your script for objects with the BASEID you are
    interested in.
-   Sphere knows how many instances of the object exist, so can abort
    the loop at an appropriate time.
-   Items inside containers (e.g. character backpacks or player banks)
    will not be missed out.

So with this in mind, the above script can be rewritten to the
following:

`<spherescript>`{=html}\[FUNCTION removespawns\] FORINSTANCES
i_worldgem_bit

`   REMOVe`

ENDFOR`</spherescript>`{=html}

Now when you run this script you should notice a significant drop in the
execution time.

**Note:** Since Sphere still has to internally search for references to
the objects you\'re after you may find that on well-populate servers
there is still a noticable pause. If you need to use this kind of loop
then you should do so sparingly, and if you need to regularly use this
then you may wish to consider finding a more optimal way of implementing
your script(s).

### FORITEMS

FORITEMS works in much the same way that FORCHARS does, except it checks
for ITEMS within the set radius as opposed to characters. Default obejct
is set to the item which can be affected.

A basic example of a function using FORITEMS:

`<spherescript>`{=html}\[FUNCTION Spawn_remover\] FORITEMS 6144 //once
again it checks the entire map

`   IF (``<TYPE>`{=html}` == t_spawn_char) //if this arguement is met`\
`       REMOVE //remove it`\
`   ENDIF //end the IF arguement`

ENDFOR //end the FOR loop `</spherescript>`{=html}

### FOROBJS

FOROBJS works in the same way that FORITEMS and FORCHARS does with the
exception that this loop will find both characters **AND** items within
the specified radius.

## WHILE

WHILE is a *conditional loop*, a block of code that will repeat itself
whilst a given condition is true. Basically you can think of this as
being an IF..ENDIF block that will run indefinately until the IF
statement returns false.

**ALWAYS AND ALWAYS:**

1.  End WHILE blocks with ENDWHILE.
2.  Perform some action within the WHILE block that will change the
    outcome of the conditional statement.

For example:

`<spherescript>`{=html}\[FUNCTION remove_all_mems\] WHILE
(\<FINDID.i_memory.UID\>) // continue to loop whilst an i_memory item is
found inside the object

`   FINDID.i_memory.REMOVE  // remove a memory item`

ENDWHILE`</spherescript>`{=html}

Whilst inside the loop, LOCAL.\_WHILE can be used to access the number
of times that the script has looped so far. In some situations you may
want to use this to impose a \'limit\' on how many times your WHILE
block can loop before it is forced to exit. An example of this could be:

`<spherescript>`{=html}\[FUNCTION random_health\] WHILE (`<HITS>`{=html}
\> 10) && (\<LOCAL.\_WHILE\> \< 20) // loop whilst the character has
more than 10 health, but no more than 20 times

`   HITS = <R1,100>    // set the character's health to a random value between 1 and 100`

ENDWHILE`</spherescript>`{=html}

Since random numbers are.. random.. it is in theory possible that the
health will never be set to a value less than or equal to 10. By
checking LOCAL.\_WHILE inside the WHILE condition we add protection
against the script looping indefinately and freezing the server.

## TRY

### TRY {#try_1}

TRY can be used to execute a line of script where the left hand side
(i.e. a property being set or a function being called) is based on the
value of an expression.

For example, we may have the following script:

`<spherescript>`{=html}LOCAL.TEST = 05 SRC.TAG0.MYTAG\_\<LOCAL.SOME\> =
1234`</spherescript>`{=html}

Sphere will add a TAG named \"MYTAG\_\<LOCAL.SOME\>\" with a value of
\"1234\", when really we were hoping for \"MYTAG_05\". We can use TRY to
accomplish this:

`<spherescript>`{=html}LOCAL.TEST = 05 TRY
SRC.TAG0.MYTAG\_\<LOCAL.SOME\> = 1234`</spherescript>`{=html}

This causes Sphere to evaluate the entire line first, as
\"`SRC.TAG0.MYTAG_05 = 1234`\" and then run it, giving us the
\"MYTAG_05\" TAG as we were after.

**Note:** Since 27-11-2006 the TRY function has become obsolete. Sphere
will now always evaluate the entire line before executing it.

### TRYP

This is the same as the TRY function, except that a PLEVEL parameter is
also supplied. If SRC\'s PLEVEL is less than this value then the line
will not be executed, for example:

`<spherescript>`{=html}TRYP 4 UID.\<TAG.CHARUID\>.NAME
Yerk`</spherescript>`{=html}

The above line will not be executed if SRC\'s PLEVEL is less than 4, so
it will not run for players but it will to GM and above. This is almost
the same as writing:

`<spherescript>`{=html}IF (\<SRC.ACCOUNT.PLEVEL\> \>= 4)

`   UID.<TAG.CHARUID>.NAME Yerk`

ENDIF`</spherescript>`{=html}

However, with TRYP the line will also run if there is no SRC (in an
\@Timer trigger, for example). So a more accurate scripted equivalent
would be:

`<spherescript>`{=html}IF !(`<SRC>`{=html})

`   TRY UID.<TAG.CHARUID>.NAME Yerk`

ELSEIF (\<SRC.ACCOUNT.PLEVEL\> \>= 4)

`   TRY UID.<TAG.CHARUID>.NAME Yerk`

ENDIF`</spherescript>`{=html}

### TRYSRC

As already mentioned in a previous chapter, the TRYSRC function can be
used to override the SRC object for a given line.

The syntax for this function is `TRYSRC uid command`, where `uid` is the
UID of the character who you want to become SRC, and `command` is the
command you want to execute.

`<spherescript>`{=html}ON=@Timer

`   // place 5000 gold coins in LINK's backpack`\
`   SERV.NEWITEM i_gold`\
`   NEW.AMOUNT = 5000`\
`   TRYSRC <LINK.UID> NEW.BOUNCE // the BOUNCE function places an item into SRC's backpack`\
`   RETURN 1``</spherescript>`{=html}

### TRYSRV

TRYSRV is similar to the TRYSRC command except that rather than running
a command with a specific character as SRC, the command is instead
executed with SRC set to the SERV object.

This can be desirable in the following situations:

-   Certain properties of accounts, such as passwords, are protected
    against being accessed unless SRC has a PLEVEL of 7 (owner). It
    would be incredibly dangerous and unwise to set a player\'s PLEVEL
    to 7, even temporarily, but the SERV object is always considered to
    have a PLEVEL of 7.
-   Certain functions/commands behave differently with a character as
    SRC, for example:
    -   SERV.NEWNPC will automatically set the new NPC\'s position to
        beside the SRC character. By using `TRYSRV SERV.NEWNPC` you can
        avoid players seeing an NPC \'flicker\' on and off their screen.

## SERV

### CHARDEF

Let\'s say you wanted to retrieve the DAM property from, say, a Liche.
Because DAM isn\'t a character property, we can only get the property
from the CHARDEF. (Technically, there is a DAM property for characters,
but it is not what we\'re looking for.)

`<spherescript>`{=html}\[FUNCTION f_return_char_prop\] LOCAL.DAM =
\<SERV.CHARDEF.`<ARGS>`{=html}.DAM\>`</spherescript>`{=html}

With the above example, Sphere will take the argument passed (ARGS),
then try to store the DAM property from the corresponding CHARDEF into
LOCAL.DAM.

Pretty simple, right?

### ITEMDEF

This works similar to SERV.CHARDEF, only it works on ITEMDEFs. Let\'s
say you wanted to get the SKILL property from a character\'s equipped
weapon.

Here\'s an example:

`<spherescript>`{=html}\[FUNCTION f_return_wep_skill\] LOCAL.WEP_SKILL =
\<SERV.ITEMDEF.`<ARGS>`{=html}.SKILL\>`</spherescript>`{=html}

That would store the SKILL property of whatever ITEMDEF passed (ARGS)
into LOCAL.WEP_SKILL. And this can get much more complex. As an example,
I recently wrote a script that does the following:

-   Use QVAL to find the equipped weapon.
-   Store the weapon found in REF1.
-   Check to see if REF1 returned a weapon UID.
-   Store the DAM property for the weapon in LOCAL.WEP_DAM.

`<spherescript>`{=html}\[FUNCTION f_weapon_dam\] REF1 = \<QVAL
\<FINDLAYER.1.UID\> ? \<FINDLAYER.1.UID\> : \<FINDLAYER.2.UID\>\> IF
(`<REF1>`{=html}) // REF1 is true; weapon found.

`   LOCAL.WEP_DAM = <SERV.ITEMDEF.<REF1.BASEID>.DAM>`

ENDIF RETURN \<LOCAL.WEP_DAM\>`</spherescript>`{=html}

That\'s not too complex, is it?

### LOG

This functions is very good if you want to see when a player makes
something or say something or when want to know the result of formulas
in your scripts. This, is for writing messages onto the console (and
logs). It is really simple to use:

`<spherescript>`{=html}SERV.LOG Hi world`</spherescript>`{=html}

And when you look at console it shows something like:

`<spherescript color="darkgreen">`{=html}21:56:(YourScript.scp,2)Hi
world`</spherescript>`{=html}

Easy and useful.

**Note:** If for some reason you don\'t want the script name to appear
in the log, prefix your log message with the \'@\' character (prefix the
message with two \'@\' characters (@@) if you actually want to start the
message with the @ symbol.

### MAP

The SERV.MAP function allows you to read the properties of a specific
point on a map. There are two syntaxes that can be used:

1.  `<SERV.MAP(x,y,map)>.KEY`
2.  `<SERV.MAP(x,y,z,map)>.KEY`

You may notice a slight \'peculiarity\' in these syntaxes and you should
be aware of them so that they don\'t catch you out: When there are 3
parameters given, the third parameter is used as the map number to
access. When 4 parameters are given, the third parameter is the height
(Z) and the fourth becomes the map number.

The KEY can be a number of things:

  ------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------
  ISNEARTYPE type distance checkmulti   Returns 1 if an item exists near the point within \<distance\> tiles. If \<checkmulti\> is 1 then multi components will also be checked.
  REGION                                Access the REGION at the map point.
  ROOM                                  Access the ROOM at the map point.
  SECTOR                                Access the SECTOR at the map point.
  STATICS                               The number of static items at the map point.
  STATICS.n.ID                          The ID of the nth static item at the map point (n starts at 0)
  STATICS.n.COLOR                       The COLOR of the nth static item at the map point (n starts at 0)
  STATICS.n.Z                           The Z level of the nth static item at the map point (n starts at 0)
  STATICS.n.\*                          If the STATICS.n.KEY does not match any of the above properties, the value will be taken from the static\'s ITEMDEF in the scripts
  TERRAIN                               The ID of the terrain at the map point.
  TYPE                                  The type of terrain at the map point.
  X, Y, Z, M, MAP                       Access the X/Y/Z/MAP values at the map point.
  COMPONENTS                            The number of components items at the map point.
  COMPONENTS.n.ID                       The ID of the nth component item at the map point (n starts at 0)
  COMPONENTS.n.Z                        The Z level of the nth component item at the map point (n starts at 0)
  ------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------

### NEWDUPE

When you use the `<font color="darkred">`{=html}.DUPE`</font>`{=html}
command you can create a \'clone\' of a targeted item. The NEWDUPE
function allows this functionality to be reproduced within scripts.

The syntax of the function is `NEWDUPE uid`, where uid is the UID of the
object you want to clone. After running this function, the SERV.NEW
reference will be set to the newly cloned item. You should know that it
creates the \'duped\' item exactly on the same spot where the targeted
item exists. So you may have to move it anywhere else or it will maybe
crush your stack.

Here is an example, the script below will clone the character\'s weapon
and place it in their backpack:

`<spherescript>`{=html}\[FUNCTION f_dupeweapon\] IF (\<WEAPON.UID\>)

`   SERV.NEWDUPE ``<WEAPON>`{=html}\
`   BOUNCE <NEW.UID>`

ENDIF`</spherescript>`{=html}

### NEWITEM

This is an easy function, used to create items. Many of you learned in
55i tutorials the format of NEWITEM, well, this changed on 56b and this
is mainly to explain that change.

Now, you can\'t use this function on some player, you have to create it
on SERV. Also, the reference to the new item isn\'t SRC.ACT anymore. It
changed to NEW, so, if i want to create an item with the color 9, it
will look like this:

`<spherescript>`{=html}SERV.NEWITEM i_example NEW.COLOR
9`</spherescript>`{=html}

As you can see, it is really easy to use. There are also additional
parameters that can be optionally passed into NEWITEM:

`NEWITEM id, amount, cont, triggerEquip`

So if I want to create 3 i_test in SRC\'s backpack I should do:

`<spherescript>`{=html}SERV.NEWITEM i_test, 3,
\<SRC.FINDLAYER.21.UID\>,1`</spherescript>`{=html}

Easy, uh?

### NEWNPC

This function can be used to create NPCs in the world. The syntax is
`NEWNPC id`, where `id` is the BASEID of the character you wish to
create. The newly created character can be accessed via the NEW
reference.

The following function creates a headless and moves it to within 10
tiles of the default object.

`<spherescript>`{=html}\[FUNCTION f_createnpc\] SERV.NEWNPC c_headless
NEW.MOVENEAR `<UID>`{=html} 10`</spherescript>`{=html}

**Note** It is also possible to create player characters this way, by
setting the ACCOUNT property after creating the new character.

### NEWSUMMON

This function similar to NEWNPC but is specific to summons. This will
allow you to create a new summoned creature for a specific time.

`<spherescript>`{=html} \[FUNCTION f_createsummon\]
SERV.NEWSUMMON=c_ogre,15 NEW.P=

`</spherescript>`{=html}

This example will summon and Ogre for 15 seconds at your current
location.

### SKILL

Well, this is an easy function, like the others. This one refers to the
SKILL section.

You can see the skill properties in sphere_skills.scp. I\'ll explain how
it works:

`<spherescript>`{=html}LOCAL.SKILL =
\<SERV.SKILL.`<ACTION>`{=html}.KEY\>`</spherescript>`{=html}

With that line you get the Skill Key (Alchemy, ex.).

There are 3 ways to use SERV.SKILL: Key, Defname, Number.

Any of them are accepted, and if you see, in most of the cases people
use Action to get the Key and get the player skill amount.

You can find many uses for it, all you need is some imagination.

[Category:Tutorials](./Tutorials.md)
