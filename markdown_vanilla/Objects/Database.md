\_\_FORCETOC\_\_ Using the [DB](DB "wikilink") object reference, scripts
can interact with an external MySQL database. The following table
details the various properties of the database object in SphereServer:

**Note:** Before the DB object can be used, MySQL must be enabled along
with the database host details, in Sphere.ini.

## Properties and Functions

Here is a list of all database properties and functions. If a function
is marked as readable then it can return a value when used as <KEY>.
Click on the name for more detailed information such as usage and
examples. If an attempt is made to access a property that does not exist
on the item, the property from the [ITEMDEF](ITEMDEF "wikilink") will be
accessed instead.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [AEXECUTE](AEXECUTE "wikilink") *function, command* | R | Executes an SQL command in a background thread, calling *function* when complete. Returns 1 if the command is successfully queued. |
| [AQUERY](AQUERY "wikilink") *function, command* | R | Executes an SQL command in a background thread, calling *function* when complete. Returns 1 if the command is successfully queued. |
| [CLOSE](CLOSE "wikilink") | W | Closes the connection to the database. |
| [CONNECT](CONNECT "wikilink") | W | Opens a connection to the database, using the settings from Sphere.ini. |
| [CONNECTED](CONNECTED "wikilink") | R | Returns 1 if the database is connected. |
| [ESCAPEDATA](ESCAPEDATA "wikilink") *text* | R | Returns *text* as an escaped SQL string. |
| [EXECUTE](EXECUTE "wikilink") *command* | W | Exectutes an SQL command that doesn't return any result. |
| [QUERY](QUERY "wikilink") *command* | W | Executes an SQL command that returns results. |
| [ROW](ROW "wikilink").NUMCOLS | R | Returns the number of columns returned in the last query. |
| [ROW](ROW "wikilink").NUMROWS | R | Returns the number of rows returned in the last query. |
| [ROW](ROW "wikilink")*.n.col_index* | R | Returns the value of the column at index *col_index* in the nth row. (zero-based) |
| [ROW](ROW "wikilink")*.n.col_name* | R | Returns the value of the column named *col_name* in the nth row. (zero-based) |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Objects](Category:_Objects "wikilink")
