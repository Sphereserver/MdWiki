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
[UID](UID "wikilink") (1 for object types that don\'t have UIDs) of the
object or 0 if it doesn\'t exist, or by using *\<REFNAME.KEY\>* where
KEY is a valid property/function/reference for the *REFNAME* object.
Click on the name for more detailed information such as usage and
examples.

  --------------------------- ---------------- ---------------------------------------------------------------------------------------
  **Name**                    **Read/Write**   **Description**
  [CHAR](CHAR "wikilink").n   R                Gets the nth [character](Characters "wikilink") attached to the account. (zero-based)
  --------------------------- ---------------- ---------------------------------------------------------------------------------------

## Properties and Functions {#properties_and_functions}

Here is a list of all account properties and functions. If a function is
marked as readable then it can return a value when used as
`<KEY>`{=html}. Click on the name for more detailed information such as
usage and examples.

  ------------------------------------------------- ---------------- ------------------------------------------------------------------------------------------
  **Name**                                          **Read/Write**   **Description**
  [ACCOUNT](ACCOUNT "wikilink")                     R                Gets the name of the account.
  [BLOCK](BLOCK "wikilink")                         RW               Gets or sets whether or the not the account is blocked.
  [CHARS](CHARS "wikilink")                         R                Gets how many characters are attached to the account.
  [CHATNAME](CHATNAME "wikilink")                   RW               Gets the name the account uses in chat.
  [FIRSTCONNECTDATE](FIRSTCONNECTDATE "wikilink")   RW               Gets the date and time on which the account first connected.
  [FIRSTIP](FIRSTIP "wikilink")                     RW               Gets the IP address that the account first connected with.
  [GUEST](GUEST "wikilink")                         RW               Gets whether or not the account is a guest account.
  [JAIL](JAIL "wikilink")                           RW               Gets whether or not the account is jailed.
  [LANG](LANG "wikilink")                           RW               Gets or sets the account\'s language.
  [LASTCHARUID](LASTCHARUID "wikilink")             RW               Gets the [UID](UID "wikilink") of the last character used on the account.
  [LASTCONNECTDATE](LASTCONNECTDATE "wikilink")     RW               Gets the date and time on which the account most recently connected.
  [LASTIP](LASTIP "wikilink")                       RW               Gets the IP address that the account most recently connected with.
  [MAXCHARS](MAXCHARS "wikilink")                   RW               Gets or sets the maximum number of characters that the player can create on the account.
  [NAME](NAME "wikilink")                           R                Gets the name of the account.
  [NEWPASSWORD](NEWPASSWORD "wikilink")             RW               Gets or sets a new password that will be set on the account.
  [PASSWORD](PASSWORD "wikilink")                   RW               Gets or sets the current password for the account.
  [PLEVEL](PLEVEL "wikilink")                       RW               Gets or sets the account\'s privelege level.
  [PRIV](PRIV "wikilink")                           RW               Gets or sets account flags.
  [RESDISP](RESDISP "wikilink")                     RW               Gets or sets the account\'s expansion level.
  [TAG](TAG "wikilink")*.name*                      RW               Gets or sets the value of a TAG.
  [TAGCOUNT](TAGCOUNT "wikilink")                   R                Gets the number of TAGs on the account.
  [TOTALCONNECTTIME](TOTALCONNECTTIME "wikilink")   RW               Gets the total number of minutes that the account has been connected for.
  ------------------------------------------------- ---------------- ------------------------------------------------------------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Objects](Category:_Objects "wikilink")
