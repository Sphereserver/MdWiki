## Description

`VAR.TAG` is a powerful construct that allows scripters to retrieve values from Tags stored directly on a `CHARDEF` block. This provides a way to define properties at the CHARDEF level and access them dynamically within scripts.

## Syntax

`<VAR.TAG(x).KEY/VAL>`

## Parameters

- `x`: The index of the TAG (0-based) or the name of the TAG.
- `KEY`: (Optional) If `x` is an index, `KEY` can be used to retrieve the name of the TAG.
- `VAL`: (Optional) If `x` is an index, `VAL` can be used to retrieve the value of the TAG.

## Example

Assuming a CHARDEF has the following TAGs defined:
```
[CHARDEF c_my_creature]
TAG.MyCustomTag=SomeValue
TAG.AnotherTag=AnotherValue
```

- To get the value of `MyCustomTag`: `<VAR.TAG(MyCustomTag)>` or `<VAR.TAG(0).VAL>`
- To get the name of the first TAG: `<VAR.TAG(0).KEY>`

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Variables](./CategoryVariables.md) [Category: CHARDEF](./CategoryCHARDEF.md)