## Description

This trigger fires when a character\'s murder count
([KILLS](KILLS "wikilink") property) is about to increase.

Fires on:

-   [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ----------------------- ------------------------------------------------------------------------
  **Name**                **Description**
  [I](I "wikilink")       The [character](Characters "wikilink") whose murder count is changing.
  [SRC](SRC "wikilink")   The [character](Characters "wikilink") whose murder count is changing.
  ----------------------- ------------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ -----------------------------------------------------------
  **Argument**   **In/Out**   **Description**
  ARGN1          IO           The new murder count that will be set.
  ARGN2          IO           If non-zero, the character will be flagged as a criminal.
  -------------- ------------ -----------------------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

*No return values are handled for this trigger.*

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink") [Category:
Characters](Category:_Characters "wikilink") [Category:
Combat](Category:_Combat "wikilink")
