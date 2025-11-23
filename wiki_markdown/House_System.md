```{=mediawiki}
{{Languages|House_System}}
```

\_\_FORCETOC\_\_

This document describes the comprehensive house system in SphereServer, including various properties, functions, and triggers related to house management, ownership, and components.

## Key Management

### AddKey

AddKey uid(RW),fDupeOnBank:
- uid: The uid of the char to give this key to.
- fPlaceOnBank: if set to 1 will place the key in the char's bank, otherwise it will be bounced to the backpack.
(When reading it, eg: ref1=<AddKey uid>) returns the UID of the generated key.

### RemoveKeys

[RemoveKeys](./RemoveKeys.md) uid(WO): Removes all the keys linked to this house for the character with the given uid.

## House Placement Checks

### f_multi_onplacement_check

This function is called from CItemMulti::Multi_Create when multis do their checks to be placed.

## Parameters

-   `return 0`: Use default checks (wich values may be modified with the below locals)
-   `return 1`: Prevents the multi from being placed.
-   `return 6`: Allows the multi to be placed without default placement checks.

## Local Variables

-   `local.check_BlockRadius=-1, 1, -1, 1` (Default: an area of +1 in each direction)
-   `local.check_MultiRadius=0, -5, 0, -5` (Default: 5 tiles in both North and South)
    -   Values are: West, North, East, South
-   `local.id=m_xxx` (Read Only)
-   `local.p=position` (Read Only)

## House Permissions

- House_Priv defnames:
    - HP_NONE = 0
    - HP_OWNER = 1
    - HP_COOWNER = 2
    - HP_FRIEND = 3
    - HP_ACCESSONLY = 4
    - HP_BAN = 5
    - HP_VENDOR = 6
    - HP_GUILD = 7

## House Properties and Functions

- Added AddHouse uid(WO): Adds the given uid to the player's house.
    If the player current count of houses is greater than the limit he has, the house will be redeeded.
- Added DelHouse uid(WO): Deletes the given uid from the player's list (Will not delete the house)(-1 clears the whole list).
- Added Houses(RO): Return the houses on the player's list.
- Added GetHousePos uid(RO): Returns the position of the given UID on the houses list (-1 if not found).
- Added MaxHouses(RW) to Accounts and Chars, when created they read this new setting from the sphere.ini (if values on sphere.ini change, they will not reflect on already created accounts/chars).
- Added REF to 'HOUSE.x' to access the house in the Nth position, eg: house.3.Redeed, local.house_p=<house.1.p>
Note: Houses generated before this change will not be updated on the player's list, instead the player will still have the memory with color=MEMORY_GUARD (0x100)
linked to the house,since there was no default behaviour other than this and each house script handles it differently, there will be no hardcoded update
to the new system, each house system should be updated according to it's behaviour (ie: removing the memory and setting AddHouse <HouseUID>)

- Added MaxHouses(RW) property for accounts, Default = Serv.MaxHousesAccount.
- Added MaxHouses(RW) property for chars (meant for players), Default = Serv.MaxHousesPlayer.
* Setting MaxHouses = 0 for Players will skip the setting and read it from it's Account.
* Setting MaxHouses = 0 for Players and Accounts will allow to build without limit.

## Ship Properties and Functions

- Added AddShip uid(WO): Adds the given uid to the player's ship.
    If the player current count of ships is greater than the limit he has, the ship will be redeeded.
- Added DelShip uid(WO): Deletes the given uid from the player's list (Will not delete the ship)(-1 clears the whole list).
- Added Ships(RO): Return the ships on the player's list.
- Added GetShipPos uid(RO): Returns the position of the given UID on the ships list (-1 if not found).
- Added MaxShips(RW) to Accounts and Chars, when created they read this new setting from the sphere.ini (if values on sphere.ini change, they will not reflect on already created accounts/chars).
- Added REF to 'SHIP.x' to access the ship in the Nth position, eg: ship.3.Redeed, local.ship_p=<ship.1.p>
Note: Ships generated before this change will not be updated on the player's list, instead the player will still have the memory with color=MEMORY_GUARD (0x100)
linked to the ship,since there was no default behaviour other than this and each ship script handles it differently, there will be no hardcoded update
to the new system, each ship system should be updated according to it's behaviour (ie: removing the memory and setting AddShip <ShipUID>)

- Added MaxShips(RW) property for accounts, Default = Serv.MaxShipsAccount.
- Added MaxShips(RW) property for chars (meant for players), Default = Serv.MaxShipsPlayer.
* Setting MaxShips = 0 for Players will skip the setting and read it from it's Account.
* Setting MaxShips = 0 for Players and Accounts will allow to build without limit.

## House Storage

- BaseStorage(RW): Limit of storage allowed by default = 489 (Max 65535).
- IncreasedStorage(RW): Increased % of storage allowed (Max 65535%).
- MaxStorage(RO): Returns the maximum storage allowed: BaseStorage + ((BaseStorage / IncreasedStorage)/100) (Max 65535).
- CurrentStorage(RO): Returns the current storage used.

- BaseVendors(RW): Limit of Vendors allowed by default = 10 (Max 255).
- MaxVendors(RO): Returns the maximum Vendors allowed: BaseVendors + ((BaseVendors / IncreasedStorage)/100) (Max 255).

- LockdownsPercent(RW): Base percent of allowed Lockdowns (Max 255).
- MaxLockdowns(RO): Total Lockdowns allowed based on MaxStorage: + ((MaxStorage / LockdownsPercent)/100) (Max 65535).

## Triggers

### @Redeed trigger for multis (t_multi, t_ship, t_multi_custom, t_addon)

- argn1=ID of the deed (Default=i_deed)
- argn2=1 (Default = 1). If set to 1 all items will be moved to the Moving Crate (and Addons redeeded).
- argn3=1 If set to 1 the Moving Crate will be transfered to Owner's Bank (if there is any).
    Note: the crate is moved to the OWNER's bank, not SRC.
    If argn2 = 0 then argn3 will be not used regardless of the value it has.
- SRC = Player doing the redeed (If Any). When the multi is being removed there is no SRC (also when an Addon is being redeeded from internal functions).
- ARGO = The deed.
- return 1 will prevent the deed from being created, but will not block the code from argn2 and argn3

### @HouseDesignBegin trigger for t_multi_custom

Called when the player enters on design mode.

- argn1: If set to 1 Redeeds all addons on the multi. (Default = 1)
- argn2: If set to 1 Transfer all Locked Items and Secured containers to the Moving Crate (default = 0)
- argn3: If set to 1 Ejects from the house all chars inside the house excepting the player entering in design mode,
        if set to 2 Ejects everyone from the house
        if set to 0 doesn't eject anyone.
        All chars ejected will be moved to the House sign.
- return 1: Forces the char to exit Customize mode.
- WARNING: Forcing the char to exit here and setting argn1=0 in @HouseDesignExit will make it enter in customize mode, exit, enter... infinitelly, hence crashing the server with an infinite loop.