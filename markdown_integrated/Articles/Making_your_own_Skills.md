## Scripted Skills

First of all, we need to cancel all the default behavoiur. How to do
this? Simple, "SKF_SCRIPTED" (Add this flag to the Skill). This flag
cancels all of the hardcoded behaviour of Sphere and leaves the work up
to us on our triggers. You only need that and this explanation of how
skills are played:

<spherescript> \[SKILL 55\] DEFNAME=SKILL_APPRAISE</spherescript>
<font color="darkgreen">**`FLAGS=SKF_SCRIPTED`**  
</font> <spherescript>KEY=ItemID TITLE=Merchant PROMPT_MSG=What do you
wish to appraise and identify? DELAY=1.0 ADV_RATE=2.5,50.0,200.0
STAT_STR=0 STAT_INT=85 STAT_DEX=0 BONUS_STR=0 BONUS_DEX=0 BONUS_INT=100
BONUS_STATS=25</spherescript> <spherescript color="darkgreen">
ON=@Select // Fires when a player selects the skill in the menu. //
RETURN 1 - Prevent using the skill // RETURN 0/2 - Allow skill to be
used

ON=@Start // Fires when the skill begins. // RETURN 1 = Prevent using
the skill // RETURN 0/2 = Allow skill to be used // ACTION = -1 = Fail
(@Fail). // ACTDIFF = Skill required to succeed (0-100). Set to a
negative value to fail the skill.

ON=@Success // Fires when the skill successfully finishes // RETURN 1 =
Abort the skill // RETURN 0/2 = Proceed with allowing player to gain
skill

ON=@Fail // Fires when a character fails the skill // RETURN 1 = Prevent
skill gain // RETURN 0/2 = Allow skill gain

ON=@Abort // Fires when a character aborts the skill (going into war
mode, for example)

ON=@Gain // Fires when a character has a chance of gaining skill //
ARGN2 = The chance to gain skill (0-1000, writable) // ARGN3 = The
maximum skill level the character can gain to (writable) // RETURN 1 =
Block skill gain // RETURN 0/2 = Allow skill gain calculation to
continue

ON=@UseQuick // Fires when the skill is used with the USEQUICK function
// ARGN2 = Skill difficulty (0-100, writable) // ARGN3 = Whether or not
attempt is successful (writable) // RETURN 1 = Fail the skill attempt
without skill gain // RETURN 0 = Succeed the skill attempt without skill
gain // RETURN 2 = Proceed with skill gain (use ARGN3 to set fail or
success)</spherescript>

## Fighting Skills

Now, we're going to create a Fighting Skill. This one is easier since
the work to make the success, speed, etc are all hardcoded. So, the
trick here is "SKF_FIGHT", add that flag to your skill and you got it!
Now, the only tweak needed is to the weapon, so if my skill is called
AxeFighting, my weapon should look like this:

<spherescript>\[ITEMDEF 0df0\] DEFNAME=i_staff_black
TYPE=T_WEAPON_MACE_STAFF FLIP=1 DAM=12,14 SPEED=37</spherescript>
<font color="darkgreen">**`SKILL=AxeFighting`**` //<-- Here you set your Skill Name.`  
</font> <spherescript>REQSTR=35 TWOHANDS=Y WEIGHT=4</spherescript>

## Crafting Skills

In this case, the calculations and formulae are hardcoded. So, in this
chapter we're going to use a new skill flag, it is named: SKF_CRAFT. You
could imagine what to do now you have this flag added. Yes, change the
item SKILLMAKE, so we're going to replace the old skill with the new.
Let's say this skill is named Herbalist, this is how it should look:

<spherescript>\[ITEMDEF 04554\] DEFNAME=i_GOLDEN_PLATEMAIL_ARMS
NAME=Golden Platemail Arms ID=i_platemail_arms ARMOR=30 REQSTR=40
WEIGHT=5 RESOURCES=18 i_ingot_gold</spherescript>
<font color="darkgreen">**`SKILLMAKE=Herbalist 64.5`**  
</font> <spherescript>CATEGORY=Provisions - Armor - Colored
SUBSECTION=Golden DESCRIPTION=Platemail Arms</spherescript>

## Magician Skills

This one use the flag SKF_MAGIC. And the logic here is go to the SPELL
section and change the SKILLREQ. But this is a tutorial and I should add
an example, I named the skill "MagicalMan", the spell should look like
this:

<spherescript>\[Spell 2\] DEFNAME=s_create_food NAME=Create Food
SOUND=snd_SPELL_CREATE_FOOD RUNES=IMY CAST_TIME=1.0
RESOURCES=i_reag_garlic,i_reag_ginseng,i_reag_mandrake_root
RUNE_ITEM=i_rune_CREATE_FOOD SCROLL_ITEM=i_scroll_CREATE_FOOD
FLAGS=SPELLFLAG_TARG_XYZ EFFECT_ID=0 EFFECT=0 DURATION=0.0
MANAUSE=4</spherescript>
<font color="darkgreen">**`SKILLREQ=MagicalMan 10.0`**  
</font> <spherescript>INTERRUPT=100.0,100.0</spherescript>

[Category:Articles](Category:Articles "wikilink")
