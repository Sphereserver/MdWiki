## Description

This trigger fires when a character\'s health reaches zero and they are
about to die.

Fires on:

-   [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

  ----------------------- ------------------------------------------------------
  **Name**                **Description**
  [I](./I.md)       The [character](./Characters.md) about to die.
  [SRC](./SRC.md)   The [character](./Characters.md) about to die.
  ----------------------- ------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

*No arguments are set for this trigger.*

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

+------------------+--------------------------------------------------+
| **Return Value** | **Description**                                  |
+------------------+--------------------------------------------------+
| 1                | Prevents the death from taking place.\           |
|                  | **Note:** The trigger will fire again unless the |
|                  | script changes the character\'s health to above  |
|                  | zero.                                            |
+------------------+--------------------------------------------------+

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
Combat](./_Combat.md)
