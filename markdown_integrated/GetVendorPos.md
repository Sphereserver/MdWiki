## Description

This function returns the position of a given vendor UID in the vendor list of a multi (house).

## Ficha

|              |                 |
|--------------|-----------------|
| **Function** | **GetVendorPos** |
| **Type**     | Multi (House)   |
| **Access**   | Read-Only       |
| **Sphere X** | Yes             |

## Syntax

`<[multi].GetVendorPos <vendor_uid>>`

## Parameters

-   `<vendor_uid>`: The UID of the vendor to find in the vendor list.

## Return Values

-   Returns the 0-based position of the vendor in the list.
-   Returns -1 if the vendor is not found.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)