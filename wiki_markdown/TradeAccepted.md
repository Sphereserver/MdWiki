## Description

This trigger fires when two players have accepted a trade agreement. The
trigger will be fired on both characters.

Fires on:

-   [Players](Characters#Players "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ---------------------------------------------------------- --------------------------------------------------------------------
  **Name**                                                   **Description**
  [ARGO](ARGO "wikilink")                                    The [player](Characters#Players "wikilink") accepting the trade.
  [I](I "wikilink")                                          The [player](Characters#Players "wikilink") accepting the trade.
  [REF](REF "wikilink")1 to [REF](REF "wikilink")\<ARGN1\>   The [items](Items "wikilink") that the player is receiving.
  [SRC](SRC "wikilink")                                      The [player](Characters#Players "wikilink") they are trading with.
  ---------------------------------------------------------- --------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ ---------------------------------------------------------
  **Argument**   **In/Out**   **Description**
  ARGN1          I            The number of items that the player is receiving.
  ARGN2          I            The number of items that the other player is receiving.
  -------------- ------------ ---------------------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ -----------------------------------------
  **Return Value**   **Description**
  1                  Prevents the transaction to take place.
  ------------------ -----------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink") [Category:
Characters](Category:_Characters "wikilink") [Category:
Players](Category:_Players "wikilink")
