# About the repo
We are porting an old mediawiki for **SphereServer** main features and scripting language (**SphereScript**).
We have fetched and converted the old content to **GitHub Flavored Markdown (GFM)** and linked the pages.
The **Changelog.txt** contains changes to the C++ core and SphereScript features relevant to end-users (game masters, scripters, admins). Information relevant for maintainers is stored elsewhere.

---

# General Rules

- Do not add information about implementation details or inner workings relevant only to C++ source code contributors.
- **Preserve Case:** SphereScript keywords/acronyms are often **UPPERCASE** or **PascalCase**.
- **(NEW) Tool Parameter Constraint:** When using any file manipulation tool (like `WriteFile`, `ReadFile`, or `EditFile`), you **must** explicitly include the `file_path` argument, even if the file is already referenced in context.
- **Progress Tracking:**
    - Every time you log a block of output (an answer of yours), execute the following shell command **immediately before the output** to print the time: `(Current time is $(date +%T.%3N))`

### ⚠️ File Handling & Context Management (Critical)

- Mandatory Editing Tool: For ALL file content modifications (replacements, insertions, or deletions), you MUST use the dedicated Python script, file_editor.py, instead of the built-in Edit tool.
Usage: python file_editor.py <filepath> --old "old_string" --new "new_string"
- Use your (gemini-cli) tools only if you can't manage to make file_editor.py to work.
- **Context Isolation & Token Management:** **NEVER** read an entire file unless absolutely necessary. After successfully performing an edit on a file, **do not read that file again** in the current batch unless it is the explicit target of a subsequent operation. Assume the change was successful and avoid polluting the context with redundant file content.
- **Edit Tool Reliability:**
    - Before performing any edit on `@filename`, use the **most scoped method possible** (e.g., `grep` or a targeted `read_file` with line/range parameters, if available) to fetch **only the specific block** containing your intended `old_string`. Only fall back to reading the entire file if a targeted search fails.
    - When using the edit tool, if the edit fails (e.g., "0 occurrences found"), **do not try to correct the `old_string` and retry.** Instead, immediately read the entire file content using the `read_file` tool and ask me for a new plan or confirmation.

---

# Tasks

Task 1) Create a **new Python script**, starting from 'convert_wiki.py', to download the mediawiki files from the old wiki and put them into the folder `wiki_mediawiki_orig`. Old wiki address: `https://wiki.spherecommunity.net/index.php?title=Main_Page`

Task 2) Review the pandoc conversion. The conversion correctly created the main wiki pages but **removed root pages** (e.g., `Category*.md`). Retrieve these missing root pages from the `wiki_markdown_old/` folder and expand them if needed, linking to their child pages.

Task 3) **Update the wiki content using the `Changelog.txt`** (Long-Running Task).

- **Work Folder**: `wiki_markdown`.
- **Goal:** Expand wiki entries/tables/infos to incorporate new features or reflect changes that affect correctness (e.g., parameter shifts like ARGN2 to ARGN3).
- **Tool for Progress & Batching:** You must use the existing Python script **`process_changelog.py`** for all changelog management.
    - **Initial Setup:** The script is responsible for creating and maintaining `changelog_progress.txt`.
    - **Batch Selection:** Use a command-line argument (e.g., `--start-point-header`) to instruct the script to find the next uncompleted entry and output a batch of **5 entries** to integrate into the wiki.
    - **Progress Tracking:** After successfully integrating a batch, use another command-line argument to instruct the script to apply **strike-through formatting** to those completed entries in the **`changelog_progress.txt`** file.
- **Content Creation:**
    - Only integrate changes of **functionalities** (new, removal, or change) that are relevant to end-users; ignore vague fixes or simple bugfixes.
    - If a page doesn't exist, **create and link it to the relevant parent page** only if you have sufficient, relevant information. New pages must contain **at least one parameter table and 1-2 paragraphs** of useful information. Do not create mostly empty pages.
- **Verification & Constraint:**
    - Do not add the date a feature was fixed. Assume the wiki is always updated to the latest build.
    - Check if the reason your file manipulation tools are failing is simply because a file **does not exist**.
    - Make sure that any files you are adding new links to **do really exist** and have the correct, non-hallucinated content.
- **Execution Plan:** **Continue with every unaddressed changelog entry** (as indicated by `changelog_progress.txt`), taking the time you need and proceeding without supervision.

Task 4) Review and fix the links you inserted between pages, as most have a **broken format** (e.g., an unnecessary leading `:`).

Task 5) Read every **Sphere.ini** setting and add it to the wiki in the relevant page, if missing.

Task 6) **Post-Processing Pass:** After all other tasks are complete, perform a single, full review of all modified/created files to ensure:
1. **Consistent Markdown Headings** (e.g., no excessive deep nesting like `#######`).
2. **Consistent Use of SphereScript/C++ Terminology** (e.g., `SphereScript` is correctly capitalized).
3. **No Redundant or Repetitive Information** was added during the batch processing of Task 3.
