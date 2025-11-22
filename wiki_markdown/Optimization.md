## Making Sphere Faster {#making_sphere_faster}

*Optimization in Sphere\
By Taran*

This will be an article about time. Incredibly small amounts of time, on
the order of thousandths of a second.

I have noticed over the years that people complain often that a Sphere
server cannot handle a significant number of players without suffering
severe lag. Most people speculate that this is because something is
inherently wrong with Sphere. After all, they\'ve played on other shards
which didn\'t have lag. Never mind that those other shards also use
Sphere. No administrator cares about other shards.

So, an oft-asked question in the Sphere community is, \"How can I make
my shard run faster?\"

By faster, most people mean to reduce lag. Most people assume that the
lag in SPHERE is the result of a slow connection. People will play on a
server run on a T1 before they will play on a Cable server. This is
because people are under the misconception that UO game play requires a
fast connection. Granted, a faster connection will accelerate your
running speed slightly. However, to get to the root of this problem, we
need to use a profiler. Profiling is generally an option on a compiler,
which builds the program so that it will measure how long its various
aspects will take. It is an important skill in real programming, because
the slow parts a program are almost never in the location the programmer
would first assume.

In UO, everything takes place in the form of packets. Packets are clumps
of data which I describe in detail in the SENDPACKET tutorial. The size
and amount of packets you receive in a second determines how much lag
you experience. The packet which describes an object (item on the
ground) to your client is between 15 and 21 bytes. You read that
correctly. This means that even sending the description of 100 items to
your character will only require 1500 or 2100 bytes. This is not a
significant amount and can be transferred nearly instantly over a decent
cable or DSL connection. Once your client knows about the items, it will
store them in a cache, so that it doesn\'t need to receive them again.
Sphere sends your client information about the items in an area equal to
the size visible on the small radar. This is how you can see multis on
your radar before you can see them on your screen.

Lag occurs when your client is not receiving data fast enough to update
its display. Since it doesn\'t know what\'s happening, it will sit there
and wait until it does receive enough data. This can be the result of
insufficient bandwidth on the server end, or it could be the result of
insufficient bandwidth on the client end. If there are 100 items at
Britain bank, and 50 players arrive there, your server will try to send
2100 bytes to 50 players, for a total of 105000 bytes. If your server
can handle sending this amount of data out in a second (105 KB/s), none
of those players will experience lag.

Now, it goes without saying that under no circumstances should you have
100 items and 50 players at Britain bank. That\'s just asking for lag.
105 KB/s is the equivalent of a full second\'s bandwidth on a very fast
DSL or cable connection (\~850 kbit) or a slow LAN connection. Those
bytes are only a small portion of the data sent out your line every
second, depending on what the players are doing. So, we have determined
already that a major cause of server lag is decoration. You should not
excessively decorate highly-traveled locations. Instead of placing 100
dynamic items, you should either make a multi which coincides with the
bank, or you should patch them into a statics file which you then
distribute to your players.

Connection issues, however, are not the primary cause of lag. Excessive
decoration is certainly a cause, but it is not the only cause. After
all, your server is required to do other things aside from send data to
players. For instance, it must keep track of all NPCs and all items at
every instant. Wandering NPCs must be moved in a way that they don\'t
collide with trees and landmasses. Fighting NPCs must fight in a way
that is sensible based on their current situation. Items with \@Timer
scripts may execute their scripts on a regular basis. And any other
scripts on players and items must execute before any data can be sent in
reply.

Unfortunately, SPHERE does not utilize a very good threading model. A
threading model allows a program to essentially do more than one thing
at any given time. A thread, which is generally helpfully defined as \"a
thread of execution,\" is basically an individual program within a
program. Threads are independent but can communicate with one another.
As they are part of the same larger process, they can also alter data
that other threads can use. If you have multiple processors, your
computer is capable of running each thread on a different processor,
which allows them to actually run at the same time, instead of taking
turns as they\'d do on a single processor.

The major advantage to threads involves input and output. Programs spend
a lot of time waiting for the computer to respond. For instance, if they
try to read data from the disk, they must wait until that data is
actually transferred into memory and presented to the program
successfully. No execution can continue until the data is received.
Windows provides a method of automatically reading data in a separate
thread, called overlapped I/O. This method allows you to ask for data,
and then do other things while you wait for it. When it arrives, you are
notified in one of many ways, and you can then do whatever you needed to
do with the data. Since data can be retrieved at the same time that your
processor is doing other tasks, your program runs faster.

Sphere does use a few threads. You may notice that exiting the program
causes the console to print \"closing background threads.\" While your
server runs, it is also keeping track of the modification dates of every
script file. It does this in a separate low-priority thread, so that it
doesn\'t get in the way of other main tasks. Sphere also uses a separate
thread to perform a background save. When you force a foreground save,
it transfers that save process from the background thread to the main
thread. While it\'s saving, then, clients will not receive data because
the main thread, which sends the data, is doing something else.

This brings us to a very important point in our discussion. Sphere uses
a single main thread to perform all of its tasks. This means that while
one task is taking place, no other tasks occur (except that
file-checking and background saving, like I said). Sphere runs in a loop
model, much like the [WHILE](./WHILE.md) loops that you can have
in scripts. Here is a rather simplistic description of the innards of
SPHERE:

While the server is running, Sphere does the following things, over and
over:

-   Execute a \"tick\" on each item and each character. This decrements
    TIMERD on all objects.
    -   o If TIMERD = 0 on any item, run its timer-based action, which
        could be a default action, like decaying or walking or fighting,
        or an \@Timer trigger, or both. Deal damage and call other
        triggers as appropriate.
-   Read data from all sockets.
-   Determine what actions are required on any objects as a result of
    that data (initiate attacks, perform default actions, run scripts,
    etc).
-   Both of the previous steps involve output to clients, so send it.

(In about the time it takes you to blink your eyes twice, Sphere should
have executed all of these things up to ten times.)

As you can see, Sphere only really cares about player input for a
reasonably short period of time. Much of the server\'s execution time
involves scripts and other actions. It turns out that internal actions
are incredibly fast, which is why the Sphere team opted to hard-code
them. This leaves us with scripts as a major cause of lag. Does that
surprise you? It won\'t in a minute.

To execute a script, Sphere must first read through each line. So, the
first task is to find the beginning of the necessary script. If this is
a function, that\'s simple. It\'s the beginning of the function. If
it\'s an item or an \[EVENTS\] block, it isn\'t so simple, because the
script could exist in one of many different places.

Next, after it identifies the location of the script in the file, Sphere
will read that file one line at a time and interpret the script.
Interpreting the script involves a lot of binary searches (a reasonably
fast algorithm for searching sorted lists) and parsing expressions.
Parsing expressions also takes time, especially when variables and
defnames are involved. When you say i_gold, for instance, Sphere needs
to look that name up in a table and find out that i_gold is actually
equivalent to the item 0EED. Each command is executed individually and
Sphere updates its state based on the result. If the execution of the
script takes it elsewhere, by calling a function, for instance, Sphere
must go find the beginning of that script. If you create new items or
characters, Sphere must first figure out exactly what the object is and
how it will appear in-game, and then execute the \@Create trigger on
that objects, which takes additional processing. If you create a list
like { 5 6 10 15 18 }, Sphere must execute an algorithm that randomly
selects a member of this list for you. Of course, this list is
interpreted on the fly, and can also contain other lists, such as { {7
9} {10 17} }. Numerical expressions, which are not stored in the file as
numbers, but rather as sequences of characters, must be transformed into
numbers and then carried out.

And Sphere does all of this remarkably quickly. However, there are a
number of things you can do to help it. Since it is the interpretation
process that takes such a long time, the sooner that process ends, the
faster your server will run. The process of making a script (or any
other program) run faster is called optimization. Unfortunately,
optimizing a script often makes it nearly unreadable. So, you should
always make your script work correctly before you try to optimize it. If
you cannot make your script work correctly and quickly at the same time,
sacrifice speed for quality.

There are many things you can do which might cause your scripts to
execute more quickly. I shall detail a few of them.

**1.** Check exit cases first, and return as soon as possible. This is
an important feature of any function in which a particular state may
cause the function to stop executing properly. A good scripter who paid
attention in my [Occam\'s Razor](./Occams_Razor.md) tutorial
might write the following:

`<spherescript>`{=html}\[FUNCTION do_something\] IF (\<SRC.STR\> \< 70)

`   // do something here`\
`   // do something here`\
`   // do something here`\
`   // do something here`\
`   // do something here`\
`   // do something here`\
`   // do something here`

ENDIF RETURN 1`</spherescript>`{=html}

When Sphere begins to execute this script, it will check to see if
SRC.STR is less than 70. If so, it will execute the body of the IF
block. Otherwise, it will search down through each line, reading every
line in as it goes, until it finds an ELSEIF, ELIF, ELSE, or ENDIF. This
takes time, as I mentioned, to read through the lines. It does not take
the same amount of time as actually executing the code within the IF
block, but it will still take time. In our example script, we return
from the script after the ENDIF, and nothing else. In this case, it
isn\'t really worthwhile to scan down through all of those lines. A
faster script might look like the following:

`<spherescript>`{=html}\[FUNCTION do_something\] IF (\<SRC.STR\> \>= 70)

`   RETURN 1`

ENDIF // do something here // do something here // do something here //
do something here // do something here // do something here // do
something here RETURN 1`</spherescript>`{=html}

This prevents the script from reading unnecessary code. When it
determines that the strength of the SRC is not appropriate for this
function\'s actions, it will immediately return from the function. Thus,
no time is wasted looking for an ENDIF. If you have a long script with
many IF/ELSEIF sections, you might consider placing a RETURN 1 within
each of those sections.

You would not want to follow this rule if you want to actually do things
after your IF statement. For instance, if our original script looked
like this:

`<spherescript>`{=html}\[FUNCTION do_something\] IF (\<SRC.STR\> \< 70)

`   // do something here`\
`   // do something here`\
`   // do something here`\
`   // do something here`\
`   // do something here`\
`   // do something here`\
`   // do something here`

ENDIF SYSMESSAGE This is the end! RETURN 1`</spherescript>`{=html}

You might want the player to receive that message regardless of his
strength. In that case, it would probably be best to leave the function
in its original state, instead of unnecessarily duplicating code.
Duplicating code leads to messes when you try to modify that code and
forget that you\'d duplicated it. Another alternative would be to use a
second function.

`<spherescript>`{=html}\[FUNCTION do_something\] IF (\<SRC.STR\> \>= 70)

`   DO_IT`\
`   RETURN 1`

ENDIF // do something here // do something here // do something here //
do something here // do something here // do something here // do
something here DO_IT RETURN 1

\[FUNCTION do_it\] SYSMESSAGE This is the end!`</spherescript>`{=html}

**2.** Avoid using ALLCLIENTS statements if at all possible. If they are
vital for your script, use them, but use them sparingly. If you use
ALLCLIENTS, you are inflicting not only one player but all of the
players currently online to the lag associated with a slow script. If
your script is not inherently slow, you probably have nothing to worry
about, but every little bit counts. A script which uses ALLCLIENTS to
transport players into a game or to send text messages in the form of a
chat system probably has very little to worry about as these scripts, if
written correctly, are not inherently slow.

**3.** Avoid excessive recursion. While a recursive function may seem
the easiest way to perform a task, you are using both time and memory
when you call that function. Calling a function is not nearly as
expensive as the commands you might execute within the function, but
like I said in the previous point, every little bit counts. If you look
at some of Swindler\'s scripts, you will find that they are
prohibitively long, but that they run extremely fast. His \"contents\"
script, which executes a function on every object in a container, is
spread out and fast. A simple way to run this script might be the
following:

`<spherescript>`{=html}\[FUNCTION contents\] // The argument is the
action to execute on the contents of the // container. For instance to
make every item in the container say // \"hello,\" we would use the
following command on the container: // // CONTENTS SAY Hello

// The last item is actually index RESCOUNT - 1, because // the first
item is index 0. The second item is index 1, etc. // Therefore, the last
item\'s index is one less than the number // of items left in the
container. VAR.HOWMANY = \<EVAL `<RESCOUNT>`{=html} - 1\> CONTENTS_AUX
`<ARGS>`{=html}

\[FUNCTION contents_aux\] // Our recursive function. Notice that I\'m
checking the // exit condition first, like I said. IF (\<VAR0.HOWMANY\>
\< 0)

`   RETURN 1`

ENDIF // This line might resolve to something like the following: //
FINDCONT.50.SAY Hello TRY FINDCONT.\<VAR.HOWMANY\>.`<ARGS>`{=html}
VAR.HOWMANY -= 1 // Don\'t forget to pass the argument to the next
iteration! :) CONTENTS_AUX `<ARGS>`{=html}`</spherescript>`{=html}

Believe it or not, there is a faster way to execute this script.
Swindler and I realized, while scripting for Ithyca, that calling a
function is slightly slower than not calling that function. Remember,
for each function call, Sphere must go find that function in a file,
which requires time.

**4.** Turn on SECTORSLEEP in sphere.ini. Sector Sleep is a function
added somewhere around TUS 0.45, which causes, well, sectors to sleep.
In sphere.ini, you can specify an integer value for SECTORSLEEP. We\'ll
call that value X for now. Every X minutes, Sphere checks to see if any
players are in a particular sector. I believe this takes place in one of
the background threads, but I\'m not certain. If no players occupy a
sector, Sphere will suspend all handling of timers in that sector. When
a timer reaches 0, it will simply stop there, without executing \@Timer
scripts or doing any default timer actions. As soon as a player enters
the sector, it will awaken and everything in that sector will come to
life again.

Since NPC movement and fighting is based on timers, this will
effectively suspend all NPC movement until a player re-enters the
region. Unfortunately, since it also suppresses timers on items, Sector
Sleep has a number of unfortunate side effects. For instance, spawn
points depend explicitly on a timer. Therefore, if you have just spawned
your world or have just reset the spawns in your world, nothing will
spawn unless a player is actually within the same sector as the spawn
point. This could be an advantage, I suppose, but I would recommend that
you remove SECTORSLEEP (set it to 0) while you are spawning your world
and for a short time after you reset all spawn points.

If you have a scripted item using \@Timer in a sleeping sector, that
item will not function correctly anymore. Unfortunately, this can affect
a number of systems. When I ran my automated capture the flag script on
Ithyca, my players experienced this difficulty first-hand. The sector
containing the game control stone would go to sleep, thus suspending
\@Timer handling on that stone. Thus, when the game ended, their game
memories would detect the end of the game and remove their clothing, but
the stone would not appropriately return them to the ready room. All of
the players would be stuck, naked, in the CTF arena until someone
happened to pass through the ready room and awaken the sector.

Thus, while SECTORSLEEP can cause some scripts to behave strangely, it
reduces lag enough that it makes timer workarounds worthwhile.

**5.** Avoid excessive use of TAG and VAR values. These values are
stored in a special type of sorted list called a linked list. A linked
list allows you to add and remove things from the middle quickly, which
makes it ideal for this sort of application. Linked lists do not allow
you to find a particular item in the list very quickly. You must search
through each element from the beginning, counting as you go, until you
find the item with the index you require. Sphere uses sorted linked
lists, which allows them to very quickly find the index of the element
they need. Despite this speed, they must still search through each
individual item until they find the one they need.

Of course, the lag you will experience from TAGs and VARs is minimal,
and probably not worth worrying about. Giving each player 350 tags might
lag your server a bit, but if you do that, your scripting dilemma is
larger than your lag dilemma.

By the way, this is why I said you should always delete a TAG or a VAR
when you are finished using it.

*(And don\'t worry about how linked lists work. If you are a programmer
and are curious, you can find plenty of information about them by
searching Google.)*

**6.** Do not spawn cities excessively, especially Britain. Since
sectors only go to sleep when there are no players, you can safely
assume that the 7 or 8 sectors in Britain will never sleep. This means
that any animals or NPCs you place in the biggest city in the game will
continue to wander about aimlessly, using your precious server time.

**7.** Avoid excessive multiplication and division in a script. This
will cause minor delays, probably unnoticable next to other types of
delays. Multiplication and, especially, division are much slower than
addition. Unfortunately, there are few workarounds for this lag issue. I
can\'t think of any reason you would need excessive multiplication and
division, except perhaps to calculate a square root, so these operators
do not pose a threat to your server.

**8.** If a function returns a value, calculate that value in the RETURN
statement, instead of using temporary variables to hold the value. One
long string is faster than a number of short strings put together later.
The perfect example of such a mistake is our SPLIT4BYTES function from
the SENDPACKET tutorial. I wrote this function so that it looked
something like this:

`<spherescript>`{=html}\[FUNCTION split4bytes\] LOCAL.PART1 = \<HVAL
\<ARGV\[0\]\> & 0FF\> LOCAL.PART2 = \<HVAL (\<ARGV\[0\]\> / 0100) &
0FF\> LOCAL.PART3 = \<HVAL (\<ARGV\[0\]\> / 010000) & 0FF\> LOCAL.PART4
= \<HVAL (\<ARGV\[0\]\> / 01000000) & 0FF\> RETURN \"\<LOCAL.PART4\>
\<LOCAL.PART3\> \<LOCAL.PART2\>
\<LOCAL.PART1\>\"`</spherescript>`{=html}

This function will run fast. However, it will not run as fast as
possible. To accomplish that, we must put all of those calculations into
the return statement, and avoid the creation of unnecessary temporary
variables:

`<spherescript>`{=html}\[FUNCTION split4bytes\] RETURN \"\<HVAL
(\<ARGV\[0\]\> / 01000000) & 0FF\> \<HVAL (\<ARGV\[0\]\> / 010000) &
0FF\> \<HVAL (\<ARGV\[0\]\> / 0100) & 0FF\> \<HVAL \<ARGV\[0\]\> &
0FF\>\"`</spherescript>`{=html}

Acratia wrote an even faster version of this function, which you will
find on the Functions & Events board, and probably on Script Sharing.
His function uses binary shifts, a topic I will probably write another
tutorial about someday.

**9.** Avoid calling EVAL or HVAL unless necessary. That\'s just simply
another unnecessary function call SPHERE could use doing something else.
You only need to use EVAL if you are dealing with:

-   Strings
-   TAGs
-   VARs
-   Displaying numbers that normally display in hexadecimal format

**10.** Avoid creating excessive new objects. Creating 100 items in a
recursive script requires 2.8 seconds. Creating 100 NPCs takes slightly
longer than that. Clearly, then, creating new objects is a slow process.
This is mostly because Sphere must first create the new object, then
fill its properties according to its TYPEDEF, then read and execute its
\@Create event.

**11.** Set the CONT of an item instead of using EQUIP or BOUNCE.
Unless, of course, you want the \@Equip event to execute. EQUIP and
BOUNCE perform extra processing which is usually unnecessary or already
completed in your script. BOUNCE also displays that unsightly \"You put
the something in your backpack\" message to whoever is putting the item
in his or her backpack.

`<spherescript>`{=html}\[FUNCTION equip_a_sword\] // To demonstrate
equipping an item SERV.NEWITEM i_sword_viking NEW.CONT `<UID>`{=html}

\[FUNCTION bounce_a_sword\] // To demonstrate bouncing an item
SERV.NEWITEM i_sword_viking NEW.CONT
\<FINDLAYER.layer_backpack.UID\>`</spherescript>`{=html}

See? Easy and fast. Of course, Sphere will still perform some extra
processing, to verify that the item can actually go where you\'re
telling it to go, but otherwise, it\'s generally faster to do it this
way.

Remember, if you want Sphere to do extra equip processing (\"You can\'t
equip that\"), you will need to call EQUIP explicitly. You must also
call EQUIP if you are expecting the \@Equip event on the item to execute
(or the \@ItemEquip event on the player).

Overall, optimization saves Sphere time on the order of a few tens or
hundreds of milliseconds. But, if you have 50 players executing a
thousand optimized functions and scripts, you will save time that Sphere
can spend doing other things, such as sending data to your clients, thus
reducing lag. Remember, for every internal function Sphere can avoid by
not executing something in a script, it has extra time to do other
internal things.

[Category:Articles](./Articles.md)
