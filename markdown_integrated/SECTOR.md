## Description

This document describes the properties and functions related to sector management, including sleep/awake states.

## Properties and Functions

| Name       | Read/Write | Description                                                               | Sphere X only? |
|------------|------------|---------------------------------------------------------------------------|----------------|
| `IsSleeping` | R          | Returns 1 if the sector is sleeping, 0 otherwise.                         | X              |
| `Sleep`    | W          | Puts the sector to sleep. `Sleep 1` skips normal checks.                   | X              |
| `Awake`    | W          | Wakes the sector up.                                                      | X              |
| `CanSleep` | R          | Returns 1 if the sector can sleep. `CanSleep 1` checks adjacent sectors. | X              |

## Notes
- `Sleep` will not work if the sector is already sleeping and `Awake` will not work if the sector is not sleeping.
- `Awake` will awake the sector, though it will instantly sleep again if conditions for sleeping are met (e.g., no clients, time since last client departed exceeds `SectorSleep` ini value). This can be used to force all items inside to tick.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Objects](./CategoryObjects.md)