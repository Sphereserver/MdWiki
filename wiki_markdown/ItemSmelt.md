## Description

This trigger is fired when the character is smelting an item by a forge
or by using the SMELT command.

Fires on:

-   [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ----------------------- -----------------------------------
  **Name**                **Description**
  [I](I "wikilink")       The item being smelt.
  [SRC](SRC "wikilink")   The character smelting the item..
  ----------------------- -----------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  --------------------------- ------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Argument**                **In/Out**   **Description**
  ARGN1                       IO           Mining skill of the character (adjusted value, base skill + stat bonuses).
  ARGN2                       I            The total amount of different resources the item being smelted has.(For example a mace is made of iron ingots and logs, so the number of different resources is 2, for t_ore item the values is always 1.
  local.resource.*n*.ID       IO           The ID of the itemdef that will be created if the smelting check is succesfull, n starts at 0.
  local.resource.*n*.amount   IO           The amount value that will set on that particular resource if the smelting check is succesfull, n starts at 0.
  --------------------------- ------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ -------------------------------------------------------------------
  **Return Value**   **Description**
  1                  Fails the smelting attempt and block default smelting behaviour..
  ------------------ -------------------------------------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
