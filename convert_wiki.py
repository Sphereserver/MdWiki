import re
import subprocess
import os
import requests
from urllib.parse import quote

BASE_URL = "https://wiki.spherecommunity.net/index.php"
OUTPUT_DIR = "wiki_markdown"

def get_wikitext(page_title):
    """Fetches the raw wikitext for a given page title."""
    # URL-encode the page title to handle spaces and special characters
    encoded_title = quote(page_title)
    url = f"{BASE_URL}?title={encoded_title}&action=raw"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {page_title}: {e}")
        return None

def find_links(wikitext):
    """Finds all MediaWiki links in the given wikitext."""
    # This regex handles standard links, links with display text, and category links
    links = re.findall(r'\[\[:?([^\]|]+)(?:\|[^\]]+)?\]\]', wikitext)
    # Filter out anchor links
    return [link for link in links if not link.startswith('#')]

def convert_to_markdown(wikitext, page_title):
    """Converts wikitext to Markdown using pandoc."""
    # Sanitize the page title to create a valid filename
    sanitized_title = re.sub(r'[^\w\s-]', '', page_title).strip().replace(' ', '_')
    if not sanitized_title:
        sanitized_title = "untitled"
    
    markdown_filename = os.path.join(OUTPUT_DIR, f"{sanitized_title}.md")
    
    # Use pandoc to convert the wikitext
    try:
        process = subprocess.run(
            ['pandoc', '-f', 'mediawiki', '-t', 'markdown'],
            input=wikitext,
            text=True,
            capture_output=True,
            check=True
        )
        with open(markdown_filename, 'w', encoding='utf-8') as f:
            f.write(process.stdout)
        print(f"Converted '{page_title}' to '{markdown_filename}'")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error converting page {page_title}: {e}")
        return False

def main():
    """Main function to crawl the wiki and convert pages."""
    to_visit = ["Main_Page"]
    visited = set()

    # Initial wikitext for the main page, which we already fetched
    main_page_wikitext = """
<div style="background-color:#a7bcdc; color:#000; min-width:650px; padding:1px; text-align:center; width:100%;">
'''Starting with SphereServer'''
</div>
<div style="min-width:650px; width:100%;">
	<div style="border-right:1px solid #a7bcdc; float:left; height:100%; margin-right:-1px; width:33%;">
		<div style="border-bottom:1px solid #a7bcdc; color:#a7bcdc; font-size:18px; padding-left:10px;">
			'''Setup of Sphere'''
		</div>
		<div style="border-bottom:1px solid #a7bcdc; padding:0px 0px 5px 10px;">
* [[Where to get Sphere]]
* [[Installing Sphere]]
* [[Configuring Sphere.ini]]
		</div>
		<div style="border-bottom:1px solid #a7bcdc; color:#a7bcdc; font-size:18px; padding-left:10px;">
			'''Sphere 101'''
		</div>		
		<div style="padding:0px 0px 5px 10px;">
* [[Chapter 1]] ''(Numbers, DEFNAME, ITEMDEF, CHARDEF)''
* [[Chapter 2]] ''(Sphere files explained)''
* [[Chapter 3]] ''(Scripting NPC's and items, Cool commands)''
* [[Chapter 4]] ''(Objects, operators, speech)''
* [[Chapter 5]] ''(Tags, Vars, Locals, Functions)''
* [[Chapter 6]] ''(LINKs, TIMERs, TARGETs)''
* [[Chapter 7]] ''(Loops and powerful functions)''
* [[Chapter 8]] ''(SKILLMENUs, MENUs, Gumps)''
* [[Chapter 9]] ''(Events)''
* [[Chapter 10]] ''(String Handling)''
		</div>
	</div>
	<div style="border-left:1px solid #a7bcdc; float:left; height:100%; margin-right:-1px; width:67%;">
		<div style="border-bottom:1px solid #a7bcdc; color:#a7bcdc; font-size:18px; padding-left:10px;">
			'''Extra Tutorials'''
		</div>
		<div style="border-bottom:1px solid #a7bcdc; padding:0px 0px 5px 10px;">
* [[Common Mistakes|Common Mistakes Explained]] ''(A revision of Maximus's tutorial on the forums, and continuation of Taran's Misconceptions tutorial)''
* [[Internet and Sphere]] ''(And how to make the right use of them)''
* [[Languages Tutorial]] ''(How to script your own language system)''
* [[Making your own Skills]] ''(How to make and customize your skill)''
* [[Mul Patching Tutorial|Nazghul's Mul Patching Tutorial]] [http://sorea.profitux.cz/patching/ external link] ''(A document about mul patching and customizing your server)''
* [[Overriding Hardcoded Commands]] ''(How to override hardcoded commands and functions)''
* [[Scheduled Reboot]] ''(How to schedule system reboots)''
* [[Using MySQL]] ''(How to use MySQL)''
* [[Bitwise Operations]] ''(How to work with FLAGS/ATTR)''
* [[Script Debugging]] ''(How to fix your scripts)''
		</div>
		<div style="border-bottom:1px solid #a7bcdc; color:#a7bcdc; font-size:18px; padding-left:10px;">
			'''IMPORTANT LINKS'''
		</div>
		<div style="padding:0px 0px 5px 10px;">
* [https://github.com/Sphereserver SphereServer Official Github]
* [https://forum.spherecommunity.net/sshare.php?srt=4 Download Nightly Builds] ''(Plus! Extra downloads, like tools and scripts!)''
* [https://github.com/Sphereserver/Source-X/blob/master/Changelog.txt SphereX Changelog] | [https://github.com/Sphereserver/Source/blob/master/changelog.txt 56d Changelog] | [https://github.com/Sphereserver/Source-X/tree/master/docst Older Changelog]
* [https://discord.gg/BZj2fEA Join us at Discord] ''(We will solve most of your doubts over there)''
		</div>		
	</div>
</div>
.

<div style="background-color:#a7bcdc; color:#000; min-width:650px; padding:1px; text-align:center; width:100%;">
'''Reference Compendium'''
</div>
<div style="min-width:650px; width:100%;">
	<div style="border-right:1px solid #a7bcdc; float:left; height:100%; margin-right:-1px; width:33%;">
		<div style="border-bottom:1px solid #a7bcdc; color:#a7bcdc; font-size:18px; padding-left:10px;">
[[:Category:Definitions|'''Definitions''']]
		</div>		
		<div style="padding:0px 0px 5px 10px;">
* [[CHARDEF|Chardef]] | [[Characters|Characters]]
* [[DIALOG|Dialogs]]
* [[EVENTS|Events]]
* [[ITEMDEF|Itemdef]] | [[Items|Items]]
* [[MENU|Menus]]
* [[REGIONRESOURCE|Region Resources]]
* [[REGIONTYPE|Region Types]]
* [[AREADEF|Regions]]
* [[ROOMDEF|Rooms]]
* [[SKILLCLASS|Skill Classes]]
* [[SKILLMENU|Skill Menus]]
* [[SKILL|Skills]]
* [[SPAWN|Spawn Groups]]
* [[SPELL|Spells]]
* [[TYPEDEF|Types]]
		</div>
	</div>
	<div style="border-left:1px solid #a7bcdc; float:left; height:100%; margin-right:-1px; width:67%;">
		<div style="border-bottom:1px solid #a7bcdc; color:#a7bcdc; font-size:18px; padding-left:10px;">
[[:Category:Objects|'''Objects''']]
		</div>
		<div style="border-bottom:1px solid #a7bcdc; padding:0px 0px 5px 10px;">
* [[Accounts]]
* [[Characters]]
* [[Database]]
* [[Files]]
* [[GM Pages]]
* [[Items]]
** ''[[Special Items]]''
* [[Map Points]]
* [[Parties]]
* [[Regions]]
* [[Rooms]]
* [[Sectors]]
* [[Server]]
		</div>
		<div style="border-bottom:1px solid #a7bcdc; color:#a7bcdc; font-size:18px; padding-left:10px;">
[[:Category:Scripts|'''Scripts''']]
		</div>
		<div style="padding:0px 0px 5px 10px;">
* [[:Category:Functions|Functions and Triggers]]
* [[:Category:Variables|General Functions, Properties and References]]
* [[Intrinsic Functions]]
* [[:Category:Statements|Statements]]
* [[:Category:Triggers|Triggers]]
</div>
</div>
.
----

.

==Useful Links==
* Modern SphereServer Nightly Downloads (Server) https://forum.spherecommunity.net/sshare.php?srt=4
* Older/Classic SphereServer downloads (Server) https://forum.spherecommunity.net/sshare.php?srt=4&prj=7
* Sphere-X Script Pack (Scripts) https://github.com/Sphereserver/Scripts-X
* Julians Script Vault (Scripts) https://github.com/JulianUO/SphereX-ScriptsVault
* List of UO Packets (Info) https://docs.polserver.com/packets/index.php
* Scripts https://mirror.ashkantra.de/scripts/Sphere/
* GM Commands (Commands) https://wiki.spherecommunity.net/index.php?title=GM_Commands
* Axis 2 Downloads (GM Tool) https://forum.spherecommunity.net/sshare.php?srt=4&prj=1 
* Leviathan (GM tool) https://github.com/cbnolok/Leviathan/releases
* Ultima Online Downloads (Clients) https://mega.nz/folder/6uYxnIpY#tahGzzz_yOkLgNM1c_DxdQ
* Client 7.0.20 https://mirror.ashkantra.de/fullclients/
* ClassicUO (Third Party Client) https://www.classicuo.eu/
* OrionUO (Third Party Client) http://orionuo.online/
* CentrED (Worldbuilding)  https://uo.wzk.cz/centred/
* UO-Pixel (Graphics) http://www.uo-pixel.de/
* UO Fiddler ( MUL Viewer) http://uofiddler.polserver.com/
* UO Grafiken by Nyray (Graphics) https://nyray.wordpress.com/
* Vestimisu (Graphics) http://vestimisu.blogspot.com/
* Ultima Online Graphics By Rubra (Graphcs) http://uographicsrubra.blogspot.com/
* Isis‘ UO Grafiken (Graphics) https://isispixel.wordpress.com/
* ServUO (Graphics) https://www.servuo.com/archive/categories/assets.13/
* UOGateway (Shard Listing) https://uogateway.com/ 

==Sphere 3rd Party Tools==
* [http://forum.spherecommunity.net/sshare.php?srt=4&uid=603 Axis II] - GM Tool for Sphere that will allow you to place objects in-game, spawns, traveling and many other useful functions for shard admins and GMs.
* [http://forum.spherecommunity.net/sshare.php?srt=4&prj=3 vSCP] - vSCP is the most complete and up-to-date syntax editor for sphere scripting. It does contain syntax highlighting, autocomplete, folding markers to specify blocks of code that can expand or collapse, bookmarks, autoindent, find/replace/gotoline, help guide for all the sphere elements added to your code, and more! 
* [http://forum.spherecommunity.net/sshare.php?srt=4&prj=2 vServerLauncher] - Install and run the latest build of sphereserver in a few clicks with vServerLauncher. It's pretty quick and simple!
* [http://forum.spherecommunity.net/sshare.php?srt=4&prj=5 SphereService] - Relaunch SphereSvr.exe everytime it closes/crashes. Automatically runs at windows startup and works in a silent mode minimized to Tray.
* [http://forum.spherecommunity.net/sshare.php?srt=4&prj=4 vCrypter] - Type the client version and the tool will calculate the correct UO login keys for classic or enhanced clients.


==Other Articles==

* [[Armor Calculation]]
* [[Client Changes]]
* [[Common Scripting Misconceptions]]
* [[Custom Object Properties]]
* [[Error Codes]]
* [[Experience System]]
* [[How Combat Works]]
* [[Occam's Razor]]
* [[Optimization|Optimization Theory]]
* [[Override TAGs]]
* [[Revisions Changelog]]
* [[Sendpacket]]
* [[Skill Gain Theory]]
* [[The Process of Scripting]]
* [[Building Component Reference]]

==Credits==

'''Special thanks to:'''

[[WhoIsWho|XuN, Nolok, Ben, and Drk]], for their hard work on the X branch taking Sphere into the next decade.

[[WhoIsWho|Ben, Cloud_Br, Ellessar, Jdog, Lord Zerofiz, Mordaunt, Nazghul-ll, RanXerox, Rattlehead, Sandman, Sharlenwar, ShiryuX, thelegbra, Maximus, WarAngel and Valios]], for helping to add content.

[[WhoIsWho|Daleth]], for writing the Sphere Reference Project, and [[WhoIsWho|Mordaunt]] for converting it to .chm format.

[[WhoIsWho|Tracker]], for writing the Sphere 56 Tracking Changes in Sphereserver.net

[[WhoIsWho|Taran]], for writing the original and now famous Sphere Scripting for Dummies tutorials, and [[WhoIsWho|MrSugarCube]] for bringing it up-to-date directly from source.

[[WhoIsWho|Ben, Khaos, Ranxerox, Shiryux, Furio, Radiant, Vjaka, Nazghul-ll, Ellessar, Torfo, Shadow Dragon, MrSugarCube and coruja747]] for continuing to develop Sphere into a powerful and very customizable Ultima Online emulator.

[[WhoIsWho|Crius]], for providing hosting for the original SphereWiki, and [[WhoIsWho|Torfo]] for providing the current hosting.

==External Links==

* [[Useful Links]] ''(An ongoing list of useful links for community members)''
* [http://www.spherecommunity.net/ Official SphereServer Website]
* [https://forum.spherecommunity.net/sshare.php?srt=4 Nightly builds]
* [http://nightly.prerelease.sphere.torfo.org/ Nightly builds - OUTDATED, use the link above]
* [http://spherepack.codeplex.com/ Sphere Community Pack 2.0]
* [http://uo.torfo.org/packetguide/ Jerrith's UO Packet Guide]
* [http://uo.torfo.org/packetguideKR/ Wyatt&Kons's UOKR Packet Guide]


[[Category: Navigation]]
"""
    # Process the main page first
    convert_to_markdown(main_page_wikitext, "Main_Page")
    links = find_links(main_page_wikitext)
    to_visit.extend(links)
    visited.add("Main_Page")

    # Now, process the rest of the pages
    while to_visit:
        page_title = to_visit.pop(0)
        if page_title in visited:
            continue

        print(f"Processing page: {page_title}")
        visited.add(page_title)

        wikitext = get_wikitext(page_title)
        if wikitext:
            if convert_to_markdown(wikitext, page_title):
                new_links = find_links(wikitext)
                # Add new, unvisited links to the queue
                for link in new_links:
                    if link not in visited and link not in to_visit:
                        to_visit.append(link)

if __name__ == "__main__":
    main()
