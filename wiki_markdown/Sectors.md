\_\_FORCETOC\_\_ The world is split into fixed-size sectors (by default,
64x64 tiles). Environmental settings (light, weather, etc) are stored on
a per-sector basis. Accessing sectors in scripts can be accomplished
using the SECTOR reference from a [character](./Characters.md),
[item](./Items.md) or [map point](./Map_Points.md) object.
The following table details the various properties of the sector object
in SphereServer:

## Properties and Functions {#properties_and_functions}

Here is a list of all sector properties and functions. If a function is
marked as readable then it can return a value when used as
`<KEY>`{=html}. Click on the name for more detailed information such as
usage and examples.

  --------------------------------------------------- ---------------- -------------------------------------------------------------------------------------------------------
  **Name**                                            **Read/Write**   **Description**
  [ALLCHARS](./ALLCHARS.md) *command*           R                Executes *command* on all characters inside the sector.
  [ALLCHARSIDLE](./ALLCHARSIDLE.md) *command*   R                Executes *command* on all disconnected characters inside the sector.
  [ALLCLIENTS](./ALLCLIENTS.md) *command*       R                Executes *command* on all clients inside the sector.
  [ALLITEMS](./ALLITEMS.md) *command*           R                Executes *command* on all items inside the sector.
  [CANSLEEP](./CANSLEEP.md)                     R                Returns 1 if the sector have all condition to sleep. (X ONLY)
  [CLIENTS](./CLIENTS.md)                       R                Gets the number of clients in the sector.
  [COLDCHANCE](./COLDCHANCE.md)                 RW               Gets or sets the chance of snow for the sector.
  [COMPLEXITY](./COMPLEXITY.md)                 R                Gets the number of characters in the sector.
  [COMPLEXITY](./COMPLEXITY.md).HIGH            R                Returns 1 if the sector has a high complexity. (less than 5 characters)
  [COMPLEXITY](./COMPLEXITY.md).MEDIUM          R                Returns 1 if the sector has a medium complexity. (less than 10 characters)
  [COMPLEXITY](./COMPLEXITY.md).LOW             R                Returns 1 if the sector has a low complexity. (10+ characters)
  [DRY](./DRY.md)                               W                Sets the weather to dry.
  [ISDARK](./ISDARK.md)                         R                Returns 1 if the light level in the sector is considered to be dark.
  [ISNIGHTTIME](./ISNIGHTTIME.md)               R                Returns 1 if the local time of day is between 9pm and 7am.
  [ISSLEEPING](./ISSLEEPING.md)                 R                Returns 1 if the sector is sleeping. (X ONLY)
  [ITEMCOUNT](./ITEMCOUNT.md)                   R                Returns the number of items in the sector.
  [LIGHT](./LIGHT.md)                           RW               Gets or sets the light level for the sector.
  [LOCALTIME](./LOCALTIME.md)                   R                Gets the local time of day, as a descriptive string.
  [LOCALTOD](./LOCALTOD.md)                     R                Gets the local time of day, in minutes.
  [NUMBER](./NUMBER.md)                         R                Gets the index number of the sector.
  [RAIN](./RAIN.md)                             W                Sets the weather to raining.
  [RAINCHANCE](./RAINCHANCE.md)                 RW               Gets or sets the chance of rain for the sector.
  [RESPAWN](./RESPAWN.md) *ALL*                 W                Resurrects dead NPC characters (not corpses). If *ALL* is provided then all sectors will be affected.
  [RESTOCK](./RESTOCK.md) *ALL*                 W                Restocks all NPCs in the sector. If *ALL* is provided then all sectors will be affected.
  [SEASON](./SEASON.md)                         RW               Gets or sets the current season in the sector.
  [SNOW](./SNOW.md)                             W                Sets the weather to snowing.
  [WEATHER](./WEATHER.md)                       RW               Gets or sets the current weather in the sector.
  --------------------------------------------------- ---------------- -------------------------------------------------------------------------------------------------------

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Objects](./_Objects.md)
