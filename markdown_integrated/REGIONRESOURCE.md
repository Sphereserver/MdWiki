```{=mediawiki}
{{Languages|REGIONRESOURCE}}
```
\_\_FORCETOC\_\_ A region resource block defines a resource that can be
found in a region.

## Properties

The following properties are available when defining a region resource:

  ------------------------------------------------------ ---------------- ---------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                                               **Read/Write**   **Description**
  [AMOUNT](./AMOUNT.md)                            RW               Gets or sets the initial amount of the resource available when it spawns. Accepts multiple values to build a weighted range of difficulty values.
  [DEFNAME](./DEFNAME.md)                          W                Gets or sets the resource defname.
  [REAP](./REAP.md)                                RW               Gets or sets the [BASEID](./BASEID.md) of the resource item.
  [REAPAMOUNT](./REAPAMOUNT.md)                    RW               Gets or sets the amount of the resource that can be gathered in one use of a skill. Accepts multiple values to adjust based on skill level.
  [REGEN](./REGEN.md)                              RW               Gets or sets the length of time it takes for the resource to decay, in seconds.
  [SKILL](SKILL_(Region_Resource_Property) "wikilink")   RW               Gets or sets the difficulty of gathering the resource. Accepts multiple values to build a weighted range of difficulty values.
  ------------------------------------------------------ ---------------- ---------------------------------------------------------------------------------------------------------------------------------------------------

## Triggers

Here is a list of all region resource triggers. Click on the trigger
name for more detailed information such as arguments and examples.

  ------------------------------------------------ -----------------------------------------------------------
  **Name**                                         **Description**
  [\@ResourceFound](./ResourceFound.md)     Fires when the resource is spawned.
  [\@ResourceGather](./ResourceGather.md)   Fires when you are going to gather a resource.
  [\@ResourceTest](./ResourceTest.md)       Fires when the resource is being considered for spawning.
  ------------------------------------------------ -----------------------------------------------------------

## Examples

`<spherescript>`{=html} // // Fish resource from default script pack. //
\[REGIONRESOURCE mr_fish1\] SKILL=1.0,100.0 // requires between 1% and
100% skill to gather AMOUNT=9,30 // between 9 and 30 fish available
REAP=i_fish_big_1 // the resource item REGEN=60\*60\*10 // decays after
10 hours `</spherescript>`{=html}

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Objects](./_Objects.md)
