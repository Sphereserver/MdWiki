## Description

This trigger fires when a character calls for the guards to attack a
criminal.

Fires on:

- [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ------------------------- ---------------------------------------------------------------------------------------------------------------

  **Name**                  **Description**
  [ARGO](ARGO "wikilink")   The guard [character](Characters "wikilink") who is going to attack the criminal (if one exists in the area).
  [I](I "wikilink")         The [character](Characters "wikilink") calling for guards.
  [REF1](REF1 "wikilink")   The [criminal](Characters "wikilink") who the guards are being called upon.
  [SRC](SRC "wikilink")     The [criminal](Characters "wikilink") who the guards are being called upon.

  ------------------------- ---------------------------------------------------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ ------------------------------------------------------------------------------------------------

  **Argument**   **In/Out**   **Description**
  ARGN1          IO           The [BASEID](BASEID "wikilink") of the [character](Characters "wikilink") to spawn as a guard.
  ARGN2          O            If set to 1, a new guard will be spawned regardless of whether a nearby guard is available.

  -------------- ------------ ------------------------------------------------------------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ---------------------------------------------------------------------------------------------------------------------------

  **Return Value**   **Description**
  1                  Prevents the guards from reacting. (When firing on a player, will prevent the guards attacking the next possible targets)

  ------------------ ---------------------------------------------------------------------------------------------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink") [Category:
Characters](Category:_Characters "wikilink") [Category:
Combat](Category:_Combat "wikilink")
