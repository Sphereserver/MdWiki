## Description

This trigger fires when a player presses a button on a Kingdom Reborn
toolbar.

Fires on:

-   [Players](Characters#Players "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ----------------------- ------------------------------------------------------------------
  **Name**                **Description**
  [I](I "wikilink")       The [player](Characters#Players "wikilink") pressing the button.
  [SRC](SRC "wikilink")   The [player](Characters#Players "wikilink") pressing the button.
  ----------------------- ------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

+--------------+------------+--------------------------------------------+
| **Argument** | **In/Out** | **Description**                            |
+--------------+------------+--------------------------------------------+
| ARGN1        | I          | The button command type. Known values are: |
|              |            |                                            |
|              |            |   ---------- -----------------             |
|              |            |   **Type**   **Description**               |
|              |            |   1          Cast spell                    |
|              |            |   2          Weapon ability                |
|              |            |   3          Use skill                     |
|              |            |   4          Use item                      |
|              |            |   5          Scroll                        |
|              |            |   ---------- -----------------             |
+--------------+------------+--------------------------------------------+
| ARGN2        | I          | The button\'s command parameter.           |
+--------------+------------+--------------------------------------------+

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ----------------------------------------------
  **Return Value**   **Description**
  1                  Prevents Sphere from processing the command.
  ------------------ ----------------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink") [Category:
Characters](Category:_Characters "wikilink") [Category:
Players](Category:_Players "wikilink")
