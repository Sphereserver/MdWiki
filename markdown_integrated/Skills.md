# Skills

This page lists various skills available in Sphere, including crafting skills and their associated recipes.

## Crafting Skills

The following crafting skills have associated recipes:

*   RecipeAlchemy
*   RecipleBlacksmith
*   RecipeBowcraft
*   RecipeCarpentry
*   RecipeCartography
*   RecipeCooking
*   RecipeInscription
*   RecipeTailoring
*   RecipeTinkering
*   RecipeMasonry
*   RecipeGlassblowing

## Specific Skill Notes
- For skills like Enticement, Peacemaking, and Provocation, if `ACTARG1` is set to the UID of an instrument to play, the sound of that instrument will be played.
- **Provocation Skill Override**: If the provoked character is in the same ally group as the targeted character, `ACTARG3` will be set to 1 in the `@Start` trigger (otherwise 0). To always allow Provocation, set `ACTARG3=0` in `@Start` or `@Success`.
- **Veterinary Skill**: The Veterinary skill now functions with all tameable creatures, which includes NPCs having a brain type of `BRAIN_ANIMAL`, `BRAIN_DRAGON`, or `BRAIN_MONSTER`, and possessing a Taming skill greater than 0. Previously, it was limited to `BRAIN_ANIMAL` NPCs. A tameable NPC is defined as having a Taming skill above 0, an Animal Lore skill set to 0, and an ID that is not one of the playable character races.

[Category: Skills](CategorySkills.md)
