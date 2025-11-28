Bitwise operations are used to perform an action on the bits (the 1's
and 0's) of a number.

In this article a "binary" formatted number (which represents the "bits"
of a number) will be written with a <sup>2</sup>... and a decimal number
with a <sup>10</sup>

## Limitations

In Sphere, numbers are stored in something called a "DWORD". The largest
number a DWORD can store is constrained by the fact that a DWORD is 32
bits wide. That means the largest number it can store is 2^32-1.

- In Binary that's 11111111111111111111111111111111.
- In Hex it's FFFFFFFF.
- In Decimal that's 4294967295.

To store a 'signed' number in a DWORD (in other words, a number that can
be positive or negative), the first bit is used to indicate the sign (a
1 is negative). Which means the largest 'signed' positive number is
2^31-1

- In Binary that's 01111111111111111111111111111111.
- In Hex it's 7FFFFFFF.
- In Decimal that's 2147483647.

In sphere script language, the EVAL function outputs a signed DWORD, and
the UVAL outputs an unsigned DWORD.

`[FUNCTION Mathtest]`  
`LOCAL.Number0=2147483647`  
`LOCAL.Number1=4294967295`  
`LOCAL.Number2=8589934588`  
`SERV.LOG eval0=<EVAL <LOCAL.Number0>> eval1=<EVAL <LOCAL.Number1>> eval2=<EVAL <LOCAL.Number2>>`  
`SERV.LOG uval0=<UVAL <LOCAL.Number0>> uval1=<UVAL <LOCAL.Number1>> uval2=<UVAL <LOCAL.Number2>>`

The output of this test is:

`13:37:(test.scp,10)eval0=2147483647 eval1=-1 eval2=-4`  
`13:37:(test.scp,11)uval0=2147483647 uval1=4294967295 uval2=4294967292`

Notes:

- The output is limited to align with the limitation of the DWORD
  itself.
- Since there are 32 "bits" in a DWORD, there can only be 32 flags in a
  set.
- Be careful when manipulating flags using EVAL, because the 32nd flag
  could get lost.

## Flags

In the Sphere server, quite a few concepts are implemented using
"flags". You can see examples of flags being defined in the Sphere.ini
file, or the sphere_defs.scp files. For example:

`[DEFNAME attr_flags]`  
`attr_identified       01`  
`attr_decay            02`  
`attr_newbie           04`  
`attr_move_always      08`  
`attr_move_never      010`  
`attr_magic           020`  
`attr_owned           040`  
`attr_invis           080`  
`attr_cursed         0100`  
`attr_cursed2        0200`  
`attr_blessed        0400`  
`attr_blessed2       0800`  
`attr_forsale       01000`  
`attr_stolen        02000`  
`attr_can_decay     04000`  
`attr_static        08000`  
`attr_exceptional  010000`  
`attr_enchanted    020000`  
`attr_imbued       040000`  
`attr_questitem    080000`  
`attr_insured     0100000`  
`attr_nodrop      0200000`  
`attr_notrade     0400000`  
`attr_lockeddown  0800000`  
`attr_secure     01000000`

This technique is a very efficient way to store a number of Boolean
values using as little memory as possible. Let's tip that list on it's
side and chart the first 8 flags:

|  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|
| Flag Name: | attr_invis | attr_owned | attr_magic | attr_move_never | attr_move_always | attr_newbie | attr_decay | attr_identified |
| Flag Position | 8th position | 7th position | 6th position | 5th position | 4th position | 3rd position | 2nd position | 1st position |
| Binary Number: | 10000000 | 01000000 | 00100000 | 00010000 | 00001000 | 00000100 | 00000010 | 00000001 |
| Hex Number: | 080 | 040 | 020 | 010 | 08 | 04 | 02 | 01 |
| Decimal Number: | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

Now you can probably see the pattern... the numbers
1,2,4,8,16,32,64,128,... are all multiples of 2 and they are special
because they all have a single 1 in them when converted to binary. To
enable or disable an individual flag on an object is accomplished using
the bitwise operators AND, OR, XOR, and NOT.

## The OR Operator (inclusive OR): \|

A *bitwise OR* takes two bit patterns of equal length and performs the
logical *inclusive OR* operation on each pair of corresponding bits.
When you perform this operation, the result in each position is 0 if
both bits are 0, and the result is 1 if either (or both) the bits
were 1. For example:

`   0101 (decimal 5)`  
`OR 0011 (decimal 3)`  
` = 0111 (decimal 7)`

In Sphere, this technique is commonly used to set a *flag* in a
register, while preserving the existing flags. So, 0010 (decimal 2) can
be considered a set of four flags, where the first, third, and fourth
flags are clear (0) and the second flag is set (1). The fourth flag may
be set by performing a bitwise OR between this value and a bit pattern
with only the fourth bit set:

`   0010 (decimal 2)`  
`OR 1000 (decimal 8)`  
` = 1010 (decimal 10)`

In the following example Sphere code, we create a new object, then set
that objects flags to equal 010, then we enable the 4th flag as well:

`SERV.NEW=i_log`  
`ATTR=010`  
`ATTR|=01000`

...that same example, using flag names:

`SERV.NEW=i_log`  
`ATTR=attr_decay`  
`ATTR|=attr_move_always`

## The AND Operator (logical and): &

A *bitwise AND* takes two equal-length binary representations and
performs the *logical AND operation* on each pair of the corresponding
bits, by multiplying them. If both bits in the compared position are 1,
the bit in the resulting binary representation is 1 (1 × 1 = 1);
otherwise, the result is 0 (1 × 0 = 0 and 0 × 0 = 0). For example:

`    0101 (decimal 5)`  
`AND 0011 (decimal 3)`  
`  = 0001 (decimal 1)`

The operation may be used to determine whether a particular bit is set
(1) or clear (0). For example, given a bit pattern 0011 (decimal 3), to
determine whether the second bit is set we use a bitwise AND with a bit
pattern containing 1 only in the second bit:

`    0011 (decimal 3)`  
`AND 0010 (decimal 2)`  
`  = 0010 (decimal 2)`

Because the result 0010 is non-zero, we know the second bit in the
original pattern was set. This concept is often called *bit masking*. In
Sphere, this is often used in an IF statement to check if a specific
flag is enabled or not. For example, the sphere code to check if an
object is identified is done by applying a AND of the object's ATTR to
the attr_identified flag like this:

`IF (`<ATTR>`&attr_identified)`

## The XOR Operator (exclusive OR): ^

A *bitwise XOR* takes two bit patterns of equal length and performs the
*logical exclusive OR* operation on each pair of corresponding bits. The
result in each position is 1 if only the first bit is 1 or only the
second bit is 1, but will be 0 if both are 0 or both are 1. In this we
perform the comparison of two bits, being 1 if the two bits are
different, and 0 if they are the same. For example:

`    0101 (decimal 5)`  
`XOR 0011 (decimal 3)`  
`  = 0110 (decimal 6)`

The bitwise XOR is often used to invert selected bits in a register
(also called toggle or flip). Any bit may be toggled by XORing it
with 1. For example, given the bit pattern 0010 (decimal 2) the second
and fourth bits may be toggled by a bitwise XOR with a bit pattern
containing 1 in the second and fourth positions:

`    0010 (decimal 2)`  
`XOR 1010 (decimal 10)`  
`  = 1000 (decimal 8)`

## The NOT Operator (bitwise not): !

The *bitwise NOT*, or complement, is an operation that performs a
logical negation on each bit, forming the *ones' complement* of the
given binary value. Bits that are 0 become 1, and those that are 1
become 0. For example:

`NOT 0111  (decimal 7)`  
`  = 1000  (decimal 8)`

The bitwise complement is equal to the two's complement of the value
minus one. If two's complement arithmetic is used, then:

`NOT x = −x − 1.`

For unsigned integers, the bitwise complement of a number is the "mirror
reflection" of the number across the half-way point of the unsigned
integer's range. For example, for 8-bit unsigned integers, NOT x = 255 -
x, which can be visualized on a graph as a downward line that
effectively "flips" an increasing range from 0 to 255, to a decreasing
range from 255 to 0.

## Left and right shift
