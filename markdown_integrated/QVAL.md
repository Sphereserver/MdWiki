## The first QVAL Syntax

`<QVAL CONDITION ? TRUE : FALSE>`

QVAL is a simple form of the IF-ELSE structure. It is used to test if an argument is true or false in a single line of code.

```
For example, this:

`IF (<EVAL <LOCAL.A>+1> < <LOCAL.B>)`
`   SYSMESSAGE A+1 is smaller than B`
`ELSE`
`   SYSMESSAGE A+1 is greater than or equal to B`
`ENDIF`

...is the same as:

`<QVAL <EVAL <LOCAL.A>+1> < <LOCAL.B> ? SYSMESSAGE A+1 is smaller than B:SYSMESSAGE A+1 is greater than or equal to B>`

In the above statement, if we say that local.a=3 and local.b=5, then local.a+1=4

Since 4 is less that 5, the condition is true, and so the first output (before the : sign) in the true:false condition will be executed

If local.a=5 and local.b=5, then local.a+1=6

Since 6 is not less than 5, the condition will return as false and the second output (after the : sign) in the true:false result will be executed.

Your "if condition" is separated from the results by the ? character. The true and false results are separated by the : character (which ismandatory, even if you dont want anything to happen in one of the cases.)

Be careful if the true:false conditions also require you to use "greater than" It is easy to inadvertently close an argument too soon with a misplaced \> after the ? or : in a QVAL argument. You should use always Less than ( \< ) or Less or Equal ( \<= )

```
## The second QVAL Syntax
```

`QVAL(VALUE1,VALUE2,LESSTHAN,EQUAL,GREATERTHAN)`

This form of the QVAL statement is useful when comparing two values.

For example:

`<eval qval(<VAR.X>,<VAR.Y>,<VAR.ONE>,<VAR.TWO>,<VAR.THREE>)>`

...will return \<VAR.ONE\> if X is less than Y, \<VAR.TWO\> if they are equal, and \<VAR.THREE\> if X greater than Y. If some of the arguments are omited like qval(1,2,,3) it will default to zero.
```
