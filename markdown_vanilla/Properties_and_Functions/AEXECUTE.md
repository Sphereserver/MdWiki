

## Description

This function will queue up a query and run it asynchronously in a background thread (rather than the script waiting for it to completelike the [EXECUTE](EXECUTE "wikilink") function). Once the query has been executed, a specified callback function will run.

***Note 1***: An open database connection is required for this function to work correctly. See the [CONNECT](CONNECT "wikilink") function for information regarding the opening of a database connection.

***Note 2***: The [AEXECUTE](AEXECUTE "wikilink") and [EXECUTE](EXECUTE "wikilink") functions are intended to run SQL commands that do not return any results (such as DELETE or UPDATE). For commands that return results (that you want to then read back) see the [AQUERY](AQUERY "wikilink") and [QUERY](QUERY "wikilink") functions.

Valid for the following objects:

- [Database](Database "wikilink")

## Syntax

`AEXECUTE `*`function`*`, `*`command`*

| **Argument** | **Type** | **Description** |  |
| --- | --- | --- | --- |
| *function* | string | A script function to call when the command has been executed. <table> **Argument** | **Description** |
| *ARGN1* | The type of command (0 = [AEXECUTE](AEXECUTE), 1 = [AQUERY](AQUERY)) |  |  |
| *ARGN2* | 0 = Command failed, 1 = Command succeeded. |  |  |
| *ARGS* | The command that was executed. |  |  |</td>
</tr> <tr> <td><p>*command*</p></td> <td><p>string</p></td> <td><p>The SQL command to execute.</p></td> </tr> </tbody> </table>

## Return Values

This function returns one of two values when executed. See the table below for the meanings of the return values:

|                  |                                           |
|------------------|-------------------------------------------|
| **Return Value** | **Description**                           |
| 0                | Command has not been successfully queued. |
| 1                | Command has been successfully queued.     |

## Examples

```
 // // Queues up an SQL command. // \[FUNCTION f_execute\]
```
`SERV.LOG` Deleting all rows from table 'tbl_name'. IF (\<DB.AEXECUTEf_execute_callback, DELETE FROM tbl_name\> == 0)

` `SERV.LOG` Failed to queue command.`

`ELSE`

` `SERV.LOG` Command queued.`

```
ENDIF RETURN
```

```
// // This function will be called when the query has been executed. //
```
\[FUNCTION f_execute_callback\] IF (<ARGN2> == 0)

` `SERV.LOG` The command failed to execute. (`<ARGS>`)`

`ELSE`

` `SERV.LOG` The command succeeded. (`<ARGS>`)`

```
ENDIF RETURN
```

[Category: Reference Compendium](Category:_Reference_Compendium "wikilink") [Category: Properties and Functions](Category:_Properties_and_Functions "wikilink")
