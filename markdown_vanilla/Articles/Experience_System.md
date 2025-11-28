Currently Sphere .56b has a built in experience system, and of course
it's designed in a way so that you can intercept it at any stage to
implement your own code.

About how to activate and configure the experience and level system
you'll find further information [here](Triggers "wikilink") and
[here.](Configuring_Sphere.ini "wikilink")

But at least you should know what amount of experience the system will
give to your characters on what occasions.

Currently you can only get EXP by slaying NPC or PC, or by crafting
valuable items:

### Experience in Combat

- You will get NO experience by killing a summoned creatures.
- You will get NO experience if your pet did the kill.
- You will get NO experience if you kill a guildmate.
- You will get between 1 and 20 percent of your enemy's EXP as
  experience; if you're a newbie fighting a very experienced enemy with
  success, you'll gain much more EXP than he would gain if he slays you.
- If there are more but one persons involved in the fight, everyone gets
  a share.
- Even monsters gain EXP while killing enemies. So finally killing a
  daemon who already killed dozens of players will give you more EXP
  than killing a "newbie daemon".
- If you've activated Sphere's level system the level difference between
  you and your victim will also influence the amount of EXP you'll gain.
- If activated in sphere.ini you may loose 10 percent of your total
  experience if you die.
- If not set explicitely set by script, monsters' EXP are calculated
  from the NPC's STR, INT and DEX, its best fighting skill, the
  remaining fighting skill, peacemaking, provocation, magery, taming,
  its base defense and attack damage values. Just to give a relation: An
  orc will have approx. 650 EXP, a daemon will have approx. 7 times the
  EXP of an orc.

### Experience in Crafting

- You will only get EXP by crafting items that have a value.
- You will gain approximately 1 percent of the value of an item as EXP.

### Levelling

If activated in Sphere.ini (`LevelSystem=1`) all characters will gain
levels related to the amount of EXP they get.

- Set "NExtLevelAt" to the amount of EXP that is needed to raise a
  character from level 0 to level 1.
- If "LevelMode=0", characters will gain a new level each time they
  receive LevelNextAt EXP.
- If "LevelMode=1", characters will need an increasing number of EXP
  points to gain at each level.
- Levelling only means that the LEVEL property rises. It also means that
  the EXP \_given\_ by a slain character will grow with its LEVEL, and
  that the EXP the killer receives will go down with *his* LEVEL.

The following table shows the different in EXP requirements for the two
different levelling modes:

<table>
<tbody>
<tr>
<td><p><strong>LEVEL</strong><br />
<em>(LevelNextAt=1000)</em></p></td>
<td><p><strong>EXP Needed</strong><br />
<em>(LevelMode=0)</em></p></td>
<td><p><strong>EXP Needed</strong><br />
<em>(LevelMode=1)</em></p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>1000</p></td>
<td><p>1000</p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p>2000</p></td>
<td><p>3000</p></td>
</tr>
<tr>
<td><p>3</p></td>
<td><p>3000</p></td>
<td><p>6000</p></td>
</tr>
<tr>
<td><p>4</p></td>
<td><p>4000</p></td>
<td><p>10000</p></td>
</tr>
<tr>
<td><p>5</p></td>
<td><p>5000</p></td>
<td><p>15000</p></td>
</tr>
</tbody>
</table>

[Category: Articles](Category:_Articles "wikilink")
