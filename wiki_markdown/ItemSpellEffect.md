## Description

This trigger fires when a character hits an item with a spell. The item
may have been targeted directly or it may have been hit by an
area-effect spell.

Fires on:

-   [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ------------------------- ------------------------------------------------------------------------------
  **Name**                  **Description**
  [ACT](ACT "wikilink")     The [item](Items "wikilink") being hit by the spell.
  [ARGO](ARGO "wikilink")   The [item](Items "wikilink") used to cast the spell (e.g. a wand or scroll).
  [I](I "wikilink")         The [character](Characters "wikilink") responsible for the spell.
  ------------------------- ------------------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

+--------------+------------+----------------------------------------+
| **Argument** | **In/Out** | **Description**                        |
+--------------+------------+----------------------------------------+
| ARGN1        | IO         | The number of the spell that has hit   |
|              |            | the object.                            |
+--------------+------------+----------------------------------------+
| ARGN2        | IO         | The strength of the spell.             |
+--------------+------------+----------------------------------------+
| ARGN3        | IO         | A multiplier for the spell\'s duration |
|              |            | or effect.\                            |
|              |            | **Note:** Only used when a character   |
|              |            | is hit by a spell.                     |
+--------------+------------+----------------------------------------+

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ -----------------------------------------------------
  **Return Value**   **Description**
  1                  Prevents the item from being affected by the spell.
  ------------------ -----------------------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
