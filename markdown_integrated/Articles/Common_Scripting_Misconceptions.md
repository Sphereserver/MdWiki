*0r, st00pid th1ngs n00bs d0?!?!?!/1/1/1*  
*By Taran*

## CHARDEF blocks must use a number

This is simply not true, and certainly not recommended. I highly
recommend that scripters use a DEFNAME instead of a new number. For
example, instead of this:

<spherescript>\[CHARDEF 04000\] DEFNAME=c_scary_man ID=c_man
...</spherescript>

You can just as easily do this:

<spherescript>\[CHARDEF c_scary_man\] ID=c_man // 0190 would work here
just as easily, since c_man = 0190 ...</spherescript>

So, you see, you can simply including a DEFNAME in the definition for
the creature. SPHERE will assign it some sort of internal number. You
don't want to worry about that sort of thing. If you REALLY want to see
what the number is, you can always use the following function:

<spherescript>\[FUNCTION examine_id\] // Usage: examine_id
<id_to_examine> // Example: examine_id c_man SYSMESSAGE \<EVAL
<ARGS>\></spherescript>

But then again, why would you want to? The entire idea behind the
DEFNAME feature is that there is no need for you to memorize those scary
numbers. Remember [Chapter 1](Chapter_1 "wikilink")? :)

## Bodies and colors revert upon death

This is an easy one. Simply set OBODY and OSKIN along with BODY and
COLOR. The player will assume his OBODY/OSKIN upon resurrection.

## IF does not require an ENDIF

All IF blocks require an ENDIF. At best, they won't work correctly. At
worst, they won't work at all. Let's look at an example:

<spherescript>\[FUNCTION superdude\] IF ( <STR> \< 100 ) STR = \<EVAL
<STR> + 2000\> IF ( <DEX> \< 100 ) DEX = \<EVAL <DEX> + 2000\> IF (
<INT> \< 100 ) INT = \<EVAL <INT> + 2000\></spherescript>

As you can see, this is a rather silly function which does nothing
except set a player's strength, dexterity, and intelligence up by 2000
points. The idea is that a stat is only modified if that stat is below
100. Can anyone spot the error? Let's see how SPHERE reads this script.
This is why it's good to indent your scripts anyway:

<spherescript>\[FUNCTION superdude\] IF ( <STR> \< 100 )

`  STR = <EVAL `<STR>` + 2000>`  
`  IF ( `<DEX>` < 100 )`  
`     DEX = <EVAL `<DEX>` + 2000>`  
`     IF ( `<INT>` < 100 )`  
`        INT = <EVAL `<INT>` + 2000>`  
`     ENDIF`  
`  ENDIF`

ENDIF</spherescript>

This is definitely NOT the result we wanted. As you can see, we could
fix this by simply adding ENDIF statements to the original function.

<spherescript>\[FUNCTION superdude\] IF ( <STR> \< 100 )

`  STR = <EVAL `<STR>` + 2000>`

ENDIF IF ( <DEX> \< 100 )

`  DEX = <EVAL `<DEX>` + 2000>`

ENDIF IF ( <INT> \< 100 )

`  INT = <EVAL `<INT>` + 2000>`

ENDIF</spherescript>

## SRC is required in functions

Absolutely NOT! In fact, it's probably a bad idea to use the SRC
reference in a function unless you're absolutely sure that you want to
reference the SRC all of the time. Example time! We'll make a function
that damages the SRC:

<spherescript>\[FUNCTION fire_damage\] // The purpose of this function
is to cause damage // along with a spectacular flamestrike effect
SRC.EFFECT 3,i_fx_fire_column,1,16,0 SRC.DAMAGE \<EVAL {20
25}\></spherescript>

So what's wrong with this? If we use it by saying SRC.FIRE_DAMAGE, there
is absolutely nothing wrong with it! However, what if we want to use
this function on someone other than the SRC? Let's say we make a cursed
shield that damages its bearer after a certain timer. Our @Timer event
might look something like this:

<spherescript>ON=@Timer

`   CONT.FIRE_DAMAGE // Call the function on the CONT`  
`   RETURN 1 // Don't let the item decay`</spherescript>

What happens now? Well, when we execute the FIRE_DAMAGE function on an
object, that object (CONT in this case) becomes the default object
inside of the function. That is, it's the item we refer to without any
sort of object reference. (Like \<STR\> or \<RESTEST 10 i_gold\>,
instead of \<SRC.STR\> or \<CONT.RESTEST 10 i_gold\>.) However, inside
of the function, we're doing all of the damage and pretty effects to the
SRC object. We're in an @Timer event. Can anyone tell me the cardinal
rule of @Timer events? That's right. There is no SRC object. And what if
we were in another event which has a SRC, but that SRC object was not
the player we wanted to affect? As you can see, it's much better to
remove SRC from functions unless it's absolutely necessary. Here's our
new and improved function:

<spherescript>\[FUNCTION fire_damage\] // The purpose of this function
is to cause damage // along with a spectacular flamestrike effect EFFECT
3,i_fx_fire_column,1,16,0 DAMAGE \<EVAL {20 25}\></spherescript>

We've removed all references to SRC from the function. Therefore, we can
call this using ANY object reference we want, including the example
above with CONT. There is one more thing to consider when doing anything
of this nature. One of the functions we call inside of our fire_damage
function depends on a SRC in its default state. Yes, it's the DAMAGE
function. See the [Reference
Compendium](Reference_Compendium "wikilink") for information about how
you might solve that problem.

I've been mentioning cases when SRC may be required in a function. I can
only think of one where it's absolutely necessary, and one where it
might be useful. Can you figure out what they are? Well, too late if you
didn't:

1.  When you call an in-game function, SRC is always the person who
    called the function and the default object is the object you
    executed it on. For example, if you type .FIRE_DAMAGE, you will be
    executing the function on yourself, so you will be both the SRC and
    the default object. However, if you type .xFIRE_DAMAGE and target
    someone, you will be the SRC and that person will be the default
    object.
2.  When you are absolutely certain that you want to reference the SRC
    in a function. I don't know when this might be, but you might find
    it necessary.

[Category: Articles](Category:_Articles "wikilink")
