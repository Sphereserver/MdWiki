```{=mediawiki}
{{Languages|MDB}}
```
An MDB object is an SQLite database instance working like [LDB](./LDB.md), with the fundamental difference that MDB works with a temporary, in-memory database (this means that all the data is lost when you close the server).

Use it if you have small databases where you query from very frequently, since accessing a table from a db file is much slower than doing that from an in-memory db.

OPEN and CLOSE methods don't work with MDB.

## Functions

  ------------------------------------------------------------------ ------------------------------------------------------------------------------------------------
  **Name**                                                           **Description**
  [IMPORTDB](./IMPORTDB.md) *database_file*                          Loads a database file into the MDB object.
  [EXPORTDB](./EXPORTDB.md) *database_file*                          Saves the MDB object's database to a file.
  [QUERY](./QUERY.md) *sql_query*                                    Executes an SQL query on the database.
  [LASTROWID](./LASTROWID.md)                                        Returns the ROWID of the last row inserted into the database.
  [NUMCHANGES](./NUMCHANGES.md)                                      Returns the number of database rows that were changed, inserted, or deleted by the most recent completed SQL statement.
  [ERRORCODE](./ERRORCODE.md)                                        Returns the numeric result code of the most recent failed SQLite API call.
  [ERRORMESSAGE](./ERRORMESSAGE.md)                                  Returns the English-language text of the most recent failed SQLite API call.
  [READONLY](./READONLY.md)                                          Returns 1 if the database connection is in read-only mode, 0 otherwise.
  [TABLEEXISTS](./TABLEEXISTS.md) *table_name*                       Returns 1 if the specified table exists in the database, 0 otherwise.
  [EXEC](./EXEC.md) *sql_command*                                    Executes one or more SQL statements.
  ------------------------------------------------------------------ ------------------------------------------------------------------------------------------------

[Category: Reference Compendium](./_Reference_Compendium.md) [Category: Objects](./_Objects.md)