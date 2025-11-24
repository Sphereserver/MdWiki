## Description

TAGs (Temporary AGs) are custom properties that can be assigned to almost any object in Sphere. They are similar to `VAR` variables, but they are attached directly to an object, allowing for more localized and persistent data storage.

## Syntax

- `TAG.`*tagname*`=value`: Sets the value of *tagname* on the object.
- `TAG.`*tagname*: Reads the value of *tagname*.

## Notes
- `TAG.OVERRIDE.MAXWEIGHT` has been removed. `ModMaxWeight` is used in its place for Banks and Corpses.
- `TAG.BARDING.DIFF` is now used to determine the difficulty of Enticement, Peacemaking, and Provocation skills. If this tag isn't set, the old behavior is used.
- `tag.override.movedelay` (msec) can be used for NPCs to override moverate checks and set the next movement timer (e.g., `tag.override.movedelay=250` for 250ms movement intervals).

## Properties and Functions

| Name | Read/Write | Description | Sphere X only? |
|---|---|---|---|
| [TAG.RESTORE](./TAG.md) *tagname* | R | Retrieves the default value of a TAG. | X |
| [TAG.OVERRIDE](./TAG.md) *tagname* | RW | Adds or changes a temporary tag on a character. | X |

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Objects](./CategoryObjects.md)