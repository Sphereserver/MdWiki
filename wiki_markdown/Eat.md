## Description

This trigger fires when someone is eating something.

Fires on:

-   [Characters](Characters "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ------------------------------------------- ------------------------------------------------------------
  **Name**                                    **Description**
  [ARGO](ARGO "wikilink")                     The [item](Items "wikilink") being ate (X ONLY).
  [I](I "wikilink") / [SRC](SRC "wikilink")   The [character](Characters "wikilink") doing the clicking.
  ------------------------------------------- ------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Argument**   **In/Out**   **Description**
  Argn1          I/O          Set to 1 to let it pass your MaxStats, ie: MaxHits=100 and local.hits + hits = 150, having it to 1 will set hits to 150 and setting it to 0 will raise hits up to MaxHits only.
  local.hits     I/O          Amount of HitPoints to regenerate.
  local.mana     I/O          Amount of Mana to regenerate.
  local.stam     I/O          Amount of Stamina to regenerate.
  local.food     I/O          Amount of Food to regenerate.
  -------------- ------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ------------------------------------------------
  **Return Value**   **Description**
  1                  Prevents the gain of stats but not the eating.
  ------------------ ------------------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
