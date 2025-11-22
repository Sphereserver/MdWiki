## Description

This trigger fires when a character fails to cast a spell.

Fires on:

-   [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ------------------------- ------------------------------------------------------------------------------
  **Name**                  **Description**
  [ARGO](ARGO "wikilink")   The [item](Items "wikilink") used to cast the spell (e.g. a wand or scroll).
  [I](I "wikilink")         The [character](Characters "wikilink") failing to cast the spell.
  [SRC](SRC "wikilink")     The [character](Characters "wikilink") failing to cast the spell.
  ------------------------- ------------------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ --------------------------------
  **Argument**   **In/Out**   **Description**
  ARGN1          I            The spell that was being cast.
  -------------- ------------ --------------------------------

The following arguments are use only in the X version:

+-------------------+------------+-----------------------------------+
| **Argument**      | **In/Out** | **Description**                   |
+-------------------+------------+-----------------------------------+
| ARGN2             | IO         | The mana loss if the spell is     |
|                   |            | failed.                           |
+-------------------+------------+-----------------------------------+
| local.tithingloss | IO         | The tithing points loss if the    |
|                   |            | spell is failed.                  |
|                   |            |                                   |
|                   |            | `        Whi                      |
|                   |            | le both are writeable, they only  |
|                   |            | works if  ManaLossFail or Reagent |
|                   |            | LossFail ( also for tithing point |
|                   |            | s) are enabled in the sphere.ini` |
+-------------------+------------+-----------------------------------+

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ------------------------------------------------------------------------------
  **Return Value**   **Description**
  1                  Prevents normal fail behaviours (fail message, fizzle effect, reagent loss).
  ------------------ ------------------------------------------------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
