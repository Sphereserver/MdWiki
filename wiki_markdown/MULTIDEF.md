## Description

`MULTIDEF` is used to define multi-part objects like houses. New keys have been added to control storage limits and lockdown percentages.

## Properties

| Name              | Read/Write | Description                                    | Sphere X Only? |
|-------------------|------------|------------------------------------------------|----------------|
| `BaseStorage`     | RW         | Base limit of item storage for this multi.     | X              |
| `BaseVendors`     | RW         | Base limit of vendor capacity for this multi.  | X              |
| `LockdownsPercent`| RW         | Base LockdownsPercent value for this multi.    | X              |
| `GenerateBaseComps`| W         | Regenerates the components the house has.      | X              |

## Notes
- Removing multis now removes all of its components by default (doors, signs, tiller, etc), but not lockdowns or other personal items.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Definitions](./CategoryDefinitions.md)