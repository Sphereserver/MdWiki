```{=mediawiki}
{{Languages|Accounts}}
```
\_\_FORCETOC\_\_ Player characters are attached to accounts. The account
object can be referenced by using *ACCOUNT.KEY* from the character
object or *ACCOUNT.name_or_index.KEY* from the server object. The
following tables detail the various properties of accounts in
SphereServer:

## References

References return pointers to other objects (e.g. the CHAR.n reference
allows you to access the characters that are attached to the account).
These can either be accessed by using *\<REFNAME\>* to return the
[UID](./UID.md) (1 for object types that don\'t have UIDs) of the
object or 0 if it doesn\'t exist, or by using *\<REFNAME.KEY\>* where
KEY is a valid property/function/reference for the *REFNAME* object.
Click on the name for more detailed information such as usage and
examples.

  --------------------------- ---------------- ---------------------------------------------------------------------------------------
  **Name**                    **Read/Write**   **Description**
  [CHAR](./CHAR.md).n   R                Gets the nth [character](./Characters.md) attached to the account. (zero-based)
  [HOUSE](./House_multi.md).x R Gets the house in the Nth position.
  [OWNER](./Owner.md) R Gets the owner of the house.
  [COOWNER.x](./Coowners.md) R Gets the Coowner in the Xth position.
  [FRIEND.x](./Friends.md) R Gets the Friend in the Xth position.
  [BAN.x](./Bans.md) R Gets the Banned character in the Xth position.
  [LOCKDOWN.x](./Lockdowns.md) R Gets the locked down item in the Xth position.
  [VENDOR.x](./Vendors.md) R Gets the vendor in the Xth position.
  [COMPONENT.x](./Comps.md) R Gets the comp in the Xth position.
  --------------------------- ---------------- ---------------------------------------------------------------------------------------

## Properties and Functions {#properties_and_functions}

Here is a list of all account properties and functions. If a function is
marked as readable then it can return a value when used as
`<KEY>`{=html}. Click on the name for more detailed information such as
usage and examples.

## Notes
- Clients with an account `PLEVEL` of 2 or greater (starting from Counselor priv) now log out instantly. Previously, this only occurred if GM mode was activated, regardless of `PLEVEL`.

  ------------------------------------------------- ---------------- ------------------------------------------------------------------------------------------
  **Name**                                          **Read/Write**   **Description**
  [ACCOUNT](./ACCOUNT.md)                     R                Gets the name of the account.
  [BLOCK](./BLOCK.md)                         RW               Gets or sets whether or the not the account is blocked.
  [CHARS](./CHARS.md)                         R                Gets how many characters are attached to the account.
  [CHATNAME](./CHATNAME.md)                   RW               Gets the name the account uses in chat.
  [FIRSTCONNECTDATE](./FIRSTCONNECTDATE.md)   RW               Gets the date and time on which the account first connected.
  [FIRSTIP](./FIRSTIP.md)                     RW               Gets the IP address that the account first connected with.
  [GUEST](./GUEST.md)                         RW               Gets whether or not the account is a guest account.
  [JAIL](./JAIL.md)                           RW               Gets whether or not the account is jailed.
  [LANG](./LANG.md)                           RW               Gets or sets the account\'s language.
  [LASTCHARUID](./LASTCHARUID.md)             RW               Gets the [UID](./UID.md) of the last character used on the account.
  [LASTCONNECTDATE](./LASTCONNECTDATE.md)     RW               Gets the date and time on which the account most recently connected.
  [LASTIP](./LASTIP.md)                       RW               Gets the IP address that the account most recently connected with.
| [MAXCHARS](./MAXCHARS.md)                   | RW               | Gets or sets the maximum number of characters that the player can create on the account.                   |
| [MAXHOUSES](./MaxHouses.md)                  | RW               | Max houses an account can have.                                                            |
  [NAME](./NAME.md)                           R                Gets the name of the account.
  [NEWPASSWORD](./NEWPASSWORD.md)             RW               Gets or sets a new password that will be set on the account.
  [PASSWORD](./PASSWORD.md)                   RW               Gets or sets the current password for the account.
  [PLEVEL](./PLEVEL.md)                       RW               Gets or sets the account\'s privelege level.
  [PRIV](./PRIV.md)                           RW               Gets or sets account flags.
  [RESDISP](./RESDISP.md)                     RW               Gets or sets the account\'s expansion level.
  [TAG](./TAG.md)*.name*                      RW               Gets or sets the value of a TAG.
  [TAGCOUNT](./TAGCOUNT.md)                   R                Gets the number of TAGs on the account.
  [TOTALCONNECTTIME](./TOTALCONNECTTIME.md)   RW               Gets the total number of minutes that the account has been connected for.
  ------------------------------------------------- ---------------- ------------------------------------------------------------------------------------------

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Objects](./_Objects.md)
