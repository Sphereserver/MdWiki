```{=mediawiki}
{{Languages|@ItemDamage}}
```
\_\_FORGETOC\_\_

## Description

This trigger fires when a character damages an item.

Fires on:

-   [Items](Items "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ----------------------- --------------------------------------------------------------------
  **Name**                **Description**
  [ACT](ACT "wikilink")   The [item](Items "wikilink") taking damage.
  [I](I "wikilink")       The [character](Characters "wikilink") responsible for the damage.
  ----------------------- --------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ -------------------------------------
  **Argument**   **In/Out**   **Description**
  ARGN1          I            The amount of damage being applied.
  ARGN2          I            The damage attributes.
  -------------- ------------ -------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ---------------------------------------
  **Return Value**   **Description**
  1                  Prevents the item from being damaged.
  ------------------ ---------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
