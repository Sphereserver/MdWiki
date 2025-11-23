## Description

The Detecting Hidden skill can now utilize values stored in its `EFFECT` property to determine the search radius.

## Ficha

|              |                     |
|--------------|---------------------|
| **Skill**    | **Detecting Hidden** |
| **Sphere X** | Yes                 |

## Behavior

-   If the `EFFECT` property is defined in the skill definition:
    -   `EFFECT=20`: Search radius will always be 20 tiles.
    -   `EFFECT=1,20`: Search radius will vary from 1 to 20 tiles, scaled by the player's skill score.
-   If `EFFECT` is not defined, the default formula is `SearchRadius = DetectingHidden / 100`. (e.g., 90.0 skill -> 9 tiles radius).

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Skills](./CategorySkills.md)