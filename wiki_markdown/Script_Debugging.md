So you've got a problem with a script and you don't know where to
turn? Or everyone you've spoken to doesn't have the answers you seek?
You're about to start pulling out your hair, you feel alone and lost,
and no one can seem to help you. Well worry no more, you're about to
help yourself! Let's talk about debugging your script

We'll go through some examples here to explain how one could get
helpful information that will lead them to their solutions. Each
situation will have it's own unique methods to help you use the tools
at your disposal to fix the problem, or guide you to finding out more
helpful information.

## Problems Understanding A Trigger {#problems_understanding_a_trigger}

Uncertain how a trigger works?

This is a great example from MalucoBeleza that illustrates the concept
of logging out your results to the console for further insight into what
objects a trigger is referencing. This can help you make sure that you
are referencing the right object in game and that whatever follows will
behave as expected.

Let's say you want to use a trigger that will fire when you kill
someone, and when you kill that person you want to give the killer some
experience points. You need to reference both the person being killed
and the person that killed them.

The trigger in this example is [@Kill](./Kill.md). One may think
that they will use the default object I as the killer and that SRC will
be the person being killed. or that ACT would be the person being
killed. But it is best not to assume any of these triggers will use any
object reference the same as another, or even the same as a similar
trigger. The best practice is to take yourself to the Spherewiki (as YOU
already have) and pull up the trigger you are looking for under the
Reference Compendium > [Objects](./Objects.md) >
[Characters](./Characters.md), this will give you a very good idea
of what references you can make in that trigger. Once you have that
information you can begin to see what you are able to work with and how
you can work with it.

As MalucoBeleza points out, this practice is required to get proper
knowledge to work with a trigger

When dealing with a trigger that is new to you... its essential to
check the wiki and do tests like this:

`ON=@Kill`
` SERV.LOG NAME: <NAME>`{=html}
` SERV.LOG I.NAME: <I.NAME>`
` SERV.LOG SRC.NAME: <SRC.NAME>`
` SERV.LOG ARGO.NAME: <ARGO.NAME>`
` SERV.LOG <NAME>`{=html}` (<UID>`{=html}`) HAVE JUST KILLED <ARGO.NAME> (<ARGO>`{=html}`)

Debugging is also a great tool when you are performing calculations.
Let's say that you want to create your own combat system, such as:

`ON=@Hit`
`   SERV.LOG <NAME>`{=html}` HAVE JUST HIT <SRC.NAME>`
`   IF ( <WEAPON>`{=html}` )`
`       SERV.LOG A WEAPON WAS USED: <WEAPON.NAME>`
`       SERV.LOG <WEAPON.NAME>'S DAMAGE IS <WEAPON.DAM.LO> - <WEAPON.DAM.HI>`
`   ELSE`
`       SERV.LOG NO WEAPON WAS USED.`
`       SERV.LOG <NAME>`{=html}`'S DAMAGE IS <DAM>`{=html}
`   ENDIF`
`   `
`   SERV.LOG DAMAGE STARTED AS <ARGN1>`{=html}
`   `
`   SERV.LOG THE SKILL USED IN THIS ATTACK IS <ACTION>`{=html}
`   IF ( <ACTION>`{=html}` == WRESTLING) || ( <ACTION>`{=html}` == MACEFIGHTING)`
`       ARGN1 = <EVAL <ARGN1>`{=html}` + ( <STR>`{=html}`/8)> //APPLY YOUR FORMULA HERE`
`   `
`   ELIF ( <ACTION>`{=html}` == ARCHERY) || ( <ACTION>`{=html}` == FENCING)`
`       ARGN1 = <EVAL <ARGN1>`{=html}` + ( <DEX>`{=html}`/8)>`
`   `
`   ELIF ( <ACTION>`{=html}` == SWORDSMANSHIP)`
`       ARGN1 = <EVAL <ARGN1>`{=html}` + ( <DEX>`{=html}`/16) + ( <STR>`{=html}`/16)>`
`   `
`   ENDIF`
`   `
`   SERV.LOG DAMAGE AFTER STATS BONUS ACCORDING TO THE SKILL IS <ARGN1>`{=html}
`   `
`   IF (<SRC.ISPLAYER>) //PLAYER HITS ANOTHER PLAYER`
`       SERV.LOG THE ARMOR OF THE DEFENDANT IS <SRC.ARMOR>`
`       LOCAL.DAMAGE_REDUCTION = <EVAL <SRC.ARMOR>/20> //APPLY YOUR FORMULA HERE`
`   `
`   ELSE //PLAYER HITS A NPC`
`       SERV.LOG THE ARMOR OF THE DEFENDANT IS <SRC.AC>`
`       LOCAL.DAMAGE_REDUCTION = <EVAL <SRC.AC>/20> //APPLY YOUR FORMULA HERE`
`   `
`   ENDIF`
`   ARGN1 -= <LOCAL.DAMAGE_REDUCTION>`
`   SERV.LOG AFTER DAMAGE REDUCTION OF <LOCAL.DAMAGE_REDUCTION>, DAMAGE IS <ARGN1>`{=html}

## Console Errors Regarding Scripts {#console_errors_regarding_scripts}

You are getting errors on your console, and it's telling you about a
script but you aren't quite sure what to do. Let's see one as an
example :

`00:17:ERROR:(i_dye_tubs.scp,52)Range isn't closed by a '}' character.`

Okay from this error we can see the filename 'i_dye_tubs' and the line
number is 52. The error is that the 'Range isn't closed by a '}'
character.' so let's go see what this line looks like and what we the
appropriate line fix is:

So here's what line 52 from i_dye_tubs.scp looks like :

`color={047e 049a`

We can see above that its missing a } at the end just like the console
error notified us about. The fix is to simply add the missing }.

this is a very elementary example but this explains the process of
breaking down a console error. It's always the same for these script
errors : "filename, line number, error description". With large
complicated systems paying attention to the exact nature of your console
error will guide you towards figuring out how to fix it.

## Notes
- The Garbage Collection report now includes the script file name and line number where objects (created via `NEWITEM`, `NEWNPC`, `NEWSUMMON`, `NEWDUPE`, `DUPE`, `ITEM`, `ITEMNEWBIE`) were created, aiding in debugging.