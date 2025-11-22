## Description

This trigger fires when a character successfully casts a spell.

Fires on:

-   [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                  **Description**
  [ARGO](ARGO "wikilink")   The source of the spell. Could be the [item](Items "wikilink") used to cast the spell (e.g. a wand or scroll) or the [character](Characters "wikilink") casting the spell.
  [I](I "wikilink")         The [character](Characters "wikilink") casting the spell.
  [SRC](SRC "wikilink")     The [character](Characters "wikilink") casting the spell.
  [ACT](ACT "wikilink")     The target of the spell, if any.
  ------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

+---------------------+------------+---------------------------------+
| **Argument**        | **In/Out** | **Description**                 |
+---------------------+------------+---------------------------------+
| ARGN1               | I          | The spell that was cast.        |
+---------------------+------------+---------------------------------+
| ARGN2               | IO         | The strength of the spell.      |
+---------------------+------------+---------------------------------+
| LOCAL.CREATEOBJECT1 | O          | For field spells, overrides the |
|                     |            | item                            |
|                     |            | [BASEID](BASEID "wikilink") to  |
|                     |            | use for the east-west           |
|                     |            | direction.                      |
|                     |            |                                 |
|                     |            | For summon spells, overrides    |
|                     |            | the character                   |
|                     |            | [BASEID](BASEID "wikilink") to  |
|                     |            | summon.                         |
+---------------------+------------+---------------------------------+
| LOCAL.CREATEOBJECT2 | O          | For field spells, overrides the |
|                     |            | item                            |
|                     |            | [BASEID](BASEID "wikilink") to  |
|                     |            | use for the north-south         |
|                     |            | direction.                      |
+---------------------+------------+---------------------------------+
| LOCAL.FIELDGAUGE    | O          | For field spells, overrides the |
|                     |            | default gauge of the field (1). |
+---------------------+------------+---------------------------------+
| LOCAL.FIELDWIDTH    | O          | For field spells, overrides the |
|                     |            | default width of the field (7). |
+---------------------+------------+---------------------------------+
| LOCAL.EFFECTCOLOR   | O          | For field spells, overrides the |
|                     |            | color of the fields.            |
+---------------------+------------+---------------------------------+

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ---------------------------
  **Return Value**   **Description**
  1                  Aborts casting the spell.
  ------------------ ---------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
