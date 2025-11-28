*Skill Gain Theory*  
*By Taran*

This is a topic of much debate on any SPHERE scripting forum, because no
one can seem to agree on an appropriate method to implement a customized
skill gain script. What IS agreed upon, however, is that the default
skill gain system that is hardcoded into SPHERE is not customizable
enough to meet the standards of today's shards. Stat gain is equally
terrible.

The obvious way to implement a skill gain script is to use the
[@SkillStart](@SkillStart "wikilink") event, which fires any time the
player starts to use any skill. The skill being used is passed into
@SkillStart as \<ARGN1\>

<spherescript>ON=@SkillStart

`   IF (`<ACTION>` == SKILL_HIDING)`  
`       SYSMESSAGE You are using the hiding skill!`  
`   ENDIF`</spherescript>

To implement customized skill gain, you must set the automatic skill
gain rate for any customized skills to zero. Open up spheretables.scp
and look for the \[SKILL\] sections. Set the three numbers after
ADV_RATE to zero (or 0FFFFFFFF, because it is inconceivable that a
player will use a skill over 4 billion times). One of these will work,
and I'm not really sure which, so try it yourself.

I have devised several methods for skill gain scripting, and I will
discuss each of them here.

## Random Skill Gain

This is the method whereby a player gains skill randomly every time he
uses the skill. I will not offer distinct code examples in most cases,
but rather a bit of pseudocode.

<spherescript>ON=@SkillStart

`   IF (<EVAL RAND(10)> == 1)  // 1 in 10 chance`  
`       gain skill`  
`   ENDIF`</spherescript>

Now, one of the major obvious problems with this script is that the
player will gain skill at the same rate whether he or she has 10 skill
or 99 skill. It's still approximately 1 out of every 10 trials. It is
also conceivable that the player will NEVER gain skill with this method,
because RAND(10) may NEVER return 1. The chances of that are extremely
small, but it still remains possible. However, this IS the simplest
method of skill gain, and the method that many shards have chosen to
implement.

## Modified Random Skill Gain

This method modifies the above section to allow for increasing
difficulty as the player gains skill. In this method, we use their
actual skill value as the argument to RAND, thus returning a number
between 0 and their current skill. We can then check whether that number
is greater or less than a certain value, which will determine whether or
not skill is gained. Here is an example:

<spherescript>ON=@SkillStart

`   IF (RAND(`<SWORDSMANSHIP>`) < 10.0)`  
`       gain skill`  
`   ENDIF`</spherescript>

Of course, you can put any skill where I have `<SWORDSMANSHIP>`. You can
also use the currently-being-used skill, which I will discuss toward the
end of this article. This method is superior to the previous method,
because, as you can see, the skill gain is dependent upon the player's
current skill.

For example, let's assume that the player has 20.0 skill in
Swordsmanship. `RAND(<SWORDSMANSHIP>)` will return a number between 0
and 200. We then check if that number is less than 10.0, which will
occur approximately 50% of the time. Therefore, with 20.0 skill, the
player gains skill 50% of the time he uses that skill.

If the player has 50.0 skill, `RAND(<SWORDSMANSHIP>)` will return 0 to
500, and the player will gain skill approximately 20% of the time.

As you can see, this method is greatly improved over the previous
method. However, there are still better ways to implement skill gain. It
still remains conceivable that the player will never gain skill with
this method. We need a way to assure that a player will always gain
skill.

## Linear Subskill Gain

Yes, I am making up these names as I go. I thought that one sounded
pretty awesome.

This method implements what I will refer to as a subskill. This is a
separate value from the skill, usually stored in the form of a TAG on
the player, which holds a value. Once that value crosses a certain
threshold, the skill is incremented by 0.1 automatically. Every time the
player uses the skill, the value is increased.

<spherescript>ON=@SkillStart

`   TAG0.SUBSKILL += 5`  
`   IF (<TAG0.SUBSKILL> > 100)`  
`       TAG0.SUBSKILL = 0`  
`       Increment skill by 0.1`  
`   ENDIF`</spherescript>

As you can see, this method will assure that the player gains skill
after a certain number of trials. If you want to speed up the skill gain
rate, add more to the subskill each try (in my example, you would change
the 5 to something larger). If you want to slow it down, add less.
Different skills will require different gain rates, so it is imperative
that you experiment with the values for the subskill.

Incidentally, this is very similar to the way that the internal system
calculates skill. Those numbers after ADV_RATE in the file can be
equated to the 100 in my script above. However, the gain method used by
ADV_RATE is what is called "variable linear", because as the player
gains skill, it becomes significantly more difficult to gain skill. With
the above example, the skill gain rate is fixed.

## Variable Subskill Gain

I am not going to bother with this one. If you want to use this method,
just use the default skill gain system.

## Exponential Subskill Gain

This is the best method I have discovered yet, although there may still
be others which are an improvement over this. Rather than comparing the
subskill to a particular number (100 for example) we compare it to the
player's current skill.

<spherescript>ON=@SkillStart

`   TAG0.SUBSKILL += 5`  
`   IF (<TAG0.SUBSKILL> > `<SKILL>`)`  
`       TAG0.SUBSKILL = 0`  
`       Increment skill by 0.1`  
`   ENDIF`</spherescript>

Of course, you would be replacing TAG.SUBSKILL with a more descriptive
name, and SKILL with the skill in question. Either way, you get a nice
rate of skill gain that increases as the skill increases. If you would
like to express it mathematically, you would write:

`ds/dt = ks`  

Of course, for those of you who understand calculus, it becomes obvious
that the solution to this equation is

`s = e kt`  

A nice exponential skillgain curve. To speed up skillgain, increase the
value added to the subskill, and do the opposite to slow it down.

## Skill Numbers as Variables

The final item to be discussed in this article is the use of a skill
number as a variable. SPHERE already has this ability included in the
system. More specifically, For example, ALCHEMY will be 01, because it
is defined in spheretables as skill \#1. Now, in the game, type this:

<spherescript>.01 100.0</spherescript>

Surprise! Your alchemy went up to 100.0! This proves that we can use
ACTION numbers as variables. Now, how is this useful to us? Here is a
script WITHOUT skill numbers as variables:

<spherescript>ON=@SkillStart

`   IF (`<ARGN1>` == Skill_Swordsmanship)`  
`       SWORDSMANSHIP += 0.1`  
`   ELIF (`<ARGN1>` == Skill_hiding)`  
`       HIDING += 0.1`  
`   ELIF (`<ARGN1>` == Skill_taming)`  
`       TAMING += 0.1`  
`   ELIF (`<ARGN1>` == Skill_Macefighting)`  
`       MACEFIGHTING += 0.1`  
`   ELIF (`<ARGN1>` == Skill_MAGICRESISTANCE)`  
`       MAGICRESISTANCE += 0.1`  
`   ELIF (`<ARGN1>` == Skill_begging)`  
`       BEGGING += 0.1`  
`   ...`  
`   ...`  
`   ...`</spherescript>  
`  `

Ugly eh? Not only that, but the system has to parse and process that
script every time you one of your players uses a skill. That could be
rather slow don't you think? Well, no, it wouldn't be unless your
processor was significantly slow, but enough scripts like that would
begin to lag the server. Now, try this script on for size:

<spherescript>ON=@SkillStart

`   TRY `<ARGN1>` = <EVAL <`<ARGN1>`> + 0.1>`</spherescript>  
`   `

That's it. :)

Two lines. It looks a lot better than the script above it, right? But
how does it work? Well, SPHERE parses this line like this, before trying
to run it:

1.  TRY \<ARGN1\> = \<EVAL \<\<ARGN1\>\> + 0.1\>
2.  TRY 01 = \<EVAL \<01\> + 0.1\>
3.  TRY 01 = \<EVAL 451 + 1\>
4.  TRY 01 = 452
5.  Execute "01 = 452"

In-game, type .01 452 and see what happens. Your alchemy goes to 45.2.
Now, do it again with a different skill number. Try 01D, I think that's
taming. So you see, this script will increment the skill for ALL skill
numbers, in two lines of code.

[Category: Articles](Category:_Articles "wikilink")
