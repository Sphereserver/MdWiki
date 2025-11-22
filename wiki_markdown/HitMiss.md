## Description

This trigger fires when a character is about to miss a combat swing.

Fires on:

-   [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ------------------------- --------------------------------------------------------------------------------
  **Name**                  **Description**
  [ARGO](ARGO "wikilink")   The [weapon](Items "wikilink") being used (can be nothing, if fists are used).
  [I](I "wikilink")         The [character](Characters "wikilink") doing the hitting.
  [SRC](SRC "wikilink")     The [character](Characters "wikilink") who was missed.
  ------------------------- --------------------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------------- ------------ --------------------------------------------------------------
  **Argument**         **In/Out**   **Description**
  LOCAL.ARROWHANDLED   IO           if set to !=0, you can do whatever you want with local.arrow
  -------------------- ------------ --------------------------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ---------------------------
  **Return Value**   **Description**
  1                  Cancels the attack swing.
  ------------------ ---------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink") [Category:
Characters](Category:_Characters "wikilink") [Category:
Combat](Category:_Combat "wikilink")
