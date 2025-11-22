## Description

This trigger fires when a character calls for the guards to attack a
criminal.

Fires on:

-   [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

  ------------------------- ---------------------------------------------------------------------------------------------------------------
  **Name**                  **Description**
  [ARGO](./ARGO.md)   The guard [character](./Characters.md) who is going to attack the criminal (if one exists in the area).
  [I](./I.md)         The [character](./Characters.md) calling for guards.
  [REF1](./REF1.md)   The [criminal](./Characters.md) who the guards are being called upon.
  [SRC](./SRC.md)     The [criminal](./Characters.md) who the guards are being called upon.
  ------------------------- ---------------------------------------------------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ ------------------------------------------------------------------------------------------------
  **Argument**   **In/Out**   **Description**
  ARGN1          IO           The [BASEID](./BASEID.md) of the [character](./Characters.md) to spawn as a guard.
  ARGN2          O            If set to 1, a new guard will be spawned regardless of whether a nearby guard is available.
  -------------- ------------ ------------------------------------------------------------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ---------------------------------------------------------------------------------------------------------------------------
  **Return Value**   **Description**
  1                  Prevents the guards from reacting. (When firing on a player, will prevent the guards attacking the next possible targets)
  ------------------ ---------------------------------------------------------------------------------------------------------------------------

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
Combat](./_Combat.md)
