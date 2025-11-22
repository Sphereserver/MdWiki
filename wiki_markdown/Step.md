## Description

This trigger fires when an item or region is stepped on by a character.
When an item is stepped, this trigger will periodically fire until the
character steps off the item. For regions, the trigger only fires when
the character takes a step.

Fires on:

-   [Items](Items "wikilink")
-   [Regions](Regions "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ----------------------- --------------------------------------------------------------------------------
  **Name**                **Description**
  [I](I "wikilink")       The [item](Items "wikilink") or [region](Regions "wikilink") being stepped on.
  [SRC](SRC "wikilink")   The [character](Characters "wikilink") stepping on the item or region.
  ----------------------- --------------------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ ----------------------------------------------------
  **Argument**   **In/Out**   **Description**
  ARGN1          I            If 1, the character is standing still on the item.
  -------------- ------------ ----------------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ----------------------------------------------------
  **Return Value**   **Description**
  1                  Prevents the item or region from being stepped on.
  ------------------ ----------------------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
