## References

The following table lists all object references that are available from
any script.

  ------------------------------------ ---------------- ----------------------------------------------------------------------------------------------------------------------------------
  **Name**                             **Read/Write**   **Description**
  [DB](DB "wikilink")                  R                Gets the server\'s [database](Database "wikilink") object.
  [FILE](FILE "wikilink")              R                Gets the server\'s [file](Files "wikilink") object.
  [I](I "wikilink")                    R                Gets the current object.
  [LIST](LIST "wikilink")              R                Gets the server\'s list object.
  [NEW](NEW "wikilink")                RW               Gets or sets the last [character](Characters "wikilink") or [item](Items "wikilink") created on the server.
  [OBJ](OBJ "wikilink")                RW               Gets or sets a reference to a [character](Characters "wikilink") or [item](Items "wikilink")
  [SRC](SRC "wikilink")                R                Gets the source [character](Characters "wikilink") of an event.
  [UID](UID "wikilink").*object_uid*   R                Gets a reference to the [character](Characters "wikilink") or [item](Items "wikilink") with the specified [UID](UID "wikilink").
  ------------------------------------ ---------------- ----------------------------------------------------------------------------------------------------------------------------------

## Properties and Functions {#properties_and_functions}

The following table lists all properties and functions that are
available from any script.

+-------------------------+----------------+-------------------------+
| **Name**                | **Read/Write** | **Description**         |
+-------------------------+----------------+-------------------------+
| [ASC](ASC "wikilink")   | R              | Converts *text* into a  |
| *text*                  |                | series of ASCII values. |
+-------------------------+----------------+-------------------------+
| [ASC                    | R              | Converts *text* into a  |
| PAD](ASCPAD "wikilink") |                | series of ASCII values, |
| *size,text*             |                | padded with 0s untill   |
|                         |                | *size* is reached. Will |
|                         |                | also truncate the       |
|                         |                | *text* if longer then   |
|                         |                | *size*                  |
+-------------------------+----------------+-------------------------+
| [BETWE                  | R              | Returns the value       |
| EN](BETWEEN "wikilink") |                | that\'s                 |
| *min, max, numerator,   |                | *numerator/denominator* |
| denominator*            |                | between *min* and *max* |
+-------------------------+----------------+-------------------------+
| [BETWEEN                | R              | Returns the value       |
| 2](BETWEEN2 "wikilink") |                | that\'s                 |
| *min, max, numerator,   |                | *numerator/denominator* |
| denominator*            |                | between *max* and *min* |
+-------------------------+----------------+-------------------------+
| [CHR](CHR "wikilink")   | R              | Returns the character   |
| *ascii_code*            |                | represented by the      |
|                         |                | given ASCII code.       |
+-------------------------+----------------+-------------------------+
| [CLEARVARS              | W              | Removes all server VARs |
| ](CLEARVARS "wikilink") |                | whose name start with   |
| *prefix*                |                | *prefix*.               |
+-------------------------+----------------+-------------------------+
| [CLR                    | R              | Returns the value of    |
| BIT](CLRBIT "wikilink") |                | *value* with *bit* not  |
| *value, bit*            |                | set.                    |
+-------------------------+----------------+-------------------------+
| [D](D "wikilink"        | R              | Forces a property or    |
| )*property_or_function* |                | function to return a    |
|                         |                | decimal value.          |
+-------------------------+----------------+-------------------------+
| [DEFMSG](DE             | W              | Sets the value of a     |
| FMSG "wikilink")*.name* |                | DEFMESSAGE. (see        |
|                         |                | sphere_msgs.scp)        |
+-------------------------+----------------+-------------------------+
| [EXPLO                  | R              | Splits *text* by the    |
| DE](EXPLODE "wikilink") |                | given separator         |
| *separators*, *text*    |                | characters.             |
+-------------------------+----------------+-------------------------+
| [EVAL](EVAL "wikilink") | R              | Evaluates an expression |
| *expression*            |                | and returns the result  |
|                         |                | as an integer.          |
+-------------------------+----------------+-------------------------+
| [F                      | R              | \| Evaluates an         |
| EVAL](FEVAL "wikilink") |                | expression and returns  |
| *expression*            |                | the result as an        |
|                         |                | integer, supports       |
|                         |                | floating point values.  |
+-------------------------+----------------+-------------------------+
| [F                      | R              | \| Evaluates an         |
| HVAL](FHVAL "wikilink") |                | expression and returns  |
| *expression*            |                | the result as a         |
|                         |                | hexadecimal value,      |
|                         |                | supports floating point |
|                         |                | values.                 |
+-------------------------+----------------+-------------------------+
| [FLOATVA                | R              | Evaluates an expression |
| L](FLOATVAL "wikilink") |                | and returns the result  |
| *expression*            |                | as a floating point     |
|                         |                | value.                  |
+-------------------------+----------------+-------------------------+
| [FVAL](FVAL "wikilink") | R              | Evaluates an expression |
| *expression*            |                | and formats the result  |
|                         |                | with a single decimal   |
|                         |                | point. (\"1000\"        |
|                         |                | becomes \"100.0\")      |
+-------------------------+----------------+-------------------------+
| *ref*.[GETREFTYPE]      | R              | Returns a code          |
| (GETREFTYPE "wikilink") |                | representing what type  |
|                         |                | of object *ref* is.     |
+-------------------------+----------------+-------------------------+
| [HVAL](HVAL "wikilink") | R              | Evaluates an expression |
| *expression*            |                | and returns the result  |
|                         |                | as a hexadecimal value. |
+-------------------------+----------------+-------------------------+
| [I                      | R              | Returns non-zero if     |
| SBIT](ISBIT "wikilink") |                | *bit* is set in         |
| *value, bit*            |                | *value*.                |
+-------------------------+----------------+-------------------------+
| [ISEMP                  | R              | Returns 1 if *value* is |
| TY](ISEMPTY "wikilink") |                | empty/blank text.       |
| *value*                 |                |                         |
+-------------------------+----------------+-------------------------+
| [I                      | R              | Returns 1 if *value* is |
| SNUM](ISNUM "wikilink") |                | a numeric value.        |
| *value*                 |                |                         |
+-------------------------+----------------+-------------------------+
| [LISTC                  | R              | Returns the alternating |
| OL](LISTCOL "wikilink") |                | colour in webpage       |
|                         |                | tables.                 |
+-------------------------+----------------+-------------------------+
| [MD5HA                  | R              | Returns an MD5 hash for |
| SH](MD5HASH "wikilink") |                | *text*.                 |
| *text*                  |                |                         |
+-------------------------+----------------+-------------------------+
| [MUL                    | R              | Returns (*num* \*       |
| DIV](MULDIV "wikilink") |                | *mul*) / *div*.         |
| *num, mul, div*         |                |                         |
+-------------------------+----------------+-------------------------+
| [NEWDU                  | W              | Clones the character or |
| PE](NEWDUPE "wikilink") |                | item with the specified |
| *object_uid*            |                | [UID](UID "wikilink").  |
+-------------------------+----------------+-------------------------+
| [NEWIT                  | W              | Creates a new item.     |
| EM](NEWITEM "wikilink") |                |                         |
| *item_defname, amount,  |                |                         |
| container, equip*       |                |                         |
+-------------------------+----------------+-------------------------+
| [NEW                    | W              | Creates a new           |
| NPC](NEWNPC "wikilink") |                | character.              |
| *character_defname*     |                |                         |
+-------------------------+----------------+-------------------------+
| [QVAL](QVAL "wikilink") | R              | Evaluates an expression |
| *expression*?           |                | and returns             |
| *va                     |                | *value_true* if the     |
| lue_true*:*value_false* |                | result is true,         |
|                         |                | otherwise returns       |
|                         |                | *value_false*. There is |
|                         |                | another variant of QVAL |
|                         |                | in the [Intrinsic       |
|                         |                | Functions](Intrinsi     |
|                         |                | c_Functions "wikilink") |
|                         |                | category.               |
+-------------------------+----------------+-------------------------+
| [R](R "wikilink")*x*    | R              | Returns a random number |
|                         |                | between 0 and *x - 1*.  |
+-------------------------+----------------+-------------------------+
| [R](R "wikilink")*x, y* | R              | Returns a random number |
|                         |                | between *x* and *y*.    |
+-------------------------+----------------+-------------------------+
| [SET                    | R              | Returns the value of    |
| BIT](SETBIT "wikilink") |                | *value* with *bit* set. |
| *value, bit*            |                |                         |
+-------------------------+----------------+-------------------------+
| [SHOW](SHOW "wikilink") | W              | Displays the returned   |
| *property_or_function*  |                | value from a property   |
|                         |                | or function to SRC.     |
+-------------------------+----------------+-------------------------+
| [STR                    | R              | Returns the first word  |
| ARG](STRARG "wikilink") |                | from *text*.            |
| *text*                  |                |                         |
+-------------------------+----------------+-------------------------+
| [STR                    | R              | Removes the first word  |
| EAT](STREAT "wikilink") |                | from *text* and returns |
| *text*                  |                | the remaining text.     |
+-------------------------+----------------+-------------------------+
| [STR                    | R              | Returns the position of |
| POS](STRPOS "wikilink") |                | a *character* within    |
| *position character     |                | the *text*, starting    |
| text*                   |                | from *position*.        |
+-------------------------+----------------+-------------------------+
| [STRREGEXNEW](          | R              | Returns 1 if *text*     |
| STRREGEXNEW "wikilink") |                | matches a regular       |
| *pattern, text*         |                | expression *pattern*.   |
+-------------------------+----------------+-------------------------+
| [STRREVERSE]            | R              | Returns *text*, after   |
| (STRREVERSE "wikilink") |                | reversing its           |
| *text*                  |                | characters.             |
+-------------------------+----------------+-------------------------+
| [STR                    | R              | Extracts *count*        |
| SUB](STRSUB "wikilink") |                | characters from *text*, |
| *position, count, text* |                | starting from           |
|                         |                | *position*.             |
+-------------------------+----------------+-------------------------+
| [STRTOLOWER]            | R              | Returns *text* in       |
| (STRTOLOWER "wikilink") |                | lowercase.              |
| *text*                  |                |                         |
+-------------------------+----------------+-------------------------+
| [STRTOUPPER]            | R              | Returns *text* in       |
| (STRTOUPPER "wikilink") |                | uppercase.              |
| *text*                  |                |                         |
+-------------------------+----------------+-------------------------+
| [STRTR                  | R              | Removes whitespace      |
| IM](STRTRIM "wikilink") |                | (i.e. spaces, tabs)     |
| *text*                  |                | from the start and end  |
|                         |                | of *text*.              |
+-------------------------+----------------+-------------------------+
| [SYS                    | R              | Executes a system       |
| CMD](SYSCMD "wikilink") |                | command on the server   |
| *command, arg1,         |                | and waits for it to     |
| arg2\...*               |                | complete.\              |
|                         |                | **Note:** Requires      |
|                         |                | OF_FileCommands to be   |
|                         |                | enabled in Sphere.ini   |
+-------------------------+----------------+-------------------------+
| [SYSSPAW                | R              | Executes a system       |
| N](SYSSPAWN "wikilink") |                | command on the server   |
| *command, arg1,         |                | and does not wait for   |
| arg2\...*               |                | it to complete.\        |
|                         |                | **Note:** Requires      |
|                         |                | OF_FileCommands to be   |
|                         |                | enabled in Sphere.ini   |
+-------------------------+----------------+-------------------------+
| [UVAL](UVAL "wikilink") | R              | Evaluates an expression |
| *expression*            |                | and returns the result  |
|                         |                | as an unsigned integer. |
+-------------------------+----------------+-------------------------+
| [VAR]                   | RW             | Gets or sets the value  |
| (VAR "wikilink")*.name* |                | of a VAR.               |
+-------------------------+----------------+-------------------------+

[Category: Reference
Compendium](Category_Reference_Compendium.md) [Category:
Scripts](CategoryScripts.md)
