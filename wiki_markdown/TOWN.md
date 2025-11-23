## Description

This document describes the properties and functions related to Towns and their members.

## References
References return pointers to other objects. These can be accessed by using *<REFNAME>* to return the UID (1 for object types that don\'t have UIDs) of the object or 0 if it doesn\'t exist, or by using *<REFNAME.KEY>* where KEY is a valid property/function/reference for the *REFNAME* object.

| Name | Read/Write | Description | Sphere X only? |
|---|---|---|---|
| [OWNER](./Owner.md) | R | Gets the owner of the town. | X |
| [COOWNER.x](./Coowners.md) | R | Gets the Coowner in the Xth position. | X |
| [FRIEND.x](./Friends.md) | R | Gets the Friend in the Xth position. | X |
| [BAN.x](./Bans.md) | R | Gets the Banned character in the Xth position. | X |
| [LOCKDOWN.x](./Lockdowns.md) | R | Gets the locked down item in the Xth position. | X |
| [VENDOR.x](./Vendors.md) | R | Gets the vendor in the Xth position. | X |
| [COMPONENT.x](./Comps.md) | R | Gets the comp in the Xth position. | X |

[Category: Reference Compendium](./CategoryReference_Compendium.md) [Category: Objects](./CategoryObjects.md)