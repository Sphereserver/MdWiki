# Usage

**EFFECT type, item_id, speed, loop, explode, colour(hue), rendermode**

# Description

Type is a number 0-3 from the table below. Item_id is the base id (thismust be a "base" item ID - which you can identify as an \[ITEMDEF 0xxx\] where xxx is a number not a name) of the item or animation. If the ID is a animation, you likely want to use the first id of the animation loop. Speed is a number determining the speed of the animation and the travel speed if it's a projectile, with 1 being the slowest and higher numbers being faster. Loop specifies the time the animation will play, 16 is a good default. This is NOT frames of animation, as a high speed results in more frames per given loop setting. Explode is a boolean defining whether the projectile should make an explosion animation when reaching the character.

The EFFECT *always* applies to SRC (and in the case of type 0, thatmeans the item will always move from SRC to it's target.) That means any reference you put in front of EFFECT (for example: OBJ.EFFECT,REF1.EFFECT, TARG.EFFECT, ec...) is ignored. To force a type 0 animation to go *to* the SRC, you need to use TRYSRC (which lets you alter SRCtemporarily) to reverse the direction.

# Effect Types

| **Effect Number** | **Short** | **Long Description** |  |  |
| --- | --- | --- | --- | --- |
| 0 | Standard flying object | The object will follow its target until it hits, and then explode if that flag is set |  |  |
| 1 | Lightning effect | This is the only way to achieve the lightning effect in-game |  |  |
| 2 | Ground-based effect | This effect will stay at a particular point on the map until it expires. As a result, it will appear lower than a type 3 effect. This is the only way to get an effect onto an item. |  |  |
| 3 | Character-based effect | This effect will follow the character as he moves, the way a flamestrike does when the spell is cast. The bottom of the effect is somewhere around the character's knees. |  |  |
| 4 | Flash effect | (New 6+ (needs verification)) Clients Only) Provides a screen-wide effect. All other parameters besides Item Id is ignored. Item Id controls the flash type: <table> **Item Id** | **Effect** | **Description** |
| 0 | Fade to Black (Slow) | Fades the screen to black before returning to normal similar to the death effect found on some client versions |  |  |
| 1 | Fade to White (Slow) | Fades the screen slowly to complete white followed by a return to normal |  |  |
| 2 | Fade to white (Fast) | Fades the screen quickly to complete white followed by a return to normal (lightning flash type effect) |  |  |
| 3 | Fade to White then Black (Slow) | Fades to complete white then to black. Behaves as if effect 1 is played immediately followed by effect 0. |  |  |
| 4 | Fade to Black (Fast) | Fades the screen quickly to complete black followed by a return to normal |  |  |</td>
</tr> </tbody> </table>
