# Usage

**EFFECT type, item_id, speed, loop, explode, colour(hue), rendermode**

# Description

Type is a number 0-3 from the table below. Item_id is the base id (this
must be a \"base\" item ID - which you can identify as an \[ITEMDEF
0xxx\] where xxx is a number not a name) of the item or animation. If
the ID is a animation, you likely want to use the first id of the
animation loop. Speed is a number determining the speed of the animation
and the travel speed if it\'s a projectile, with 1 being the slowest and
higher numbers being faster. Loop specifies the time the animation will
play, 16 is a good default. This is NOT frames of animation, as a high
speed results in more frames per given loop setting. Explode is a
boolean defining whether the projectile should make an explosion
animation when reaching the character.

The EFFECT *always* applies to SRC (and in the case of type 0, that
means the item will always move from SRC to it\'s target.) That means
any reference you put in front of EFFECT (for example: OBJ.EFFECT,
REF1.EFFECT, TARG.EFFECT, ec\...) is ignored. To force a type 0
animation to go *to* the SRC, you need to use TRYSRC (which lets you
alter SRC temporarily) to reverse the direction. You can also use
[EFFECTLOCATION](./EFFECTLOCATION.md) to target a specific terrain
location instead of an object.

## Notes
- For Enhanced Client, the duration of the effect is multiplied by 3 to compensate for the shorter effect display time compared to the Classic Client.


# Effect Types {#effect_types}

+-------------------+-----------------------+-----------------------+
| **Effect Number** | **Short**             | **Long Description**  |
+-------------------+-----------------------+-----------------------+
| 0                 | Standard flying       | The object will       |
|                   | object                | follow its target     |
|                   |                       | until it hits, and    |
|                   |                       | then explode if that  |
|                   |                       | flag is set           |
+-------------------+-----------------------+-----------------------+
| 1                 | Lightning effect      | This is the only way  |
|                   |                       | to achieve the        |
|                   |                       | lightning effect      |
|                   |                       | in-game               |
+-------------------+-----------------------+-----------------------+
| 2                 | Ground-based effect   | This effect will stay |
|                   |                       | at a particular point |
|                   |                       | on the map until it   |
|                   |                       | expires. As a result, |
|                   |                       | it will appear lower  |
|                   |                       | than a type 3 effect. |
|                   |                       | This is the only way  |
|                   |                       | to get an effect onto |
|                   |                       | an item.              |
+-------------------+-----------------------+-----------------------+
| 3                 | Character-based       | This effect will      |
|                   | effect                | follow the character  |
|                   |                       | as he moves, the way  |
|                   |                       | a flamestrike does    |
|                   |                       | when the spell is     |
|                   |                       | cast. The bottom of   |
|                   |                       | the effect is         |
|                   |                       | somewhere around the  |
|                   |                       | character\'s knees.   |
+-------------------+-----------------------+-----------------------+
| 4                 | Flash effect          | Provides a screen-wide effect. Can be used only directly on client chars and requires client >= 6x. All other parameters besides Item Id are ignored. Item Id controls the flash type:
|                   |                       |   -   `0`: Fade to Black (Slow)
|                   |                       |   -   `1`: Fade to White (Slow)
|                   |                       |   -   `2`: Fade to White (Fast)
|                   |                       |   -   `3`: Fade to White then Black (Slow)
|                   |                       |   -   `4`: Fade to Black (Fast)
+-------------------+-----------------------+-----------------------+
