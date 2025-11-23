```{=mediawiki}
{{Languages|SKILL}}
```
\_\_FORCETOC\_\_ A skill block defines the basic properties and
behaviours of a skill.

## Properties

The following properties are available when defining a skill:

+-------------------------+----------------+-------------------------+
| **Name**                | **Read/Write** | **Description**         |
+-------------------------+----------------+-------------------------+
| [ADV_RAT                | RW             | Gets or sets the        |
| E](ADV_RATE "wikilink") |                | skill\'s advance rate.  |
|                         |                | Accepts multiple values |
|                         |                | to adjust based on      |
|                         |                | skill level.            |
+-------------------------+----------------+-------------------------+
| [BONUS_DEX              | RW             | Gets or sets a          |
| ](BONUS_DEX "wikilink") |                | multiplier for how much |
|                         |                | dexterity affects a     |
|                         |                | character\'s non-real   |
|                         |                | skill amount, and       |
|                         |                | affects stat gain.      |
+-------------------------+----------------+-------------------------+
| [BONUS_INT              | RW             | Gets or sets a          |
| ](BONUS_INT "wikilink") |                | multiplier for how much |
|                         |                | intelligence affects a  |
|                         |                | character\'s non-real   |
|                         |                | skill amount, and       |
|                         |                | affects stat gain.      |
+-------------------------+----------------+-------------------------+
| [BONUS_STATS](          | RW             | Gets or sets a modifier |
| BONUS_STATS "wikilink") |                | for gaining stats when  |
|                         |                | using the skill.        |
+-------------------------+----------------+-------------------------+
| [BONUS_STR              | RW             | Gets or sets a          |
| ](BONUS_STR "wikilink") |                | multiplier for how much |
|                         |                | strength affects a      |
|                         |                | character\'s non-real   |
|                         |                | skill amount, and       |
|                         |                | affects stat gain.      |
+-------------------------+----------------+-------------------------+
| [D                      | RW             | Gets or sets how long   |
| ELAY](DELAY "wikilink") |                | it takes to attempt to  |
|                         |                | complete the skill, in  |
|                         |                | tenths of a second.     |
|                         |                | Accepts multiple values |
|                         |                | to adjust based on      |
|                         |                | skill level.            |
+-------------------------+----------------+-------------------------+
| [EFF                    | RW             | Gets or sets a value    |
| ECT](EFFECT "wikilink") |                | which effects skills in |
|                         |                | different ways.         |
|                         |                | (Crafting = Resource    |
|                         |                | Loss % on Fail, Healing |
|                         |                | = Amount Healed).       |
|                         |                | Accepts multiple values |
|                         |                | to adjust based on      |
|                         |                | skill level.            |
+-------------------------+----------------+-------------------------+
| [F                      | RW             | Gets or sets skill      |
| LAGS](FLAGS "wikilink") |                | attributes. The         |
|                         |                | available flags are     |
|                         |                | defined in the          |
|                         |                | sphere_defs.scp file:   |
|                         |                |                         |
|                         |                |   ---------             |
|                         |                | ------- ------ -------- |
|                         |                | ----------------------- |
|                         |                | ----------------------- |
|                         |                | ----------------------- |
|                         |                | ----------------------- |
|                         |                | ----------------------- |
|                         |                | ----------------------- |
|                         |                | ----------------------- |
|                         |                |   SKF_SCRIPTED          |
|                         |                |  0001   fully scripted, |
|                         |                |  no hardcoded behaviour |
|                         |                |   SKF                   |
|                         |                | _FIGHT        0002   co |
|                         |                | nsidered a fight skill, |
|                         |                |  maintains fight active |
|                         |                |   SK                    |
|                         |                | F_MAGIC        0004   c |
|                         |                | onsidered a magic skill |
|                         |                |   SKF_CRAFT             |
|                         |                | 0008   considered a cra |
|                         |                | fting skill, compatible |
|                         |                |  with MAKEITEM function |
|                         |                |   SKF_IMMOBILE          |
|                         |                |   0010   skilluser can  |
|                         |                | not move while skilluse |
|                         |                |   SKF_SEL               |
|                         |                | ECTABLE   0020   from s |
|                         |                | kill list. ATTENTION: T |
|                         |                | his does *not* place th |
|                         |                | e button next to the sk |
|                         |                | ill in the client\'s sk |
|                         |                | ill list! For this you  |
|                         |                | have to edit skills.mul |
|                         |                |  or script the trigger. |
|                         |                |                         |
|                         |                | SKF_NOMINDIST    0040   |
|                         |                |  you can mine, fish, ch |
|                         |                | op, hack on the same po |
|                         |                | int you are standing on |
|                         |                |   SK                    |
|                         |                | F_NOANIM       0080   d |
|                         |                | on\'t show hard-coded a |
|                         |                | nimation for this skill |
|                         |                |   SKF_NOSFX        0100 |
|                         |                |    don\'t play hard-cod |
|                         |                | ed sound for this skill |
|                         |                |   SKF_R                 |
|                         |                | ANGED       0200   cons |
|                         |                | idered a ranged skill ( |
|                         |                | combine with SKF_FIGHT) |
|                         |                |   ---------             |
|                         |                | ------- ------ -------- |
|                         |                | ----------------------- |
|                         |                | ----------------------- |
|                         |                | ----------------------- |
|                         |                | ----------------------- |
|                         |                | ----------------------- |
|                         |                | ----------------------- |
|                         |                | ----------------------- |
+-------------------------+----------------+-------------------------+
| [GAINRADIUS]            | RW             | Gets or sets a          |
| (GAINRADIUS "wikilink") |                | difficulty \"radius\"   |
|                         |                | that prevents           |
|                         |                | characters from gaining |
|                         |                | skill when performing   |
|                         |                | \"easy\" actions.       |
|                         |                | Skillgain will only be  |
|                         |                | calculated if the       |
|                         |                | current skill is less   |
|                         |                | than the actual         |
|                         |                | difficulty +            |
|                         |                | GAINRADIUS. If          |
|                         |                | skillgain is aborted    |
|                         |                | due to GAINRADIUS not   |
|                         |                | met, a message will     |
|                         |                | only be displayed if    |
|                         |                | TAG.NOSKILLMSG=1 on     |
|                         |                | character.              |
+-------------------------+----------------+-------------------------+
| [G                      | RW             | Get or sets the         |
| ROUP](GROUP "wikilink") |                | skill\'s group flags.   |
+-------------------------+----------------+-------------------------+
| [KEY](KEY "wikilink")   | RW             | Gets or sets the        |
|                         |                | skill\'s defname.       |
+-------------------------+----------------+-------------------------+
| [NAME](NAME "wikilink") | RW             | Gets or sets the name   |
|                         |                | of the skill.           |
+-------------------------+----------------+-------------------------+
| [STAT_DE                | RW             | Gets or sets the        |
| X](STAT_DEX "wikilink") |                | maximum dexterity a     |
|                         |                | character can gain up   |
|                         |                | to when using this      |
|                         |                | skill.                  |
+-------------------------+----------------+-------------------------+
| [STAT_IN                | RW             | Gets or sets the        |
| T](STAT_INT "wikilink") |                | maximum intelligence a  |
|                         |                | character can gain up   |
|                         |                | to when using this      |
|                         |                | skill.                  |
+-------------------------+----------------+-------------------------+
| [STAT_ST                | RW             | Gets or sets the        |
| R](STAT_STR "wikilink") |                | maximum strength a      |
|                         |                | character can gain up   |
|                         |                | to when using this      |
|                         |                | skill.                  |
+-------------------------+----------------+-------------------------+
| [PROMPT_MSG]            | RW             | Gets or sets the        |
| (PROMPT_MSG "wikilink") |                | message shown when the  |
|                         |                | character selects the   |
|                         |                | skill, and also forces  |
|                         |                | characters to select a  |
|                         |                | target when non-empty.  |
+-------------------------+----------------+-------------------------+
| [T                      | RW             | Gets or sets the        |
| ITLE](TITLE "wikilink") |                | professional title for  |
|                         |                | the skill.              |
+-------------------------+----------------+-------------------------+
| [VAL                    | RW             | Gets or sets a modifier |
| UES](VALUES "wikilink") |                | for the value of items  |
|                         |                | that are created using  |
|                         |                | the skill. Accepts      |
|                         |                | multiple values to      |
|                         |                | adjust based on skill   |
|                         |                | level.                  |
+-------------------------+----------------+-------------------------+

## Triggers

The following table lists all of the triggers that can be placed under a
skill definition. All of the triggers here have an equivalent \@Skill
trigger on the [character](Characters "wikilink") object.

  ------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                             **Description**
  [\@Abort](@Abort "wikilink")         Fires when a character aborts an attempt at using the skill.
  [\@Fail](@Fail "wikilink")           Fires when a character fails an attempt at using the skill.
  [\@Gain](@Gain "wikilink")           Fires when a character is given the chance to gain in the skill.
  [\@PreStart](@PreStart "wikilink")   Fires when a character starts to use the skill, before any hardcoded behaviour takes place.
  [\@Select](@Select "wikilink")       Fires when a character selects the skill from their skill menu.
  [\@Start](@Start "wikilink")         Fires when a character starts to use the skill.
  [\@Success](@Success "wikilink")     Fires when a character succeeds an attempt at using the skill.
  [\@UseQuick](@UseQuick "wikilink")   Fires when a character quickly uses the skill, without changing their [ACTION](ACTION "wikilink").
  [\@Wait](@Wait "wikilink")           This is called whenever Sphere wants to check if a character must wait before starting a skill. Normally this will be when a skill is selected from the skill menu (before [\@Select](@Select "wikilink")), but also when snooping a container or using a musical instrument.
  ------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Examples

`<spherescript>`{=html} // // Alchemy skill from the default script
pack. // \[SKILL 0\] DEFNAME=SKILL_ALCHEMY KEY=Alchemy TITLE=Alchemist
DELAY=3.0,1.0 ADV_RATE=10.0,200.0,800.0 VALUES=1,20,100

BONUS_STATS=10 BONUS_STR=0 BONUS_DEX=20 BONUS_INT=80

STAT_STR=5 STAT_INT=75 STAT_DEX=40

ON=@Fail

`   SRC.SYSMESSAGE You toss the failed mixture from the mortar, unable to create a potion from it.`

ON=@Abort

`   SRC.SYSMESSAGE You fail to complete the potion.`

`</spherescript>`{=html}

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Definitions](Category:_Definitions "wikilink")
