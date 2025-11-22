## Description

This trigger fires when a player attempts to invoke a virtue by using a
macro.

Fires on:

-   [Players](Characters#Players "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ------------------------- ------------------------------------------------------------------
  **Name**                  **Description**
  [ARGO](ARGO "wikilink")   The [player](Characters#Players "wikilink") invoking the virtue.
  [I](I "wikilink")         The [player](Characters#Players "wikilink") invoking the virtue.
  [SRC](SRC "wikilink")     The [player](Characters#Players "wikilink") invoking the virtue.
  ------------------------- ------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

+--------------+------------+---------------------------------------------+
| **Argument** | **In/Out** | **Description**                             |
+--------------+------------+---------------------------------------------+
| ARGN1        | I          | The virtue being invoked. Known values are: |
|              |            |                                             |
|              |            |   ----------- -----------------             |
|              |            |   **Value**   **Description**               |
|              |            |   1           Honor                         |
|              |            |   2           Sacrifice                     |
|              |            |   3           Valor                         |
|              |            |   ----------- -----------------             |
+--------------+------------+---------------------------------------------+

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

*No return values are handled for this trigger.*

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink") [Category:
Characters](Category:_Characters "wikilink") [Category:
Players](Category:_Players "wikilink")
