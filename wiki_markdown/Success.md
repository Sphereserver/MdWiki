## Description

This trigger fires when an attempt to use skill has succeeded.

Fires on:

-   [Skills](SKILL "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ----------------------- ----------------------------------------------------------------------
  **Name**                **Description**
  [I](I "wikilink")       The [character](Characters "wikilink") succeeding the skill attempt.
  [SRC](SRC "wikilink")   The [character](Characters "wikilink") succeeding the skill attempt.
  ----------------------- ----------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ --------------------------------------
  **Argument**   **In/Out**   **Description**
  ARGN1          I            The skill number that has succeeded.
  -------------- ------------ --------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ -----------------------------------------
  **Return Value**   **Description**
  1                  Aborts the skill attempt.
  0                  Aborts the skill, but grants Skillgain.
  2                  Aborts the skill, but grants Skillgain.
                     
  ------------------ -----------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
