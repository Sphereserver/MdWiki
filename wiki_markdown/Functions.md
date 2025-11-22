## References

The following references are available within function and trigger
scripts. If an attempt is made to access a reference that is not listed
here then the object the function/trigger is called on will be accessed
instead.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [ARGO](./ARGO.md) | RW | Gets or sets a reference to a [character](./Characters.md) or [item](./Items.md). |
| [REF](./REF.md)*x* | RW | Gets or sets a reference to a [character](./Characters.md) or [item](./Items.md). |

## Properties and Functions

The following properties and functions are available within function and
trigger scripts. If an attempt is made to access a property or function
that is not listed here then the object the function/trigger is called
on will be accessed instead.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [ARGN1](./ARGN1.md) | RW | Gets the first parameter passed into the function, as a numeric value. |
| [ARGN2](./ARGN2.md) | RW | Gets the second parameter passed into the function, as a numeric value. |
| [ARGN3](./ARGN3.md) | RW | Gets the third parameter passed into the function, as a numeric value. |
| [ARGS](./ARGS.md) | RW | Gets the entire argument string passed into the function. |
| [ARGV](./ARGV.md) | R | Returns the number of parameters passed into the function. |
| [ARGV](./ARGV.md)\[*n*\] | R | Returns the nth parameter passed into the function. (zero-based) |
| [FLOAT](./FLOAT.md)*.name* | RW | Gets or sets the value of a local floating point variable. |
| [LOCAL](./LOCAL.md)*.name* | RW | Gets or sets the value of a local variable. |
| [RETURN](./RETURN.md) *value* | W | Exits the function, passing *value* back to whatever called it (if the function was used as *\<FUNCTION\>*. *value* can be either a string or numeric value. |
| [TRY](./TRY.md) *command* | W | Executes *command*. |
| [TRYSRV](./TRYSRV.md) *command* | W | Executes *command*, with the [SERV](./Servers.md) object as SRC. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Scripts](./_Scripts.md)
