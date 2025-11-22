## Description

This trigger fires when a player logs in to the server.

Fires on:

-   [Players](Characters#Players "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ----------------------- --------------------------------------------------------
  **Name**                **Description**
  [I](I "wikilink")       The [player](Characters "wikilink") who is logging in.
  [SRC](SRC "wikilink")   The [player](Characters "wikilink") who is logging in.
  ----------------------- --------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ ---------------------------------------------------------------------------------------------------------------------------
  **Argument**   **In/Out**   **Description**
  ARGN1          O            If set to 1, welcome messages won\'t be displayed to the player (i.e. server description, client count, last logged date)
  ARGN2          IO           If set to 1, no messages will be displayed to the player (as above, but also includes guards notification)
  -------------- ------------ ---------------------------------------------------------------------------------------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ --------------------------------------
  **Return Value**   **Description**
  1                  Prevents the player from logging in.
  ------------------ --------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
