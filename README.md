# SphereServer Markdown Wiki

This repo is a work in progress effort to create a new updated Wiki for SphereServer-X.

Steps:
- Done: Translate the [old MediaWiki](https://wiki.spherecommunity.net/index.php?title=Main_Page) (available in `mediawiki_orig/`) to Markdown (in `mediawiki_orig_conv_markdown/`).
- In-progress: Auto-update the md Wiki with Python scripts and AI agents (gemini-cli) with information from `Changelog.txt`.
    - `GEMINI.MD` is a System Instruction and Constraint Set for the agent. It also contains the workflow organized in sequential tasks.
    - `.gemini/settings.json` are suggested settings for the agent.
    - `agent_helpers/` holds the Python 3 helper scripts for the agent.
    - `markdown_integrated/` is the folder with the integrated markdown wiki files.
    - If interested in using gemini-cli, test it for a while and, if it works for you without needing many manual "corrections", you can run it with the YOLO flag (do not ask permission for anything), provided you already made a backup: `gemini --yolo`.
