## Description

This trigger fires when a character attempts to access the context menu
on an object. The [ADDCONTEXTENTRY](./ADDCONTEXTENTRY.md) function
can be called on SRC to add custom menu entries to the menu.

Fires on:

-   [Characters](./Characters.md)
-   [Items](./Items.md)

## References

The following object references are explicitly available for this
trigger:

  ----------------------- ------------------------------------------------------------------------------------
  **Name**                **Description**
  [I](./I.md)       The [character](./Characters.md) or [item](./Items.md) being accessed.
  [SRC](./SRC.md)   The [client](./CharactersClients.md) requesting the menu.
  ----------------------- ------------------------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Argument**   **In/Out**   **Description**
  ARGN1          IO           1 on the first fire, 2 on the second. Set to a value other than 1 during the first call to have the trigger fire again after hardcoded menu entries have been added.
  -------------- ------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ----------------------------------------------
  **Return Value**   **Description**
  1                  Prevents hardcoded menu entries being added.
  ------------------ ----------------------------------------------

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
