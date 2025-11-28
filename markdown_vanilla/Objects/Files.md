\_\_FORCETOC\_\_ Using the [FILE](FILE "wikilink") object reference,
scripts can interact with text files. The following table details the
various properties of the file object in SphereServer:

**Note:** Before the FILE object can be used, the OF_FileCommands flag
must be set in Sphere.ini's OptionFlags setting.

## Properties and Functions

Here is a list of all file properties and functions. If a function is
marked as readable then it can return a value when used as <KEY>. Click
on the name for more detailed information such as usage and examples.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [CLOSE](CLOSE "wikilink") | W | Closes the currently open file. |
| [DELETEFILE](DELETEFILE "wikilink") *file_name* | W | Deletes *file_name*. |
| [FILEEXIST](FILEEXIST "wikilink") *file_name* | R | Returns 1 if *file_name* exists. |
| [FILELINES](FILELINES "wikilink") *file_name* | R | Returns the total number of lines in *file_name*. |
| [FILEPATH](FILEPATH "wikilink") | R | Returns the name of the currently open file. |
| [FLUSH](FLUSH "wikilink") | W | Forces all buffered output to be written to the file, |
| [INUSE](INUSE "wikilink") | R | Returns 1 if a file is currently open. |
| [ISEOF](ISEOF "wikilink") | R | Returns 1 if there are no more lines left to read from the file. |
| [LENGTH](LENGTH "wikilink") | R | Returns the total length of the currently open file, in bytes. |
| [MODE](MODE "wikilink").APPEND | RW | Gets or sets whether or not the file will be appended to when opened. Cannot be set after the file has been opened. |
| [MODE](MODE "wikilink").CREATE | RW | Gets or sets whether or not the file will be created when opened. Cannot be set after the file has been opened. |
| [MODE](MODE "wikilink").READLFLAG | RW | Gets or sets whether or not the file will be opened for reading from. Cannot be set after the file has been opened. |
| [MODE](MODE "wikilink").WRITEFLAG | RW | Gets or sets whether or not the file will be opened for writing to. Cannot be set after the file has been opened. |
| [MODE](MODE "wikilink").SETDEFAULT | W | Sets the mode to the default setting. Cannot be set after the file has been opened. |
| [OPEN](OPEN "wikilink") *file_name* | R | Opens a file, and returns 1 if the attempt was successful, using the set [MODE](MODE "wikilink") flags. |
| [POSITION](POSITION "wikilink") | R | Gets the current position in the currently open file, in bytes. |
| [READBYTE](READBYTE "wikilink") | R | Reads the next byte from the currently open file. |
| [READCHAR](READCHAR "wikilink") | R | Reads the next character from the currently open file. |
| [READLINE](READLINE "wikilink") *n* | R | Reads the nth line from the currently open file (1-based). 0 Reads the last line. |
| [SEEK](SEEK "wikilink") *position* | R | Changes the current position in the currently open file to *position*. Accepts "BEGIN" for the start of the file and "END" for the end of the file. Returns the new position in the file. |
| [WRITE](WRITE "wikilink") *text* | W | Writes *text* to the currently open file. |
| [WRITECHR](WRITECHR "wikilink") *ascii_value* | W | Writes a single character to the currently open file. |
| [WRITELINE](WRITELINE "wikilink") *text* | W | Writes *text* to the currently open file, with newline character(s) on the end. |

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Objects](Category:_Objects "wikilink")
