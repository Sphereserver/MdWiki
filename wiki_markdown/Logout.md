## Description

This trigger fires when a player logs out.

Fires on:

-   [Players](Characters#Players "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ----------------------- -------------------------------------------------------------
  **Name**                **Description**
  [I](I "wikilink")       The [player](Characters#Players "wikilink") who logged out.
  [SRC](SRC "wikilink")   The [player](Characters#Players "wikilink") who logged out.
  ----------------------- -------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ ----------------------------------------------------------------------------------------
  **Argument**   **In/Out**   **Description**
  ARGN1          IO           The length of time that the character will linger in the world, in tenths of a second.
  ARGN2          IO           If non-zero, the character will instantly log out.
  -------------- ------------ ----------------------------------------------------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

*No return values are handled by this trigger.*

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
