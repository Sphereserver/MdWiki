## Description

This trigger fires when a [skill menu](SKILLMENU "wikilink") is
displayed to a player. Note that the trigger only fires when Sphere
attempts to display the menu through hardcoded behaviour, using the
[SKILLMENU](SKILLMENU "wikilink") command will not cause this trigger to
fire.

Fires on:

-   [Players](Characters#Players "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ----------------------- -----------------------------------------------------------------------------
  **Name**                **Description**
  [I](I "wikilink")       The [player](Characters#Players "wikilink") who the menu is being shown to.
  [SRC](SRC "wikilink")   The [player](Characters#Players "wikilink") who the menu is being shown to.
  ----------------------- -----------------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

+-----------------+------------+-------------------------------------+
| **Argument**    | **In/Out** | **Description**                     |
+-----------------+------------+-------------------------------------+
| ARGS            | I          | The skillmenu\'s defname. This is   |
|                 |            | expected to be one of the           |
|                 |            | following:                          |
|                 |            |                                     |
|                 |            | -   sm_alchemy                      |
|                 |            | -   sm_blacksmith                   |
|                 |            | -   sm_bolts                        |
|                 |            | -   sm_bowcraft                     |
|                 |            | -   sm_carpentry                    |
|                 |            | -   sm_cartography                  |
|                 |            | -   sm_inscription                  |
|                 |            | -   sm_polymorph                    |
|                 |            | -   sm_summon                       |
|                 |            | -   sm_tailor_cloth                 |
|                 |            | -   sm_tailor_leather               |
|                 |            | -   sm_tinker                       |
+-----------------+------------+-------------------------------------+
| BIG change on X | I          | <ht                                 |
|                 |            | tps://github.com/Sphereserver/Sourc |
|                 |            | e-X/blob/3b2c4d9c6dec393eaea725770b |
|                 |            | b86237e2a85074/Changelog.txt#L3408> |
+-----------------+------------+-------------------------------------+

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ----------------------------------------------
  **Return Value**   **Description**
  1                  Prevents the skillmenu from being displayed.
  ------------------ ----------------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
