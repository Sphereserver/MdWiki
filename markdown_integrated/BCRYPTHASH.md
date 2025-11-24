## Description

This function generates a bcrypt hash of a given string.

## Ficha

|              |                 |
|--------------|-----------------|
| **Function** | **BCRYPTHASH**  |
| **Type**     | String          |
| **Access**   | Read-Only       |
| **Sphere X** | Yes             |

## Syntax

`<BCRYPTHASH prefix_code, cost_factor, string>`

## Parameters

-   `prefix_code`: Numeric code for the bcrypt prefix:
    -   `0`: "$2a$"
    -   `1`: "$2b$"
    -   `2`: "$2y$"
    -   `3`: "$1$"
    -   `4`: "_"
-   `cost_factor`: The algorithmic cost factor (minimum 4, maximum 31). Higher values mean slower hashing.
-   `string`: The string to be hashed.

## Warning
- Higher `cost_factor` values result in significantly slower hashing, which can potentially block Sphere.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)