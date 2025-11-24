# Description

X branch only. This property is a bitmask, like the CAN property, and
stores the [CAN (Characters)](CAN_(Characters) "wikilink") flags to be
dynamically switched on or off from the base CAN property.

When retrieving the CAN property, now it is first XORed with CANMASK
(the return value will be CAN \^ CANMASK), so in other words:

If a flag set in the CANMASK is also set in CAN, the flag is ignored; If
a flag set in the CANMASK isn\'t set in CAN, the flag is considered as
set.
