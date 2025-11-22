## Description

This trigger fires when a client selects a context menu option for an
object.

Fires on:

-   [Characters](./Characters.md)
-   [Items](./Items.md)

## References

The following object references are explicitly available for this
trigger:

  ----------------------- -----------------------------------------------------------------------------------------
  **Name**                **Description**
  [I](./I.md)       The [character](./Characters.md) or [item](./Items.md) displaying the menu.
  [SRC](./SRC.md)   The [character](./Characters.md) who selected the option.
  ----------------------- -----------------------------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ -------------------------------------
  **Argument**   **In/Out**   **Description**
  ARGN1          I            The ID of the menu option selected.
  -------------- ------------ -------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ---------------------------------------------
  **Return Value**   **Description**
  1                  Prevents any hardcoded action taking place.
  ------------------ ---------------------------------------------

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
