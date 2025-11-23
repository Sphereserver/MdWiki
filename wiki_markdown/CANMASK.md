## Description

`CANMASK` is an item and character property that acts as a bitmask to dynamically switch `CAN` flags on or off from the base `CAN` property.

## Ficha

|              |             |
|--------------|-------------|
| **Property** | **CANMASK** |
| **Type**     | Item/Character |
| **Access**   | Read/Write  |
| **Sphere X** | Yes         |

## How it Works

When the `CAN` property is retrieved (`<CAN>`), it is first XORed with `CANMASK`. This means:
- If a flag set in `CANMASK` is also set in `CAN`, that flag is ignored (effectively turned off).
- If a flag set in `CANMASK` is *not* set in `CAN`, that flag is considered as set (effectively turned on).

## Notes
- This property allows for dynamic modification of an object's `CAN` flags without altering its base `ITEMDEF`/`CHARDEF` `CAN` property.
- The base `CAN` property is now read-only and can only be set in `ITEMDEF`/`CHARDEF` sections.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)