# Clilocs

Client Localization (`Clilocs`) are a system used by the Ultima Online client to display localized text messages, item names, and other dynamic content. Instead of sending raw text, the server sends a numerical ID and a list of arguments, which the client then interprets using its local Cliloc files. This system now correctly parses empty and NULL arguments, and the Cliloc for the item name is forcefully sent first to ensure proper display.

[Category: Game Mechanics](./CategoryGame_Mechanics.md)