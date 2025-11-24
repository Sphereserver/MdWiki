## Description

This function schedules a script function to be executed on an object after a specified time.

## Ficha

|              |             |
|--------------|-------------|
| **Function** | **TIMERF**  |
| **Type**     | Object      |
| **Access**   | Write       |
| **Sphere X** | Yes         |

## Syntax

`[object].TIMERF time, function_name`
`[object].TIMERF CLEAR`
`[object].TIMERF STOP, function_name`

## Parameters

- `time`: The delay in seconds before the `function_name` is executed.
- `function_name`: The name of the script function to execute.
- `CLEAR`: Clears all scheduled functions from the object.
- `STOP, function_name`: Stops the specified function from the object.

## Notes
- The `MaxLoopTimes` setting in `sphere.ini` now controls `TIMERF` executions. If too many `TIMERFs` are executed in a single tick, the loop will be aborted and a warning issued. Setting `MaxLoopTimes` to 0 removes this limit, but it is recommended to set a value to prevent deadlocks from script errors.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)