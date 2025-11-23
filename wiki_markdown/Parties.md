\_\_FORCETOC\_\_ Clients are able to form parties with each other by
using the `/add` command. When in a party, the party object can be
referenced by using **PARTY.KEY** from the
[client](./CharactersClients.md) object. The following tables
detail the various properties of parties in SphereServer:

## References

References return pointers to other objects (e.g. the CHAR.n reference
allows you to access the characters that are attached to the account).
These can either be accessed by using *\<REFNAME\>* to return the
[UID](./UID.md) (1 for object types that don\'t have UIDs) of the
object or 0 if it doesn\'t exist, or by using *\<REFNAME.KEY\>* where
KEY is a valid property/function/reference for the *REFNAME* object.
Click on the name for more detailed information such as usage and
examples.

  --------------------------------- ---------------- ------------------------------------------------------------------------------------------------
  **Name**                          **Read/Write**   **Description**
  [MASTER](./MASTER.md)       R                Gets the party master, the [character](./Characters.md) who originally formed the party.
  [MEMBER](./MEMBER.md)*.n*   R                Gets the nth [party member](./Characters.md). (zero-based)
  --------------------------------- ---------------- ------------------------------------------------------------------------------------------------

## Properties and Functions {#properties_and_functions}

Here is a list of all party properties and functions. If a function is
marked as readable then it can return a value when used as
`<KEY>`{=html}. Click on the name for more detailed information such as
usage and examples.

  --------------------------------------------------------------- ---------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                                                        **Read/Write**   **Description**
  [ADDMEMBER](./ADDMEMBER.md) *character_uid*               W                Adds a character to the party.
  [ADDMEMBERFORCED](./ADDMEMBERFORCED.md) *character_uid*   W                Adds a character to the party. If the character is already in a party then they will be forced out of it. The character will be added even if the party has reached the maximum size of 10.
  [CLEARTAGS](./CLEARTAGS.md)                               W                Removes all TAGs from the party.
  [DISBAND](./DISBAND.md)                                   W                Disbands the party.
  [ISSAMEPARTYOF](./ISSAMEPARTYOF.md) *character_uid*       R                Returns 1 if a specified character is a member of this party.
  [MEMBERS](./MEMBERS.md)                                   R                Gets the total number of characters in the party.
  [REMOVEMEMBER](./REMOVEMEMBER.md) *character_uid*         W                Removes a character from the party.
  [REMOVEMEMBER](./REMOVEMEMBER.md) @*n*                    W                Removes the nth character from the party. (zero-based)
  [SPEECHFILTER](./SPEECHFILTER.md)                         RW               Gets or sets a function that will be called every time a party member speaks to the party.
  [SYSMESSAGE](./SYSMESSAGE.md) *character_uid, message*    W                Sends a message to a party member (0 = Entire party).
  [SYSMESSAGE](./SYSMESSAGE.md) @*n, message*               W                Sends a message to the nth party member.
  [TAG](./TAG.md)                                           RW               Gets or sets the value of a TAG.
  [TAGAT](./TAGAT.md)*.index*                               R                Gets a TAG at the given zero-based index.
  [TAGAT](./TAGAT.md)*.index*.KEY                           R                Gets the name of the TAG at the given zero-based index.
  [TAGAT](./TAGAT.md)*.index*.VAL                           R                Gets the value of the TAG at the given zero-based index.
  [TAGCOUNT](./TAGCOUNT.md)                                 R                Gets the number of TAGs stored on the party.
  [TAGLIST](./TAGLIST.md)                                   W                Displays a list of all TAGs to SRC.
  --------------------------------------------------------------- ---------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Objects](./_Objects.md)

## Notes
- The PARTY.CREATE function was fixed on 12-05-2017 to work properly.
