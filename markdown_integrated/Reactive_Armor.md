# Reactive Armor

Reactive Armor is a spell that reflects a percentage of incoming physical damage back to the attacker.

- **Damage Reflection Storage**: The percentage of damage reflected by Reactive Armor is now stored in `More1L` of its rune item.
- **Magery Skill Dependence**: The default damage reflection value is linearly assigned based on the caster's Magery skill and the spell's effect value.
- **Modification via `@EffectAdd`**: The damage reflection value can now be modified using the `@EffectAdd` trigger.
[Category: Spells](./CategorySpells.md)