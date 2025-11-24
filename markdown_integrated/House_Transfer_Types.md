## Description

This `DEFNAME` block defines the types of transfers possible when dealing with moving crates for houses.

## Definitions

- `transfer_nothing`: 0 (Do not transfer any item to the Moving Crate, the crate will still be moved if uid is given.)
- `transfer_all`: 01 (Transfer LockDowns, Addons and every other item found inside a house that is not a component of it.)
- `transfer_lockdowns`: 02 (Transfer LockDowns)
- `transfer_addon`: 04 (Transfer Addons)
- `transfer_secured`: 08 (Transfer Secured Containers)

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Definitions](./CategoryDefinitions.md)