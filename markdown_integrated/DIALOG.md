```{=mediawiki}
{{Languages|DIALOG}}
```
\_\_FORCETOC\_\_ Dialogs are a more advanced form of user interface
whose layout can be completely customised.

## Syntax

The definition of a dialog consists of *three* different blocks of
script; a layout, a list of text strings used in the dialog and a
buttons section which handles button responses from the client.

### Layout

The layout section of the dialog defines how the dialog will look to
clients.

`[DIALOG `*`defname`*`]`\
*`x, y`*\
*`script`*\

  ----------- --------------------------------------------------
  **Name**    **Description**
  *defname*   The dialog\'s defname.
  *x, y*      The screen coordinates to display the dialog at.
  *script*    The dialog\'s layout script.
  ----------- --------------------------------------------------

The script text can be a complete script that is executed in the same
way as a function or trigger script, and can even contain conditional
statements to display different layouts to different clients if desired.
The default object is the [character](./Characters.md) or
[item](./Items.md) that the dialog has been called upon, and
[SRC](./SRC.md) is the [client](./CharactersClients.md) who
is viewing the dialog. If the dialog ends with a \"RETURN 1\" then
Sphere will cancel displaying the dialog.

In addition to the usual functions, properties and references you would
have access to in a normal script, there are also functions that place
elements on to the dialog. The following table lists all elements that
can be used:

  ----------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                                                                                                                **Description**
  [button](./button.md) *x y gump_down gump_up is_pressable page id*                                                Places a button on to the page
  [buttontileart](./buttontileart.md) *x y gump_down gump_up is_pressable page id tile_id tile_hue tile_x tile_Y*   Places a button on to the page, with an item image placed over the top as part of the button.
  [checkbox](./checkbox.md) *x y gump_check gump_uncheck initial_state id*                                          Places a checkbox on to the page.
  [checkertrans](./checkertrans.md) *x y width height*                                                              Adds a transparent area of the dialog.
  [croppedtext](./croppedtext.md) *x y width height colour text_index*                                              Places some text on to the page that wraps to specified boundaries.
  [dcroppedtext](./dcroppedtext.md) \'\'x y width height colour text                                                Places some text on to the page that wraps to specified boundaries. Accepts dynamic coordinates relative to [dorigin](./dorigin.md) using **-**, **+**, **\*** prefixes.
  [dorigin](./dorigin.md) *x y*                                                                                     Sets the origin coordinates for dynamically positioned elements.
  [dhtmlgump](./dhtmlgump.md) *x y width height has_background has_scrollbar text*                                  Places some HTML text on to the page. Accepts dynamic coordinates relative to [dorigin](./dorigin.md) using **-**, **+**, **\*** prefixes.
  [dtext](./dtext.md) *x y colour text*                                                                             Places some text on to the page. Accepts dynamic coordinates relative to [dorigin](./dorigin.md) using **-**, **+**, **\*** prefixes.
  [dtextentry](./dtextentry.md) *x y width height colour id text*                                                   Places a text entry field on to the page where the client can enter text. Accepts dynamic coordinates relative to [dorigin](./dorigin.md) using **-**, **+**, **\*** prefixes.
  [dtextentrylimited](./dtextentrylimited.md) *x y width height colour id limit text*                               Places a text entry field on to the page where the client can enter a limited amount of text. Accepts dynamic coordinates relative to [dorigin](./dorigin.md) using **-**, **+**, **\*** prefixes.
  [group](./group.md) *id*                                                                                          Defines a new group ID, for grouping sets of radio buttons.
  [gumppic](./gumppic.md) *x y gump hue*                                                                            Places a gump on to the page.
  [gumppictiled](./gumppictiled.md) *x y width height gump*                                                         Tiles a gump over an area of the page.
  [htmlgump](./htmlgump.md) *x y width height text_index has_background has_scrollbar*                              Places some HTML text on to the page.
  [noclose](./noclose.md)                                                                                           Prevents the dialog from being closed when right-clicked.
  [nodispose](./nodispose.md)                                                                                       Prevents the dialog from being closed by the \"Close Dialogs\" macro.
  [nomove](./nomove.md)                                                                                             Prevents the dialog from being moved around the screen.
  [page](./page.md) *num*                                                                                           Begins defining page *num* of the dialog. (page 0 content is shown on all pages)
  [radio](./radio.md) *x y gump_check gump_uncheck initial_state id*                                                Places a radio button on to the page.
  [resizepic](./resizepic.md) *x y gump width height*                                                               Places a multi-part *gump* on to the page, often used for dialog backgrounds.
  [picinpic](./picinpic.md) *x y gump spritex spritey width height*                                                 Used to add sprites pictures on dialogs.
  [text](./text.md) *x y colour text_index*                                                                         Places some text on to the page.
  [textentry](./textentry.md) *x y width height colour id text_index*                                               Places a text entry field on to the page where the client can enter text.
  [textentrylimited](./textentrylimited.md) *x y width height colour id text_index limit*                           Places a text entry field on to the page where the client can enter a limited amount of text.
  [tilepic](./tilepic.md) *x y item_id*                                                                             Places an item image on to the page.
  [tilepichue](./tilepichue.md) *x y item_id hue*                                                                   Places a coloured item image on to the page.
  [tooltip](./tooltip.md) *cliloc_id \@args*                                                                        Places a tooltip on to the page (multiple arguments separated by @).
  [xmfhtmlgump](./xmfhtmlgump.md) *x y width height clilod_id has_background has_scrollbar*                         Places some localised HTML text on to the page.
  [xmfhtmlgumpcolor](./xmfhtmlgumpcolor.md) *x y width height cliloc_id has_background has_scrollbar colour*        Places some localised HTML text on to the page with the specified colour.
  [xmfhtmltok](./xmfhtmltok.md) *x y width height has_background has_scrollbar colour cliloc_id \@args@*            Places some localised HTML text on to the page, with arguments to the cliloc (multiple arguments separated by @).
  ----------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Text

The text section of the dialog simply lists the different text strings
used in the dialog\'s layout. When using dialog elements that represent
text, such as *text* or *htmlgump*, an index into the TEXT block will be
specified so that the client knows which text to actually display on
that dialog element. This dialog section is optional, and may be omitted
if there are no text elements on the dialog or if the newer dialog text
elements, such as *dtext* or *dhtmlgump*, are used because their text
string is specified in the layout and Sphere will automatically populate
the TEXT block for you.

`[DIALOG `*`defname`*` TEXT]`\
*`string1`*\
*`string2`*\
*`string3`*\

### Buttons

This section contains button triggers that fires when the client presses
a certain button on the dialog. There are two ways that a button press
can be handled, the syntaxc for both is shown below:

`[DIALOG `*`defname`*` BUTTON]`\
`ON=`*`button_id`*\
`    `*`script`*\
\
`ON=`*`button_id_start`*` `*`button_id_end`*\
`    `*`script`*\

The first \"`ON=`*`button_id`*\" will handle the button press for the
button with the matching ID, the second will handle any button press
where the ID is between *button_id_start* and *button_id_end*.

**Note:** If the client cancels the dialog by right clicking it, the
trigger for button 0 will be fired.

Inside the button triggers there are some arguments passed in that
aren\'t available in normal functions and triggers. The following table
describes each argument passed in to dialog button triggers:

  --------------------------------------- ----------------------------------------------------------------------------------
  **Name**                                **Description**
  [ARGCHK](./ARGCHK.md)             Returns the number of selected checkboxes/radio buttons.
  [ARGCHK](./ARGCHK.md)\[*id*\]     Returns 1 if the checkbox/radio button with a specified ID was pressed down.
  [ARGCHKID](./ARGCHKID.md)         The ID of the first selected checkbox/radio button, or -1 if none were selected.
  [ARGN1](./ARGN1.md)               The ID of the button pressed.
  [ARGTXT](./ARGTXT.md)             Returns the number of text fields submitted.
  [ARGTXT](./ARGTXT.md)\[*id*\]\]   Returns the submitted text for the text field with the specified ID.
  --------------------------------------- ----------------------------------------------------------------------------------

## Examples

`<spherescript>`{=html} // // Simple travel dialog from default script
pack. // \[DIALOG d_TravelTown\] 0, 0 resizepic 0 0 3600 215 200 page 0
text 40 17 0 0 text 40 37 1152 1 text 40 57 1152 2 text 40 77 1152 3
text 40 97 1152 4 text 40 117 1152 5 text 40 137 1152 6 text 40 157 0 7
button 20 40 1209 1210 1 0 1 button 20 60 1209 1210 1 0 2 button 20 80
1209 1210 1 0 3 button 20 100 1209 1210 1 0 4 button 20 120 1209 1210 1
0 5 button 20 140 1209 1210 1 0 6

\[DIALOG d_TravelTown TEXT\] Which Town? Britain Serpent\'s Hold Cove
Vesper Bucaneer\'s Den Papua

\[DIALOG d_TravelTown BUTTON\]

ON=0

`   SYSMESSAGE Menu Aborted`

ON=1 //BRITAIN

`   SRC.GO 1427,1697,0`

ON=2 //SERPENTS HOLD

`   SRC.GO 3009,3363,15`

ON=3 //COVE

`   SRC.GO 2264,1202,0`

ON=4 //VESPER

`   SRC.GO 2892,686,0`

ON=5 //BUCANEER\'S DEN

`   SRC.GO 2733,2160,0`

ON=6 //PAPUA

`   SRC.GO=5726,3205,-3`

`</spherescript>`{=html}

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Definitions](./_Definitions.md)
