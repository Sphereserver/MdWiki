## Common Mistakes Explained

This tutorial is a revised copy of Maximus's "Common Mistakes Explained" tutorial from the SphereServer forums for Sphere 56b.

Ideally, the following information should cut down on help requests that have already been asked and answered many times in different threads.

This tutorial is very simple and easy to read, and is a MUST for all beginner scripters... let's begin!

### Target Functions

Probably the most common mistake I've seen since in my time with Sphere is with targets being called directly from functions, like this:

\[FUNCTION target_test\] TARGET Select target

```
ON=@TargOn_Item // code here
```

This isn't going to work too well :) 56b has introduced a new targeting function, eliminating the need for memory targets - [TARGETF](TARGETF "wikilink") and its 3 different variations:

|  |  |
|----|----|
| [TARGETF](TARGETF "wikilink") | allows you to target characters and non-static items |
| **TARGETFG** | same as above only this one allows you to target the ground |
| **TARGETFW** | targst characters and non-static items, and also warns against criminal action |

Syntax:

`TARGETF[GW] function_to_be_called`

Some things to note:

- In the called function, ARGO is the targetted object
- You CAN pass arguments through the function (ex.`TARGETF F_WHATEVER <UID>`, \<UID\> being the argument) and that
  argument can be referenced in the called function
- If ground is targeted, those coordinates will be TARGP

Here is an example:

\[FUNCTION target_fun\] SYSMESSAGE Select target. // message displayed with target TARGETF f_target_fun // calls the target and the function

\[FUNCTION f_target_fun\] ARGO.SAY MY NAME IS \<ARGO.NAME\> AND I AM A CLOWN!! IF (\<ARGO.ISITEM\>)

`   ARGO.SAY I am an item too!`

```
ENDIF
```

## Comparing Strings & Tags

Sphere utilizes many different methods for comparing two pieces of information. What many users don't realize is that storage variables such as TAGs, VARs and LOCALs hold information as if it were a value, rather than either a number or a word.

```
For example, say you have a TAG on a player, TAG.TEST, that holds a word, and you want to use an IF statement to check to see if that word is "blue". Many users new to Sphere might try to do something like this:

IF (\<TAG.TEST\> == blue)

Sphere wants to compare the tag to a value, rather than a string, and so an error will be shown on the Sphere console because Sphere cannot translate "blue" into a numeric value.

For comparing strings, the most common string comparison keywords are STRCMPI and STRMATCH.

Proper syntax for the above comparison could be:

IF !STRCMPI("<VARIABLE>", "STRING") IF !STRCMPI("\<TAG.TEST\>", "blue")

-OR-

IF STRMATCH("STRING", "<VARIABLE>") IF STRMATCH("blue","\<TAG.TEST\>")

The reason for the ! (means "does not", put simply) is that STRCMPI compares two strings and returns -1 if the first string is 'less than' the second, 1 if the first string is 'greater than' the second, or 0 if the two strings are equal. So for this function we need to check if it returns FALSE (0) to see if the two strings are equal.

```
## = vs. ==
```

I can see why many scripters could be confused about the difference between a single equals sign and two of them in a row. In short, a single equals sign is an assignment operator, while the double equals sign is, well, the equals sign.

The single sign should only be used when "assigning" variables, locals, tags, etc... while the double equals sign should be used in conditional (e.g. [IF](IF "wikilink"), [WHILE](WHILE "wikilink")) statements:

LOCAL.IMNAKED = 1 // correct LOCAL.IMNAKED == 1 // incorrect

IF (\<LOCAL.IMNAKED\> == 1) // correct IF (\<LOCAL.IMNAKED\> = 1) // incorrect

[Category:Articles](Category:Articles "wikilink")
```
