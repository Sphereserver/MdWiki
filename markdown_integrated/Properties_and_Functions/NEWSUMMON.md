## NEWSUMMON

This function works like [NEWNPC](NEWNPC) and [NEWITEM](NEWITEM). It summons a creature for a specified amount of time.

### Arguments

*   **creature_defname**: The defname of the creature to summon.
*   **duration**: The duration in seconds for which the creature will be summoned. If not specified, a default timer based on the character's magery skill will be used.
*   **p**: The position where the creature will be summoned.

### Example

`SERV.NEWSUMMON=c_ogre,15 NEW.P=<P>`

This will summon an ogre for 15 seconds at the current position.
