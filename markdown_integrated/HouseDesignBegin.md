## Description

X branch only. This trigger is called when the player enters on design
mode in a t_custom_multi multi.

Fires on:

- [Multis](./Multis.md)

## References

The following object references are explicitly available for this
trigger:

|                   |                            |
|-------------------|----------------------------|
| **Name**          | **Description**            |
| [I](./I.md) | The multi about to design. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|  |  |  |
|----|----|----|
| **Argument** | **In/Out** | **Description** |
| ARGN1 | IO | If set to 1 Redeeds all addons on the multi. (Default = 1) |
| ARGN2 | IO | If set to 1 Transfer all Locked Items and Secured containers to the Moving Crate (default = 0) |
| ARGN3 | IO | If set to 1 Ejects from the house all chars inside the house excepting the player entering in design mode, if set to 2 Ejects everyone from the house, if set to 0 doesn't eject anyone. All chars ejected will be moved to the House sign. |

## Return Values

The following return values are explicitly defined for this trigger:

<table>
<tbody>
<tr>
<td><p><strong>Return Value</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>Forces the char to exit Customize mode.</p>
<p><code>   WARNING: Forcing the char to exit here and setting argn1=0 in @HouseDesignExit will make it enter in customize mode, exit, enter... infinitelly, hence crashing the server with an infinite loop.</code></p></td>
</tr>
</tbody>
</table>
