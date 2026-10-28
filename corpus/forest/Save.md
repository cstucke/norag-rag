# Save
Source: https://theforest.fandom.com/wiki/Save
Categories: Pages with image sizes containing extra px, Gameplay
Revision: 74519

Saving is a mechanic that saves the game, it can only be done on certain buildings and game objects. You cannot save the game in random locations without the use of Console Commands or mods.

## Function

For single player games it allows the player to save their position in the world and keep their inventory the same so they can safely quit the game and return to continue where they last saved.

For multiplayer or co-op, you can save at your respective positions in the world. When the host saves the game, it takes all current players and their inventories and remembers it. If you play with anyone, be sure to have them all online with you when you save as they can lose their data.

So its ALWAYS important to save the game before leaving an online server if you wish to return and have all the same items.

## Backing up/Accessing your saves

Step by step in how to get to your Save folder for Windows 8 and 10

1. Press the `Left Windows key` + `R` to bring up the find/search function.
2. Type in `%appdata%\..\LocalLow\SKS\TheForest` and click `OK`

* The Directory will look something like this: C:\Users\ \*\*Your Username\*\* \AppData\LocalLow\SKS\TheForest
* You can copy these files and back them up in a folder elsewhere.
* This is how you can move saves in between single player and multiplayer as well.
* ALWAYS back up your saves before doing any modifications.
* Opening older versions of The Forest MAY delete all your save games.

On linux save are inside: /home/ \*\*Your Username\*\* /.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/compatdata/242760/pfx/drive\_c/users/steamuser/AppData/LocalLow/SKS/TheForest/

## Saving Points

This is a list of buildings and in game objects where you can save.

| Name and Image | Building Requirements |
| --- | --- |
| Temporary Shelter | | 1 | **=** | 26 | **+** | 14 | | --- | --- | --- | --- | --- | | Temporary Shelter |  | Leaf |  | Stick | |
| Hunting Shelter | | 1 | **=** | 7 | **+** | 6 | **+** | 7 | | --- | --- | --- | --- | --- | --- | --- | | Hunting Shelter |  | Stick |  | Rock |  | Log | |
| Log Cabin | | 1 | **=** | 82+ | | --- | --- | --- | | Log Cabin |  | Log | |
| Small Cabin | | 1 | **=** | 13 | | --- | --- | --- | | Small Cabin |  | Log | |
| Tree House | | 1 | **=** | 35 | **+** | 1 | | --- | --- | --- | --- | --- | | Tree House |  | Log |  | Rope (optional) | |
| Alpine Tree House | | 1 | **=** | 18 | **+** | 29 | **+** | 1 | | --- | --- | --- | --- | --- | --- | --- | | Alpine Tree House |  | Stick |  | Log |  | Rope (optional) | |
| Bed | | 1 | **=** | 17 | **+** | 1 | **+** | 4 | | --- | --- | --- | --- | --- | --- | --- | | Bed |  | Stick |  | Rope |  | Rabbit Fur | |
| Orange Tents | Can't be built |
| Blue Tents | Can't be built |
| Yacht | Can't be built |

## Update history

| Version | Changes |
| --- | --- |
| v1.0 | Fixed the very first lag spike that use to occur when launching a game Food no longer loads in save games on fires  Added a confirm overwrite save feature  Fixed player name display on load save screen  Fixed stash item whoosh playing when loading a saved game  Fixed molotov liquid sfx playing when loading a saved game  Player can no longer save while doing other actions like entering caves or climbing ropes  Fixed missing dates on save slots in title scene |
| v0.72b | Fixed save system not always initializing correctly, possibly causing some player made structures to go missing such as log holders |
| v0.72 | (Multiplayer) Fixed ghost cranes not synced properly upon loading a saved game |
| v0.71b | Fixed old saves resetting the strength stat value (if not saved over) |
| v0.71 | (Performance) Moved asset preloading to before loading saved game, while the black screen is up rather than right after the game starts |
| v0.70 | (performance) Dead enemies are no longer saved in traps on loading |
| v0.69 | Fixed dying in the endgame area while not fighting the boss returning player to the hanging scene without properly unloading the endgame and cleaning up relevant data, leaving game in an unable to save state and with broken lighting outside Caves – Added save tent towards end of game |
| v0.68b | Fixed chainsaw not working after loading a save if it was equipped while saving |
| v0.68 | Added a fail safe when loading a save saying player is in caves to ensure he is actually above terrain, this should work around rare/edge cases or bugs that could lead to save with the wrong in-cave data and wrongly drop player below terrain upon loading the save (Multiplayer) Fixed an issue crane data initialization when loading a save causing crane to be wrong size for clients and the bottom trigger grab icon to not be visible |
| v0.66 | Fixed very large save games sometimes crashing on load on 64 bit systems Fixed loading saves with toy not initializing properly all renderers |
| v0.64 | Fixed save game timestamps not showing correct save time or correct amount of days survived Fixed tree stumps from old saves not being cuttable in newer builds Added collision to trapped enemies in saved games |
| v0.62 | Switched stick marker and sled flag icons to new system (same has house icon on shelters). On the first time loading an old save it tries to match the former color to the closest available color Fixed loading a save with chainsaw fuel fully depleted not updating the fuel UI properly Contents of catapult's basket is now saved Fixed passenger manifest being invisible if players tried to take it for the first time from a saved game Fixed bonuses from upgrades on weapons not properly restored after loading a saved game (retroactive !) |
| v0.61b | Fixed issue with regrowing trees in MP games causes them in some saves to not be cuttable on load Fixed some issues with storage and water holders for clients in some saves |
| v0.61 | (Multiplayer) In-cave flag is now stored in player data, this will prevent the cave not loading properly issue for clients saving in caves around the sinkhole (not retroactive for saves already broken but compatible with working saves and prevents the issue from that point forward) |
| v0.60b | Prevented repair system from wrongly prompting player for repair in the event of having deprecated HP data in old saves |
| v0.60 | (Dedicated Server) Autosave is now only active if there are players connected to the server (Dedicated Server) Autosave is now triggered instantly when the last player leaves the server (Dedicated Server) Limited autosave time to 15 minutes minimum, and set default time to 30 minutes. (Dedicated Server) Clients now know the game was saved server side, and see a “Server is saving the game” message if saving takes too long |
| v0.58 | Added a failsafe in case inventory was saved with some missing/destroyed inventory views so that it keeps functioning regardless |
| v0.57 | Optimized animal and enemy traps to only spawn in nearby caught animals and enemies instead of loading in all of them to improve memory use in large saves |
| v0.56c | Fixed excessive memory when opening save menu which could often result in out of memory crashes when saving. |
| v0.56 | Flashlight will no longer be replaced with lighter when loading a save whilst holding flashlight Added fail safe in inventory when loading a save to prevent losing an item if an issue occurs while restoring an equipped item Trapped enemies in happy birthday, Noose and Dead Fall traps, are saved and loaded. (loaded enemies in noose trap will always load in dead) Pedometer now saves the steps walked when you save the game Rock swing trap now properly saves the attached tree ID and also preserves it when rearmed (not retroactive) |
| v0.55 | Fixed a couple rare errors that could prevent a few wall chunks from showing up in saves that suffered data loss after a patch Improved support for updating greeble zones data from old saves, should prevent cases of deprecated data causing error spam and causing severe lag Trapped animals remain in traps after save/load |
| v0.54b | Fixed bug with some caves not loading in saved games for clients |
| v0.54 | Fixed some issues with restoring meat decay state after loading a saved game Fixed some issues with restoring arrow bonus after loading a saved game Fixed log cabin sleep and save icons remaining visible if active when a wall is destroyed Fixed loading a save outside of caves but in sinkhole not enabling cave grounds properly |
| v0.53b | Fixed save game ui issue where single player games would say they were multiplayer saves (had no effect on saves themselves, only the ui text) Fixed changing Steam user in the save slot window in game not properly refreshing in single player |
| v0.53 | Fixed incendiary upgrade of the upgraded spear not restored after loading a save Fixed small cabin having the save icon always visible Save slot selection screen in title screen now allows to switch to saves from another Steam account than the one currently logged in (if there are multiple on same pc) |
| v0.50b | (Multiplayer) Fixed bug when attempting to load and play an old saved game with more than 20 holes in a floor (Multiplayer) Fixed a specific race condition when launching game causing client to fail to joining saved games |
| v0.50 | Fixed some structures not getting cut from nav mesh correctly on loading a saved game (Multiplayer) Fixed stone caches loaded exploded from a save not properly working for clients Fixed story item pickups respawning when game was saved/loaded |
| v0.49 | (Performance) Fixed excessive overhead occurring when loading saves with huge amount of player made structures, possibly using 50% CPU for up to several minutes after black screen goes off Exploded state of caches is now saved Difficulty mode is now saved in the upper node of the save file and visible in title screen save slot thumbnails |
| v0.48 | (Multiplayer) Fixed some issues with tree save states being different between host and client depending on where client was when trees were cut down or game was saved |
| v0.47d | Added fail safe to attempt recovering data loss in wrongly saved autofill wall chunks – Note: some walls will need to be rebuilt in game to function correctly |
| v0.47c | Fixed bug with some save games not loading |
| v0.47 | Fixed meat not set to back to the saved decay state after loading a saved game |
| v0.46b | Fixed some items being impossible to select in inventory with new snap controller system in old saves |
| v0.46 | Fixed a bug when loading a save with ceiling skull lamps causing it to not be properly toggled on/off based on distance with player |
| v0.45 | (Multiplayer) Fixed issue with missing buildings for clients when loading a saved game with lots of structures (instead of attaching all buildings at once they will instead be attached to the networking system up to 100 at a time per frame, this delays just a little the time it takes for everything to show up on clients and should likely be unnoticed) |
| v0.44 | Walls/Fences and Floors/Roofs each save and restore the latest autofill/manual mode |
| v0.44 | Fixed loading game on a computer for the first time clearing cloud saves! |
| v0.43b | Fixed max amount bonus from having stick or rock bag in inventory stacking up each time a saved game is loaded |
| v0.43 | Fixed some structures not getting cut out of nav mesh correctly on loading save game |
| v0.42 | (Multiplayer) Fixed ghost tree structures loaded from a saved game not getting removed if tree is cut down Added new cheat code: “woodpaste”. Can be used to reset floor & roof holes in a saved game. Cheat works once when game is started then gets reset when going back to title screen. Does nothing for MP clients (Multiplayer) Fixed client not seeing host climb rope animation, if loading a save game with no weapon equipped It is no longer possible to place items such as bomb when in range of an interacting trigger (such as save trigger from shelters) to avoid blowing yourself up when trying to save with C whilst also holding a bomb. (Multiplayer) Fixed distant cut down trees not refreshed and showing billboard when late joining a game or joining a saved game Fixed a bug when loading a saved game without owning plane axe preventing inventory system from functioning, notably causing both inventory and book to be impossible to open (Audio) Fixed some environment SFX (like waterfalls) not working after loading a saved game |
| v0.41b | Fixed loading saves with buildings ghost past ingredient requirements, it now automatically completes it (to fix rare cases of this occurring) |
| v0.41 | Fixed plane lod being drastically lower in save game versus new game for interior |
| v0.40 | New difficulty changing cheat code: rawmeatmode ! Enables perma death mode, can be turned off by typing vegan, vegetarian or meatmode. In this mode the second death in single player deletes the save slot and after loading a saved game or having saved once in a new game, it is no longer possible to save in another slot. |
| v0.39 | (Multiplayer) Fixed lock on distant doors loaded from a save file unusable for host (Multiplayer) Fixed story clues not showing up after loading a saved game for client (retro active) (Multiplayer) Fixed walky talky not working after loading a game that was saved in SP |
| v0.38 | Caves- added more save tents deeper inside caves Fixed ghost rock holder loading from save file as a stick holder |
| v0.36 | Effigies now save burn status and done duration Paint on weapons is now saved Blood on weapons is now saved Fixed lighting fires loaded from a save with 0 fuel causing errors and killing performance Fixed some issues loading saves with meat in inventory (Multiplayer) Fixed loading save as host sometimes causing duplicate ghost bridge to show up client side |
| v0.35 | Fixed destroying nested building from old saves causing damage to parent structure, they no longer propagate any damage if not having the right destruction setup Fixed skull lamps sometimes not visible after loading a saved game Fixed cave map sometimes not loading correctly from saves (Multiplayer) Fixed loading a saved game inside yacht as client causing player to swim and see ocean through yacht Now saving which garden blueberry have already been used so that gardens no longer respawn at full yield after loading a saved game if previously consumed Added Steam username display in save slot screens of title scene, defaults to Anonymous if not connected, should make it clearer that you have to be connected to your own account to see your saves and avoid feel of having lost save files (Multiplayer) Fixed high CPU usage when loading old save with tree structures attached to trees that no longer exists |
| v0.34 | State of cave enemy encounters are now saved! Instead of all the mutants respawning when you re-enter a cave. |
| v0.33c | Fixed performance issues in save games where players had rabbit fur boots |
| v0.33b | Fixed issue with cutting down trees in some multiplayer save games |
| v0.33 | Fixed stick marker overlay flag icon sometimes missing in old saves Fixed issue with garden preventing to load properly from a save if it had planted seeds most player built wood-based structures are now destructible ! (Not retroactive: already built structures in saved games will remain not destructible, but newly built ones will be) Fixed tree stumps spawning wrong model in saved games Fixed cut up tree stumps being wrong size for some tree types in saved games Fixed an issue with saves that have rabbit fur boots equipped, was stacking bonuses each time game was loaded |
| v0.32 | Fixed bug with saved games stumps removal Fixed an issue with auto cloud save Fixed sleeping not available out of the box in really old saves Fixed Grass/Shadows/Low memory settings not saved/restored properly |
| v0.31 | Texture quality setting is now properly saved and restored |
| v0.30 | Passenger manifest is now retrievable from plane in save games if it was not retrieved previously |
| v0.29c | Fixed issue with some walls or fences appearing unfinished in older save games even if they were previously completed |
| v0.29c | Fixed a bug with stealth icon not operating correctly in some old save games |
| v0.29b | Fixed some issues with some save games conflicting with latest todo list save system |
| v0.28c | Fixed cave map not loading correctly when save was done in the outside world Fixed passenger manifest not loading correctly with saves done in previous versions |
| v0.28b | Fixed plane missing collision in save games |
| v0.28 | Fixed Cave Map not restoring map properly after loading a saved game Cut down thin trees are no longer loaded in saved game as tiny floating pine tree stumps |
| v0.27 | (Art) Torn version of blue tent added (can't be slept in or used to save game) |
| v0.26d | Fixed a case of save with bridge not loading |
| v0.26c | Fixed issue with saving a game if no previous save game existed |
| v0.26b | (multiplayer) Fixed loading save file with custom rope sometimes breaking loading (multiplayer) Fixed loading save file with fires erroring Empty save slot can no longer be clicked to load from |
| v0.26 | (multiplayer) Fixed a case of save failing for clients (performance) Combined ocean/lake depth passes to save memory Fixed raft sometimes being unusable after loading a saved game Garden revamp: Seeds are now added one by one and spawn little dirt piles in the garden. Plants grow visually over time and provide from 1 to 3 of their respective yield based on growth time. Plants die after 1 to 2 days (depending on plant) at max yield. Plants growth timer now properly saves as well as account for slept time. Hitting escape while in options in game now saves it You can now save/Sleep at the tents in world and in caves! Added a safety net to bridge saving, to allow recovering it if anchor data gets lost. This isn't retro active, broken bridges are gone but all the new ones as well as working ones from saves will make use of the system after saving |
| v0.25 | (multiplayer) Fixed issue with scale of fire after loading a saved game in multiplayer |
| v0.24b | Fixed issue with lighting arrows when having more than 12 arrows in a saved game |
| v0.24 | Fixed bug with ghost skull decoration when loading a saved game Fixed some survival settings (starvation/thirst/cold) broken after loading a saved game, causing for example breathing duration to be really small Fixed issues with save files date not displaying sometimes |
| v0.23 | (multiplayer) Fixed client not properly waiting for building bellow to be loaded before removing black screen, thus causing to fall down below (when game was saved while on a player made structure) |
| v0.23 | Fixed some bugs with fire particle size when fires were re-lit and stocked after loading a saved game |
| v0.22 | (multiplayer) Fixed bug where client entering save game would hear multiple building complete sounds (multiplayer) Fixed clients having lighter stuck after loading a saved game with lighter equipped (multiplayer) Fixed partially cut down trees saved as cut down in MP Pressing escape while in save screen now properly closes it Fixed ghost wall defensive not saving properly (retro compatibility hack might cause old saves to have an overlapping log in between chunks) |
| v0.21c | Fixed bug where some old saved games wouldn't load Fixed bug where equipping some items in left hand in old saved games could break items/cause items to vanish |
| v0.21 | Following features now require to hold their respective button for half a second to be triggered: cancel ghost buildings, drink & gather water, procedural buildings auto fill, eat berries and mushrooms found in world, eat plane food, eat cooked/dried food, light fires, save, sleep Clicking back button of option menu now saves settings (was done in following menus until now) (multiplayer) Fixed loading a game saved in caves as client Gamepad mappings are now properly refreshed when a new one is plugged in and each gamepad has its settings saved independently |
| v0.20b | (multiplayer)Fixed an issue that could cause abnormally long save times or crash game (multiplayer)Fixed possible drastic performance drop if player was cold as host and loaded a saved game (possibly only relating to 0.19 saves) (multiplayer) fixed an issue where if you attached a bridge to a tree platform, neither of them would replicate out to clients after loading a save possible fix for issues with logs not visible in lod sled or log holder for older save games (not able to reproduce here, let us know if its still happening) |
| v0.20 | Partially cut trees are no longer saved as cut down, instead they are fully restored when loading a saved game Eaten berries & some bushes no longer respawn after loading a saved game (multiplayer) Fixed not being able to continue saves as client (multiplayer) Loading a game saved on a building as client should now respawn on top of it (multiplayer) Fixed client not seeing present ingredients in ghost buildings until some more were added after host loaded a saved game Fixed error in story clue folder when loading a saved game Improved look of save game thumbnails & added date/time (community request) Loading a save with a bridge not attached to anchors now destroys it instead of erroring (could block loading in mp) |
| v0.19c | Fix issue where multiplayer save game issues would occur if a tree with a tree platform and connecting bridge was partially cut before saving. |
| v0.19b | Fixed issue with saved games for players using a fresh install of game. |
| v0.19 | (multiplayer) Fixed issues with log sled after loading a saved multiplayer game (multiplayer) Clients now have a different save per server and respawn after loading where they saved instead of in plane (respawn after dying is still located in plane) (multiplayer) Fixed a bug with experimental stairs in saved games which could cause issues for clients loading Fixed several tree structures which did not properly save which tree they are built on (not retro active) Fixed tree structures not getting destroyed when their attached tree is found cut down after loading a saved game New save slot system, you can now have up to 5 SP games and up to 5 mp games (as host) Save slots are organized per steam user id to prevent cloud from messing things up when using the game with multiple steam accounts on a single computer Saving now archives the previous save file in case you need to restore a backup (local only) New save slot selection screen when saving in game Save black screen is now in sync with the time saving takes Improved cloud save management Fixed a save/load issue that could cause experimental walls to increase size of save game drastically and crash loading Revamped multiplayer start game UI to be compatible with gamepads and save slot system |
| v0.18c | Metal door now has a trigger on the other side that completely opens the door once crossed (to fix issue if anyone saved behind it) Fixed loading a saved game with a plastic torch equipped stuck |
| v0.18b | Fixed bug where anchors on foundations could cause issues and break save games! Fixed old plane seat models loaded after loading a saved game |
| v0.18 | Fires now properly save their fuel amount and lit state |
| v0.17b | Fixed loading a game that was saved inside a cave (not retroactive) |
| v0.17 | Fixed item holder being empty when loading a saved game as host |
| v0.16 | Fixed rebreather's air resetting to 0 after loading a saved game |
| v0.15 | Fixed loading upgrades from saved games (not retro-active) When the game is already started and an MP invite arrives, player can now choose to either start a new game or continue with his saved MP character Fixed hydration icon fill values not set properly after loading a saved game at full thirst |
| v0.14 | Added monitoring system to alert players if their save game has been corrupted beyond repair Save script now uses the grabber system (adding items to item holder next to a shelter no longer saves the game unexpectedly) |
| v0.13b | Fix for broken saved games (dark shadows, no time passing, sleeping at shelters broken and lots of other bugs in corrupt save games, along with low performance due to error spam) |
| v0.13 | Fixed trees initializing after black screen removal when loading a saved game |
| v0.12 | MP Client loading added – will now keep client player stats and inventory when client continues a multiplayer game (buildings are still saved on server) Fixed crash clearing not removing trees on loading a save game (fixing issue where trees would sometimes block exit from plane or from home you've built near crash site) |
| v0.11c | Fixed error with multiplayer save games sometimes breaking due to racing condition with data fetching in gui. Fixed some issues with single and multiplayer save games when a large amount of buildings were built. |
| v0.11 | Multiplayer save/load added Note: Currently limited to server being able to load the savegame, clients will start game fresh each time but still be able to enter a previously saved hosts game. Server/host will be able to save state of game world/structures. Steamworks saving to cloud added – Regular save/load still works however it will now try and load from cloud first and pick most recent file (We’ve just hit the checkbox to enable this, it should be available soon) |
| v0.10 | Re-worked save game system so future updates will (likely) not erase save games to work! |
| v0.09 | Fixed bug where building a bench could cause save games to break |
| v0.08d | Improved raft and fixed issues with raft and save/load |
| v0.08c | Out of date saved games will now be ignored, instead of attempted to load if incompatible with latest patch (clicking load on these will start you back on plane) Fixed issue where buildings would disappear from your save game and you would have to load from a fresh game to see them. (this one was hard to track down! let us know if it's still happening for anyone after this update) |
| v0.08b | Fixed some player stats not being set on load save game (lizard armor, hunger etc.) Fixed bug where cut trees were not saved the first time you saved/loaded a game Fixed suitcases around plane not having working pickups on loading a saved game rabbits should now be saved in rabbit cages on save/load Fixed upgrades not showing on weapons after loading a saved game |
| v0.06 | You can now save your game at a shelter without sleeping Fixed plane seats vanishing on loading save game |
| v0.04 | Fixed bug where some partially built structures couldn't be completed after loading a saved game Yacht random position won't change now or get lost when saved game is loaded Fixed fullness always starting at half when loading a saved game Fixed stick marker vanishing on loading saved game |
| v0.03 | Partially built structures are now saved |
| v0.02 | Fixed some items not being saved in inventory when game is loaded (some might still vanish, expect more saving fixes/improvements soon) Fixed log holder not saving logs on load/save |
