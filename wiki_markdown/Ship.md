## Description

This document describes properties, functions and behaviors related to ship multis.

## Movement (CCMultiMovable Class)

All multi objects can now move like a ship without external scripts by utilizing the `CCMultiMovable` class.

-   **Requirements for Movement**:
    -   Movable multis need `ShipSpeed.period` and `ShipSpeed.tiles` to be higher than 0.
-   **Speech Commands**:
    -   Houses that can move require `spk_ship_cmds` speech on them for player speech support.
-   **Directionality**:
    -   Since multis don't have direction like ships, their direction is inverted:
        -   Forward will move to the south
        -   Left will move to the right
        -   Right will move to the left
        -   Back will move to the north
-   **Timer-based Movement**:
    -   Movement is set via 'timer'. Any house that can move will attempt to move instead of expiring on its `ON=@Timer`. If you want a house that moves and decays, use `timerf` for decay.

## Region Change Support

-   Ships now support region change triggers. `@Enter` and `@Exit` triggers will be fired on the regions they enter and leave.
-   Characters inside the ship will not trigger these events; they will receive region enter/leave events when landing from the ship.

## Triggers

-   `@RegionEnter`: Fired when the ship enters a region.
-   `@RegionLeave`: Fired when the ship leaves a region.
-   `@itemRegionEnter`: Homologue to `@RegionEnter`, but specifically for ships.
-   `@itemRegionLeave`: Homologue to `@RegionLeave`, but specifically for ships.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Objects](./CategoryObjects.md)