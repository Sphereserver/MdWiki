\_\_FORCETOC\_\_ Skill menus are a more advanced form of
[MENU](MENU "wikilink") where options can be hidden from the client
based on criteria.

## Syntax

The syntax for a skill menu is identical to a menu except for the
definition starting with \[SKILLMENU rather than \[MENU. As with menus
there are both text-based and item-based styles possible. Only the
syntax for the item-based style of skill menu is shown below:

`[SKILLMENU `*`defname`*`]`\
*`title`*\
\
`ON=`*`baseid`*` `*`text`*\
`    `*`script`*\
\
`ON=`*`baseid`*` @`*`hue`*`, `*`text`*\
`    `*`script`*\
\

  ----------- --------------------------------------------------------------------------------------------------------
  **Name**    **Description**
  *defname*   The menu\'s defname.
  *title*     The title of the menu. Properties and references of the object the menu was called on can be accessed.
  *baseid*    The item [BASEID](BASEID "wikilink") to display for the button.
  *hue*       If the @*hue* syntax is used, the item will be displayed in the specified colour.
  *text*      The text to display for the option. Properties of the ITEMDEF that *baseid* refers to can be accessed.
  *script*    The script to run when the button is pressed.
              
  ----------- --------------------------------------------------------------------------------------------------------

## Functions

Whilst the syntax for a skill menu is identical to a menu, the
difference is that before displaying an option to the client Sphere will
search the *script* lines for the following functions (more than one can
be present). These functions affect the visibility of the menu option.

  -------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                                           **Description**
  [MAKEITEM](MAKEITEM "wikilink") *item_baseid*      Checks if the client meets the criteria for crafting the item ([SKILLREQ](SKILLREQ "wikilink") and [RESOURCES](RESOURCES "wikilink") properties on the item\'s [ITEMDEF](ITEMDEF "wikilink")).
  [SKILLMENU](SKILLMENU "wikilink") *skillmenu_id*   Searches the skillmenu to see what options are available to the client. If there are no visible items in the submenu then the option will be hidden from the client.
  [TEST](TEST "wikilink") *resource_or_skill_list*   Checks if the client possesses all of the listed resources/skills. If they do not then the menu option will not be available to them.
  [TESTIF](TESTIF "wikilink") *condition*            Checks the condition. If it evaluates to false then the menu option will not be available to the client.
  -------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Triggers

When the client selects an option from the skill menu, the \"ON=*\...*\"
section will be executed, in a similar fashion to how a trigger would
fire.

If the client cancels the menu (by right-clicking it, or for text-based
menus by pressing \"Cancel\"), an \@Cancel trigger will be fired.

In both cases, the following references and arguments are available:

  --------------------------- ------------------------------------------------------------------------------------------------------------
  **Name**                    **Description**
  **[I](I "wikilink")**       The [character](Characters "wikilink") or [item](Items "wikilink") that the MENU function was called from.
  **[SRC](SRC "wikilink")**   The client operating the menu.
  --------------------------- ------------------------------------------------------------------------------------------------------------

## Examples

`<spherescript>`{=html} // // sm_cloth_misc skill menu from the default
script pack. // \[SKILLMENU sm_cloth_misc\] Misc.

ON=i_SASH `<NAME>`{=html} (`<RESMAKE>`{=html}) MAKEITEM=i_SASH

ON=i_apron_half `<NAME>`{=html} (`<RESMAKE>`{=html})
MAKEITEM=i_apron_half

ON=i_apron_full `<NAME>`{=html} (`<RESMAKE>`{=html})
MAKEITEM=i_apron_full `</spherescript>`{=html}

`<spherescript>`{=html} // // Similar to the MENU example, except adds
conditions to the options. // \[SKILLMENU sm_itemmenu\] Which item would
you like?

ON=i_sword_viking `<NAME>`{=html}

`   TESTIF (<SRC.STR> > 100)             // client must have more than 100 strength to see this option`\
`   SERV.NEWITEM i_sword_viking`\
`   SRC.BOUNCE <NEW.UID>`\
`   RETURN`

ON=i_gold 5000 `<NAME>`{=html}

`   TESTIF (<SRC.BANKBALANCE> < 5000)    // client must have less than 5000gp in their bank to see this option`\
`   SERV.NEWITEM i_gold, 5000`\
`   SRC.BOUNCE <NEW.UID>`\
`   RETURN`

ON=i_backpack \@020, a red backpack

`   TEST 1 i_backpack, 10.0 TAILORING    // client must have 1 backpack and 10% tailoring to see this option`\
`   SERV.NEWITEM i_backpack`\
`   NEW.COLOR = 020`\
`   SRC.BOUNCE <NEW.UID>`\
`   RETURN`

ON=0 Nothing

`   SRC.SYSMESSAGE You get nothing!      // no special function here, this option will always be visible`\
`   RETURN`

`</spherescript>`{=html}

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Definitions](Category:_Definitions "wikilink")
