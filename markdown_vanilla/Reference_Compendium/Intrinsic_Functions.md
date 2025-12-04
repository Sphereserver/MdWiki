Intrinsic functions are special functions that can only be used within evaluation functions, such as [EVAL](EVAL "wikilink"), [FEVAL](FEVAL "wikilink"), [FHVAL](FHVAL "wikilink"), [FVAL](FVAL "wikilink"), [HVAL](HVAL "wikilink"), and [UVAL](UVAL "wikilink"). Some of the builtin functions and properties will automatically evaluate their parameters, for example the [IF](IF "wikilink"), [WHILE](WHILE "wikilink") statements will automatically evaluate their conditions.

Unlike the syntax for normal functions (\<FUNCTION args\>), the syntax
```
for returning a value from an instrinsic function is:

`FUNCTION(`*`args`*`)`

The following table details all of the intrinsic functions in SphereServer:

```
|  |  |
|----|----|
| **Name** | **Description** |
| [ABS](ABS "wikilink")(*value*) | Returns the absolute *value* of a number. |
| [COS](COS "wikilink")(*value*) | Returns the cosine of *value*. |
| [ID](ID "wikilink")(*defname*) | Returns the numeric value of *defname*. |
| [ISOBSCENE](ISOBSCENE "wikilink")(*text*) | Returns 1 if *text* is considered to contain obscene language. |
| [ISNUMBER](ISNUMBER "wikilink")(*value*) | Returns 1 if *value* is a number. |
| [LOGARITHM](LOGARITHM "wikilink")(*value*) | Returns the base-10 logarithm of *value*. |
| [LOGARITHM](LOGARITHM "wikilink")(*value*, *base*) | Returns the base-*base* logarithm of *value*. (Accepts "e" and "pi" as bases, as well as numeric values) |
| [NAPIERPOW](NAPIERPOW "wikilink")(*value*) | Returns e (2.7182818) to the power of *value*. |
| [QVAL](QVAL "wikilink")(*a, b, less_than, equal_to, greater_than*) | Returns *less_than* if *a* is less than *b*, *equal_to* is *a* is equal to *b*, or *greater_than* if *a* is greater than *b*. |
| [RAND](RAND "wikilink")(*value*) | Returns a random value between 0 *value-1*. |
| [RAND](RAND "wikilink")(*min, max*) | Returns a random value between *min* and *max*. |
| [RANDBELL](RANDBELL "wikilink")(*value, variance*) | Calculates a value based on a bell-shaped curve. |
| [SIN](SIN "wikilink")(*value*) | Returns the sine of *value*. |
| [STRCMP](STRCMP "wikilink")(*string1, string2*) | Compares *string1* to *string2* and returns the result. Case-sensitive. (\<= 1 = *string1* less than *string2*, 0 = *string1* equal to *string2*, \>= 1 = *string1* greater than *string2*) |
| [STRCMPI](STRCMPI "wikilink")(*string1, string2*) | Compares *string1* to *string2* and returns the result. Case-insenstive. (\<= 1 = *string1* less than *string2*, 0 = *string1* equal to *string2*, \>= 1 = *string1* greater than *string2*) |
| [STRINDEXOF](STRINDEXOF "wikilink")(*text, search, n*) | Returns the index of the *search* string within *text*, starting from the *n*th character. (zero-based) |
| [STRLEN](STRLEN "wikilink")(*text*) | Returns the length of *text*. |
| [STRMATCH](STRMATCH "wikilink")(*pattern, text*) | Returns 1 if *text* matches the specified wildcard *pattern*. |
| [STRREGEX](STRREGEX "wikilink")(*pattern, text*) | Returns 1 if *text* matches the specified regular expression *pattern*. |
| [SQRT](SQRT "wikilink")(*value*) | Returns the square root of *value*. |
| [TAN](TAN "wikilink")(*value*) | Returns the tangent of *value*. |
```

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Scripts](Category:_Scripts "wikilink")
```
