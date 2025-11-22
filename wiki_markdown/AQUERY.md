\_\_FORCETOC\_\_

## Description

This function will queue up a query and run it asynchronously in a
background thread (rather than the script waiting for it to complete
like the [QUERY](QUERY "wikilink") function). Once the query has been
executed, a specified callback function will run.

Unlike the [QUERY](QUERY "wikilink") function, results are not stored in
the [ROW](ROW "wikilink") object. Instead they are passed in to the
callback function as [LOCALs](LOCAL "wikilink"). The following table
shows the differences between accessing the results for the two
functions:

  ----------------------------------------------- -------------------------------
  [QUERY](QUERY "wikilink")                       [AQUERY](AQUERY "wikilink")
  [ROW](ROW "wikilink").NUMROWS                   LOCAL.NUMROWS
  [ROW](ROW "wikilink").NUMCOLS                   LOCAL.NUMCOLS
  [ROW](ROW "wikilink").*row_index*.*col_index*   LOCAL.*row_index*.*col_index*
  [ROW](ROW "wikilink").*row_index*.*col_name*    LOCAL.*row_index*.*col_name*
  ----------------------------------------------- -------------------------------

***Note 1***: An open database connection is required for this function
to work correctly. See the [CONNECT](CONNECT "wikilink") function for
information regarding the opening of a database connection.

***Note 2***: The [AQUERY](AQUERY "wikilink") and
[QUERY](QUERY "wikilink") functions are intended to run SQL commands
that return results (such as SELECT). For commands that do not return
results consider using the [AEXECUTE](AEXECUTE "wikilink") and
[EXECUTE](EXECUTE "wikilink") functions.

Valid for the following objects:

-   [Database](Database "wikilink")

## Syntax

`AQUERY `*`function`*`, `*`command`*

+--------------+----------+------------------------------------------+
| **Argument** | **Type** | **Description**                          |
+--------------+----------+------------------------------------------+
| *function*   | string   | A script function to call when the       |
|              |          | command has been executed.               |
|              |          |                                          |
|              |          |   -------------- ------------            |
|              |          | ---------------------------------------- |
|              |          | ---------------------------------------- |
|              |          |   **Argument**   **Description**         |
|              |          |   *ARGN1*        The type o              |
|              |          | f command (0 = [AEXECUTE](AEXECUTE "wiki |
|              |          | link"), 1 = [AQUERY](AQUERY "wikilink")) |
|              |          |   *ARGN2*        0                       |
|              |          | = Command failed, 1 = Command succeeded. |
|              |          |   *ARGS                                  |
|              |          | *         The command that was executed. |
|              |          |   -------------- ------------            |
|              |          | ---------------------------------------- |
|              |          | ---------------------------------------- |
+--------------+----------+------------------------------------------+
| *command*    | string   | The SQL command to execute.              |
+--------------+----------+------------------------------------------+

## Return Values {#return_values}

This function returns one of two values when executed. See the table
below for the meanings of the return values:

  ------------------ -------------------------------------------
  **Return Value**   **Description**
  0                  Command has not been successfully queued.
  1                  Command has been successfully queued.
  ------------------ -------------------------------------------

## Examples

`<spherescript>`{=html} // // Queues an SQL query. // \[FUNCTION
f_aquery\] SERV.LOG Selecting some values in the background. IF
(\<DB.AQUERY f_aquery_callback, SELECT 10 AS test1, 20 AS test2, 30 AS
test3\> == 0)

` SERV.LOG Failed to queue command.`

ELSE

` SERV.LOG Command queued.`

ENDIF RETURN

// // This function will be called when the query has been executed. //
\[FUNCTION f_aquery_callback\] IF (`<ARGN2>`{=html} == 0)

` SERV.LOG The command failed to execute. (``<ARGS>`{=html}`)`

ELSE

` SERV.LOG The command succeeded, <dLOCAL.NUMROWS> row(s) of data returned. (``<ARGS>`{=html}`)`\
` FOR 0 <EVAL <LOCAL.NUMROWS> - 1>`\
`   SERV.LOG #<EVAL <LOCAL._FOR> + 1>. <LOCAL.<dLOCAL._FOR>.test1>, <LOCAL.<dLOCAL._FOR>.test2>, <LOCAL.<dLOCAL._FOR>.test3>`\
` ENDFOR`

ENDIF RETURN `</spherescript>`{=html}

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Properties and Functions](Category:_Properties_and_Functions "wikilink")
