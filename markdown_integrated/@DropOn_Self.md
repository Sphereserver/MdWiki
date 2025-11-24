# @DropOn_Self

This trigger fires when an item has been dropped on to this item.

## Ficha

|              |                  |
| ------------ | ---------------- |
| **Trigger**  | **@DropOn_Self** |
| **Type**     | Item             |
| **Access**   | Read             |
| **Sphere X** | Yes              |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

| Argument | In/Out | Description             |
| -------- | ------ | ----------------------- |
| ARGO     | I      | The item being dropped. |

## Return Values

The following return values are explicitly defined for this trigger:

| Return Value | Description                           |
| ------------ | ------------------------------------- |
| 1            | Prevents the item from being dropped. |

## Notes

- This trigger is now called by the `BOUNCE` function. If a `RETURN 1` is performed and a new `CONT` has not been set via scripts on the trigger call, the item is dropped on the ground, otherwise the item is left in the new `CONT`.

[Category: Triggers](CategoryTriggers.md)
