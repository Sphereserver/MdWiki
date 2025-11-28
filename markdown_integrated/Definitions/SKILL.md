\_\_FORCETOC\_\_ A skill block defines the basic properties and
behaviours of a skill.

## Properties

The following properties are available when defining a skill:

<table>
<tbody>
<tr>
<td><p><strong>Name</strong></p></td>
<td><p><strong>Read/Write</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p><a href="ADV_RATE" title="wikilink">ADV_RATE</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the skill's advance rate. Accepts multiple values to
adjust based on skill level.</p></td>
</tr>
<tr>
<td><p><a href="BONUS_DEX" title="wikilink">BONUS_DEX</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets a multiplier for how much dexterity affects a
character's non-real skill amount, and affects stat gain.</p></td>
</tr>
<tr>
<td><p><a href="BONUS_INT" title="wikilink">BONUS_INT</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets a multiplier for how much intelligence affects a
character's non-real skill amount, and affects stat gain.</p></td>
</tr>
<tr>
<td><p><a href="BONUS_STATS" title="wikilink">BONUS_STATS</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets a modifier for gaining stats when using the
skill.</p></td>
</tr>
<tr>
<td><p><a href="BONUS_STR" title="wikilink">BONUS_STR</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets a multiplier for how much strength affects a
character's non-real skill amount, and affects stat gain.</p></td>
</tr>
<tr>
<td><p><a href="DELAY" title="wikilink">DELAY</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets how long it takes to attempt to complete the skill,
in tenths of a second. Accepts multiple values to adjust based on skill
level.</p></td>
</tr>
<tr>
<td><p><a href="EFFECT" title="wikilink">EFFECT</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets a value which effects skills in different ways.
(Crafting = Resource Loss % on Fail, Healing = Amount Healed). Accepts
multiple values to adjust based on skill level.</p></td>
</tr>
<tr>
<td><p><a href="FLAGS" title="wikilink">FLAGS</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets skill attributes. The available flags are defined in
the sphere_defs.scp file:</p>
<table>
<tbody>
<tr>
<td><p>SKF_SCRIPTED</p></td>
<td><p>0001</p></td>
<td><p>fully scripted, no hardcoded behaviour</p></td>
</tr>
<tr>
<td><p>SKF_FIGHT</p></td>
<td><p>0002</p></td>
<td><p>considered a fight skill, maintains fight active</p></td>
</tr>
<tr>
<td><p>SKF_MAGIC</p></td>
<td><p>0004</p></td>
<td><p>considered a magic skill</p></td>
</tr>
<tr>
<td><p>SKF_CRAFT</p></td>
<td><p>0008</p></td>
<td><p>considered a crafting skill, compatible with MAKEITEM
function</p></td>
</tr>
<tr>
<td><p>SKF_IMMOBILE</p></td>
<td><p>0010</p></td>
<td><p>skilluser can not move while skilluse</p></td>
</tr>
<tr>
<td><p>SKF_SELECTABLE</p></td>
<td><p>0020</p></td>
<td><p>from skill list. ATTENTION: This does <em>not</em> place the
button next to the skill in the client's skill list! For this you have
to edit skills.mul or script the trigger.</p></td>
</tr>
<tr>
<td><p>SKF_NOMINDIST</p></td>
<td><p>0040</p></td>
<td><p>you can mine, fish, chop, hack on the same point you are standing
on</p></td>
</tr>
<tr>
<td><p>SKF_NOANIM</p></td>
<td><p>0080</p></td>
<td><p>don't show hard-coded animation for this skill</p></td>
</tr>
<tr>
<td><p>SKF_NOSFX</p></td>
<td><p>0100</p></td>
<td><p>don't play hard-coded sound for this skill</p></td>
</tr>
<tr>
<td><p>SKF_RANGED</p></td>
<td><p>0200</p></td>
<td><p>considered a ranged skill (combine with SKF_FIGHT)</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><a href="GAINRADIUS" title="wikilink">GAINRADIUS</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets a difficulty "radius" that prevents characters from
gaining skill when performing "easy" actions. Skillgain will only be
calculated if the current skill is less than the actual difficulty +
GAINRADIUS. If skillgain is aborted due to GAINRADIUS not met, a message
will only be displayed if TAG.NOSKILLMSG=1 on character.</p></td>
</tr>
<tr>
<td><p><a href="GROUP" title="wikilink">GROUP</a></p></td>
<td><p>RW</p></td>
<td><p>Get or sets the skill's group flags.</p></td>
</tr>
<tr>
<td><p><a href="KEY" title="wikilink">KEY</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the skill's defname.</p></td>
</tr>
<tr>
<td><p><a href="NAME" title="wikilink">NAME</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the name of the skill.</p></td>
</tr>
<tr>
<td><p><a href="STAT_DEX" title="wikilink">STAT_DEX</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the maximum dexterity a character can gain up to
when using this skill.</p></td>
</tr>
<tr>
<td><p><a href="STAT_INT" title="wikilink">STAT_INT</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the maximum intelligence a character can gain up to
when using this skill.</p></td>
</tr>
<tr>
<td><p><a href="STAT_STR" title="wikilink">STAT_STR</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the maximum strength a character can gain up to when
using this skill.</p></td>
</tr>
<tr>
<td><p><a href="PROMPT_MSG" title="wikilink">PROMPT_MSG</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the message shown when the character selects the
skill, and also forces characters to select a target when
non-empty.</p></td>
</tr>
<tr>
<td><p><a href="TITLE" title="wikilink">TITLE</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the professional title for the skill.</p></td>
</tr>
<tr>
<td><p><a href="VALUES" title="wikilink">VALUES</a></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets a modifier for the value of items that are created
using the skill. Accepts multiple values to adjust based on skill
level.</p></td>
</tr>
</tbody>
</table>

## Triggers

The following table lists all of the triggers that can be placed under a
skill definition. All of the triggers here have an equivalent @Skill
trigger on the [character](Characters "wikilink") object.

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

<spherescript> // // Alchemy skill from the default script pack. //
\[SKILL 0\] DEFNAME=SKILL_ALCHEMY KEY=Alchemy TITLE=Alchemist
DELAY=3.0,1.0 ADV_RATE=10.0,200.0,800.0 VALUES=1,20,100

BONUS_STATS=10 BONUS_STR=0 BONUS_DEX=20 BONUS_INT=80

STAT_STR=5 STAT_INT=75 STAT_DEX=40

ON=@Fail

`   SRC.SYSMESSAGE You toss the failed mixture from the mortar, unable to create a potion from it.`

ON=@Abort

`   SRC.SYSMESSAGE You fail to complete the potion.`

</spherescript>

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Definitions](Category:_Definitions "wikilink")
