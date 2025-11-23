# About the repo
We are porting an old mediawiki for SphereServer main features and scripting language (SphereScript).
We already fetched the old content, converted it with pandoc to Github flavored Markdown, linked the pages between them, through some python scripts we written.
Since the old wiki was not updated often, and for sure most of the features and commits slipped away, in this folder you have our Changelog.txt. It contains the changes to the c++ core and SphereScript features that are relevant to the end users, the game masters, scripters, admins. Informations relevant for maintainers of SphereServer are stored elsewhere.

# General rules
- Do not add informations about implementation details or inner workings relevant only to contributors of the c++ source code.
- Preserve case. Most of SphereScript short keywords/acronyms are UPPERCASE, but something else could be in PascalCase for better readability (often for long keywords, especially if long and containing more english words together).
- Before performing any edit on @filename, please print the block of code you intend to replace (your old_string) to ensure you have the correct, current content.
- When using the edit tool, if the edit fails, do not try to correct the old_string and retry. Instead, immediately read the entire file content using the read_file tool and ask me for a new plan or confirmation.
- Everytime you log a block of output (an answer of yours), execute the following shell command, in order to print the time at which each answer was provided: `(Current time is $(date +%T.%3N))`


# Tasks
Task 1) Create another python script, starting from 'convert_wiki.py', to download the mediawiki files from the old wiki, and put them into the folder 'wiki_mediawiki_orig'
Task 2) You did most of the pandoc conversion and md linking correctly, a little issue is that you removed root pages (like Category*.md files), but those are still in the wiki_markdown_old/ folder, so you can take them from there and expand if needed with the child pages.
Task 3) We are working on updating the wiki with the informations on the changelog.
Do not add the raw changelog data. i need you to expand the wiki entries/tables/infos to add the new features you see in the changelog, or reflect the changes that affect the correctness of what is already written in the wiki (i.e. for trigger 'xx' now ARGN2 does not contain the current world timestamp, but now it's stored in ARGN3).
If a page doesn't exist, you are free to create and link it to the parent one, provided you have sufficient/a relevant quantity of informations to add about that command/topic. Do not add pages and leave them mostly empty. They need to have at least one parameter table and 1 to 2 paragraphs of useful informations.
Check if the reason your find/replace tools are failing is simply because a file does not exist.
Don't add the date a feature was fixed. we are under the assumpion that the wiki is always updated to the last build/commit/change.
Ignore vague fixes. integrate only change of functionalities or new or removal or functionalities, not bugfixes
Process changelog entries in 5 entries batches. Doing that one entry at a time will bee too expensive and inefficient.
You need to process every changelog entry
Make sure that the files you are adding new links to, if actually needed, do really exist and have the correct, not hallucinated content.
I don't want to supervise you. Continue with every changelog entry (if not yet addressed), take the time you need and proceed, even if it takes hours.
Task 4) Please note that most of the links you inserted between pages have a broken format (ie. an unnecessary leading ':'). Review and fix them.
Task 5) Read every Sphere.ini setting and add it to the wiki in the relevant page, if missing.
