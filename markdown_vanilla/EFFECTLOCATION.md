# Usage

**EFFECTLOCATION x,y,z,type, item_id, speed, loop, explode, colour(hue),
rendermode**

Example:

`  [FUNCTION testLocationZ]`  
`  effectLocation <p.x>,<p.y>,`<height>`+1,0,i_sword_long,1,0,0,colors_red,3`

# Description

X branch only. x,y,z are de coordinates where the effect will show on
the ground. Type is a number 0 or 2 from the table below (other effects
will not be played, only effect 0(bolt) and 2(ground level) seems valid,
probably cause they don't accept a map point). Item_id is the base id
(this must be a "base" item ID - which you can identify as an \[ITEMDEF
0xxx\] where xxx is a number not a name) of the item or animation. If
the ID is a animation, you likely want to use the first id of the
animation loop. Speed is a number determining the speed of the animation
and the travel speed if it's a projectile, with 1 being the slowest and
higher numbers being faster. Loop specifies the time the animation will
play, 16 is a good default. This is NOT frames of animation, as a high
speed results in more frames per given loop setting. Explode is a
boolean defining whether the projectile should make an explosion
animation when reaching the character.

# EffectLocation Types

|  |  |  |
|----|----|----|
| **Effect Number** | **Short** | **Long Description** |
| 0 | Standard flying object | The object will follow its target until it hits, and then explode if that flag is set |
| 2 | Ground-based effect | This effect will stay at a particular point on the map until it expires. As a result, it will appear lower than a type 3 effect. This is the only way to get an effect onto an item. |
|  |  |  |
