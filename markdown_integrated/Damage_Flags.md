# Damage_Flags

This page lists the various flags used to define damage types in SphereServer. These flags can be used to specify the nature of damage dealt by abilities, spells, or items.

## Flags

| Flag       | Value   | Description                                                                                                                                                                                |
| :--------- | :------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DAM_BREATH` | `0xXXXX`  | Indicates damage originating from a breath attack (e.g., dragon's fiery breath). This flag is automatically added to `BREATH.DAMTYPE` properties. (Hex value needs verification)             |
| `DAM_THROWN` | `0xXXXX`  | Indicates damage originating from a thrown object (e.g., an NPC throwing an item). This flag is automatically added to `THROWDAMTYPE` properties. (Hex value needs verification)         |

[Category: Game Mechanics](./CategoryGame_Mechanics.md)