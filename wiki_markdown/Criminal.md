## Description

This trigger fires when a character is going to become criminal.

Fires on:

-   [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

  ----------------------- ----------------------------------------------------------
  **Name**                **Description**
  [I](./I.md)       The [criminal](./Characters.md).
  [SRC](./SRC.md)   The [character](./Characters.md) seeing the crime.
  ----------------------- ----------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ -------------------------------------------------------------------------------------
  **Argument**   **In/Out**   **Description**
  ARGN1          IO           How much time will be criminal for this action ( Reading ini\'s setting, writable).
  -------------- ------------ -------------------------------------------------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ -----------------------------------------
  **Return Value**   **Description**
  1                  Prevents the char of becoming criminal.
  ------------------ -----------------------------------------

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
