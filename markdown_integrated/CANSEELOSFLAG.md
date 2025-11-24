## Description

This property allows modifying how Line of Sight (LOS) is checked when using the `I.CANSEELOSFLAG` function.

## Ficha

|              |                 |
|--------------|-----------------|
| **Property** | **CANSEELOSFLAG** |
| **Type**     | Item            |
| **Access**   | Read            |
| **Sphere X** | Yes             |

## Syntax

`<I.CANSEELOSFLAG(flags)>`

## Parameters

- `flags`: A numeric value representing the LOS flags to apply. (Specific flag values are usually defined in `sphere_defs.scp` or similar configuration files).

## Example

`IF (<I.CANSEELOSFLAG(0)> == 1) SAY "I can see it ignoring blockers!"`

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Properties](./CategoryProperties.md)