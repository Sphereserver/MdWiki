## Description

This trigger fires on all characters who are responsible for another
character\'s death.

The trigger is fired based on the Attacker list, \@Death is called
before it and \@DeathCorpse after, so the \@Death trigger can pre-handle
who will receive this trigger by adding or removing attackers.

Fires on:

-   [Characters](./Characters.md)

## References

The following object references are explicitly available for this
trigger:

  ------------------------- -------------------------------------------------------------
  **Name**                  **Description**
  [ARGO](./ARGO.md)   The [character](./Characters.md) who has been killed.
  [I](./I.md)         The [character](./Characters.md) doing the killing.
  [SRC](./SRC.md)     The [character](./Characters.md) doing the killing.
  ------------------------- -------------------------------------------------------------

## Arguments

The following arguments are set for this trigger. If an argument is
marked as \"In\" then a value will be passed in to the trigger, if an
argument is marked as \"Out\" then it can be set to a value to affect
Sphere\'s behaviour:

  -------------- ------------ --------------------------------------------------------------------
  **Argument**   **In/Out**   **Description**
  ARGN1          I            The total number of characters involved in the character\'s death.
  -------------- ------------ --------------------------------------------------------------------

## Return Values {#return_values}

The following return values are explicitly defined for this trigger:

  ------------------ ---------------------------------------------------------
  **Return Value**   **Description**
  1                  Prevents the killer from receiving credit for the kill.
  ------------------ ---------------------------------------------------------

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
Combat](./_Combat.md)
