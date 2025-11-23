## Description

This trigger fires when tooltips are about to be sent to a client. Due to recent changes, tooltips are now cached on the character or item. This means the
[ADDCLILOC](./ADDCLILOC.md) function needs to be called directly on the object (e.g., using `ADDCLILOC`), rather than on the player.

Fires on:

- [Characters](./Characters.md)
- [Items](./Items.md)

## References

The following object references are explicitly available for this
trigger:

  ----------------------- ---------------------------------------------------------------------------------------------------
  **Name**                **Description**
  [I](./I.md)       The [character](./Characters.md) or [item](./Items.md) whose tooltips are to be sent.
  [SRC](./SRC.md)   The [client](./CharactersClients.md) who is receiving tooltips.
  ----------------------- ---------------------------------------------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

*No arguments are set for this trigger.*

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ------------------------------------------------
  **Return Value**   **Description**
  1                  Prevents Sphere from sending its own tooltips.
  ------------------ ------------------------------------------------

## Notes
- `@ClientTooltip` now correctly receives ARGS in all circumstances.

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
Items](./_Items.md)

