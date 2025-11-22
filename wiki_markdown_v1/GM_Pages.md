```{=mediawiki}
{{Languages|GM_Pages}}
```
\_\_FORCETOC\_\_ When a client submits a GM page, these pages can be
accessed through scripts using the *GMPAGE.n* reference from the
[server](Server "wikilink") object. The following table details the
various properties of GM pages in SphereServer:

## Properties and Functions {#properties_and_functions}

Here is a list of all GM page properties and functions. If a function is
marked as readable then it can return a value when used as
`<KEY>`{=html}. Click on the name for more detailed information such as
usage and examples.

  ------------------------------- ---------------- ------------------------------------------------------------------------------
  **Name**                        **Read/Write**   **Description**
  [ACCOUNT](ACCOUNT "wikilink")   R                Gets the name of the account that sent the page.
  [HANDLED](HANDLED "wikilink")   R                Gets the [UID](UID "wikilink") of the character currently handling the page.
  [P](P "wikilink")               RW               Gets or sets the location that the page was sent from.
  [REASON](REASON "wikilink")     RW               Gets or sets the reason for the page.
  [STATUS](STATUS "wikilink")     R                Gets the status of the page sender (OFFLINE, LOGIN or character name).
  [TIME](TIME "wikilink")         RW               Gets the time since the page was originally sent in seconds.
  ------------------------------- ---------------- ------------------------------------------------------------------------------

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Objects](Category:_Objects "wikilink")
