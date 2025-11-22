## Description

This trigger fires when a player sends an extended command packet
(packet 0x12).

Fires on:

-   [Players](Characters#Players "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ----------------------- ------------------------------------------------------------------
  **Name**                **Description**
  [I](I "wikilink")       The [player](Characters#Players "wikilink") sending the command.
  [SRC](SRC "wikilink")   The [player](Characters#Players "wikilink") sending the command.
  ----------------------- ------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

+--------------+------------+----------------------------------------+
| **Argument** | **In/Out** | **Description**                        |
+--------------+------------+----------------------------------------+
| ARGN1        | I          | The command type. Known commands are:  |
|              |            |                                        |
|              |            |   ------------- ---------------------- |
|              |            |   **Command**   **Description**        |
|              |            |   0x24          Use Skill macro        |
|              |            |   0x27          Cast spell from book   |
|              |            |   0x2F          Auto targeting macro   |
|              |            |   0x43          Open Spellbook macro   |
|              |            |   0x56          Cast Spell macro       |
|              |            |   0x88          Open Door macro        |
|              |            |   0x6B          God Client command     |
|              |            |   0xC7          Bow or Salute macro    |
|              |            |   0xF4          Invoke Virtue macro    |
|              |            |   ------------- ---------------------- |
+--------------+------------+----------------------------------------+
| ARGS         | IO         | The command text.                      |
+--------------+------------+----------------------------------------+

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
