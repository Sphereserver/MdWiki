+-----------------------+-------------------+-----------------------+
| **Statement**         | **End Statement** | **Description**       |
+-----------------------+-------------------+-----------------------+
| [BEG                  | END               | Groups a set of lines |
| IN](BEGIN "wikilink") |                   | together, for use     |
|                       |                   | with                  |
|                       |                   | [DORAN                |
|                       |                   | D](DORAND "wikilink") |
|                       |                   | and                   |
|                       |                   | [DOSWITCH]            |
|                       |                   | (DOSWITCH "wikilink") |
|                       |                   | statements.           |
+-----------------------+-------------------+-----------------------+
| [DORAN                | ENDDO             | Executes a random     |
| D](DORAND "wikilink") |                   | line of code within   |
| *line_count*          |                   | the block.            |
+-----------------------+-------------------+-----------------------+
| [DOSWITCH]            | ENDDO             | Executes the          |
| (DOSWITCH "wikilink") |                   | specified line of     |
| *line_number*         |                   | code within the       |
|                       |                   | block.                |
+-----------------------+-------------------+-----------------------+
| [FOR](FOR "wikilink") | ENDFOR            | Loops through the     |
| *start end*           |                   | block of code         |
+-----------------------+-------------------+-----------------------+
| [FORCHARLAYER](FOR    | ENDFOR            | Loops through all     |
| CHARLAYER "wikilink") |                   | items that a          |
| *layer_id*            |                   | character has         |
|                       |                   | equipped on a         |
|                       |                   | specified layer.      |
+-----------------------+-------------------+-----------------------+
| [FORCHA               | ENDFOR            | Loops through all     |
| RMEMORYTYPE](FORCHARM |                   | memory items on a     |
| EMORYTYPE "wikilink") |                   | character that have   |
| *memory_flags*        |                   | one of the specified  |
|                       |                   | flags.                |
+-----------------------+-------------------+-----------------------+
| [FORCHARS]            | ENDFOR            | Loops through all     |
| (FORCHARS "wikilink") |                   | characters within     |
| *distance*            |                   | *distance* tiles.     |
+-----------------------+-------------------+-----------------------+
| [FORCLIENTS](F        | ENDFOR            | Loops through all     |
| ORCLIENTS "wikilink") |                   | connected clients     |
| *distance*            |                   | within *distance*     |
|                       |                   | tiles.                |
+-----------------------+-------------------+-----------------------+
| [FORCONT              | ENDFOR            | Loops through all     |
| ](FORCONT "wikilink") |                   | items inside a        |
| *container_uid,       |                   | container.            |
| max_subcontainers*    |                   |                       |
+-----------------------+-------------------+-----------------------+
| [FORCONTID](          | ENDFOR            | Loops through all     |
| FORCONTID "wikilink") |                   | items inside a        |
| *item_id,             |                   | container with a      |
| m                     |                   | specified             |
| ax_subcontainers*\'\' |                   | [BASEI                |
|                       |                   | D](BASEID "wikilink") |
+-----------------------+-------------------+-----------------------+
| [FORCONTTYPE](FO      | ENDFOR            | Loops through all     |
| RCONTTYPE "wikilink") |                   | items inside a        |
| *type,                |                   | container with a      |
| max_subcontainers*    |                   | specified             |
|                       |                   | [T                    |
|                       |                   | YPE](TYPE "wikilink") |
+-----------------------+-------------------+-----------------------+
| [FORINSTANCES](FOR    | ENDFOR            | Loops through all     |
| INSTANCES "wikilink") |                   | instances of          |
| *defname*             |                   | characters or items   |
|                       |                   | with the specified    |
|                       |                   | [BASEI                |
|                       |                   | D](BASEID "wikilink") |
+-----------------------+-------------------+-----------------------+
| [FORITEMS]            | ENDFOR            | Loops through all     |
| (FORITEMS "wikilink") |                   | items within          |
| *distance*            |                   | *distance* tiles.     |
+-----------------------+-------------------+-----------------------+
| [FOROBJS              | ENDFOR            | Loops through all     |
| ](FOROBJS "wikilink") |                   | items and players     |
| *distance*            |                   | within *distance*     |
|                       |                   | tiles.                |
+-----------------------+-------------------+-----------------------+
| [FORPLAYERS](F        | ENDFOR            | Loops through all     |
| ORPLAYERS "wikilink") |                   | players (online and   |
| *distance*            |                   | offline) within       |
|                       |                   | *distance* tiles.     |
+-----------------------+-------------------+-----------------------+
| [IF](IF "wikilink")   | ENDIF             | Executes the block of |
| *condition*\          |                   | code if *condition*   |
| [ELIF](IF "wikilink") |                   | is true.              |
| *condition*\          |                   |                       |
| [E                    |                   |                       |
| LSEIF](IF "wikilink") |                   |                       |
| *condition*           |                   |                       |
+-----------------------+-------------------+-----------------------+
| [WHI                  | ENDWHILE          | Loops through the     |
| LE](WHILE "wikilink") |                   | block of code whilst  |
| *condition*           |                   | *condition* is true.  |
+-----------------------+-------------------+-----------------------+
| \<local.\_for\>       |                   | Current Step of the   |
|                       |                   | Loop for the FOR      |
|                       |                   | statements. Note, not |
|                       |                   | all of the FOR        |
|                       |                   | statements use this   |
|                       |                   | concept\... for       |
|                       |                   | example, in a         |
|                       |                   | FORITEMS statement,   |
|                       |                   | the \<local.\_for\>   |
|                       |                   | counter will always   |
|                       |                   | be zero no matter how |
|                       |                   | many objects the      |
|                       |                   | statement loops over. |
+-----------------------+-------------------+-----------------------+
| \<local.\_while\>     |                   | Current Step of the   |
|                       |                   | Loop for the WHILE    |
|                       |                   | statement.            |
+-----------------------+-------------------+-----------------------+

[Category: Reference
Compendium](Category_Reference_Compendium.md) [Category:
Scripts](CategoryScripts.md)
