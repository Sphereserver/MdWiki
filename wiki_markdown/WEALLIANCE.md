## Description

This function sets or checks the current guild's alliance status with another specified guild. It works similarly to `WEWAR` but for alliances.

## Ficha

|              |                 |
|--------------|-----------------|
| **Function** | **WEALLIANCE**  |
| **Type**     | Guild           |
| **Access**   | Read/Write      |
| **Sphere X** | Yes             |

## Syntax

- Read: `<GUILD.WEALLIANCE(guild_uid)>`
- Write: `GUILD.WEALLIANCE(guild_uid) = <value>` (value can be 0 or 1)

## Parameters

- `guild_uid`: The UID of the guild to set/check alliance status with.

## Return Values

- Returns 1 if allied, 0 otherwise (when read).

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)