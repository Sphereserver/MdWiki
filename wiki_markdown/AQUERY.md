\_\_FORCETOC\_\_

## Description

This function will queue up a query and run it asynchronously in a
background thread (rather than the script waiting for it to complete
like the [QUERY](./QUERY.md) function). Once the query has been
executed, a specified callback function will run.

Unlike the [QUERY](./QUERY.md) function, results are not stored in
the [ROW](./ROW.md) object. Instead they are passed in to the
callback function as [LOCALs](./LOCAL.md). The following table
shows the differences between accessing the results for the two
functions:

|  |  |
|----|----|
| [QUERY](./QUERY.md) | [AQUERY](./AQUERY.md) |
| [ROW](./ROW.md).NUMROWS | LOCAL.NUMROWS |
| [ROW](./ROW.md).NUMCOLS | LOCAL.NUMCOLS |
| [ROW](./ROW.md).*row_index*.*col_index* | LOCAL.*row_index*.*col_index* |
| [ROW](./ROW.md).*row_index*.*col_name* | LOCAL.*row_index*.*col_name* |

***Note 1***: An open database connection is required for this function
to work correctly. See the [CONNECT](./CONNECT.md) function for
information regarding the opening of a database connection.

***Note 2***: The [AQUERY](./AQUERY.md) and
[QUERY](./QUERY.md) functions are intended to run SQL commands
that return results (such as SELECT). For commands that do not return
results consider using the [AEXECUTE](./AEXECUTE.md) and
[EXECUTE](./EXECUTE.md) functions.

Valid for the following objects:

- [Database](./Database.md)

## Syntax

`AQUERY `*`function`*`, `*`command`*

<table>
<tbody>
<tr>
<td><p><strong>Argument</strong></p></td>
<td><p><strong>Type</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p><em>function</em></p></td>
<td><p>string</p></td>
<td><p>A script function to call when the command has been executed.</p>
<table>
<tbody>
<tr>
<td><p><strong>Argument</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p><em>ARGN1</em></p></td>
<td><p>The type of command (0 = <a href="AEXECUTE"
title="wikilink">AEXECUTE</a>, 1 = <a href="AQUERY"
title="wikilink">AQUERY</a>)</p></td>
</tr>
<tr>
<td><p><em>ARGN2</em></p></td>
<td><p>0 = Command failed, 1 = Command succeeded.</p></td>
</tr>
<tr>
<td><p><em>ARGS</em></p></td>
<td><p>The command that was executed.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><em>command</em></p></td>
<td><p>string</p></td>
<td><p>The SQL command to execute.</p></td>
</tr>
</tbody>
</table>

## Return Values

This function returns one of two values when executed. See the table
below for the meanings of the return values:

|                  |                                           |
|------------------|-------------------------------------------|
| **Return Value** | **Description**                           |
| 0                | Command has not been successfully queued. |
| 1                | Command has been successfully queued.     |

## Examples

<spherescript> // // Queues an SQL query. // \[FUNCTION f_aquery\]
SERV.LOG Selecting some values in the background. IF (\<DB.AQUERY
f_aquery_callback, SELECT 10 AS test1, 20 AS test2, 30 AS test3\> == 0)

` SERV.LOG Failed to queue command.`

ELSE

` SERV.LOG Command queued.`

ENDIF RETURN

// // This function will be called when the query has been executed. //
\[FUNCTION f_aquery_callback\] IF (<ARGN2> == 0)

` SERV.LOG The command failed to execute. (`<ARGS>`)`

ELSE

` SERV.LOG The command succeeded, <dLOCAL.NUMROWS> row(s) of data returned. (`<ARGS>`)`  
` FOR 0 <EVAL <LOCAL.NUMROWS> - 1>`  
`   SERV.LOG #<EVAL <LOCAL._FOR> + 1>. <LOCAL.<dLOCAL._FOR>.test1>, <LOCAL.<dLOCAL._FOR>.test2>, <LOCAL.<dLOCAL._FOR>.test3>`  
` ENDFOR`

ENDIF RETURN </spherescript>

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Properties and Functions](./_Properties_and_Functions.md)
