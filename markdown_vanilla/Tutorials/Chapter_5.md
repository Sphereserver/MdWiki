## Tags

All these things you have learned so far seem rather restrictive don't
you think? Well, I personally don't think they are very restrictive and
I was able to script most things that people are scripting today in
about version .40. But think about it. Items are restricted to MORE,
MORE2, etc. Those poor characters only have PLOT2 to store stuff in
before you have to start resorting to storing information on the
variables of their backpack.

So SPHERE developers gave us a long-awaited feature:

The TAG.

Important TAG principle number one, even before you know how to use
them:

**ALL TAGS ARE STRINGS. PERIOD.**

They are also just about the simplest part of SPHERE you will ever use.
Here is an example of a tag:

<font color="darkblue">`SRC.TAG.JOE = 1`  
</font>

What did we just do? We just CREATED a variable on the SRC of this
script. This variable is named TAG.JOE and has a value of 01. (Keep in
mind that is the string 01, not the number 01.) It will be saved with
the character and we can put ANYTHING WE WANT into it.

How's that for powerful?

Here are some more examples of TAGs:

<font color="darkblue">`ON=@DClick`  
`:SRC.TAG.CLICKS += 1`  
`:RETURN 1`  
  
`ON=@Equip`  
`:SRC.TAG.GOOFYTAG = This is a really stupid tag.`  
`:SRC.SYSMESSAGE <SRC.TAG.GOOFYTAG> // Will see "This a really stupid tag."`  
`:RETURN 0 // Allow them to equip`  
  
`ON=@UnEquip`  
`:SRC.TAG.GOOFYTAG = // remove the tag`  
`:RETURN 0 // Allow them to unequip`  
</font>

In those three examples, you have the three ways you can use a TAG.

1.  A TAG can store a number as in the first example. Unfortunately, it
    stores that number as a string, so we must use EVAL every time we
    want to use that number.
2.  A TAG can store a string, as in the second example. Actually TAGs
    always store strings, but this one is obviously a string.
3.  You can delete a TAG. We do this by typing the name of the tag and
    then an equal sign with nothing after it. Why would we ever want to
    delete a TAG? Well, TAGs, like everything else, use memory. The more
    memory you use, the more lag your server has.

TAG principle number two:

**ALWAYS DELETE A TAG YOU ARE FINISHED USING.**

You may not be finished using a TAG at the end of a script. Or even when
the server shuts down. In fact, there are some TAGs you'll want to stay
on the character forever. However, if you finish using a TAG for any
reason, DELETE IT. It conserves memory and is good scripting practice in
general.

Here is another important TAG principle. While the TAG is a very
powerful feature, it has its limits. A TAG can ONLY be used on the
following objects:

1.  Characters.
2.  Items.
3.  Regions. Yes, regions can have TAGs.

It's very hard to give examples of the use of TAGs without going into a
complex system. Most complex systems will use two, three, or more
PERMANENT tags. For example, a system involving experience points might
store numbers in TAG.CURRENT_EXPERIENCE_POINTS and TAG.CURRENT_LEVEL.
You'll find a good example of when to use TAGs to your advantage in
chapters from now on, as I present more and more complex scripts. BTW,
when you're dealing with tags, sometimes you need to check if a tag
exists or if it has a value. If it doesn't exist SPHERE gives a stupid
error on the console. To avoid that, we make TAG's default to 0 by using
TAG0 instead of TAG if the tag doesn't exist. If you want to you can
always use TAG0 instead of TAG to be safe. Say you write this line of
code:

<font color="darkblue">`MORE = <EVAL <TAG.JOE>>`  
</font>

If TAG.JOE contains no value (or hasn't been defined yet), you will get
an error on the console that says something like this: Undefined value '
'. To complicate matters, the value of MORE will not change, which will
severely screw up your script. To prevent this, use the following
method:

<font color="darkblue">`MORE = <EVAL <`**`TAG0`**`.JOE>>`  
</font>

In this case we have used TAG**0** to access the TAG value. Accessing
the TAG in this manner will return the value as normal, except for when
TAG.JOE is undefined a "0" will be returned rather than a script error
being raised.

The same trick can also be used when setting the value of a TAG. For
example:

<font color="darkblue">`TAG0.JOE = <MORE>`  
</font>

As you may expect, this sets the value of TAG.JOE to whatever value is
held in MORE. The difference however is that because we have used TAG0
when setting the value, if the value of MORE is zero then TAG.JOE will
actually be cleared! This may initially sound undesirable but it offers
the benefit of reducing the number of TAGs stored on the object. Since
we can use TAG0 to retrieve a value of zero when a tag doesn't exist
then you may be wasting memory by storing a large number of TAGs all
with a value of zero. Of course if you do decide to use TAG0 when
setting the value of a TAG then you should ensure that you also use TAG0
when reading that value back, or else you will quickly run into the
aforementioned "Undefined value" script error.

## CTags

CTAGs are temporary versions of TAGs that are only available with
objects (i.e. online player characters). CTAGs are not saved and will be
cleared when the player logs out. This means that you don't have to
worry about removing the tag after using it, assuming the player logs
out one day :). You can use CTAG0 too, used just the same as you can
with TAG0. In short, if you are going to use tags that will no longer be
needed after logging out, it is probably a good idea to consider using a
CTAG.

**Note:** CTAG can only be used with online players. Attempting to read
from or write to a CTAG on a logged out player *will* raise a script
error.

## Useful TAG/CTAG Functions

|  |  |
|----|----|
| CLEARTAGS | Removes all TAGs on an object, eg SRC.CLEARTAGS. Be careful with this as once the tag is gone there is no way to get it back. |
| CTAGLIST | Displays a list of tags on a client to SRC. |
| CTAGLIST LOG | Displays a list of tags on a client to the Sphere console (but not into logfile). |
| TAGAT.x.KEY | Returns the name of the TAG at position x. (the first TAG is at position 0) |
| TAGAT.x.VALUE | Returns the value of the TAG at position x. (the first TAG is at position 0) |
| TAGCOUNT | This function returns the number of TAGs on an object. |
| TAGLIST | Displays a list of tags on an object to SRC. |
| TAGLIST LOG | Displays a list of tags on an object to the Sphere console (but not into logfile). |

## Vars

Perhaps you're wondering if there is a less memory-consuming method. Of
course you were, don't deny it.

And here I present it to you:

<font color="darkblue">`VAR.CHEESE = 1`  
</font>

Important VAR principles:

1.  Like TAGs, VARs are always stored as strings.
2.  Unlike TAG, VARs are not attached to any particular object. You
    never EVER use \[obj\].VAR.BLAH.
3.  VAR variables are GLOBAL, meaning they can be accessed from any
    script.
4.  Never assume a VAR has a specific value stored at the beginning of
    an event, especially if the same VAR is used in multiple scripts.
5.  Like TAGs, VARs can have any name. VAR.CHEESE, VAR.BLAH,
    VAR.WORLD_TIME, VAR.HELLO_WORLD
6.  If you don't need a value to be permanent, but need a place to store
    it temporarily during a script, use LOCAL, not TAG, not VAR.

VARs are global TAGs. That's about it.

If you want to get list of all VARs on your server type (into client or
console): **SERV.VARLIST**, and if you want to log them into console
write **SERV.VARLIST LOG** (this will not be saved into logfile).

If you want to remove all server variables (VARs) type
**SERV.CLEARVARS**.

And that's your entire lesson on the VAR feature. I told you it would be
short. As with TAG0 and CTAG0, you can also do VAR0. It works just like
TAG0 or CTAG0 does. If that variable has no value then VAR0 will return
0 instead of nothing.

## Locals

LOCALs are like VARs except they are only accessible within the script
block they are defined in (i.e. a function or trigger) and then they are
immediately cleared. The advantage is that they are much faster than
VARs and you also don't have to worry about different scripts
interfering with each other.

The following script demonstrates why you may want to use a LOCAL rather
than a VAR:

<font color="darkblue">`[FUNCTION f_var_joe]`  
`VAR.NAME = Joe`  
`F_VAR_BOB`  
`SYSMESSAGE <VAR.NAME>`  
`RETURN`  
  
`[FUNCTION f_var_bob]`  
`VAR.NAME = Bob`  
`SYSMESSAGE <VAR.NAME>`  
`RETURN`  
</font>

The idea with the two functions above is that F_VAR_JOE will show the
message "Joe" and F_VAR_BOB will show the message "Bob". However, if you
were to go ingame and type **.F_VAR_JOE**, you would receive two
messages saying "Bob". Why is this?

Well, if you look closely at F_VAR_JOE you will see that after setting
VAR.NAME to Joe, it then executes the function F_VAR_BOB and inside
F_VAR_BOB we then set VAR.NAME to Bob. Because VARs are global
variables, this inadvertently affects the behaviour of F_VAR_JOE and we
don't get the output that we were after. Another flaw you may have not
spotted with this script is that we haven't cleared VAR.NAME before the
script ends and so Sphere still has VAR.NAME stored in memory (which in
this particular case is a waste of resources as we have no further use
for VAR.NAME).

In this particular scenario we could modify the functions to use
different VAR names but unless we intend to manually check every script
on the server we could easily end up using a VAR that another script is
using and prevent that from working instead.

This is where the LOCAL comes in to play, see the following example:

<font color="darkblue">`[FUNCTION f_local_joe]`  
`LOCAL.NAME = Joe`  
`F_LOCAL_BOB`  
`SYSMESSAGE <LOCAL.NAME>`  
`RETURN`  
  
`[FUNCTION f_local_bob]`  
`LOCAL.NAME = Bob`  
`SYSMESSAGE <LOCAL.NAME>`  
`RETURN`  
</font>

The above functions are identical to the previous ones, except they use
LOCAL instead of VAR. This time when you type **.F_LOCAL_JOE** ingame
you will receive "Joe" and "Bob" messages as we originally intended.

This is because the LOCALs only exist within the functions that define
them. When F_LOCAL_BOB attempted to use LOCAL.NAME it received its own
version of the variable that doesn't interfere with the one defined in
F_LOCAL_JOE. When F_LOCAL_BOB returns, F_LOCAL_JOE still has its
original LOCAL.NAME with "Joe" still stored inside it.

Of course there may come a time where you *do* want to share LOCALs with
another function, and this can be accomplished by using the **CALL**
command. When you use the CALL command to run a function instead of
running the function directly the LOCALs are shared between both
scripts, for example:

<font color="darkblue">`[FUNCTION f_bla]`  
`LOCAL.DUDE = Bob`  
`RETURN`  
  
`[FUNCTION f_bleep]`  
**`CALL F_BLA`**  
`NAME = <LOCAL.DUDE>`  
`RETURN`  
</font>

When we run the **F_BLEEP** function above, the CALL line allows
LOCAL.DUDE to be set in F_BLA and be accessible to F_BLEEP afterwards.
Therefore, the `NAME = <LOCAL.DUDE>` line will set the name of the
object to whatever the F_BLA function set LOCAL.DUDE to (in this case
"Bob").

Unlike TAGs, CTAGs and VARs, LOCALs *do not* have a LOCAL0 equivalent.
This is because LOCALs will always return 0 when they empty (and so,
they can *never* be blank/empty).

## Floats

This is the most simple. Since you know many variables at this point and
know how to use them. FLOATs are almost the same as LOCALs, just a
difference. LOCALs store only text or entire numbers (34 or 12), while
FLOATs stores decimals (23.1 or 45.3). Another difference is the EVAL
here is changed to FLOATVAL. This is one example of FLOAT used to
calculate hit speed:

<font color="darkblue">`[EVENTS e_test]`  
`ON=@HitTry`  
`:FLOAT.FSPEED = <FLOATVAL <SERV.SPEEDSCALEFACTOR> / ((<DEX> + 100) * <ARGO.SPEED> + 1)>`  
`:ARGN1 = <FLOAT.FSPEED>`  
</font>

## Functions

What's your \[FUNCTION\]?

The single most powerful SPHERE scripting tool to date.

You have a wealth of built-in object functions available to you.
However, there seems to be some limits. For example, let's take a look
at the following example of a very poorly written script:

<font color="darkblue">`ON=@DClick`  
`:SERV.NEWITEM=ispell_7_water_sparkle`  
`:NEW.P = <SRC.TARG.P>`  
`:NEW.LINK = <SRC.UID>`  
`:NEW.MORE = 017a6`  
`:NEW.MOVE -1 -1`  
`:SERV.NEWITEM = ispell_7_water_sparkle`  
`:NEW.P = <SRC.TARG.P>`  
`:NEW.LINK = <SRC.UID>`  
`:NEW.MORE = 017a3`  
`:NEW.MOVE -1 0`  
`:SERV.NEWITEM = ispell_7_water_sparkle`  
`:NEW.P = <SRC.TARG.P>`  
`:NEW.LINK = <SRC.UID>`  
`:NEW.MORE = 017a8`  
`:NEW.MOVE -1 1`  
`:SERV.NEWITEM = ispell_7_water_sparkle`  
`:NEW.P = <SRC.TARG.P>`  
`:NEW.LINK = <SRC.UID>`  
`:NEW.MORE = 0179f`  
`:NEW.MOVE 0 -1`  
`:SERV.NEWITEM = ispell_7_water_sparkle`  
`:NEW.P = <SRC.TARG.P>`  
`:NEW.LINK = <SRC.UID>`  
`:NEW.MORE = 0179b`  
`:NEW.MOVE 0 0`  
`:SERV.NEWITEM = ispell_7_water_sparkle`  
`:NEW.P = <SRC.TARG.P>`  
`:NEW.LINK = <SRC.UID>`  
`:NEW.MORE = 017a1`  
`:NEW.MOVE 0 1`  
`:SERV.NEWITEM = ispell_7_water_sparkle`  
`:NEW.P = <SRC.TARG.P>`  
`:NEW.LINK = <SRC.UID>`  
`:NEW.MORE = 017a5`  
`:NEW.MOVE 1 -1`  
`:SERV.NEWITEM = ispell_7_water_sparkle`  
`:NEW.P = <SRC.TARG.P>`  
`:NEW.LINK = <SRC.UID>`  
`:NEW.MORE = 0179d`  
`:NEW.MOVE 1 0`  
`:SERV.NEWITEM = ispell_7_water_sparkle`  
`:NEW.P = <SRC.TARG.P>`  
`:NEW.MORE = 017a7`  
`:NEW.LINK = <SRC.UID>`  
`:NEW.MOVE 1 1`  
`:RETURN 1`  
</font>

Do you notice anything about this script? How about the fact that it's
repeating the same few lines over and over? Do you think we could do
anything to fix this problem? I thought so too. We need a way to write a
set of code once, like this:

<font color="darkblue">`SERV.NEWITEM = ispell_7_water_sparkle`  
`NEW.P = <SRC.TARG.P>`  
`NEW.MORE = 017a7`  
`NEW.LINK = <SRC.UID>`  
`NEW.MOVE 1 1`  
</font>

And have a way to "call" this code over and over again. I give you....
the \[FUNCTION\]!

<font color="darkblue">`[FUNCTION create_sparkle]`  
`SERV.NEWITEM = ispell_7_water_sparkle`  
`NEW.P = <TARG.P>`  
`NEW.MORE = 017a7`  
`NEW.LINK = <UID>`  
`NEW.MOVE 1 1`  
`:RETURN`  
</font>

And in a script, we could go like this:

<font color="darkblue">`ON=@DClick`  
`:SRC.CREATE_SPARKLE`  
`:SRC.CREATE_SPARKLE`  
`:SRC.CREATE_SPARKLE`  
`:SRC.CREATE_SPARKLE`  
`:SRC.CREATE_SPARKLE`  
`:SRC.CREATE_SPARKLE`  
`:SRC.CREATE_SPARKLE`  
`:SRC.CREATE_SPARKLE`  
`:RETURN 1`  
</font>

Once you have learned how to use FOR loops, you could also reduce this
script even further to:

<font color="darkblue">`ON=@DClick`  
`:FOR 8`  
`::SRC.CREATE_SPARKLE`  
`:ENDFOR`  
`:RETURN 1`  
</font>

Doesn't that look slightly more pretty than the previous version? We
managed to cut about 40 lines down into 3 or so. But do you notice a
problem? Our code is fixed. Those items are going to be created and
moved 1 square down and one square right, every single time. We need a
way to specify some parameters to our function!

And so we have the ARG\* commands. There are three types of arguments we
can give to a function: numeric, string, or object. I recommend always
using the string arguments and using EVAL to get whatever else you need.
What variables are associated with these arguments?

ARGN, ARGS, and ARGO respectively. N for "number", S for "string" and O
for "object".

Let's rewrite our function and event using this new information:

<font color="darkblue">`[FUNCTION create_sparkle]`  
`SERV.NEWITEM = ispell_7_water_sparkle`  
`NEW.P = <TARG.P>`  
`NEW.MORE = 017a7`  
`NEW.LINK = <UID>`  
`NEW.MOVE <ARGS>`  
  
`[SOME ITEMDEF GOES HERE]`  
  
`ON=@DClick`  
`:SRC.CREATE_SPARKLE -1 -1`  
`:SRC.CREATE_SPARKLE -1 0`  
`:SRC.CREATE_SPARKLE -1 1`  
`:SRC.CREATE_SPARKLE 0 -1`  
`:SRC.CREATE_SPARKLE 0 1`  
`:SRC.CREATE_SPARKLE 1 -1`  
`:SRC.CREATE_SPARKLE 1 0`  
`:SRC.CREATE_SPARKLE 1 1`  
`:RETURN 1`  
</font>

Get it? Every time we call the function with our new *create_sparkle*
command, we "pass" it the values following the command. SPHERE
automatically puts those values in ARGS, without any help from us.

There is another problem with functions that many new scripters do not
understand, and that is the concept of the default object. In a normal
script, the default object is the object on which the script is being
executed. In a @DClick script, it's the item being double-clicked. In an
@Equip script, it's the item being equipped. But what are the objects
available in a function. Well, it all depends on how you call it.

The default object in a function is the object that called the function.
In the case of our above example, SRC called the function, so the SRC
becomes the default object. You'll notice that I removed any mention of
SRC from the lines inside of the function itself. We could easily have
said this instead:

<font color="darkblue">`CREATE_SPARKLE`  
</font>

Then, the default object would have been the item and SRC would still be
SRC. But its a lot easier to see it the other way, at least in my
opinion. That way you don't get confused either. If you WERE to include
the SRC, and accidentally call your function with something like this:

<font color="darkblue">`SRC.ACT.CREATE_SPARKLE // Not a really likely occurrence in this case, but in other cases it is`  
</font>

Then you would no longer have a SRC and you would get a lot of scary
errors that would be kinda difficult to track down, since you probably
wouldn't think to check the function call. Functions generate enough
scary errors as it is when you screw them up. Don't make it worse. :)

There is still another problem with my script. It's assigning the same
MORE value to each of the newly created items, and as you can see from
the original long script, this isn't what I wanted it to do. I wanted
each item to have a specific MORE value, which is used elsewhere in the
script. So what are we to do? Well there are a number of solutions, but
the most obvious would be to utilize that VAR feature we discussed in
the previous section. Let's take a look at the completed script:

<font color="darkblue">`[FUNCTION create_sparkle]`  
`SERV.NEWITEM = ispell_7_water_sparkle`  
`NEW.P = <TARG.P>`  
`NEW.MORE = <EVAL <VAR.MORE_VALUE>>`  
`NEW.LINK = <UID>`  
`NEW.MOVE <ARGS>`  
  
`[SOME ITEMDEF GOES HERE]`  
  
`ON=@DClick`  
`:VAR.MORE_VALUE = 017a6`  
`:SRC.CREATE_SPARKLE -1 -1`  
`:VAR.MORE_VALUE = 017a3`  
`:SRC.CREATE_SPARKLE -1 0`  
`:VAR.MORE_VALUE = 017a8`  
`:SRC.CREATE_SPARKLE -1 1`  
`:VAR.MORE_VALUE = 0179f`  
`:SRC.CREATE_SPARKLE 0 -1`  
`:VAR.MORE_VALUE = 017a1`  
`:SRC.CREATE_SPARKLE 0 1`  
`:VAR.MORE_VALUE = 017a5`  
`:SRC.CREATE_SPARKLE 1 -1`  
`:VAR.MORE_VALUE = 0179d`  
`:SRC.CREATE_SPARKLE 1 0`  
`:VAR.MORE_VALUE = 017a7`  
`:SRC.CREATE_SPARKLE 1 1`  
`:VAR.MORE_VALUE =`  
`:RETURN 1`  
</font>

The value of the VAR is carried over, since VAR variables, as we know,
are global. We've managed to reduce a 40 line script into a 20 line
script and keep the original functionality. And this is only for calling
a function 8 times. The more you use a function, the more space it saves
later.

And that is my chapter on functions. Later on, we'll see very useful
purposes for doing this, other than eliminating a lot of lines of
typing.

[Category:Tutorials](Category:Tutorials "wikilink")
