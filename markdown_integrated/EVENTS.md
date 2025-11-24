```{=mediawiki}
{{Languages|EVENTS}}
```
\_\_FORCETOC\_\_ An EVENTS definition contains a set of trigger scripts
which can be attached to characters. There are different properties that
can be used to attach an event block to a character or set of
characters:

-   [Character definitions](./CHARDEF.md) via their
    [TEVENTS](./TEVENTS.md) property
-   [Characters](./Characters.md) via their
    [EVENTS](./EVENTS.md) property,
-   All [players](./CharactersPlayers.md) via the
    [EVENTSPLAYER](./EVENTSPLAYER.md) setting in Sphere.ini.
-   All [NPCs](./CharactersNPCs.md) via the
    [EVENTSPET](./EVENTSPET.md) setting in Sphere.ini

## Syntax

The syntax for defining an event is:

`[EVENTS `*`defname`*`]`\
`ON=`*`trigger_name`*\
`    `*`script`*\
\
`ON=`*`trigger_name`*\
`    `*`script`*\
\

Any number of triggers can be handled by one [EVENTS](./EVENTS.md)
definition, however it is not possible to handle the same trigger twice
without using multiple definitions.

The trigger name can be the name of any [character
trigger](./CharactersTriggers.md). The return value from the
script can affect Sphere\'s hardcoded behaviour in different ways. See
the documentation for the trigger to discover what parameters are passed
in to each trigger and what the return values do.

## Examples

`<spherescript>`{=html} // // When attached to a character, character
speaks when double-clicked // \[EVENTS e_exampleevent\] ON=@DClick SAY I
have been double clicked! RETURN 2 `</spherescript>`{=html}

`<spherescript>`{=html} // // e_Human_Environ from default script pack
// Attached to NPCs to make them light a torch during the night //
\[EVENTS e_Human_Environ\] ON=@EnvironChange

`   IF (``<FLAGS>`{=html}` & statf_war)`\
`       RETURN 0`\
`   ENDIF`\
`   IF !(<SECTOR.ISDARK>) || (``<FLAGS>`{=html}` & statf_nightsight)`\
`       IF (<FINDLAYER.layer_hand2>)`\
`           IF (<FINDLAYER.layer_hand2.TYPE> == t_light_lit)`\
`               FINDLAYER.layer_hand2.BOUNCE`\
`           ENDIF`\
`       ENDIF`\
`       RETURN 0`\
`   ENDIF`\
`   // already have a lit light ?`\
`   IF (<FINDLAYER.layer_hand2>)`\
`       IF (<FINDLAYER.layer_hand2.TYPE> == t_light_lit)`\
`           RETURN 0`\
`       ENDIF`\
`   ENDIF`\
`   // try to use a torch or light source if i have one. (and it's dark)`\
`   IF (<FINDTYPE.t_light_out>)`\
`       FINDTYPE.t_light_out.EQUIP`\
`       FINDTYPE.t_light_out.USE`\
`   ENDIF`\
`   RETURN 0`

`</spherescript>`{=html}

[Category: Reference
Compendium](./_Reference_Compendium.md) [Category:
Definitions](./_Definitions.md)
