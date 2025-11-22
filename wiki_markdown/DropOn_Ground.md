## Description

This trigger fires when an item is dropped on to the ground.

Fires on:

-   [Items](Items "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ----------------------- -----------------------------------------------------------
  **Name**                **Description**
  [I](I "wikilink")       The [item](Items "wikilink") being dropped.
  [SRC](SRC "wikilink")   The [character](Characters "wikilink") dropping the item.
  ----------------------- -----------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ ----------------------------------------------
  **Argument**   **In/Out**   **Description**
  ARGN1          IO           The decay time that will be set on the item.
  ARGS           I            The location that the item was dropped at.
  -------------- ------------ ----------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ -----------------------------------------------------------
  **Return Value**   **Description**
  1                  Prevents the item from being deleted if dropped on water.
  ------------------ -----------------------------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
