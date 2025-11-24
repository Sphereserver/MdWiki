# DESCRIPTION

HVAL is the [Hexadecimal](http://en.wikipedia.org/wiki/Hexadecimal)
version of [EVAL](http://wiki.sphere.torfo.org/index.php?title=EVAL), it
returns the given values as HEX and it's the default numerical system
used by Sphere and the one that will be used to store the numerical
values you give in most variable types (TAG,VAR,LOCAL...).

## Warning
- The defname numeric value has a different byte order now. Previously, you might have used `<hval s_clumsy&(~0ce000000)>` to retrieve a spell number. This no longer works as the structure of the `hval` return has changed. Use `RESOURCEINDEX` instead.

# USAGE

\<spherescript "darkblue"\>\[FUNCTION TestHVAL\] LOCAL.str=<str>
Sysmessage=My real STR is <STR> and when it's stored Sphere uses this
value \<LOCAL.str\> Sysmessage=I can also get this value using \<HVAL
<STR>\></spherescript>
