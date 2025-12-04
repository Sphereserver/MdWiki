## Description

This trigger fires when a multi is about to redeed. Valid for `t_multi`, `t_ship`, `t_multi_custom` and `t_addon.`

Fires on:

- [Items](Items "wikilink")

## References

The following object references are explicitly available for this trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](ARGO "wikilink") | The deed |
| [I](I "wikilink") | The multi |
| [SRC](SRC "wikilink") | Player doing the redeed (If Any). When the multi is being removed there is no SRC (also when an Addon is being redeeded from internal functions). |

## Arguments

The following arguments are set for this trigger. If an argument is marked as "In" then a value will be passed in to the trigger, if an argument is marked as "Out" then it can be set to a value to affect Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | I | ID of the deed (Default=i_deed) |
| ARGN2 | I | (Default = 1). If set to 1 all items will be moved to the Moving Crate (and Addons redeeded). |
| ARGN3 | I | If set to 1 the Moving Crate will be transfered to Owner's Bank (if there is any). Note: the crate is moved to the OWNER's bank, not SRC. If argn2 = 0 then argn3 will be not used regardless of the value it has. |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Prevents the deed from being created, but will not block the code from argn2 and argn3 |

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Triggers](Category:_Triggers "wikilink")
