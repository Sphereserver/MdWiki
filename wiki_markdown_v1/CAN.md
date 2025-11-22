# Description

CAN is a Flag like variable, predefined values must be added with
special characters and not with sums or sustractions ( + or - ).

These values adds some behaviour modification for items, like make
sphere they are water (can_i_water), a tile where Gargoyles can hover
over (can_i_hover) and much more.

On X version: CAN flags are read only. You can\'t edit them after the
item/char creation. I you want modify the can Flags you should use
[CANMASK](CANMASK "wikilink")

# Usage

`<spherescript>`{=html} \[itemdef i_test\] id=i_pickaxe name=Pickaxe
can=can_i_flip\|can_i_dye\|can_i_repair //This is how values must be
added, using the \| means they are being sum.

ON=@DClick src.say `<name>`{=html}\'s current can_flags are:
`<can>`{=html} //To check any specific flag this is how its done:

if (`<can>`{=html}&can_i_dye)

`src.say and can be dyeable.`

endif

`</spherescript>`{=html}

`<spherescript>`{=html} CANMASK EXAMPLE ON X VERSION

IF `<CANMASK>`{=html}&mt_nonmover // is on, turn it off

`   CANMASK &=~mt_nonmover`\
`   SYSMESSAGE @,,1 Can move`

else// is off, turn it on

`   CANMASK |= mt_nonmover `\
`   SYSMESSAGE @,,1 Can't move`

ENDIF `</spherescript>`{=html}

# Actual Flags {#actual_flags}

CAN_I_DOOR 000001 // Is a door UFLAG4_DOOR

CAN_I_WATER 000002 // Need to swim in it. UFLAG1_WATER

CAN_I_PLATFORM 000004 // we can walk on top of it. (even tho the item
itself might block) UFLAG2_PLATFORM

CAN_I_BLOCK 000008 // need to walk thru walls or fly over. UFLAG1_BLOCK

CAN_I_CLIMB 000010 // step up on it, UFLAG2_CLIMBABLE

CAN_I_FIRE 000020 // Is a fire. Ussually blocks as well. UFLAG1_DAMAGE

CAN_I_ROOF 000040 // We are under a roof. can\'t rain on us. UFLAG4_ROOF

CAN_I_HOVER 000080 // We are hovering. UFLAG4_HOVEROVER

CAN_I_PILE 000100 // Can item be piled UFLAG2_STACKABLE (\*.mul)

CAN_I_DYE 000200 // Can item be dyed UFLAG3_CLOTH? (sort of)

CAN_I_FLIP 000400 // will flip by default.

CAN_I_LIGHT 000800 // UFLAG3_LIGHT

CAN_I_REPAIR 001000 // Is it repairable (difficulty based on value)

CAN_I_REPLICATE 002000 // Things like arrows are pretty much all the
same.

CAN_I_DCIGNORELOS 004000 // when dclicked, ignore LOS checks

CAN_I_DCIGNOREDIST 008000 // when dclicked, ignore distance checks

CAN_I_BLOCKLOS 010000 // blocks LOS, but not walking thru
