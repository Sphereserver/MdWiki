## Description

This trigger fires when a character is sent to or released from jail.

Fires on:

-   [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ----------------------- ----------------------------------------------------------------------------------
  **Name**                **Description**
  [I](I "wikilink")       The [character](Characters "wikilink") being sent to or released from jail.
  [SRC](SRC "wikilink")   The [character](Characters "wikilink") responsible for the jailing or releasing.
  ----------------------- ----------------------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ ---------------------------------------------------------------------------------------------
  **Argument**   **In/Out**   **Description**
  ARGN1          I            Indicates if the character is being sent to jail (1 = sent to jail, 0 = released from jail)
  ARGN2          I            The cell number the character is to be sent to.
  -------------- ------------ ---------------------------------------------------------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ----------------------------------------------------
  **Return Value**   **Description**
  1                  Prevents the character from being jailed/released.
  ------------------ ----------------------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
