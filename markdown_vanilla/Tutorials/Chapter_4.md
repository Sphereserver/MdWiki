## Introduction to Objects

Your first glimpse of real scripting!

First and foremost, you MUST understand the object structure of the SPHERE system. Now, because SPHERE interacts with something visible, most of these objects are relatively easy to understand. But first, you must understand this simple fact about object-oriented programming (aterm I'm sure all you programmers havel come to know and fear):

**OBJECT-ORIENTED SCRIPTING IS CENTERED AROUND OBJECTS.**

Duh.

Actually, it isn't as "Duh" as you may think. Here is a list of the objects available to you in a SPHERE script:

| **Who** | **What** |  |
| --- | --- | --- |
| SRC | The **"source"** of an event. If an item is damaged, the SRC is whatever damaged it. If a player is hit, the SRC is whoever hit the player. If an item is double-clicked, the SRC is the player who double-clicked it. The ONLY event that does not have a SRC, as we shall see later, is @Timer, for good reasons. Note that usually on functions the SRC isn't always the one who called the functions, but the default object (I or just an empty thing, eg: &lt;I.NAME&gt; or &lt;NAME&gt; are the same thing. |  || ACT | The last object acted upon by the referenced character, for example on that char trigger @ItemDclick, ACT is the item the player double-clicked. |  |
| TARG | The object targetted by the character. |  |
| CONT | The container of the object. |  |
| TOPOBJ | If an object is buried in several containers within containers, this is always the top-level container before you get to the world. If an item is buried in a player's backpack, TOPOBJ is the player. |  |
| ACCOUNT | The account of a player, obviously. |  |
| REGION | The current region/area a player is in. |  |
| SECTOR | The world is divided into 64 by 64 tile sectors (by default but you can change it by setting the MAPx settings (look at sphere.ini section for this)). This is the player's current sector. |  |
| SERV | used to call server commands, like serv.save, serv.allclients, etc. **Object references from SERV** <table> LASTNEWITEM | The last item created from NEWITEM/NEWDUPE functions. |
| LASTNEWCHAR | The last character created by NEWNPC/NEWDUPE functions. |  |</td>
</tr> <tr> <td><p>LINK</p></td> <td><p>The object referred to in the LINK property of an **item**.</p></td> </tr> <tr> <td><p>UID.x</p></td> <td><p>The object with UID equal to X.</p></td> </tr> <tr> <td><p>FINDLAYER.X</p></td> <td><p>The object in layer X.</p></td> </tr> <tr> <td><p>FINDCONT.X</p></td> <td><p>The xth object in the container referenced.</p></td> </tr> <tr> <td><p>FINDID.x</p></td> <td><p>The first object with ID of x in the container.</p></td> </tr> <tr> <td><p>FINDTYPE.x</p></td> <td><p>The first object with TYPE of X in the container.</p></td> </tr> <tr> <td><p>NEW</p></td> <td><p>The newer object created from NEWITEM/NEWNPC/NEWDUPE functions.</p></td> </tr> <tr> <td><p>OBJ</p></td> <td><p>An empty object variable, which you need to set to use, eg:</p> <p><font color="darkblue">`OBJ = &lt;FINDLAYER.`**`layer_bankbox`**`&gt;`<br /> `OBJ.SAY HEHE`<br /> </font></p> <p>will make I's bank box say hehe.<br /> **NOTE**: OBJ is a global variable so it can possibly interfere with other scripts.<br /> It's best to set it back to nothing when not in use in a certain script.</p></td> </tr> <tr> <td><p>REFx</p></td> <td><p>This works in the same way as OBJ except the reference is local and will not interfere with other scripts. 'x' is a number between 1 and 65535, allowing you to reference as many objects as you need simultaneously (e.g. REF1 = &lt;FINDLAYER.layer_bankbox&gt;).</p></td> </tr> <tr> <td><p>FILE</p></td> <td><p>Call the file commands on the current FILE object.</p></td> </tr> <tr> <td><p>DB</p></td> <td><p>See [MySQL](MySQL)</p></td> </tr> <tr> <td><p>PARTY.MEMBER.x</p></td> <td><p>The xth party member of the referenced party.</p></td> </tr> <tr> <td><p>GUILD.MEMBER.x</p></td> <td><p>The xth guild member of the referenced guild.</p></td> </tr> </tbody> </table>

As you can see, we're rather limited in what we can do! Actually, not really. With the current scripting system, you can do almost anything imaginable with SPHERE. It might run slow or be laggy, but it can be done. Those last five events (the ones with the x in them) are complex and I don't expect you to know how to use them yet.

Now that we know the objects, we need to know how to access the properties of those objects, and above all, do things to those objects. We use the dot operator (.) to access properties of objects. For example:

<font color="darkblue">``SRC.STR``
`ACT.MOREP`
``SRC.ACT.MOREP``
``SRC.TARG.HITS``
``SRC.DAMAGE` {1 5} 01 <ACT>`
``SERV.NEWITEM` i_gold`
``NEW.AMOUNT` 10000`
``SRC.TARG.KILL``
`CONT.KILL`
`FINDLAYER.layer_backpack.FINDID.i_gold.AMOUNT`
</font>

I don't expect you to understand what all of these things do yet, but you will by the end of this chapter.

**Some notes**: You must also understand that OBJECTS aren't ITEMS, when someone say OBJECT they probably mean a character/item/some of those in the table. The objects can also be called REFERENCE, for example, ACT.STR 100 the reference is ACT.

Here is the next principle of SPHERE scripting:

**ALL ACTIONS ARE TRIGGERED BY EVENTS OR FUNCTIONS, WHICH DEFINE THE OBJECTS**

Nothing happens in a SPHERE script that just sits there. A player, or something else in the game, must do something to an item or a character
```
for a script to execute. For example, being hit executes the @GetHit script on the person being hit, and @Hit on the hitter. Stepping on an item executes the @Step script on the item and the @ItemStep script on the player. When an item is double-clicked, @DClick is executed on the item and @ItemDClick is executed on the player.

If the player is the one who double-clicks the ITEM, he becomes SRC. If he targets an item, in the @Targon_Item script, the player is SRC, and the item he targeted is SRC.TARG.

We refer to an event like this:

<font color="darkblue">`ON=@DClick `</font>

Following that line would be everything that we want to happen when the player clicks the item.

We'll see examples in the next section of the use of both events and objects.

```
## Making Decisions
```

It was an amazing day when someone showed this script to me. This was actually the script that tested the "new" scripting system in version .37. SPHERE wasn't even SPHERE then. It was called "Grayworld" and was on menasoft.com. Actually, I believe it was in the Admin FAQ that they used to have on the website. Here it is, updated to 56b format:

<tt><font color="darkblue">\[TYPEDEF T_VEND_MACHINE\]
// Some other trigger.
// Vending machine.

ON=@DCLICK


IF (\<SRC.RESTEST 10 i_gold\>)
:SERV.NEWITEM={ i_HAM 1 i_fruit_apple 1 i_bread_loaf 1 i_bacon_slice 1 i_RIBS_COOKED 1 i_SAUSAGES 1} :SRC.BOUNCE \<NEW.UID\> // put it in your pack. :SRC.CONSUME 10 i_gold :SRC.MESSAGE That will be 10 Gold Thank Thee. :SOUND 0F7

ELSE
:MESSAGE You lack 10 Gold to pay.

ENDIF

RETURN 1
</font></tt>

Put this script into one of your files and resync your server. I like to use spheretrig.scp for test triggers like this. Now, in the game, type <font color="darkred">.set type t_vend_machine</font> and target any item (like a door). Then double-click it and watch what happens. If you get the "not enough gold" message, <font color="red">.add</font> yourself some i_gold, and try again.

See the result of this simple little script? It's got a lot that we've dicussed, and even more that we haven't. First, you may notice the use of this strange IF construction. You will use this again and again, so pay attention! The IF structure looks like this:

<font color="darkblue">`IF (1 or 0)`
`// Execute these lines if 1`
`ELIF (1 or 0)`
`// Execute these lines if the first wasn't 1, but this one is`
`// You can have as many ELIFs as you need`
`ELSE`
`// Execute if none of the above are 1`
`ENDIF`
</font>

Always, always, always, always pair your IF with an ENDIF. It doesn't matter what's in the middle. You can have eight hundred ELIFs and an ELSE. But ALWAYS be sure your IF is paired somewhere with an ENDIF. Actually those are the only two required parts of this construction. ELSE and ELIF are completely optional, and you should only use them if they are absolutely needed.

So what is this "1 or 0" thing? How does it help me in my scripting if I'm just typing a 1 or a 0 in there? Actually, you will NEVER type a 1 or a 0 in there, and this is a perfect time to introduce the equivalence test operators. Here they are:

```
|         |                              |
|---------|------------------------------|
| **==**  | **equal to**                 |
| **!=**  | **not equal to**             |
| **\>**  | **greater than**             |
| **\<**  | **less than**                |
| **\<=** | **less than or equal to**    |
| **\>=** | **greater than or equal to** |
```


**1 = true**
**0 = false**

I've put this table in bold since it's so incredibly important. And here is another SPHERE principle:

**Do not use == and = interchangably in an IF statement. SPHERE actually allows this, but you will get confused and use == where you mean =, and vice versa.**

Here is an example of using a equivalence operator in an IF statement:

<font color="darkblue">`IF (<SRC.STR> == 75)`</font>

Read this "If src.str is equal to 75". Want to know something interesting? Internally, if SRC.STR is in fact equal to 75, SPHERE will replace the ENTIRE part inside the parentheses with a 1. If it is not equal to 75, SPHERE will replace that part with a 0. That's where your 1 and 0 comes from.

Now you may be wondering, what the \< \> brackets around \<SRC.STR\> are doing there. Actually, this is one of the most elusive concepts in SPHERE scripting. The \< \> brackets mean "Replace whatever is inside with the actual value of that thing." This is done before any testing is executed. Say SRC.STR has been set to 71. Here are the steps SPHERE takes in simplifying this IF statement:

<font color="darkred">`1. IF (<SRC.STR> == 75)`</font>

<font color="darkred">`2. IF (71 == 75)`</font>

<font color="darkred">`3. IF (0)`</font>

Notice above in the example script that we have this statement:

<font color="darkred">`<SRC.RESTEST 10 i_gold>`</font>

"What the heck is <font color="darkred">RESTEST</font>?" <font color="darkred">RESTEST</font> is what we call a function. It takes parameters (in this case an amount and an item ID) and returns a value. SPHERE replaces the entire function statement \<SRC.RESTEST 10 i_gold\> with that value. RESTEST checks to see if the player has an amount of the item specified greater than the amount specified:

"Does the player have an amount of i_gold equal to or greater than 10?" is what the function asks. Internally SPHERE says "Yes" and replaces it with a 1, or "No" and replaces it with a 0.

Say the player had 9 gold in his backpack. Here is the simplification of the IF statement:

<font color="darkred">`1. IF (<SRC.RESTEST 10 i_gold>)`

`2. IF (0)`
</font>

We'll see in later chapters how to define our own functions, give them parameters and have them return a value!

I hope you have a general understanding of the <font color="darkred">IF</font> statement now. Here is a more complex example for you to analyze:

<font color="darkblue">`IF (<SRC.STR> > 60)`
`:SRC.SYSMESSAGE Your strength is greater than 60.`
`ELIF (<SRC.STR> > 40)`
`:SRC.SYSMESSAGE Your strength is greater than 40, but less than 60.`
`ELIF (<SRC.STR> > 20)`
`:SRC.SYSMESSAGE You are a weakling with between 20 and 40 strength.`
`ELSE`
`:SRC.SYSMESSAGE Start lifting weights because your strength is less than 20!`
`ENDIF`
</font>

What does this do? Well first, SPHERE looks at the IF statement, and says "Is the value of SRC.STR greater than 60?" If the answer is no, SPHERE replaces that with a 0, and jumps down to the first ELIF. "Is the value of SRC.STR greater than 40?" If not, it jumps down to the next one. "Is the value of SRC.STR greater than 20?" If not, it looks for further ELIFs. Unable to find them, it jumps to the ELSE statement, since nothing above was true.

SYSMESSAGE prints out a message to the corner of the screen of the referenced object. In this case, that's SRC. Earlier, you saw an example involving the MESSAGE function. It prints the message above the object referenced. If the object is inside of a closer container, it does a SYSMESSAGE to the topmost container object. This means that if an item in a backpack is given a MESSAGE command, and the backpack is not opened, the player will see the message in the corner of his screen.

<font color="darkred">**`SYSMESSAGE`**` [text]`
**`MESSAGE`**` [text]`
**`RESTEST`**` [amount] [item]`
**`NEWITEM`**` [item]`
**`BOUNCE`**` // Put an item into the character's backpack`
</font>

Your first five functions. Congratuations. Actually, you saw another one in an earlier script! Remember what it is?

<font color="darkred">**`SAY`**` [text]`
</font>

This, of course, causes the object to SAY (so everyone can hear it) the text given. With MESSAGE and SYSMESSAGE, the text is private to a single client. MESSAGE text is only visible to the SRC. (In other words,LINK.MESSAGE or SRC.TARG.MESSAGE will show a message over LINK or SRC.TARG that only SRC can see!)

So finally, what is this weird <font color="darkred">RETURN 1</font> at the end of the script?

RETURN is used in a variety of ways. In the case of an event script, if you RETURN 1, it prevents the default action from happening. For example, if you put this on an item in the game and double-click it, it doesn't actually try to use the item too. It just executes the double-click script. (To a player it would look like he was using theitem, but we know better.) If you change it to RETURN 0, it would try to use the item too, realize it had no idea what to do with this item, and say "You are not sure how to use this item" or something like that. Either way, the script ends as soon as it sees a RETURN statement. The distinction between RETURN 1 and RETURN 0 is even more clear in character events, and I shall make an effort to point that out at the time.

```
## \[SPEECH\] for Dummies
```

I say "Hello" you say "Goodbye", or "Cheese", or "You are a bad scripter"

Well, it's time to introduce you to your newest concept in SPHERE scripting:

NPC SPEECH is an event.

A long time ago there was supposed to be a @Hear trigger, and we waited and waited and waited, and it was going to be the next big thing in TUS (SPHERE's name before version .50), but nothing ever came of it. Then came SPHERE with all these new scripting revelations, and we said "Hey! We don't even need @Hear! Speech works just like any other event!

For example:

<font color="darkblue">`[SPEECH spk_human_test]`
`ON=*hello*`
`:SAY @55 Cheese!`
</font>

You should recognize that from a previous chapter when we created this script and set it on an NPC. But what if we want that NPC to do more than say "Cheese!" in a yellow colored font. What if we want him run away as fast as he possibly can, or drop his gold on the ground and faint?

We could easily do this:

<font color="darkblue">`[SPEECH spk_human_test]`
`ON=*hello*`
`:IF (<SRC.KARMA> < <SERV.PLAYERNEUTRAL>) // Are they less than good?`
`::SAY You are evil! Get away from me!`
`::FLEE // Causes an NPC to run away from SRC (this can have an argument (the one to flee from))`
`:ELSE`
`::SAY Cheese!`
`::BOW //Makes him bow to src (this can have an argument (the one to be bowed to uid))`
`:ENDIF`
`:RETURN 1`
</font>

If you don't RETURN 1, the processing will pass through to the default handler, which will make the NPC say something like "Huh? I don't understand thee!"

In an NPC speech event, <font color="darkred">SRC</font> is the player who triggered the event, the speaker who said "hello" in this case. The default object is the NPC with the event on him, as you can see from the script above. That is why SAY works without an object reference.

You can have ANYTHING in a speech script that you can have in a normal script. Just remember, there are no items involved. No MORE, no MORE2, no MOREP. But I'll tell you in a little bit how to get as many variables as you want on both NPCs and humans.

This section doesn't need to be any longer, does it? You already know how to write an event, and you already know some basic statements, like <font color="darkred">IF</font>. That should provide some very robust NPC speaking on your shard!

==The Difference Between = And ==?== In most programming languages, = is called the "assignment operator". == is called the "equals sign".

Here are my style guidelines, for better readability of your scripts, and so on. (If we can't read your scripts, we can't help you with them.)

1.  == should only be used in test statements, like an IF
    `IF (<SRC.STR> `**`==`**` 75)`
2.  = should be used for assignments, like setting a variable to a
    value
    `MORE `**`=`**` 3`
    `MOREP `**`=`**` 45 65 12 4`

And that's about it. I'm pretty lenient huh?

As a comparison, my Java class at school has style guidelines in a set of pages the size of this entire tutorial.

[Category:Tutorials](Category:Tutorials "wikilink")
```
