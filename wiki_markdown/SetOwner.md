## Description

This property sets the owner of a house.

## Ficha

|              |               |
|--------------|---------------|
| **Property** | **SetOwner**  |
| **Type**     | House (Multi) |
| **Access**   | Write-Only    |
| **Sphere X** | Yes           |

## Syntax

`[house].SetOwner <uid>`

## Parameters

-   `<uid>`: The UID of the character to set as the new owner.

## Notes
- Setting a new owner will remove the house from the previous owner (if any) and delete their keys for this house.
- It automatically forces `AddHouse <multi_uid>` on the new owner.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)