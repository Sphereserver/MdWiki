## Description

This trigger fires when a spell memory item is removed (and after the
\@Destroy trigger of the item).

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

  ------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Return Value**   **Description**
  0                  prevents default spell behaviour be executed when the spell item get removed. This is necessary when return 0 is used in \@EffectAdd of the same spell. For Summoning spells, returning 0 in \@EffectRemove will prevent the summon to disappear.
  ------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Note:** Poisoning spells are not affected by this trigger

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
