## Description

This function displays a targeting cursor to SRC. It can now support colored multis for clients compatible with HS 7.0.9.0+.

## Ficha

|              |             |
|--------------|-------------|
| **Function** | **TARGET**  |
| **Type**     | Character   |
| **Access**   | Write-Only  |
| **Sphere X** | Yes         |

## Syntax

`[char].TARGET *FGMW* *function*`
`[char].TARGETM [multiID, color]`
`[char].TARGETFM [function, multiID, color]`

## Parameters

-   `*FGMW*`: Flags for targeting behavior:
    -   `F`: Makes the `function` available.
    -   `M`: Allows placing a `multi` item.
    -   `G`: Forces the target to only be the ground.
    -   `W`: Checks the criminal status of the player before (or after?) the target selection is made.
-   `*function*`: The function to be executed after targeting.
-   `multiID`: The ID of the multi to color.
-   `color`: The color to apply to the multi.

## Notes
- `TARGETM` and `TARGETFM` are compatible with HS clients 7.0.9.0+ only.
- The target will inherit the deed color when triggered from a deed.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)