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

[Category: Skills](CategorySkills.md)
