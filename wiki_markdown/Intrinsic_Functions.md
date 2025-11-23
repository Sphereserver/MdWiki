```{=mediawiki}
{{Languages|Intrinsic_Functions}}
```
Intrinsic functions are special functions that can only be used within
evaluation functions, such as [EVAL](./EVAL.md),
[FEVAL](./FEVAL.md), [FHVAL](./FHVAL.md),
[FVAL](./FVAL.md), [HVAL](./HVAL.md), and
[UVAL](./UVAL.md). Some of the builtin functions and properties
will automatically evaluate their parameters, for example the
[IF](./IF.md), [WHILE](./WHILE.md) statements will
automatically evaluate their conditions.

Unlike the syntax for normal functions (\<FUNCTION args\>), the syntax
for returning a value from an instrinsic function is:

`FUNCTION(`*`args`*`)`\

Arguments for intrinsic functions are now recognized even if separated by a whitespace from the function, in addition to being enclosed by parentheses. For example, `MIN(1, 2)` and `MIN 1, 2` are both valid.

The following table details all of the intrinsic functions in
SphereServer:

  -------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                                                             **Description**
  [ABS](./ABS.md)(*value*)                                       Returns the absolute *value* of a number.
  [COS](./COS.md)(*value*)                                       Returns the cosine of *value*.
  [ID](./ID.md)(*defname*)                                       Returns the numeric value of *defname*.
  [ISOBSCENE](./ISOBSCENE.md)(*text*)                            Returns 1 if *text* is considered to contain obscene language.
  [ISNUMBER](./ISNUMBER.md)(*value*)                             Returns 1 if *value* is a number.
  [LOGARITHM](./LOGARITHM.md)(*value*)                           Returns the base-10 logarithm of *value*.
  [LOGARITHM](./LOGARITHM.md)(*value*, *base*)                   Returns the base-*base* logarithm of *value*. (Accepts \"e\" and \"pi\" as bases, as well as numeric values)
  [NAPIERPOW](./NAPIERPOW.md)(*value*)                           Returns e (2.7182818) to the power of *value*.
  [QVAL](./QVAL.md)(*a, b, less_than, equal_to, greater_than*)   Returns *less_than* if *a* is less than *b*, *equal_to* is *a* is equal to *b*, or *greater_than* if *a* is greater than *b*.
  [RAND](./RAND.md)(*value*)                                     Returns a random value between 0 *value-1*.
  [RAND](./RAND.md)(*min, max*)                                  Returns a random value between *min* and *max*.
  [RANDBELL](./RANDBELL.md)(*value, variance*)                   Calculates a value based on a bell-shaped curve.
  [SIN](./SIN.md)(*value*)                                       Returns the sine of *value*.
  [STRCMP](./STRCMP.md)(*string1, string2*)                      Compares *string1* to *string2* and returns the result. Case-sensitive. (\<= 1 = *string1* less than *string2*, 0 = *string1* equal to *string2*, \>= 1 = *string1* greater than *string2*)
  [STRCMPI](./STRCMPI.md)(*string1, string2*)                    Compares *string1* to *string2* and returns the result. Case-insenstive. (\<= 1 = *string1* less than *string2*, 0 = *string1* equal to *string2*, \>= 1 = *string1* greater than *string2*)
  [STRINDEXOF](./STRINDEXOF.md)(*text, search, n*)               Returns the index of the *search* string within *text*, starting from the *n*th character. (zero-based)
  [STRLEN](./STRLEN.md)(*text*)                                  Returns the length of *text*.
  [STRMATCH](./STRMATCH.md)(*pattern, text*)                     Returns 1 if *text* matches the specified wildcard *pattern*.
  [STRREGEX](./STRREGEX.md)(*pattern, text*)                     Returns 1 if *text* matches the specified regular expression *pattern*.
  [SQRT](./SQRT.md)(*value*)                                     Returns the square root of *value*.
  [TAN](./TAN.md)(*value*)                                       Returns the tangent of *value*.
  -------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Scripts](./_Scripts.md)