# @NPCActWander

This trigger is called each step an NPC does while wandering.

## Ficha

|              |                    |
|--------------|--------------------|
| **Trigger**  | **@NPCActWander**  |
| **Type**     | Character (NPC)    |
| **Access**   | Read               |
| **Sphere X** | Yes                |

## Arguments

The following arguments are set for this trigger:

| Argument | Description |
|----------|-------------|
| ARGN1    | Wandering decision: `0` for continue wandering, `1` for randomly deciding to stop, `2` for stopping after finding something interesting. |
| ARGN2    | Returning home: `1` if the NPC is returning to home, `0` otherwise. |

## Return Values

| Return Value | Description |
|--------------|-------------|
| 1            | Stops decisions for this step (NPC will not return home, take another step, or stop wandering for this step). |

[Category: Triggers](CategoryTriggers.md)
