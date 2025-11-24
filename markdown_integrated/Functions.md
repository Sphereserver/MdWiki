## References

The following references are available within function and trigger
scripts. If an attempt is made to access a reference that is not listed
here then the object the function/trigger is called on will be accessed
instead.

  -------------------------- ---------------- -----------------------------------------------------------------------------------------------
  **Name**                   **Read/Write**   **Description**
  [ARGO](ARGO "wikilink")    RW               Gets or sets a reference to a [character](Characters "wikilink") or [item](Items "wikilink").
  [REF](REF "wikilink")*x*   RW               Gets or sets a reference to a [character](Characters "wikilink") or [item](Items "wikilink").
  -------------------------- ---------------- -----------------------------------------------------------------------------------------------

## Properties and Functions {#properties_and_functions}

The following properties and functions are available within function and
trigger scripts. If an attempt is made to access a property or function
that is not listed here then the object the function/trigger is called
on will be accessed instead.

  --------------------------------------- ---------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                                **Read/Write**   **Description**
  [ARGN1](ARGN1 "wikilink")               RW               Gets the first parameter passed into the function, as a numeric value.
  [ARGN2](ARGN2 "wikilink")               RW               Gets the second parameter passed into the function, as a numeric value.
  [ARGN3](ARGN3 "wikilink")               RW               Gets the third parameter passed into the function, as a numeric value.
  [ARGS](ARGS "wikilink")                 RW               Gets the entire argument string passed into the function.
  [ARGV](ARGV "wikilink")                 R                Returns the number of parameters passed into the function.
  [ARGV](ARGV "wikilink")\[*n*\]          R                Returns the nth parameter passed into the function. (zero-based)
  [FLOAT](FLOAT "wikilink")*.name*        RW               Gets or sets the value of a local floating point variable.
  [LOCAL](LOCAL "wikilink")*.name*        RW               Gets or sets the value of a local variable.
  [RETURN](RETURN "wikilink") *value*     W                Exits the function, passing *value* back to whatever called it (if the function was used as *\<FUNCTION\>*. *value* can be either a string or numeric value.
  [TRY](TRY "wikilink") *command*         W                Executes *command*.
  [TRYSRV](TRYSRV "wikilink") *command*   W                Executes *command*, with the [SERV](Servers "wikilink") object as SRC.
  --------------------------------------- ---------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------

[Category: Reference

Compendium](Category_Reference_Compendium.md) [Category:

Scripts](CategoryScripts.md)
