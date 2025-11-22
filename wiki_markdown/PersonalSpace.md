## Description

This trigger fires when a character is stepped on by another character.

Fires on:

-   [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ----------------------- ------------------------------------------------------------
  **Name**                **Description**
  [I](I "wikilink")       The [character](Characters "wikilink") being stepped on.
  [SRC](SRC "wikilink")   The [character](Characters "wikilink") doing the stepping.
  ----------------------- ------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ ------------------------------------------------------------------------------
  **Argument**   **In/Out**   **Description**
  ARGN1          IO           The amount of stamina needed to step on to the character.
  ARGN2          O            Setting it to 1 allow NPCs to pass over another NPCs, 0 reject the movement.
  ARGN3          IO           Maximum stamina requirement (default 1 = require maximum stamina)(X-Only)
  -------------- ------------ ------------------------------------------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ -----------------------------------------------
  **Return Value**   **Description**
  1                  Prevents the character from being stepped on.
  ------------------ -----------------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
