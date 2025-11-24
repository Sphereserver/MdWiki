## Description

This function is used to transfer an item directly by its Unique ID (UID) from one character to another.

## Ficha

|              |               |
|--------------|---------------|
| **Function** | **SERV.TRANSFER.UID** |
| **Type**     | Server        |
| **Access**   | Write         |
| **Sphere X** | Yes           |

## Syntax

`SERV.TRANSFER.UID target_char_uid, item_uid`

## Parameters

- `target_char_uid`: The UID of the character to whom the item will be transferred.
- `item_uid`: The UID of the item to be transferred.

## Example

`SERV.TRANSFER.UID <SRC.UID>, <ITEM.UID>` - Transfers the targeted item to the SRC character.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)