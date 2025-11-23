This function is called from CItemMulti::Multi_Create when multis do their checks to be placed.

## Parameters

-   `return 0`: Use default checks (which values may be modified with the below locals).
-   `return 1`: Prevents the multi from being placed.
-   `return 6`: Allows the multi to be placed without default placement checks.

## Local Variables

-   `local.check_BlockRadius = -1, 1, -1, 1` (Default: an area of +1 in each direction)
-   `local.check_MultiRadius = 0, -5, 0, -5` (Default: 5 tiles in both North and South)
    -   Values are: West, North, East, South
-   `local.id`: Read Only (e.g., `m_xxx`)
-   `local.p`: Read Only (position)