## Description

This trigger fires when a client attempts to access the virtue dialog
for a character, or double clicks a virtue icon on the dialog.

Fires on:

- [Clients](Characters#Clients "wikilink")

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [ARGO](ARGO "wikilink") | The [character](Characters "wikilink") whose virtue dialog is being requested. |
| [I](I "wikilink") | The [client](Characters#Clients "wikilink") attempting to access or use the virtue dialog. |
| [SRC](SRC "wikilink") | The [client](Characters#Clients "wikilink") attempting to access or use the virtue dialog. |

## Arguments

The following arguments are set for this trigger. If an argument is
marked as "In" then a value will be passed in to the trigger, if an
argument is marked as "Out" then it can be set to a value to affect
Sphere's behaviour:

<table>
<tbody>
<tr>
<td><p><strong>Argument</strong></p></td>
<td><p><strong>In/Out</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p>ARGN1</p></td>
<td><p>I</p></td>
<td><p>The action that the client is attempting. Known values are:</p>
<table>
<tbody>
<tr>
<td><p><strong>Action</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>Requesting <a href="ARGO" title="wikilink">ARGO</a>'s virtue
dialog.</p></td>
</tr>
<tr>
<td><p>105</p></td>
<td><p>Compassion button double clicked.</p></td>
</tr>
<tr>
<td><p>106</p></td>
<td><p>Honesty button double clicked.</p></td>
</tr>
<tr>
<td><p>107</p></td>
<td><p>Honoe button double clicked.</p></td>
</tr>
<tr>
<td><p>108</p></td>
<td><p>Humility button double clicked.</p></td>
</tr>
<tr>
<td><p>109</p></td>
<td><p>Justice button double clicked.</p></td>
</tr>
<tr>
<td><p>110</p></td>
<td><p>Sacrifice button double clicked.</p></td>
</tr>
<tr>
<td><p>111</p></td>
<td><p>Spirituality button double clicked.</p></td>
</tr>
<tr>
<td><p>112</p></td>
<td><p>Virtue button double clicked.</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

## Return Values

The following return values are explicitly defined for this trigger:

*No return values are handled for this trigger.*

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Triggers](Category:_Triggers "wikilink") [Category:
Characters](Category:_Characters "wikilink") [Category:
Players](Category:_Players "wikilink")
