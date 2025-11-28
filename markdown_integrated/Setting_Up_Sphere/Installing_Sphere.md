## Windows

Start by downloading Sphere. See the [Where to get
Sphere](Where_to_get_Sphere "wikilink") page for download links. You
should end up with two different zip files, one containing the Sphere
executable and the other containing the [Script
Pack](Script_Pack "wikilink").

1.  Extract the SphereServer.zip file to wherever you want to run it
    from. I would recommend "c:\sphere"
2.  Extract Scripts.zip to the directory where you previously extracted
    the file in the previous step. Now you should have the directory
    scripts in "c:\sphere".
3.  Create three new folders, one named "accounts", another called
    "logs", and the third one called "save".
4.  Now, go to your "save" folder, recently created. And create an empty
    text file (I recommend using the Start Menu to access Notepad
    instead of "Right Click =\> New"). Write an empty line and add
    "\[EOF\]" in the second one. Save the file as "spheredata.SCP" (not
    .txt).
5.  Copy this file four times an rename them as: spherestatics,
    spherechars.scp, spheremultis.scp and sphereworld.scp
6.  Now, [configure your sphere.ini](Configuring_Sphere.ini "wikilink").
    This is a must before running Sphere for the first time!
7.  Double Click on SphereSvr.exe to launch the Console. This black
    window is your server console from which you can enter commands.
8.  Create an Account for yourself. In the console, type in
    "<font color="darkred">account add USERNAME PASSWORD</font>". With
    whatever username and password you want. Then, type in
    "<font color="darkred">account USERNAME plevel 7</font>" to grant
    your account Owner privileges.

Now you can go around your map and explore some parts of it. You can use
the navigation bar on the left to read various tutorials to learn how to
script and learn something about Sphere. After that, read the other
articles and check the [reference
compendium](Main_Page#Reference_Compendium "wikilink") if you need
something special.

## Linux

### Preface

Installing Sphere on a Linux box is not more difficult as doing this
task on a Windows PC. Either way you will have to have basic knowledge
about your operation system, and you should not rely on that you simply
have to doubleclick like mad to get the beast up and running.

Even more, this tutorial will assume that you are using a shell on the
linux box, and that you have root access. You do not trust your skills
to type a command without mistakes, or no one will trust your knowledge
enough to give you system administrator privileges on his Linux PC?
Well, then - your busted. Go home, and play Solitaire on a neat little
Windows box, ok?

Finally, this tutorial will NOT cover the ways to get the necessary
files onto the Linux server. If you cannot figure this out yourself -
read the last sentence of the paragraph before. THIS IS NOT A LESSON
"Linux for Dummies"! Do your homework, and learn. There are many books
about Linux' basics, even E-Books you can download free of charge.
Surfing to [<http://www.linux.org>](http://www.linux.org) will be a good
point to start.

One last word about syntax: LINUX commands and filenames are case
sensitive! So if later on a file cannot be found it usually is because
you typed something like "sphere.INI" instead of "sphere.ini".

And in this document lines in italics are denoting what you have to type
into (or read from) the shell.

### Preparations

On the Linux box you will need a MySQL client installation. You do not
need a server if you do not plan to use the database features, but
Sphere will not start without the proper MySQL client libraries. Period.

You also need access to a Sphere prerelease FOR LINUX, the default
script package for this version, and eventually additional libraries
(libboost for recent releases).

### Installation Step-By-Step

**1)** As user root, create a user named 'sphere'. Set or create it's
home directory (usually /home/sphere/), give it the correct owner and
permissions:

`useradd -d /home/sphere sphere`  
`mkdir /home/sphere`  
`chown sphere /home/sphere`  
`chmod 700 /home/sphere`

**2)** Copy the files from the Sphere LINUX package and the scriptpack
into this newly created directory. Create all missing directories like
"save", "logs", "accounts" as they are named in your sphere.ini and
spheretables.scp. You should end up with a structure like this:

`/home/sphere --- spheresvr`  
`               | sphere.ini`  
`               | sphereCrypt.ini`  
`               |-------------------- accounts/`  
`               |-------------------- logs/`  
`               |-------------------- muls/`  
`               |-------------------- save/`  
`               |-------------------- scripts/`

**3)** After copying all related files to their respective positions,
make sure that they all have the correct permissions and ownerships.
Still as root do:

`cd ~sphere`  
`chown -R sphere *`  
`find . -type d | xargs chmod 0700`  
`find . -type f | xargs chmod 0600`  
`chmod 4700 spheresvr`

**4)** Still as root, print the shared library dependencies:

`ldd spheresvr`

the output should be something like this:

`longbow:/home/sphere# ldd spheresvr`  
`libpthread.so.0 => /lib/libpthread.so.0 (0x4001f000)`  
`libmysqlclient.so.15 => /usr/lib/libmysqlclient.so.15 (0x40071000)`  
`libboost_regex-gcc-1_33_1.so => /usr/lib/libboost_regex-gcc-1_33_1.so (0x40243000)`  
`libstdc++.so.6 => /usr/lib/libstdc++.so.6 (0x402ea000)`  
`libm.so.6 => /lib/libm.so.6 (0x403c9000)`  
`libgcc_s.so.1 => /lib/libgcc_s.so.1 (0x403ef000)`  
`libc.so.6 => /lib/libc.so.6 (0x403fa000)`  
`/lib/ld-linux.so.2 (0x40000000)`  
`libcrypt.so.1 => /lib/libcrypt.so.1 (0x4051c000)`  
`libnsl.so.1 => /lib/libnsl.so.1 (0x4054a000)`  
`libz.so.1 => /usr/lib/libz.so.1 (0x40561000)`

<strong>LOOK FOR MISSING LIBRARIES!</strong> If something is missing,
just install it. You should know how to do. If it's just libboost what
is missing, you have got this with the preparations. Copy it into
/usr/lib/ and type:

`ldconfig`

### Test the Installation

It does matter if you start your test as user *root* or user *sphere*...
But setting the permissions of the spheresvr executable to 4700 forces
it to always be started as it's owner, and if you followed the earlier
instuctions, that owner is *sphere*. So start it like this:

`cd ~sphere`  
`./spheresvr`

You will get the usual startup yaddayadda, perhaps including some
warnings such as:

`longbow:/home/sphere# ./spheresvr`  
`WARNING:(sphere.ini,587)'scripts/spherestatusbase.html' not found...`  
`ERROR:(sphere.ini,587)Can't open web page input 'spherestatusbase1.htm'`  
`Sphere Version 0.56b [Linux] by www.sphereserver.com, compiled at Sep 15 2006 (23:23:07)`  
`Signal handlers installed.`  
`Expansion maps supported: T2A, LBR, AOS, SE, ML`  
`ERROR:(spheretables.scp,59)Unable to open directory scripts/custom/`  
`ERROR:(spheretables.scp,59)DirList=-1 for 'scripts/custom/'`  
`Allocating map sectors: 0=7168 1=7168 2=900 3=1280 4=32761`  
`Indexing 211 scripts...`  
`Loading scripts/sphere_defs.scp`  
`[...]`

Finally your Sphere will tell you something like:

`[...]`  
`Loading save/spheredata...`  
`Loading save/spherestatics...`  
`Loading save/sphereworld...`  
`Loading save/spherechars...`  
`166 Objects accounted for`  
`Option flags: CommandSysmsgs + NoHouseMuteSpeech`  
`Experimental flags: DiagonalWalkCheck + ScriptsReturnStrings + NewTriggersEnable + NewPositionChecks + WalkCheck + ScriptProfiler + SizeOptimize`  
`Admin=me@my.email.com, URL=www.myshard.com, Lang=English, TZ=0`  
`Startup complete. items=0, chars=0`  
`Creating thread.`

You can safely ignore script warnings and errors regarding missing web
pages. But if the sphere issues other errors, or terminates, dont just
stare at the error number like the rabbit stares at the snake: The text
immediately above the error will tell you what's wrong. So fix it. For
example, after starting the server, if you see errors like:

`16:55:FATAL:Segmentation fault 16:55:FATAL:Error Pri=1, Code=11, Desc='Segmentation fault', in CChar::CanMoveWalkTo() #1 "Check Valid Move"`

...the filesystem ACLs may be wrong, specifically the ACLs on the UO mul
and uop files in the UO client directory. There are numerous solutions,
but one way to fix this is to change the permissions on these files to
644.

But I digress.... Assuming no catestrophic failures, you are now in the
sphere console and can issue the common commands (type '?' to get a
list). So create an account, activate it, edit the login.cfg (or host
details) on your windows box with the client installation to point to
the address of the Linux box, and be the first to log in.

To stop the Sphere, type 'S' in the console, then 'x'. Linux will tell
you something about deinstalling handlers and shutting down. But often
it will just "hang" after this, not really terminating. Clear this
situation by typing CTRL-c

### Preparing for production

Perhaps you closed your shell during the test. Then you should have
noticed that the operating system killed your Sphere at the same moment.
That's not a bug but wanted behaviour: Linux is a multi user os, and
when a user logs out processes started by him shall not accidentally
kept running.

But of course you will not be able to keep open the console all the
time, at least if your Linux box can only be reached remotely, perhaps
by ssh. If it's the main service running on the box, you should create a
startup script what starts spheresvr in an endless loop, thus restarting
it in the event it should crash. To do this, first install the 'screen'
utility using the packet manager of your distribution. Then use the text
editor of your choice and create a script like this:

`#!/bin/sh`  
`cd ~sphere`  
`while true; do`  
`screen -D -m /home/sphere/spheresvr`  
`sleep 30`  
`done`

This way the server will be run in a virtual window to what you always
can attach with 'screen -r'. Read the manpage for screen for more
information.

Then take it to the next level! Perhaps create an
/etc/init.d/sphereserver script to start, stop, or restart the server...
then softlink that script in the various /etc/rc\*.d/ directories so
that the sphere server automatically starts when the linux server is
rebooted... maybe setup a cron job to automatically rotate and archive
the log files that sphere creates.

## FreeBSD

We currently have no guide for this OS. Anyway, the developers have
posted a list of required stuff. Here is the list:

Compiled on:

`FreeBSD freebsdvbox.fastwebnet.it 7.0-RELEASE FreeBSD 7.0-RELEASE #0: Sun Feb 24 19:59:52 UTC 2008     root@logan.cse.buffalo.edu:/usr/obj/usr/src/sys/GENERIC  i386`

With:

`Using built-in specs.`  
`Target: i386-portbld-freebsd7.0`  
` Configured with: ./..//gcc-4.1-20071105/configure --disable-nls --with-system-zlib --with-libiconv-prefix=/usr/local --program-suffix=41 --libdir=/usr/local/lib/gcc-4.1.3 --with-gxx-include-dir=/usr/local/lib/gcc-4.1.3/include/c++/ --disable-rpath --prefix=/usr/local --mandir=/usr/local/man --infodir=/usr/local/info/gcc41 i386-portbld-freebsd7.0`  
`Thread model: posix`  
`gcc version 4.1.3 20071105 (prerelease)`

Linked Against:

`libthr.so.3 => /lib/libthr.so.3 (0x281f3000)`  
`libmysqlclient.so.15 => /usr/local/lib/mysql/libmysqlclient.so.15 (0x28206000)`  
`libstdc++.so.6 => /usr/lib/libstdc++.so.6 (0x28265000)`  
`libm.so.5 => /lib/libm.so.5 (0x2835a000)`  
`libgcc_s.so.1 => /lib/libgcc_s.so.1 (0x2836f000)`  
`libc.so.7 => /lib/libc.so.7 (0x2837a000)`  
`libcrypt.so.4 => /lib/libcrypt.so.4 (0x28476000)`  
`libz.so.4 => /lib/libz.so.4 (0x2848f000)`

If you use this release, please check [this
topic](http://www.sphereserver.net/index.php?showtopic=44153).

[Category: Setting Up Sphere](Category:_Setting_Up_Sphere "wikilink")
