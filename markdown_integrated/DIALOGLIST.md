

## Properties and Functions

Here is a list of all dialoglist properties and functions. If a function is marked as readable then it can return a value when used as <KEY>. Click on the name for more detailed information such as usage and examples.

This parameters must use with [DIALOGLIST](#Properties_and_Functions "wikilink"). For examples, please go [Examples](#Examples "wikilink").

|  |  |  |
|----|----|----|
| **DIALOGLIST***.key* | **Read/Write** | **Description** |
| [COUNT](COUNT "wikilink") | R | Gets the number of number of dialogs currently considered to be visible on SRC's screen. |
| *n*.[COUNT](COUNT "wikilink") | R | Gets the number of instances of nth dialog SRC has open (zero-based). |
| *n*.[ID](ID "wikilink") | R | Gets the ID of the nth dialog that SRC has open (zero-based). |

## Examples

The following examples are about [dialoglist](#Properties_and_Functions "wikilink").

**DIALOGLIST.COUNT**

------------------------------------------------------------------------

 \[Function dialogtotal\] `SERV.LOG` Total number of dialogs: \<dialoglist.count\>

You will see *total number of dialogs* output to the console.

**DIALOGLIST***.n***.COUNT**

------------------------------------------------------------------------

 \[Function dialogtotal\] `SERV.LOG` Instant dialogs: \<dialoglist.0.count\>

You will see *how many dialog same id with first dialog* output to the concole.

**DIALOGLIST***.n***.ID**

------------------------------------------------------------------------

 \[Function dialogtotal\] `SERV.LOG` First dialog id: \<dialoglist.0.id\>

You will see *id for first dialog* output to the console.
