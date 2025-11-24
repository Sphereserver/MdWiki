# Description

`CAN` is a property that defines various behaviors and attributes for items and characters through a system of flags. These flags are typically combined using special characters rather than simple arithmetic sums.

## Ficha

|              |             |
|--------------|-------------|
| **Property** | **CAN**     |
| **Type**     | Item, Character |
| **Access**   | Read Only   |
| **Sphere X** | Yes         |

## Notes

- In Sphere X, the `CAN` property is **Read-Only** and can only be set in the `ITEMDEF` or `CHARDEF` sections. This ensures that the base `CAN` property of an object is always synchronized with its definition.
- To dynamically modify `CAN` flags, use the `CANMASK` property. The retrieved `CAN` value (`<CAN>`) is the result of an XOR operation with `CANMASK`.
- To retrieve the base `CAN` value directly from a definition, use `<SERV.ITEMDEF(defname).CAN>` for items or `<SERV.CHARDEF(defname).CAN>` for characters.

## Individual CAN Flags
- `CAN_I_DAMAGEABLE`: Enables health bars on items (for HS clients >= 7.0.30.0). Requires `MORE1L` for current hitpoints and `MORE1H` for maximum hitpoints.
