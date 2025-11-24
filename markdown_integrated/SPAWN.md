# SPAWN

This page describes the mechanics of spawn groups and their associated properties and functions for controlling item and character spawning.

## Types
- `t_spawn_item`: Generates items.
- `t_spawn_char`: Generates characters.

## Properties and Functions

- `SPAWNID`/`MORE`/`MORE1` (R/W): ID of the spawn (item/template for `t_spawn_item` or char/template for `t_spawn_char`).
- `MORE2`/`COUNT` (R): For `t_spawn_char`, returns the total spawned characters.
- `MORE2`/`PILE` (R/W): For `t_spawn_item`, total amount of items that may be generated at once.
- `MOREX`/`TIMELO` (R/W): Minimum spawn time in minutes.
- `MOREY`/`TIMEHI` (R/W): Maximum spawn time in minutes.
- `MOREZ`/`MAXDIST` (R/W): Maximum spawn distance (for distance away from spawn when created, and max distance to wander from spawn for NPCs).
- `MOREP` (R/W): Groups `MOREX`, `MOREY`, `MOREZ` as one property.
- `AT*` (R/W): Accesses the object at the N position and reads/writes/executes the given text (e.g., `at.0.remove`, `<at.0.str>`).
- `AMOUNT` (R/W): Total amount of objects this spawn can have at the same time.
- `ADDOBJ` (W): Adds an object with the given UID to the spawn (must be a valid UID).
- `DELOBJ` (W): Deletes an object with the given UID from the spawn (must be a valid UID).
- `START` (W): Forces the spawn to start spawning.
- `STOP` (W): Stops the spawn and removes everything it created.
- `RESET` (W): Forces a `STOP` and then `START` again.

## Basic Explanation
1.  When double-clicking on a STOPPED spawn (nothing has yet spawned from it), `START` is called.
2.  One object is generated within a distance of `MOREZ`/`MAXDIST`.
    -   For `t_spawn_item`, the amount of items generated each time is a random value between 1 and `PILE`.
    -   For `t_spawn_char`, the maximum distance the NPC can wander away is set equal to `MAXDIST`.
3.  The spawn's timer is set to a value (in minutes) between `MOREX` and `MOREY` (`TIMELO` and `TIMEHI`).
4.  Steps 2 and 3 are repeated while `COUNT < AMOUNT`. When `COUNT` reaches or surpasses `AMOUNT`, only step 3 will be repeated.

[Category: Game Mechanics](CategoryGame_Mechanics.md)