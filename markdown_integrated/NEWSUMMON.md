## Description
This function creates a new summoned creature. It works similarly to NEWNPC and NEWITEM.

## Ficha
|              |               |
|--------------|---------------|
| **Function** | **NEWSUMMON** |
| **Type**     | World         |
| **Access**   | Read/Write    |
| **Sphere X** | Yes           |

## Syntax
`SERV.NEWSUMMON=<character_defname>,<duration>`

## Example
`SERV.NEWSUMMON=c_ogre,15`
This will summon an ogre for 15 seconds on your position. If the duration is not provided, a default timer will be used based on the magery skill.

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Functions](./CategoryFunctions.md)