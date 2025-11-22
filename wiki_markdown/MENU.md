\_\_FORCETOC\_\_ Menus are a simple way of displaying a selection dialog
to clients. Menus can be shown to players in one of two styles:

-   Text-based
-   Item-based

## Text-Based Menu {#text_based_menu}

A text-based menu simply shows a list of text options the choose from in
a vertical list. The player can select an option and then press a
\"Continue\" button to submit it.

The syntax for defining a text-based menu is as follows:

`[MENU `*`defname`*`]`\
*`title`*\
\
`ON=0 `*`text`*\
`    `*`script`*\
\
`ON=0 `*`text`*\
`    `*`script`*\
\

  ----------- ---------------------------------------------------------------------------------------------------------------------
  **Name**    **Description**
  *defname*   The menu\'s defname.
  *title*     The title of the menu. Properties and references of the object the menu was called on can be accessed.
  *text*      The text to display for the option. Properties and references of the object the menu was called on can be accessed.
  *script*    The script to run when the option is pressed.
  ----------- ---------------------------------------------------------------------------------------------------------------------

## Item-Based Menu {#item_based_menu}

The syntax for an item-based menu is as follows:

`[MENU `*`defname`*`]`\
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
  *baseid*    The item [BASEID](./BASEID.md) to display for the button.
  *hue*       If the @*hue* syntax is used, the item will be displayed in the specified colour.
  *text*      The text to display for the option. Properties of the ITEMDEF that *baseid* refers to can be accessed.
  *script*    The script to run when the button is pressed.
              
  ----------- --------------------------------------------------------------------------------------------------------

## Triggers

When the client selects an option from the menu, the \"ON=*\...*\"
section will be executed, in a similar fashion to how a trigger would
fire.

If the client cancels the menu (by right-clicking it, or for text-based
menus by pressing \"Cancel\"), an \@Cancel trigger will be fired.

In both cases, the following references and arguments are available:

  --------------------------- ------------------------------------------------------------------------------------------------------------
  **Name**                    **Description**
  **[I](./I.md)**       The [character](./Characters.md) or [item](./Items.md) that the MENU function was called from.
  **[SRC](./SRC.md)**   The client operating the menu.
  --------------------------- ------------------------------------------------------------------------------------------------------------

## Examples

`<spherescript>`{=html} // // Displays a menu asking if the player wants
more gold, and creates it // if they select Yes. // \[MENU m_goldmenu\]
You currently have \<SRC.BANKBALANCE\>gp in your account. Would you like
some more gold?

ON=0 Yes

`   SERV.NEWITEM i_gold, 5000`\
`   SRC.BOUNCE <NEW.UID>`\
`   RETURN`

ON=0 No

`   SRC.SYSMESSAGE Ok then!`\
`   RETURN`

`</spherescript>`{=html}

`<spherescript>`{=html} // // Displays a menu asking the player which
item they would like. // \[MENU m_itemmenu\] Which item would you like?

ON=i_sword_viking `<NAME>`{=html}

`   SERV.NEWITEM i_sword_viking`\
`   SRC.BOUNCE <NEW.UID>`\
`   RETURN`

ON=i_gold 5000 `<NAME>`{=html}

`   SERV.NEWITEM i_gold, 5000`\
`   SRC.BOUNCE <NEW.UID>`\
`   RETURN`

ON=i_backpack \@020, a red backpack

`   SERV.NEWITEM i_backpack`\
`   NEW.COLOR = 020`\
`   SRC.BOUNCE <NEW.UID>`\
`   RETURN`

ON=0 Nothing

`   SRC.SYSMESSAGE You get nothing! `\
`   RETURN`

`</spherescript>`{=html}

`<spherescript>`{=html} // // Demonstrates the \@Cancel trigger //
\[MENU m_cancelmenu\] Don\'t cancel this menu!

ON=0 Ok!

`   SRC.SYSMESSAGE Thank you!`\
`   RETURN`

ON=@Cancel

`   SRC.SYSMESSAGE I said don't cancel this menu!`\
`   MENU m_cancelmenu`\
`   RETURN`

`</spherescript>`{=html}

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Definitions](./_Definitions.md)
