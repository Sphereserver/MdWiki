\_\_FORCETOC\_\_ Instead of setting the MORE1 property of a spawn to a
single [character](Characters "wikilink") defname, a spawn group can be
used instead so that a random character is spawned. A spawn group
contains a set of character defnames, with optional weights to affect
their chances of spawning.

## Syntax

The syntax for defining a spawn group is:

`[SPAWN `*`defname`*`]`  
`ID=`*`character_defname_1`*` `*`weight`*  
`ID=`*`character_defname_2`*` `*`weight`*  
`ID=`*`character_defname_3`*` `*`weight`*  
*`etc..`*  

The weight parameter can be used to make a defname more likely to be
selected than the other defnames in the group. With a weight of 10 for
example, a defname would be 10 times more likely to be selected.

## Properties

The following properties are available when defining a spawn group:

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [CALCMEMBERINDEX](CALCMEMBERINDEX "wikilink") | R | Selects a defname from the spawn group at random, and returns its zero-based index. |
| [DEFNAME](DEFNAME "wikilink") | W | Sets the spawn group's defname. |
| [ID](ID "wikilink") *defname* *weight* | W | Adds a defname to the spawn group with the specified weight. |
| [RESOURCES](RESOURCES "wikilink") | R | Gets a list of defnames contained in the spawn group. |
| [RESOURCES](RESOURCES "wikilink").COUNT | R | Gets the number of defnames in the spawn group. |
| [RESOURCES](RESOURCES "wikilink")*.n*.KEY | R | Gets the *nth* defname in the spawn group. *(1-based)* |
| [RESOURCES](RESOURCES "wikilink")*.n*.VAL | R | Gets the weight of the *nth* defname in the spawn group. *(1-based)* |

## Examples

<spherescript> // // Undead spawn from default script pack. // \[SPAWN
08001\] DEFNAME=SPAWN_Undead_Weak ID=c_spectre,2 ID=c_skeleton_w_axe
ID=c_skeleton_w_sword ID=c_skeleton,5 ID=c_zombie,10 </spherescript>

<spherescript> // // Lists the characters of a spawn in the console, and
picks one at random. // Usage: DescribeSpawn <spawn_defname> //
\[FUNCTION describespawn\] // validate args IF !(\<SERV.SPAWN.<ARGS>\>)

`   SERV.LOG Spawn '`<ARGS>`' does not exist.`  
`   RETURN`

ELSEIF !(\<SERV.SPAWN.<ARGS>.RESOURCES.COUNT\>)

`   SERV.LOG Spawn '`<ARGS>`' has no contents.`  
`   RETURN`

ENDIF

// list characters SERV.LOG Spawn '\<SERV.SPAWN.<ARGS>.DEFNAME\>',
\<SERV.SPAWN.<ARGS>.RESOURCES.COUNT\> characters) FOR 1
\<SERV.SPAWN.<ARGS>.RESOURCES.COUNT\>

`   SERV.LOG Character <dLOCAL._FOR>: <dSERV.SPAWN.`<ARGS>`.RESOURCES.<LOCAL._FOR>.VAL>x <SERV.SPAWN.`<ARGS>`.RESOURCES.<LOCAL._FOR>.KEY>`

ENDFOR

// pick character (obeying weights) LOCAL.INDEX = \<EVAL
\<SERV.SPAWN.<ARGS>.CALCMEMBERINDEX\> + 1\> SERV.LOG Picked
'\<SERV.SPAWN.<ARGS>.RESOURCES.\<LOCAL.INDEX\>.KEY\>'. RETURN
</spherescript>

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Definitions](Category:_Definitions "wikilink")
