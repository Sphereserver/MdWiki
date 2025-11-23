## Description

This function allows adding or removing waypoints on the client's radar map. This functionality is supported only for enhanced clients.

## Ficha

|              |                 |
|--------------|-----------------|
| **Function** | **MAPWAYPOINT** |
| **Type**     | Character       |
| **Access**   | Write           |
| **Sphere X** | Yes             |

## Syntax

`[character].MAPWAYPOINT ObjectUID, WaypointType`

## Parameters

-   `ObjectUID`: The UID of the object to place a waypoint for.
-   `WaypointType`: A numerical value specifying the type of waypoint:
    -   `0`: Remove waypoint
    -   `1`: Corpse
    -   `2`: Party Member
    -   `4`: Quest Giver
    -   `5`: New Player Quest
    -   `6`: Healer
    -   `11`: Shrine
    -   `12`: Moongate
    -   `14`: Green Dot
    -   `15`: Green Dot (flashing)

## Example

`SRC.MAPWAYPOINT <ARGO.UID>, 1` - Adds a corpse waypoint for the `ARGO` object on `SRC`'s map.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)