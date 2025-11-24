```{=mediawiki}
{{Languages|Error_Codes}}
```
\_\_FORCETOC\_\_

## Exit Codes {#exit_codes}

When Sphere closes, an \'exit code\' will normally be shown in the
console to describe why it is being shut down. In general, an exit code
less than 0 is considered to be an error code, and values above 0 are
normal shutdown codes. In most cases, a more descriptive error will be
shown in the console and/or log file to help better diagnose the reason
behind error codes.

The following table lists all of the current codes and their meanings.

+----------+---------------------------------------------------------------+
| **Code** | **Description**                                               |
+----------+---------------------------------------------------------------+
| -10      | Unexpected error occurred                                     |
+----------+---------------------------------------------------------------+
| -9       | Failed to bind server port                                    |
+----------+---------------------------------------------------------------+
| -8       | Failed to load world save(s)                                  |
+----------+---------------------------------------------------------------+
| -3       | Failed to load server settings (script, ini, mul files) *or*\ |
|          | did not write AGREE=1 in the sphere.ini                       |
+----------+---------------------------------------------------------------+
| -1       | Shutdown via commandline (/?, /T and /Q switches)             |
+----------+---------------------------------------------------------------+
| 1        | X in console *or*\                                            |
|          | SIGHUP signal, terminal closed (Linux Only)                   |
+----------+---------------------------------------------------------------+
| 2        | SHUTDOWN command                                              |
+----------+---------------------------------------------------------------+
| 4        | Service shutdown *(Windows Only)*                             |
+----------+---------------------------------------------------------------+
| 5        | Console window closed *(Windows Only)*                        |
+----------+---------------------------------------------------------------+
| 6        | SIGABRT signal, process aborted *(Linux Only)*                |
+----------+---------------------------------------------------------------+

## Garbage Collection {#garbage_collection}

The purpose of garbage collection is to validate all of the server
objects and free up unused UIDs. Garbage collection is initiated:

-   After the world save is loaded at startup.
-   Before a world save begins, if the
    [FORCEGARBAGECOLLECT](./FORCEGARBAGECOLLECT.md) setting is
    enabled in Sphere.ini.
-   After the [IMPORT](./IMPORT.md) or
    [RESTORE](./RESTORE.md) functions have been used on the
    [server](./Server.md) object.
-   When the \'G\' command is entered via the Sphere console
-   When the [GARBAGE](./GARBAGE.md) function is used on the
    [server](./Server.md) object.

When garbage collection encounters a problem with an object it may
attempt to automatically correct the error, otherwise the object will be
removed. When an object is removed by garbage collection there will
normally be an error shown in the console describing the item that was
removed along with the reason. The following table lists all of the
garbage collection codes along with their description:

  ---------- ------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----
  **Code**   **Message**                                                                     **Description**                                                                                                                                                                                                                                                                
  1102       Disconnected charr not acting as such                                           A character has been marked disconnected from the world, but it is not listed in the sector\'s disconnected character\'s list.                                                                                                                                                 \*
  1103       Ridden NPC not acting as such                                                   An NPC has the [statf_ridden](./FLAGS.md) flag set, but does not have its [ACTION](./ACTION.md) property set to 111.                                                                                                                                               
  1104       Ridden NPC without a mount item                                                 An NPC has the [statf_ridden](./FLAGS.md) flag set, but its [ACTARG1](./ACTARG1.md) property isn\'t set to the [UID](./UID.md) of an item whose [TYPE](./TYPE.md) property is set to [t_figurine](./TYPE.md) or [t_eq_horse](./TYPE.md).   
  1105       Ridden NPC with a mislinked mount item                                          An NPC has the [statf_ridden](./FLAGS.md) flag set, but its [ACTARG1](./ACTARG1.md) property isn\'t set to the [UID](./UID.md) of an item whose [MORE2](./MORE2.md) property matches the NPC\'s [UID](./UID.md).                                 
  1106       Disconnected NPC neither dead nor ridden                                        An NPC has been disconnected from the world, but does not have either one of the [statf_ridden](./FLAGS.md) or [statf_dead](./FLAGS.md) flags set.                                                                                                                 
  1107       In game char that is neither a player nor an NPC                                A character is not a player or an NPC.                                                                                                                                                                                                                                         \*
  1108       Char not on a valid position                                                    A character\'s [position](./P.md) is outside of the map boundaries.                                                                                                                                                                                                      
  1203       Ridden NPC not acting as such                                                   Same as 1103.                                                                                                                                                                                                                                                                  
  1204       Ridden NPC without a mount item                                                 Same as 1104.                                                                                                                                                                                                                                                                  
  1205       In game char that is neither a player nor an NPC                                Same as 1107.                                                                                                                                                                                                                                                                  
  2102       Item without ITEMDEF                                                            An item does not have an [ITEMDEF](./ITEMDEF.md) section.                                                                                                                                                                                                                \*
  2103       Item ITEMDEF with ID = 0                                                        An item\'s [ITEMDEF](./ITEMDEF.md) has an [ID](./ID.md) of zero.                                                                                                                                                                                                   \*
  2104       Disconnected item                                                               An item has been marked as disconnected from the world.                                                                                                                                                                                                                        \*
  2105       Item not on a valid position                                                    An item is not in a container and its [position](./P.md) is outside of the map boundaries.                                                                                                                                                                               
  2106       Item flagged as being in a container but it isn\'t                              An item is flagged as not being top level, but it does not have a container.                                                                                                                                                                                                   
  2202       Item flagged as equipped but it isn\'t                                          An item is flagged as being equipped, but its parent is not a character.                                                                                                                                                                                                       
  2205       Mislinked item                                                                  An item\'s [LINK](./LINK.md) property matches its [UID](./UID.md), or has been set to a [UID](./UID.md) that doesn\'t exist.                                                                                                                                 
  2206       Gm Robe / Deathshroud not on a char                                             A GM robe or death shroud ([ID](./ID.md) of 0204E or 0204F) is not equipped to a character.                                                                                                                                                                              
  2207       Deathshroud not on a dead char                                                  A death shroud ([ID](./ID.md) of 0204F) is equipped to a character without the [statf_dead](./FLAGS.md) flag set.                                                                                                                                                  
  2208       Gm Robe on a char without privilege                                             A GM robe ([ID](./ID.md) of 0204E) is equipped to a character whose [PLEVEL](./PLEVEL.md) is less than 2.                                                                                                                                                          
  2220       Trade window memory not equipped in the correct layer                           A [t_eq_trade window](./TYPE.md) item type is not equipped, has its [LAYER](./LAYER.md) property set to something other than [layer_none](./LAYER.md), or is equipped to an NPC.                                                                             
  2221       Client linger memory not equipped in the correct layer                          A [t_eq_client_linger](./TYPE.md) item type is not equipped, has its [LAYER](./LAYER.md) property set to something other than [layer_flag_clientlinger](./LAYER.md), or is equipped to an NPC.                                                               
  2222       Memory not equipped / not in the memory layer / without color                   A memory item ([ID](./ID.md) of 02007) is not equipped, or a non-memory item has had its [TYPE](./TYPE.md) set to [t_eq_memory_obj](./TYPE.md) after creation.                                                                                               
  2226       Mount memory not equipped in the correct layer                                  A [t_eq_horse](./TYPE.md) item type is not equipped, or has its [LAYER](./LAYER.md) property set to something other than [layer_horse](./LAYER.md).                                                                                                          
  2227       Hair/Beard item not equipped / not in a corpse / not in a vendor box            A [t_hair](./TYPE.md) or [t_beard](./TYPE.md) item type that isn\'t equipped, is either not in a container or its container has an [ID](./ID.md) other than 02006 or 02AF8.                                                                                  
  2228       Hair/Beard item not equipped / not in a corpse / not in a vendor box            A [t_hair](./TYPE.md) or [t_beard](./TYPE.md) item is equipped, but has its [LAYER](./LAYER.md) property set to something other than [layer_hair](./LAYER.md) or [layer_beard](./LAYER.md).                                                      
  2229       Game piece not in a game board                                                  A [t_game_piece](./TYPE.md) item has been found outside of a container.                                                                                                                                                                                                  
  2230       Item equipped in the trade window layer but it isn\'t a trade window            An equipped item has been found with its [LAYER](./LAYER.md) property set to [layer_none](./LAYER.md), but its [type](./TYPE.md) is not [t_eq_trade_window](./TYPE.md).                                                                                
  2231       Item equipped in the memory layer but it isn\'t a memory                        An equipped item has been found with its [LAYER](./LAYER.md) property set to [layer_special](./LAYER.md), but its [type](./TYPE.md) is not [t_eq_memory_obj](./TYPE.md) or [t_eq_script](./TYPE.md).                                             
  2233       Item equipped in the mount memory layer but it isn\'t a mount memory            An equipped item has been found with its [LAYER](./LAYER.md) property set to [layer_horse](./LAYER.md), but its [type](./TYPE.md) is not [t_eq_horse](./TYPE.md).                                                                                      
  2234       Item equipped in the client linger layer but it isn\'t a client linger memory   An equipped item has been found with its [LAYER](./LAYER.md) property set to [layer_flag_clientlinger](./LAYER.md), but its [type](./TYPE.md) is not [t_eq_client_linger](./TYPE.md).                                                                  
  2235       Item equipped in the murder memory layer but it isn\'t a murder memory          An equipped item has been found with its [LAYER](./LAYER.md) property set to [layer_flag_murders](./LAYER.md), but the character is an NPC or the player has its [KILLS](./KILLS.md) property set to 0.                                                      
  2236       Item flagged as decay but without timer set                                     A top-level item has the [attr_decay](./ATTR.md) flag set, but its [TIMER](./TIMER.md) property has not been set.                                                                                                                                                  
  3101       Object is totaly lost, no parent exists                                         An object has no parent.                                                                                                                                                                                                                                                       \*
  3102       Object was deleted or UID is incorrect                                          An object does not have a valid [UID](./UID.md).                                                                                                                                                                                                                         \*
  3201       Object not correctly loaded by server (UID conflict)                            More than one object has the same [UID](./UID.md) value.                                                                                                                                                                                                                 \*
  4222       Memory not equipped / not in the memory layer / without color                   A memory item is not flagged as equipped, has its [LAYER](./LAYER.md) property set to something other than [layer_special](./LAYER.md), or has its [COLOR](./COLOR.md) property set to 0.                                                                    
  4223       Memory not on a char                                                            A memory item is flagged as equipped, but it\'s [parent](./CONT.md) is not a character.                                                                                                                                                                                  
  4224       Stone/Guild memory mislinked                                                    A memory item\'s [COLOR](./COLOR.md) property has one of the [memory_guild](./COLOR.md) or [memory_town](./COLOR.md) flags set, but the [LINK](./LINK.md) property is not set to the [UID](./UID.md) of a guild or town stone.                   
  4225       Stone/Guild memory linked to the wrong stone                                    A memory item\'s [COLOR](./COLOR.md) property has one of the [memory_guild](./COLOR.md) or [memory_town](./COLOR.md) flags set, but the character the memory is equipped to is not a member of the guild or town.                                            
  7101       Object\'s UID does not match up with server\'s UID table.                       An object does not have the expected [UID](./UID.md) value.                                                                                                                                                                                                              \*
  7102       Object does not exist.                                                          An object does not exist.                                                                                                                                                                                                                                                      \*
  FFFF       Bad memory allocation                                                           An exception was thrown whilst checking the object\'s validity.                                                                                                                                                                                                                \*
  ---------- ------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----

**Note**: *Garbage collection codes marked with \* generally indicate a
serious error within an object\'s internal state and should not normally
be seen. If you are experiencing and are able to reliably reproduce any
such errors then please report the details to the [bug
tracker](http://tracker.sphere.torfo.org/bugs/main_page.php).*
