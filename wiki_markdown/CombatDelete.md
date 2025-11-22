## Description

This trigger fires when someone is being deleted from my attacker list.

Fires on:

-   [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

  ----------------------- -------------------------------------------
  **Name**                **Description**
  [I](./I.md)       Myself.
  [SRC](./SRC.md)   The character being removed from my list.
  ----------------------- -------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

+--------------+------------+----------------------------------------+
| **Argument** | **In/Out** | **Description**                        |
+--------------+------------+----------------------------------------+
| ARGN1        | I          | Shows if the deletion was forced by    |
|              |            | your scripts (1) or called by Sphere   |
|              |            | (0)                                    |
+--------------+------------+----------------------------------------+
| ARGN2        | I          |   -----------------------------------  |
|              |            | ------------------------- ------------ |
|              |            |   **Type description**                 |
|              |            |                             **Values** |
|              |            |   Forced (Blocked attack,              |
|              |            | default uncategorized actions\...)   0 |
|              |            |   Max fight time has reach             |
|              |            | ed (Elapsed)                         1 |
|              |            |   Distance/LOS                         |
|              |            |                                      2 |
|              |            |   The character is no long             |
|              |            | er existing                          3 |
|              |            |   Forced via attacker.dele             |
|              |            | te methods (ingame/script)           4 |
|              |            |   -----------------------------------  |
|              |            | ------------------------- ------------ |
+--------------+------------+----------------------------------------+
|              |            |                                        |
+--------------+------------+----------------------------------------+

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ---------------------------------------------------------------------------------------
  **Return Value**   **Description**
  1                  Prevents src of leaving my list, however I\'ll try to delete him as soon as possible.
  ------------------ ---------------------------------------------------------------------------------------

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
Combat](./_Combat.md)
