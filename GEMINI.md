# About the repo

We are porting an old MediaWiki for **SphereServer** main features and scripting language (**SphereScript**).
We have fetched and converted the old content to **GitHub Flavored Markdown (GFM)** and linked the pages.
The `Changelog.txt` file contains changes to the C++ core and SphereScript features relevant to end-users (game masters, scripters, admins). Information relevant for maintainers is stored elsewhere.

---

# General Rules

- Do **not** add information about implementation details or inner workings relevant only to C++ source code contributors.
- **Preserve Case:** SphereScript keywords/acronyms are often **UPPERCASE** or **PascalCase**.
- **Tool Parameter Constraint:** When using any file manipulation tool (like `WriteFile`, `ReadFile`, or `EditFile`), you **must** explicitly include the `file_path` argument, even if the file is already referenced in context.
- **Progress Tracking:**
    - Every time you log a block of output (an answer of yours), execute the following shell command **immediately before the output** to print the **client local time**: `(Current time is $(date +%T.%3N))`

## File Handling & Context Management (Critical)

- Mandatory Editing Tool: For ALL file content modifications (replacements, insertions, or deletions), you MUST use the **dedicated Python script**, `agent_helpers/file_editor.py`, instead of the built-in Edit tool.
Usage: `python3 file_editor.py <filepath> --old "old_string" --new "new_string"`
- If appropriate, prefer using Unix shell commands to offload work to the client invoking the agent (awk, cat, diff, find, grep, etc)
- Use your Replace tools **only** if you can't manage to make file_editor.py to work, or if more suitable shell commands didn't work.
- **Context Isolation & Token Management:** **NEVER** read an entire file unless absolutely necessary. After successfully performing an edit on a file, **do not read that file again** in the current batch unless it is the explicit target of a subsequent operation. Assume the change was successful and avoid polluting the context with redundant file content.
- **Edit Tool Reliability:**
    - Before performing any edit on `@filename`, use the **most scoped method possible** (e.g., `grep` or a targeted `read_file` with line/range parameters, if available) to fetch **only the specific block** containing your intended `old_string`. Only fall back to reading the entire file if a targeted search fails.
    - When using the edit tool, if the edit fails (e.g., "0 occurrences found"), **do not try to correct the `old_string` and retry.** Instead, immediately read the entire file content using the `read_file` tool and ask me for a new plan or confirmation.

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

### Handling SphereScript code by AI Agents
- Do **NOT** assume, best guess or hallucinate language grammar or features. If not sure of the correctness of what you are writing, try to stick with the exact sentences the Changelog or the existing md wiki text are using for that topic. If still unsure, do not add *ex novo* (100% reasoned and produced by you) code or examples.
    
---

# Tasks

## Task 1) Done

>! Create a **new Python script**, starting from `agent_helpers/download_mediawiki.py`, to download the mediawiki files from the old wiki and put them into the folder `mediawiki_orig`. Old wiki address: `https://wiki.spherecommunity.net/index.php?title=Main_Page`

## Task 2) Done

>! Convert the original mediawiki files from the `mediawiki_orig` folder into markdown files in the `mediawiki_orig_conv_markdown` folder through the python script `agent_helpers/convert_wiki.py`, which leverages `pandoc` for the conversion.

## Task 3) Done

>! If missing, retrieve the missing root pages (e.g., `Category*.md`) from the `mediawiki_orig_conv_markdown` folder and expand them if needed, linking to their child pages.

## Task 4) Current, not yet completed.

**Update the wiki content using the `Changelog.txt`** (Long-Running Task).
- **Work Folder**: `markdown_integrated`.
- **Goal:**
    - Expand wiki entries/tables/infos to incorporate new features or reflect changes that affect correctness (e.g., parameter shifts like ARGN2 to ARGN3).
    - Do **NOT** add informations about existing features fixes.
    - If there's a change on how a feature works, do not mention both the old and the new feature usage. Keep only the latest.
- **Tool for Progress & Batching:** You must use the existing Python script `agent_helpers/process_changelog.py` for all changelog management.
    - **Initial Setup:** The script is responsible for creating and maintaining `agent_helpers/changelog_progress.txt`.
    - **Batch Selection:** Use a command-line argument (e.g., `--start-point-header`) to instruct the script to find the next uncompleted entry and output a batch of **5 entries** to integrate into the wiki.
    - **Progress Tracking:** After successfully integrating a batch, use another command-line argument to instruct the script to apply **strike-through formatting** to those completed entries in the **`changelog_progress.txt`** file.
- **Content Creation:**
    - Only integrate changes of **functionalities** (new, removal, or change) that are relevant to end-users; ignore vague fixes or simple bugfixes.
    - If a page doesn't exist, **create and link it to the relevant parent page** only if you have sufficient, relevant information. New pages must contain **at least one parameter table and 1-2 paragraphs** of useful information. Do not create mostly empty pages.
- **Verification & Constraint:**
    - Do not add the date a feature was fixed. Assume the wiki is always updated to the latest build.
    - Check if the reason your file manipulation tools are failing is simply because a file **does not exist**.
    - Make sure that any files you are adding new links to **do really exist** and have the correct, non-hallucinated content.
- **Execution Plan:** **Continue with every unaddressed changelog entry** (as indicated by `agent_helpers/changelog_progress.txt`), taking the time you need and proceeding without supervision.

## Task 5) TODO.

Review and fix the links you inserted between pages, as most have a **broken format** (e.g., an unnecessary leading `:`). Moreover, for each markdown "root" file (has multiple links to other pages, and the other pages are "children" and do have only one root file), create a folder with the "root" markdown file name. Keep every child file in that folder. Subfolders are allowed.

## Task 6) TODO.

Read every **Sphere.ini** setting and add it to the wiki in the relevant page, if missing.

## Task 7) TODO.

**Post-Processing Pass:** After all other tasks are complete, perform a single, full review of all modified/created files to ensure:
1. **Consistent Markdown Headings** (e.g., no excessive deep nesting like `#######`).
2. **Consistent Use of SphereScript/C++ Terminology** (e.g., `SphereScript` is correctly capitalized).
3. **No Redundant or Repetitive Information** was added during the batch processing of Task 3.
