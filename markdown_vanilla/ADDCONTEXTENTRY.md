AddContextEntry takes 2 to 4 arguments separated by a comma:

`SRC.AddContextEntry EntryTag,TextID,Flags,Color`

<table>
<tbody>
<tr>
<td><p>EntryTag</p></td>
<td><ul>
<li>the number to return as ARGN by @(item)ContextMenuSelect. Make it
unique.</li>
<li>EntryTags from 0 to 100 are reserved by Sphere for internal use, so
do not use those.</li>
</ul></td>
</tr>
<tr>
<td><p>TextID</p></td>
<td><ul>
<li>CLILOCed name of the button. The number from
cliloc.[your_localization]</li>
<li>the legal range is between 3,000,000 and 3,032,767 (or 0 and
32,767... in which case, 3000000 is added for you.)</li>
</ul></td>
</tr>
<tr>
<td><p>Flags</p></td>
<td><ul>
<li>01 - locked (will be grayed out)</li>
<li>02 - consecutive entries with this flag set will be summarized under
a golden arrow</li>
<li>020 - can be colored</li>
</ul></td>
</tr>
<tr>
<td><p>Color</p></td>
<td><ul>
<li>applied only if Flags &amp; 020</li>
<li>any hue value can be specified</li>
</ul></td>
</tr>
</tbody>
</table>
