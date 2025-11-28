# Usage

**EFFECT type, item_id, speed, loop, explode, colour(hue), rendermode**

# Description

Type is a number 0-3 from the table below. Item_id is the base id (this
must be a "base" item ID - which you can identify as an \[ITEMDEF 0xxx\]
where xxx is a number not a name) of the item or animation. If the ID is
a animation, you likely want to use the first id of the animation loop.
Speed is a number determining the speed of the animation and the travel
speed if it's a projectile, with 1 being the slowest and higher numbers
being faster. Loop specifies the time the animation will play, 16 is a
good default. This is NOT frames of animation, as a high speed results
in more frames per given loop setting. Explode is a boolean defining
whether the projectile should make an explosion animation when reaching
the character.

The EFFECT *always* applies to SRC (and in the case of type 0, that
means the item will always move from SRC to it's target.) That means any
reference you put in front of EFFECT (for example: OBJ.EFFECT,
REF1.EFFECT, TARG.EFFECT, ec...) is ignored. To force a type 0 animation
to go *to* the SRC, you need to use TRYSRC (which lets you alter SRC
temporarily) to reverse the direction.

# Effect Types

<table>
<tbody>
<tr>
<td><p><strong>Effect Number</strong></p></td>
<td><p><strong>Short</strong></p></td>
<td><p><strong>Long Description</strong></p></td>
</tr>
<tr>
<td><p>0</p></td>
<td><p>Standard flying object</p></td>
<td><p>The object will follow its target until it hits, and then explode
if that flag is set</p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>Lightning effect</p></td>
<td><p>This is the only way to achieve the lightning effect
in-game</p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p>Ground-based effect</p></td>
<td><p>This effect will stay at a particular point on the map until it
expires. As a result, it will appear lower than a type 3 effect. This is
the only way to get an effect onto an item.</p></td>
</tr>
<tr>
<td><p>3</p></td>
<td><p>Character-based effect</p></td>
<td><p>This effect will follow the character as he moves, the way a
flamestrike does when the spell is cast. The bottom of the effect is
somewhere around the character's knees.</p></td>
</tr>
<tr>
<td><p>4</p></td>
<td><p>Flash effect</p></td>
<td><p>(New 6+ (needs verification)) Clients Only) Provides a
screen-wide effect. All other parameters besides Item Id is ignored.
Item Id controls the flash type:</p>
<table>
<tbody>
<tr>
<td><p><strong>Item Id</strong></p></td>
<td><p><strong>Effect</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr>
<td><p>0</p></td>
<td><p>Fade to Black (Slow)</p></td>
<td><p>Fades the screen to black before returning to normal similar to
the death effect found on some client versions</p></td>
</tr>
<tr>
<td><p>1</p></td>
<td><p>Fade to White (Slow)</p></td>
<td><p>Fades the screen slowly to complete white followed by a return to
normal</p></td>
</tr>
<tr>
<td><p>2</p></td>
<td><p>Fade to white (Fast)</p></td>
<td><p>Fades the screen quickly to complete white followed by a return
to normal (lightning flash type effect)</p></td>
</tr>
<tr>
<td><p>3</p></td>
<td><p>Fade to White then Black (Slow)</p></td>
<td><p>Fades to complete white then to black. Behaves as if effect 1 is
played immediately followed by effect 0.</p></td>
</tr>
<tr>
<td><p>4</p></td>
<td><p>Fade to Black (Fast)</p></td>
<td><p>Fades the screen quickly to complete black followed by a return
to normal</p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>
