## Description

The `PILOT` function for ships has been modified. You can now set a UID to pilot the ship. Self-double-clicking the ship will remove the pilot memory (after triggering `@UnMount`). Setting the same UID twice as the pilot will detach the pilot from the ship.

## Ficha

|              |             |
|--------------|-------------|
| **Function** | **PILOT**   |
| **Type**     | Ship        |
| **Access**   | Write-Only  |
| **Sphere X** | Yes         |

## Syntax

`[ship].PILOT <char_uid>`

## Parameters

-   `<char_uid>`: The UID of the character to set as the pilot.

## Notes
- Example `spk_ship_cmds` modification:
```
ON=Pilot
PILOT <SRC.UID>
```

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)