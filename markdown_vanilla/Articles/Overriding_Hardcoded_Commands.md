```
For the longest time, we've all been needing or wanting to replace that stupid teleport command to something that looks and sounds much cooler, or change the way .KILL kills you. With the release of 56b came a useful feature found in your sphere.ini called **CommandTrigger**.

**How it works:**
If enabled, when a command is used by a player in the game, Sphere calls the function defined by the "CommandTrigger" setting BEFORE it actually executes the command in question.

Open up your sphere.ini file and scroll down to the **Client Management** section. Towards the bottom of the section, you will see this:

// Function to call if client is executing a command to override the default. //CommandTrigger=f_oncommand

If you want to override a default command, uncomment the second line. Make sure it looks just like that. Now go make a new file in your scripts and create a new function called "f_oncommand" This is the function you will use to make your changes. Now, whenever ANYONE executes a command, they will also execute the function f_oncommand, before the command is even run. (it doesnt HAVE to be f_oncommand, justmake sure that the function matches the setting in the .ini file)

Now, when the server calls **f_oncommand**, the original command will be stored in ARGS. So say you want to prevent the .TELE command from ever being used, you'd do this:

\[FUNCTION f_oncommand\] IF (STRCMPI("<ARGS>", "TELE") == 0) // if command was .tele

`   SYSMESSAGE Tele command has been disabled.`
`   RETURN 1 // stop default command`

ELSE // if command was not .tele

`   RETURN 0 // allow default command`

ENDIF // end of if block

That's pretty much it... With this setting and function, you can pretty much change any of the hardcoded commands. You can even completely re-script the commands, maybe you want .KILL to actually resurrect the player, or something like that... it's all possible!

[Category:Articles](Category:Articles "wikilink")
```
