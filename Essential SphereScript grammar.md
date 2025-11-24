## Essential SphereScript Grammar Rules

1. Data Types and Variables
SphereScript is weakly and dynamically typed, meaning variable types are determined at runtime, and you generally don't declare the type explicitly.
    - Numeric: Integers (1, -500) are standard. SphereScript handles large numbers, often used for item IDs or world coordinates.
    - String: Text data enclosed in single quotes ('text') or sometimes double quotes ("text"), though single quotes are most common for literal strings.
    - References (Objects): Most powerful type. Variables often hold references to in-game entities like items (i_staff), characters (c_guard), or accounts. References allow you to access the properties and execute methods (commands) on those objects. Strings or numbers are not objects.
    - Arrays: There is not the concept of arrays. As a workaround, one could use a comma separated value string, or the SERV.LIST object.

2. Core Syntax and Execution
    - Separators: All script commands, commands, and expressions are separated by a newline. There is typically no semicolon required at the end of a line.
    - Comments: Comments are lines beginning with a double forward slash (//). Also C-style block comments (/* */) are valid.
     - Script Labels (Triggers): Script execution is primarily driven by event labels or "triggers," which start with @. These define the entry points for the server to run custom code.
    - Assignment: The = operator assigns a value to a variable or property.
    - Expressions (Brackets): Expressions (calculations, data retrieval) must be enclosed in angle brackets (<>).

3. Property and Method Access
SphereScript uses dot notation (.) to access properties and execute methods (commands) on objects.
    - Properties: Directly access object attributes (e.g., SRC.hp, TARG.p).
    - Methods (Commands): Commands are functions executed on an object (e.g., SRC.say 'Hello', I.move 1).
Understanding the grammar starts with knowing who the script is running on (SRC) and what other objects it can reference (TARG, I, etc.).
