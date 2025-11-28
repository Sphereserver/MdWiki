# Description

CAN is a Flag like variable, predefined values must be added with
special characters and not with sums or sustractions ( + or - ).

These values adds some behaviour modification for items, like make
sphere they are water (can_i_water), a tile where Gargoyles can hover
over (can_i_hover) and much more.

This flag is only readable in X branch. Please check @CANMASK instead.

# Usage

<spherescript> \[chardef c_test\] id=c_man name=Dummy
can=mt_male\|mt_swim\|mt_walk //This is how values must be added, using
the \| means they are being sum.

ON=@Create str=10 dex=10

ON=@DClick src.say <name>'s current can_flags are: <can> //To check any
specific flag this is how its done:

if (<can>&mt_swim)

`src.say and can walk on water.`

endif

</spherescript>

# Actual Flags

<spherescript> mt_male 00000 mt_nonmover 00000 mt_ghost 00001 // Moves
through doors mt_swim 00002 // Moves on water mt_walk 00004 // Can walk
on land mt_passwalls 00008 // Walk through walls mt_fly 00010
mt_fire_immune 00020 mt_indoors 00040 // Can go under roof mt_hover
00080 // Hovers (can follow gargoyle flight paths) mt_equip 00100
mt_usehands 00200 mt_mount 00400 // can ride mountables mt_female 00800
mt_nonhum 01000 // Body type for combat messages mt_run 02000
mt_nodclicklos 04000 // when dclicking sth., ignore LOS checks
mt_nodclickdist 08000 // when dclicking sth., ignore distance checks
</spherescript>
