## Description

This trigger fires when a player renames another character. The trigger
also fires at character creation when the player's name is set.

Fires on:

- [Players](./CharactersPlayers.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](./ARGO.md) | The [character](./Characters.md) being renamed. |
| [I](./I.md) | The [player](./CharactersPlayers.md) renaming the character. |
| [SRC](./SRC.md) | The [player](./CharactersPlayers.md) renaming the character. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

|              |            |                             |
|--------------|------------|-----------------------------|
| **Argument** | **In/Out** | **Description**             |
| ARGS         | I          | The name that is being set. |

## Return Values

The following return values are explicitly defined for this trigger:

|  |  |
|----|----|
| **Return Value** | **Description** |
| 1 | Disallows the new name. **Note:** During character creation, this will force the character to be named using the NAMES_HUMANMALE or NAMES_HUMANFEMALE [name pool](./NAMES.md). |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
