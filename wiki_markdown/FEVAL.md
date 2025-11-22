# Description

FEval is a function that returns the given value treating the last
number as a decimal and removing it, the best example is to retrieve
your skill points without decimals.

# Usage

\<spherescript \"darkblue\"\> \[function ShowAlchemy\] alchemy=99.9 say
Alchemy is: \<feval `<alchemy>`{=html}\> // This will say \'Alchemy is:
99\', removing the last number (.9).`</spherescript>`{=html}
