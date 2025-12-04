## Basic String Explanation

This section will explain how to handle strings (separation, comparing,transforming, reversing, storing). Hope you enjoy it.

First, we're gonna start with the separations ways of Sphere. The most common and simple is using comma (,). Most of Sphere's functions use it as a separator and it is easier than using a space. Also, the space is a valid one but not really used at all. With this function you can see why:

\[FUNCTION f_test\] `SERV.LOG` Arguments :: <ARGV> `SERV.LOG` Arg. 1 :: \<ARGV\[0\]\> `SERV.LOG` Arg. 2 :: \<ARGV\[1\]\> `SERV.LOG` Arg. 3 :: \<ARGV\[2\]\> `SERV.LOG` Arg. 4 :: \<ARGV\[3\]\>

```
If we enter "<font color="darkred">.f_test Hello to all World</font>" in-game we should see something like this in the Sphere console:

23:01:(Test.scp,2)Arguments :: 1 23:01:(Test.scp,3)Arg. 1 :: Hello To all World 23:01:(Test.scp,4)Arg. 2 :: 23:01:(Test.scp,5)Arg. 3 :: 23:01:(Test.scp,6)Arg. 4 ::


This means that we have only 1 argument and it's our complete string. This is not too useful because later we will have to cut it using the [STRARG](#STRARG "wikilink") or [STREAT](#STREAT "wikilink") functions. But if we check what happens if we use commas, by typing "<font color="darkred">.f_test Hello,to,all,World</font>":

23:02:(Test.scp,2)Arguments :: 4 23:02:(Test.scp,3)Arg. 1 :: Hello 23:02:(Test.scp,4)Arg. 2 :: To 23:02:(Test.scp,5)Arg. 3 :: All 23:02:(Test.scp,6)Arg. 4 :: World

We now have the whole string separated into arguments ready for our script. Pretty Simple, uh? Well, this is just the start.

We can do almost whatever we want with a string: Comparing, cutting, removing, moving, etc.. To see all of the valid functions check the [list below](#String_Functions "wikilink"). They're heavily explained.

```
## String Functions
```

```
### EXPLODE
```

The EXPLODE function can be used to convert a string into a comma-delimited list based on one or more delimiters. The resultant string can then be passed into a function where you can then use ARGV to access the individual pieces.

The syntax for the command is: `EXPLODE separators, string_to_separate`

See the following example, which separates a string by both the "-" and "+" characters and logs the output to the Sphere console:

\[FUNCTION f_explode\] F_EXPLODE_LOG \<EXPLODE -+,<ARGS>\> // separate string by - and +, passing result into the F_EXPLODE_LOG function

\[FUNCTION f_explode_log\] SERV.LOG ARGV Length = <ARGV> // output number of comma-separated arguments FOR 0 \<EVAL (<ARGV> - 1)\> // loop through each argument

`   SERV.LOG ARGV[<LOCAL._FOR>] = <ARGV[<LOCAL._FOR>]>  // output individual arguments`

ENDFOR
```

### STRARG

STRARG can be used to extract the first word from a string. The following example demonstrates this:

\[FUNCTION f_strarg\] `SERV.LOG` <STRARG One Two Three>

You will see the word "One" output to the console.

### STREAT

STREAT is the counterpart function to STRARG. Whereas STRARG gives you the first word in a string, STREAT will 'eat' the first word from a string and return the remaining text. The following code shows the difference:

\[FUNCTION f_streat\] `SERV.LOG` <STREAT One Two Three>

You will see the text "Two Three" output to the console.

### STRCMP

Sooner or later you may find the need to compare one string to another. You may start out by attempting to write the following line:

```
IF ("String1" == "String2")

If you tried to do that you would find an ugly looking error on the Sphere console, and your IF statement would simply not work correctly at all. This is because IF statements are designed to compare numerical values, and so cannot understand how it can compare two strings.

So you need to find out if "String1" is equal to "String2", right? Well, that's why we have STRCMP. Let's look at the basics of it.

`STRCMP(string1, string2)`

Now, before you start to use this you should be aware that this function does not simply compare two strings for equality. STRCMP actualls compares two strings to determine if they are less than, greater than, or equal to each other! Therefore, this function has three different return values:

```
|                  |                                 |
|------------------|---------------------------------|
| **Return Value** | **Meaning**                     |
| -1               | string1 is less than string2    |
| 0                | The two strings are equal       |
| 1                | string1 is greater than string2 |
```

It's important to bear these return values in mind when using the function, as you will quickly discover, the function actually returns *false* (0) when the two strings are equal to each other!

Take a look at the following at the following example:

IF !(STRCMP(\<SRC.NAME\>, Tiny))

`   SRC.SAY My name is Tiny!`

ENDIF

You might be asking, "Why didn't you have to surround the function with \< \> there?".

Well, STRCMP is not a 'normal' function. It is known as an *[intrinsic function](intrinsic_function "wikilink")*, a special kind of function that can only be used inside an \<EVAL ...\> statement and rather than being surrounded by \< \> it instead has its arguments surrounded by brackets ( ).

"Wait, but that STRCMP *isn't* inside an EVAL!?" you may say, but this is not actually the case. Inside conditional statements (such as[IF](IF "wikilink") and [WHILE](WHILE "wikilink")), Sphere automatically treats the entire line as if it were inside an EVAL function, and so the above script will work fine for comparing strings.

Another thing you should remember is that STRCMP is case-sensitive, and so "STRING1" will not be equal to "string1". If you want to perform a case-insensitive comparison, use [STRCMPI](#STRCMPI "wikilink") instead.

```
### STRCMPI
```

The STRCMPI function can be used to compare two strings, ignoring their case. Apart from being case-insensitive this function is identical to [STRCMP](#STRCMP "wikilink").

```
### STRLEN
```

This function can be used to count the number of characters in a string. For example:

LOCAL.LENGTH = \<EVAL STRLEN(<ARGS>)\>

Let's say the value of ARGS is "This one has 26 characters". The value of LOCAL.LENGTH will be 26.

```
### STRPOS
```

The STRPOS function can be used to locate the position of a particular character within some text. The syntax of the command is:

`STRPOS pos ch string`

```
|  |  |
|----|----|
| **Parameter** | **Meaning** |
| pos | The position to start searching from (first character is position 0) |
| ch | The character to search for, or the ASCII code of the character |
| string | The text to search in |
```

Here are a couple of examples:

LOCAL.POS = \<STRPOS 0 32 Where is the first space\> // returns 5 LOCAL.POS = \<STRPOS 3 e Where is the first 'e'\> // returns 4

```
### STRREVERSE
```

This function simply reverses the order of a string. For example:

SERV.LOG <STRREVERSE Hello>

The above line of code will output "olleH" into the console.

```
### STRSUB
```

STRSUB is used to extract a series of characters from a string. Why is it useful? Well I can't think of a specific reason right now, but I'm sure you'll be able to handle that.

\[FUNCTION TestStrSub\] SERV.LOG \<STRSUB 0 1 Hello\>

As you can see, STRSUB takes three parameters. The first parameter is the start location (zero-based). The second parameter is the length. Finally, the third parameter is the string in question.

If you were to use that function in-game, then look at your Sphere console, you'll see that it prints the first character from the third position. One thing I need to point out is the index (first parameter) is zero-based. If you wanted to start at the first character of the string, you'll need to use zero. The second parameter simply tells Sphere how many characters we need returned, starting from the index.

Specifying a negative value for the index will tell Sphere to begin at the end of the string, and count backwards from there. Here's an example:

\[FUNCTION TestStrSub\] SERV.LOG \<STRSUB -1 1 Hello\>

Use the function in-game once again, then look at your Sphere console. Amazingly, it prints the last character of the string.

That isn't too difficult, is it?

```
### STRTOLOWER
```

This function simply converts all uppercases characters to lowercase. A simple example would be:

LOCAL.LOWER = <STRTOLOWER StRiNgS ArE fUn To PlAy WiTh>

The function will return "strings are fun to play with".

```
### STRTOUPPER
```

This function performs the opposite action to [STRTOLOWER](#STRTOLOWER "wikilink"). It converts all lowercase characters to uppercase. Following on from the previous example:

LOCAL.UPPER = <STRTOUPPER StRiNgS ArE fUn To PlAy WiTh>

The function will return "STRINGS ARE FUN TO PLAY WITH".

```
### STRTRIM
```

This function be used to strip all whitespace (spaces, tabs, newlines) from the start and end of a string.

The following script demonstrates this:

\[FUNCTION f_strtrim\] LOCAL.TEXT = " TEST " SERV.LOG 1. \<LOCAL.TEXT\> SERV.LOG 2. \<STRTRIM \<LOCAL.TEXT\>\>

When run, the following output will be seen on the Sphere console:

`1.      TEST     `
`2. TEST`

```
### STRMATCH
```

The STRMATCH function enables you to check if a string matches a simple expression using wildcards (\*), which you have more than likely encountered before.

The syntax of this function is `STRMATCH(pattern, string)`. It will return 1 if the string matches the pattern, and 0 if it doesn't. Look at the following example script:

\[FUNCTION f_strmatch\] IF (STRMATCH(\*ex\*, <ARGS>))

`   SERV.LOG ARGS contains 'ex'!`

ELSE

`   SERV.LOG ARGS does not match.`

ENDIF

In the Sphere console type <font color="darkred">F_STRMATCH Mexico</font>. You will see the message "ARGS contains 'ex'!". You can try experimenting with different arguments and changing the pattern around until you get the hang of this.

Had fun? STRMATCH is actually slightly more powerful than this. \* isn't actually the only special character that you can use inside the pattern text:

```
| **Pattern** | **Meaning** |
| ------------- | ------------------------------------------------ |
| * | Matches any number of characters, including none |
| ? | Matches any one single character |
| [\*] | Matches the '*' character |
| [abcdef] | Matches any of the characters in the list |
| [!abc] [^abc] | Matches any characters not in the list |
| [a-z] | Matches any character between A and Z. |
```

That's everything there is that you need to know about STRMATCH. A finally note however, is that the pattern will be case-insensitive. (the`*ex*` example will match on "TEXT")

**Note:** Some users have also found that the STRMATCH function is a convenient way of determining if two strings are equal (i.e`IF (STRMATCH(string1, string2))`). This is not how the function was intended to be used and you will be at a disadvantage for doing so:

- Sphere will still attempt to perform a pattern match, wasting CPU
  resources.
- When a wildcard is used in the first string, you may not get the
  result you want (imagine something similar to`STRMATCH(`<ARGS>`, SOMETEXT))`,, and ARGS happens to contain *\*MET\**)

If you want to check the equality of two strings, use either the [STRCMP](#STRCMP "wikilink") or [STRCMPI](#STRCMPI "wikilink") function.

```
### STRREGEX
```

As useful as STRMATCH is, it is unfortunately not powerful enough to match more precise patterns.

Imagine you want to check if a string contains a floating point number (a number that may have one or more decimal places). Using STRMATCH we may start out with something like this:

\[FUNCTION f_fpmatch\] IF (STRMATCH(\[0-9\].\[0-9\],<ARGS>))

`   SERV.LOG `<ARGS>` is a floating point number.`

ELSE

`   SERV.LOG `<ARGS>` is NOT a floating point number.`

ENDIF

If we type <font color="darkred">F_FPMATCH 1.0</font> in the Sphere console the match will be successful, however if we attempt to enter a number larger than 9.9 or a number that doesn't have exactly 1 decimal place then it will not match. We could add more "\[0-9\]"s in the STRMATCH but this would not solve the problem since we'd have to enter a fixed amount of numbers regardless. For example if we tried `STRMATCH([0-9][0-9][0-9].[0-9][0-9][0-9], <ARGS>)` Then we'd have to enter 001.500 for the match to work for 1.5!

STRREGEX solves this problem by using the regular expression language to perform advanced pattern matching. In fact, it is so advanced that the patterns are almost a language of their own, and there would be way too much to document here! To learn about the regular expression patterns, you want to visit one of the many websites that are dedicated to documenting regular expressions, such as [regular-expressions.info](http://www.regular-expressions.info/tutorial.html).

To match a floating point using regular expressions, we can use the following pattern:

^\[-+\]?\[0-9\]\*\\?\[0-9\]+\$

If you don't understand the regular expression language then that will probably look like a random set of symbols, and believe me when I say that is actually a simple example of a regular expression! Fortunately, you can trust for now that the pattern is correct, and that we can use this in STRREGEX. The function above can be modified to the following:

\[FUNCTION f_fpmatch\] IF (STRREGEX(^\[-+\]?\[0-9\]\*\\?\[0-9\]+\$, <ARGS>))

`   SERV.LOG `<ARGS>` is a floating point number.`

ELSE

`   SERV.LOG `<ARGS>` is NOT a floating point number.`

ENDIF

As complicated as that looks it does the job well. For example it matches values such as "1.5", "-250.002", "50", and even ".007"!

[Category:Tutorials](Category:Tutorials "wikilink")
```
