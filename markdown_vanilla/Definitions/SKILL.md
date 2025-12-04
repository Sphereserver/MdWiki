 A skill block defines the basic properties and behaviours of a skill.

## Properties

The following properties are available when defining a skill:

| **Name** | **Read/Write** | **Description** |  |  |
| --- | --- | --- | --- | --- |
| [ADV_RATE](ADV_RATE) | RW | Gets or sets the skill's advance rate. Accepts multiple values to adjust based on skill level. |  |  |
| [BONUS_DEX](BONUS_DEX) | RW | Gets or sets a multiplier for how much dexterity affects a character's non-real skill amount, and affects stat gain. |  |  |
| [BONUS_INT](BONUS_INT) | RW | Gets or sets a multiplier for how much intelligence affects a character's non-real skill amount, and affects stat gain. |  |  |
| [BONUS_STATS](BONUS_STATS) | RW | Gets or sets a modifier for gaining stats when using the skill. |  |  |
| [BONUS_STR](BONUS_STR) | RW | Gets or sets a multiplier for how much strength affects a character's non-real skill amount, and affects stat gain. |  |  |
| [DELAY](DELAY) | RW | Gets or sets how long it takes to attempt to complete the skill, in tenths of a second. Accepts multiple values to adjust based on skill level. |  |  |
| [EFFECT](EFFECT) | RW | Gets or sets a value which effects skills in different ways. (Crafting = Resource Loss % on Fail, Healing = Amount Healed). Accepts multiple values to adjust based on skill level. |  |  |
| [FLAGS](FLAGS) | RW | Gets or sets skill attributes. The available flags are defined in the sphere_defs.scp file: <table> SKF_SCRIPTED | 0001 | fully scripted, no hardcoded behaviour |
| SKF_FIGHT | 0002 | considered a fight skill, maintains fight active |  |  |
| SKF_MAGIC | 0004 | considered a magic skill |  |  |
| SKF_CRAFT | 0008 | considered a crafting skill, compatible with MAKEITEM function |  |  |
| SKF_IMMOBILE | 0010 | skilluser can not move while skilluse |  |  |
| SKF_SELECTABLE | 0020 | from skill list. ATTENTION: This does *not* place the button next to the skill in the client's skill list! For this you have to edit skills.mul or script the trigger. |  |  |
| SKF_NOMINDIST | 0040 | you can mine, fish, chop, hack on the same point you are standing on |  |  |
| SKF_NOANIM | 0080 | don't show hard-coded animation for this skill |  |  |
| SKF_NOSFX | 0100 | don't play hard-coded sound for this skill |  |  |
| SKF_RANGED | 0200 | considered a ranged skill (combine with SKF_FIGHT) |  |  |</td>
</tr> <tr> <td><p>[GAINRADIUS](GAINRADIUS)</p></td> <td><p>RW</p></td> <td><p>Gets or sets a difficulty "radius" that prevents characters from gaining skill when performing "easy" actions. Skillgain will only be calculated if the current skill is less than the actual difficulty + GAINRADIUS. If skillgain is aborted due to GAINRADIUS not met, a message will only be displayed if `TAG.NOSKILLMSG`=1 on character.</p></td> </tr> <tr> <td><p>[GROUP](GROUP)</p></td> <td><p>RW</p></td> <td><p>Get or sets the skill's group flags.</p></td> </tr> <tr> <td><p>[KEY](KEY)</p></td> <td><p>RW</p></td> <td><p>Gets or sets the skill's defname.</p></td> </tr> <tr> <td><p>[NAME](NAME)</p></td> <td><p>RW</p></td> <td><p>Gets or sets the name of the skill.</p></td> </tr> <tr> <td><p>[STAT_DEX](STAT_DEX)</p></td> <td><p>RW</p></td> <td><p>Gets or sets the maximum dexterity a character can gain up to when using this skill.</p></td> </tr> <tr> <td><p>[STAT_INT](STAT_INT)</p></td> <td><p>RW</p></td> <td><p>Gets or sets the maximum intelligence a character can gain up to when using this skill.</p></td> </tr> <tr> <td><p>[STAT_STR](STAT_STR)</p></td> <td><p>RW</p></td> <td><p>Gets or sets the maximum strength a character can gain up to when using this skill.</p></td> </tr> <tr> <td><p>[PROMPT_MSG](PROMPT_MSG)</p></td> <td><p>RW</p></td> <td><p>Gets or sets the message shown when the character selects the skill, and also forces characters to select a target when non-empty.</p></td> </tr> <tr> <td><p>[TITLE](TITLE)</p></td> <td><p>RW</p></td> <td><p>Gets or sets the professional title for the skill.</p></td> </tr> <tr> <td><p>[VALUES](VALUES)</p></td> <td><p>RW</p></td> <td><p>Gets or sets a modifier for the value of items that are created using the skill. Accepts multiple values to adjust based on skill level.</p></td> </tr> </tbody> </table>

## Triggers

The following table lists all of the triggers that can be placed under a skill definition. All of the triggers here have an equivalent @Skill trigger on the [character](Characters "wikilink") object.

|  |  |
|----|----|
| **Name** | **Description** |
| [@Abort](@Abort "wikilink") | Fires when a character aborts an attempt at using the skill. |
| [@Fail](@Fail "wikilink") | Fires when a character fails an attempt at using the skill. |
| [@Gain](@Gain "wikilink") | Fires when a character is given the chance to gain in the skill. |
| [@PreStart](@PreStart "wikilink") | Fires when a character starts to use the skill, before any hardcoded behaviour takes place. |
| [@Select](@Select "wikilink") | Fires when a character selects the skill from their skill menu. |
| [@Start](@Start "wikilink") | Fires when a character starts to use the skill. |
| [@Success](@Success "wikilink") | Fires when a character succeeds an attempt at using the skill. |
| [@UseQuick](@UseQuick "wikilink") | Fires when a character quickly uses the skill, without changing their [ACTION](ACTION "wikilink"). |
| [@Wait](@Wait "wikilink") | This is called whenever Sphere wants to check if a character must wait before starting a skill. Normally this will be when a skill is selected from the skill menu (before [@Select](@Select "wikilink")), but also when snooping a container or using a musical instrument. |

## Examples

```
 // // Alchemy skill from the default script pack. //
```
\[SKILL 0\] DEFNAME=SKILL_ALCHEMY KEY=Alchemy TITLE=Alchemist
```
DELAY=3.0,1.0 ADV_RATE=10.0,200.0,800.0 VALUES=1,20,100
```

```
BONUS_STATS=10 BONUS_STR=0 BONUS_DEX=20 BONUS_INT=80
```

```
STAT_STR=5 STAT_INT=75 STAT_DEX=40
```

```
ON=@Fail
```

`   `SRC.SYSMESSAGE` You toss the failed mixture from the mortar, unable to create a potion from it.`

```
ON=@Abort
```

`   `SRC.SYSMESSAGE` You fail to complete the potion.`


[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Definitions](Category:_Definitions "wikilink")
