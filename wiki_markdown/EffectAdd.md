## Description

This trigger fires when any type of effect memory is being added, like
stat changes for s_bless, s_cunning\... s_weaken \...

Fires on:

-   [Spells](SPELL "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ------------------------- -------------------------------------------------------------------
  **Name**                  **Description**
  [ARGO](ARGO "wikilink")   The memory item.
  [I](I "wikilink")         The [character](Characters "wikilink") affected by the effect.
  [SRC](SRC "wikilink")     The [character](Characters "wikilink") responsible for the spell.
  ------------------------- -------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ -----------------
  **Argument**   **In/Out**   **Description**
  ARGN1          I            The spell ID
  -------------- ------------ -----------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ --------------------------------------------------------------------------------------------------------------------------------------------------
  **Return Value**   **Description**
  0                  Let the memory exist but block default checks, perfect to override default effects and do some custom stuff.
  1                  Blocks any action and stops everything, also deletes the memory (Blocking any changes, this will cause also the effect to do not have duration).
  ------------------ --------------------------------------------------------------------------------------------------------------------------------------------------

**Note:** Poisoning spells are not affected by this trigger

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
