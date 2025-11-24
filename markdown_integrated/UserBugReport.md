## Description

This trigger fires when a player submits a bug report.

Fires on:

- [Players](./CharactersPlayers.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [player](./CharactersPlayers.md) submitting the report. |
| [SRC](./SRC.md) | The [player](./CharactersPlayers.md) submitting the report. |

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
<td><p>The report category code. Expected codes are:</p>
<table>
<tbody>
<tr>
<td><p><strong>Code</strong></p></td>
<td><p><strong>Meaning</strong></p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>Environment</p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p>Wearables</p></td>
</tr>
<tr>
<td><p>3</p></td>
<td><p>Combat</p></td>
</tr>
<tr>
<td><p>4</p></td>
<td><p>UI</p></td>
</tr>
<tr>
<td><p>5</p></td>
<td><p>Crash</p></td>
</tr>
<tr>
<td><p>6</p></td>
<td><p>Stuck</p></td>
</tr>
<tr>
<td><p>7</p></td>
<td><p>Animations</p></td>
</tr>
<tr>
<td><p>8</p></td>
<td><p>Performance</p></td>
</tr>
<tr>
<td><p>9</p></td>
<td><p>NPCs</p></td>
</tr>
<tr>
<td><p>10</p></td>
<td><p>Creatures</p></td>
</tr>
<tr>
<td><p>11</p></td>
<td><p>Pets</p></td>
</tr>
<tr>
<td><p>12</p></td>
<td><p>Housing</p></td>
</tr>
<tr>
<td><p>13</p></td>
<td><p>Lost Item</p></td>
</tr>
<tr>
<td><p>14</p></td>
<td><p>Exploit</p></td>
</tr>
<tr>
<td><p>15</p></td>
<td><p>Other</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p>ARGS</p></td>
<td><p>I</p></td>
<td><p>The report text.</p></td>
</tr>
<tr>
<td><p>LOCAL.LANG</p></td>
<td><p>I</p></td>
<td><p>The language the report was submitted in.</p></td>
</tr>
</tbody>
</table>

## Return Values

The following return values are explicitly defined for this trigger:

*No return values are handled this trigger.*

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md) [Category:
Characters](./_Characters.md) [Category:
Players](./_Players.md)
