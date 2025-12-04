*Occam's Razor
By Taran*

Occam's Razor is a philosophical precept first stated by the controversial but brilliant philosopher and monk William of Occam (orOckham) during the 14th century. It is widely used in scientific investigation and philosophical debate. It has also taken a number of
```
forms over the years.

The most commonly used form is, "All things being equal, the simplest explanation is to be preferred." It does not mean that the simplest explanation is correct, merely preferred. More experimentation and proof is necessary to demonstrate the correctness of the more complex explanation, but it does happen. In physics, Newton's theory of motion (F=ma) is far simpler than Einstein's more complex, but more correct, theory of relativity.

However, this is not the way in which the original statement was written by William. In Latin, he wrote, "Pluralitas non est ponenda sine neccesitate." This is translated literally as "Plurality should not be posited without necessity," or sometimes as "Entities should not be multiplied unnecessarily." It is this last translation we shall be examining as it applies to scripting and to programming in general.

In the case of SPHERE, the entities are the aspects of your script. They include the variables, methods, and tricks you use to accomplish your goal. Occam's Razor suggests that you should not use any more of these entities than you absolutely need to use. Unfortunately, many beginning scripters who haven't realized how much you can really do with the UO scripting language will try to multiply these entities without any need to do so.

I was talking to a scripter last night on ICQ, when he asked me about a script which looked something like the following:

\[ITEMDEF i_first_item\] ID=i_something

ON=@DClick

`   // If we've already used the item, don't`
`   // let them use it again until their`
`   // timer expires.`
`   IF (<SRC.TAG0.USEDONCE> == 1)`
`       SRC.SYSMESSAGE You already used this item once.`
`       RETURN 1`
`   ELSE`
`       SRC.SYSMESSAGE You equip the time`
`       SERV.NEWITEM i_timer_item`
`       NEW.EQUIP`
`       SRC.TAG.USEDONCE = 1`
`       RETURN 1`
`   ENDIF`
`   RETURN 1`

\[ITEMDEF i_timer_item\] ID=i_memory TYPE=t_eq_script

ON=@Create

`   TIMER = some_number`

ON=@Timer

`   CONT.SYSMESSAGE Your timer has expired!`
`   // Do some stuff here`
`   CONT.TAG.USEDONCE = 0`
`   REMOVE`
`   RETURN 1`

The violation of Occam's Razor in this script is not immediately obvious. However, upon closer examination it seems that we have a TAG that is not really necessary. This tag stores a value to determine whether the timer item still exists on the player. When the timer item decays, it sets the TAG back to zero, so that the player can use the i_first_item again.

Think about this. If the item is on the player, can't we merely check that the item still exists? Wouldn't using FINDID to determine whether the player has the item be simpler than using a TAG along with that item? In this case, it would also reduce the likelihood that this script conflicts with other scripts, which might also use a TAG.USEDONCE. (Naming your tags creatively in each system is usually important towardavoiding conflicts.)

A few other violations of Occam's Razor appear in this script. First, there are too many RETURN statements. In this case, it doesn't matter, but in other scripts you might have unforeseen effects. Since both parts of the IF statement return 1, we could simply move it to the end of the script, where it will execute regardless of how the IF evaluates. However, my preferred method is to take care of all exceptional cases at the start, so that the rest of the script will execute cleanly without as many conditionals. In this case, the exceptional status is when the player has his timer item and cannot get another. We will have two RETURN statements instead of one, but this is not a violation of Occam's Razor because speed is also a necessity in a script, and the faster we get out of any script, the better our server will run.

An improved version of this script might look as follows:

\[ITEMDEF i_first_item\] ID=i_something

ON=@DClick

`   // Handle all exception cases.`
`   // Check the UID of the item to see if it exists. If not, this`
`   // will return 0 and so the IF statement will evaluate as false.`
`   IF (<SRC.FINDID.i_timer_item.UID>)`
`       SRC.SYSMESSAGE You already used this item once.`
`       RETURN 1`
`   ENDIF`

`   // Execute the "true" case, which is what we'd like to do`
`   // if nothing went wrong.`
`   SRC.SYSMESSAGE You equip the timer`
`   SERV.NEWITEM i_timer_item`
`   NEW.EQUIP`
`   RETURN 1`

\[ITEMDEF i_timer_item\] ID=i_memory TYPE=t_eq_script

ON=@Create

`   TIMER = some_number`

ON=@Timer

`   CONT.SYSMESSAGE Your timer has expired!`
`   // Do some stuff here`
`   REMOVE`
`   RETURN 1`

So you see, by applying Occam's Razor to our script, we have shortened it and removed an unnecessary TAG.

This principle is even more important when applied to the content of user-defined functions, those fun bits of code inside of \[FUNCTION\] blocks. I have seen so many functions which contain unnecessary code. In this case, such code generally restricts the re-usability of a function, so that you can use it in one or maybe two places, but then are required to alter it or write a new function for a third extremely similar case. Even some of the built-in functions contain unnecessary code which definitely hinders the scripting ability.

Last night, I was experimenting with the built-in BUY and SELL functions of NPCs. I discovered that both functions have a built-in distance check, where an NPC will not respond to you if he is a particular distance away. This distance check is completely unrelated to any sort of buying and selling. If you want to check distance, do it in a script, such as:

ON=\*buy\*

`   IF (`<DISTANCE>` < 15)`
`       BUY`
`   ENDIF`

This way, not only can you modify the distance if you wish, but you can also buy from incredibly large distances. It would be slightly (but notmuch) better if all functions had such a restriction, but other NPC-related functions are not affected by distance. So, we have a restriction that not only is entirely unrelated to the problem, but also hinders our ability to script particular things, such as an NPC who can respond to this type of request over long distances. Certainly, we can script a function which brings the NPC to our position, executes the BUY or SELL function, and puts him back where he was, but that is unnecessarily complication. If we want a distance check in some cases, the complication should appear in THOSE cases, not the cases where we simply want to BUY or SELL something.

I have seen many functions which impose unnecessary restrictions upon their execution. For instance, let's look at this incredibly simple script whose entire purpose is to give the player two named swords when he double-clicks another item.

\[ITEMDEF i_named_sword_dispenser\] ID=1828 // A runic tile TYPE=t_script

ON=@DClick

`   GIVE_NAMED_SWORD doom`
`   GIVE_NAMED_SWORD fire`
`   RETURN 1`

\[FUNCTION give_named_sword\] SERV.NEWITEM i_sword_viking // Set the name to the original name, plus "of something," where something is // whatever we passed as an argument to the function (in our case, "doom"or // "fire"). We'll end up with "viking sword of doom" or "viking sword of fire". NEW.NAME \<NEW.NAME\> of <ARGS> // Put it in their backpack SRC.BOUNCE \<NEW.UID\>

Can you see the problem with this script? It certainly will work and the player will end up with a sword of doom and a sword of fire in their backpack when they double-click the dispenser. We've used a function to save ourselves some typing and allow us to easily change the names of the dispensed swords. However, our function is needlessly complex. That is, it violates our Occam's Razor principle of using the simplest method possible to perform an action. Which part of our function is unnecessary?

Well, for one, the SRC is unnecessary. We would be better to remove the SRC from all statements in the function, because it is not necessary. If we call the function as SRC.GIVE_NAMED_SWORD, the SRC will be the default object in the function. The SRC will still receive the necessary items, but now our function is no longer complicated by that restriction. What restriction, you may be asking? Well, take a look at the following script. Imagine that the above function is included.

\[ITEMDEF i_target_sword_dispenser\] ID=1828 // A runic tile TYPE=t_script

ON=@DClick

`   TARGET Who to provide with weapons?`
`   RETURN 1`

ON=@Targon_Char

`   // Give our target viking swords of fire and ice.`
`   SRC.TARG.GIVE_NAMED_SWORD fire`
`   SRC.TARG.GIVE_NAMED_SWORD ice`
`   RETURN 1`

Make one of these items, double-click it, and target someone else (notyourself). If no one else is on your server, target an NPC, and then inspect his backpack. Instead of ending up in the targeted character's backpack, the swords have mysteriously arrived in your own backpack. This is the result of our over-complication of the script. We have restricted it so that it will ONLY work for the SRC. No matter who invokes the function (SRC.TARG or anything else), it will always act upon the SRC. This could be disasterous in @Timer, where there is no useful SRC.

So, we can remove SRC from the function, combine our three scripts, and have the following:

\[ITEMDEF i_named_sword_dispenser\] ID=1828 // A runic tile TYPE=t_script

ON=@DClick

`   GIVE_NAMED_SWORD doom`
`   GIVE_NAMED_SWORD fire`
`   RETURN 1`

\[ITEMDEF i_target_sword_dispenser\] ID=1828 // A runic tile TYPE=t_script

ON=@DClick

`   TARGET Who to provide with weapons?`
`   RETURN 1`

ON=@TargOn_Char

`   // Give our target viking swords of fire and ice.`
`   SRC.TARG.GIVE_NAMED_SWORD fire`
`   SRC.TARG.GIVE_NAMED_SWORD ice`
`   RETURN 1`

\[FUNCTION give_named_sword\] SERV.NEWITEM i_sword_viking NEW.NAME \<NEW.NAME\> of <ARGS> NEW.CONT \<FINDLAYER.layer_backpack.UID\>

Notice that I'm setting the CONT of the new item instead of using the BOUNCE function. This is because BOUNCE will always place the items in the backpack of the SRC, which is not what we want. Instead, I set CONT (the container reference) to the UID of the default object's backpack. I retrieve that UID using the FINDLAYER reference with layer_backpack as an argument.

Now, we have a simpler function which can be used in many places instead of a needlessly complicated function which can be used in one place.

Essentially, a function should perform exactly one task, and not perform other tasks which may or may not be related to that task. Distance/line-of-sight checking is a common unrelated feature people place into their functions. However, like with the built-in BUY and SELL, chances are, you'll need different functionality one day, and it's better to insert distance checks where you need them, instead of using workarounds where you don't.

The following are things which people like to include in their functions, which should NOT be included in their functions:

1.  Extra RETURN statements
2.  SRC references or SRC-specific commands (such as BOUNCE and DIALOG)
3.  Extra conditionals (too many IFs) and unnecessary TAGs
4.  Events (syntax error)
5.  Messages/Sysmessages which are not appropriate in all situations
6.  Mixing of SRC and non-SRC functions (I see this all the time)
7.  Using INVUL or INVIS to change the player's invisibility state
8.  Using enormously complex storage methods for fear that TAGs will
    cause lag
9.  Use of complex IF statements instead of using TRY or TRYP
10. Use of EVAL where unnecessary

Simple is almost always better. Do not do things which are unnecessary to achieve your goal.

And remember the following stages of scripting:

1.  Make it work - That is, make it do something similar to what you
    want it to do
2.  Make it work RIGHT - Debug all of the little mistakes
3.  Make it work FAST - Not always necessary. I could post an article on
    [optimization](Optimization "wikilink") some other time.

[Category: Articles](Category:_Articles "wikilink")
```
