## References

The following table lists all object references that are available from
any script.

|  |  |  |
|----|----|----|
| **Name** | **Read/Write** | **Description** |
| [DB](./DB.md) | R | Gets the server's [database](./Database.md) object. |
| [FILE](./FILE.md) | R | Gets the server's [file](./Files.md) object. |
| [I](./I.md) | R | Gets the current object. |
| [LIST](./LIST.md) | R | Gets the server's list object. |
| [NEW](./NEW.md) | RW | Gets or sets the last [character](./Characters.md) or [item](./Items.md) created on the server. |
| [OBJ](./OBJ.md) | RW | Gets or sets a reference to a [character](./Characters.md) or [item](./Items.md) |
| [SRC](./SRC.md) | R | Gets the source [character](./Characters.md) of an event. |
| [UID](./UID.md).*object_uid* | R | Gets a reference to the [character](./Characters.md) or [item](./Items.md) with the specified [UID](./UID.md). |

## Properties and Functions

The following table lists all properties and functions that are
available from any script.

<table>
<tbody>
<tr>
<td><p><strong>Name</strong></p></td>
<td><p><strong>Read/Write</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p><a href="ASC" title="wikilink">ASC</a> <em>text</em></p></td>
<td><p>R</p></td>
<td><p>Converts <em>text</em> into a series of ASCII values.</p></td>
</tr>
<tr>
<td><p><a href="ASCPAD" title="wikilink">ASCPAD</a>
<em>size,text</em></p></td>
<td><p>R</p></td>
<td><p>Converts <em>text</em> into a series of ASCII values, padded with
0s untill <em>size</em> is reached. Will also truncate the <em>text</em>
if longer then <em>size</em></p></td>
</tr>
<tr>
<td><p><a href="BETWEEN" title="wikilink">BETWEEN</a> <em>min, max,
numerator, denominator</em></p></td>
<td><p>R</p></td>
<td><p>Returns the value that's <em>numerator/denominator</em> between
<em>min</em> and <em>max</em></p></td>
</tr>
<tr>
<td><p><a href="BETWEEN2" title="wikilink">BETWEEN2</a> <em>min, max,
numerator, denominator</em></p></td>
<td><p>R</p></td>
<td><p>Returns the value that's <em>numerator/denominator</em> between
<em>max</em> and <em>min</em></p></td>
</tr>
<tr>
<td><p><a href="CHR" title="wikilink">CHR</a>
<em>ascii_code</em></p></td>
<td><p>R</p></td>
<td><p>Returns the character represented by the given ASCII
code.</p></td>
</tr>
<tr>
<td><p><a href="CLEARVARS" title="wikilink">CLEARVARS</a>
<em>prefix</em></p></td>
<td><p>W</p></td>
<td><p>Removes all server VARs whose name start with
<em>prefix</em>.</p></td>
</tr>
<tr>
<td><p><a href="CLRBIT" title="wikilink">CLRBIT</a> <em>value,
bit</em></p></td>
<td><p>R</p></td>
<td><p>Returns the value of <em>value</em> with <em>bit</em> not
set.</p></td>
</tr>
<tr>
<td><p><a href="D"
title="wikilink">D</a><em>property_or_function</em></p></td>
<td><p>R</p></td>
<td><p>Forces a property or function to return a decimal value.</p></td>
</tr>
<tr>
<td><p><a href="DEFMSG"
title="wikilink">DEFMSG</a><em>.name</em></p></td>
<td><p>W</p></td>
<td><p>Sets the value of a DEFMESSAGE. (see sphere_msgs.scp)</p></td>
</tr>
<tr>
<td><p><a href="EXPLODE" title="wikilink">EXPLODE</a>
<em>separators</em>, <em>text</em></p></td>
<td><p>R</p></td>
<td><p>Splits <em>text</em> by the given separator characters.</p></td>
</tr>
<tr>
<td><p><a href="EVAL" title="wikilink">EVAL</a>
<em>expression</em></p></td>
<td><p>R</p></td>
<td><p>Evaluates an expression and returns the result as an
integer.</p></td>
</tr>
<tr>
<td><p><a href="FEVAL" title="wikilink">FEVAL</a>
<em>expression</em></p></td>
<td><p>R</p></td>
<td><p>| Evaluates an expression and returns the result as an integer,
supports floating point values.</p></td>
</tr>
<tr>
<td><p><a href="FHVAL" title="wikilink">FHVAL</a>
<em>expression</em></p></td>
<td><p>R</p></td>
<td><p>| Evaluates an expression and returns the result as a hexadecimal
value, supports floating point values.</p></td>
</tr>
<tr>
<td><p><a href="FLOATVAL" title="wikilink">FLOATVAL</a>
<em>expression</em></p></td>
<td><p>R</p></td>
<td><p>Evaluates an expression and returns the result as a floating
point value.</p></td>
</tr>
<tr>
<td><p><a href="FVAL" title="wikilink">FVAL</a>
<em>expression</em></p></td>
<td><p>R</p></td>
<td><p>Evaluates an expression and formats the result with a single
decimal point. ("1000" becomes "100.0")</p></td>
</tr>
<tr>
<td><p><em>ref</em>.<a href="GETREFTYPE"
title="wikilink">GETREFTYPE</a></p></td>
<td><p>R</p></td>
<td><p>Returns a code representing what type of object <em>ref</em>
is.</p></td>
</tr>
<tr>
<td><p><a href="HVAL" title="wikilink">HVAL</a>
<em>expression</em></p></td>
<td><p>R</p></td>
<td><p>Evaluates an expression and returns the result as a hexadecimal
value.</p></td>
</tr>
<tr>
<td><p><a href="ISBIT" title="wikilink">ISBIT</a> <em>value,
bit</em></p></td>
<td><p>R</p></td>
<td><p>Returns non-zero if <em>bit</em> is set in
<em>value</em>.</p></td>
</tr>
<tr>
<td><p><a href="ISEMPTY" title="wikilink">ISEMPTY</a>
<em>value</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if <em>value</em> is empty/blank text.</p></td>
</tr>
<tr>
<td><p><a href="ISNUM" title="wikilink">ISNUM</a>
<em>value</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if <em>value</em> is a numeric value.</p></td>
</tr>
<tr>
<td><p><a href="LISTCOL" title="wikilink">LISTCOL</a></p></td>
<td><p>R</p></td>
<td><p>Returns the alternating colour in webpage tables.</p></td>
</tr>
<tr>
<td><p><a href="MD5HASH" title="wikilink">MD5HASH</a>
<em>text</em></p></td>
<td><p>R</p></td>
<td><p>Returns an MD5 hash for <em>text</em>.</p></td>
</tr>
<tr>
<td><p><a href="MULDIV" title="wikilink">MULDIV</a> <em>num, mul,
div</em></p></td>
<td><p>R</p></td>
<td><p>Returns (<em>num</em> * <em>mul</em>) / <em>div</em>.</p></td>
</tr>
<tr>
<td><p><a href="NEWDUPE" title="wikilink">NEWDUPE</a>
<em>object_uid</em></p></td>
<td><p>W</p></td>
<td><p>Clones the character or item with the specified <a href="UID"
title="wikilink">UID</a>.</p></td>
</tr>
<tr>
<td><p><a href="NEWITEM" title="wikilink">NEWITEM</a> <em>item_defname,
amount, container, equip</em></p></td>
<td><p>W</p></td>
<td><p>Creates a new item.</p></td>
</tr>
<tr>
<td><p><a href="NEWNPC" title="wikilink">NEWNPC</a>
<em>character_defname</em></p></td>
<td><p>W</p></td>
<td><p>Creates a new character.</p></td>
</tr>
<tr>
<td><p><a href="QVAL" title="wikilink">QVAL</a> <em>expression</em>?
<em>value_true</em>:<em>value_false</em></p></td>
<td><p>R</p></td>
<td><p>Evaluates an expression and returns <em>value_true</em> if the
result is true, otherwise returns <em>value_false</em>. There is another
variant of QVAL in the <a href="Intrinsic_Functions"
title="wikilink">Intrinsic Functions</a> category.</p></td>
</tr>
<tr>
<td><p><a href="R" title="wikilink">R</a><em>x</em></p></td>
<td><p>R</p></td>
<td><p>Returns a random number between 0 and <em>x - 1</em>.</p></td>
</tr>
<tr>
<td><p><a href="R" title="wikilink">R</a><em>x, y</em></p></td>
<td><p>R</p></td>
<td><p>Returns a random number between <em>x</em> and
<em>y</em>.</p></td>
</tr>
<tr>
<td><p><a href="SETBIT" title="wikilink">SETBIT</a> <em>value,
bit</em></p></td>
<td><p>R</p></td>
<td><p>Returns the value of <em>value</em> with <em>bit</em>
set.</p></td>
</tr>
<tr>
<td><p><a href="SHOW" title="wikilink">SHOW</a>
<em>property_or_function</em></p></td>
<td><p>W</p></td>
<td><p>Displays the returned value from a property or function to
SRC.</p></td>
</tr>
<tr>
<td><p><a href="STRARG" title="wikilink">STRARG</a>
<em>text</em></p></td>
<td><p>R</p></td>
<td><p>Returns the first word from <em>text</em>.</p></td>
</tr>
<tr>
<td><p><a href="STREAT" title="wikilink">STREAT</a>
<em>text</em></p></td>
<td><p>R</p></td>
<td><p>Removes the first word from <em>text</em> and returns the
remaining text.</p></td>
</tr>
<tr>
<td><p><a href="STRPOS" title="wikilink">STRPOS</a> <em>position
character text</em></p></td>
<td><p>R</p></td>
<td><p>Returns the position of a <em>character</em> within the
<em>text</em>, starting from <em>position</em>.</p></td>
</tr>
<tr>
<td><p><a href="STRREGEXNEW" title="wikilink">STRREGEXNEW</a>
<em>pattern, text</em></p></td>
<td><p>R</p></td>
<td><p>Returns 1 if <em>text</em> matches a regular expression
<em>pattern</em>.</p></td>
</tr>
<tr>
<td><p><a href="STRREVERSE" title="wikilink">STRREVERSE</a>
<em>text</em></p></td>
<td><p>R</p></td>
<td><p>Returns <em>text</em>, after reversing its characters.</p></td>
</tr>
<tr>
<td><p><a href="STRSUB" title="wikilink">STRSUB</a> <em>position, count,
text</em></p></td>
<td><p>R</p></td>
<td><p>Extracts <em>count</em> characters from <em>text</em>, starting
from <em>position</em>.</p></td>
</tr>
<tr>
<td><p><a href="STRTOLOWER" title="wikilink">STRTOLOWER</a>
<em>text</em></p></td>
<td><p>R</p></td>
<td><p>Returns <em>text</em> in lowercase.</p></td>
</tr>
<tr>
<td><p><a href="STRTOUPPER" title="wikilink">STRTOUPPER</a>
<em>text</em></p></td>
<td><p>R</p></td>
<td><p>Returns <em>text</em> in uppercase.</p></td>
</tr>
<tr>
<td><p><a href="STRTRIM" title="wikilink">STRTRIM</a>
<em>text</em></p></td>
<td><p>R</p></td>
<td><p>Removes whitespace (i.e. spaces, tabs) from the start and end of
<em>text</em>.</p></td>
</tr>
<tr>
<td><p><a href="SYSCMD" title="wikilink">SYSCMD</a> <em>command, arg1,
arg2...</em></p></td>
<td><p>R</p></td>
<td><p>Executes a system command on the server and waits for it to
complete.<br />
<strong>Note:</strong> Requires OF_FileCommands to be enabled in
Sphere.ini</p></td>
</tr>
<tr>
<td><p><a href="SYSSPAWN" title="wikilink">SYSSPAWN</a> <em>command,
arg1, arg2...</em></p></td>
<td><p>R</p></td>
<td><p>Executes a system command on the server and does not wait for it
to complete.<br />
<strong>Note:</strong> Requires OF_FileCommands to be enabled in
Sphere.ini</p></td>
</tr>
<tr>
<td><p><a href="UVAL" title="wikilink">UVAL</a>
<em>expression</em></p></td>
<td><p>R</p></td>
<td><p>Evaluates an expression and returns the result as an unsigned
integer.</p></td>
</tr>
<tr>
<td><p><a href="VAR" title="wikilink">VAR</a><em>.name</em></p></td>
<td><p>RW</p></td>
<td><p>Gets or sets the value of a VAR.</p></td>
</tr>
</tbody>
</table>

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Scripts](./_Scripts.md)
