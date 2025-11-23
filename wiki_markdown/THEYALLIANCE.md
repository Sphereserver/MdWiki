## Description

This function sets or checks another specified guild's alliance status with the current guild. It works similarly to `THEYWAR` but for alliances.

## Ficha

|              |                  |
|--------------|------------------|
| **Function** | **THEYALLIANCE** |
| **Type**     | Guild            |
| **Access**   | Read/Write       |
| **Sphere X** | Yes              |

## Syntax

- Read: `<GUILD.THEYALLIANCE(guild_uid)>`
- Write: `GUILD.THEYALLIANCE(guild_uid) = <value>` (value can be 0 or 1)

## Parameters

- `guild_uid`: The UID of the guild whose alliance status to set/check.

## Return Values

- Returns 1 if allied, 0 otherwise (when read).

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)