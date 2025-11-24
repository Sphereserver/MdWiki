```{=mediawiki}
{{Languages|Sendpacket}}
```
*Sendpacket*\
*By Taran*

One of the coolest new features that has arrived with the 56-series
versions of SPHERE is the SENDPACKET command. This command allows us to
directly send streams of data to the client. To those of us who know a
bit about programming, this is probably one of the coolest features
they\'ve implemented in a long time. Let\'s start from the beginning.

UO is obviously an online game. Everyone knows this, considering it\'s
in the name, \"Ultima Online.\" However, I don\'t know that many people
actually know how an online game works. Well, first we need to talk a
bit about networking and protocols. UO uses what\'s known as a
client-server protocol to accomplish its goal. In networking, a client
is a program which connects to a server somewhere else on the internet.
A server is a program which allows clients to connect and processes data
it receives. Many times, the server will also send data back to the
client in response to the client\'s messages. This is known as \"serving
information,\" which is how those types of programs acquired their name.

Servers and clients must speak a common language. If they did not, it
would be like a person speaking English trying to communicate with a
person who only speaks French or Chinese or Russian. For example, if you
try to connect to a mail server with your UO client, the two programs
will not be able to communicate. The language spoken by the mail server
is different than the language spoken by your UO client. In the computer
world, a language spoken between two programs is called a protocol. We
use protocols every day without realizing it. When you request a
website, your web browser speaks HTTP (Hypertext Transfer Protocol) with
a web server somewhere. Some people may have used an FTP (File Transfer
Protocol) program to upload and download files from a remote computer.
When you send mail, you are communicating using SMTP (Simple Mail
Transfer Protocol) with the mail server. When you receive mail, you\'re
probably using POP3 (Post Office Protocol, version 3). In fact, all
messages sent across the internet have their own protocols, such as
TCP/IP (Transmission Control Protocol/Internet Protocol) or UDP (User
Datagram Protocol).

UDP is used by many online FPS games, like Quake and Unreal Tournament.
The advantage of UDP is that it\'s fast, and that you don\'t have to
maintain a connection. However, for whatever reason, the people at
Origin (the company that developed UO) decided that they were going to
use the TCP/IP protocol instead. This means that there is a constant
connection over the internet between your client and someone else\'s UO
server. Or, if you run a server, there are many clients with constant
connections to your server. If you want to see how many TCP/IP
connections your computer is currently maintaining, go to a command
prompt in Windows or Unix and type \"netstat\".

Some protocols (such as HTTP and SMTP) were designed so that humans
could easily emulate them. For example, if you connect using a simple
telnet client to a mail server, you can type the same commands that your
mail program would send, and the mail would be sent exactly as though
you used Netscape or Outlook to send it. A sample communication with a
mail server might look something like the following:

`<spherescript color="">`{=html}HELO 220 Hello! I\'m rit.edu! Pleased to
meet you! MAIL FROM:\<joe@joesmail.com\> 250 Email address accepted RCPT
TO:\<joesfriend@joesmail.com\> 250 Recipient address accepted DATA 250
Okay, end with `<CRLF>`{=html}.`<CRLF>`{=html} Subject: Hello!

This is a test email. .`</spherescript>`{=html}

As you can see, any person reading this transmission would know exactly
what was happening. The SMTP protocol is what we call a plain-text
protocol. It uses normal English words, and responds as though it\'s
talking to a person. The protocol used by the UO server/client (UOP) is
slightly different. It is sent as a simple stream of data which no one
could understand unless they knew how to interpret it. However, to help
the client and server do their jobs better, Origin decided that it would
be best to use clumps of data to send commands back and forth. One
\"clump\" of data that describes one of those EFFECT command animations
might contain the following information:

-   That this command tells the client how to display an effect
-   Which type of effect we\'re using
-   Which item is used in the effect
-   Who is the source of the effect?
-   Who is the destination of the effect?
-   Should the effect change direction to follow the target?
-   Should the effect explode when it hits the target?
-   What color is the effect?
-   Is the effect transparent?
-   \... Many more things \...

A clump of data describing the local light level to a player probably
contains much less information:

-   That this command is telling the client about the local light level
-   The player in question
-   The light level

So, each clump of data has a few things in common. Each performs exactly
one function (displaying an item, displaying an effect, displaying a
character, changing the light level). Each clump is capable of
identifying itself to the client, and each clump contains a bit of
additional information as necessary. These bits of data have a name. In
the world of programming, we\'d call these clumps of data \"packets.\" A
packet is simply a collection of data that is sent as part of a protocol
between two computers. In the case of UO, these packets tell the server
and the client what the other is doing. There are packets for anything
and everything you can do in the game, from using a skill to displaying
your radar to opening a container. Even the process of logging in and
out require the use of special packets.

You can find a list of these packets
[here](http://jerrith.com/projects/JUOPackets.doc). That link will take
you directly to Jerrith\'s UO Packets Guide, the most well-known guide
to UO packets on the Internet. You can find it on many sites other than
the one I\'ve linked.

After reading over that list, you\'re either very confused or very
enlightened. You now know that when you do something in the game, the
client will send a packet to the server informing it of your actions.
You also know that the server sends a lot of packets to the client
telling it to display certain things (items, characters, etc) or to
perform certain actions (change the light level). Other packets are
simply a response to an information request. When you open your status
window, your client sends a packet to the server, which asks it for your
character information. The server replies with a different packet,
detailing your character\'s strength, dexterity, intelligence, and all
of the other vital information for that status window.

You may also notice references to bytes and lengths and sizes in that
packet guide. We\'re going to have to introduce another new concept
here. All computers think in a numbering system known as binary. The
binary numbering system consists of only 2 digits (0/1). When a computer
sends data to another computer over a network, the data is also sent in
binary. Instead of sending letters and numbers, it sends a long string
of zeros and ones. When you store music or images or programs on your
computer, they are stored on your hard drive not as those things, but as
long strings of zeros and ones. The advantage of doing this is that
it\'s convenient for the hardware. Hardware that works with zeros and
ones to perform a task is known as digital hardware. Tasks performed on
those zeros and ones are digital logic. When we talk about those zeros
and ones, we refer to them as bits (which is a contraction of \"binary
digit\").

In binary, each bit represents a power of two. Just like in our base-10
(decimal) system that we use every day, each digit represents a power of
ten. The number 1564 can be represented as the sum of powers of ten. For
example:

`<spherescript color="">`{=html}1564 = 1\*1000 + 5\*100 + 6\*10 + 4\*1

1000 = 10 \^ 3

`100 = 10 ^ 2 `

` 10 = 10 ^ 1 `

`  1 = 10 ^ 0``</spherescript>`{=html}

In the same way, a binary number can represent any number by using
powers of two. Here\'s a short table of some bytes in binary and how
they can be expanded into powers of two. If you would add and multiply
those expressions, you would find that they add up to a decimal number.
This means that for every decimal number, there is a number to match in
binary. In fact, any number can be represented in ANY number base,
without changing the value of the number. Certainly, you\'ll change what
it looks like to a human, but you won\'t change the actual numeric value
of the number.

  ---------- ---------------------------------------------------------------------------------------
  10010101   1 \* 2 7 + 0 \* 2 6 + 0 \* 2 5 + 1 \* 2 4 + 0 \* 2 3 + 1 \* 2 2 + 0 \* 2 1 + 1 \* 2 0
  10011100   1 \* 2 7 + 0 \* 2 6 + 0 \* 2 5 + 1 \* 2 4 + 1 \* 2 3 + 1 \* 2 2 + 0 \* 2 1 + 0 \* 2 0
  00100011   0 \* 2 7 + 0 \* 2 6 + 1 \* 2 5 + 0 \* 2 4 + 0 \* 2 3 + 0 \* 2 2 + 1 \* 2 1 + 1 \* 2 0
  01000101   0 \* 2 7 + 1 \* 2 6 + 0 \* 2 5 + 0 \* 2 4 + 0 \* 2 3 + 1 \* 2 2 + 0 \* 2 1 + 1 \* 2 0
  00000011   0 \* 2 7 + 0 \* 2 6 + 0 \* 2 5 + 0 \* 2 4 + 0 \* 2 3 + 0 \* 2 2 + 1 \* 2 1 + 1 \* 2 0
  ---------- ---------------------------------------------------------------------------------------

So, as you can see, powers of two are very important to the computer and
to the computer programmer. So, when someone decided that we needed to
make groupings of bits (similar to the way that we have groupings called
hundreds and thousands in the decimal system), they decided they were
going to use powers of two to group them. The smallest grouping of bits
is called a nibble. A nibble is equal to exactly 4 binary digits. For
example, 1001 and 0001 are nibbles, but 0001010 consists of more than
one nibble. Can you spot them? You\'re right, the two nibbles in 0001010
are 0000 and 1010. Adding a zero to the front of a binary number does
not change its value.

The second and most important division of binary numbers is called the
byte. A byte is exactly 8 bits and is the basic unit of storage on any
sort of device. Your computer probably uses gigabytes, megabytes, and
kilobytes on a regular basis. You probably know from school that the
prefix \"kilo\" usually means 1000. For example, a kilometer is exactly
1000 meters. However, in keeping with our practice of using powers of 2,
the people who invented the computer decided that one kilobyte should be
1024 (2 10 ) bytes. A megabyte is exactly 1024 kilobytes, which means
that one megabyte is equal to 1048576 (1024 2 )bytes. A gigabyte is
equal to 1024 megabytes, so one gigabyte is equal to 1073741824 (1024 3
) bytes. Transforming these numbers into binary brings us to the
not-so-surprising realization that the two larger numbers are also
powers of 2. (If you think about it, you\'ll also realize that RAM comes
in quantities of 32 MB, 64 MB, 128 MB, 256 MB, 512 MB, and 1024 MB. Each
of those numbers is, of course, a power of two.)

However, we\'re not going to be using anything close to even a kilobyte
when we play with packets. The vast majority of computers store numbers
in one of three sizes: 1 byte, 2 bytes (a word), or 4 bytes (a double
word, or dword). You will, of course, notice that 1, 2 and 4 are powers
of two. In fact, data is almost never stored in 3 bytes or 5 bytes.
Sometimes it\'s stored in 8 bytes, which is the next power of two after
4. Later, I might refer to these numbers using their bit equivalences. 1
byte is 8 bits, 2 bytes is 16 bites, and 4 bytes is 32 bits.

(Sidenote: The fact that 2 bytes is 16 bits and 4 bytes is 32 bits is
also important in computing. The 32 in \"Win32\" or \"FAT32\" is the
same number that appears in the phrase \"32-bit.\" The reason for this
is far too complicated for this tutorial, but it deals with the fact
that memory is now represented by one 32-bit, or four byte, number
instead of two 16-bit, or two byte, numbers.)

Now, Jerrith\'s packet guide might make a bit more sense when it\'s
referring to certain numbers of bytes and bits. Let\'s look at an
example packet from the guide:

**0x05 Packet**\
**Attack Request (5 bytes)**\
\
\* **BYTE cmd**

-   **BYTE\[4\] ID to be attacked**

The first two lines tell us the number of the packet and a short
description. Sometimes these descriptions are a bit cryptic, but I chose
this one because it\'s obvious. This packet is sent to the server by the
client when the player double-clicks on someone in war mode. It is
actually requesting permission from the server to attack something on
the screen. The next lines are the actual data that must be sent with
this packet. The first bulleted line tells us that we need to send a
piece of data that is 1 byte long. This data must represent the command
we\'re sending. In the last line, BYTE\[4\] means that value should be
represented using 4 bytes. If you look at a UID in the game, you\'ll
find that it is indeed represented by exactly 4 bytes. Also, when you
see a number preceded by 0x, such as 0x4A, it means that number is in
hexadecimal. The SPHERE equivalent is 04A.

Generally packets have this format. The first byte of any packet is the
ID of that packet. So in our case, the first byte is going to contain
the number 05. The four bytes following that one are going to be the UID
of the character that\'s being attacked. The client knows the UIDs of
characters on the client\'s display as well as the server, and can
inform the server which character is being attacked by the player.

Now, finally, we reach the formatting of the SENDPACKET command. It\'s a
bit confusing and very different than anything you\'ve seen before.

**SENDPACKET**\
**Type:** Client Function\
**Usage:** SENDPACKET \<bytes in hexadecimal\>\
**Description:** The SENDPACKET function sends the bytes specified
exactly as-is to the client. If the client isn\'t expecting that
command, or the command is not formed correctly, the client WILL crash.
All SENDPACKET strings must therefore be perfectly formed and expected.

**Example:**\
`<spherescript>`{=html}SENDPACKET 05 040 00 010 011 // Sends an attack
request (in the wrong direction) to attack player with UID
040001011`</spherescript>`{=html}

You\'ll notice that the bytes must be represented in hexadecimal. 1 byte
is exactly 2 hexadecimal digits. (In the example above, those bytes are
05 40 00 10 11.) This is not difficult. Most numbers in UO are already
represented in hexadecimal when displayed. However, just to be sure, you
can force a number to display in hex by using the HVAL function: \<HVAL
`<number>`{=html}\>

The real problem arises when we realize that the SENDPACKET function
treats each number as a single byte, but most of our numbers are
displayed as longer numbers. A UID is diaplyed as 040001011, not 040 000
010 011. In the past we had to create the most hieous function I\'ve
ever seen to take care of this problem, but now we can actually prefix
each number with a character that identifies how many bytes a number
should fill. These prefixes are B (1 byte), W (word, 2 bytes) and D
(dword, 4 bytes). Our example above could be rewritten to become:

`<spherescript>`{=html}SENDPACKET 05 D040001011 // Sends an attack
request (in the wrong direction) to attack player with UID
040001011`</spherescript>`{=html}

This tells Sphere that the number 040001011 is a DWORD value and should
fill 4 bytes. The same thing works with smaller number, `D01` would be
the same as writing `00 00 00 01`.

So, finally, we have all of the tools we need to use SENDPACKET
successfully! Scroll up and see how far we\'ve come. Don\'t get lost.
When you return, we\'ll take a look at a script that alters the personal
light level of a player (like nightsight) without altering the base
light level. It turns out that there\'s actually a separate packet for
personal light and global light.

**0x4E Packet**\
**Personal Light Level (6 bytes)**\
\
\* **BYTE cmd**

-   **BYTE\[4\] creature id**
-   **BYTE level**

We\'ve got three parameters we need to provide here. We need a one-byte
command ID (04E in this case), a 4-byte creature id (the UID of the
person whose light level we\'re changing), and a one-byte level. So,
let\'s form the SENDPACKET command:

`<spherescript>`{=html}\[FUNCTION change_light_level\] // Usage:
change_light_level lightlevel SENDPACKET 04E D`<UID>`{=html}
\<ARGV\[0\]\>`</spherescript>`{=html}

That isn\'t very hard, is it? The first byte is 04E, which is the
command ID. The second 4 bytes are provided by prefixing the UID with a
\"D\", and they represent the UID of the person whose light level we are
changing. The last byte is given in the argument to the function. Don\'t
worry too much about what happens if the value of ARGV\[0\] does not fit
into a single byte (e.g. 010292). Since we did not prefix the value with
a W or D, Sphere will assume that the value is intended to be a single
byte and will treat it as such, although obviously the value 010292
won\'t fit into a byte so the value will be something else completely.
If you\'re worried about invalid values being passed into the function
then you should add some form of validation (for example,
`IF (<ARGV[0]&gt> < 30`).

That was easy, wasn\'t it? Now let\'s look at a more complicated
function, written by Acratia and altered to use Sphere\'s W and D
prefixes:

`<spherescript>`{=html}\[FUNCTION huedeffect\] // Usage: huedeffect
type,itemid,speed,frames,explode,hue,rendermode SERV.ALLCLIENTS
SENDPACKET 0C0 \<ARGV\[0\]\> D\<SRC.UID\> D`<UID>`{=html} W\<ARGV\[1\]\>
W\<SRC.P.X\> W\<SRC.P.Y\> \<SRC.P.Z\> W\<P.X\> W\<P.Y\> \<P.Z\>
\<ARGV\[2\]\> \<ARGV\[3\]\> 00 00 00 \<ARGV\[4\]\> D\<ARGV\[5\]\>
D\<ARGV\[6\]\>`</spherescript>`{=html}

We see here that this command requires a lot of information, which
explains the long script. Actually, the best idea would be to break the
script down into its constituent pieces. You\'ll see that each piece
corresponds to a part of the packet description.

  ---------------- ------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Data**         **Length**   **Description**
  0C0              1 byte       The command ID
  \<ARGV\[0\]\>    1 byte       The first argument, which is a one-byte EFFECT type
  D\<SRC.UID\>     4 bytes      The UID of the source of the effect
  D\<UID\>         4 bytes      The UID of the target of the effect
  W\<ARGV\[1\]\>   2 bytes      The ID of the item to display as the effect
  W\<SRC.P.X\>     2 bytes      The X coordinate of the source
  W\<SRC.P.Y\>     2 bytes      The Y coordinate of the source
  \<SRC.P.Z\>      1 byte       The Z coordinate of the source
  W\<P.X\>         2 bytes      The X coordinate of the destination
  W\<P.Y\>         2 bytes      The Y coordinate of the destination
  \<P.Z\>          1 byte       The Z coordinate of the destination
  \<ARGV\[2\]\>    1 byte       The speed of the effect (if it\'s flying)
  \<ARGV\[3\]\>    1 byte       The duration of the effect (in animation frames)
  00 00            2 bytes      This is marked in the packet guide as \"unknown.\" Usually, if something is unknown, it\'s safe to leave it as 0, so we put two 0 bytes here. It would also be safe to do this: `W00`
  00               1 byte       Fixed direction. I\'m not sure what this means, but we\'re going to set it to zero since we\'re not sure. It does not adversely affect the script.
  \<ARGV\[4\]\>    1 byte       Explosion. This should either be a 1 or a 0, depending on if you want an explosion or not.
  D\<ARGV\[5\]\>   4 bytes      The hue of the effect. I wasn\'t aware that hues were 4 bytes, but apparently they are. That\'s odd, because SPHERE represents colors as 2 bytes. Anyway, the D prefix doesn\'t care how many bytes you give it. You\'re getting four in the return value, no matter what.
  D\<ARGV\[6\]\>   4 bytes      Change the seventh argument into a 4-byte number.
  ---------------- ------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Interestingly enough, this \"render mode\" number determines
transparency or fading of effects. This could lead to some fun things.

See? After we split it into its constituent parts, it isn\'t very
difficult at all. In fact, the only thing that remains a mystery is the
fact that we\'re using SERV.ALLCLIENTS with this command. That\'s simple
when you think about it as well. The only people who will see this
effect are those who receive the packet. Therefore, if we want everyone
in the area to see the effect, we need to send everyone the packet. The
only way to be absolutely certain that everyone in an area receives a
packet is to send it to the entire server. Certainly, it\'ll increase
lag by an infinitesimal amount to send 36 bytes to 200 players, but
that\'s the price you pay for colored effects.

And that\'s about it for sending packets. Maybe later I\'ll post a way
to divide a string up into packets, unless one of the other gurus gets
there first. SENDPACKET is actually very simple. However, it does have a
few limitations:

It can\'t do anything for which there is no packet. This one should seem
obvious. An example is an idea that proposed coloring tilepics in gumps.
The client simply doesn\'t support that, so we can\'t do it. It can\'t
do anything that requires two-way communication. For example, you could
send a dialog to the client using a very very long SENDPACKET, but the
server won\'t be expecting a response, and you won\'t be able to handle
events in your dialog. It could become very laggy if you send a lot of
huge packets to a lot of players. Different clients support different
packets. I believe that the hued effects are relatively new, so older
clients like 2.0.0 or 1.26.4 may not support them. Clients greater than
about 2.0.7 should support all packets listed in the Guide. And that\'s
it. Easy, right? :)

[Category: Articles](./_Articles.md)
