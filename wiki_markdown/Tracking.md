## Description

The `TRACKING` skill allows characters to track other characters. It can now utilize values stored in its `EFFECT` property to determine the tracking maximum distance.

## Notes
- The Tracking skill can now correctly track `brain_berserk` NPCs.
- If the `EFFECT` property is defined in the skill definition:
    -   `EFFECT=20`: Maximum tracking distance is 20 tiles.
    -   `EFFECT=10,100`: Maximum tracking distance will vary from 10 to 100 tiles, scaled by the player's skill score.
- If `EFFECT` is not defined, the default formula is `MaximumDistance = Tracking / 10 + 10`. (e.g., 90.0 skill -> 100 tiles).
- When using the `Tracking` skill, the maximum distance is stored in `ACTARG2`. This value can be changed in the `@PreStart`, `@Start`, and `@Stroke` triggers.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Skills](./CategorySkills.md)