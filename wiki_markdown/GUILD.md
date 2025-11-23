## Description

This document describes the properties and functions related to Guilds and their alliances.

## References
References return pointers to other objects. These can be accessed by using *<REFNAME>* to return the UID (1 for object types that don\'t have UIDs) of the object or 0 if it doesn\'t exist, or by using *<REFNAME.KEY>* where KEY is a valid property/function/reference for the *REFNAME* object.

| Name | Read/Write | Description | Sphere X only? |
|---|---|---|---|
| [ISALLY](./ISALLY.md) *guild_uid* | R | Checks if a guild is an ally. | X |
| [WEALLIANCE](./WEALLIANCE.md) *guild_uid* | RW | Sets or checks our guild's alliance status with another guild. | X |
| [THEYALLIANCE](./THEYALLIANCE.md) *guild_uid* | RW | Sets or checks another guild's alliance status with our guild. | X |
| [OWNER](./Owner.md) | R | Gets the owner of the guild. | X |
| [COOWNER.x](./Coowners.md) | R | Gets the Coowner in the Xth position. | X |
| [FRIEND.x](./Friends.md) | R | Gets the Friend in the Xth position. | X |
| [BAN.x](./Bans.md) | R | Gets the Banned character in the Xth position. | X |
| [LOCKDOWN.x](./Lockdowns.md) | R | Gets the locked down item in the Xth position. | X |
| [VENDOR.x](./Vendors.md) | R | Gets the vendor in the Xth position. | X |
| [COMPONENT.x](./Comps.md) | R | Gets the comp in the Xth position. | X |

## Notes
- Setting `GUILD` to `0` will empty the guild value for list-based values (Coowners, Friends, Bans, Vendors, Accesses).

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Objects](./CategoryObjects.md)