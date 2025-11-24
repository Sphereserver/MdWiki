## Description

`SERV.TILEDATA` allows direct reading of item and terrain properties from the `tiledata.mul` file. This is useful for retrieving raw client-side data.

## Syntax

- `SERV.TILEDATA.TERRAIN(id).property`: Accesses properties of a landtile by its `id`.
- `SERV.TILEDATA.ITEM(id).property`: Accesses properties of an item by its `id`.

## Properties

### For `SERV.TILEDATA.TERRAIN(id)`:

- `FLAGS`
- `UNK`
- `INDEX`
- `NAME`

### For `SERV.TILEDATA.ITEM(id)`:

- `FLAGS`: Represents various properties of the item. For High Seas tiledata, this is now correctly read as a 64-bit number.
- `UNK5`
- `WEIGHT`
- `LAYER`
- `UNK11`
- `ANIM`: Originally considered a 4-bit field, it's actually a 2-bit number related to animation. Can be used with an offset (e.g., `50000` for male gumps, `60000` for female gumps) to retrieve the paperdoll gump ID.
- `LIGHT`: Represents the light value of the item. Formerly known as `UNK19`.
- `HUE`: Represents the hue value of the item, newly added to reflect the reinterpretation of the ANIM field.
- `HEIGHT`
- `NAME`

## Example

- `SYSMESSAGE <SERV.TILEDATA.ITEM(<DISPIDDEC>).ANIM> + 50000` (to get male paperdoll gump ID)

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)