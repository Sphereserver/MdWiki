## Description

This trigger fires when a resource is being gathered and Sphere is
determining which resource to spawn. This trigger fires on every region
resource attached to the region that Sphere is selecting from.

Fires on:

-   [Region Resources](REGIONRESOURCE "wikilink")

## References

The following object references are explicitly available for this
trigger:

  ----------------------- ------------------------------------------------------------------
  **Name**                **Description**
  [I](I "wikilink")       The [region resource](REGIONRESOURCE "wikilink") being gathered.
  [SRC](SRC "wikilink")   The [character](Characters "wikilink") gathering the resource.
  ----------------------- ------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

*No arguments are set for this trigger.*

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ----------------------------------------------
  **Return Value**   **Description**
  1                  Prevents Sphere from selecting the resource.
  ------------------ ----------------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink")
