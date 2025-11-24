# MaxHouses

This property defines the maximum number of houses a character or account can own.

## Ficha

|              |                 |
|--------------|-----------------|
| **Property** | **MaxHouses**   |
| **Type**     | Character, Account |
| **Access**   | Read/Write      |
| **Sphere X** | Yes             |

## Notes
- When a character or account is created, this setting is read from `sphere.ini` (`Serv.MaxHousesAccount` for accounts, `Serv.MaxHousesPlayer` for players).
- Changes to `sphere.ini` values will not reflect on already created accounts/characters.
- Setting `MaxHouses = 0` for players will make it read the value from their account.
- Setting `MaxHouses = 0` for both players and accounts will allow building without limit.

[Category: Properties](CategoryProperties.md)
