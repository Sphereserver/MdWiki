## Introduction

You've seen it. Swindler posts on the boards those long extensive
posts, which can make huge scripts seem like simple, trivial tasks.
Belgar posts something, which you read over, and wonder why you didn't
think of it. Then, you sit down to write a script like theirs, and you
end up with a 28kb script which can probably be condensed by at least
90%. I've done it. Swindler has done it. Belgar has done it. The
difference is, we've all learned from our mistakes.

So what do we have that you don't? It certainly isn't knowledge. If
you read my tutorials, you will have an equal amount of knowledge as
Belgar, Swindler, Kell, pmouse, or any of the other good scripters. None
of them use techniques that will be beyond your scope. Does that make
you stupid? Certainly not! There are some brilliant scripters on the
boards, who cannot seem to put together a coherent program if their
lives depended on it.

Now, there are entire majors in college involving what I am about to
summarize. I'm in one: software engineering. Yes, you read that right.
The first person I said that to asked me if it was meant to be an
oxymoron. You see, many new programmers have only been exposed to
programming via movies and literature, where programmers are depicted as
a single man in a dark room, who types code and then a program runs.
That is absolutely nothing like the real world. But I won't get into
that, because all we're dealing with is SPHERE scripting.

This tutorial will be a lesson on learning. Doesn't that sound strange?
Many people seem to have the idea in their minds that if they read a
tutorial many times, and memorize every nuance of the scripting
language, they will suddenly become a good scripter. And then they feel
stupid when they post their incomprehensible scripts and a perfectionist
comes along, cleans it up, and reduces it to three lines of code.

## Never, Ever Memorize Code {#never_ever_memorize_code}

"But how am I supposed to learn this if I don't memorize code?" you
are asking. Learning and memorizing are two different things, and use
two different functions of the brain. If you memorize, you can
regurgitate perfectly, for example, the objects you receive when the
@DClick event fires, and what each of those objects represents.
However, your brain has not realized that these objects are also related
to other objects (for example, a person is related to everything he is
wearing, and vice versa).

The most common instance of this problem is trying to place items into a
container that is not the backpack, or equipping them on someone else. A
person in this situation will look through my reference database, and
find that there is a command called BOUNCE which puts the referenced
item into the backpack of the SRC (SRC is the person dclicking in this
trigger), like so:

`<spherescript>`{=html}ON=@DClick

`   SRC.SAY The sword is mine!`\
`   SERV.NEWITEM i_cool_sword`\
`   NEW.BOUNCE`</spherescript>`{=html}

The i_cool_sword item magically is placed into the backpack of the SRC.
What most people don't seem to understand is that this piece of code is
only one of many ways to achieve the same effect. For example, what if
there is no SRC? What if this script is a @Timer script running on a
memory object, where the player in question is that object's CONT or
TOPOBJ?

`<spherescript>`{=html}ON=@Timer

`   CONT.SAY The sword is mine!`\
`   SERV.NEWITEM i_cool_sword`\
`   NEW.BOUNCE`</spherescript>`{=html}

This will be the most common attempt to complete this script. However,
it is WRONG . BOUNCE only places the item into the backpack of the SRC.
In this case, there is no SRC, so the item will not move from its
undefined location. In-game, no item will appear, because in theory,
none was ever created in the real world. What we need to solve this
problem is a different approach. One must realize how objects interact.
What exactly do we want to do with this i_cool_sword? We desire to place
it into the player's backpack. In other words, the player's backpack
must become the container of the i_cool_sword. So why not just:

`<spherescript color="darkgreen">`{=html}ON=@Timer

`   CONT.SAY The sword is mine!`\
`   SERV.NEWITEM i_cool_sword`\
`   NEW.CONT <CONT.FINDLAYER.layer_backpack.UID>`</spherescript>`{=html}

Now what does this do? It looks more complicated, you're saying. Look
at it for a moment. CONT contains the UID of the container of a
particular item. In this script, we are SETTING that CONT object to be
the UID of the player's backpack. We access the player's backpack
object through the FINDLAYER function, and retrieve its UID.

Now, if our scripter had learned the concepts behind containers and
items, before memorizing the BOUNCE command, he would have realized that
the code in green is the correct way to implement the solution. In fact,
it is a far better method, because it is easily changable. For example,
what if we want to place this item into the player's bank box instead
of his backpack? We'd simply change layer_backpack to layer_bankbox,
and it would be finished. No fancy functions, no new commands to learn.
We're simply altering a command we already know to provide new
functionality.

That is step one in your becoming a proficient SPHERE scripter. You must
learn to extend what you already know to provide new functionality.
SPHERE scripting can do nearly anything. Yes, that's right. Anything.
But how? You'll just have to sit back and think about it:

## Plan Your Project Before You Begin {#plan_your_project_before_you_begin}

This is another result of the lone hacker syndrome that people pick up
in the media. If you read a programming book, the entire beginning
chapters will be on the proper design of a program. My entire major in
college is devoted to the proper design of a functioning program.
That's what I will be doing for the rest of my life, and being paid
large sums of money to do so.

All programming projects come in five stages:

1.  Requirements
2.  Specifications
3.  Design
4.  Coding
5.  Debugging

This is known as the "software life cycle" and was one of the first
things I was taught in my very first computer class as a software
engineering student. Notice that you don't even begin to write lines of
script until the second to last step of the process.

### The Requirements Stage {#the_requirements_stage}

The requirements stage is simply the statement of the problem, and what
you want your script to do:

"This in-game command .build should create a house which can be of any
specified size and number of floors. The style of the walls, floor, and
roof (which must be slanted) should also be specified. Houses always
take rectangular form. The roof adjusts itself according to the length
and width of the house. Houses which are narrower in the north-south
direction should have a north-south facing roof, and the same is true
for east-west houses."

That is a requirement. You know it as an idea. Notice that we have not
yet even MENTIONED a scripting command. However, from the problem we
should have a more general idea how we want our program to work. Next,
we write the specifications of the problem. This is basically
subdividing and conquering the problem, to make it easier. In the real
world, different pieces of the problem would be handed off to different
people. For example, one person might design the roof script, one might
design the walls, and one might design the floor. Of course, as a SPHERE
scripter, you rarely have the chance to work with anyone else. SPHERE
scripting is simply not that type of programming language.

### The Specifications Phase {#the_specifications_phase}

Next, we reach the specifications stage of the project. This is slightly
longer, and in my case, it takes the form of a numbered list:

1.  Retrieve the styles from the command line
2.  Use the styles to find the correct items to construct the house
3.  Set the variables to their defaults
4.  Build the current floor using the specified type
5.  Build the walls for the current floor
6.  If this is not the final floor, increment the Z location by 20, and
    start from step 4
7.  Otherwise, choose the appropriate roof type and build it

Doesn't the problem seem slightly easier now that you've laid out a
plan? You COULD code at this point, but what if you made a mistake in
your specification. Obviously, this is a rather small specification.
This stage of the process, in the professional world, usually takes the
form of a report which can be up to 100 pages in length.

Next, we must subdivide further, and design how we are going to
implement the specifications.

### The Design Phase {#the_design_phase}

First, we see that several functions are going to be needed. Let's name
them now and write down what they are supposed to do:

**FUNCTION build**
This is the main function called by the command line. All it does is
call other functions.

1.  Call function retrieve_cmd_line
2.  Check if the command line information was valid, and exit if not (we
    don't want to build a bad house)
3.  Call function get_style_data
4.  Call function variable_defaults
5.  Call function do_all_floors
6.  Call function do_roof

**FUNCTION retrieve_cmd_line**
This function is a bit more difficult. We know that we need six pieces
of information. What would be the best way to retrieve this information.
If you read the tutorial correct, you know that we have a trick where we
store the `<ARGS>`{=html} variable into the MOREP of an item, which we
can then access as four different variables MOREX, MOREY, MOREZ, and
MOREM. However, we need six, so where do the other two come from? The
answer is, they don't. Why can we not store three different numbers
into MOREX? If the user types 300, could this not be interpreted as a 3,
a 0, and a 0? Therefore, our build command, must have the following
parameters:

`<spherescript color="">`{=html} .build [floor type][wall
type][roof type] [width] [length] [number of
floors]`</spherescript>`{=html}

Notice that there are no spaces between the first three parameters. Now,
here are the steps this function takes:

1.  Create a new i_memory item
2.  Store ARGS into the MOREP of that item
3.  Fill VAR.FLOORTYPE, VAR.ROOFTYPE, and VAR.WALLTYPE with the data
    from MOREX
4.  Fill VAR.WIDTH with MOREY
5.  Fill VAR.LENGTH with MOREZ
6.  Fill VAR.FLOORS with MOREM

You get the idea. The design phase is where you lay out exactly what
each part of your program should do. The idea is that any scripter
should be able to take your design and create a working script from it.
If I cannot understand your design, then chances are you cannot either,
and you should either divide it farther, or explain it better. The
reason you can all understand Swindler's scripts that he posts on the
message boards is because he places his design comments directly within
the scripts themselves. If not there, he certainly offers some
explanation as to why his script is built the way it is.

### The Coding Phase {#the_coding_phase}

Before you begin, CAREFULLY review your specifications to make sure that
they meet the requirements. Also review your design to be sure it makes
sense. If your find a mistake in an early stage of the Software Life
Cycle, you must REDO all steps following it, because they will no longer
be accurate. It is a terrible thing to develop a complete working
script, and then find out that it doesn't do what you originally wanted
it to do. Usually, that situation involves a complete rewrite of the
script. When your scripts are over a thousand lines, that is a BAD
thing.

Now, implement your code one piece at a time. You should be able to
develop it in the order specified in the design phase. If you cannot,
there is something wrong with your design, and you need to go back and
fix it. If you learned the scripting language enough, you should only
have to consult the tutorial once or twice during your script. The
design will make the steps obvious.

### The Debugging Phase {#the_debugging_phase}

This phase is endless. A quote I read one time goes something like this:

*"It is twice as difficult to debug a program as to write it.
Therefore, if you put all of your creativity and effort into writing the
program, you are not smart enough to debug it."

However, that doesn't mean you can't go look for help. Chances are,
this is the step where you will approach the members of the SPHERE
community for help. However, don't blindly post help. First, check for
typos. The biggest source of errors is simple typos. Did you type !
where you mean ~? Did you type a ( where you wanted to insert a <?
Those simple errors cause innumerable problems. Also, check to see if
your EVAL statements have that closing bracket. *`<EVAL` will not work,
but `<EVAL &ltVAR.HELLO>> will.`*

In fact, today in my computer science class, the instructor had two
variables. In SPHERE, they would be called VAR.BOLD and VAR.ITALIC. Here
is what her program would have looked like, translated into the SPHERE
language:

`<spherescript>`{=html}IF (`<some condition>`{=html})

`   VAR.BOLD = 1`

ELSE

`   VAR.BOLD = 0`

ENDIF IF (`<some other condition>`{=html})

`   VAR.ITALIC = 1`

ELSE

`   VAR.BOLD = 0`

ENDIF`</spherescript>`{=html}

See the problem? Obviously the VAR.BOLD in the second ELSE should be
VAR.ITALIC. This caused the very interesting effect that when you
deselected the "italicized" option in her program, the text stayed
italic, and lost its boldness instead. We spent 10 minutes trying to
find the error. Fortunately, she had 50 people in the class to help her
find it.

## Handling Arguments and Ranges

Script instructions now correctly parse arguments containing `{}` ranges, resolving a previous bug that caused unexpected values or behavior. The '-' symbol is no longer used as a range argument separator. When parsing weighted ranges, only the randomly extracted argument will be completely parsed and resolved, instead of parsing recursively each argument of the range.

## Ask For Help {#ask_for_help}

Never be afraid to ask someone else for help. However, there are certain
rules that you are expected to follow when seeking help. Before seeking
help from a person, try to find the answer yourself. Not only will you
learn more in the process, but chances are you won't make the same
mistake again.

After this fails, post a message on the message boards. Do NOT send
someone a message on ICQ begging that person to help you. This is simply
common courtesy. If you do not receive a satisfactory answer on the
message boards, resort to ICQ. My ICQ number is listed on the main page.
However, if I do not respond to your first message, do not continue to
message me saying "Hello?" and "Are you there? I need some help?"
every five minutes. That is an excellent way to end up on my or any
other expert's ignore list. If I do not respond, I am busy.

The method in which you ask for help is also very useful. First, clearly
define the problem you are trying to solve. This does not help at all:

`<spherescript color="orange">`{=html}SUBJECT: HELP!!!!!!!!!!!!!!11111

Why doesn't this script work????/// I've tried everything and it
won't work! WHY?!?1/1/ HELP ME!

IF !<EVAL <ARGTXT[1]> > SRC.SYSMESSAGE You MUST enter a valid
price!! DIALOG d_auction_item ELSE VAR.CURRENTPRICE=<EVAL
0<ACT.TAG.ITEM<EVAL <TAG.SELECTED> >PRICE> > IF
(<VAR.CURRENTPRICE> <<EVAL <ARGTXT[1]> > VAR.BID=<EVAL
<ARGTXT[1]> > IF (<SRC.FINDLAYER(LAYER_BANKBOX).RESCOUNT i_gold>
<<EVAL <VAR.BID> >) SRC.SYSMESSAGE Sorry, you don't have enough
money in your bank box to bid that. ELSE TRYP 0 ACT.TAG.ITEM<EVAL
<TAG.SELECTED> >PRICE=<EVAL <VAR.BID> > SRC.SYSMESSAGE You bid
<EVAL <VAR.BID> > gold on the item! SRC.CONSUMEGOLD <eval
<var.bid> > //SYSMESSAGE ACT=<ACT.TAG.ITEM<EVAL <TAG.SELECTED>
>TIMERMEM> ACT=<ACT.TAG.ITEM<EVAL <TAG.SELECTED> >TIMERMEM>
ACT.TAG.HIGHBID=<EVAL <VAR.BID> > VAR.OLDHIGHBIDDER=<ACT.LINK>
ACT.LINK=<SRC.UID> // Give the previous bidder his money back, since
he lost // The owner of the item gets no money back, it's his risk IF
<EVAL <VAR.OLDHIGHBIDDER> >!=<ACT.MORE> SRC.NEWITEM=i_gold
SRC.ACT.AMOUNT=<eval <var.currentprice> > TRYP 0
SRC.ACT.CONT=<UID.OLDHIGHBIDDER.FINDLAYER(LAYER_BANKBOX).UID> ENDIF
ENDIF ELSEIF (<VAR.CURRENTPRICE> ==<EVAL <ARGTXT[1]> >)
SRC.AUCTION ELSE SRC.SYSMESSAGE You must bid MORE than the previous
bidder! ENDIF ENDIF`</spherescript>`{=html}

Can you tell me what that script is supposed to do? Can you tell me how
it fits into the entire system? There are context clues (for example, the presence of ARGTXT) that would suggest that it belongs in a gump
button section, but other than that, we have no idea what it is supposed
to do. We also don't know where all these mysterious objects, like ACT,
are coming from. None of the code is indented either, so we have spend
ten times longer than we should, just to work out what's happening in
that particular piece of code.

Also, learn to hold down the shift key for the entire time you are
typing ! or ? characters. !!!!111 and ???// are irritating to see.

## Never Stop Learning {#never_stop_learning}

You will never learn all of the SPHERE language. Even I don't know all
of the language. Even Swindler doesn't. We are both constantly learning
and figuring out new ways to use old concepts. Well, he is, I have
stopped scripting to continue my writing. That is the only way you will
become better at scripting. That is the only way that you will ever
reach a level where you can help other people.

I will end this lesson on design by introducing you to something
interesting known as Bloom's Taxonomy. It was developed by a researcher
in the 1950s, I believe, and it lays out the process in which the human
mind learns information. It works in a hierarchy. You start on the
bottom step (Knowledge) and cannot move your way upward until you
complete that step. Here is Bloom's Taxonomy in SPHERE terms:

**Step 1: KNOWLEDGE**
This is the step where all new scripters enter the process. You have
probably never seen a program before. You don't understand logic. You
don't understand how the variables work. This is the stage where you
learn how to place your brackets and parentheses correctly. You also
learn the majority of the scripting commands here and most of the
objects. Read over other people's scripts and try to make sense of
them. This step is mostly that memorization I told you avoid. Leave it
as fast as possible! If you continue to memorize, rather than comprehend
scripts, you will never leave this level of learning.

**Step 2: COMPREHENSION**
This is the step where most scripters are lost. Unfortunately, as you
can see, it is the second step. You must understand not only WHAT to
type, but WHY. For example, in my above example using the CONT vs
BOUNCE, you must understand why BOUNCE is an inappropriate choice for
that situation, and you must understand how the objects are interacting.
Continue to study other people's scripts, and try to understand not
only THAT they work, but how they work.

**Step 3: APPLICATION**
Script, script, script. You know what to do, and why to do it. Now do
it. Practice. Chances are you'll learn more in the process. Don't be
afraid to ask for help.

**Step 4: ANALYSIS**
This is the step where you can compare and contrast methods of
scripting. Those of you who have reached this stage are very far along
indeed. It is those people who find the technical errors in my scripting
techniques, and will probably ICQ me about errors in this very tutorial.
You should not begin helping others with scripting until you reach this
stage.

**Step 5: SYNTHESIS**
This is where the fun begins. This is where you begin taking old things
and make new things. You begin designing your own library of functions
to make your life easier. You begin posting complex scripts onto the
message boards, with the full design document attached. You also are
revered as a high member of the SPHERE community. Chances are that if
you have reached this stage, you are able to post scripted bugfixes to
many of the problems with the current release of the software. You've
been around a while, and are probably ready for a much-deserved break
from SPHERE.

**Step 6: EVALUATION**
Unfortunately, since SPHERE is a closed-source project, this option is
unavailable. Generally, it would make you think about how to improve the
system, like I tried to do when I suggested the TARGET function to the
SPHERE devs back in version .42, when no one thought targeting was
possible. Just be as cordial as possible in the process.

[Category:Articles](./Articles.md)