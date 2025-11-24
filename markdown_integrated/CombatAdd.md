## Description

This trigger fires when someone is being added to my attacker list.

Fires on:

-   [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

  ----------------------- --------------------------------------------------------------------------------------
  **Name**                **Description**
  [I](./I.md)       Myself, someone is being entering in combat with me (or I am entering in combat with
  [SRC](./SRC.md)   The character entering in my list.
  ----------------------- --------------------------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  ---------- ------------------------------------------------------------------
  **Name**   **Description**
  ARGN1      Threat set to this SRC, if enabled on ini and I\'m not a player.
  ARGN2      Sets wether to add SRC as ignored or not.
  ---------- ------------------------------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ----------------------------------------------------------------------------------------
  **Return Value**   **Description**
  1                  Prevents src of being added to my list, however I will try to add him each time I can.
  ------------------ ----------------------------------------------------------------------------------------

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
Combat](./_Combat.md)
