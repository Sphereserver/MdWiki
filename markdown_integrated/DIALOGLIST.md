```{=mediawiki}
{{Languages|DIALOGLIST}}
```
\_\_FORCETOC\_\_

## Properties and Functions {#properties_and_functions}

Here is a list of all dialoglist properties and functions. If a function
is marked as readable then it can return a value when used as
`<KEY>`{=html}. Click on the name for more detailed information such as
usage and examples.

This parameters must use with
[DIALOGLIST](./Properties_and_Functions.md). For examples, please
go [Examples](./Examples.md).

  ------------------------------- ---------------- -------------------------------------------------------------------------------------------
  **DIALOGLIST***.key*            **Read/Write**   **Description**
  [COUNT](./COUNT.md)       R                Gets the number of number of dialogs currently considered to be visible on SRC\'s screen.
  *n*.[COUNT](./COUNT.md)   R                Gets the number of instances of nth dialog SRC has open (zero-based).
  *n*.[ID](./ID.md)         R                Gets the ID of the nth dialog that SRC has open (zero-based).
  ------------------------------- ---------------- -------------------------------------------------------------------------------------------

## Examples

The following examples are about
[dialoglist](./Properties_and_Functions.md).

**DIALOGLIST.COUNT**

------------------------------------------------------------------------

`<spherescript>`{=html} \[Function dialogtotal\] SERV.LOG Total number
of dialogs: \<dialoglist.count\> `</spherescript>`{=html}

You will see *total number of dialogs* output to the console.

**DIALOGLIST***.n***.COUNT**

------------------------------------------------------------------------

`<spherescript>`{=html} \[Function dialogtotal\] SERV.LOG Instant
dialogs: \<dialoglist.0.count\> `</spherescript>`{=html}

You will see *how many dialog same id with first dialog* output to the
concole.

**DIALOGLIST***.n***.ID**

------------------------------------------------------------------------

`<spherescript>`{=html} \[Function dialogtotal\] SERV.LOG First dialog
id: \<dialoglist.0.id\> `</spherescript>`{=html}

You will see *id for first dialog* output to the console.
