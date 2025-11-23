# ACTION

This property gets or sets the skill that the character is currently using.

## Ficha

|              |               |
|--------------|---------------|
| **Property** | **ACTION**    |
| **Type**     | Character     |
| **Access**   | Read/Write    |
| **Sphere X** | Yes           |

## Notes

- Previously, `<ACTION>` returned the skill defname. Now it returns the skill key directly. For example, it returns `hiding` instead of `skill_hiding`.
- This property is now stored in save files, ensuring that the character's current action is preserved across server restarts.

[Category: Properties](CategoryProperties.md)
