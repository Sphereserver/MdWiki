# DESCRIPTION

HVAL is the [Hexadecimal](http://en.wikipedia.org/wiki/Hexadecimal)
version of [EVAL](http://wiki.sphere.torfo.org/index.php?title=EVAL), it
returns the given values as HEX and it\'s the default numerical system
used by Sphere and the one that will be used to store the numerical
values you give in most variable types (TAG,VAR,LOCAL\...).

# USAGE

\<spherescript \"darkblue\"\>\[FUNCTION TestHVAL\]
LOCAL.str=`<str>`{=html} Sysmessage=My real STR is `<STR>`{=html} and
when it\'s stored Sphere uses this value \<LOCAL.str\> Sysmessage=I can
also get this value using \<HVAL
`<STR>`{=html}\>`</spherescript>`{=html}
