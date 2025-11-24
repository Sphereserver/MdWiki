# f_multi_setup

The `f_multi_setup` function is a new function called automatically after a multi-part object (like a house or ship) has been fully created, placed in the world, and all its components have been added. This function provides a dedicated point for setting up events and types for the multi, eliminating the need for complex workarounds during the multi-creation process.

## Syntax

`f_multi_setup()`

## Parameters

This function accepts no arguments.

## Return Values

This function returns no values.

## Notes

- This function is particularly useful for attaching events (`EVENTS` or `TEVENTS`) or setting `TYPE` properties that rely on the multi being fully constructed and placed in the world.

[Category: Functions](./CategoryFunctions.md)