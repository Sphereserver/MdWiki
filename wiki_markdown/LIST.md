\_\_FORCETOC\_\_

## LIST Functions {#list_functions}

These functions will allow the insertion and referencing of elements in
a list, this is a global property much like VAR and can be referenced or
set globally.

  ----------------------------------------------------------------------- ---------------- ---------------------------------------------------------------------------------------------------------------------------------
  **LIST***.key*                                                          **Read/Write**   **Description**
  **SERV.**[LIST](LIST "wikilink").*xxx*                                  R                Shows elements in LIST.*xxx*
  **SERV.**[LIST](LIST "wikilink").*xxx*.ADD *`<args>`{=html}*            W                Adds *`<args>`{=html}* as a new element in LIST.*xxx*
  **SERV.**[LIST](LIST "wikilink").*xxx*.APPEND *`<args>`{=html},\...*    W                Sets each *`<args>`{=html}* as a new element in LIST.*xxx*
  **SERV.**[LIST](LIST "wikilink").*xxx*.CLEAR                            W                Clears LIST.*xxx*
  **SERV.**[LIST](LIST "wikilink").*xxx*.SET *`<args>`{=html},\...*       W                Clears the list and sets each *`<args>`{=html}* as a new element in LIST.*xxx*
  **SERV.**[LIST](LIST "wikilink").*xxx*.SORT *`<args>`{=html}*           W                Re-orders LIST.*xxx* according to *`<args>`{=html}*. (possible values are: *no args* , *i* , *asc* , *iasc* , *desc* , *idesc*)
  **SERV.**[LIST](LIST "wikilink").*xxx*.*n*                              R                References the *nth* zero based index of the LIST.*xxx*
  **SERV.**[LIST](LIST "wikilink").*xxx*.COUNT                            R                Gets the total number of elements in LIST.*xxx*
  **SERV.**[LIST](LIST "wikilink").*xxx*.*n*.REMOVE                       W                Removes the *nth* element in LIST.*xxx*
  **SERV.**[LIST](LIST "wikilink").*xxx*.*n*.INSERT *`<args>`{=html}*     W                Inserts *`<args>`{=html}* at the *nth* index of LIST.*xxx*
  **SERV.**[LIST](LIST "wikilink").*xxx*.FINDELEM *`<args>`{=html}*       W                Searches LIST.*xxx* for *`<args>`{=html}* starting from the beginning of LIST.*xxx*
  **SERV.**[LIST](LIST "wikilink").*xxx*.*n*.FINDELEM *`<args>`{=html}*   W                Searches LIST.*xxx* for *`<args>`{=html}* starting from the *nth* index of LIST.*xxx*
  **SERV.PRINTLISTS**                                                     R                Prints all LIST*s* and their respective ELEMENTS
  **SERV.CLEARLISTS**                                                     W                Clears all LIST*s*. If used with mask parameter, then it will clear LIST*s* with specified name
  ----------------------------------------------------------------------- ---------------- ---------------------------------------------------------------------------------------------------------------------------------

## Examples

Below are examples of the use of the **LIST** functions:

### Adding to LIST {#adding_to_list}

This example shows how to add elements to your LIST.*xxx* :

`<spherescript>`{=html} \[FUNCTION f_add_to_mylist\]
SERV.LIST.MyList.ADD MyElement1 SERV.LIST.MyList.ADD MyElement2
SERV.LIST.MyList.ADD MyElement3 SERV.LIST.MyList.ADD MyElement4

\...

SERV.LIST.MyList.SET MyElement1,MyElement2,MyElement3,MyElement4 - will
have the same effect as the f_add_to_mylist function above
`</spherescript>`{=html}

### Referencing the LIST {#referencing_the_list}

To reference your LIST.*xxx* :

`<spherescript>`{=html} \[FUNCTION f_show_mylist\] serv.log
\<serv.list.MyList\> `</spherescript>`{=html}

*`displays; "MyElement1","MyElement2","MyElement3","MyElement4"`*

### Referencing Single Elements {#referencing_single_elements}

in the LIST above, in order to reference by index :

`<spherescript>`{=html} serv.list.MyList.0 - outputs \"MyElement1\"
serv.list.MyList.1 - outputs \"MyElement2\" . . .
`</spherescript>`{=html}

### Sorting the LIST {#sorting_the_list}

This example shows how to sort your LIST.*xxx* :

`<spherescript>`{=html} SERV.LIST.MyList.SORT - ascending sort in case
sensitive SERV.LIST.MyList.SORT asc - ascending sort in case sensitive
SERV.LIST.MyList.SORT i - ascending sort in case insensitive
SERV.LIST.MyList.SORT iasc - ascending sort in case insensitive
SERV.LIST.MyList.SORT desc - descending sort in case sensitive
SERV.LIST.MyList.SORT idesc - descending sort in case insensitive
`</spherescript>`{=html}

[Category: Reference
Compendium](Category:_Reference_Compendium "wikilink") [Category:
Scripts](Category:_Scripts "wikilink")
