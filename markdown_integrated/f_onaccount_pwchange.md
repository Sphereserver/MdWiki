## Description

This function (or trigger) is called before an account's password change is finalized. It now provides access to the old password.

## Ficha

|              |                          |
|--------------|--------------------------|
| **Function** | **f_onaccount_pwchange** |
| **Type**     | Server-side              |
| **Access**   | (Implied by context)     |
| **Sphere X** | Yes                      |

## Arguments

-   `LOCAL.OLDPASSWORD`: Stores the old password string, accessible before the requested change is applied.

## Notes
- This allows scripts to perform actions based on the old password before it is changed.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)