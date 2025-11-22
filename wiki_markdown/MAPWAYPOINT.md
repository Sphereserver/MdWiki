# Usage

REFERENCE.MAPWAYPOINT ObjectUID,WayPointType

# Description

This function adds/removes waypoints on client radar map (enhanced
clients only).

Waypoint types:

`   0 = Remove waypoint`\
`   1 = Corpse`\
`   2 = Party Member`\
`   4 = Quest Giver`\
`   5 = New Player Quest`\
`   6 = Healer`\
`   11 = Shrine`\
`   12 = Moongate`\
`   14 = Green Dot`\
`   15 = Green Dot (flashing)`

# Example

`<spherescript>`{=html}ON=@Dclick //let\'s suppose that dclicked item is
a map (for example) where the target is stored in its link.
src.mapwaypoint `<link>`{=html},4`</spherescript>`{=html}
