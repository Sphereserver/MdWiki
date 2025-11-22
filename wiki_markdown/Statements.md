<table>
<tbody>
<tr>
<td><p><strong>Statement</strong></p></td>
<td><p><strong>End Statement</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p><a href="BEGIN" title="wikilink">BEGIN</a></p></td>
<td><p>END</p></td>
<td><p>Groups a set of lines together, for use with <a href="DORAND"
title="wikilink">DORAND</a> and <a href="DOSWITCH"
title="wikilink">DOSWITCH</a> statements.</p></td>
</tr>
<tr>
<td><p><a href="DORAND" title="wikilink">DORAND</a>
<em>line_count</em></p></td>
<td><p>ENDDO</p></td>
<td><p>Executes a random line of code within the block.</p></td>
</tr>
<tr>
<td><p><a href="DOSWITCH" title="wikilink">DOSWITCH</a>
<em>line_number</em></p></td>
<td><p>ENDDO</p></td>
<td><p>Executes the specified line of code within the block.</p></td>
</tr>
<tr>
<td><p><a href="FOR" title="wikilink">FOR</a> <em>start
end</em></p></td>
<td><p>ENDFOR</p></td>
<td><p>Loops through the block of code</p></td>
</tr>
<tr>
<td><p><a href="FORCHARLAYER" title="wikilink">FORCHARLAYER</a>
<em>layer_id</em></p></td>
<td><p>ENDFOR</p></td>
<td><p>Loops through all items that a character has equipped on a
specified layer.</p></td>
</tr>
<tr>
<td><p><a href="FORCHARMEMORYTYPE"
title="wikilink">FORCHARMEMORYTYPE</a> <em>memory_flags</em></p></td>
<td><p>ENDFOR</p></td>
<td><p>Loops through all memory items on a character that have one of
the specified flags.</p></td>
</tr>
<tr>
<td><p><a href="FORCHARS" title="wikilink">FORCHARS</a>
<em>distance</em></p></td>
<td><p>ENDFOR</p></td>
<td><p>Loops through all characters within <em>distance</em>
tiles.</p></td>
</tr>
<tr>
<td><p><a href="FORCLIENTS" title="wikilink">FORCLIENTS</a>
<em>distance</em></p></td>
<td><p>ENDFOR</p></td>
<td><p>Loops through all connected clients within <em>distance</em>
tiles.</p></td>
</tr>
<tr>
<td><p><a href="FORCONT" title="wikilink">FORCONT</a> <em>container_uid,
max_subcontainers</em></p></td>
<td><p>ENDFOR</p></td>
<td><p>Loops through all items inside a container.</p></td>
</tr>
<tr>
<td><p><a href="FORCONTID" title="wikilink">FORCONTID</a> <em>item_id,
max_subcontainers</em>''</p></td>
<td><p>ENDFOR</p></td>
<td><p>Loops through all items inside a container with a specified <a
href="BASEID" title="wikilink">BASEID</a></p></td>
</tr>
<tr>
<td><p><a href="FORCONTTYPE" title="wikilink">FORCONTTYPE</a> <em>type,
max_subcontainers</em></p></td>
<td><p>ENDFOR</p></td>
<td><p>Loops through all items inside a container with a specified <a
href="TYPE" title="wikilink">TYPE</a></p></td>
</tr>
<tr>
<td><p><a href="FORINSTANCES" title="wikilink">FORINSTANCES</a>
<em>defname</em></p></td>
<td><p>ENDFOR</p></td>
<td><p>Loops through all instances of characters or items with the
specified <a href="BASEID" title="wikilink">BASEID</a></p></td>
</tr>
<tr>
<td><p><a href="FORITEMS" title="wikilink">FORITEMS</a>
<em>distance</em></p></td>
<td><p>ENDFOR</p></td>
<td><p>Loops through all items within <em>distance</em> tiles.</p></td>
</tr>
<tr>
<td><p><a href="FOROBJS" title="wikilink">FOROBJS</a>
<em>distance</em></p></td>
<td><p>ENDFOR</p></td>
<td><p>Loops through all items and players within <em>distance</em>
tiles.</p></td>
</tr>
<tr>
<td><p><a href="FORPLAYERS" title="wikilink">FORPLAYERS</a>
<em>distance</em></p></td>
<td><p>ENDFOR</p></td>
<td><p>Loops through all players (online and offline) within
<em>distance</em> tiles.</p></td>
</tr>
<tr>
<td><p><a href="IF" title="wikilink">IF</a> <em>condition</em><br />
<a href="IF" title="wikilink">ELIF</a> <em>condition</em><br />
<a href="IF" title="wikilink">ELSEIF</a> <em>condition</em></p></td>
<td><p>ENDIF</p></td>
<td><p>Executes the block of code if <em>condition</em> is
true.</p></td>
</tr>
<tr>
<td><p><a href="WHILE" title="wikilink">WHILE</a>
<em>condition</em></p></td>
<td><p>ENDWHILE</p></td>
<td><p>Loops through the block of code whilst <em>condition</em> is
true.</p></td>
</tr>
<tr>
<td><p>&lt;local._for&gt;</p></td>
<td></td>
<td><p>Current Step of the Loop for the FOR statements. Note, not all of
the FOR statements use this concept... for example, in a FORITEMS
statement, the &lt;local._for&gt; counter will always be zero no matter
how many objects the statement loops over.</p></td>
</tr>
<tr>
<td><p>&lt;local._while&gt;</p></td>
<td></td>
<td><p>Current Step of the Loop for the WHILE statement.</p></td>
</tr>
</tbody>
</table>

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Scripts](./_Scripts.md)
