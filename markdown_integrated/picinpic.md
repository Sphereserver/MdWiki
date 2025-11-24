# picinpic

Used to add sprites pictures on dialogs.

## Syntax

`picinpic x y gump spritex spritey width height`

## Parameters

| Parameter | Description                                                                   |
| :-------- | :---------------------------------------------------------------------------- |
| `x`       | X-coordinate of the top-left corner of the background area.                   |
| `y`       | Y-coordinate of the top-left corner of the background area.                   |
| `gump`    | Gump ID containing the sprite.                                                |
| `spritex` | X-coordinate of the sprite within the gump.                                   |
| `spritey` | Y-coordinate of the sprite within the gump.                                   |
| `width`   | Width of the background area.                                                 |
| `height`  | Height of the background area.                                                |

## Example

`picinpic 0 0 09d3b 150 150 30 30` (add background area on 0,0 to 30,30 and add sprite 150,150 from gump 09d3b inside it)

[Category: Dialog Elements](./CategoryDialog_Elements.md)
