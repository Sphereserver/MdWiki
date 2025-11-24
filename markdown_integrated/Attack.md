## Description

This trigger fires when one character initiates an attack on another.

Fires on:

-   [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

  ----------------------- ---------------------------------------------------------------
  **Name**                **Description**
  [I](./I.md)       The [character](./Characters.md) initiating the attack.
  [SRC](./SRC.md)   The [character](./Characters.md) being attacked.
  ----------------------- ---------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  --------------------------- ---------------------------------------------------------------------------------------------
  **Name**                    **Description**
  [ARGN1](./ARGN1.md)   Threat being assigned to the target after starting the fight (Only for NPCs).
  [ARGN2](./ARGN2.md)   replace Ignore status. 1-\>Force to ignore attacker 0-\>Force to unignore attacker (X-ONLY)
  --------------------------- ---------------------------------------------------------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ----------------------------------------
  **Return Value**   **Description**
  1                  Prevents the character from attacking.
  ------------------ ----------------------------------------

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
Combat](./_Combat.md)
