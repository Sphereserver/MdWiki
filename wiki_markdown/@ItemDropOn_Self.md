## Description

This trigger fires when a character drops an item inside another item (e.g. a backpack).

## References

| Name | Description |
| --- | --- |
| ACT | The item that is being dropped on to. |
| ARGO | The item being dropped on to the item. |
| I | The character dropping the item. |

## Arguments

No arguments are set for this trigger.

## Return Values

| Return Value | Description |
| --- | --- |
| 1 | Prevents the item from being dropped on to the item. If no CONT is set, item will drop on ground. If a RETURN 1 is performed and a new CONT has not been set via scripts on the trigger call, the item is dropped on ground, otherwise the item is left in the new CONT. |

## Notes
- `BOUNCE` now calls this trigger.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Triggers](./CategoryTriggers.md)