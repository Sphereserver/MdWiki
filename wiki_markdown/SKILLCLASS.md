\_\_FORCETOC\_\_ A skill class restricts the maximum skill and stat
values that a character can have. Skill classes also act an EVENTS
block, and can contain character triggers that will fire for all
characters with the skill class.

## Properties

The following properties are available when defining a skill class:

  --------------------------------- ---------------- -------------------------------------------------------------------------------------------------------------------
  **Name**                          **Read/Write**   **Description**
  [DEX](./DEX.md)             RW               Gets or sets the maximum dexterity value allowed for characters with the class.
  [INT](./INT.md)             RW               Gets or sets the maximum intelligence value allowed for characters with the class.
  [NAME](./NAME.md)           RW               Gets or sets the name of the class.
  *skill_key*                       RW               Gets or sets the maximum amount of *skill_key* is allowed for characters with the class.
  [SKILLSUM](./SKILLSUM.md)   RW               Gets or sets the maximum skill total allowed for characters with the class.
  [STATSUM](./STATSUM.md)     RW               Gets or sets the maximum stat total allowed for characters with the class. (dexterity, intelligence and strength)
  [STR](./STR.md)             RW               Gets or sets the maximum strength value allowed for characters with the class.
  --------------------------------- ---------------- -------------------------------------------------------------------------------------------------------------------

## Examples

`<spherescript>`{=html} // // \'Undeclared\' skill class from the
default script pack. (default for all new characters) // \[SKILLCLASS
0\] DEFNAME=Class_undeclared NAME=undeclared STATSUM=300 // maximum
total of 300 in str+dex+int SKILLSUM=10000.0 // maximum total of 10000%
in all skills STR=100 INT=100 DEX=100 Alchemy=100.0 Anatomy=100.0
AnimalLore=100.0 ItemId=100.0 ArmsLore=100.0 Parrying=100.0
Begging=100.0 Blacksmithing=100.0 Bowcraft=100.0 Peacemaking=100.0
Camping=100.0 Carpentry=100.0 Cartography=100.0 Cooking=100.0
DetectingHidden=100.0 Enticement=100.0 EvaluatingIntel=100.0
Healing=100.0 Fishing=100.0 Forensics=100.0 Herding=100.0 Hiding=100.0
Provocation=100.0 Inscription=100.0 LockPicking=100.0 Magery=100.0
MagicResistance=100.0 Tactics=100.0 Snooping=100.0 Musicianship=100.0
Poisoning=100.0 Archery=100.0 SpiritSpeak=100.0 Stealing=100.0
Tailoring=100.0 Taming=100.0 TasteId=100.0 Tinkering=100.0
Tracking=100.0 Veterinary=100.0 Swordsmanship=100.0 Macefighting=100.0
Fencing=100.0 Wrestling=100.0 Lumberjacking=100.0 Mining=100.0
Meditation=100.0 Stealth=100.0 RemoveTrap=100.0 Necromancy=100.0
Focus=100.0 Chivalry=100.0 Bushido=100.0 Ninjitsu=100.0
Spellweaving=100.0 `</spherescript>`{=html}

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Definitions](./_Definitions.md)
