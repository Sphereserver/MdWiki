# f_onchar_create_init

This function is called during the character creation process, specifically after the client has sent the character creation data but *before* the character is created server-side. This allows for validation or modification of character creation parameters.

## Parameters

- **Read-Write**:
    - `ARGN1`: Feature flags sent by the client.
    - `ARGN2`: Character profession (0=Advanced, 1=Warrior, 2=Mage, 3=Blacksmith, 4=Necromancer, 5=Paladin, 6=Samurai, 7=Ninja).
    - `ARGN3`: Character race (1=Human, 2=Elf, 3=Gargoyle).
- **Read-Only**:
    - `ARGS`: The account name.
    - `ARGO`: The client creating the character.

## Return Values

- `0`: Allows character creation (default action).
- `1`: Denies character creation.

[Category: Functions](./CategoryFunctions.md)