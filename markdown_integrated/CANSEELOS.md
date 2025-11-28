# Usage

REFERENCE.CANSEELOS TARGET

# Description

CANSEELOS is a test, so it is most often used in an IF statement. What
it does is calculate a direct line from the eyes of the character
(typically SRC) to the item, character, or point location... and if
there is anything that blocks on that path, then you can't see.

If you *can* see the target, the return value is 1, and if you *cannot*
see, the return value is 0.

When testing... keep in mind that a GM has line of sight to everything!

# Example

<spherescript>ON=@TargOn_Item

`IF !(<SRC.TARG.CANSEELOS>)`  
` SRC.SYSMESSAGE @032 That item is not within line of sight`  
` RETURN 1`  
`ENDIF`

ON=@TargOn_Ground

`IF !(<SRC.CANSEELOS <SRC.TARGP>>)`  
` SRC.SYSMESSAGE @032 That location is not within line of sight`  
` RETURN 1`  
`ENDIF`</spherescript>
