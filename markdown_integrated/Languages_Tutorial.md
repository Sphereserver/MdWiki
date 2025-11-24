```{=mediawiki}
{{Languages|Languages_Tutorial}}
```
The script below is in no way complete, all it does at the moment is
retransmit what the player said (from the player\'s point of view
nothing happened). It is up to you to add what you want to the script
and make it work the way you want to.

In your *sphere.ini* look for the line:

`<spherescript>`{=html}SpeechSelf=spk_player // make sure it is equal to
spk_player`</spherescript>`{=html}

In sphere_speech.scp you\'ll find the **\[SPEECH spk_player\]** block.
Under it add the code as shown below:

`<spherescript>`{=html}\[SPEECH spk_player\] ON=\*

`   IF !(``<ISGM>`{=html}`)`\
`       VAR.MODE = ``<ARGN1>`{=html}\
`       CAPTURE_SPEECH ``<ARGS>`{=html}\
`       ARGN1 = talkmode_prompt`\
`   ENDIF`\
`   RETURN 0``</spherescript>`{=html}

*talkmode_prompt* prevents speech from appearing above the player\'s
head, but allows npc\'s to react to things like \"buy\" and other
commands.

Next, in a seperate file you can script the capture_speech function.
Here\'s the outline of what it looks like:

`<spherescript>`{=html}\[FUNCTION capture_speach\] REF1 = `<UID>`{=html}

// Get player speach modes LOCAL.MODE = \<VAR.MODE\>

// Get hearing distance based on speech mode IF (\<LOCAL.MODE\> ==
talkmode_system)

`   LOCAL.HEAR_DIST = 15    // normal hearing distance  `

ELSEIF (\<LOCAL.MODE\> == talkmode_yell)

`   LOCAL.HEAR_DIST = 30    // yell hearing distance`

ELSEIF (\<LOCAL.MODE\> == talkmode_whisper)

`   LOCAL.HEAR_DIST = 2     // whisper hearing distance`

ENDIF

LOCAL.SENTENCE = `<ARGS>`{=html} // do things with your sentence here

FORCLIENTS \<LOCAL.HEAR_DIST\>

`    // here you can define who hears what, changing the sentence to whatever you want, changing the color ect..`\
`    REF1.TRYSRC ``<UID>`{=html}` MESSAGEUA 0 0 0 0 <LOCAL.SENTENCE>`

ENDFOR`</spherescript>`{=html}

Good luck!

[Category:Articles](./Articles.md)
