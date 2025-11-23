## Description

This property gets or sets the maximum number of houses an account or character can own.

## Ficha

|              |               |
|--------------|---------------|
| **Property** | **MaxHouses** |
| **Type**     | Account/Character |
| **Access**   | Read/Write    |
| **Sphere X** | Yes           |

## Notes
- For accounts, the default value is `Serv.MaxHousesAccount`.
- For characters (players), the default value is `Serv.MaxHousesPlayer`.
- Setting `MaxHouses = 0` for players will make the setting read from their account.
- Setting `MaxHouses = 0` for players and accounts allows building without limit.
- Values set here will not reflect on already created accounts/characters if the `sphere.ini` values change.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)