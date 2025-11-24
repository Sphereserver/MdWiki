## Description

This trigger fires when a [skill menu](./SKILLMENU.md) is
displayed to a player. Note that the trigger only fires when Sphere
attempts to display the menu through hardcoded behaviour, using the
[SKILLMENU](./SKILLMENU.md) command will not cause this trigger to
fire.

- The training context menu now filters out and does not display disabled skills (those marked with the `SKF_DISABLED` flag).
Fires on:

- [Players](./CharactersPlayers.md)

## References

The following object references are explicitly available for this
trigger:

|  |  |
|----|----|
| **Name** | **Description** |
| [I](./I.md) | The [player](./CharactersPlayers.md) who the menu is being shown to. |
| [SRC](./SRC.md) | The [player](./CharactersPlayers.md) who the menu is being shown to. |

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
<td><p>ARGS</p></td>
<td><p>I</p></td>
<td><p>The skillmenu's defname. This is expected to be one of the
following:</p>
<ul>
<li>sm_alchemy</li>
<li>sm_blacksmith</li>
<li>sm_bolts</li>
<li>sm_bowcraft</li>
<li>sm_carpentry</li>
<li>sm_cartography</li>
<li>sm_inscription</li>
<li>sm_polymorph</li>
<li>sm_summon</li>
<li>sm_tailor_cloth</li>
<li>sm_tailor_leather</li>
<li>sm_tinker</li>
</ul></td>
</tr>
<tr>
<td><p>BIG change on X</p></td>
<td><p>I</p></td>
<td><p><a
href="https://github.com/Sphereserver/Source-X/blob/3b2c4d9c6dec393eaea725770bb86237e2a85074/Changelog.txt#L3408">https://github.com/Sphereserver/Source-X/blob/3b2c4d9c6dec393eaea725770bb86237e2a85074/Changelog.txt#L3408</a></p></td>
</tr>
</tbody>
</table>

## Return Values

The following return values are explicitly defined for this trigger:

|                  |                                              |
|------------------|----------------------------------------------|
| **Return Value** | **Description**                              |
| 1                | Prevents the skillmenu from being displayed. |

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Triggers](./_Triggers.md)
