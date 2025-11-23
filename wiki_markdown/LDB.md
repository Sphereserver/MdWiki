```{=mediawiki}
{{Languages|LDB}}
```
An LDB object is an SQLite database instance working with a disk-based database file.

## Functions

  ------------------------------------------------------------------ ------------------------------------------------------------------------------------------------
  **Name**                                                           **Description**
  [OPEN](./OPEN.md) *database_file*                                  Opens a connection to the specified SQLite database file.
  [CLOSE](./CLOSE.md)                                                Closes the connection to the database.
  [IMPORTDB](./IMPORTDB.md) *database_file*                          Loads a database file into the LDB object.
  [EXPORTDB](./EXPORTDB.md) *database_file*                          Saves the LDB object's database to a file.
  [QUERY](./QUERY.md) *sql_query*                                    Executes an SQL query on the database.
  [LASTROWID](./LASTROWID.md)                                        Returns the ROWID of the last row inserted into the database.
  [NUMCHANGES](./NUMCHANGES.md)                                      Returns the number of database rows that were changed, inserted, or deleted by the most recent completed SQL statement.
  [ERRORCODE](./ERRORCODE.md)                                        Returns the numeric result code of the most recent failed SQLite API call.
  [ERRORMESSAGE](./ERRORMESSAGE.md)                                  Returns the English-language text of the most recent failed SQLite API call.
  [READONLY](./READONLY.md)                                          Returns 1 if the database connection is in read-only mode, 0 otherwise.
  [TABLEEXISTS](./TABLEEXISTS.md) *table_name*                       Returns 1 if the specified table exists in the database, 0 otherwise.
  [EXEC](./EXEC.md) *sql_command*                                    Executes one or more SQL statements.
  ------------------------------------------------------------------ ------------------------------------------------------------------------------------------------

## Properties

  ------------------------------------------------------------------ ------------------------------------------------------------------------------------------------
  **Name**                                                           **Description**
  [FILENAME](./FILENAME.md)                                          Returns the filename of the database connected to. Returns an empty string if there isn't an open connection.
  ------------------------------------------------------------------ ------------------------------------------------------------------------------------------------

[Category: Reference Compendium](./_Reference_Compendium.md) [Category: Objects](./_Objects.md)