An object property is a more advanced way of setting or retrieving a tag from an object. This advanced method uses a single function to replace the step of setting the tag's value and the step of getting the tag's value. Object properties also allow other events to occur each time the tag is set or retrieved without the need for repetitive code.

**Example**
Whenever a player kills a creature, they gain a certain amount of gold. Gold is stored as a `tag.` Whenever a player's gold tag is set, we also need to update a global gold variable.

\[FUNCTION gold\] IF !(\<ISEMPTY <ARGS>\>)

`   // The function was passed arguments; therefore, `
`   // the player's gold is increased by the passed amount.`
`   // The global gold count is also increased at the same`
`   // time, eliminating the need for repetitive code.`
`   `TAG0.GOLD` += `<ARGS>
`   `VAR0.TOTAL_GOLD` += `<ARGS>

`ELSE`

`   // There were no arguments which means that the amount`
`   // of gold is being referenced.`
`   `RETURN`<dTAG0.GOLD>`

```
ENDIF
```

Demonstration of what the code does:

`VAR.TOTAL_GOLD` = 5000 // `var.total_gold` is now: 5,000 `SRC.GOLD` += 5000 // `tag.gold` is now: 5,000 // `var.total_gold` is now: 10,000 LOCAL.X = \<`SRC.GOLD`\> // local.x is now: 5,000 `SRC.GOLD` -= 2000
```
// tag.gold is now: 3,000 // var.total_gold is now: 8,000
```

[Category: Articles](Category:_Articles "wikilink")
