## Description

This document describes the properties and functions available through the `SERV` object, which represents the server itself.

## Properties and Functions

| Name | Read/Write | Description | Sphere X only? |
|---|---|---|---|
| [LOGICALRANGE](./LOGICALRANGE.md) *min,max* | R | Gets a random number in a specified range, now supports reverse ranges (e.g., `SERV.LOGICALRANGE(20,-10)`). | X |
| [TRANSFER](./TRANSFER.md) *target_char_uid, item_uid* | W | Transfers an item directly by UID from one character to another. | X |
| [ITEMDEF(defname).CAN](./CAN.md) | R | Retrieves the base CAN property from an ITEMDEF. | X |
| [CHARDEF(defname).CAN](./CAN.md) | R | Retrieves the base CAN property from a CHARDEF. | X |
| [ITEMDEF(defname).ISTEVENT](ISTEVENT "wikilink")*.event_defname* | R | Returns 1 if the ITEMDEF has an event attached to it. | X |
| [CHARDEF(defname).ISTEVENT](ISTEVENT "wikilink")*.event_defname* | R | Returns 1 if the CHARDEF has an event attached to it. | X |
| [TILEDATA](./TILEDATA.md) | R | Reads item and terrain properties directly from `tiledata.mul`. | X |
| [MAXXHOUSES](./MAXXHOUSES.md) | RW | Sets house X limits from scripts. | X |
| [MAXYHOUSES](./MAXYHOUSES.md) | RW | Sets house Y limits from scripts. | X |
| [MAXZHOUSES](./MAXZHOUSES.md) | RW | Sets house Z limits from scripts. | X |
| `SERV.N.SAY` | W | Sends multiple-line messages (up to 4 lines) to the client. | X |
| `SERV.N.SYSMESSAGE` | W | Sends multiple-line system messages (up to 4 lines) to the client. | X |
| `SERV.LOG` | W | Supports writing a log (up to 4 lines) instead of one (client-like). | X |
| `SERV.TIME` | R | Returns the internal time in tenths of seconds (for backwards compatibility). | X |
| `SERV.TIMEHIRES` | R | Returns the internal timer in milliseconds. | X |
| `SERV.TICKPERIOD` | R | Shows how much server ticks are in a real-world second. | X |