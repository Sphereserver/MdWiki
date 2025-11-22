## Description

This trigger fires when an attempt to quickly use a skill is made
without changing the character\'s [ACTION](ACTION "wikilink") property.

Fires on:

-   [Skills](SKILL "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ----------------------- -----------------------------------------------------------------
  **Name**                **Description**
  [I](I "wikilink")       The [character](Characters "wikilink") quickly using the skill.
  [SRC](SRC "wikilink")   The [character](Characters "wikilink") quickly using the skill.
  ----------------------- -----------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ -----------------------------------------------------
  **Argument**   **In/Out**   **Description**
  ARGN1          I            The skill number that is being used.
  ARGN2          IO           The difficulty of the skill attempt.
  ARGN3          IO           If 0 then the skill failed, if 1 then it succeeded.
  -------------- ------------ -----------------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ -----------------------------------------------------
  **Return Value**   **Description**
  0                  Fails the skill use without awarding skill gain.
  1                  Succeeds the skill use without awarding skill gain.
  ------------------ -----------------------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
