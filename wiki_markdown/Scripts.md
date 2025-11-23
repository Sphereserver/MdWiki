Scripts are used to control what actions take place when certain things
happen. For example a script can be used to control what happens when a
player double clicks a certain object. Through the use of scripts,
Sphere can be customised in a very particular way that should meet the
needs of virtually any server.

The [Definitions](./CategoryDefinitions.md) category describes
how scripts can be used to define the basic properties of objects, and
the [Objects](./CategoryObjects.md) category describes each of
the different types of object and how they can be manipulated by
scripts.

The pages in this category describe more general information about
scripts, such as global properties and functions that are available from
any script in Sphere, as well as the arguments that are available when
creating scripting functions and triggers.

## Scripts

[Category: Reference Compendium](./CategoryReference_Compendium.md)

## Notes
- Hardcoded speech commands such as 'I must consider my sins', 'I resign from my guild', and 'I resign from my town' have been moved to scripts. It is highly recommended to update your scripts accordingly, or these commands will cease to function.
- The `ADD` command no longer displays a console error when provided with an invalid argument; however, the sysmessage is still displayed.
- The `.ADD` command now accepts a second parameter to specify the amount of the item to create (e.g., `.add i_gold, 500`).
