## Description

This property is used to manage a container for transferring items when a multi (house) is being moved or removed.

## Ficha

|              |               |
|--------------|---------------|
| **Property** | **MovingCrate** |
| **Type**     | Multi (House) |
| **Access**   | Read/Write    |
| **Sphere X** | Yes           |

## Syntax

`[multi].MovingCrate = <container_uid>`
`<[multi].MovingCrate>`

## Notes
- When setting to a container's UID, if there was any other existing `MovingCrate`, its contents will be transferred to the new crate.
- When the multi is being deleted, all linked items will be transferred to the current `MovingCrate` and the crate to the owner's bank (if any).
- A `TAG.MULTI_UID` with the multi's UID will be set on the crate.
- When accessing the `MovingCrate` via script, a new one will be created if the existing one does not exist.
- `MovingCrates` created by the server will have `t_moving_crate` TYPEDEF event applied.
- Setting `MovingCrate` to `0` will empty the house value for list-based values (Coowners, Friends, Bans, Vendors, Accesses).
- The `@Destroy` trigger is no longer strictly needed for deleting items from the house list; pointers are now added back on `CItem` and `CItemStone` to handle this.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)