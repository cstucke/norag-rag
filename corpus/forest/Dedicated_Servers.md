# Dedicated Servers
Source: https://theforest.fandom.com/wiki/Dedicated_Servers
Categories: Guide, Help
Revision: 74932

**Dedicated Servers** are a tool that was implemented by Endnight Games in update v0.59. This allows player to create multiplayer games that run constantly at their homes or through server providers. It is recommended you visit the official steam links below for tutorials on how to setup a **dedicated server**.

## Dedicated Server Tutorial

This is the official dedicated server tutorial that is posted on Steam by Endnight Games

Official Guide to Dedicated Servers  
 Official Discussion: Dedicated Servers  
 Dedicated Server Bug Reports  
 Unofficial Dedicated Server Troubleshooting Guide

## Adding Favorite Servers

This needs to be done within Steam for it to work, it cannot be done in game:

* 1. Go to Steam
* 2. View > Servers
* 3. Favorites
* 4. Add a Server
* 5. Input IP: xx.xx.xx.xxx:27016 <--(IMPORTANT)
* 6. Add27016 IS I
* 7. Refresh

## In Game Server Commands

These commands are available to players who provided a valid admin password when joining. Use these commands in the in-game multi-player chat, accessed by pressing the `Enter` key. Here is a list of the current known commands:

| Command | Description |
| --- | --- |
| `/help` | Provides you with a help menu of all the known commands |
| `/save (slot number 1-5)` | Saves the game on the chosen slot number. Be careful as it may save over another game in your dedicated server save folder |
| `/restart` | Restarts the server, resets save game (WARNING: SAVE DATA WILL BE DELETED) |
| `/shutdown` | Shuts down the server, unknown if it will save prior |
| `/ban (steam id)` | Bans the user, REQUIRES MORE INFORMATION |
| `/kick (steam id)` | Kicks the user, REQUIRES MORE INFORMATION |
| `/treeregrowmode` | Regrow 10% of cut down trees when sleeping. Options are `treeRegrowMode on` or `treeRegrowMode off` |
| `/allowbuildingdestruction` | Allow building destruction. Options are `allowBuildingDestruction on` or `allowBuildingDestruction off` |
| `/allowenemiescreative` | Allow enemies in creative games. Options are `allowEnemiesCreativeMode on` or `allowEnemiesCreativeMode off`. |
| `/openlogs` | REQUIRES INFORMATION |
| `/closelogs` | REQUIRES INFORMATION |

## Server Commands

These are the commands that are listed in the txt file:

| Command | Description |
| --- | --- |
| `serverIP` | Server IP address - Note: If you have a router, this address is the internal address, and you need to configure ports forwarding. Don't use your global IP address. |
| `serverSteamPort 8766` | Steam Communication Port - Note: If you have a router you will need to open this port. |
| `serverGamePort 27015` | Game Communication Port - Note: If you have a router you will need to open this port. |
| `serverQueryPort 27016` | Query Communication Port - Note: If you have a router you will need to open this port. |
| `serverName` | Server display name. How it is seen in the game lobby. |
| `serverPlayers 8` | Maximum number of players, default is 8. |
| `enableVAC off` | Enable VAC (Valve Anti-cheat System at the server. Options are `enableVAC on` or `enableVAC off`. |
| `serverPassword` | Server password. Blank means no password. It is recommended to have a password to prevent griefers. |
| `serverPasswordAdmin` | Server administration password. Blank means no password. |
| `serverSteamAccount` | Don't leave this blank or use your actual Steam account name. You can obtain an ID number here. The Forest App ID number is `242760`. DO NOT SHARE THIS CODE! |
| `serverAutoSaveInterval 30` | Time between server auto saves in minutes - The minimum time is 15 minutes, the default time is 30. |
| `difficulty HardSurvival` | Game difficulty mode. Must be set to `Peaceful` / `Normal` / `Hard` / `HardSurvival` |
| `initType Continue` | Must be set to `New` or `Continue`. If left on `New`, the game won't save and you will have to restart each time. |
| `slot 1` | Slot to save the game. Must be set to either `slot 1` / `slot 2` / `slot 3` / `slot 4` / `slot 5`. |
| `showLogs on` | Show event log. Must be set off or on. It is highly recommended to leave this on, this will show if your server is working or not and what issues you may be having, if any. Options are `showLogs on` or `showLogs off`. |
| `serverContact` | Contact email for server admin. Not required. |
| `veganMode off` | No enemies if switched off. Options are `veganMode on` or `veganMode off`. |
| `vegetarianMode off` | No enemies during day time. Options are `vegetarianMode on` or `vegetarianMode off`. |
| `resetHolesMode off` | Reset all structure holes when loading a save. These are holes caused by the hole cutter. This has the same effect as the woodpaste command. Options are `resetHolesMode on` or `resetHolesMode off` |
| `treeRegrowMode off` | Regrow 10% of cut down trees when sleeping. Options are `treeRegrowMode on` or `treeRegrowMode off` |
| `allowBuildingDestruction on` | Allow building destruction. Options are `allowBuildingDestruction on` or `allowBuildingDestruction off` |
| `allowEnemiesCreativeMode off` | Allow enemies in creative games. Options are `allowEnemiesCreativeMode on` or `allowEnemiesCreativeMode off`. |
| `allowCheats on` | Allow clients to use the built in debug console. This only disables console commands, it has no effect on mods such as the *Ultimate Cheat Menu*. People can still grief your game. Options are `allowCheats on` or `allowCheats off`. |
| `saveFolderPath` | Allows defining a custom folder for save slots, leave empty to use the default location. |
| `targetFpsIdle 5` | Target FPS when no client is connected. |
| `targetFpsActive 60` | Target FPS when there is at least one client connected. |
| `configfilepath` | Changes the config file path used by the server |
| `realisticPlayerDamage off` | Realistic Player Damage (On/Off), this allows the game to be more PvP based. Damage to other players will be increased dramatically, depending on the weapon. |

## Dedicated Server List

Here is a list of The Forest Dedicated Game Server Providers and their price per slot/player. These Game Server providers allow you to rent an The Forest Game Server from them.

| Host Name | Price per Slot\Player\* | Minimum Slots | Location(s) | Control Panel | Notes | Last Update |
| --- | --- | --- | --- | --- | --- | --- |
| 4Netplayers | ($1.24) | 10 Slots Min | \* Germany  * United Kingdom * France * Poland * Finland * Spain * Romania * USA * Singapore * Australia | Custom | Instant Setup, Cloud Gameserver, Update Service, High Performance Server, DDoS protection. | 2023-02-23 |
| AA Game Hosting | ($0.65) | 30 Slots Min | USA, Australia, Singapore, Canada, UK, France, Germany | TCAdmin 2.0 | Instant Setup, Advanced DDoS Protection, Mod Support, TCAdmin Control Panel, 24/7 Support, High Performance Servers, Free location swap anytime, Full FTP file access, Backup & Restore functionality, Easy to use Configuration Editor, Custom command lines, Easy one-click updater, 4 GHz+ processor with SSD/NVMe storage, Voice servers availablem, 48 hour refund | 2020-02-22 |
| AscendServers | ($0.59) | 10 Slots Min | USA, Canada, UK, France, Germany, Singapore | TCAdmin 2.0 | Instant Setup, No Branding, FTP / File Manager Access, Configurable Options, Advanced DDoS protection, Mod Support | 2018-01-30 |
| BlueFangSolutions | ($1.50-$0.42) | 10 Slots Min | USA, UK, Germany, France, Singapore, Australia | Custom Solution | No Branding, FTP / File Manager Access, Configurable Options, Advanced DDoS protection, Phone Support, Backup Upon Request, Live Chat, 72-hour Refund Policy | 2022-01-29 |
| CitadelServers | ($0.48) | 10 Slots Min | * USA * Canada * UK * France * Germany * Italy * Poland * Norway * Finland * Netherlands * Singapore * Japan * Australia | TCAdmin 2.0 | Instant Setup, No Branding, FTP / File Manager Access, Configurable Options, Advanced DDoS protection, Mod Support | 2018-01-30 |
| EUGameHost.com | $1.52 | 4 Slots Min | Germany, United Kingdom, Dallas Texas. | TCAdmin 2.0 | Instant Setup, Ready To Play Game Servers, No Branding, Amazing Reviews, SSD NVMe Storage, SFTP Access, Path.net 17Tbit/s DDoS protection, Easy Configuration, Full mod/plugin support, Free backups, free website hosting, free Mysql database. | 2023-12-11 |
| Game Host Bros | $7.99 / month | Unlimited | USA, Canada, UK, France, Germany, Japan, Singapore | Custom Panel (Bropanel) | Beginner Friendly, 7-Day Refund Policy, Instant Setup, Full File / SFTP Access, Automatic Backups, Enterprise-Grade DDoS Protection, Free Server Migrations, NVMe Storage, AMD Ryzen 9 9950X Hardware, 10Gbps Networks, 24/7 Support, Game Swapping, Location Swapping, Comprehensive Knowledgebase | 2026-09-08 |
| Gameservers.com | ($1.10) | 8 Slots Min | 20+ locations including, USA, Canada, UK, NL, France, DE, Italy, Poland, Russia, Japan, South Africa, Australia and more. | Custom | Instant setup, No Branding, 5 day satisfaction full refund, 24/7 technical support, High performance dedicated servers, Worldwide network, DDOS protection, Easy setup with server settings editor, Mod support, Clan Pay, Free location swap anytime, FTP / File Manager Access, Voice servers available. | 2019-1-13 |
| godlike.host | Not Slot Based | Not Slot Based | USA, Canada, UK, France, Germany, Poland, Singapore, Australia, Ukraine, India, Finland, Netherlands | Pterodactyl | Unlimited Player Slots, Unrivaled Hardware, Schedule Tasks, DDoS Protection, SFTP Access, SSD Drives, Subuser Access, Resource Usage Statistics, 24/7 Support | 2025-12-08 |
| GG Host | Not Slot Based | No slot limit | * USA * UK * Brazil * Germany * Finland * South Africa * Singapore * Australia * Thailand * Japan * Hong Kong | TCAdmin 2.0 | \*Ultra-performance server (no need to pay extra for the best performance)  * 10GB of RAM Free! * M.2 NVMe SSDs as a standard * Any number of slots, no extra charge! * No Branding * FTP / File Manager Access * Configurable Options * Advanced DDoS protection * 48-hour Refund Policy | 2023-02-17 |
| GPORTAL | ($1.40) | 10 Slots Min | Germany, The United Kingdom, Spain, Russia, USA, Canada, Brazil, Japan, Australia, Taiwan, Singapore, South Africa | Custom | Instant Setup, No Branding, FTP / File Manager Access, Configurable Options, Advanced DDoS protection, 24/7 support, High Performance Servers, Donation URL | 2020-07-17 |
| GTXGaming | ($0.96) | 16 Slots Min | USA, Canada, UK, France, Spain, Sweden, Germany, Russia, Australia | TCAdmin 2.0 | Instant Setup, No Branding, FTP / File Manager Access, Configurable Options, Advanced DDoS protection, Mod Support | 2018-05-03 |
| LogicServers.com | ($0.90) | 10 Slots Min | London, UK - Stockholm, SE - Nuremberg, DE - Montreal, CA - New York, US - Los Angeles, US - Dallas, US - Chicago, US | TCAdmin 2.0 | Instant Setup, Advanced DDoS Protection, Mod Support, TCAdmin Control Panel, 24/7 Support, High Performance Servers, Free location swap anytime, Full FTP file access, Backup & Restore functionality, Easy to use Configuration Editor, Custom command lines, Easy one-click updater, 4 GHz+ processor with SSD/NVMe storage, Voice servers availablem, 48 hour refund | 2019-09-12 |
| LOW.MS | ($0.76) | 12 Slots Min | \*London, UK  * Nuremberg, Germany * Ashburn, USA * Miami, USA * Dallas, USA * Los Angeles, USA * Helsinki, Finland * Sydney, Australia * Singapore | TCAdmin 2.0 | \*5-Day Refund Policy  * One-Click Setup * Automatic mod updating * 24/7 Support * FTP Access * No Branding | 2021-08-24 |
| Needaserver | ($1.01) | 8 slot minimum | Worldwide locations | TCAdmin 2.0 | Instant Setup, FTP / File Manager Access, Configurable Options, Advanced DDoS protection | 2018-15-05 |
| NodePlay | Not Slot Based | No Slot Limit | * Germany * Poland * Russia | NodeHub (Custom) | Game Panel  * Easy Management * One-Click Installation   Convenience   * Game Switching * Custom Settings   Reliability   * DDoS Attack Protection * Auto-Backups and Tasks   Speed   * Premium Servers * Stability and FPS | 2026-03-03 |
| Nodecraft | Unlimited $3-$5/GB RAM | No Slot Limit | * North America * South America * Asia-Pacific * Europe * Australia | Custom | * AMD Ryzen 9 and EPYC CPUs * No Overselling * Custom Game Panel * Easy Management * One-Click Installation * Game Swapping * DDOS Attack Protection * Auto-Backups and Tasks * (s)FTP Access | 2026-09-11 |
| Nodium Hosting | Not Slot Based | No Slot Limit | Germany | Custom | Instant Setup, No Branding, 24/7 support via Live Chat/Email/Ticket, SSD Storage, SFTP Access, Advanced DDOS protection, Easy Configuration, Full mod/plugin support, Free backups | 2023-02-23 |
| Nitrado | Not Slot Based | 4 Slots Min | \*London, UK  * Frankfurt, DE * New York, USA * Miami, USA * Los Angeles, USA * Singapore, SG * Sydney, AUS * Tokyo, JPN * São Paulo, BRA | Nitrado Panel | \*Easy Management  * Install Mods & Plugins easily * High Reliability * Flexible Runtime * Switch active game any time * DDoS Protection * Support of all current mods & updates | 2023-02-15 |
| PingPlayers | ($1.44) | 4 slot minimum | * Europe (Amsterdam) * US East (New York) | Custom | Rapid-setup time, 100% uptime guarantee, 24/7 multi-lingual support, High-end powerful hardware, DDoS protection and Easily schedule server events | 2024/11/14 |
| Pingperfect | ($1.11) | 8 Slot Min | * USA * Canada * Brazil * UK * France * Germany * Netherlands * Russia * Australia * Singapore * South Africa | TCAdmin 2.0 | Instant Setup, FTP /File Manager Access, Configurable Options, Advanced DDOS protection, Mod Support, 24/7 Support, Discounts available, Phone Support, Daily backups, swap to any other game with a support ticket | 2018-25-06 |
| SandBox Hosting | 0.50 | 10 Slot Min | * USA * Canada * Brazil * UK * France * Germany * Netherlands * Australia * Singapore | TCAdmin 2.0 | Instant setup, 72-hours refund policy, 24/7 support, amazing DDOS protection, full FTP access, unlimited NVMe storage, high-performance hardware. | 2025-17-06 |
| ServerBlend | ($1.16) | 10 Slot Min | * USA (Dallas, Texas) * Canada (Montreal) * France * Germany | TCAdmin 2.0 | Instant setup, Cancel anytime, 14 day satisfaction refund, 24/7 technical support, High performance dedicated server, Optimised network with low ping, DDOS protection, Easy setup with server settings editor, Public Pay, FREE transfer service, FREE Enjin premium for 45 days | 2018-03-11 |
| Servers4Gamers | $2.5 GB/RAM | min. 2 GB RAM | * Falkenstein (DE) * Helsinki (FI) * Montreal (CA) | Pterodactyl | Intel i9 or Ryzen CPU,Full NVMe storage,Unlimited slots,DDR4 RAM memory, Server splitter, One-click mod install, Advanced DDoS Protection,7 Days Free Trial, Instant Setup, Automatic Updates, Full Mod/Plugin Support, Support via LiveChat, Email, Ticket, No branding | 2024-07-01 |
| Shockbyte | ($0.87) | 8 Slot Min | * USA * Canada * Europe * Australia * Singapore | Multicraft | Instant setup, 72-hours refund policy, 24/7 support, amazing DDOS protection, full FTP access, unlimited NVMe storage, high-performance hardware. | 2022-11-04 |
| Supercraft | ($0.75) | 8 Slots (every plan) | * USA (Oregon) * Canada * France * Australia (Sydney) | Custom | All plans take the full 8 players and differ in hardware. FTP access, private password, region switching, on-demand backups, DDoS protection, 2-day refund. | 2026-10-27 |
| Vilayer | ($1.90) | 20 Slots min | Worldwide locations | TCAdmin 2.0 | Instant Setup, FTP / File Manager Access, Configurable Options, Advanced DDoS protection | 2018-01-30 |
| ZAP-Hosting | ($0.96) | 10 | United Kingdom, USA, Germany, Canada, Singapore, Australia, Brazil | Custom | Instant Setup, 24/7 support via Live Chat/Email/Ticket, SSD Storage, FTP Access, Advanced DDOS protection, Easy Configuration, Full mod/plugin support, Free backups | 2020-02-21 |

## Update history

| Version | Changes |
| --- | --- |
| v1.08 | DS - In game browser, fixed server request timing out before fetching all available servers (decoupled server data fetching from UI element creation, improved time to create UI elements, lowered refresh rate of the UI grid when adding new rows) DS - Fixed issues with config file parameter |
| v1.06 | DS - Fixed interval timer counting time while no player is connected DS - Fixed time calculation precision issue causing time to no longer getting properly accounted for at some point  DS - It is now possible to choose whether clients are allowed or not to use the built in debug console, either with the "allowcheats <on|off>" entry in the config file or "-allowcheats" command line parameter |
| v1.0 | Fixed walkie talkies not working correctly on dedicated servers |
| v0.68 | (DS) It is now possible to join a server through Steam's server browser as well as through the “Join game” menu of the friend list when a friend is already connected to it |
| v0.67 | (DS) Fixed tree regrowth (DS) Fixed water collector not working  (DS) Fixed Kick and Ban features, admin commands now also supports kicking, banning and unbanning by name |
| v0.65 | (UI) Fixed DS browser scrollbar mess + improved perfs (DS) Fixed animal pool not getting cleaned up properly when leaving the game to title screen, leaving further runs with no visible animals when playing as client |
| v0.64 | DS – Fixed tree regrow, allow building destruction, allow enemies in creative settings getting overridden on game start |
| v0.63 | (DS) Fixed issue where enemy weapons could cause error spam (DS) Fixed turtles behaviour on dedicated servers.  (DS)Teeth now appear in dedicated server games  (DS) Fixed issues with incorrect material count on custom structures  (DS) Fixed invalid password message not showing in some sessions when attempting to join with the wrong password.  (DS) Fixed some issues with attempting to load regular multiplayer games into dedicated server games  (DS) Fixed issues where errors would spam after exiting boss fight and attempting to load into server  (DS) Fixed enemies sometimes getting stuck in burning animation on dedicated server games.  (DS) Added network configuration diagnostic to help admins |
| v0.62 | off>, vegetarianMode <on|off>, resetHolesMode <on|off>, treeRegrowMode <on|off>, allowBuildingDestruction <on|off>, allowEnemiesCreativeMode <on|off> (DS) New command line options: -veganmode, -vegetarianmode, -resetholesmode, -treeregrowmode, -allowbuildingdestruction, -allowenemiescreative  (DS) Added -configfilepath <filePath> command line option, if target file doesn't exists it tries to create it with the default values  (DS) New admin commands: /treeregrowmode <on|off>, /allowbuildingdestruction <on|off>, /allowenemiescreative <on|off>  (DS) Fixed catapult not working at all in dedicated servers |
| v0.61 | (DS) Fixed issues with repairing custom foundations (DS) Connected players in dedicated servers should now be correctly listed  (DS) Dedicated Steam server authentication added, allows performing security checks  (DS) No longer attempting to hook with the Steam client, it is no longer needed to worry about launching the game first to have a server running on the same machine as the one running the game |
| v0.60 | (Optimization) Completely removed motion blur cpu cost when running a dedicated server (Dedicated Server) Clients now know the game was saved server side, and see a “Server is saving the game” message if saving takes too long  (Dedicated Server) Dedicated server can now be downloaded, installed and launched without the steam client (see -nosteamclient option in guide)  (Dedicated Server) Limited autosave time to 15 minutes minimum, and set default time to 30 minutes.  (Dedicated Server) Autosave is now triggered instantly when the last player leaves the server  (Dedicated Server) Autosave is now only active if there are players connected to the server  (Dedicated server) Fixed some spamming enemy errors in dedicated servers  (Optimization) Reduced overall cpu usage when enemies are enabled on a dedicated server  (Multiplayer) Added “Experimental” text to dedicated server source buttons in game browser to clarify the current state of the feature |
| v0.59b | DS – When attempting to connect to a server that is not configured correctly, players will now receive an error message and be returned to title screen DS – Player list in game now shows amount of players in game  DS – Fixed basic fires not lightable by clients after loading into games  DS – Added a version check to servers. This will inform players if the dedicated server they are attempting to join is from a different release than the current build they are using. Players who see this message should make sure their game is up to date, or alternatively try a different server as server may not be up to date  DS – Connecting to a dedicated server now shows a client connecting message during the initial stages  DS – Join server button on dedicated server has been renamed from ‘new’ to ‘join’  DS – Prevented dedicated server from saving quality presets |
| v0.59 | Added experimental support for players to host their own dedicated servers Added new dedicated server tool (downloadable via tools menu in steam) |
