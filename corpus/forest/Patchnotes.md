# Patchnotes
Source: https://theforest.fandom.com/wiki/Patchnotes
Categories: The Forest Wiki
Revision: 72346

Here's is a compilation of all officially released patch notes and information about the different versions of the game. The most recent alpha build is V1.12 - VR.

Versions History

# v0.71 (released December 15, 2017)

* Added new electrical tape pickup
* Added new modern arrow pickup
* Explosives now require electrical tape to be crafted
* Electrical tape can now be found in some suitcases
* New craftable weapon added! To make a slingshot combine 1 stick, with a cloth and electrical tape. Use small rocks for ammo.
* Small rocks are now collected directly to your inventory
* (Performance) AI of enemies optimized
* Reduced stutter from navmesh update when new structures are completed
* Fixed enemies not positioned on ceiling correctly in caves
* Fixed player able to get stuck if entering a rope trigger while knocked down on ground
* Fixed enemies not drowning for clients in caves while host is in overworld
* Fixed camera shake missing from explosions
* Fixed player movement getting locked if getting hit while holding the catapult
* (Performance) Improved clean up speed when closing game or after finishing game fixing issue where it would appear the game had crashed before entering end cutscene
* Fixed partially burnt plants that are returned to the pooling system after going away before it finished burning not resetting the burn effect properly and looking partially burnt when reused
* (Performance) Plant burning system no longer needs to duplicate materials
* (Multiplayer) Fixed tortoises sometimes disappearing for clients while hiding in their shell
* Fixed trap icons visible with the ShowHud option off
* (Multiplayer) Fixed bats not being affected by explosions for clients
* Fixed a case of player throw animation getting stuck on after jumping
* Fixed fish getting thrown very far when blown up with explosives
* (Multiplayer) Added in controller support for invite menu
* (Performance) Shorter trunks on trees (previously some would extend far below terrain even though they were not visible)
* Fixed issue with taking damage while filling waterskin causing icon interaction to break and making player unable to switch weapons
* (Performance) Moved asset preloading to before loading saved game, while the black screen is up rather than right after the game starts
* Fixed gamepad back button sometimes not working after using a menu
* (Performance) Slightly optimized enemy encounter objects spawning CPU cost
* Fixed a case of getting cold in caves due to rain outside
* (Multiplayer) Fixed clients sometimes unable to kill fish with the spear
* Fixed some story items in inventory not having correct outlines
* Fixed enemies sometimes ragdolling weirdly when caught in traps
* Fixed enemies sometimes not placed correctly when caught in happy birthday trap
* Turned down intensity of cave worms
* Fixed players sometimes swimming at wrong speed after colliding with ROV objects when underwater
* Fixed enemies being difficult to set on fire when caught in a HBD trap
* Fixed enemies sometimes getting stuck in burn animation loop forever
* (Translations) Setup the various loading and error message in the MP screen to be translated, currently translated to: french
* (UI) R/L gamepad button icons are now bigger
* (Multiplayer) Moved prefab database warm up to when actually starting a game instead of when loading the MP start scene to smooth out menu navigation and hide the hiccup with a proper black screen
* (multiplayer) Fixed bodies not dropping from happy birthday traps when reset for clients
* Fixed player occasionally getting stuck underneath terrain when letting go of a climb out rope near the very top
* Fixed player sometimes rotating away from cliff face when first using climbing axe on a cliff
* Fixed finalizing roof with the Build action not working (was accepting Fire1 only)
* Numerous improvements to MP scene navigation when using a gamepad, including using Back button (B on Xbox gamepad, Circle on Dualshock) to go back to previous screen
* Fixed current book entry not properly selected itself after placing a ghost and going back in book when using a gamepad
* It is now possible to close book and cancel ghost placement with Xbox gamepad B button or dualshock Circle button
* Fixed forcing cursor back in center after opening inventory
* (Multiplayer) Reduced stutter on falling trees that could sometimes happen for clients
* Fixed crafted club not doing correct ground attack animation
* Action icon is now hidden if there's no mapping for it instead of showing the default sprite (i.e.: the Utility action with dualshock gamepads)
* Fixed timed out / kick message not closable when using a gamepad
* Nutrition System Revamp: Consuming edible items now yields calories on top of fullness, doing physical activities counts as burnt calories and strength, excess calories are resolved and transformed in weight and strength gain or loss
* Cave 2 lighting improvements
* Calories are now listed in the food and drinks when hovered over in inventory
* New craftable item: Small rock bag increases how many small rocks you can carry.
* Some yellow crates have modern arrows now
* Fixed some cases of enemies getting stuck running against walls inside enclosed areas
* It is now possible to tape plastic torches onto the bows, the flintlock and the chainsaw
* It is now possible to have more items than what a recipe requires to complete and doing so will leave the unused ingredients on the crafting mat along with the created item (i.e.: can add all booze and cloth to the crafting mat, and thus quickly iterate through the molotov making process)

## v0.71b (released December 19, 2017)

* Fixed dying with toggle crouch on causing issues in hanging cutscene
* Fixed old saves resetting the strength stat value (if not saved over)
* Calories system balance pass, should make weight and strength more manageable
* Fixed dried meat eaten from inventory having the calories applied twice
* Added calories display in stats page
* Fixed blue berries, soda, fish, generic meat and oysters yielding wrong calories amount or having wrong displayed amount
* Fixed crafting recipes with overlapping ingredients and different costs not completable before having done the recipes will fewer ingredients. It will now check all valid recipes and pick the completed one with highest amount of ingredients, completing ones with fewer ingredients can be achieved by having less ingredients on the crafting mat than other recipes require (i.e.: it is now possible to make rabbit fur boots before the small rock bag)
* Fixed shoes vanishing when on turtle shell sled
* Fixed colliders on tennis players being too large

# v0.70 (released November 18, 2017)

* Fixed second arrow appearing if fire button pressed immediately after releasing an arrow from the bow
* (multiplayer) Fixed fireman cannibals appearing with wrong texture as client
* (multiplayer) Fixed birds disappearing if shot with a flare gun as client
* Added new recorded dialogue to end game sequence
* Fixed lizards occasionally becoming invulnerable to damage
* Fixed bodies on fire not blowing up from explosives
* Adjusted look sensitivity when using a gamepad to allow for more precise aiming with bows and other projectile weapons
* (UI) Action icons are now twice as big when using a gamepad
* Book navigation with a gamepad should now be a lot simpler, it will no longer go through tabs and links in bottom right page and instead display the PrevPage / NextPage action icons that should be used
* (Multiplayer) Fixed adding ingredients to a stew as client not updating cooking time for all players
* Using the chainsaw with a gamepad now has a vibration effect ! (requires the XInput option to be on for most gamepads)
* Added new art for the collected coins and cash in inventory
* (performance) Dead enemies are no longer saved in traps on loading
* Fixed rope not attaching to enemy properly when noose trap was triggered
* Fixed missing collision from the deadfall trap large log
* Fixed Happy Birthday trap missing collision sometimes after being repaired
* Fixed navmesh not being updated correctly when some structures were destroyed
* (multiplayer) fixed clients able to see other player on floor during first part of plane crash sequence
* Fixed spears sometimes disappearing if player was hit while throwing a spear
* (multiplayer) Fixed clients unable to pick up rabbits from animal traps
* Fixed cowman exploded gibs never being despawned
* Fixed player able to throw projectiles while in knocked down state
* Fixed player sometimes getting thrown into air after skinning animals
* (Balance) Reduced damage from arrows on modern bow slightly
* Fixed creepy enemies not reacting to players when shot from a distance
* Fixed players unable to throw spear while airborne
* When holding a burning stick, player will do the regular downwards ground attack
* Fixed birds sitting on structures not flying away when structure is damaged or destroyed
* Fixed player not performing proper downward jumping attack with a held rock
* (Performance) Main camera is now disabled while in inventory which greatly increases FPS and locked fps in inventory to 60fps.
* (UI) Items inventory tooltip is now bigger
* Fixed targeted button in book changing when switching page with L/R gamepad buttons
* Book now always uses snapping with a gamepad
* (Performance) LOD distance calculations are now offloaded to a secondary thread lowering the cpu cost
* (UI) New cursor in inventory.
* Adjusted cursor sensitivity when using gamepad in inventory
* Fixed animation sync issues with picking up megan in the end game
* Fixed throw animation not playing if throwing molotov while airborne
* Fixed opening survival book while holding megan causing player to move at wrong speed
* Player no longer plays hit animation from thirst damage while aiming or holding book or lighting fires
* Added small amount of blood effect when taking thirst damage
* (Performance) Added a threshold to the activation range of greeble zones when already visible to prevent it from ever going on and off when standing at the toggling range
* Locking tree structure to trees now uses the same raycast system as anchors which is going to accurately pick whatever tree is currently targeted instead of the legacy fiddly way
* Simple rumble setup for when attacking & getting hit when playing with a gamepad (tested only on Xbox controller)
* (Performance) Terrain pixel error no longer takes screen height into consideration
* Fixed stuck arrows not falling from trees when tree is cut down
* Deprecated the “Gamepad cursor mode” option
* Added “Gamepad Rumble” option
* The construction UI now snaps towards player at a lower angle than previously
* Hand cursor icon is no longer visible when using a gamepad in book
* Added new recorded dialogue to end sequence of game to fix what sounded like a bug with end cut-scene
* Survival Book – added numbering to custom building and decoration/furniture pages to match tabs
* Fixed enemies sometimes falling asleep in front of the player while in caves
* Added missing note tabs in book
* Added gamepad action icon in book
* Tweaked highlighted tabs display to be easier to read
* Light burnable item tutorial now displayed for all burnable items
* Zipline rope now renders as far as its wooden gates
* Small rocks now require to hold the “Take” button for 0.5s to pickup
* Eating dried meat now gives 5% thirst in Normal mode and 20% thirst in Hard Survival
* Dualshock 4 touchpad button now opens inventory
* Navigating book and inventory with a gamepad now uses the Horizontal & Vertical axis (left stick by default)
* Water based cave entrances now have an enter/exit system similar to land based entrances
* (Hard Survival) Fixed single player inventory time pause not working in hard survival mode
* (Hard Survival)Food fullness amount set to same as normal mode
* (Hard Survival)Meat spoil time same as normal mode
* (Hard Survival)Reduce dehydration increase rate back to default
* (Hard Survival)halved hydration gain from berries
* (Hard Survival)Reduced amount of turtles and birds in hard survival mode
* Thirst damage now ticks every 30s (from 8) and deals 11 damage (from 2) in normal mode, and 27 damage in HS
* Going to book index when using a gamepad automatically select the Fire chapter button and index button is no longer accessible while in index
* (UI) while having items on the crafting mat It is now displayed that you can press the Drop button to clear out everything
* (Performance)Improved cpu performance when loading into cave reducing the amount of stutters
* Adjusted timing of load when exiting a climb out cave to reduce visible pop in of trees
* Increased speed and hit damage from boars
* (Performance) Fixed chainsaw smoke drift causing significant allocations
* Standing fires no longer set fire to player, enemies or animals
* Fixed fire arrows on modern bow not lightable from standing fires
* Improved underwater player movement: player will now sink in water if looking up and moving backwards
* It is now possible to gain specific bonus when cooking a stew with various ingredient combinations
* It is now possible to gather boiled water from pot using a waterskin or even another pot
* Less small rocks will now spawn in world
* Performance – lowered distance decorative ground sticks (not pickups) spawn
* Performance – optimized collision physics on animals
* Slightly reduced animal spawn distances from player
* Player will now shine light on held story item pickups when plastic torch is equipped
* Mushroom stumps can now be destroyed by hitting them!
* Fixed log sled occasionally flipping up wildly when full of bodies
* Fixed boars sometimes not targeting player correctly when attacking
* Player can no longer do downward axe attacks while crouching and head height is blocked by a low ceiling
* (Performance) Animal shadows are now disabled at distance from the player
* Fixed aim down sights mode getting stuck on if inventory was opened while in aim mode
* (Performance) Optimized Fish AI and animations
* Fixed burning bodies in sled causing body to burn forever
* Blocked equip weapon from inventory while placing building
* Poisoned weapons will now display a visual
* Enemies will now tend to keep their distance if player is already surrounded by enemies
* Fixed a case of enemies sometimes stuck running in circles
* (Performance) Pooling system now handles better mass despawn of a single object type, this will prevent spikes when leaving dense areas, with many ferns for example
* Lowered amount of bird landing spots on birdhouse
* Fixed adding empty pot on fire in SP having water

## v0.70b (released November 20, 2017)

* Fixed drinking boiled water from pot not providing hydration
* Fixed draw distance on lizards and rabbits being too close causing them to pop on
* (Multiplayer)Fixed a case of enemies sometimes not spawning in caves for clients
* (Multiplayer)Fixed a case of enemies not drowning when underwater
* (Multiplayer)Fixed a case of in cave status staying on for clients if they exited a climbing exit whilst climbing very close behind another player

## v0.70c (released November 21, 2017)

* Improved performance of bone chandelier
* Fixed some cases of terrain collision not loading correctly if game was saved inside a cave

# v0.69 (released October 20, 2017)

* (Audio) Nitrogen tanks now play an air hiss audio event when stuck and about to explode.
* (Audio) Adding a stick to a trap in order to reset it now plays an audio event.
* (Audio) Turtle sled now plays a snow texture on top of turtle shell event when used on snow area.
* (Audio) Polished audio events for molotov, flare and dynamite when holding and then throwing. Flares also now emit a burning sfx after thrown.
* (Audio) Fixed bug where dropping bodies on some rock types wouldn't trigger a body drop audio event.
* Fixed cave map in inventory not showing the hovered outline
* Fixed dying in the endgame area while not fighting the boss returning player to the hanging scene without properly unloading the endgame and cleaning up relevant data, leaving game in an unable to save state and with broken lighting outside
* Fixed megan sometimes disappearing if player gets hit while while picking her up in the end game
* Fixed held logs colliding awkwardly when quickly dropped by player
* Lowered Birdhouse build log cost to 1
* (multiplayer) Fixed tortoise ragdolls causing frame rate issues as host in MP
* Optimized dead shark ragdolls when players are far away
* Optimized animator cpu usage on lizards
* (Performance) Inventory & book are now kept outside of the player hierarchy at runtime which frees 2-3% of the total CPU usage while moving around
* (Performance) Setting shadow quality to low or lower now disables shadow casting from the lighter
* (Performance) Far shadows are now always disabled while in caves
* Fixed greeble layer sometimes throwing errors and breaking the work scheduler, thus preventing it from further updating the environment
* (performance) yacht collision and interior objects are now disabled unless player is close by
* Added Hard Survival game difficulty, playing in this mode will cause less animals and fish to appear in world, and with a longer respawn after killing them. Greater & faster cold penalties. Fire has been made more dangerous to the player. More food required per meal to fill stomach. Thirst comes faster. Slower respawn on gathered herbs. Meat spoils faster. It's easier to get sick or infected and there are greater penalties from sickness and infection. A rebalancing of poisonous food, drinking bad water and eating out of date food. Along with this there is a much lower amount of spawned suitcases.
* Caves – Cave 8 cleanup and improvements
* Caves – Added save tent towards end of game
* Caves – fixed holes in caves 3,6,7
* (performance) Optimized cpu usage on enemies that are far from the player
* Fixed creepy female sometimes not attacking player when close
* Updated model/texture of rusty axe
* Cooking pot on fire is now slightly bigger
* (Multiplayer) After an attempt to join a game that banned you, fixed further attempts to connect leaving game stuck on “starting client…”
* Improved fire on enemies and player texture resolution
* Fixed player net shark head held being wrong version
* Fixed Pacifist achievement wrongly unlocking after 10 days during which enemies have been killed
* (performance) disabled physics on doorways when players are far way
* Fixed Vegan & Survive The Forest achievements not obtainable if creative mode is already available
* Optimized some areas around lakes with excessive seaweed underwater
* Fixed masked enemies sometimes appearing with invisible bodies
* You can now poison most weapons by combining them with poison berries, or poison mushrooms.
* Taking items from the sled while already at max capacity for that item will now drop it to the ground
* The list of possible recipe displayed while combining ingredients on the crafting mat now shows only distinct entries (i.e.: 3 recipes yield a poisoned plane axe, it will display “Poisoned Plane Axe” only once instead of 3 times)
* Fixed enemies sometimes still animating after being killed in a hbd trap
* (Performance) Now scaling down shadows at dawn and sunset to prevent it from stretching far away and causing excessive amount of objects being rendered and hindering performances
* Gathered herbs now take 1 in game day to respawn
* (Translations) Updated translations with some of recently added texts as well as some translation fixes
* (Translations) Fixed regression with book camera management that prevented translation tags from being visible
* Weapon speed calculation now clamps negative values so that a slow weapon like the crafted axe with full damage upgrade doesn't end up with wrong animation speed value and is unable to properly cut down trees
* Caves- fixed polaroid pickup in cave 8 not showing up in book
* Arrow basket now stores the type of arrow that was added (SP only at the moment)
* (multiplayer) Fixed an issue with clients sometimes taking damage when starting on the plane
* It is now possible to add pot without water on the fire, it will be possible to pick it back up after 40s if nothing is added to it
* It is now possible to cook a stew with the cooking pot ! After adding the pot filled with water on a fire, add a choice of 20 ingredients (8 meats, 6 mushrooms, 4 herbs and 1 berry and oysters), it will start a 30s cooking period after which stew will be ready to eat, providing hydration, fullness and other benefits based on recipe. Can remain on the fire up to 10 minutes. Note, you can also add ingredients to pot without water, however this will not provide hydration and will burn food extremely fast.
* Slightly reduced damage and firing range of crafted bow

## V0.69b(released October 21, 2017)

* Fire lit weapons not setting enemies alight
* Fixed missing arrow + jack mushroom = poison arrow recipe
* Fixed weird visual on the held poisoned plane axe
* Fixed stew being usable from distance when it completes if not targeting it
* Fixed boss disappearing if player died and respawned during fight
* (Multiplayer)Fixed boss monster sometimes causing players to lock into place depending on connection issues

# V0.68 (released October 5th, 2017)

* Fixed being unable to cut the rope during hanging cutscene after dying while sitting on a bench
* Player can no longer crouch while driving the logsled
* Improved model/textures for the first person rebreather geometry
* Fixed some cases of the player arms clipping with camera during attack animations
* Fixed rabbit skin boots disappearing sometimes while on turtle sled
* (Multiplayer) Fixed other players visible during opening plane crash cutscene
* Caves – most hanging bodies now have blood when hit
* (Performance) Cutting off bushes now properly brings it back to the pooling system to avoid unnecessary allocations
* Fixed death tutorial saying “you backpack” instead of “your backpack”
* Added trend display to strength in stats page
* Removed strength and athleticism red cross icons when having food & blood infection
* Stats page now displays an approximation of the Athleticism skill level progress as a decimal value
* Athleticism is now displayed on a 1-99 scale to match strength (underlying values remain the same)
* (Balance) Resetting traps now requires to hold the “Take” action 3 seconds
* (Performance) Animation cost cpu cost lowered by unparenting all right hand held items
* Nitrogen tanks can now be exploded with projectile weapons
* Fixed case of weapons not working after switching weapon while about to throw spear
* Fixed thrown spears disappearing after picking up speared fish
* (UI) Dying of thirst and starvation messages are now with other tutorials in bottom left, but with greater emphasis to showcase the urgent need to take action
* Strength now updates 100 times per in game day instead of once per day. This makes changes to strength easier to track.
* (UI) Better looking up & down arrows in stats page for Strength and Weight
* (Multiplayer) Fixed sharing newest items on tray
* Fixed a specific case of adding ingredients on the crafting mat that allowed to turn arrows into other types of arrows if having less than 5
* (Multiplayer) Fixed client players sometimes getting launched into sky when letting go of log sleds
* Fixed ‘close to wall’ weapon animation from activating when standing over downed enemies
* Fixed left hand items from clipping with body while on turtle shell sled
* Fixed some world collision issues
* Matched color of suitcase cloth with pickup and inventory cloth color
* Fixed case of uncollectable tennis ball on body in cannibal village
* Fixed weird square blocks visible when emerging from under geese lake
* Fuel canisters now have dynamics so enemies/players won't get stuck on them
* Dropped animal heads now have a sound effect when dropped
* Improved look of sharks and of dead sharks on beach
* Fixed a case of player able to attack indefinitely while blocking after doing a heavy attack
* (Multiplayer) When first joining a game as client, current time of day is sent and that time is used until the regular time sync begins, this will avoid having the sky visibly catching up when time of day data arrives
* (Performance) Tactical light turns off shadow when shadow quality setting is set to Low, Fastest or UltraLow
* (Multiplayer) Removed p2p host alt tab warning regarding clients disconnecting
* Caves – chainsaw moved to cave 3
* Optimized animator cpu usage when bodies are placed in log sleds
* Fixed missing lizard eye texture on held lizard head
* (Multiplayer) Fixed megan's body appearing offset sometimes when picked up by clients
* Fixed arrows freezing in mid air when shot towards end boss cutscene trigger
* Animal head pickups now have the trophy icon instead of the head icon
* Fixed wrong button icon in endgame section
* Added new particle effects to one of the endgame animations
* Fixed player not appearing in dead pose after dying in water
* Small cannibal benches and chairs are now breakable
* Updated model and texture of the red man
* (Audio) Changed use fuel sfx to twinkle instead of whoosh
* Setup stats page for new layout + added stealth + changed font
* Fixed opening book then inventory not equipping the previously held item back
* Fixed opening book from inventory not working
* Creative mode unlocked message is no longer displayed after finishing the game if already available
* Fixed cannibal village dead tree sometimes missing
* Fixed player head sometimes able to clip into wall of end game crawl space sections
* (Multiplayer) Fixed fire not visible on burning animals for clients
* Fixed meat not collectable from dead geese
* Fixed wrong texture on dead geese
* (Multiplayer) Fixed mutant babies and some enemies not appearing on fire when burnt to death
* Fixed issue with crocodiles not swimming in the water anymore
* Thirst damage now occurs on a 8s timer instead of a low random chance each frame and is displayed in hud like starvation, with the icon filling back up in red
* Thirst & Hunger damage message now flashes in red when taking a hit
* (Performance) Overlay icons logic is now batched to reduce the CPU overhead cost (should help on games with lots of shelters, cabins, tree houses, beds, stick marker, sleds with the overlay icon turned on)
* If trying to place a building on a dynamic scenery element, it will instead turn red and not be placeable (move the scenery prop first if location is desired)
* Filtered out some scenery elements like the huts in the cannibal village that can no longer be built on
* Sled's storage interaction scheme has been updated to match rest of game systems, it now has a widget to pick what to add when it's free based on what items player has available. \*When sled carries something it is as always limited to that one item type
* Improved look of blood on katana
* Fixed rocks spawning above cave entrances
* Stand & rockpit fires are no longer destroyed after burning out and don't turn into a half built ghost after being hit when lit
* Fixed area where player could swim under rocks, under a lake
* (Multiplayer) fixed some enemies not appearing with correct textures in end game section for clients
* Fixed some holes in world where cliffs connected to terrain
* Fixed some wrong regular grass cliff caps in snow area
* Fixed some cave holes and some cave pop in issues
* (multiplayer) Fixed rafts moving at different speeds sometimes
* Made rafts move overall slightly faster
* (Multiplayer) Fixed passengers manifest wrongly counting up and unlocking the achievement without actually discovering all passengers
* (Multiplayer) Fixed some possible errors in hud initialization when joining games as client
* (DS) It is now possible to join a server through Steam's server browser as well as through the “Join game” menu of the friend list when a friend is already connected to it
* (Multiplayer) Fixed defensive wall gate looking client side like it's quickly opening & closing when first built
* Loosened up positioning constraints to drink water at ponds, it is now possible to have water up to ankle level and it is not needed to look down as much as before
* Added new control option “Sprint Mode” allowing to choose between hold (legacy & default) and toggle, which leaves player running as long as he has stamina, the run button isn't pressed again, or movement stops
* Fixed players able to be set on fire while swimming
* Fixed a case of animals sometimes spawning underwater in geese lake
* (UI) Fixed offset in between fullness & starvation hud visual and underlying values
* Fixed repair tool sometimes having the wrong material after hitting animals
* All bodies accountable for on manifest
* Fixed a case of player able to get stuck in certain rock formations in over world
* Ai has been tweaked to help prevent players getting swarmed by many enemies in late game
* Fixed grass displacement object becoming visible after destroying sled with the hole cutter
* (UI) Revamped armor display in hud, each nub now shows an armor slot free or not and has a specific color for each armor type
* Fixed fish continuing to flop forever after being killed
* Added a fail safe when loading a save saying player is in caves to ensure he is actually above terrain, this should work around rare/edge cases or bugs that could lead to save with the wrong in-cave data and wrongly drop player below terrain upon loading the save
* (Multiplayer) Fixed an issue crane data initialization when loading a save causing crane to be wrong size for clients and the bottom trigger grab icon to not be visible
* Fixed player getting stuck in fall animation if getting hit while picking up megan
* When discovering passengers it now displays their seat number instead of the underlying ID
* Armor value displayed in stats page is now the total armor HP value instead of the legacy irrelevant percentage
* Fixed player sometimes getting stuck if jumping and activating a bench
* (Multiplayer) In the event of the Steam lobby getting destroyed for any reason during a P2P game, it will no longer error out in the saving process leaving the game in a broken state and instead try to fallback and finish the operation as well as technically possible
* Armor displayed in stats page now match worn armor types
* Health no longer shows a % sign after its value, showing this is the actual HP value
* While suffering from blood infection, the strength stats & its trend indicator (if any) are tinted in red to showcase it is being affected
* Fixed Megan sometimes duplicating while being picked up in end game

## V0.68b (released October 6, 2017)

* Fixed chainsaw not working after loading a save if it was equipped while saving
* Fixed dig ground for coins no longer working
* Fixed killing held live rabbit not working correctly
* Fixed passenger task not crossed off upon finding the 43rd passenger
* Fixed repair tool continuously playing the repair complete sfx when hitting a perfectly sane foundation based structure
* Fixed reset trap missing filling icon fail safe not working until player gets close to the trigger

## V0.68c (released on October 9, 2017)

* Fixed weapon drifting away over time as it gets stashed and equipped back multiple times
* Fixed reset trap filling icon still not showing up sometimes

## V0.68d (released October 10, 2017)

* Fixed issues with dropping items when maximum were already held
* Fixed some issues with items not appearing correctly on weapon racks or holders or in the catapult
* Fixed hotkeyed items not appearing in player shadow

# V0.67 (released September 21st, 2017)

* Fixed back index button on fire page not working
* Fixed bug where controls for client could break after some animations towards end game were triggered.
* (optimization)Animals in the overworld are now properly despawned when entering caves
* It is now possible to add logs to damaged ziplines
* Fixed some cases of the show hud option ticked off not behaving as expected
* (DS) Fixed tree regrowth
* Fixed enemies opening suitcases by running into them
* (Multiplayer) Sharks are now working in multiplayer games
* Explosive traps can now be triggered by projectile weapons
* Fixed current feeling calculation in book stats page
* Up and down weight trend arrows are now back in the stats page
* Fixed player getting cold and wet from rain while in caves
* (multiplayer) fixed some player clothing variations blurring incorrectly
* Added new book tabs to match new look of book
* Fixed enemy position when dropped on fire
* Fixed log on zipline offsetting from the zipline rope if placed while standing too close from the zipline and within collision range of player
* (Multiplayer) Improved log on zipline movement smoothing
* Fixed survival book not opening properly sometimes when closing inventory and immediately opening book
* Fixed camera snap when opening book with very low mouse smoothing setting
* Logs traveling on zipline are now visible from further away
* Fixed lizard ragdolls causing low framerate in multiplayer games when lizards are killed
* Improved enemy spec textures
* Turtle shell model and texture re-work
* Plant 18 and 15 rework
* Correction for previous page button on Crafting tab saying Bestiary 5 instead of 4
* Fixed player able to get stuck in corner of one of the huts in the large cannibal village
* Fixed player arms clipping with body when looking down
* Tennis racquet now uses single arm block animation
* Flare gun now displays amount of ammo in the inventory tooltip
* Fixed head on drying rack not pickupable for a long time before turning into skull
* Fixed missing amount display on mushrooms inventory tooltip
* Fixed an error when zipline is destroyed while riding it leaving player in a broken and infinite zipline riding state
* New held pot model and textures
* Fixed some wrong icons in inventory
* Fixed some overly glowy icons in world
* Fixed game crashing while in caves sometimes if progressing through and not killing enemies
* (multiplayer) Player can no longer be revived after being killed by a shark or drowning
* Optimized animator cpu usage in multiplayer
* Optimized physics cpu usage
* UI – Fixed ‘Mouse X Sensitivity’ saying ‘Mouse sensitivity’
* Fixed UI widget staying visible if grabbing log quickly from log holder after it gets destroyed
* UI – Bottom left messages are now hidden while in inventory to avoid overlapping with item tooltips
* Added hole cutter removal to ceiling skull light
* Fixed hole cutter removal for rabbit skin decoration
* Water detection of basic, rock pit and bon fires is now significantly more forgiving so that fires must be clearly underwater to be prevented from lighting up
* New building: Ground/log weapon holder ! Wall weapon holder now swaps to an on-ground log version that can be placed anywhere by not targeting a wall. Costs 1 log. Relevant items have a specific positioning on that structure
* Fixed hole cutter targeting lit fires from far away
* Caves – Fixed water zones not lining up in Cave 9
* Fixed raft making water splash sounds when on land
* (Multiplayer) Fixed issue with syncing skin variations, including red paint
* (Multiplayer) Fixed missing craft sfx when combining items with the metal tray
* Fixed inside of yacht being climbable with the climbing axe
* Fixed bone arrow feathers missing alpha channel and some birds missing alpha channels
* (multiplayer)Fixed loose bag floating visible in coop player seat at start of game
* All 4 fire types can now be destroyed without lighting it first
* Survival Book – new tutorial page design
* Caves- fixed some buggy swim areas
* Fixed mushrooms always having sheen in inventory
* (Multiplayer) Hole cutter can no longer target boat or the sled while it is currently being driven by someone
* (DS) Fixed water collector not working
* (Multiplayer) Fixed foundation based structures with only foundations damaged not offering repair prompt to clients until host first inspected it with the repair tool
* Fixed happy birthday traps sometimes not killing enemies after being reset once by player
* Added new audio to turtle shell sled, and new airborne sound effects
* Destroy supporting structure under either side of a zipline now destroys the zipline (not retroactive)
* Setup stats page to display Fullness & Hydration (thus matching hud display) instead of ‘Stomach’ and ‘Thirst’
* Happy birthday and dead fall traps can now damage players
* Happy Birthday and dead fall traps have been tweaked to increase chance of enemies dying reliably when trap is triggered
* Fixed a case of enemies sometimes not receiving damage when Happy birthday trap was sprung
* Improved log mesh/textures in HB and deadfall traps
* Improved look of stats page materials
* Fixed an issue with some tutorials possibly remaining visible if active while dying
* Fixed creepy mutant ragdolls able to trigger traps, causing them to trigger indefinitely
* Creepy mutants will now stagger backwards when hit by traps
* Creepy mutants can now damage traps with their attacks
* (Multiplayer) Speared fishes are now visible on remote players !
* Fixed bone arrows blurring wrongly when equipped on bow
* It is now possible to take items off weapon racks while not having room for it in the inventory in which case a pickup version of the items is dropped
* (Multiplayer) Player interaction system is now reset after player gets respawned, so that dying may clear out interaction bugs
* Fixed issues with disconnecting from sled by other means than the regular, intended let go like taking damage
* Fixed regression from last patch causing the repair prompt to not show up with repair tool equipped if logs are needed to repair a structure
* Soda cans should no longer fly out as high when boxes of them are opened
* Fixed getting knocked down from explosions while in inventory breaking all interaction and movement
* (Performance) Optimized boat foam system, games with many boats will benefit from this most
* (DS) Fixed Kick and Ban features, admin commands now also supports kicking, banning and unbanning by name
* Caves- replaced old bloody tables with new models
* Fixed regression with redman on yacht animation breaking
* (Multiplayer) Fixed banned players list not working
* (Multiplayer) Possibly fixed remote player heads missing sometimes

## v0.67b (released September 21st, 2017)

* Fixed issue with players being unable to let go of log sled unless hit or taking damage.

## V0.67c (released September 25th, 2017)

* Fixed strength always displayed as 1 in the stats page (underlying value was not affected)
* Fixed camera position sometimes becoming offset if skinning an animal on an angle
* Fixed an issue with cold armor having the possible side effect of leaving the frost effect active fullscreen
* Fixed a specific case of toggling quickly between book and inventory that could leave the hud invisible

# V0.66 (released September 8th, 2017)

* Fixed Sea Turtles sometimes being blocked by walls
* Sea turtles will now be set alight if passing through a fire
* Higher resolution textures on turtle shell
* Hitting enemies with repair tool should no longer make them bloodied
* Fixed very large save games sometimes crashing on load on 64 bit systems
* Optimized cpu usage of all enemy ai routines
* Better collision on some cannibal village props
* Added new large bloody tables and broken bloody table variations
* Deer now run away from player more after being attacked
* Player will now spin to face direction of attack after being killed by a shark or crocodile
* Improved cave wall collision accuracy
* Improved look of cannibal village hut thatched grass textures
* Fixed bodies ragdolling weirdly if dropped on bonfire
* It's No longer possible to attach bombs to enemy gibs
* Held small rocks and tennis balls are now dropped when sitting on a bench
* Fixed player arm clipping through camera sometimes during axe attacks
* Fixed slightly laggy movement on player camera during plane crash
* Fixed animals sometimes not pathing correctly around structures and other obstacles
* Lowered overall movement speed while attacking with chainsaw
* Reduced chainsaw damage against creepy mutants and end game boss
* (Multiplayer) Fixed small meat not visible in remote player hands when held
* It is now possible to bind mouse buttons to axis actions such as movement
* Looking at a damaged structure (not needing logs for repair) while holding a log no longer shows the repair widget and instead shows the missing repair tool icon
* Fixed loading saves with toy not initializing properly all renderers
* Fixed flashlight not properly set as the current light item after selecting it in inventory
* Fixed prev page button in Boats page of book pointing to Traps 2 instead of Traps 3 (defensive structures)
* New HUD elements added. Replaced stomach drawing, and cleaned up and created new HUD backing, and added new gradients for bars
* (multiplayer)Fixed player standing up after being killed while in injured state
* (multiplayer) Enemies and animals will now collide with rocks for client players when the host is very far away
* (UI) Revamped build mission UI items are now striked off and animated when completed
* It is now possible to add logs to ziplines to let it transport them across to the other end!
* When the Drop button is pressed and an actual item is dropped (rather than stashed) the previously equipped item is now equipped automatically
* (Performance) Simplified physics setup of defensive wall reinforcements
* (UI) New design for collected item messages and tutorials
* Mushrooms may now be collected using the pouch ! It is now possible to carry up to 10 mushrooms
* Gardens created in caves now have the option to plant mushrooms instead of seeds.
* Survival book pages re-worked for majority of pages. Some pages are still wip such as bestiary, and older crafting pages
* Fixed player camera breaking if taking damage during hanging in cave cutscene
* You can now use equipped shell as a sled by jumping and doing a downward attack
* Arrows, spears and flintlock pistol can now deal increased headshot damage to enemies
* Hole cutter can now also remove rock path, deer skin, rabbit skin and skull decorations
* Added mouse smoothing setting with option to set this to zero
* Fixed player sometimes able to jump while crouched in vents and other tight areas
* Improved held pot pose and added gather water animation when using pot at lakes and ponds
* You can now make poison arrows using poisoned mushrooms
* Fixed a case of prefab bundle loader going on and off quickly when placed as greeble creating several routines for a single object and causing the bundle to end up unloaded automatically after finishing loader as if unused (would result in some items not appearing when they should such as types of corpses in caves)
* Added cpu ocean optimization when far away

# V0.65 (released August 9th, 2017)

* (Multiplayer)Fixed camcorder strap clipping into player's hand
* Fixed flintlock not properly returning to aim mode if aim button was held down after firing
* Fixed player visibility not being affected by held flaming arrow light
* Improved skinned textures on rabbit, lizard, deer and crocodile
* Flare gun now has aim down sights mode and a reload animation
* Fixed standing fire doubling up after burning out/getting destroyed
* Further memory optimization of some end game animations and assets
* Fixed dead rabbit dropped from hand using wrong texture
* (Translations) Fixed case of “added to backpack” dynamic text not translating
* (Multiplayer) Fixed sleep on yacht achievement for clients
* (Multiplayer) Fixed building related tasks and achievements for clients
* Improved snap to items in inventory with a gamepad feature, it now targets groups of objects with same properties (so that it goes through the pile of sticks in 1 click but allows to target fire arrows amongst normal ones, decayed meats etc.)
* Ghosts and building requirements updated for raft and houseboat
* Ghosts updated for small and large holders to match finished log visuals
* (Audio) Fixed missing SFX when killing a held live rabbit
* (Audio) Tuned volume levels of chainsaw
* (Audio) Added gore footsteps to some gore assets in endgame areas
* (Audio) Added reload sound to flare gun
* (Audio) Added sound to new held flare ignite animation
* Held flares now have a ‘light flare’ animation as they are equipped
* Overhead smash attacks now produce blood sprays correctly when hitting an animal or enemy
* Dead flight attendant can now be hit with weapons and with get bloody
* (Translations) Updated Finnish translation
* Player will now drop from a climbing wall if climbing axe is unequipped
* Fixed some parts of the building system still using legacy “Take” action instead of the “Build” action
* Fixed regression in previous patch caused by an optimization of ocean system leading to ocean looking laggy while swimming, optimization is now only effective while not \* \* swimming in ocean
* Fixed enemy textures sometimes turning black when killed in traps
* Caves- fixed player head intersecting with Climb walls
* Fixed asset bundles system unloading dependencies before a bundle is completely out of use
* Caves – fixed holes in cave 9
* (Performance) Fixed one of the LOD scripts so that it doesn't go on and off constantly when standing at visibility threshold range
* Added slight battery charge upsurge when equipping plastic torch, it now equips and flashes for a split second before getting stashed to showcase battery is out of charge
* Fixed walky talky not equipping when out of plastic torch battery charge
* (Multiplayer) Now syncing Zipline and Crane sfx
* (Multiplayer) Sped up scrolling in game browser x7
* Animals now appear bloody when struck!
* Added new bucket, bench, wicker sleeping mat and plats/bowl models to cannibal villages
* Endgame scene will now attempt to load again if the initial loading fails, which may occur if harddrive is under heavy load.
* Fixed held plane axe clipping through player hands
* Fixed bird landing on hand misaligned while holding the flintlock or flaregun
* Larger animal heads (shark, crocodile and deer) have collision so the player cannot stand inside them.
* Fixed block animation getting stuck while interacting with crane and other triggers
* Boss enemy in the end game section has been made overall more aggressive and difficult to kill
* Previously, stairs built in a circle could not be completed if you were standing in the circle, even if you did not intersect with the stairs. They should now be buildable so long as you are not intersecting with the stairs
* Fixed offset plant pickup and sheen icons on some plants
* Replaced fxaa with a working version
* Fixed ghost leaf shelter rendering over book
* After dying in endgame while fighting boss enemy player now respawns next to a bed and has a wake up animation
* (UI) Fixed issues with using a gamepad in the options menu, it can now be fully navigated and used, including sliders (use the right stick) and remapping screen (use triggers instead of right/left click to edit & delete mappings)
* (UI) Fixed DS browser scrollbar mess + improved perfs
* Changed gamepad snap in inventory feature to free by default
* Decorated the beach houses with new props and pickups
* End boss health now scales with the amount of players currently in the game
* Added herb health pickups to some cannibal village locations
* Increased health on deer
* Fixed issue with accuracy of the map revealing system
* Revamped cave exploration tasks, instead of being based on invisible triggers it is now based on revealed map areas, which should make cave exploration tasks clearer and the spelunker achievement possible without cheats
* Fixed player not taking armour damage from enemy stomp attacks
* Fixed blood screen effect missing when hit with stomp attacks
* Fixed stashing map leaving it active in hand
* Fixed arrows not sticking into rabbits correctly
* It is no longer possible to take damage before finishing loading & plane sequence (if playing) at start of game
* (DS) Fixed animal pool not getting cleaned up properly when leaving the game to title screen, leaving further runs with no visible animals when playing as client
* Explore Hanging cave task is now made available when going through the main entrance instead of after the hanging cutscene

## V0.65b (released August 10th, 2017)

* Fixed defensive wall gate not buildable
* Fixed end boss enemy spin attack not damaging clients

# V0.64 (released July ?, 2017)

* Fixed some issues with logsled being harder to push
* Fixed save game timestamps not showing correct save time or correct amount of days survived
* Fixed equipping armor whilst holding flashlight causing player to revert to a 2 handed pose and when opening door animation plays
* Fixed tree stumps from old saves not being cuttable in newer builds
* Added in a hover effect for the main index tab in the survival book
* Added lobby is full message when the lobby is full for multiplayer
* Fixed crane sometimes trying to cut the floor right below when placed
* Crane properly ignores collision in view after locking first point (could turn red/unplaceable if looking at a tree for example)
* Fixed thrown spears losing ground collision after hitting an enemy or animal.
* Fixed attack input sometimes locked after firing flintlock and then switching to another weapon
* DS – Fixed tree regrow, allow building destruction, allow enemies in creative settings getting overridden on game start
* Fixed zip line structure not updating nav mesh correctly
* Walls, fences and affiliated can no longer be placed through trees
* Audio – Updated machete weapon sfx to be consistent with other weapons of similar type.
* Audio – Flintlock bullets now have impact sfx for plants, mutants, animals and other world objects.
* Audio – Added gore impact sfx for when exploding Armsy enemy type.
* Audio – Added sound event for applying mud
* Audio: Fix for the dynamic life buoy, now plays correct events when pushed on terrain and no longer triggers log hits when colliding with rocks.
* Audio: Updated enemy death animation audio tags.
* Fixed zipline ghost rope not fully covering entire length of the structure
* Fixed crane icon job when it cannot be placed & improved invalid placement detection
* Fix dead fall trap visibility in some angles.
* Fixed small campsite with some purple pots
* Fixed Temporary shelter, Log Cabin, and Skull lamp ghosts appearing as white outlines regardless of color setting in options
* Fixed issue with drinking water from lakes at extreme edges of waterline
* Fixed thirst and hunger warning messages not leaving screen even after drinking or eating
* Fixed terrain quality not applied when starting game
* Fixed missing cassette tape 5 + walkman combine recipe
* Machete can now be upgraded with teeth, booze or feathers !
* Balanced Machete to be faster and more effective at cutting bushes and saplings and can now also be used to chop trees
* Fixed log sled freaking out when placing dead bodies into it
* Fixed some small holes in caves
* Fixed dropping the leftmost fish in inventory spawning wrong prefab
* Crane now has a control trigger at the bottom and thus can be pulled down without being on the moving platform
* Walked steps are now only accounted for when player owns the pedometer
* Fixed some wrongly scaled bodies at camp sites
* (Translations) Added Czech, Italian, Polish, Finnish, Swedish and Turkish
* (Translations) Updated German, Spanish, Portuguese, Russian, Korean, Chinese and Japanese
* (Translations) Improved error detection in languages, notably with popup texts which could retain the last selected language value if current one was wrong
* Fixed issues with settings of timmy's toy crafting recipe possibly causing an error that would leave it in an invalid state
* Fixed a race condition in inventory and crafting logic allowing to craft item past the max amount (but not take it in inventory) by adding the product on crafting mat and then back in inventory
* Killing a held live rabbit gives you now both skin and meat
* Fixed translations positioning in stats page of book
* Caves – polish pass to Cave 10
* Fixed flashlight causing endgame glass to flashbrightly
* Fixed issue with enemy motion blur sometimes not correctly enabling
* Fixed crossing passengers off the manifest
* Fixed sled add item sfx not playing after moving sled
* Now also checking for the finish game achievement to unlock creative mode (so that it remains available for an account even when changing computer)
* Prevented bone from getting equipped when gained from eating meat

# V0.63 (released July 6th, 2017)

* Fixed book opening on its own when plugging in a gamepad at runtime
* Fixed breath bar not decreasing when player first enters water
* Tweaked flag colors to better differentiate between green and blue
* Fixed hud not enabling if starting a game with it disabled
* Fixed baby enemies not appearing bloody when hit
* (multiplayer) Fixed blood not appearing to clean off for client characters weapons
* Fixed short procedural wall collision being slightly wrong
* Fixed issue where you could sprint infinitely by spamming the sprint key
* Fixed player blocks also blocking hits from behind
* (multiplayer) Improved performance issue when hitting animals with arrows
* (multiplayer) Fixed Arrows stuck in animals not being synced correctly between players
* (multiplayer) Fixed issue where fish trap could vanish if players went far away and then returned
* (multiplayer) Trapped Cave fish are now correctly synced between players
* Fixed issue with equip weapon animations interfering with open book animation
* Fixed some structures missing dust when broken apart
* (Performance)Optimized clothing and hair geometry on player
* Fixed certain endgame cutscenes breaking if player was attacking while activating the cutscene
* Fixed shooting arrows downward while standing on logsled causing player to fly up into the air
* Fixed picking up bodies in end game breaking player animation if spear was held in throw position
* (Audio) Added extra sounds for endgame boss
* (Audio) Made walking on glass a little louder
* (Audio) Tuned endgame boss audio events to fill the space better
* (Audio) Added blood drips to endgame
* (Audio) Added impact event for when arrow hits plane wreckage
* (Audio) Additional polish pass of ambient audio emitters in endgame area
* (Audio) Added new audio event for hitting dirt terrain with stick to keep consistent with other stick/spear weapons.
* (Audio) Added sound for pushing raft on ground and water.
* (Audio)Added body part impact sound events when male and female mutants are exploded.
* Fixed boats and rafts being able to be built on top of each other
* Fixed animation bug, if you attack while trying to drinking water
* Added collision to trapped enemies in saved games
* Fixed issue with enemy hit animations conflicting with being caught in noose trap
* (UI) Fixed XInput setting reset when opening the menu
* (Multiplayer) Prevent spamming take from food holders (and similar) as client from providing several of the item stored until host responds
* (Translation) Added missing translations keys in title scene, options menu, MP Screen, Hints, pause menu, items/meats inventory tooltips, todo list, tick off system, available recipes list
* (Translation) Fixed texts missing/capitalisation/formating in title scene, options menu, MP Screen, book for the French language
* (Translation) Added Spanish, Simplified Chinese an updated Portuguese
* (multiplayer) Fixed bug with generic meat on fire turning into small generic meat for client
* Added look down sights mode for flintlock!
* Hole cutter now properly clears out the yellow hammer on ghost structures
* Hole cutter no longer has issues when targeting ropes
* Added “Ghost building tint” option in gameplay/interface, allows picking one of white, blue, purple or green
* Added “Ghost building opacity” option in gameplay/interface
* New weapon added: Machete !
* Trapped enemies now load with correct props
* (Audio) Added placement sound when adding explosive to tree
* New building: Zipline ! Has 2 gates, place either one high up and the other below and at distance, it will procedurally create a rope in between.
* New building: Tree Zipline ! Both endpoints can be hooked to trees and optionally second end point can be hooked with terrain
* New building: Crane ! When placing it you have to first choose its bottom position then its height up to 4 stories high, it then cuts floors and removes structures in its way when placed. Takes small storage structures and can be used to transport logs and other items higher up.
* Fixed flare on crafting mat appearing lit when it wasn't
* (Audio) Added new sound fx when raft is pushed
* Fixed turtle shell not making a sound when swung
* (Multiplayer) Fixed issues between MP player list, pause menu, book, and inventory screens
* (Multiplayer) Fixed players being able to interact whilst player list was active
* New building: Bird house! Once built will attract birds, who will likely drop feathers
* (Multiplayer) Fixed motion blur missing on some enemy types
* (DS) Fixed issue where enemy weapons could cause error spam
* Fixed issues with male pale enemies in noose trap
* Fixed issue where trapped enemies props could vanish
* (Multiplayer) Mutant dropped teeth pickup are now synced on host and client.
* (DS)Teeth now appear in dedicated server games
* (DS) Fixed turtles behaviour on dedicated servers.
* Pressing E to lock the first point of procedural buildings is no longer possible
* (DS) Fixed invalid password message not showing in some sessions when attempting to join with the wrong password.
* (DS) Fixed issues with incorrect material count on custom structures
* Weather system now prevents rain from showing up during the plane sequence
* (Caves)Fixed water zone in stalactite room
* (Caves)Fixed a couple areas you could get stuck in in the stalactite room and cavern room
* (DS) Fixed some issues with attempting to load regular multiplayer games into dedicated server games
* Fixed tree sap collector cutting leaves when attached to a tree
* New item added: tactical flashlight! Replaced old flashlight. Is much brighter and has a better 3d model.
* (DS) Fixed issues where errors would spam after exiting boss fight and attempting to load into server
* (Survival book)Moved Defensive Structures to last page of Traps section of book
* (Survival book)Added side numbers to sections of book that have more than one page
* (DS) Fixed enemies sometimes getting stuck in burning animation on dedicated server games.
* (Performance) Massively reduced memory use taken up by defensive walls, and optimized a ton of other models to improve memory usage
* New building: Custom garden ! Replaces the legacy garden, amount of available grow spots based on its size. Ground with slope/holes will prevent from placing it really big
* New art added: crashed helicopter
* It is no longer possible to grow plants in garden while in caves
* (DS) Added network configuration diagnostic to help admins
* Fixed issue where stumps to trees would be instantly cut if using a chainsaw in single player games
* Fixed L to light prompt not always appearing on lightable items
* Fixed some small overlapping and intersecting items in plane
* Fixed some small gaps in world
* Herbal meds, and energy mixes now have fake drops, and will drop if you try and carry too many
* New buildings: Fireplace, Bone chair, Bone chandelier, Bone frame, Stick frame, Wood couch and Small table.
* It is now possible to have several structures on a single tree (for example, platform and zipline!)
* Fixed major issue with hud & pickups after completing last structure requiring bones
* Fixed building airborne structures in sinkhole locking to their max height
* Fixed grabbing rope in sinkhole sending player high up above terrain level

## V0.63b (released July 7th, 2017)

* Fixed issue with regrowing trees in MP games causes them in some saves to not be cuttable on load
* Fixed issue with foundation ghosts not working correctly for clients
* Fixed some issues with storage and water holders for clients in some saves
* Fixed a bunch of MP related issue due to a bug with itemID numbers that broke in the 0.61 patch release

# V0.62 Released June 8th, 2017)

* Fixed home icon not going away if trigger is active while it gets destroyed
* Fixed crouch mode inverted when opening options menu
* Fixed procedural bridges not registering damage when hit
* Fixed tree sap collector ghost construction hammer position
* Fixed error in multiplayer when hitting bushes or water zones with arrows
* It is now possible to jump when placing ghost buildings with a gamepad
* Switched stick marker and sled flag icons to new system (same has house icon on shelters). On the first time loading an old save it tries to match the former color to the closest available color
* Fixed UI switch widget sometimes wrongly bringing up the list when it should just update the currently shown icon
* Improved differentiation between green & blue overlay icons color in world
* Fixed birds not being set on fire when shot with flare gun
* Fixed enemies playing trapped animation when loading a game with enemies caught in a noose trap
* Fixed animals not reacting to being struck by thrown rocks or low damage weapons
* Fixed birds sometimes flying underneath the ground
* (UI) Grey panels in options now light up when hovered
* Fixed missing combine prompt for some items when backpack is on the crafting mat to assign items to quick select
* Fixed spears and arrows not sticking into fig trees
* Fixed repair hammer sometimes not responding properly if used while equip animation is still playing
* Improved collision mesh on logs
* Improved selection mesh of bone armour pieces in inventory
* Caves – Pass on Cave 1 holes and items placement.
* (Multiplayer) Fixed dirt piles remaining in world if owning garden gets destroyed
* Fixed item inventory tooltip issues with broken toy, feathers, flintlock, Gun parts, blueberry and coneflower seeds, deer skin and leaves
* Crocodiles can now attack players standing directly behind them, and will generally attack more often
* (Multiplayer) Fixed repairing structures on Large Raft launching player into air
* Fixed pressing R on fires with nothing but cash in inventory causing the widget to rotate continuously
* Fixed right hand equipped item reverting to default weapon when passing through non rope caves entrances
* Fixed loading a save with chainsaw fuel fully depleted not updating the fuel UI properly
* (Multiplayer) Dead backpack now preserves item bonuses such as fire, poison or bone arrows
* Replaced old repair & log needed display with a new circular widget
* Fixed player stats being affected by armsy knocking down trees
* Fixed boars not moving at all after being hit
* Caves – Pass on Cave 4 holes and item placement
* (UI) Updated look of MP screen to match the new UI design
* Fixed boar attacks sometimes not connecting properly with player
* Fixed some cases of sfx not playing when using repair tool at distance from structures
* Hybrid buildings (using a preplaced structure combined with procedural foundations, i.e. the gazebo) now properly account for both the structure and the foundation repair hit & log requirement before allowing the repair to complete
* Fixed excessive snapping distance when placing procedural walls & fences near other walls
* Fixed plane axe using wrong icon during hanging scene
* Custom rope now validate anchor height before enabling the icon so that only working anchors are advertised
* All animals now explode into chunks when hit by explosives
* Reduced chance of player doing unintentional ground attacks when attacking enemies standing downhill of player
* Fixed proximity check for several structures ghosts (so it cannot be placed within trees)
* (Multiplayer) Fixed gun ammo respawning on client cache when loading.
* (Multiplayer) Fixed clients not seeing trapped fish in caves.
* Effigies now properly use the new light fire icon
* Included missing dust effects in most structures
* Effigies can now be repaired (preserving the on fire state)
* Arrow and bone baskets can now be placed on tables!
* Bottom collision of procedural wall windows is no longer thicker than the model, fixing nested structure like wall planter placing visibly away from the wall
* (Multiplayer) Trapped fishes are now synced correctly between players
* (Audio) Updated physics sfx on items in endgame area.
* (Audio) Added new rock debris audio emitter in collapsed walkway leading to endgame office areas
* Contents of catapult's basket is now saved
* Repairing catapult no longer clears out the content of its item holder
* (Translation) Improved support for missing keys in translations files, labels now retain previous value for missing keys, if a font for a language isn't installed (or the game cannot reach it) the language won't be listed in options
* (Translation) Added Chinese, German and Russian (all keys)
* (Translation) Added Japanese, Korean, Portuguese (WIP, only 284 first keys)
* After destroying a weapon rack, stored items are spawned and can be picked up
* Suitcases no longer disappear when host is in cave and clients out
* Player is no longer launched into the air, when destroy a bridge
* Players next sleep time is now synced in multiplayer
* Fixed some incorrect USE/TAKE naming on various inventory items
* Fixed passenger manifest being invisible if players tried to take it for the first time from a saved game
* Fixed deer and rabbit skin ghosts becoming invisible if placed on ground
* Fixed some areas in world with incorrect collision allowing players to float/walk above terrain
* (Audio) Added new audio system for inside structures! Audio will now sound differently if you are inside a closed structure or not.
* Fixed some loose ropes in overworld being placed floating above items
* Fixed babies not getting bloody when struck
* Improved look of cannibal village huts and added variation in wood construction
* Fixed marigold, aloe, coneflower and chicory not dropping their world pickup if you have too many in inventory and try to collect them.
* Arrows stuck into fishes and are now retrievable.
* Removed old beach towels.
* Removed unbreakable boxes – now only breakable box will spawn
* Removed loose flares in the world, replaced with more openable flare boxes
* Fixed tree house branch clearing being undone when tree was cut
* New small decorative prop added: captains hat
* Fixed Large raft repair and destroy issues
* (Performance) New asset bundles for improved memory usage. Tennis players, first class passengers, dead frozen bodies, cannibal village tree, Hanging woman Plane bathroom, pilots, cockpit, Anchor, Old boats and hanging bodies now add to memory only when in range
* Fixed issues with dock sometimes being hard or impossible to place even in a valid location
* Fixed destroying unlit effigy while targeting the light trigger leaving the icon active
* Fixed bonuses from upgrades on weapons not properly restored after loading a saved game (retroactive !)
* Added new backsplash texture to loading screen hint
* Fixed destroying animal trap leaving trapped animals inactive on spot
* Fixed hint text not specifying that ‘lit’ effigies will scare enemies away from camp
* (Multiplayer) Added new hair variations to multiplayer character type
* Added a 15% opacity dark backing behind options to improve readability when background is bright
* Fix weapon rack positions for Flare Guns, Flintlocks, Tennis Rackets, Katanas and Upgraded Spears.
* (DS) New command line options: -veganmode, -vegetarianmode, -resetholesmode, -treeregrowmode, -allowbuildingdestruction, -allowenemiescreative
* (DS) New config file options: veganMode <on|off>, vegetarianMode <on|off>, resetHolesMode <on|off>, treeRegrowMode <on|off>, allowBuildingDestruction <on|off>, allowEnemiesCreativeMode <on|off>
* (DS) New admin commands: /treeregrowmode <on|off>, /allowbuildingdestruction <on|off>, /allowenemiescreative <on|off>
* (DS) Added -configfilepath <filePath> command line option, if target file doesn't exists it tries to create it with the default values
* (Performance) Lowered CPU usage of building placer system
* Fixed blood not being cleaned off weapons if they got bloody during rain. Previously would only clean off if bloody when rain started
* Fixed lighter in inventory using old version of lighter art compared to held version
* (Audio) Fixed Swinging rabbits, fish,lizard, bones, tennis racket, turtle shell and lizard missing whoosh sound effect when swung
* (Multiplayer) Fixed some underwater particles being visible for players who died in water on respawn
* (Multiplayer) Fixed foundation built in caves not working properly for clients
* (UI) Updated control remapping screen to new design, also fixes some issues introduced last patch
* (UI) Increased size of the main UI font asset (improves crispness)
* Fixed chainsaw missing icon in the weapon rack UI widget
* Fixed cave ground not properly initializing down cave 1's sinkhole ledge
* (Optimization) Improved CPU performance of the on screen tutorial messages
* Fixed a water area in cave 1 that was missing it's trigger making it not swimmable
* (Multiplayer) Arrows in birds and animals should now be visible and retrievable by both players
* Grabbing items from food holders and skin rack type of storage while full will now attempt to drop the item on ground if a pickup exists for that item
* It is now possible to add items to the catapult by choosing which item through the UI like other holders
* (DS) Fixed catapult not working at all in dedicated servers
* Catapult now filters out all weapons (flintlock, stick upgraded etc. cannot be added to catapult holder but simple sticks & rocks can for example)
* Repair log requirements must now be fulfilled before performing the repairs with the repair tool
* (Multiplayer) Fixed foundation with collapsed chunks not properly initialized for late joining clients causing collapsed chunks to be there for the client and leaving client unable to repair it

# V0.61 (released May 19th, 2017)

* (DS) Dedicated Steam server authentication added, allows performing security checks
* (DS) Connected players in dedicated servers should now be correctly listed
* (DS) Fixed issues with repairing custom foundations
* (Multiplayer) Fixed chainsaw engine SFX playing on remote players when out of fuel
* Improved hair model/texture on female cannibal types
* Fixed enemies sometimes spawning in the sinkhole on peaceful mode
* Added the yellow hammer overlay icon to all building ghosts that didn't have it yet
* Fixed placing climbing rope sometimes not responding
* Fixed standing fires lacking collision
* Fixed bed, chair and table missing wood sfx when hit or walked on
* Ghost dock now performs an accurate presence check to prevent players from completing it while inside the model
* Improved construction icons positioning when inside larger structures
* Fixed wrong texture on cannibal leader skull lamps
* Fixed defensive wall placement missing the Fire1 action icon before locking the first point
* (DS) No longer attempting to hook with the Steam client, it is no longer needed to worry about launching the game first to have a server running on the same machine as the one running the game
* Fixed rotate icon missing during placement of nest-able structures (i.e.: wall planter) when not targeting a supporting structure
* Damaging foundations no longer distorts nested buildings (i.e.: a rope anchored to a gazebo)
* Fixed ghost Wall Planter, Wall Weapon Rack, Head Trophy, Ceiling Skull Lamp, Wood Bench and Sap Collector not turning red when not placeable
* Chainsaw fuel pickups no longer respawn (we actually missed one inside a tent that does respawn, the rest should not however)
* Increased chainsaw damage against enemies
* Fixed coop players sometimes sending wrong damage to certain structures
* Fixed some animation issues during end game cut scenes
* (Multiplayer) Reduced jitteriness of animal movement for client players
* (Translations) Fixed all HUD elements anchoring to allow proper positioning regardless of text size
* Fixed some end game assets being preloaded even if no players were in the end game section
* (Translations) Setup translation as overlay in most of the book
* Updated structure anchor icon, repair icons and re-arm trap icon to new design
* Custom foundations repair cost is now limited to 20 hammer hits regardless of damage sustained
* Updated Survival book texture in opening plane scene to display correct name
* Caves - Updated icons for cave entrances
* Optimized memory usage of various animation assets
* Fixed houseboat not saving HP
* Fixed drying rack leaving icons visible if destroyed while targeted
* Fixed dock walkway not receiving damage
* Stashing the current weapon no longer equips the previous (or default) weapon
* Device management screen no longer displays keyboard and mouse
* Input mapping system no longer separates settings between hardware types, all types are seen from the same screen and can be changed or set from there
* (Balance) Health regeneration after using meds or eating is now of 5 hp/s in normal difficulty and 0.5 hp/s in hard instead of instantaneous. A visual indicator displays the current target health value while health is regenerating
* Caves - Cleaned up cave 4 greebles and walls in main cavern
* Fixed players able to climb down very narrow gaps between structures while on rope
* Fixed player camera becoming offset if activating certain end game cut scenes while attacking with various weapons
* (Multiplayer) In-cave flag is now stored in player data, this will prevent the cave not loading properly issue for clients saving in caves around the sinkhole (not retroactive for saves already broken but compatible with working saves and prevents the issue from that point forward)
* (Multiplayer) Added several hair variations to the one of the multiplayer characters
* Fixed spec on red paint
* Lowered brightness of enemy drop down splash
* Fixed trapped enemies not dropping to ground if trap is destroyed
* (Multiplayer) Fixed player movement locked after being revived while sending a chat message
* Fixed issues with hint texts
* (Multiplayer) Fixed host camera shaking on plane when client first joins
* (UI) New title scene, options and pause menu designs

## V0.61b (released May 19th, 2017)

* Fixed issue with regrowing trees in MP games causes them in some saves to not be cuttable on load
* Fixed issue with foundation ghosts not working correctly for clients
* Fixed some issues with storage and water holders for clients in some saves
* Fixed a bunch of MP related issue due to a bug with itemID numbers that broke in the 0.61 patch release

## V0.61c (released May 19th, 2017)

* Fixed a host of issues in some MP games that had rope traps built in them, including some item holders not working and trees not being cuttable.

# V0.60 (released May 4th, 2017)

* (Audio) Fixed bug where mutant body drop audio event was being triggered when dynamic mutant gameobject was switched for dummy prefab.
* (Audio) Revision of bow draw sound event timing to improve sync with animation.
* Updated breath bar sprite with new design
* Replaced dust on buildings that break apart
* Fixed soda cans sometimes appearing in the sky around the world
* Player now drops any held logs when skinning dead animals
* Fixed arrows spawning a duplicate when shooting seagulls
* Made top edge of sinkhole less slippery so players do not unintentionally fall in as much
* Fixed enemies not turning bloody when hit with spears or arrows
* Fixed teeth pickups not spawning when hitting enemies
* (Optimization) Completely removed motion blur cpu cost when running a dedicated server
* (Optimization)Reduced cpu usage when motion blur is disabled in options
* (Optimization) Improved performance of heavy, mid and low snow
* (Optimization) Reduced overall cpu usage when enemies are enabled on a dedicated server
* (Dedicated server) Fixed some spamming enemy errors in dedicated servers
* (Dedicated Server) Autosave is now only active if there are players connected to the server
* (Dedicated Server) Autosave is now triggered instantly when the last player leaves the server
* (Dedicated Server) Limited autosave time to 15 minutes minimum, and set default time to 30 minutes.
* (Dedicated Server) Dedicated server can now be downloaded, installed and launched without the steam client (see -nosteamclient option in guide)
* (Dedicated Server) Clients now know the game was saved server side, and see a “Server is saving the game” message if saving takes too long
* New damage balance on all structures. Stick structures are now noticeably weaker than bone, which are much weaker than stone. Defensive walls are now much stronger than regular walls. Also fixed issues with some structures being stronger than others for no reason
* Added first pass of translation system. This currently includes French language only. It is possible to copy translation files and replace the text values to create new translations – however more official translations will be coming in upcoming patch releases.
* Fixed player hair not visible in player shadow!
* (Performance) Now unloading some objects from the world while saving to free some memory up to help with crashes when saving on huge games
* (Multiplayer) Added 3 toque clothing variations
* Caves – replaced broken rope with slope in cave 9
* Setup new loading progress design
* Fixed some cut stumps using wrong/old textures
* (Multiplayer) Added new jacket, hoodie up, open shirt, closed shirt clothing variations
* Improved look of underwater bubbles from rebreather
* Caves – Fixed some misaligned rocks
* Caves – removed duplicate modern axe from Cave 7
* (Multiplayer) Added “Experimental” text to dedicated server source buttons in game browser to clarify the current state of the feature
* It is no longer possible to use refilling item when already at max capacity

## V0.60b (released May 4th, 2017)

* Prevented repair system from wrongly prompting player for repair in the event of having deprecated HP data in old saves

# v0.59 (released on 18 April 2017)

* Added experimental support for players to host their own dedicated servers
* Added new dedicated server tool (downloadable via tools menu in steam)
* Fixed grabbing a sled partially in water sometimes resulting in all following interactions no longer working

# v0.59b (released on 19 April 2017)

* Fixed a bug where some structures would vanish on loading games
* DS - Added a version check to servers. This will inform players if the dedicated server they are attempting to join is from a different release than the current build they are using. Players who see this message should make sure their game is up to date, or alternatively try a different server as server may not be up to date
* DS - Connecting to a dedicated server now shows a client connecting message during the initial stages
* DS - When attempting to connect to a server that is not configured correctly, players will now receive an error message and be returned to title screen
* DS - Join server button on dedicated server has been renamed from ‘new’ to ‘join’
* DS - Fixed basic fires not lightable by clients after loading into games
* DS - Prevented dedicated server from saving quality presets
* DS - Player list in game now shows amount of players in game

# V0.58 (released April 12th, 2017)

* Added new home icon UI to tree houses
* Updated boar model + texture
* Players no longer intersect each other when sitting on a bench
* (Multiplayer) Only 2 players can sit on a bench at one time now
* Fixed enemies sometimes losing texture/material when killed
* Added look around animations when players are sitting on a bench or chair
* Weapons are now put away when sitting on a bench
* New stealth meter icon
* New unlock door icon (when door is locked)
* Reduced amount of hits needed to chop down maple trees
* Tweaked stealth values, player is now more visible when holding a light
* New construction UI
* Players can no longer spam jump to get up vertical cliff faces around the world
* Enemies will now react to seeing the players torch light at night and in caves
* Player now collects turtle meat when skinning a turtle, leaving the shell behind
* Fixed wrong attack animation sometimes playing when attacking with a bird on player hand
* Fixed some rocks around cave entrances being climbable with climbing axe
* New procedural buildings UI icons
* (Multiplayer) Fixed coop player sometimes falling through the floor when activating certain cutscenes in the end game
* (Multiplayer) Fixed clients sometimes not seeing many birds compared to host
* (Multiplayer) Fixed dropping logs as client sometimes shooting the player up into the air
* Fixed dynamic objects getting stuck underneath newly built gardens, causing player to be knocked into the air when walked over
* Roof ghost now turns red during the lock height phase while height isn't valid
* Fixed unlocking bridge anchors with right click
* Added new rain refractive particle, and new cave drips
* (Audio)Further tuned audio to work better in surround sound
* (Audio) Fixed modern axe playing incorrect impact sound when hitting plane wreckage.
* (Audio) Tuned existing arrow impact sounds and added new arrow impact sounds for animals and mutants.
* (Audio) Added new arrow impact sounds for when arrows hit bushes, small trees and water surfaces.
* (Audio) Fixed mutant corpses playing wood foots and impact sounds when walked over and hit with various weapons.
* (Audio) Tuned volume for paddling sound event when on rafts and house boats.
* Fixed cases of dropped logs flying off when dropped close to other physics objects
* Improved collision on log sled when full of logs
* Added new hair to player crawling forward during coop plane crash cutscene
* (Multiplayer) Fixed amount of chops need to fell trees being different in multiplayer compared to singleplayer
* Added foam and splash particles when moving through water on rafts
* Fixed rabbit cage icons remaining visible if it gets destroyed while looking at it
* Fixed interacting with bonfire with nothing in the right hand
* Added a failsafe in case inventory was saved with some missing/destroyed inventory views so that it keeps functioning regardless
* Players can no longer climb through each other when climbing ropes
* Improved lod on plane cockpit and fixed some placement/texture issues with cockpit/pilots
* Fixed player movement getting locked sometimes when grabbling log sled while eating meat
* (Multiplayer) Fixed other players flares visible over survival book
* Fixed caged rabbits having synchronized animation
* Fixed cases of tortoises spawning underwater in north area of map
* (Multiplayer) Fixed wall toggle addition icon out of sync with current wall addition
* Fixed holders possibly leaving icons active behind after being destroyed
* (Multiplayer) Added 3 hair style variations to the original character
* (Multiplayer) Fixed toy parts and toy full positioning in tray
* Fixed Sapling 5 vertex colours
* Added a failsafe to ensure missing repair tool icon goes off when looking away from the structure
* (Multiplayer) Fixed restarting an endgame co\*op session without restarting the game causing the endgame keypad door to not open for others
* (Multiplayer) Added clean up when finishing the game that should help with out of memory crashes that occurred when loading the epilogue

## v0.58b (released on 13 April 2017)

* Optimized rain collision settings
* Fixed issues where players could end up in sky when climbing ropes
* Fixed an issue with item duplication which would also cause issues with hud

# v0.57 (released on 23 March 2017)

* Fixed being unable to pick up fish killed with weapons other than spear
* (Multiplayer) Fixed animals not spawning snow particles
* Improved look of kicked up sand/dust particles
* Added snow burst particle when walking into and hitting snow bushes
* (Multiplayer) Smoothed movement on several dynamic projectiles, fixes stuttering look when viewing other players throw molotovs/bombs
* (Multiplayer)Fixed player net holding old flare particle
* Fixed player exiting chairs at wrong position during end game section
* Fixed survival book sometimes not opening properly while blocking and fixed book sometimes opening at wrong screen position when cold
* Blocked quick select usage during in game cut scenes
* Enemies no longer sometimes hit other enemies when targeting structures
* Fixed enemies not able to target player when attacking and caught in a noose trap
* Fixed player clipping through enemies that are caught in noose trap
* Fixed enemies hit by cowman turning burnt and exploding
* Audio - Opening Plane and other sequences now mixed in surround sound
* Audio - Cave Reverberation made less bass heavy
* Audio - Hitting rocks in caves now has reverberation
* Audio - rain sounds more varied and smoother and more surrounding
* Audio - Shipping container area given unique plastic audio event
* Audio - Animal skinning animation sequence now has unique sound event
* Audio - Added flapping wings sound for crows flying
* If enemies lose sight of a player going into a structure, they will now more often attempt to break down the walls blocking the way
* Particulate matter now appears when player is underwater
* Fixed enemies sometimes ragdolling incorrectly when burning to death
* Fixed enemies being unable to see player through built windows
* (Multiplayer) Fixed wood chop particles missing visually on other players chopping trees
* Improved look of sapling 5 and replaced with new billboard
* Fixed player sometimes unintentionally doing tree chop animation when swinging melee weapon near a tree
* Improved transition between tree cut sections and tree models
* Added cash as a fueling option for fires (Previously it would only fallback to cash when out of leaves)
* Fixed some more climb down areas in caves with wrong lod setting/popping off too soon
* Fixed issues with skinning animals and holding walkman causing walkman to be reset
* Fixed animals sometimes rolling away from player while being skinned
* Fixed held log hand animation sometimes being slow to respond after picking up a log
* (Multiplayer) Fixed clients able to cut down trees with the climbing axe
* Fires, Drying rack, Armor mannequin, Skin rack, food holders, weapon rack, explosive holder, stick, rock and log holders, arrow and bone baskets, and gardens all have a new UI
* Players and enemies can no longer run up the sides of cannibal huts
* Players can no longer carry or pick up dead bodies while swimming
* Fixed arrows sometimes going underneath terrain if shot directly downwards
* Fixed running while crouching speed being applied inconsistently
* Fixed player able to fast climb ropes with no stamina
* Wearing cold armor now also increases the delay in between frost damage hits up to 4 times at full armor
* New "home" icon UI on shelters, cabins and bed. Select a tinted icon to have the icon visible in world or the faded icon to hide the icon
* Fixed enemy bodies not falling down if floor was destroyed/removed
* Fixed player getting thrown up in air if standing over a rock supply cache when it explodes
* (multiplayer)New player hair/beard model and shader added
* Blood now accumulates on all player clothing variations
* Fixed dropped logs not colliding with log sleds
* It is no longer possible to duplicate items by spamming take/add weapon on rack
* Player can no longer take damage while at max cold armor and will even defrost if equipping full cold armor while already frozen
* Fixed enemies sometimes snapping to new position if falling down dead very close to a wall
* Fixed trees sometimes spinning around wildly when blown up with explosives
* Caves- fixed holes in Cave 2 and 10
* Caves - new waterfalls added
* Added new icons for pickups in world and for inventory
* (Multiplayer) Mixed some forced variation to the randomness of the player skin and clothing rolls
* Optimized animal and enemy traps to only spawn in nearby caught animals and enemies instead of loading in all of them to improve memory use in large saves
* (Multiplayer) Fixed picking up items in suitcase while full causing it to duplicate as host or remain floating in the air as client

## v0.57b (released on 23 March 2017)

* (multiplayer)Fixed skinny females appearing without color detail for clients in some cases
* Improved distance noose trap and fixed a bug with duplicating bodies on the noose trap
* Fixed metal door weight not considering the max amount bonus of craftable bags and thus preventing to gather back sticks and rocks past the base limit of each item

## v0.57c (released on 27 March 2017)

* Fixed crocodiles duplicating when killed
* Fixed first flight attendant spoken line missing
* Fixed garden not showing any UI when owning a single seed type
* Fixed distorted enemies continuously duplicating in traps
* Fixed rabbits not takable from traps
* Large traps now all damage creepies

# v0.56 (released March 8th, 2017)

* New bone pile art added
* (Multiplayer) Fixed stand up after being revived animation not playing for other players
* (Multiplayer) Fixed skinny cannibal swing stick animation not playing for clients
* New particles for: flare, dynamite and held fire stick
* Fixed enemies sometimes blocking player movement when killed
* Improved animations throughout end game cut scenes and enemies
* Increased chance of enemies investigating large player built bases
* Fixed enemies sometimes able to climb structures built over water
* Fixed enemies sometimes not drowning when underwater
* Fixed enemies able to see through player built walls
* Improved light dynamite animation
* Fixed being able to throw dynamite during light dynamite animation
* Fixed enemies sometimes launching player through the air during combat
* (Multiplayer)Fixed some issues with meat left on fires after saving and loading not syncing correctly
* Flare and dynamite textures improved
* Fixed player able to get tree sap by hitting tree with severed arm or leg
* Fixed player able to see down neck when sitting on a bench
* Fixed player moving at wrong speed when climbing walls at very low fps
* New abandoned small wood boat art (replaces placeholder art)
* New burnt creepy enemy textures, and new graded textures/better resolution and better balanced regular, blue and dead textures
* Improved particles when hitting trees and added fine particle dust effect
* It is no longer possible to use quick select while swimming/on rope/driving raft
* Flashlight will no longer be replaced with lighter when loading a save whilst holding flashlight
* Added fail safe in inventory when loading a save to prevent losing an item if an issue occurs while restoring an equipped item
* Fixed an issue of first time equipping through quick select stashing back the item and returning to previously held item
* (Multiplayer) Quick select items selection is now preserved after respawning
* Added a fail safe to prevent the lighter system to never reset if a race condition causes it to be in a wrong state
* (Multiplayer) Fixed dropping spoilt oysters
* Trapped enemies in happy birthday, Noose and Dead Fall traps, are saved and loaded. (loaded enemies in noose trap will always load in dead)
* It is no longer possible to build structures attached to traps
* Added new yacht sail art (replaces placeholder art)
* Snow blowing effects added to snowy area of map
* Added sound effect to flare lit held
* Added new incandescent texture to lit flare and new lit dynamite wick
* New cut trunk ends art!(replaced placeholder art)
* Fixed enemies sometimes triggering animal traps causing them to vanish or error
* (Performance) Added pooling system to quick item selection views to reduce memory usage
* Fixed items like herbs missing SFX when assigned to quick select
* Targeting quick select assignment cogs on backpack now works the same regardless of monitor resolution
* Assigning an item to a quick select slot, if it is already assigned to a different slot will change its assignment to the newly assigned slot
* Stick, rock, pouch and repair tool can now be assigned to quick select
* Fixed catapult not properly receiving damage hits
* Increased amount of pooled animals to fix issue where animals would vanish from traps if you had several traps (may still occur with very high number of traps)
* (Multiplayer) Fixed fire not saving it's lit state on server when loading
* Fixed hole in title scene cave walls visible on ultra wide monitors
* It no longer rains inside the shipping containers
* Fixed timing of start/stop walkman sometimes not synced to animation of pressing button
* Fixed hoodie outfit popping off sometimes on player when looking up and down
* Fixed splash particles when hit with spear looking overly dark
* Caves- fixed some cave areas where players can fall through collision
* Assigning quick select is now done with the "AltFire" button (right click with K/M) when hovering the little cogs to make it consistent with pressing on the large cog
* (Multiplayer) Fixed game locking up if trying to add more than 6 different items to the metal tray
* (Multiplayer) Fixed trade system not always properly disabled after use making long range trades possible
* (Multiplayer) Fixed revive system not always properly disabled after use making long range revives possible
* (Multiplayer) Fixed metal door not properly initializing for clients when first joining a game preventing items already placed on the weight from showing up
* Pedometer now saves the steps walked when you save the game
* Removed visibility of non-equipment items on backpack quick select.
* Flares now turn off when entering water and switch to dead flare material
* Fixed pedometer screen vanishing when partially underwater
* Fixed enemies not spawning in caves if client loaded into a cave with host being outside in the overworld
* Added new foot step particles to player on snow, sand and some leafy surfaces
* Fixed stashing lighter while holding a lightable item in right hand causing circle filling icon to remain visible
* Lowered place distance of the rock swing trap, fixed ghost being away from completed trap position
* When placing stairs while a new chunk can be locked, it automatically locks it before placing
* It is now possible to lock a 1 log wide stairs chunk
* Fixed platform part of stairs not registering hits
* Improved look of fire smoke particles
* Rock swing trap now properly saves the attached tree ID and also preserves it when rearmed (not retroactive)
* Arrows hitting a partially cut down tree now remain attached to the tree
* Right-click will now cancel the arrow draw and preserve the arrow
* Fixed missing splash particle when using upgraded spear in water
* Fixed getting hit while opening Survival book with ignitables equipped breaking camera
* Caves - Fixed broken swimzone in Cave 1 hallway
* (Multiplayer) Fixed rabbits not appearing white in snow area for clients
* (Multiplayer) Fixed positions of all items on metal tray!
* Changed order of offscreen particle rendering to account for image effects on main camera such as tone mapping and bloom
* Fixed bow looking distorted when placed on weapon rack
* Bon fire icons are now dynamically positioned to solve the visibility issue
* Fixed caught fish flickering in traps
* (multiplayer)Fixed some exploded cave in areas not syncing correctly between players
* Missing repair tool icon no longer shows up when building ingredient icons are visible
* Lit dynamite will be removed from hand now when placing it on a tree
* Unlit dynamite can be placed on trees
* Switched rendering BRDF to GGX

## v0.56b (released March 13th, 2017)

* Optimized building construction icons management to use less memory
* Removed some enemy script logging

## v0.56c (released March 13th, 2017)

* Fixed excessive memory when opening save menu which could often result in out of memory crashes when saving.

# v0.55 (released February 16th, 2017)

* Suitcases around the plane crash site no longer respawn
* Snow now lands on water in the north area instead of going through
* Frost damage will no longer occur while player is jumping or actively climbing a rope
* Fixed spoilt oysters not drop-able from the inventory
* Updated armor mannequin stealth armor model
* Fixed a couple rare errors that could prevent a few wall chunks from showing up in saves that suffered data loss after a patch
* Fixed painted cannibal leader switching to wrong texture on death
* Fixed animals moving at different speeds depending on current frame rate
* Fixed arrows sometimes floating when shot into terrain
* Fixed skin animal animation sometimes not playing if skinning is started immediately after picking up a spear
* Improved support for updating greeble zones data from old saves, should prevent cases of deprecated data causing error spam and causing severe lag
* (Multiplayer) Frost damage will no longer be applied to players who are in a downed state
* (Multiplayer) Moved chat to the left of the screen to avoid overlapping with building ingredients
* (Multiplayer) Added a dark backing to the chat to improve readability
* Traps will now correctly load to the correct state
* Traps will now restore to correct state after being repaired
* (Multiplayer) Fixed some issues with noose trap visuals for clients not syncing
* New gameplay option: Allow Enemies (Creative mode only)
* Fixed drop spoilt food option in inventory not available on food that was picked up already spoilt
* Fixed bed missing collision and bed not being repairable
* Caves - fixed some small holes/gaps
* Trapped animals remain in traps after save/load
* Fixed Squirrels and Lizards not always being inside trap when caught
* Added new late game mutant tribe wearing skinned face masks
* New arrow type: Bone arrows! Combine 1 stick + 5 Feathers + 5 bones to create 5 bone arrows
* New item quick select feature. Combine weapons on the crafting mat with the backpack to assign. Default keys are 1, 2, 3 and 4 on keyboard. Holding “AltFire” (block) while playing on a gamepad now switches the D-pad to quick select item slots
* Fixed enemies floating over spikes or moving when caught in the happy birthday trap
* (Multiplayer) Added new clothing: Vest with 3 texture variations
* Fixed upgrading weapons not cleaning up everything correctly causing other items around or on the crafting to be hard to target afterwards
* (Multiplayer) Improved walking and running animations on other players when holding all types of weapons
* Player no longer reaches for an arrow after firing the bow with no more arrows in backpack
* Fixed enemies using wrong burnt texture when dropped on a fire
* Fixed creepy enemies switching to burnt texture when hit with a flying axe attack
* Player dropped logs now spawn slightly away from player to prevent physics interaction issues
* Fixed poison arrow effects not being applied to enemies correctly
* Fixed sticky bombs not attaching to enemies or animals
* Fixed tortoises sometimes not going into their shell when hit
* (Multiplayer) Fixed birds sometimes not playing flying animation for clients
* Fixed player incorrectly blocking if block is pressed immediately after picking up a spear
* Fixed player able to continue repair hammer attacks even after switching to another weapon
* Fixed player not attaching to rope properly if rope trigger was underwater
* Cave9 - added more sound effects, and more stalactite models
* Added more cave fish to cave water zones
* Fixed clients not dealing correct damage from flying axe attack
* Fixed saving of items added to metal doors weights
* Fixed log sled glitching through terrain if grabbed and holding logs at the same time
* Fixed spears and arrows not sticking into some large tree stumps around the world
* (Multiplayer) Fixed arrows collected from bodies not being removed for other players
* Fixed animals sometimes not being caught in traps
* Fixed some stippling settings on some large logs/dead wood
* Replaced damaged buildings 3D icons by 2D versions
* Fixed jumping into water while lighting a cloth wrapped weapon causing lighter interactions to break
* (Multiplayer) Fixed a case of player variation not initializing at start of game
* Fixed player not disconnecting from treehouse rope if treehouse was destroyed
* Fixed player not disconnecting from raft oar properly if raft was destroyed
* (Multiplayer) Added new clothing: Hoodie with 3 texture variations
* Improved accuracy of hovering detection for some items in inventory
* First 4 weapons/projectiles equipped are automatically added to quick select free slots
* Fixed saving & loading exploded rocks walls in caves
* (Audio) Added break wood sfx when fires are destroyed
* Fixed plane recording wrong position sometimes in new games

## v0.55b (released February 16th, 2017)

* Fixed some usable items such as meds or armor being infinite if added to hot select slots
* Fixed issues with hot key items being visible whilst swimming or climbing ropes

# v0.54 (released February 1st, 2017)

* (Performance) Lowered engine CPU overhead cost from active sound emitters
* (Performance) Optimized cpu usage on some enemy ai scripts
* Fixed custom effigy costing 2 rocks instead of 3
* Updated stairs stilt model to use latest log art
* (Performance) Optimized clean up process of various systems to speed up time game takes to close
* Closing inventory with metal tray and decayed meat not combined on the crafting mat no longer loses the meat decay state when it returns to the inventory
* Fixed some issues with restoring meat decay state after loading a saved game
* Fixed some issues with restoring arrow bonus after loading a saved game
* (Multiplayer) Weapon paint now correctly syncs to other players
* Fixed weak spear sometimes disappearing when thrown directly downwards
* Caves – fixed hole in Cave 8
* Fixed gamepad navigation in the new game difficulty menu
* Rabbits in cages now have a 10% chance to breed each time player sleeps when there are 2 to 4 rabbits in the cage
* Fixed weapon rack sometimes not refreshing the current target item type
* Fixed painted inventory item material reverting when hovered
* (Multiplayer) Birds are now synced properly in multiplayer games
* (Multiplayer) Optimized total memory usage on clients
* Fixed enemy bodies ragdolling incorrectly when killed in a noose trap
* Fixed player able to get permanently stuck between gardens placed close together
* Fixed already cooked meat reverting to raw if the fire runs out
* Meat left on fire when saving the game now delay resuming the cooking until the black screen has gone away
* (Multiplayer) It is no longer possible to open the chat silently while having the survival book open
* (Balance) Opening inventory no longer pauses time in hard mode
* Blood effect that shows when getting hit now occurs while in inventory
* Lowered time inventory takes to pause the game in single player non hard mode games to 0.05s (from 1s)
* (Balance) Skinny cannibals now have a chance of carrying sticks as weapons
* Drying rack “rotate icon” now is properly positioned to avoid enter the meat placed on the rack
* Hole cutter can no longer be applied if is there is an enemy in range
* (Multiplayer) Fixed some cases of meat reverting to raw after using it on crafting mat with metal tray
* Fixed log cabin sleep and save icons remaining visible if active when a wall is destroyed
* Fixed spelling mistake in inventory arrows
* Fixed picking up small rock and spear at the same time breaking weapon usage
* Fixed loading a save outside of caves but in sinkhole not enabling cave grounds properly
* Added back in experimental support for 5:4 and 4:3 resolutions
* Revamped the frost survival feature. When the visual frost effect stops increasing, damage will occur if standing still for 8 consecutive seconds. Screen will visually frost entirely the time of a flash to indicate the source \* of the damage
* New high level painted tribe mutants added to world
* Regular mutants can now sometimes appear carrying crafted weapons
* Fixed weapons flying away from mutants sometimes when killed
* Added a slight blue tint to player skin when cold
* Player now does the check arms anim when getting cold if there are no enemies around
* Fixed adding and removing rabbits quickly from cages causing them to disappear
* Fixed scale of the static on ground snow particles
* (Balance) Added some skinny pale enemies to cave 1 armsy room
* (Balance) Cave 3 improved enemy layouts and added more enemies
* Caves: Removed old purse model
* Cave 3 added floating items and floating heads
* Cave 3 lighting pass, extra planks, extra floating items, old pot prefabs, air canisters to flooded room, fixed missing climbing wall, added swim out area to above ground
* Cave 1 More cave audio ambience between wood plank walls, Added broken wood plank details moved cross pick up to before first wall breakdown, Fixed unbreakable box on walkout side to sinkhole area
* Caves: Fixed spawn sticks often intersecting rocks and positioned incorrectly
* (Multiplayer) Extended player in ghost building check to prevent completion to other players in game
* Snow no longer washes off blood, mud and red paint like rain
* Current steam build ID is now displayed in bottom right of title screen
* Bow and arrow improvements. Bow will now be at maximum strength when animation shows arrow fully pulled back. Slightly increased reload speed.
* Fire arrows can now be lit by holding them close to a fire source while bow is drawn
* Birds can now land on the cannibal art scattered around the world
* Fixed gold keycard not getting picked up if picked quickly after the cutscene, while last weapon is equipping back
* Using booze now also resets all current frost effect/timer
* Player now shivers when cold
* (Audio) Tuned sinkhole ambience to increase volume on cave exits into sinkhole area
* (Audio) Tuned trigger threshold for player\_splash sfx
* (Audio) Added gore foot sfx for when stepping in gore piles.
* New stealth armour model and textures added to player
* Hole cutter no longer has any effect on ghost procedural buildings (which was making it non completable)
* (Multiplayer) Fixed nutrition/exercise/strength stat not restored properly for clients
* (Multiplayer) Fixed exploded cave rock walls respawned after leaving and returning to caves for host
* Fixed Cave 9 curled body in ground
* Fixed some cave shimmy areas set to wrong scale and not functioning correctly as a result
* Fixed some crates in caves not breakable or breaking at the wrong scale/wrong position when hit
* New temporary (leaf) shelter leaf texture/model
* (Multiplayer) Fixed players getting pushed around by enemies while injured and waiting for revive
* (Multiplayer) Fixed spawning in sinkhole as client preventing cave entrances to work properly

## v0.54b (released February 1st, 2017)

* Fixed bug with some caves not loading in saved games for clients

# v0.53 (released January 19, 2017)

* Creepy mutants can now travel in groups
* (Balance) Overall more creepy mutants will spawn in hard mode
* (Balance) Increased chance of seeing fire mutants in hard mode
* (Balance) Slightly reduced amount of skinny mutants overall in normal and hard mode
* (Balance) Thrown firebombs from fire mutants travel faster now in hard mode
* (Balance) Increased health of tribal leaders in both normal and hard modes
* New craftable item: Repair tool ! 2 Sticks + 1 Rock + 2 Clothes + 10 Tree Sap. Replaces adding tree sap to repair structures
* (Multiplayer) New jacket clothing variation added
* Fixed being unable to interact with triggers after equipping an item from inventory while pushing sled
* Fixed enemies sometimes not dying properly when killed from behind
* (Multiplayer) Improved idle, walk and run animations on other coop players
* (Multiplayer) Fixed large raft moving erratically sometimes when client player attempts to walk under stair geometry
* Fixed missing collision on step section on left side of large raft
* Fixed player not grabbing log sled correctly if a bird is landing on his finger at the same time
* (Multiplayer) Fixed clients not dealing correct damage to knocked down enemies
* Fixed some holes in terrain where former hidden caches were
* Removed old stalactite model from caves
* Fixed some rocks and objects inside sinkhole being climbable with climbing axe
* Fixed flintlock sometimes not registering hits on targets
* Improved aiming on flintlock so it's easier to hit targets above or below
* Fixed ball floating slightly near fingers when reloading flintlock
* Left hand items are now correctly hidden and restored when reloading flintlock
* Fixed flintlock ammo size on the crafting mat + added the multi view option
* Fixed incendiary upgrade of the upgraded spear not restored after loading a save
* (Multiplayer) All weapons can now be shared with the metal tray
* Fixed a case of upgrade not completing if there previously was a full recipe on the crafting mat without room for the product in inventory
* (Multiplayer) Fixed client not able to trigger trip wire traps with projectiles
* Added a fail safe to force player to let go of sled when swimming (it already happened when entering water while moving sled around but didn't work when sled was in water and player grabbed it)
* Tennis racket can now receive tooth, glass and feather upgrades !
* Fixed story items on yacht and cassette pickups respawning even after being collected by player
* Fixed light changing on cave ground after opening big door
* Fixed some items in inventory having wrong outline(herbs, medicine, berries)
* (Multiplayer) Fixed burning a shelter causing client to get kicked
* (Multiplayer) Fixed destroying garden blueberry bush not working after collecting all berries on host side
* Caves - Removed unusable climbing wall leading down to stash room
* Fixed camp cots sometimes flying up into the air when approached by player
* Fixed pickups dropped onto raft and large raft falling through
* (Audio) Fixed clients loading in caves sometimes not having any cave audio effects
* (Audio) Fixed boss music popping off abruptly for clients
* Fixed waterfall falling water appearing black from a distance
* Fixed pedometer screen in inventory changing when leaves are hovered over
* (Performance) Optimized physics CPU usage when there's a raft in game
* (Balance) Set rebreather max air to 300 seconds (from 600)
* Now showing current world coordinates in bottom right corner of the pause menu, can be used when reporting location specific issues on the hub
* Replaced drying rack with a "lite", single row version. Costs 5 sticks. This version should alleviate the targeting issues last version of the drying rack had. (not retroactive, previously made racks will still be the old version)
* Added support for multiple renderers to inventory item views, allowing items such as shoes etc. to be fully highlighted when hovered
* Fixed small cabin having the save icon always visible
* Replaced the Iron Forest cheat with gameplay option setting: Iron Forest (No building destruction)
* Ghost foundations now check more accurately if player is below/within to prevent completion
* Added a fail safe for plane hull position saving so that it can no longer get lost sometimes (not retroactive)
* Fixed gold keycard not appearing in inventory
* Fixed ghost rabbit cage sticks having sheen
* Improved blood seams on Cowman
* Fixed stretched texture in yacht salon
* Sled grab trigger no longer shows the action icon while sled is grabbed
* Fired Arrows now stick into all enemies and animals!
* Fixed arrows sometimes bouncing off target doing no damage
* (Multiplayer) Fixed female bodies sometimes disappearing when killed as host
* Skinning an animal now makes the plane axe bloody
* (Multiplayer) Metal tray held by another player no longer shows any icon if empty
* Fixed basic fire food placement collision being offset from renderers
* (Multiplayer) Fixed rock side platform not destructible
* Fixed "Sticky" upgrade recipe tooltip not showing up
* Added "Steam not initialized. Try launching the game from Steam" label in title screen when needed (happens when there is a privilege difference between the Windows user currently running Steam and the one running the game)
* Fixed some items not retaining their last active bonus & content amount after saving and loading (such as pot not saving current water)
* Fixed arrows not going through custom wall windows
* Fixed arrows not correctly registering hits on some structures such as storages
* Meat cooking on fire while the fire runs out of fuel is now returned as raw meat that can be picked up (instead of continuing to cook)
* Fixed flintlock gun smoke appearing overly bright in shadows or in caves
* Fixed lighting when sunset first turns to night time having overly bright ground lighting on some objects
* Fixed rock thrower having no collision when built on a raft
* Fixed rock thrower projectiles sometimes damaging player when released from thrower
* Fixed suit clipping through backpack model
* Fixed some missing collision in some caves
* Save slot selection screen in title screen now allows to switch to saves from another Steam account than the one currently logged in (if there are multiple on same pc)
* Fixed player sometimes falling through the floor during a cutscene in the end section of the game
* Fixed 2 players being able to both activate certain cutscenes at the same time
* Changed ‘iron forest’ option to ‘Allow building destruction’ for clarity

## v0.53b (released January 19, 2017)

* Fixed repair hammer remaining visible on crafting mat if you closed inventory without removing it first
* Fixed save game ui issue where single player games would say they were multiplayer saves (had no effect on saves themselves, only the ui text)
* Fixed crafting recipe list only showing closest 3 valid recipes. Will now list closest 7
* Fixed changing Steam user in the save slot window in game not properly refreshing in single player

## v0.53c (released January 19, 2017)

* Fixed some climbing walls not being climbable

# v0.52 (released December 20, 2016)

* A new game mode now gets unlocked at the end of the epilogue
* A new clothing option is available in mp for players who complete the game
* Lighter can no longer be equipped during a particular cutscene
* Ghost wall type switch is no longer concurrent with the regular ghost interaction trigger (both can be used at the same time, regardless of holding log or not)
* New gameplay option: Regrowing Trees On/Off (replaces the regrow mode cheat)
* Added latest story items to notes chapter of book
* Made boss creature more resistant to molotov attacks
* Some texture memory optimizations
* Optimized memory usage of some end game animations
* Fixed snow falling into some areas it shouldn't
* Fixed water source trigger appearing to not respond if trying to interact with it before the end of the re-use delay
* Fixed keycard doors not retaining unlocked state
* (Multiplayer) Fixed restarting a new game lobby not working after finishing the story as host
* (multiplayer) Fixed other player weapons sometimes being held in wrong pose when first joining a game
* (multiplayer) Fix for an enemy turning invisible during transformation
* (multiplayer) Fixed players overlapping each other in a cutscene
* (multiplayer) Fixed clients seeing additional dropped bodies
* (multiplayer) Fixed some dropped bodies not being visible for clients
* (Multiplayer) Fixed a case of story progression getting blocked if client left the game at the wrong time

## v0.52b (released December 20, 2016)

* Fixed end game characters using excessive motion blur memory

* (multiplayer) Fixed game seeming to crash/take a long time loading for clients during loading of particular scene

# v0.51 (released December 14, 2016)

* The door at the bottom of the sinkhole cave is now openable (if you have the keycard)
* New drawings and story items added near red paint locations in caves and overworld
* Changed delay in between appearance of light tutorial to 10 minutes (from 1)
* Fixed player camera sometimes facing seat during plane crash sequence
* Improved navigation mesh quality around geese lake and other lakes
* Molotov fires now get put out by water
* Fixed flintlock part 8 not showing inventory tooltip
* Fixed some tutorials possibly staying visible if dying while active
* Ghost tree structures no longer prevent completing it when standing below it
* Fixed thirst icon displaying full when starting new game then a second later when player looks at hand drops to correct amount
* (Multiplayer) Fixed a racing condition when taking item from food holder causing take icon to stay visible sometimes
* (Multiplayer) Fixed adding crafted meds & energy mix to food holders
* Fixed large stick holder turning into small stick holder when repaired
* (Multiplayer) Fixed possible item duplication when attempting to grab too quickly from food holders
* Fixed arrows and spears bouncing off animals and sometimes landing angled on trees etc.
* Flintlock shots now destroy breakable wood object (such as tables and crates) and stalagmites
* (Performance) Added a limit to the amount of collected item etc. entries HUD will show to avoid possible excessive amount of memory allocated
* (Performance) Now unloading asset memory when exiting caves to help on systems which are short on RAM
* It is no longer possible to place buildings only partially on dynamic support (i.e. the raft), it now has to be completely on the support. This is to prevent placing buildings crooked on the side which can cause physics issues (and in some cases make the raft sink or even fly)
* Fixed a case of player not properly climbing rope if there was something around the bottom trigger (like a cliff or bumpy terrain)
* Fixed grabbing a rope high up causing player to grab it at ground level instead of bottom of rope
* Lighter now stays equipped when entering and exiting caves
* (Balance) reduced katana damage and increased received block damage on katana
* Fixed entering caves through rope entrance sometimes bringing player back up in world
* Added fail safe to hopefully fix sled sometimes staying mounted to player doing something else
* Fixed a specific case of water triggers not processed in the right order causing player to visible warp out of water for a couple frames
* Changed default distance from player for ghost rabbit cage, water collector, weapon rack, stick marker, bench
* (Multiplayer) Fixed exploded rocks in caves not properly synced with late joining clients and being stuck not exploded
* Fixed molotov sometimes getting stuck non ignitable for a few seconds if trying to light it too fast after equipping it

# v0.50 (released November 14, 2016)

* Fixed climb rope action bugging out if grabbing a rope while in another rope's top trigger vicinity

* Fixed getting damage from small rock fake drop

* (Multiplayer) fixed small rock duplication

* (Multiplayer) Fixed not getting any prompt when trying to join a game from the Steam friend list when the game is already running (in title or MP scene)

* Fixed performance issue if players wore red paint around large distorted mutants

* Added inventory gamepad navigation to new find cache photos and flintlock parts

* (Building) Explosive holder now allows the new interaction scheme, switch with which item to add with the “Rotate” button

* Fixed whoosh sfx playing several times in a row repeatedly before even finishing when batching items to or from crafting mat by holding right click

* Fixed hold right click batching in inventory wrongly triggering in some cases, like after emptying waterskin

* Added a slight thirst threshold before it is possible to drink from waterskin or pot in inventory to prevent spamming the polluted water damage

* Fixed some structures not getting cut from nav mesh correctly on loading a saved game

* Batteries inventory tooltip now displays amount

* Cassette player fake drops no longer floats mid air

* It is no longer possible to use air canister while not carrying a rebreathing

* (Multiplayer) Fixed stone caches loaded exploded from a save not properly working for clients

* (Balance) Aloe, Chicory, Coneflower, Marigold are now limited to 10 each in inventory

* (Balance) Meds, crafted meds, energy mixes are now limited to 5 each in inventory

* (Balance) Hard AI setting: fire damage ratio 50% of normal

* (Balance) Hard AI setting: creepy fire damage 35% of normal

* (Building) Fixed grab chair icon turning on then off before being in range of use

* (Multiplayer) Fixed “cold & wet” tutorial not getting cleaned up after dying and respawning

* (Multiplayer) Fixed mutant babies not dealing damage correctly to clients

* Players now smoothly move into position when climbing onto a rope

* Fixed some bag inventory icons set to wrong icon

* Fixed player camera sometimes becoming offset after being knocked into water by an explosion

* Fixed axes sometimes appearing to hit enemies after weapon has already swung through screen

* Fixed texture stretching on top of shipping crates

* Fixed some incorrect survival book recipes

* Creepy mutants now try to avoid following players down narrow passages inside caves

* (Multiplayer) Fixed (again)other players being visible during red death screen

* (Multiplayer) Fixed host not revivable after opening the pause menu

* Tortoises now have same drop as turtles

* Fixed a couple icon not refreshing issues with racks

* Fixed eating spoilt oysters not having the spoilt meat poison effect

* (Multiplayer) Fetching items backpack now restores content of water holder and other item bonus such as the incendiary upgrade

* Fixed a case of “Fire1″ action icon not showing in inventory tooltip for hybrid equipment/edible items (like waterskin or meats)

* Shipping manifest can now be seen in survival book notes (page 3)

* (Multiplayer) Fixed boat loading unmoored from dock when launching game with a client in lobby

* (Multiplayer) Fixed client not getting fat man entry in bestiary when hit

* (Multiplayer) Improved emergency/last moment shutting down of server & client connection, should help with cases of player staying connected in game after application closed without going through the menu or not being able to restart server immediately

* Fixed story item pickups respawning when game was saved/loaded

* (Balance) Hard survival setting: player fire damage x2 from normal

* (Balance) Hard animal setting: land animal spawn amount 66% of normal

* (Balance) Hard animal setting: fish spawn amount 66% of normal

* Fixed bug with ocean sometimes rendering extra reflection layers on custom quality setting

* (Balance) Each killed fish now has a 2 in game days respawn delay

* (Balance) Hard animal setting: fish respawn delay is 5 in game days

* (Balance) Increased health of pale skinnies and cannibal leaders in hard mode

* (Balance) Reduced chance of enemies being knocked down from heavy attacks in hard mode

* Animals now run away from player more consistently

* Fixed game settings for difficulty no longer changing after going back to title screen once

## v0.50b (released November 17, 2016)

* (Multiplayer) Fixed bug when attempting to load and play an old saved game with more than 20 holes in a floor

* (Multiplayer) Fixed a specific race condition when launching game causing client to fail to joining saved games

## v0.50c (released November 18, 2016)

* Fixed old pot and water skins not being able to hold water

# v0.49 (released November 3, 2016)

* New cave paintings added to some cave story spots
* Red storage container company logo added
* Storage container manifest pickup added
* New photo pickups showing location to hidden caches added around world and especially in caves
* Red paint - added more buckets to world and in caves. These can now be worn by players to scare off enemies, or have enemies pray to you.
* (Building) Ghost structures now prevent adding the very last ingredient until the player exits the premises - fixes players getting stuck inside foundations or flying into air when completing raft
* (Performance) Fixed excessive overhead occurring when loading saves with huge amount of player made structures, possibly using 50% CPU for up to several minutes after black screen goes off
* Fixed dried meat added to fire before eating it not yielding anything
* (Multiplayer) Fixed houseboat oar not working
* (Building) Meds & Snack holders have been replaced by the Small and Large food holders which let you choose which item you wish to store in each slot with the “Rotate” button
* Improved animations for client during plane crash sequence and waking up on plane
* (Building) Skin rack has been revamped to use the new storage control scheme, each slot can now hold any type of skin, which can be selected with the “Rotate” button when prompted on empty slots
* (Building) Weapon rack & wall weapon rack have been revamped to use the new storage control scheme, equipment type to be stored can be selected with the “Rotate” button when prompted on empty slots, it will default to whatever is currently held when first interacting with the rack
* Exploded state of caches is now saved
* (Building) Drying rack has been revamped to use slots for each drying meat piece
* Increased speed of animals and increased the rate that lizards will run away from player
* Fixed placing bombs on explodable caches not working
* (Building) Floor & Roofs ghost triggers now better conform with the visible model (prevents the new system from not allowing to complete it when standing bellow)
* Slightly pull out inventory camera and tilted up to give a bit of space for upper items
* Fixed a case of thrown spear not being possible to pick up (i.e. after hitting a rock)
* (Building) Slightly re-positioned large food holder (former snack holder) triggers to prevent the 3rd one to be inaccessible when up close
* Difficulty mode is now saved in the upper node of the save file and visible in title screen save slot thumbnails
* Added Peaceful/normal/Hard mode selection with hover tooltip after clicking on new game
* Fixed large raft stick requirement icon
* Improved cut/not cut tree materials not matching
* Switched garden icon positions and replaced rotate icon with switch one
* Fixed eating burnt meat not playing eat sfx
* Added whoosh sfx when adding items to fire and drying rack
* Fixed arrow basket icons on wrong layer
* Switched all rotate icons to switch icon (except rotating buildings)
* Hard survival setting: polluted water damage x20 from normal (which is 1)
* Hard survival setting: polluted water thirst replenishment 50% of normal
* Hard survival setting: frost speed x3 from normal
* Hard survival setting: frost damage x3 from normal
* Hard survival setting: defrost speed 50% of normal
* Fixed north area slight constant snow not properly following player
* Weapon rack & wall weapon rack now only accept weapon items
* Ammo pickup added and added to cave spots
* New pickup icons added for katana, bow and spears
* Updated enemy layout and navmesh in cave 8
* Improved look of cloud/sky at night especially if overcast

## v0.49b (released November 4, 2016)

* Fixed skin rack not functioning in multiplayer games
* Fix drying rack items remaining selectable even when player moved away from rack
* Removed red crosses from overhead map (found photos should show location to explodable caches)
* Fixed bug with some enemy types hits not registering

# v0.48 (released October 21, 2016)

* (Building) Procedural stairs may now be built both up and down in a single unit instead of being one way only

* (Building) Fixed a bug with hole cutter causing some buildings to leave a broken ghost behind when targeted, increased amount of buildings it can remove, and fixed some errors/crashes with removing some structures

* (Multiplayer) Fixed edible items shared with tray not always usable

* (Multiplayer) Added support for syncing meat decay state when shared with tray

* (Building) Building repair trigger no longer shows the "Take" action icon when not owning any repair material

* (Building) Fixed dock not having a max point limit

* (Building) Lowered max angle between dock chunks

* (Building) Collapsed building parts now have an accurate collider so they don't go half way inside other objects or ground and no longer spin on themselves

* (Building) Fixed placing rock fence stub looking slightly different than placed version

* (Building) Improved system that prevents autofilled walls and fences from placing over existing ones

* (Multiplayer) Fixed coop players sometimes spawning on top of each other inside the plane

* (Multiplayer) Fixed players spawning in wrong pose when first joining a coop session

* (Multiplayer) Fixed other players and enemies visible during the player death sequence

* (Building) Rock fence now breaks into individual rocks when collapsed

* (Building) Added collision to defensive wall reinforcement spikes

* (Building) Added angle snap when placing foundation, walls, fences and stairs!

* (Building) Wall and fence chunks now attempt when placed to be nested with the support structure below if any. Fixes issue of destroying a single chunk possibly collapsing the entire upper row (not

retroactive)

* Fixed gamepad not automatically selecting the first UI element of opening panels (such as the received MP invite one or pause menu in game)

* (Building) Fixed aiming back and forth between fences and floors breaking wall & fences placement in autofill mode

* (Building) Switched walls and fences placement to a cast based system instead of trigger based, meaning that it will target whatever support is being looked at in autofill mode instead of having to bring the default log model (which isn't always visible) in direct vicinity of the support

* (Building) Revamped defensive wall reinforcement placement with the new cast based targeting system

* (Building) Added snapping with other walls when placing procedural walls in manual mode

* (Building) Each floor and roof now has a 20 holes limit, this works around an issue in multiplayer causing clients to no longer receive holes past a certain amount, also prevents escalating computation costs due to inappropriate use of the hole cutter

* (Building) Added new way to interact with fires: it is now possible to cook meat without holding it, when prompted press the "Rotate" button to select which meat you wish to cook, you may also choose to fuel the fire this way. Holding the meat item you wish to cook still works, it will lock the targeted meat type to whatever meat is currently held

* (Building) Added new way to interact with drying rack: it is now possible to store meat without holding it, when prompted press the "Rotate" button to select which meat you wish to add for drying. Holding the meat item you wish to add still works, and will lock the targeted meat type to whatever meat is currently held

* (Building) Not yet dried food on the drying rack can now be picked back up without waiting (it may be cooked on fire or relocated this way)

* (Building) Centered drying rack repair trigger

* (Building) New dynamic structure: Large Raft ! Features 2 oars that can be wielded by 2 players for greater speed and more accurate controlling

* (Building) Added large stick holder storage option, after placing stick holder press the "Rotate" button when prompted to toggle to large version, cost 24 stick and stores up to 40 sticks

* Fixed missing area not available message at end game door

* Fixed fire mutants not aiming projectiles at target correctly

* Improved far shadow and offscreen particles performance most animals now collide with walls and other objects in the world

* (Multiplayer) Improved accuracy of animation transitions for enemies and players as client

* Fixed thrown rocks not dealing damage to animals

* Fixed limbs not matching host body when chopped off.

* Fixed a bunch of text ‘can’t carry anymore’ items missing correct pluralization

* Fixed bunch of items having incorrect item name capitalization

* Fixed dropped climbing axe floating

* (Multiplayer) Fixed(again) snow trees turning into regular trees when cut

* Fixed missing Combine prompt in inventory item tooltips for a bunch of items

* Set bushes and small plants to no longer spawn under lakes/ponds

* Improved look of small tree and added touch bending

* New textures for bush08

* Fixed cave fires incorrectly rotated

* Fixed club selected material in inventory having wrong texture plugged in and a bunch of other selected materials looking wrong when hovered over

* Added collision to beach log, and hollow log and wood sound when hitting or walking over

* Plant 21 vertex colour fix

* Caves - removed old map pick up

* Fixed touch bending on Sapling 5

* Caves - fixed angled magazines on cave floors

* (Multiplayer) Fixed player switching to previous weapon after being revived

* Fixed player camera getting permanently offset sometimes when skinning an animal very close to a wall

* Fixed creepy mutants sometimes running away from player when in shallow water inside caves

* Caves - removed doubled up magazine in cave 5

* Fixed flares and tennis balls not having splash effect when hitting water

* Fixed berry pop in for blueberry and snowberry bushes

* Increased view distance on some cave climb down areas/surrounding rocks

* Fixed cowman blood seams

* Improved ai pathfinding around cliff edges and plane crash sites

* Fixed bombs/dynamite/talky place on wall system interacting with invisible triggers, thus allowing to sometimes place the item mid air

* Sheen billboards are now more consistent/brighter

* Improved resolution on plane seats/tray

* Increased meat on fire overcook duration to 90s (from 60s)

* Fixed thrown rocks not dealing damage to enemies

* (Multiplayer) Fixed weapon upgrades not showing on remote player if he hasn't opened inventory once since starting game

* (Multiplayer) Fixed defensive wall reinforcement possibly not loading for clients in bigger games or laggy conditions

* (Multiplayer) Fixed excessive distortion when building receive damage

* (Multiplayer) Fixed some issues with tree save states being different between host and client depending on where client was when trees were cut down or game was saved

* (Multiplayer) Fixed severe lag when client joins a game that has garden with planted seeds located far away from all current player locations

* (Multiplayer) Fixed and smoothed out world object sync sweep that occurs when a client joins a game

## v0.48b (released October 20, 2016)

* Fixed player bodies in multiplayer games sometimes being invisible
* Fixed small trees appearing red/without textures or invisible on some graphics cards

# v0.47 (released September 21, 2016)

* Enemies can now dodge away from player attacks immediately after being hit
* Improved parry hit detection, should be easier to consistently perform parries on enemies
* Fixed enemy attacks sometimes still registering after being parried
* Increased length of stagger animation on parried enemies
* (Multiplayer) Clients can now parry enemy attacks
* (Multiplayer) Fixed bug where clients could be kicked from game if attempting to chop shark head
* (Multiplayer) client player body and skin materials are now correct during opening plane crash
* Fixed incorrect stamina drain when doing heavy attacks
* Fixed camera rotating upwards slightly when exiting survival book
* Fixed some cases of buildings placing bellow terrain while player isn't in caves
* Fixed ghost procedural stairs trigger not matching shape and environment well enough to always be reachable.
* Improved ghost building placer staying above floors instead of constantly snapping to terrain
* Fixed floor hole cutter rendering on wrong layer
* Fixed floor hole cutter not properly showing wood particles at all rotations
* Procedural walls/foundations and fences can now be placed after the first locked point and reaching the minimum length requirement
* While placing a ghost wall or fence, parts that cannot be locked and wont be placed by pressing the place button now have a red tint to differentiate it from the rest of the structure
* Placing a procedural wall with a short chunk places logs vertically for that chunk, instead of not allowing placement. These vertical chunks cannot be made into window or doors
* Lowered min angle requirement for procedural walls and fences
* Removed all ghost procedural buildings placement legacy gizmos (round half circle, grid)
* Procedural foundations, floors and roofs now have a new dot and line gizmo when placing it in manual mode to fully visualize what is going on within
* Revamped procedural floors & roofs manual placement in a similar way to bridge anchor locking, except that instead of targeting a single point it is possible to slide along the supporting structure shape (i.e. edge of wall)
* It is now possible to place bridge directly when targeting it's second anchor instead of having to first lock the second anchor and then place the bridge
* Fixed ghost bridge being red after locking first anchor
* Fixed red ghost material visibility
* Added edge intersection check when placing floors and roofs
* Floor hole cutter now also removes (some) overlapped structures
* Optimized calls to nav mesh update when opening and closing defensive gate
* Improved large log holder repair trigger positioning
* Fixed attacking with held meat items not doing any damage
* Fixed cut snow tree trunks material
* Fixed stick & rock holder icons positions
* Fixed wrong material on ghost log holder sticks, ghost basket sticks, raft built sticks and wrong layer settings for ghost weapon rack and floor hole cutter
* Fixed player/player\_net held log still using old model and textures
* Fixed a bunch of material numbers for buildings being incorrect
* Fixed eat meat animation not playing while player was on fire
* Fixed eat meat animation not playing when eating burnt meat
* (Multiplayer) Fixed camera shake not working for client during fat creepy foot stomps
* Added a slight offset to fake gamepad cursor in menu so it doesn't overlap texts so much
* (Performance) Fixed unnecessary allocations in multiplayer games when in range of lakes or ponds
* The escape key (on keyboard) or back button (on gamepad, either B or Circle) can now be used to navigate back to previous menu location
* (Multiplayer) Added a “Profile” button in player list pointing to the Steam profile
* Fixed broken transparency on coral and part of arrow feathers
* Added heavy attack for large axe type weapons
* (Multiplayer) Setup steal item feature to transport extra data such as meat decay state
* Added new hit rock particle effect
* Improved look of wood chunk particle effect when hitting structures (now uses 3d geometry)
* (Multiplayer) Fixed case of dropped meat reverting to previous decay state
* Fixed medicine cabinet using old log model/texture
* Bone basket and arrow basket now have unique models and dedicated icons
* Fixed rock and stick holder book pictures looking different than built versions
* Fixed head cooking bug after using a decaying meat item
* Fixed cooking head floating high above fires
* Increased stipple range on some plants that were set wrong causing them to fade out too soon
* (Multiplayer) Fixed dropping bodies sometimes being unpredictable/difficult to judge drop distance
* Fixed cut fern texture not matching fern type
* Fixed garden rotate seed type icon remaining visible after planting max amount of seed
* New rain follow system that compensates player movement and time it takes particles to hit the ground
* Improved look of dead mossy log
* Fixed meat not set to back to the saved decay state after loading a saved game
* Fixed eating oysters not working
* (Multiplayer) Looting backpack now equips the plane axe if not already owned
* Fixed a.i issue with enemies in caves sometimes not attacking players

## v0.47b (released September 22, 2016)

* Fixed cases of camera locking vertically when attempting to eat meat whilst cold
* Fixed unlocking all ghost foundation points leaving a floating ghost behind
* Fixed issue preventing to use manual floor & roofs placement to function as expected in some cases
* Improved procedural wall terrain detection which was in some cases not switching to manual placement

## v0.47c (released September 22, 2016)

* Fixed bug with some save games not loading
* Fixed plant pot showing wrong icon

## v0.47d (released September 23, 2016

* Fixed newly placed autofill walls not always saving correctly
* Added fail safe to attempt recovering data loss in wrongly saved autofill wall chunks – Note: some walls will need to be rebuilt in game to function correctly

# v0.46 (released September 8, 2016)

* (Multiplayer) Fixed client dried meat not being dried when taken by host
* Fixed crouch toggle not working correctly on controllers
* (Performance) Replaced all pickups with deferred shader version
* (Audio) Added sound effect for running water on terrain when raining!
* Rabbits and lizards now have collision when moving around the world
* Improved ai navmesh around rocks and sinkhole area
* Optimized physics calls on animals
* Caves – Fixed some small holes and gaps in some caves
* Caves – Fixed cave6 cut female legs not being dynamic
* When using a gamepad, cursor now snaps to buttons instead of moving freely mouse style, thus making navigating book easier.
* (Multiplayer) Clients now start the plane crash in separate seats from host, and watch timmy taken away from different \* perspective
* Fixed logs flying up in the air when chopping down trees (hopefully)
* Updated ReWired (input plugin), should fix the issue with Xbox One gamepad drivers after the windows 10 update
* (Multiplayer) Cloth, tooth, feather and booze weapon upgrades are now visibly synced to other players !
* Fixed a bug when loading a save with ceiling skull lamps causing it to not be properly toggled on/off based on distance with player
* Fixed the default “Map” gamepad mapping when not using the Advanced Input (X-Input) option
* Added another way to batch items from inventory to the crafting mat, it is now possible to hold the “Combine” button to incrementally add more and more items
* Fixed logs floating in water that get reused by the pooling system not getting their buoyancy properly reset (past 100 spawned logs, oldest ones gets reused for new spawns)
* Optimized cpu/physics usage on enemies and animals
* Mutant babies will now drown if submerged in water for too long
* Fixed navmesh in cave 6 causing enemies to not find paths to player sometimes
* Added second skull to two headed effigy when broken apart
* Revamped crafting system to allow inputs when not hovering the cog
* Hitting the “Jump” button while having a valid crafting recipe on the crafting mat will now fulfill it
* Hitting the “Drop” button while having ingredients on the crafting mat will now return everything to the inventory
* Now clamping item info tooltip so that it is always entirely visible
* Fixed crafting guide page showing the “AltFire” action instead of the “Combine” action, causing it to show wrong buttons when using a gamepad
* Fixed some navmesh issues in Cave 1
* (Multiplayer) Reduced animation cpu usage as host
* Improved textures on some bushes/plants
* Improved/changed ugly plant like grass type with a more natural grass
* Fixed some cases of enemies still able to glitch through walls
* Fixed some item naming issues since the introduction of carryable dried meat
* Fixed page link button highlighting not working in book
* Caves – Fixed hole in Cave 4
* Added skin animal animation to player!
* Fixed some weird collision around islands where rocks were using a wrongly scaled collision mesh
* (Multiplayer) Fixed a bug causing built logs from a ghost procedural roof to not be visible until structure is completed
* Fixed next update part of title scene blurry at some resolutions
* Fixed missing mud pickup icon
* Fixed issues with survival book sometimes drifting away from players hands
* Fixed player movement slowing down when trying to open survival book while carrying a log
* Fixed enemies sometimes disappearing from noose trap when sleeping
* (Multiplayer) Fixed enemy movement appearing offset after being released from noose trap as client
* Fixed player sometimes not able to paddle raft or houseboat
* (Multiplayer) Fixed some logs flying for clients
* Dried meat can now be properly put back on drying rack and retain decay status
* Dried meat put down on a fire can now be eaten immediately
* Increased range of catapult
* Rotating ghosts buildings now speeds up after half a second
* Procedural Floor/Walkway swap system can no longer place walkway below terrain when not in caves
* Fixed eating dried meat from inventory not yielding fullness
* Moved bone & arrow baskets in book to the page 3 of storage
* New buildable furnitures: table and chair
* Floors & roofs no longer show the autofill/manual mode toggle action icon when not in direct vicinity of a supporting structure
* Physical exercise is now taken into account in the character weight formula so that exercising a lot slows down gaining weight when over fed and speeds up loosing weight if underfed
* Added home icon to bed structure
* Fixed player sometimes sliding forward after a hard fall
* Procedural floor no longer suggests and allow the autofill feature on a foundation (since it would just make a second floor matching the foundation embedded one)
* Improved nav mesh around big lakes area
* Tweaked inventory management to allow items that are both equipment and edible (such a pot filled with water) to be used with the combine button, thus leaving open the option to equip the item even when currently edible
* Fixed wall/fence attempting to go up the sky when placed on slopes with great height difference
* Floor now shows a preview starting after the first locked point instead of after the second locked point
* Fixed floor ghost color code not matching exactly rest of building system
* Fixed fire arrow not lighting up leaf traps
* (Multiplayer) Fixed arrow basket, bone basket, ceiling skull light, drying rack, rabbit skin, snack holder, meds cabinet, \* skull light, trophy, wall plant pot, explosive holder, catapult and water collector not following supporting dynamic \* structure for clients
* Fixed building repair trigger not following dynamic structures movement
* Slowed down enemy movement if underwater
* Enemies will now drown if submerged in water for too long
* (Multiplayer) Fixed placing a ceiling skull light as client leaving the place icon active

## v0.46b (released September 8, 2016)

* Added option to use legacy controller system to game options menu (free move cursor)
* Fixed some items being impossible to select in inventory with new snap controller system in old saves
* Fixed bone & arrow baskets inverted in book
* Player now returns to their original position when exiting chair/bench – should fix issue of players stuck in chairs built too close to tables
* Reduced trigger range on chair so players can't teleport across room to sitting position

## v0.46c (released September 9, 2016)

* Fixed skinning animal animation not resetting if player is on fire
* Fixed sitting on bench animation getting stuck if player sits whilst attacking
* Fixed stick + cloth upgrade recipe not working when not owning bow
* Fixed items hard to interact with in inventory at low FPS
* Fixed twinberries pink on the crafting mat

# v0.45 (released August 18, 2016)

* Fixed rock path keeping last autofill setting instead of disabling it, resulting in a state where rock path cannot be used after placing another wall or fence in autofill mode

* Fixed repaired anchor version of tree structures having a rope

* Fixed shutting down upgrading system before having applied all 5 views of a single glass shard upgrade leaving crafting system in a partially broken state

* Fixed disassembling upgrades not properly clearing up bonuses (100% retroactive)

* Fixed disassembling upgraded stick upgrades breaking it

* Fixed disassembling upgrades causing burning upgrade cloth to no longer show up in inventory

* Fixed material icons not visible when building a structure nested with a dynamic one (like houseboat) that has moved after ghost was placed

* Interacting with docking trigger is now exclusive so that it is no longer possible to interact with other nearby triggers at the same time

* Improved gamepad menu navigation, currently selected menu element highlighting should now be consistent when going back and forth in menus

* (Multiplayer) Fixed invite popup not usable with a gamepad

* Fixed some dynamic objects sometimes flying up into the air when approached

* Fixed missing collision from some cannibal art props around the world

* It is now possible to nest small buildings in both treehouses (considered dynamic, so it has same limitations as the houseboat)

* Several small buildings like rabbit skin decoration and snack holder can now properly be nested to dynamic structures (like houseboat or tree structures)

* (Multiplayer) It is no longer possible to equip items that are added to the metal tray directly from it, it needs to be moved back on crafting mat or inventory first (this is to prevent a duplication exploit)

* New building: Large Log Holder ! Once placed, the ghost regular log holder can be toggled into a large holder. Holds up to 12 logs

* New building: Large Rock Holder ! Once placed, the ghost regular rock holder can be toggled into a large holder. Holds up to 40 rocks

* (Multiplayer) Fixed issue with missing buildings for clients when loading a saved game with lots of structures (instead of attaching all buildings at once they will instead be attached to the networking system up to 100 at a time per frame, this delays just a little the time it takes for everything to show up on clients and should likely be unnoticed)

* (Multiplayer) Sped up time it takes to attach all trees at start of game

* (Audio) Added impact sound for when hitting tents with weapons.

* (Audio) Added impact sound for when hitting cannibal camp fires with weapons.

* (Audio) Added new sound event for spear throwing.

* (Audio) Added new sound for bone fence weapon impacts.

* Optimized cpu usage on enemy ai routines

* Fixed high cpu usage when survival book was open

* Improved collision on old white tents, lowered wind distortion and added stipple effect when they become visible

* New mud art

* New muddy arms textures

* New mud now stipples in instead of popping on

* New bloody gore cave models added

* Fixed nav mesh not updating correctly when some structures were destroyed

* Viewing passenger manifest can now be cancelled by pressing attack

* Fixed passenger manifest being activated at inconvenient moments such as when enemies are nearby

* Fixed player weapon sometimes becoming unresponsive for a moment when near trees

* Fixed shell attack not responding during jump

* Fixed shell attack clipping with player camera

* New building: Armor mannequin ! Stores a total of 10 Lizard Skin, Deer Skin, Stealth Armor or Bone Armor in a suited shape

* Fixed case of wrong weapon stats being used after upgrading a weapon and closing inventory with escape (without selecting a weapon)

* (Performance) Fixed unnecessary CPU usage from metal doors

* (Multiplayer) Adding more items to a holder than its maximum capacity now attempts to return it

* (Multiplayer) Now showing an icon next to other player name indicating they currently are inside a cave

* Added Storage page 3 tab in book

* New story item added to (spoiler, removed)

* New story pickup added to (spoiler, removed)

* New story pickup added to (spoiler, removed)

* New story item added to (spoiler, removed)

* (Multiplayer) Fixed tree structures vanishing instead of visibly collapsing for clients when supporting tree is cut down

* (Multiplayer) Fixed a case of fake drop causing duplication in MP, fixes duplicating animals meat when full

* (Multiplayer)Fixed cave fires doubling up visually when lit

* Improved popon of some rivers in parts of world

* Fixed player able to glitch through houseboat collision under some circumstances

* Hand icon will now point towards the selected menu item when navigating title scene and in-game menu with a gamepad

* Software cursor shown when using gamepad in book now has a more reasonable size

* Fixed some gamepad navigation issues in options

* Disabled prev/next action icons shown when using gamepad in book

* Grabbing sled is now hold “Take” action instead of simple press

* Increased max amount of rocks in sled to 26 (from 15)

* Fixed sled rocks using sheen material instead of regular one

* Arrow basket, bone basket, drying rack and skull light can now be nested with dynamic structures (i.e.: houseboat)

* (Performance) Turned off some additional cave floors that were on even when player was above ground

* Deer should no longer run straight through walls and structures

* Climbing axe can be used on above ground cliff faces again, (except for sinkhole)

* Fixed broken glitchy waterfall particles in sinkhole

* Fixed player sometimes surviving fall into sinkhole

* Fixed some cave entrances popping on too close

* Dried meat on rack can now be collected with a simple press of the “Take” action (instead of holding it for 0.5s which will still eat it)

* It is now possible to eat dried meat in inventory

* Player can now attack with held items such as fish, dead rabbits and generic meat

* Picking up small rocks/tennis balls when holding logs no longer drops the logs

* Fixed player animation breaking sometimes when picking up a spear while doing a downward axe chop

* Small rocks will now deal damage when thrown at player or enemies

* (Performance) Fixed star system having high CPU usage when in caves

* Fixed placing several buildings ghost with the Batch feature blocking opening inventory

* (Multiplayer) Fixed meat client gets on drying rack always fresh regardless of actual decay state meat had for host

* (Multiplayer) Fixed client adding edible/spoilt meat on rack turning to fresh meat

* Improved texture resolution on cave corpses in cave6

* Fixed incendiary upgrade on spear not saving

* (Multiplayer)Optimized mutant transform cpu usage for clients

## v0.45b (released August 18, 2016)

* Fixed navmesh generation which was missing trees and rocks, causing enemies and animals to run through these more often.

* Fixed bright purple stick visible in ghost rockpit

# v0.44 (released August 04, 2016)

* (Audio) Added new ambient emitters to more empty parts of world

* (Audio) Added sound effect when opening wooden doors on cabins and doorways

* (Audio) Added new sound for fish trap being triggered

* (Audio) Added new sound for air tank dropping when inventory is full

* (Audio) Fix for crafting sound sometime being inaudible in inventory!

* (Audio) Impact sound for bone, stick and rock fences when hit with weapon.

* It is now possible to rotate ceiling skull lamps and decorations in ghost mode

* There is now a 60s minimum duration to rain after it actually starts to rain

* (Multiplayer) Setup cloud forming for clients before rain starts

* Wall auto - fill mode is no longer available on terrain, it always uses manual placement

* Walls/Fences and Floors/Roofs each save and restore the latest autofill/manual mode

* Now enforcing a UI refresh after sleeping, should prevent tutorial that should be in bottom left corner to remain at top of screen occasionally

* Fixed repairing a damaged stick marker breaking its color toggling

* (Multiplayer) Fixed time of day looping really fast when host isn't responding

* Fixed regression with stick & rock bag changes causing poisoned arrows to not show up as such (but functional anyways) and incendiary upgraded spear to not work correctly

* It is now possible to remove fixed upgrades from weapons (tooth/feather/glass): Place an upgraded weapon alone on the crafting mat and press the "Craft" button. Upgrades will visibly fall off the weapon and about 40% of the tooth/feather/booze will be returned to the inventory if there is room for it

* Caves - better collision on curved rock wall

* Built rope now has a visible connection to structures

* Updated world nav mesh system, reduced memory cost and improves navigation inside and around player built structures

* New buildings: Skin rack ! Has slots for rabbit, deer, and lizard skin each with room for 15 items

* Fixed platform anchors icon being inside its foundation instead of outside

* Collision added to some tourist models you could walk through

* (Audio) Fixed one of the big rock types in world not sounding like rock when walked over or hit

* Fixed rope bottom trigger position not set correctly if ground is at the verge of its max distance

* Fixed rare type of dead tree that had cut point too hard making it hard/impossible to chop down

* (Multiplayer) Fixed decoration place icon staying up after placing one as client

* Fixed ceiling skull lamp not snapping to procedural ceilings

* Fixed toggling back and forth between book and inventory switching back to default weapon or no weapon

* (Multiplayer) Fixed meat decaying state resetting when dropped and grabbed by another player

* (Multiplayer) Fixed client toggling stick marker or sled flag color not properly syncing to other players

* Added a cap to damaged building distort ratio for building with lower max HP, fixes really high distortion on smaller buildings like skull lights

* Fixed ghost skull light placing floating above ground

* Tree house, Tree House Chalet and Tree Platform can now be toggled with the "Rotate" button after being placed on a tree (but still in ghost mode) to a version in which rope has been replaced by an anchor !

* Blocked small rocks and regular rock pickups from spawning in lakes and ponds to fix issue where drink trigger could be blocked by these

* (Multiplayer) Fixed error when picking up rabbits in traps as client causing it to be duplicated

* (Performance) Work around some engine physics allocations on player to reduce garbage memory generated each frame

* Enemies will now attempt to climb structures to get to the player and break down the ceiling if on the roof!

* Improved positioning of ropes on several buildings anchor (not retroactive, already placed ropes will likely be slightly off)

* (Multiplayer) Fixed player movement breaking if hit while waking up on plane

* Fixed held rock and other weapon speed not being affected by low stamina

* Fixed spear attacks not draining stamina at all

* Added stipple to plane food carts and blue/green tents

* Planting seeds in garden now uses the "Craft" button (use to be the "Take" button but was inconsistent with other feature that imply adding items in world, like food on fire)

* Fixed cooked rabbit (from rabbits burnt live) not edible

* Added hit proxy system to main stairs colliders (was only on stilts previously)

* New casting based anchoring for single anchor structures (currently climbing ropes only), grabs anchor in view near center of screen instead of within range of ghost, thus requiring less accuracy in aiming and being a lot easier to lock with anchors

* (Audio) Fixed cave footsteps playing on terrain footsteps instead of on rock footsteps

* Added splash particle when throwing small rocks into water

* Fixed ghost procedural stairs bug preventing from locking perfectly fine short stairs (within constraints)

* Removed delay on picking up rocks and other small items before equipping

* (Multiplayer) Now returning extra ingredients added to ghost building by going faster than syncing speed to complete the required amount

* (Multiplayer) Fixed input getting stuck and unusable if interacting with chat at wrong time when dying

* Massively lowered memory usage pathfinding takes and fixed a memory leak when going back to main scene multiple times

* Fixed loading game on a computer for the first time clearing cloud saves!

* Changed default "Build" action mapping for gamepads to the bottom row 1 button ("A" or "Cross") \* note that this change won't override custom settings if any

* (Performance) Reduced CPU usage when survival book is open

* Fixed some icon positioning issues in book

* Fixed some cases of weapon switching to default axe or none when toggling between book and inventory

* Fixed some issues with thrown upgraded/incendiary spear not acting as expected

* Fixed equipping items from crafting mat losing its active bonus

* Player death camera will no longer show extra in world enemies walking around

## v0.44b (released August 04, 2016)

* Fixed animals not spawning in vegan mode

* Fixed selecting ghost in book with a gamepad using “Build” or “Take” action instead of “Fire1” wrongly placing ghost even if not meeting requirements, allowing for example to place rope on ground

* Fixed bug preventing to change gamepad input mappings

* Fixed cave climbing axe not functioning

## v0.44c (released August 05, 2016)

* Fixed dropping meat leaving a broken unusable view in inventory

* (Multiplayer) Fixed swapping ghost tree structure as client causing it to be grabbed by host even if far away

# v0.43 (released July 21, 2016)

* Audio - added sounds to book opening on plane

* Audio - fixed timing of meat eating to fit new animation

* Fixed some structures not getting cut out of nav mesh correctly on loading save game

* Mutants will now attempt to eat food from drying racks, once there is no meat left they will destroy the rack

* Fixed some cases of enemies running somewhere when there was no path to the target

* Prevented animals from spawning inside player built structures

* Added new craftable item: Meds+. Craft with 1 marigold, 1 aloe and 1 coneflower, restores 100 health points

* Added new craftable item: EnergyMix+. Craft with 1 coneflower, 1 chicory and 1 aloe

* Fixed 2d filling cog not functioning properly in specific cases, i.e. upgrade recipe matching some ingredient with a recipe which currently has all its ingredient on the crafting mat but not valid amounts yet (like arrows & speed+ upgraded stick)

* Clamped garden plants scale to prevent it from ever going into negative

* Caves - Camping garbage added to cave 10 and 2

* It is no longer possible to be brought under terrain by the climbing down top of rope animation.

* It is no longer possible to use the top rope trigger to initiate rope climbing from below it, bottom trigger should be used instead. This prevents playing the climbing down rope animation when not effectively trying to climb down

* Fixed greebles switching from regular to snow when standing right on the edge in between

* New craftable item: Stick Bag. Combine 2 ropes, 3 cloth and 1 rabbit skin. Increases stick carry capacity by 10

* New craftable item: Rock Bag. Combine 3 ropes, 3 cloth and 3 rabbit skin. Increases rock carry capacity by 5

* Updated meds crafting page in survival book

* Fixed repair building trigger position not calculated properly, causing icon to possibly be inside the building depending on its orientation

* Moved shelter's icon a little bit more outside structure

* Eating marigold now gives 5% fullness (same as other plants) and plays eating sound when used

* Increased cooked meat trigger size, should make it easier to target meat over the fuel fire trigger

* Unlit molotov thrown at lit fires now fuel it (but still doesn't light unlit ones)

* Increased duration collapsed building pieces remain to 5s (from 2.5)

* Fixed collapsing foundation not releasing its logs individually and instead staying glued in oddly shaped chunks of several logs

* Improved look of Pine Tree Top Heavy - straighter trunk, removed lower branches.

* Fixed glowing mutant leader straps

* Fixed wrong uv's on back of some magazines and pickups

* Fixed missing backfaces on dropped lizard and rabbit skin prefabs

* Caves - better collision on rockground rock type

* Caves - fixed holes in cave 6

* Fixed repetition of female head on stick art placed around the world

* Improved responsiveness of weapon when attacking while recovering from a swing

* It is no longer possible to place a defensive wall reinforcement on gate chunks

* (Multiplayer) Fixed fish trap resetting when there's a fish trapped remotely

* (Multiplayer) Fish trap no longer syncs its sprung state, since fishes are local to each player it allows traps to catch fish on each player side independently. Resetting fish trap is still common to all players

* Fixed player collision getting stuck on enemies standing directly below player

* Life buoy now make sound when pushed and now float in water

* Player blood map seams fixed

* Fixed ghost roof default visual not centered and weirdly offset

* Fixed resetting fish trap not having a delay allowing currently caught fish to escape

* Fixed all types of maple trees not blowing up when within an explosion happening mid range from a player

* Fixed some tree/tent intersections

* Revamped procedural wall auto fill: in the same fashion as floors & roofs, walls now show a preview of the result of "auto fill" feature. By default it tries to guess what mode is desired and toggles between manual and auto fill depending on ghost touching terrain or a player made structure, holding the "Craft" button (C by default) allows to toggle between modes manually. After doing so it no longer switches mode automatically until a new wall is being made

* Placing a procedural wall on a foundation with floor will now cover the floor area instead of matching the foundation shape (so if foundations have an open side the ghost wall will cover that part as well instead of leaving it open, note that as all constructions it can be cancelled if not wanted)

* Now checking against existing wall chunks (or derivatives such as fences) when placing a ghost wall (or derivatives) and skip placing new chunks over existing chunks that share exact same position and size (for example, after autofilling a wall and cancelling a chunk, autofill can be used a second time to fill the gap without spawning doubled up wall chunks overlapping the existing ones)

* (Multiplayer) Fixed cave pre-placed fires not being lightable Better lod for sinkhole base lowest lod and matched to latest layout

* (Multiplayer) Fixed gamepad not having same restrictions as keyboard when using chat, causing issues such as allowing to double jump and possibly breaking all input

* Increased chance of enemies dodging thrown molotovs and other projectiles

* Enforcing trigger validation while paddling raft to ensure driver unlocking when landing

* Defensive wall gates are now considered dynamic buildings which doesn't allow nesting other structures to it (not retroactive)
* Vertically snapping structures (like decorative skulls) can no longer be parented to dynamic buildings which do not allow it

* Timmy drawings can no longer be attached to dynamic buildings which do not allow it

* Fixed excessive distortion when damaging gardens

* Fixed logs thrown into the sinkhole staying floating mid air, they now properly go all the way down !

* Fixed screen sometimes shaking randomly when walking around the world

* Fixed meat clipping into player body while eating

* Fixed player crouch getting stuck sometimes when moving through shallow water

* (Multiplayer) Reduced some jerkiness in squirrel animation as client

* (Multiplayer) Fixed player slowly rotating to the side and ending upside down when using chat box while swimming

* (Multiplayer) Fixed flickering on back of tabloid magazine when viewing another player holding it

* Fixed player getting thrown up in the air if standing on top of an explosive

* Added screen distortion effect to plane TV screens when plane begins to crash

* (Multiplayer) Fixed game freezing when closing inventory after adding more items than shown using metal tray on the crafting mat (i.e. add metal tray and 40 leaves to crafting mat then close inventory without combining)

* (Multiplayer) Fixed (again)backpack overlay icon not showing up in world after dying in a cave

* Fixed lizards and other animals not falling from trees that are cut down

* Lizards will no longer try to climb trees that the player is chopping

* (Multiplayer) Fixed interaction distance with item holder trigger of sled being really short

* (Multiplayer) Fixed cutting stumps away from host not not blowing up

* New memory and performance optimizations added to pathfinding

## v0.43b (released July 21, 2016)

* Fixed max amount bonus from having stick or rock bag in inventory stacking up each time a saved game is loaded

## v0.43c (released July 22, 2016)

* Toggling between autofill and manual placement for walls, floors and roofs is now done with a simple press of the "Craft" button (instead of hold), fixes issues with other trigger breaking the toggling such as drink trigger when building over a lake

# v0.42 (released July 8, 2016)

* Fixed limbs being difficult to chop from dead bodies

* Fixed birds sometimes flying in small circles

* Added additional particle effects to exploded enemies

* Enemies will now die when falling from a great height

* **(Multiplayer)** Floor/Roof hole cutter is now available! Clients cannot cut holes in ironforest mode to prevent griefing

* Caves – fixed 2 holes in cave 2

* Fixed player head clipping through objects when doing downward axe chop

* Added missing rabbit fur cost for bed in survival book

* Fixed excessive random jitter sometimes occurring on floors after cutting holes

* Fixed deer sometimes standing on edges of cliffs

* Fixed survival book not mentioning rabbit fur cost of bed

* **(Multiplayer)** Fixed random object spawned at the location of metal tin tray for clients

* **(Multiplayer)** Fixed distortion of damaged procedural buildings

* New poisoned effect: when shot with poisoned arrows enemy movement is slowed and damage output is reduced for a short time

* Bigger structures that can't be placed on houseboat floor can no longer be placed on its walls

* Fixed enemies sometimes able to kill players who are in downed state

* Killing enemies in trees should now cause them to fall to the ground

* Enemies should no longer get stuck running inside cannibal huts

* Log sled can now also be used for transportation of up to 58 sticks ! When sled is empty, hold a rock or stick to place the first and thus select the carried item type, after that the selected item can be added without needing to hold it first (like on regular holders)

* **(Multiplayer)** Fixed ghost tree structures loaded from a saved game not getting removed if tree is cut down

* **(Multiplayer)** Fixed remote player plastic torch flashing when they enter the game

* **(Performance)** Fake drop feature now re-uses existing instance whenever possible (only when used pickup is dynamic, otherwise we have to spawn a dynamic one), also fixes fake drop cleaning up decaying meat

* Fixed extremities of foundation's floor not perfectly overlapping the area, eventually causing foundation to be visible on the sides, also fixes some weirdness with holes on sides of floors and roofs not perfectly conforming with hole area. Might have an impact on look of previously made buildings/holes

* Added new cheat code: “woodpaste”. Can be used to reset floor & roof holes in a saved game. Cheat works once when game is started then gets reset when going back to title screen. Does nothing for MP clients

* Shortened minimum stairs locking length down to the minimum technically possible length with current formula

* Downwards stairs (place first point up then aim down) now skips the platform part on the first chunk if locked shorter than the regular minimum length

* Deadfall, HB, swinging rock, noose, rabbit and fish traps now cost one stick to reset

* Ghost foundations can now be snapped back at first locked point regardless of what height is currently aimed at

* Enemies will now attempt to jump up onto structures built low to the ground to get to the player

* **(Multiplayer)** Fixed client not seeing host climb rope animation, if loading a save game with no weapon equipped

* Added new cheat code: type: regrowmode in title scene to activate/deactivate. When enabled 10% of cut down trees will grow back each night the player sleeps, For multiplayer games this needs to be enabled by host to have an effect on game. Only stumps will regrow into trees, so if you want trees cleared in some areas, for example inside your base, be sure to remove the stumps!

* **(Multiplayer)** Fixed syncing of iron forest mode so clients no longer run distortion logic when it's enabled, which could cause clients to see highly distorted structures that will never be destroyed

* New art added: pamphlet

* When a bush is burning, its remaining berries are now removed

* **(Multiplayer)** Stalagmite destruction is now synced to nearby players

* Improved enemy pathfinding around villages and firepits

* Fixed jumping axe attacks sometimes not registering hits on enemies

* Regular enemies will interact more with dynamic objects in the environment

* It is no longer possible to place items such as bomb when in range of an interacting trigger (such as save trigger from shelters) to avoid blowing yourself up when trying to save with C whilst also holding a bomb.

* Fixed gap between roofs and walls

* Added ‘eat meat’ action to player when consuming cooked meat

* Fixed repaired fish trap turning into rabbit trap

* Fixed pause menu not visible on super wide monitors

* Now filtering out rocks from clearing system (used by ponds etc.), preventing to end up with invisible collision like at the pond near the cannibal village

* Fixed lizard, crocodile and rabbit skin vanishing if player tried to pick them up whilst already carrying max amount. Dynamic version will now drop in its place

* Fixed mud spawning underwater after rain

* Burnt headless bodies now stipple in

* Fixed cave waterfalls missing flowing water effect making them dark/hard to see

* Improved raft buoyancy settings, should prevent it from not properly unlocking driver when leaving water

* Fixed tortoises not dropping heads

* Fixed tortoises not dying when set on fire

* **(Multiplayer)** Fixed distant cut down trees not refreshed and showing billboard when late joining a game or joining a saved game

* Fixed a bug when loading a saved game without owning plane axe preventing inventory system from functioning, notably causing both inventory and book to be impossible to open

* Added generic protection against inventory initialization failure, game should keep working even if something goes wrong in there

* **(Audio)** Fixed some environment SFX (like waterfalls) not working after loading a saved game

* Added information about poison arrows to survival book

* **(Multiplayer)** Fixed survival book on other players not using correct texture for front of book

* Roof hole cutter now allows cutting several holes aligned with each other without completely cutting the roof in between holes

* Fixed elephant leaf plant billboard turning off too soon

* Fixed bird on hand not motion blurring correctly

* **(Multiplayer)** Fixed bird on hand not appearing on other players

* Light molotov tutorial now gets hidden when opening inventory or book

* **(Multiplayer)** Fixed bow not being drawn back on other players

* Upgrade recipes now show the 2d filling cog when there's at least 2 different ingredients on the mat

* Fixed small crafting ingredient (such as teeth) below crafting cog not reachable when crafting cog is hidden

* **(Multiplayer)** Fixed enemies tending to target host more than clients

* **(Multiplayer)** Fixed client unable to remove tree stumps when far away from host

* **(Multiplayer)** Fixed sky lightning getting stuck visible for clients when host is in snow biome and client isn't

* Fixed FPS lowering when survival book was opened

## v0.42b (released July 10, 2016)

* Fixed some bugs with regrow mode in multiplayer games that could cause regrown trees to vanish for client and be uncuttable for host in some cases

* Fixed a case of player weapon getting stuck unable to swing during combat

* Fixed player sometimes gliding when running up slopes and other objects

## v0.42c (released July 10, 2016)

* Fixed some incorrect quality presets causing lower than expected performance on quality levels lower than highest

# v0.41 (released June 22, 2016)

* (Performance) Reduced CPU overhead cost from animal spawning logic

* (Performance) Reduced allocations from tree wind sfx logic

* All mutants now have improved explosion gibs

* Physics objects will react more to nearby explosions

* Particles - replaced fire effect on lit arrows!

* Fixed arrow fire wrongly showing fire hit particles when shot

* New art added: Dead baby corpses combined

* Fixed issue with HBAO artifacts on ati cards

* Chopping dead sharks will now leave a headless ragdoll

* Fixed walls sometimes snapping below when placing on custom floor

* Hole cutter can now cut several buildings at once, whether side by side, at different heights and/or overlapping each other, making it a lot easier to edit complex/composed structures. Watch out for side effects of this change when trying to cut a single floor

* Ghost floor is now red when it cannot be placed

* Added rolloff to building distortion intensity, looks a lot more natural and avoids axe hits from distorting a whole house boat (for example ;)

* Fixed book tabs not having sheen effect when player is in cave

* Caves - Dead baby piles added to cave 4

* Fixed pine tree cut having shimmering cut section where model was overlapping

* Caves - ROV added to cave 9

* Ghost raft now stays above water

* Ghost house boat now stays above water and can only be placed above water

* Improved look of bestary drawing outlines

* Caves - thicker collision on cave entrances

* Option menu now updates its centering after resolution changed

* Limited framerate to 60 in title screen to fix overheating issue on some graphics cards

* Added low SSAO quality (effective with HBAO only)

* Setup buoyancy on logs !

* (Performance) Fixed extra physics cost for MP clients when there was a raft or houseboat in the game

* Push houseboat icon is now outside its walls

* Hybrid ragdoll system added - enemies will conform better to the floor when dead or dropped from carried.

* Fixed dropped bodies sometimes disappearing when dropped on a steep slope

* New building: Fish trap ! Bring the legacy rabbit trap to a water area and it'll turn into a net able to catch fish. Must be suitably placed in a fishing area to be efficient !

* Arrows are now limited to 5 on the crafting mat and adding/removing arrows from the crafting mat moves all 5 without requiring to hold the batch button

* Added cloth to burnable arrow upgrade recipe

* Setup burnable cloth model on arrows

* Fixed rock path rocks not getting a randomized rotation

* Increased view range for all ponds

* Pond spawned rocks now stipple on

* Caves - reachable skull lamps now all dynamic

* More health on elephant leaf plant

* Touchbending added to saplings!

* Fixed plane lod being drastically lower in save game versus new game for interior

* Dead bodies can no longer be dropped when standing very close to walls/rocks etc.

* New art added: Revised log model, spike log model, and 3x half log variations

* Ex Floors now accepts log model variations + setup 3 variations

* Ex Stairs now accepts log model variations + setup 3 variations

* Ex Dock now accepts log model variations + setup 3 variations

* Setup new log model on wall, foundations, log pickup

* Setup new defensive wall log model

* Setup burnable cloth model on crafted club ! (recipe was already in but not working because this wasn't setup)

* (Multiplayer) Fixed alt tabbing while chat input is open breaking all input

* (Multiplayer) Enabled physics on log pickups for clients so that they may push logs

* (Multiplayer) Improved granularity of dynamic pickups position syncing to reduce jitter

* (Multiplayer) Client adding 2 logs to a log holder/sled with only one free slot will get back the extra log instead of it being forever gone

* (multiplayer) Reduced pop when spawning creepy ragdoll bodies as client

* Added docking capability to house boat ! Approach houseboat close to dock stilts until the dock icon shows up and use the "Take" button to toggle the docking. While docked the boat cannot move or rotate

* Fixed being unable to block while jumping

* Fixed being able to pass through the edges of some cave entrances

* Replaced arrow type toggle icon with a suited one

* WaterSkin and pot inventory tooltip now shows current water fill percentage

* Fixed ghost tree structures not going down when tree is cut down

* Updated houseboat with new log model

* Fixed player still moving sometimes while inventory is open

* Fixed foundation's floor position locking possibly going out of sync with foundation's one

* Fixed aiming up or down from last locked foundation position allowing to go around the minimum chunk length limitation

* Fixed cowman not showing up in bestiary

* (multiplayer)Fixed bodies being dropped in wrong place for client when first dropped

* Slightly lowered randomisation of floor logs (was giving bad result sometimes and it's far less necessary now that we have variations)

* Fixed houseboat on land not automatically unlocking the driving player

* Setup new log model on procedural wall doors

* Rebalanced procedural wall door physics to ease entering structures in some cases

* Fixed dead bodies floating in air if dropped from a height

* Better scale/position of deadshark head when held by player

* (Performance) Revamped floor hole cutter preview, instead of cutting the actual floor or roof it shows a ghost overlaying it with no physics/navigation cost involved

* Fixed player being shot out of cave 2 exit if they had entered via rope entrance

* (Multiplayer) Fixed snow trees turning into regular trees when chopped in MP games

* Fixed explosion damage not always being properly accounted for on buildings

* (Multiplayer) Fixed damaged building distortion being so soft that it wasn't visible

## v0.41b (released June 24, 2016)

* Fixed completing ghost tree structure causing trees of this type to keep the cut leaves when pooled/reused across the world

* Calibrated floor & foundation floor log cost with new log size to match old cost for a given area coverage

* Fixed loading saves with buildings ghost past ingredient requirements, it now automatically completes it (to fix rare cases of this occurring)

* Fixed blocking while in hanging cut scene breaking animation

* Updated navmesh in cave 2 to improve enemy pathfinding

* Fixed boats not properly undocking when dock gets destroyed

* Floor hole cutter now only cuts structure within the visible white rectangle area and no longer those that have been targeted and are above or below

* Fixed roof hole breaking height calculation, causing roof shape to change when applying the cut

* Fixed roof not calculating height properly depending on alignment with world

* (Multiplayer) Further increased damage distortion of regular (not procedural) buildings for clients

* (Multiplayer) Fixed bombs exploding over a foundation floor not distorting for client

# v0.40 (released June 10th 2016)

* (Audio) Added hurt sounds to baby fire anim

* (Audio) Balanced tree wind in distance, tuned waterfall large, tuned snow footsteps and snow jump in wet

* (Multiplayer) Fixed book tabs flashing when second player held bomb

* Fixed rotation when flat items are placed on the crafting mat using multiview positioning (i.e.: ropes)

* (Performance) Heavily optimized cost of stippling system for objects that aren't in viewing range (when using high draw distance it can lead to up to 2\* 3% FPS increase)

* (audio) Added deafness when standing next to large explosions!

* (audio) Fixed missing creepy mutant burning sfx for clients

* (audio) Fixed missing animation sfx on cowman for clients

* (audio) added snapshot to duck ambient audio when inside house boat

* Fixed ocean floor ending too soon and allowing players to fall through or stop seeing sand

* New art added: bloody gibs (added to armsy blown apart model)

* Fixed tennis balls on dead tennis players being scaled too small

* Fixed rope trap view distance set wrong and popping off too close

* Fixed gap between emergency plane door exit and plane wall

* Fixed area under yacht you could swim through that would remove underwater effects temporarily

* Foam added around yacht in ocean

* Improved yacht lod distance that high details appear

* Revamped building explosion: buildings now suffer regular damage instead of having parts removed altogether and instead will collapse when their HP reaches 0

* (Balance) Lowered explosion range of crafted explosive to 12 (from 15), 500 point blank damage to buildings

* (Balance) Lowered explosion range of head bomb to 14 (from 15), 600 point blank damage to buildings

* (Balance) Increased explosion range of dynamite to 17 (from 15), 750 point blank damage to buildings

* Building explosion damage now has a rolloff applied based on the explosion radius

* (Multiplayer) Improved building distortion calculation to better reflect accounted damage

* Fixed ghost walkway not buildable

* Player can no longer die from staying too long in plane crash sequence

* Color highlighted items in the crafting section of survival book to make them clearer and stand out more

* New building: Procedural Dock ! Must be built near water, places like walls except it stays over water at a fixed height, can have several chunks like other procedural buildings

* (Performance) Fixed rocks never going to lowest lod level

* New difficulty changing cheat code: rawmeatmode ! Enables perma death mode, can be turned off by typing vegan, vegetarian or meatmode. In this mode the second death in single player deletes the save slot and after loading a saved game or having saved once in a new game, it is no longer possible to save in another slot.

* Reduced player melee damage to structures if hitting an enemy at the same time

* (Performance) Optimised enemy ai routines around lots of built structures

* Fixed misaligned water zone near upper part of map

* Added a full reset when entering a trigger using a delayed action (i.e.: saving at a shelter), should prevent it from ever getting stuck

* Fixed cooked rabbit meat looking like it is burnt

* (Performance) Cleared out a bunch of small runtime allocations, helps reducing stutter/freezes

* (Performance) Fixed/improved slowdown/stutter when approaching enemies or when enemies attack

* Revamped sun rotation delaying formula, it is now based off time of day rather than sun rotation which allows greater control such as making sure it never cumulates delay past a certain point. This should prevent the occasional weirdness with sun rotation

* Fixed dead sea weed not stippling in. Fixed small green rock not stippling in.

* (Performance) Lowered amount of starfish and now stippling them in only when closer to player

* Water collector's water visual now scales with amount of water and visibly fills when it rains

* Fixed water collector not working after being repaired and water collector giving infinite clean water if damaged whilst full

* Improved lod switch for cockpit

* Fixed cases of enemies glitching through walls

* Fixed camera clipping through plane floor sometimes during intro stand up sequence

* Fixed stairs ghost mode's built stilt having a collider before being finalized

* Fixed player getting dragged through a tree sometimes during drag away cutscene

* Fixed some cases of enemies following player into water while attacking

* New tick off system, can be found at end of book, currently wired with usable plants (either eaten or picked up with pouch) and animals (must grab cut off head)

* (Performance) Added pooling to hud's tutorial runtime generated entries and removed unnecessary anchors causing extra CPU cost

* Fixed player view sometimes becoming misaligned after entering cave doors

* Survival book - fixed wrongly linked pages

* (Performance) Switched 1000 cliff caps that used unity lod for much faster lod system and now lowest low level will stipple on

* Fixed slightly misaligned buttons for building tutorial fire and tutorial hunting shelter

* Fixed log sleds not colliding with other log sleds

* Fixed log sled getting stuck to player if hit while entering log sled

* Fixed jagged icons in Hud tutorials

* New bestiary chapter in book: fills with information regarding enemies as you encounter them !

* Added a rowing paddle to house boat !

* Fixed weapon block sometimes getting stuck when using a gamepad

* Fixed yacht life preserver sticking through ceiling

* Improved some plant billboard distances

* (Multiplayer) Unblocked house boat

* Fixed player body disappearing sometimes while driving raft/houseboat

* Increased delay before adding find timmy task at start of game to 10s (from 3)

* Fixed jitteriness sometimes when driving raft/houseboat

* Fixed player camera occasionally facing the wrong way during planecrash

* (Multiplayer) Fixed destroying custom effigies leaving parts flying behind

* Custom effigy parts now properly collapse along the effigy

* Fixed opening book immediately after entering place ghost mode causing player camera to lock up

* (Multiplayer) Fixed raft paddle getting stuck if player leaves the trigger right after engaging control of it

* (Multiplayer) Fixed issue of remote non driving player falling off raft while moving it (not very noticeable on raft but was mandatory with houseboat)

* (Multiplayer) Fixed red sphere showing under turtles for clients

# v0.39 (released May 24th, 2016)

* (Multiplayer) Fixed downed enemies blocking player movement

* (Multiplayer) Fixed lock on distant doors loaded from a save file unusable for host

* (Multiplayer) Client's in game day time is now local until end of plane crash sequence for both host & himself

* (Multiplayer) Fixed adding lizard on drying rack taking a long time to show up client side

* (Multiplayer) Fixed story clues not showing up after loading a saved game for client (retro active)

* (Multiplayer) Added motion blur to items on metal tray

* (Multiplayer) Fixed some item positioning issues in metal tray

* (Multiplayer) Cleared out metal tray black list ! Flare/Skull/Cloth/Bomb can now be shared with it

* (Multiplayer) Fixed rain stopping for clients when host enters caves

* (Multiplayer) Fixed client getting rain while in caves

* (Multiplayer) Now retrying up to 3 times to connect when failing to join a game (fixes at least the case of joining back a game that was improperly disconnected)

* (Multiplayer) Fixed picking up flares in crates not removing the correct object

* (Multiplayer) Fixed yellow crates not opening for host

* (Multiplayer) Fixed missing sound when reloading catapult as client

* (Multiplayer) Added held dynamite sparks syncing

* (Multiplayer) Fixed bug where enemies could exist in world but be invisible and unmoving for clients

* (Multiplayer) Fixed bug where enemy attacks could hit player even if they didn't complete the animation

* (Multiplayer) Fixed missing audio on cowman for clients

* (Multiplayer) Fixed cowman not showing burnt texture as client

* (Multiplayer) Fixed cowman blood not syncing on death as client

* (Multiplayer) Fixed creepy ragdolls sometimes spinning weirdly as client

* (Multiplayer) Fixed activating door locks as client when host is far away

* (Multiplayer) Improved time of day syncing when joining a game to account for possible delay before receiving all required data to perform accurate local calculations (should prevent clients from sometimes starting game starving/thirsty even though it wasn't saved like that)

* (Multiplayer) Fixed tree structures not properly synced so that cut leaves system and collapsing works properly for clients

* (Multiplayer) Fixed walky talky not working after loading a game that was saved in SP

* (Multiplayer) Fixed not able to reset noose traps after removing dead mutant

* (Multiplayer) Fixed players backpacks popping off early/having different visibility settings than body

* (Multiplayer) Fixed rabbits in traps not resetting properly for clients causing issues with active rabbits later on in game

* (Multiplayer) Fixed enemy body pickup trigger sometimes not working after enemy died while looking at it

* (Multiplayer) Fixed sticky bombs not working for clients

* (Multiplayer) Fix trees not syncing properly for clients after host went back to title scene once and started a game again

* (Multiplayer) Fixed enemies not appearing in caves in multiplayer, if client entered cave alone

* (Multiplayer) Fixed some animation glitches when fighting enemies as client

* (Multiplayer) Fixed creepy mutant ragdolls disappearing for client

* (Multiplayer) Fixed mutant position popping slightly when dying as client

* (Multiplayer) Clamped player velocity when chat window is open

* (Balanced) Slightly lowered pale mutant speed and aggressiveness

* Fixed missing twinkle when crafting items

* Ocean update - lower memory allocations and hopefully fixed all cases of glowing sections visible from some parts of world

* Fixed equip light message staying on screen when player dies

* Fixed wrong darker material on one of the built stick from simple and rockpit fires ghost

* Fixed rock hole in geese lake waterfall

* Fixed some trees being hard/impossible to cut due to cut point being positioned too high

* Caves - Removed all old rocks from cave 1

* Caves - replaced cave 1 hanging skull lamps with dynamic versions

* Caves - added more sfx to cave 1

* Fixed big trunk suitcase launching player when broken apart and minimized amount of broken apart pieces

* (Performances) Optimized fire warmth system

* Fixed issues with mutants dealing damage to player while on ground/at a distance

* Defensive Wall Gate can now be opened and closed from both sides !

* Fixed incompatibility between stashing lighter while holding burning weapon and put out burning weapon features from last patch

* Allowed back drinking dirty water in pot from inventory

* Replaced deprecated input action name "useDistration" by actual semantics "WalkyTalky"

* Fixed adding non crafting material items (i.e.: soda) on the crafting mat for storage in metal tray causing duplicate views to be created

* Audio - Balanced tent flapping sound on old tents

* Fixed burnt female body having wrong textures plugged in

* Fixed all gamepad menu navigation issues

* Fixed keycard not going to inventory when picked up

* Fixed log count issue when placing platform

* Fixed camera stutter when drinking at a lake with empty hands

* Fixed louis suitcases breaking into too many pieces

* Fixed incorrect outline shader settings on a bunch of inventory items

* Fixed big creepies blood textures fading on instead of snapping on

* Fixed seam in regular female blood texture

* Fixed Virginia ragdoll stuttering wildly sometimes

* Fixed seams on Cowman

* Overlay icons are now visible from either cave or outside world when located within sinkhole area (i.e.: in MP you don't need to be in caves to see the marker indicating backpack location)

* Fixed rope in cave 2 not correctly aligned causing hands to not visually attach

* Added whoosh sfx when toggling custom wall addition

* Building repair action icon is on the 3D billboard icon instead of the 2D action icon

* Fixed Armsy getting stuck on wooden planks inside cave 7

* Creepy mutants can now break down wooden planks

* Fixed some items missing in some cave greebles causing performance to tank due to errors

* Change book text to just ‘for timmy’

* (Balance) Slightly lowered contrast on grey dying image effect to make it easier to see when in low health state

* Fixed hits sometimes showing blood but no hit reaction, when attacking enemies

* Aiming reticle now always looks up instead of aligning with ground

* Aiming reticle now uses player position as base position for the trajectory calculations instead of item position (slightly less accurate but far more stable)

* Defensive wall gate now has an icon an each side

* Changed multi - thrower holder icons to the generic add/take ones

* Fixed thrown spear sometimes passing through cave rocks and other objects

* Position basket icon on catapult closer to centre

* Fixed bug where enemy would spill blood without being hit or playing hit animation

* Fixed water drink icon looking darker than all other icons

* Fixed saving used content of yellow crates

* Replaced door lock model by a single sided door lock one

* (Audio) Lowered volume of cow man when close

* Added tree structure cut leaves system to pine / moss / winter trees!

* Garden now toggles to whatever seed type player has available, fixing issue of garden eventually getting stuck on a not available seed type without possibility to switch to another one

* Added exit tutorial when in manual upgrading mode

* Fixed plane going through water briefly sometimes during crash

* Fixed hud visible during sleeping black screen

* Fixed cowman sometimes not doing 180 attack on player standing directly behind

* Re\* arranged triggers so that switching between gate and repair trigger is easier when looking at a damaged gate

* Moved shelter's repair trigger position outside of its logs

* Fixed wall lods not having a visible door past lod0

* Now forcing sun rotation update until past the last frame of sleeping to ensure it is up to date afterwards

* Sleep black screen is now 1s longer

* It is no longer possible to add meat to drying racks built in water (like fires)

* Fixed soil in gardens not casting shadows and darkened dirt piles to make them easier to see

* Tennis players and lawyers now show up on passenger manifest

* Fixed axe getting stuck occasionally when doing repeated ground chop attacks

* Fixed player movement getting stuck when entering rockThrower while crouched

* Caves - fixed hole in cave 3

* Caves - lighting and layout work in cave 8

* Caves - fixed hole in cave 7

* Reduced rotation speed of enemies when doing jumping attacks, prevents enemies appearing to orbit around player position

* Fixed molotov/burning weapons sometimes getting put out when player has water at ankle level

* (Performance) Fixed high physics cost from sound detection system when moving around in caves

* Audio - lowered volume of held dynamite

## v0.39b patch (released May 25th, 2016)

* Fixed reticle for dynamite and flares shaking in distance

* (multiplayer)Fixed explosives thrown via thrower sometimes kicking clients

# v0.38 (released May 11th, 2016)

* All equipment pieces on the crafting mat can now be equipped directly from there!

* Enemies will attempt to run away from thrown bombs more often

* Burning weapons are now put out and can be relit for remaining burn duration when entering a water trigger

* Burning weapons are now put out and can be relit for remaining burn duration when stashed (i.e. when climbing rope)

* Passenger manifest is no longer automatically equipped while in combat

* A simple press on the "Lighter" button now stashes it when holding a lightable item (holding the button still lights the item)

* Fixed equipping pot in inventory

* Revamped roofs to show autofill preview by default (like floors)

* Fixed switching floor between autofill and manual placement when there's a preview floor displayed causing preview structure to remain visible and eventually causing improper icons to be displayed

* Fixed lighter sometimes being equipped while survival book is open

* Fixed teeth no longer dropping when hitting enemies

* Fixed incorrect normals on plane seat metal

* Plane crash set to nighttime and relit plane and abduction scene

* Adjusted enemy layout in caves 1, 8 & 10

* (balance) Increased player walking sound detection range

* When woken from sleep, enemies will now walk towards the sound source

* (balance) Increased speed and aggressiveness of large pale mutants

* Fixed mutants occasionally getting stuck in fall pose when dropping down from ceilings

* Changed armor hud display formula to be solely based off amount of pieces equipped and not armor value (boots cold protection no longer shows at all in this)

* Now saving cloth (burning) weapon upgrade

* Fixed plastic torch not getting bloody anymore

* Each deer skin armor piece now has 10 HP and can be destroyed like all other armor types

* Ghost stairs now use a half log as default mesh

* Dynamite can now be attached to walls & trees

* Aiming reticle is now 3x smaller and has a vertical cylinder halo

* New art added - campsite junk

* Added more props/layout and details to old film crew camp

* Hanging scene now only shows the equip light tutorial and no other hud element

* Fixed skin shading appearing black when using legacy renderer

* (particles) Improved look of flies (made darker, especially in caves)

* Player now conforms to the angle of terrain when dying and injured

* Adjusted timmy toy position on plane to make it more visible

* Fixed cave mutants when feeding on limbs sometimes not being alerted to nearby player

* (balance) Increased health of pale skinny cave mutants

* Caves - fixed intersecting sticks in cave 1

* Caves - brighter lamps

* Caves - fixed skulls inside walls in cave 1

* Caves - removed bone texture from timmy drawings room

* Caves - removed old rocks from Cave 1

* Caves - fixed some rock textures

* Caves - fixed bad value on hanging body in cave 5

* Caves - brighter bible textures

* Caves - work on badly placed stalagmites

* (Performance) Halved mesh resolution of main building log

* Increased quality of collision detection of flare gun flares so they work better in caves

* Fixed ghost custom effigy rendering issues

* Caves - Better collision on main cave rocks

* Caves - Moved Climbing Axe to cave 9

* Creepy enemies now spawn blood particles when hit

* Added a restore defaults button in main scene's control settings panel

* Fixed icons not refreshing when pressing escape while in control settings panel after changing an input mapping without saving

* Fixed pressing escape while having the input mapping conflict resolution popup, it now has same effect as pressing the cancel button

* Fixed a case of input mapping override not getting applied correctly

* Audio - Fixed missing sound effect for cave door in sinkhole

* Audio - Increased Bats flying out of caves sound

* Audio - Fixed missing book opening sound

* Audio - Increased volume of page turning sound effect

* (particles) Added broken glass particles to plane crash scene

* (particles) Dust and small rocks will now explode out of broken stalagmites when hit

* Caves - adjusted tennis player lod so they don't pop on

* Caves - added more save tents deeper inside caves

* Caves - replaced old skull lamps with dynamic versions

* Caves - cave 7 entrance work

* Caves - more lighting in cave 7

* Caves - fixed hole in cave 7 where you could fall out.

* Armsy is faster and more aggressive now when attacking player

* New death and melee reaction animations added to armsy

* Virginia is now faster and more aggressive when attacking player

* Updated enemy cave layout to have more difficult enemies in later caves

* Added back missing stars to night sky!

* (Balance) Climbing axe now only works on climbing walls

* Added blood particles to babies when hit, and to their ragdolls

* Caves - Smaller peek hole in cave 8

* Caves - Fix for door popping in inside the sinkhole.

* Cave - Fixed ceiling too low in cave 8 exit to sinkhole

* Moon cycles added!

* Audio - Fixed mutant audio not pausing when player was in inventory in single player giving illusion game wasn't actually paused

* Fixed ghost rock holder loading from save file as a stick holder

* Audio - plane crash sound now gradually fades out if plane crash is skipped

* New building: Rock Path ! Place and extend it like custom walls, conforms with terrain when placed, cuts grass when built

* Fixed dropping bones & fixed inventory item tooltip displaying 0 bone after dropping last bone

* Fixed enemy club not displaying pickup icon when dropped

* Fixed dropped enemy club using old mesh/old texture

* (multiplayer) Fixed player\_net molotov fire looking different than local player molotov fire

* Limited the amount of turtles that can spawn over time

* Fixed ghost sometimes rotating automatically

* Lowered opacity of stealth icon and lowered position on screen

* Climbing wall made brighter, and added leftover old climbing props on wall to make climbable clearer

* Updated enemy layout in cave 5

* (balance)Added more supplies to cave4 room (Virginia room)

* (balance)Added food and soda near cave 5 air pickups

* Replaced granite cave rock material with mineral rock material

* Added more fat mutants to caves

* Audio - New creaking large tree sound added

* Removed loose sodas and cash pickups from caves, instead these are found on bodies, under bodies, or in suitcases/crates

* Added small rock pickups to caves to aid with stealth (hint: try throwing them as a distraction)

* Audio - added new distant cave variations to various caves

* Audio - Bats exiting caves will now play multiple squeals and squeaks

* Fixed custom effigy not working after being damaged and repaired

* Fixed garden plant flashing big when planted before getting proper size

* You will now only get cold in cave water if you stay swimming in it for 12seconds or more

* (Multiplayer) Fixed saving inventory for clients

* Fixed creepy mutants not breaking apart stalagmites inside caves

* Merged walkway and procedural floor in a single placement tool, bring near terrain to swap to walkway or bring it back up to swap to extensible floor which can be added to a custom structure

* (Balance) Added more rocks/layout to bottom of sinkhole and tweaked enemy positions/layout

* New art added: Corpse piles, added to cave 6

* Audio - added new extinguish sound for when molotov is put out by water

* Survival book pickup added to the start of plane crash sequence

* Add hit reaction animation to cowman

* (Audio) Added experimental “Voice Count” in gameplay sound options to hopefully work around some audio issues for some players.

## v0.38b (released May 12th, 2016)

* Fixed enemy clubs duplicating when picked up

* Fixed wall door not being respawned correctly when wall was repaired

* Fixed missing louis crate in caves, and made breakable - now contains cloth inside and made new model/textures

# v0.37 (released April 29th, 2016)

* Improved sinkhole cave door textures

* (Multiplayer) Fixed molotovs thrown from multi\* thrower not breaking correctly for clients

* Fixed lizard ragdoll distorting when dropped if carrying maximum amount already

* Fixed partial ocean waves visible inside yacht when outside yacht

* Fixed animation issues when picking up small rocks/tennis balls while blocking

* Better yacht interior and exterior reflections

* Fixed life preservers clipping in cave 10

* Increased speed/aggressiveness of cowman mutant

* Audio - House boat now plays audio event when on water.

* Audio - Added impact sfx when the rope swing trap hits enemies or player

* Audio - Tuned wet footsteps and leaves falling sounds

* Audio - Tuned tent flap sounds

* Audio - Added drop sound to many items when dropped

* Audio - Added waterfall sounds to waterfalls in sinkhole

* Audio - Player now gasps for air when surfacing with the rebreather equipped

* Audio - Armsy now makes sound when detecting player presence nearby.

* Audio - Improved deer audio when deers are set alight.

* Audio - Fixed doubled up fall sound effect in multiplayer

* Audio - Fixed building repair sound always playing from hosts location in mp

* Audio - Fixed push sled sound not being synced in multiplayer

* Audio - Fixed player burning vocals not being synced in multiplayer

* Caves - Fixed holes in cave 10

* Caves - Fixed various rock scale issues

* Fixed player not taking fall damage while doing flying axe attack

* Fixed block animation not showing correctly for remote players in MP

* New art added: Timmy crayons

* Cleaned up/improved some areas around beach cliff terrain

* Improved player fall down injured animation

* Caves - Fixed cave 9 sinkhole entrance not being visible from above ground

* Caves - adjusted some misaligned rocks in sinkhole

* Enemy skull bag effigy added more pick up skulls

* New art added: Dead lawyers 1 body, 2 heads. Court papers, suitcase etc.

* Cliff rocks will now appear wet/dark based on height of ocean

* Ripped Practical Caver magazine version for survival book notes section

* (Multiplayer) Fixed missing lighter texture on other players lighters

* New craft recipe: Weak spear (stick x2)

* New gameplay option: Crouch Mode (Hold / Toggle), default is hold (legacy feature)

* Filled Waterskin now holds up to 2 full thirst replenishment and drinking from it is now based on exact amount so you can replenish as often as wanted without worrying of wasted amount

* New (outside) waterfall falling particles added!

* (Multiplayer) Fixed host sometimes appearing on angle for clients in MP

* Fixed/improved uv's on yacht interior

* Current armor display in hud is now based on max amount of both armor and cold armor

* Adding item to weapon rack structure now properly clears up cloth and/or fire

* (Multiplayer) Clamped player velocity when pause menu or player menu is open

* Increased water jump height slightly to make it easier to get onto raft while in water

* Caves - Fixed timmy drawing 2 in cave 1 not being pickupable

* Caves - Fixed hole in cave 1 leaking light

* Fixed offset between cursor and actual click position in menus

* When having a healthy diet, weight now goes towards base value at a very slow rate (player no longer stays at a bad weight when being healthy and instead goes back to normal)

* Fixed food & blood poisoning settings preventing it from being effective

* Rephrased lighter tutorial to be more generic and work with flash light as default light

* Added another shelf to medicine cabinet

* Improved positioning when placing ghost medicine cabinet

* New snow particle effects added for mountain/snow area

* Fixed geese sometimes floating above water

* (Multiplayer) Fixed animation glitchiness when dropping bodies as client in MP

* Weather system now shows snow particles instead of rain if player is in snow area

* Audio - Sinkhole ambient audio working

* Fixed blur on particles when pause menu is open

* Fixed basic fire being on slight angle when placed

* New fire effects!

* New blood effects!

* Rock fences can now be used as support for floors and roofs !

* Fixed enclosed walls not properly storing data, causing stacked walls to not go all the way around

* Fixed some issues with placing floors/roofs on non\* flat walls, it now tries to cancel positions that are too far from the rest to try preventing floors from floating mid air,   
  eventually cancelling autofill if not enough points remain

* Revamped floors to toggle between autofill and manual placement mode, by default in autofill floors will now show the ghost of whatever support is currently targeted and can be placed with E   
  (or switch to manual placement with C to cherry pick each point like in legacy)

* (multiplayer) Fixed jerky crocodile movement for clients

* (multiplayer) Fixed animals not aligning to terrain correctly as client

* Increased hit trigger range of deadfall and swinging rock traps

* Player now disconnects from logsled when falling from a height

* Logsled no longer floats if pushed into sinkhole

* Audio - mutant dodge roll audio added

* Fixed fires turning huge if burnt out while culled then lit again

* Fixed hole in player mesh visible to other players in MP

* (particles) Improved look of lighter flame

* New magazine/story item pick up added!

* Revamped upgrade system: You now get to manually position your upgrades ! Start by making the upgrade recipe as usual, then rotate the item with Horizontal/Vertical input actions   
  (WASD on keyboard by default), aim with mouse, and left click to place ! Repeat until all upgrade views are in place or right click to cancel upgrading

* Upgrading system now tries to take items in inventory after ones from recipe have been used to keep placing until player quits upgrading

* Fixed positioning of glass upgrade views

* Increased book tab numbers readability

* Audio - tuned mix of player footsteps on wet surfaces, lakes, rivers, leaf rustle cardboard drags and after storm sounds

* Audio - new jump/land on snow sfx

* Audio - added dynamic sfx to broken parts of cages

* Audio - new audio event for upgrade success

* Fixed umbrella effigy having single sided faces and improved shading

* Fixed some items in enemy built effigies not being pickupable

* Added moss to enemy placed effigies

* New molotov fire effect!

* Moss added to plane hull shader. Moss will accumulate over the days eventually turning the plane moss covered

* Cleaned up cook icon

* Fixed some of the Dead Trees being uncuttable

* (Multiplayer) Fixed clients not getting logs from dead trees

* Fixed upgrades not properly applying bonus + also fixes reloading flare gun with flares

* New graphics option: SSAO Type ! Option are SESSAO (legacy) and the new HBAO (should render faster)

* Recipe tutorial now goes away as soon as there is any valid recipe on the crafting mat

* Having a burning weapon in right hand now counts as a light in regards of the equip light tutorial in caves

* Added a fail safe when starting game with a Steam Controller active but the "Advanced Controller Support (XInput)" option not selected

* Added a device management tab to control settings in title screen, allowing either all devices as input (legacy) or to cherry pick which should be used   
  (allows to disable input sources conflicting with the game, and thus no longer require to be unplugged to play the game)

* New crafting information page in book: Clothing !

* Setup expand tabs for crafting and notes chapters of books

* Fixed some navigation issues in between information chapters of book

* Poison arrow can no longer poison player when shooting while sprinting forward

* Fixed meat on rack not properly syncing status updates with clients

* Meat placed on drying rack by clients no longer goes away when client disconnects

* Audio - added new close surf sounds

* Fixed thrown molotov missing fire

* New improved FXAA added!

* Broken stalagmites should now react to cave floors instead of falling through them

* Fixed missing item throwing reticle

* Added dynamic movement to new lighter and molotov flames

* Increased speed and range that weapon will move away when close to a wall

* (balance) Removed soda/meds spawning from dead mutant bodies

* Fixed wall chunks replaced by a textured quad at a distance also getting cleared out of the navigation grid

* (Multiplayer) Fixed clients not seeing animals after an extended play time!

* Fixed held molotov blur breaking when camera moved

* Fixed throwing unlit molotov at unlit fires lighting it

* Fixed Alt tab breaking opening animation of crash

* (Multiplayer) Fixed picking up logs in holder while jumping causing it to vanish, it now properly drops the log

* Fixed having a movement key pressed bringing mouse back to center of screen while in menu

* Audio - added sound of liquid when equipping a molotov

* Audio - Balanced ocean sounds

* Audio - added squeal to burning babies when they die

* Audio - added leafless whoosh when burnt trees fall

* (Multiplayer) Fixed blocking animation cutting off for remote players

* (Multiplayer) Fixed client picking up animal yields leaving a broken duplicate copy behind

* Fixed rain emitters not properly following player rotation

* Cleaned up position of building buttons in book!

* Enabled popups for resolution & preset options settings (should help setting things up on lower end hardware)

# v0.36 (released April 6th, 2016)

* Fixed opening survival book breaking look at special item animation

* Improved skinning on small bird wings

* Winter TopHeavy pine now drops sticks

* Fixed timmy's shirt clipping through body during plane crash

* Fixed timmy legs clipping through seats during taken away cutscene

* Fixed No Hud option not working

* Fixed top part of ghost Ex\* Platform looking different color than rest of building

* Feathers are now detached from bird ragdolls thus remaining active even after small meat has been picked up

* Fixed cave map clipping through legs while crouch walking

* Fixed dead sharks sometimes duplicating on contact with player

* Bloody tables now move when hit with melee weapons

* Fixed player grabbing end of burning stick while blocking

* Fixed wrapped cloth clipping with held stick

* Fixed cash sometimes getting stuck when spawned from hanging bodies

* Fixed player being able to double jump while player menu is open in MP game

* Better single armed block pose on player

* Fixed anim glitch when transitioning into single arm block

* Catapult can now be built on the raft without it sinking

* Effigies now save burn status and done duration

* Closing inventory or removing an item from crafting mat while implanting upgrades now attempts to instantly place all the views

* Underwater air consumption stops while time is paused in SP

* Paint on weapons is now saved

* Blood on weapons is now saved

* Fixed stashing bow while looking down leaving the toggle arrow type icon active

* Eating cooked or dried arm & leg now also yields 1 bone

* Fixed sinkhole rocks making bush hit sound and giving leaves when hits

* Opened up blocking to cave system at bottom of sinkhole!

* New art added: (Text removed \* SPOILER)

* Fixed crafted axe not getting bloody

* Fixed black line passing through ghost objects against horizon at night!

* (audio) Rabbit Boots reduce/muffle sound of footsteps when worn

* New option menu look matching new UI look

* Fixed swimming no longer cleaning weapons, it now cleans all weapons in inventory

* Reworked top of sinkhole mesh to make it harder to glitch down it

* Removed sinkhole blocking collision, you can now jump down to your death if you like. Or if you have the climbing axe climb down! (or up)

* You may now build in/out the sinkhole

* Fixed enemies not appearing at bottom of sinkhole area

* Dying inside the sinkhole no longer plays the drag away sequence

* Fixed duplicating equipped item using batch in inventory

* (multiplayer) Fixed crocodile looking different/worse than single player version

* Fixed watch missing fake drop when you pick up more than you can carry

* Fixed arrows sometimes bouncing off deer and other animals

* Fixed host game new game and continue buttons being flipped compared to single player

* Fixed lighting fires loaded from a save with 0 fuel causing errors and killing performance

* (Multiplayer) Fixed jerkiness in some player animations

* Limited ability for player to stand on extreme slopes

* New building: Multi Thrower ! (replaces the rock thrower) Most right hand held items can now be added to the holder. Projectiles such as bombs produce their standard effect while other items act like rocks previously did

* Meat picked up from multi thrower is now always spoilt

* Fixed some issues loading saves with meat in inventory

* (Multiplayer) Stand up animation added when revived

* Fixed animation breaking after being revived from dying while on a rope

* Fixed player not being able to climb ropes while affected by poison/cold/thirst etc.

* Fixed player doing knockdown animation if hit with explosive while in water

* New art added: 5 new timmy drawings

* New timmy drawings placing system: Hold timmy drawings while looking at a wall and press the Craft button (‘C’ on PC by default)

* (audio) New audio added for multi\* thrower

* (audio) Fixed clients not being able to hear dropped body sound

* (audio) Fixed missing cave water splatter sound effect

* (audio) Sticks dropped from saplings, effigies and bush2 now all make a dynamic sound when hitting ground

* Improved shadows inside sinkhole

* Fixed cowman not dealing damage to structures and walls

* Sinkhole cubemap added to sinkhole water

* New rocks added in sinkhole to (hopefully) prevent players surviving jump in by landing in water

* (Multiplayer) Fixed ghost rock fence looking filled when placed

* New art added: Sinkhole entrance models x3

* Fixed Climbing axe halting player in mid\* air if used on wall while falling/jumping

* Fixed yacht magazine in cave10 being caver magazine when picked up

* More accurate sinkhole ground collision added

* Fixed camera shaking if grabbing onto a cliff with climbing axe while falling

* Fixed player block reaction animation sometimes not playing correctly

* Fixed player not damaging other players with downward axe strike

* New building: Rock Side Platform ! Bring a procedural platform next to a big rock to swap to a lighter structure attached by the side to the rock. Has 3 anchor points

* Stopped player receiving camera shake from cowman footsteps while in water

* (Multiplayer) Fixed loading save as host sometimes causing duplicate ghost bridge to show up client side

## v0.36b (released April 7th, 2016)

* Fixed issue with some partially built platform meshes rendering on top of everything else

* (multiplayer) Fixed platform cost being higher than it should be in some circumstances depending where placed on terrain

* Fixed platforms red tint when not placeable

* Fixed issue with body drop sound effect erroring causing slight stutter and missing sound

* Fixed some issues with placement of platform breaking under some cases

# v0.35 (released March 24th, 2016)

* Player now drops held logs when swimming

* Fixed single/first arrow not upgrading like others

* Fixed destroying nested building from old saves causing damage to parent structure, they no longer propagate any damage if not having the right destruction setup

* Fixed skull lamps sometimes not visible after loading a saved game

* (Multiplayer)Fixed overflow dynamites fake dropped from picking up in trading tray exploding

* Fixed arm mesh poking through sleeves on player model

* Fixed log sled movement glitches when driven over a happy birthday trap

* Added dodge animations to regular cannibal types

* Caves – Bloody table and robot toy part are now dynamic

* Improved first person crouch walk/idle animation

* Caves – loose heads and headless body now have sound if you hit them.

* Fixed crocodiles killing player in 1 hit

* (Multiplayer)Fixed dying by crocodile breaking respawn in MP

* Fixed player being able to walk along the ocean floor while underwater

* Better held position of toy head pickup

* Fixed heavy axe behaving like a stick if swung while jumping

* Fixed cave map sometimes not loading correctly from saves

* Rock based fires that are destroyed now spawn a partially filled ghost after showing the broken apart model (you have to put sticks & leaves in to restore the fire)

* New art added: Fig tree re-do

* Blood now washes from weapon/body if player is crouched in shallow water

* Dynamic trunk/leaf bending added to falling trees

* Fixed exploding wood particles in chopped trees from pushing player around

* Better held position of spear on player in MP

* Fixed playing in vegan mode clearing out caves for good (not retroactive)

* Fixed taking damage when going through legacy wall with door

* Added an icon as visual feedback when using the ‘batch’ place building feature

* (Performance) Massively lowered physics per frame allocation cost

* (Performance) Reduced allocations involved in the tree burning process

* (Multiplayer) Clients may now burn trees even if away from host

* Improved collision on huts, and fixed bug where if holding climbing axe huts were climbable

* Fixed crosses on wooden walls sometimes hanging in air after wall has broken away

* Fixed yacht windows reflecting trees

* (Multiplayer) Fixed cave map positioning on remote players and removed the fully revealed map material

* (Multiplayer) Fixed head bomb exploding when dropped from picking up in metal tray while full

* Fixed log pickups sometimes having the E action icon visible from far away

* (Multiplayer) Now syncing rotation of fire particle, should better follow weapons

* (Multiplayer) Now spawning correct amount of overflown items when trying to pick up from metal tray while full

* Fixed toggling Defensive wall gate increasing log count in build mission

* Toggling partially filled Defensive wall and defensive wall Gate now drops back same amount it would have if ghost had been cancelled

* Fixed bonfire not lightable after going out of fuel

* Cutting down a tree that has a ghost building attached to it now properly destroys it in Single player

* Tree structure ghost destroyed through removal of the tree now drops back same amount it would have if ghost had been cancelled

* Fixed picking up held only item (i.e.: small rock) while holding logs causing the small rock to vanish, now logs will be dropped and the item equipped

* Lods – fixed inside of plane vanishing from some distances. Added new lods for anchor and big dead wood to stop them popping on. Fixed camping chairs pop on distance. Fixed tennis team corpses popping on. Fixed dead seaweed popping on, now stipples on.

* Added missing collision to beach anchor

* Berry bushes now have touch bending!

* Fixed batching items in inventory being limited to amount of views in inventory

* Fixed setting the default arrow type to use with bow on the crafting mat

* Fixed bone fence collider height, stacking other buildings on top of it shouldn't leave a huge vertical gap anymore

* Added door visual to legacy wall doorway ghost

* (Audio) Improved and balanced bird chirps sound effects

* Yacht & Caver magazine kept in notes of survival book is now a ripped piece of the cover

* Improved pickup auto equip feature: it will now work regardless of current state of inventory, this way it goes through even while item slot is locked while equipping another item (hint: allows super fast combat style with spears)

* Winter Top Heavy tree has new fire points

* (Multiplayer) Fixed player count stuck at 1 for clients

* (Multiplayer) Fixed delayed action icon (the white circle filling in black) sometimes staying up when action was first completed by another player (i.e.: resetting traps)

* (Multiplayer) Fixed client resetting Happy birthday trap while in its trigger causing trap to be sprung on host side but not client

* (Multiplayer) Fixed loading a saved game inside yacht as client causing player to swim and see ocean through yacht

* (Audio) Added book close sound effect

* (Audio) Added new sound effect for when player blocks

* Maple trees are now burnable

* Fixed blocking animation breaking sitting on bench action

* New structure: Catapult added

* Fixed fish sometimes swimming through yacht

* Fixed camera shaking continuously if grabbing a rope while falling

* (Multiplayer) Consuming blueberries in garden no longer removes the whole bush and instead each individual berry can be used as expected

* (Multiplayer) Fixed missing mud after rain for clients

* Now saving which garden blueberry have already been used so that gardens no longer respawn at full yield after loading a saved game if previously consumed

* Fixed cave map sometimes not loading correctly

* (Multiplayer) Fixed an issue with streamed cave props causing lag on remote endpoints

* Fixed arrow combined with bow losing its bonus

* Added Steam username display in save slot screens of title scene, defaults to Anonymous if not connected, should make it clearer that you have to be connected to your own account to see your saves and avoid feel of having lost save files

* New item: Small generic meat ! Can be cooked on fires. Dropped from Squirrels and most birds. Yields lower fullness, health and energy when eaten than other meats

* (Audio)Tuned volume and distance setting for mutant corpse burning on campfire

* Fixed automated removal of multiview items from the crafting mat when closing inventory

* (Multiplayer) Fixed adding first material to repair buildings not refreshing display

* (Multiplayer) Fixed first tick of toggling wall addition not going to window

* Traps reset trigger now uses a 3D sheen billboard icon instead of the 2D icon

* Fixed oysters starting with the “none” decay state

* (Performance) Optimized inventory animator scripting cost

* Creepy mutants will attack walls and structures that are blocking the path to the player more often

* White tents no longer climbable with climbing axe

* New title screen!

* New pause menu – and now blurs camera instead of black screen backing

* New dead screen and dead eaten animations

* Fixed attempting to climb rope while sitting on a bench breaking player animations

* (Multiplayer) Fixed clients being unable to deal melee damage to armsy

* (Multiplayer) Fixed player's weapon fire not following weapon perfectly on remote avatar

* Fixed bird landing on hand breaking the lighting campfire sequence

* (Multiplayer) Fixed high CPU usage when loading old save with tree structures attached to trees that no longer exists

* Updated Crafting pages in Survival book

* Caves – Fixed cave blocker intersecting cave 7 entrance.

* Fixed sapling 2 fading on too close to player

* Caves – Fixed dead body intersecting with pedestal in cave 5

* (Multiplayer) Fixed birds flying into fires for client

* Custom effigy can now always be lit by everyone when there's no limb attached but will have an effect area of 0

* (Multiplayer) Fixed bug with steam lobby displaying very few public games

## v0.35b (released March 24th, 2016)

* Fixed bone armor broken in patch 0.35

## v0.35c (released March 25th, 2016)

* Fixed issue where getting out of water after swimming could be sometimes be difficult/impossible

* Fixed issue with Virginia and possibly some other ragdolls moving around violently when killed and tanking fps

* Blocked players from opening book whilst using catapult

* (multiplayer)Fixed issue with invites send outside game not appearing on title screen

* (multiplayer)Fixed dead screen not displaying correctly in co-op games

## v0.35d (released March 25th, 2016)

* Fix for dying inside a cave in singleplayer causing hud to vanish

# v0.36 (released April 6th, 2016)

* Fixed opening survival book breaking look at special item animation

# v0.34 (released March 8th, 2016)

* (Multiplayer) Fixed item duplication when quickly picking up items that are spawned when picking up something while being full

* (Multiplayer) Fixed player anim breaking if killed while holding a logsled

* (Multiplayer) Fixed sun rotation not matching time of day when starting game as client

* (Multiplayer) Fixed bug where clients could not share items with each other only with host

* (Multiplayer) Fixed player\_net held cave map looking transparent for other players

* (Multiplayer) Fixed trip wire traps sometimes leaving bits behind after being triggered by client

* (Multiplayer) Fixed delay/flash when placing walls and fences as client

* Skinny mutants will sometimes attempt to avoid player attacks by rolling out of the way

* Birds will attempt to avoid flying through trees and structures now

* Fixed entering cave sometimes breaking if player was blocking while entering

* Improved look of player bone armor

* Improved model/textures of mutant leader props

* Fixed player arms still appearing to hold oar for a second when disconnecting from raft

* Suitcases now stipple on instead of popping in

* More accurate Bone Fence image in survival book

* New art added – plane bathroom!

* Rain now has a maximum time limit to avoid raining for entire days

* Sharks now swim at varying depth and can be killed

* State of cave enemy encounters are now saved! Instead of all the mutants respawning when you re-enter a cave.

* Burnt trees trunks now turn into small log pieces

* Fixed blood on female mutants not syncing on death

* Fixed flying axe attack sometimes not triggering correctly

* Fixed missing motion blur on mutant baby

* (Balance) Slightly faster transition into heavy axe attack

* Stick swinging now blends correctly with walking animation

* Fixed fern alt being difficult to cut due to positioning of trigger

* Improved some player third person animations

* Improved sapling 1 billboard, now uses vface shading

* Fixed cave mutants sometimes spawning in very close to player

* Blocked bird from landing on player hand while survival book is open

* Fixed slight delay on stealth icon removal when standing up from crouch

* Virginia is now more deadly at close range

* Fixed blue creepy mutants skin not syncing on death

* Fixed repairing bone & arrow basket breaking display of content

* Made stealth eye icon less opaque

* Improved some tree/cliff/rock intersections

* All book pages now have a numbered tab which expands from the chapter tab when hovered over

* (Performance) Halved ocean waves allocations per frame

* (Performance) Improved memory usage of ai pathfinding routines

* (Performance) Further optimized physics usage on animals

* (Performance) Reduced memory allocations on ai routines

* (Performance) Reduced memory allocations of cave map revealing system

* (Performance) Several minor allocations improvements

* (Audio) Fixed some sounds not being affected by volume slider

* (Audio) Added exertion sound when a log is dropped

* (Audio) New burning bodies and bones breaking apart sound added

* (Audio) Improved underwater ocean audio

* (Audio) Arrows hitting trees now have a sound effect!

* (Audio) Added sound effect when player held shield is hit

* Fixing some trees/plants in wrong areas, in water, inside sinkhole etc.

* Blocked look at arms animation playing while survival book is open

* (Audio) Caves – fixed footstep sounds in caves

* Blur removed from crafting and notes tabs in survival book

* Ground axe chops now adjusts based on the angle of terrain

* Clamped player rotation when chopping trees, in the same way as chopping at ground

* Fixed dropping lit dynamite spawning an unlit one

* Collision from above with a collapsing foundation now kills player

* Collision from above with a collapsed structure now deals damage to player based on velocity (i.e.: flying log)

* Plane fixes – fixed missing net under seats, fixed small gap in wall. Fixed/improved plane distance lod and cockpit lod

* (Audio) Dead bodies and limbs should now sound fleshy when hit

* Tread water animation added when swimming and stationary in water

* Fixed some anim popping issues when transitioning into swimming from walking

* Fixed arms clipping through rebreather when swimming underwater

* Fixed falling from a height sometimes causing mouse rotation speed to decrease

* (Audio) Added sfx to skull rolling away when getting axe in hanging cutscene

* Fixed a bunch of holes in terrain/cliffs in snow area of map

* Removed black squares from cowman

* Improved skin deformation on cowman

* Fixed Rope, Circuit boards, air canisters and booze vanishing when players attempt to pick them up whilst already holding maximum. Will now spawn dropped version.

* Caves – fixes to cave 8 sinkhole entrance

* New procedural Defensive Wall addition: Defensive Wall Gate ! Ghost DW chunks can be turned into standalone one-sided gates (same fashion as regular wall window/doors) and 2 concomitant one-sided gates will automatically merge into a 2 sided gate, you may then toggle the gate again to switch orientation, or again to go back to DW chunks
* (Multiplayer) Fixed hand icon occasionally getting stuck on screen after trading with another player

* Fixed fire over sky breaking over horizon!

* Fixed mutant babies becoming invincible if hit with a burning cloth wrapped weapon

* Fixed batching multiview item on the crafting mat not working

* Fixed bugs when mixing fire/poison/regular arrows on crafting mat

* Fixed inventory batching with fire/poison/regular pile of arrows (both to and from the crafting mat), batching arrows will now only grab the targeted type (i.e. control click on poison arrow while having 7 poison arrow and 20 fire arrow in the pile will move only 7 poison arrow instead of 10 arrows with undetermined bonus)
* Fixed held arrow type switching when having a mixed fire/poison/regular pile of arrows, also fixes fire staying up on arrow sometimes

* Added R to toggle arrow type while looking down with having bow equipped (you can still use crafting mat to specify which arrow type to use in advance)

* Replaced glowing “B to close” text in book by a nicer looking image & the matching action icon when using a gamepad

* Fixed molotov exploding when dropped from sharing tray

* Fixed rockpit fires not lighting dynamite

* Player can no longer be cold and wet while being on fire

* Fixed cowman in cave 10 sometimes disappearing when approached

* Fixed mutants sometimes appearing to drag nothing, instead of a downed friendly

* Added dying in water animation when drowned or killed by shark

* Fixed crocodiles sometimes floating in the sky

* Increased chance of crocodiles attacking while in water

* Fixed lighter flame breaking when camera moved due to motion blur!

* New seed loot odds 70% = 0, 30% = 1 (was 50% = 0, 25% = 1, 25% = 2)

* New item: Aloe vera seed (can be planted in garden and wall plant pot)

* New item: Coneflower seed (can be planted in garden and wall plant pot)

* New item: Blueberry bush seed (can be planted in garden)

* You can now pick which seed type to plant in garden and wall plant pot !

* (Audio) Added hit from behind while blocking sfx

* Improved lighting on Timmy carried away scene, made red man clearer.

* (Audio) New sliding down rope sfx added

* Fixed client hit animation not playing when hit by enemy in MP

* Fixed mutant baby ragdoll not being removed after time

* Fixed turtles intersecting each other all the time

* New Upgraded Spear upgrade: Incendiary ! Combine Upgraded Spear with 1 booze and 1 cloth to burn targets when spear is thrown (one time use)

* Arrows on the crafting mat show the tint matching their current bonus

* (Audio) Added player crawl forward sfx during opening cutscene

* (Audio) Added player stand up sfx at end of plane crash

* (Audio) Fixed missing sound when spears hit trees

* fixed player animation sometimes breaking when sprinting up hills

# v0.33 (released February 18th, 2016)

* Fixed stick marker overlay flag icon sometimes missing in old saves

* Fixed issue with garden preventing to load properly from a save if it had planted seeds

* Fixed eating berries after failing at collecting with pouch because of having reached max carried capacity

* (Performance) Lowered grass displacement CPU cost during stutter/spike frames

* (Balance) Increased arrow poison tick delay & total duration

* Fixed player camera breaking when taking starvation damage while sitting on bench

* Fixed wake up music playing at wrong time at start of game

* Fixed a skinning issue on player sleeves

* (Multiplayer) Added left/right hit animations when attacking another player

* (Multiplayer) Added client hit prediction to player

* Added grass displacement to suitcases & food cart

* Improved sled grass displacement settings

* Improved rain particles settings to help it catch up with player when moving

* Optimized animal and enemy cpu usage

* Fixed cave 1 bats exiting cave at wrong position

* Fixed mutants sometimes spawning very close to plane crash on first day

* Applied new door physics settings to small cabin, log cabin, and legacy doorway

* Fixed arrow, thrown spear and upgraded spear not properly targeted when trying to pick it up, making it difficult to collect

* Thrown spear and thrown upgraded spear are now automatically equipped when picked up, thus making them a more viable hunting option most player built wood-based structures are now destructible!  
  (Not retroactive: already built structures in saved games will remain not destructible, but newly built ones will be)

* Fixed issue where fire thrown by enemies could cause explosions and destroy bases in multiplayer games.

* Creepy mutants in the overworld can now travel in groups with other mutants!!

* Tougher, pale creepy mutants can now be encountered in the overworld

* Slightly increased health of all creepy mutants

* Fixed applying bow arrow bonus with crafting cog while having bow equipped

* (Multiplayer) Fixed weapons sometimes not visible on other player

* (Multiplayer) Fixed enemies sometimes snapping into death pose as client

* (Balance) Removed the part of the weight formula which was causing it to change faster if player had lots of overeating points   
  (eating 10 chocolate bars in a row shouldn't cause player to take 5 lbs in a single day anymore, weight gain will however keep going for several days anyways until nutrition points are stabilized)

* (Audio) Added break apart SFX to non-foundation building collapsing

* (Multiplayer) Lowered MP data memory footprint of each non foundat ion based buildings by 95%

* Defensive spikes now use a combined spike log mesh to have proper distortion & destruction effects

* Mutants now become blackened and bloody when hit with explosives

* Fixed lighter clipping through various weapons when blocking

* Player can no longer spin freely when axe is contacting the ground with a downward strike

* (Multiplayer) Fixed quiver bonus not preserved after pickin g up backpack

* Poisoned arrows can now also infect players & animals! Pla yers can cure it with aloe vera

* Fixed tree stumps spawning wrong model in saved games

* Fixed cut up tree stumps being wrong size for some tree types in saved games

* Fixed Shelter, Log Cabin & Gazebo destruction looking weird with LODs wrongly taking part in the distortion/collapsing sequences of the destruction system

* Fixed small cabin floating above ground a little bit (not retroactive)

* Player can no longer hold anything he picks up while underwater, held only items are dropped again and other items can only go to inventory

* Underwater sound now triggers when water covers about half the screen

* Fixed projectiles not preserving memory of the previously equipped item after running out

* Fixed waterskin content not saving properly

* Caves – extended water zone in cave 9 climb entrance pool so you don't fall through to the ground.

* Caves – fixed short rope alignment in Cave 2

* Wall Garden image added to survival book

* Fire warm whole home system of custom buildings has been expanded to log cabins as well

* (Multiplayer) Fixed sleeping in temporary shelter not collapsing them for clients

* Trip wire traps are now triggered by nearby explosions

* Only fuel based fire weapons (such as molotov) will now cause enemies to flail around on fire, otherwise they will receive fire damage, stagger back but still remain able to attack

* Arrow on held bow now shows arrow bonus material

* Added poison arrow bonus green looking material

* Added arrow bonus material toggling to quiver arrows

* Fixed hair still visible when chopping off head of female mutant

* Removed hint from dead screen that tells players to build fires to scare away mutants since fire will attract them

* Caves – New cave 6 climb down entrance added

* Fixed seam on severed head model

* Added “stable” weight forward arrow in stats page of book

* Added the “fortune” story clue to pages 3 of notes

* Added page numbers to survival book sections to make clearer some building sections have multiple pages (i.e. custom building which has 3 pages)

* Wearing fur boots now correctly reduces the sound detect range of walking/running

* (Multiplayer) Improved fall to ground animation of mutants as client

* Fixed an issue with saves that have rabbit fur boots equipped, was stacking bonuses each time game was loaded

* Increased chance of seeing enemies drag away injured family members during combat

* New art added: small cave rocks

* Caves - rock clumps replaced with small cave rocks

* (Multiplayer) Player name is now hidden for crouched players!

* Fixed a case of enemies sometimes not transitioning to death animation

* (Multiplayer) Fixed issue with nested buildings causing clients to get kicked out when destroying foundations

* (Multiplayer) Fixed ghost vanishing for a second when placing buildings as client for all but custom building types

* (Multiplayer) Fixed not being able to gather arrows/spears from other players

* (Multiplayer) Fixed connecting issues with receiving multiple invites to the same lobby

* (multiplayer) Fixed enemies not turning head to client/looking at clients

* Fixed turtle shell shield not correctly blocking attacks

* (Multiplayer) Improved enemy spin around when hit reaction for clients

* (hopefully) Fixed some issues with enemies running into plane crash and getting stuck

* Added right click to drop from inventory action on spoilt meat

* Fixed issue with pond reflection in upper part of map

* Caves – Tighter light blocking around cave 10 climb entrance to prevent leaks

* Position of axe tip is now dynamically adjusted when hitting crocodiles/turtles and other objects

* Fixed player camera sometimes offset after plane crash when starting a new game directly after saving an existing game

* Fixed hanging enemies in noose trap being offset from noose position for client

* New craftable item: Bone Armor! (5 bones + 2 cloth)

* New armor formula based on armor HP, lizard & stealth armor take 20 damage, bone armor takes 40, following damage goes to the next armor piece and to player when there's no armor left

* Replacing a damaged armor piece doesn't give back the item in inventory

* Better positioning of all held animal heads

* Fixed random rocks & sticks found on ground stop spawning after picking up a bunch

* (Multiplayer) Fixed building warmth not functioning properly for clients

* Added dedicated destruction to bonfire (similar to other fires)

## v0.33b (released February 18th, 2016)

* Fixed issue with cutting down trees in some multiplayer save games

## v0.33c (released February 19th, 2016)

* Fixed performance issues in save games where players had rabbit fur boots

* Fixed clients getting kicked when foundation with fire on top is destroyed by an explosive

* Fixed an issue with armor values for new armor system

* Added compatibility with new system to previously equipped armor pieces

## v0.33d (released February 19th, 2016)

* (Multiplayer) Fixed log sled not working correctly for host player

# v0.32 (released February 6th, 2016)

* (Multiplayer) More natural spine rotation on player character

* (Multiplayer) Better crouching animation on player character

* (Multiplayer) Fixed equipped items not going into loot backpack when dying

* (Multiplayer) Fixed glitchy animation when dropping bodies as client

* (Multiplayer) Fixed body drop animation not playing for clients if body was dropped by another player

* (Multiplayer) Fixed sled sfx playing continuously after first use

* (Multiplayer) Optimized enemy material syncing

* (Multiplayer) Fixed 2 bodies briefly visible when picking up a body as client

* (Multiplayer) Optimized animator and memory usage on enemies as client

* (Multiplayer) Fixed cases of enemies popping/sliding around when knocked down and dying as client

* (Multiplayer) Improved gamepad UI navigation in game start scene

* (Multiplayer) Now saving player's skin & clothing variation

* (Multiplayer) Fixed trees vanishing for a frame when cut down by client

* (Multiplayer) Fixed an issue preventing clients to join games in some cases

* Removed broken rebreather from cave 2. Is now only findable in cave 5

* Overlay icons (i.e. shelter house icon) now check if they are above or below terrain and only show up when appropriate

* New item: Rabbit Fur Boots ! (craft with 3 rabbit skins and 2 ropes, wear on feet to gain some protection from cold and slightly increased stealth)

* New item: Quiver ! (craft with 3 rabbit skins and a rope, adds 20 to passive arrow carry capacity)

* New upgrade recipe: Arrows + 4 Twinberry = Poisoned arrows (can be batched) (Poison lasts longer but does smaller damage per tick than fire)

* Added upgrade recipes to all items with the burning weapon upgrade: Add booze (after cloth, as a second upgrade) to triple burn duration and slightly increase light intensity

* Increased range of mouse sensitivity slider in gameplay options

* Re-enabled depth of field in graphics options

* Fixed back of log cabin vanishing from outside

* Collision added to coral

* Fixed logs dropped in caves spawning above terrain

* Fixed bug with saved games stumps removal

* Fixed some misaligned elements visible when on floor during plane opening scene and removed soda spawned by player

* Improved lod on waterfall prefabs

* Fixed missing rusty axe mesh causing it to be invisible when equipped

* Fixed arrow going through terrain and objects

* Fixed an issue with auto cloud save

* Fixed sleeping not available out of the box in really old saves

* Fixed issues with fish sliding/blurring when speared

* Added leaf shelter destruction sound

* New building: Decorative wall plant pot ! Similar to garden but has 2 grow spots and only grows aloe or coneflower

* Rain no longer goes through player made structures !

* Revamped procedural wall door physics settings, doors are now easier to go through, always go back in position, and in the event of shady placement (i.e. with a floor going through the bottom log row) door should work anyways

* It is now possible to toggle and chose orientation of procedural wall door (same as window toggle)

* Ghost wall with door addition now displays ghost door (to show orientation)

* Procedural wall doors now have a one sided lock!

* Bush 08 mid version uses proper AO model

* Fixed camera glitch when standing up from explosion knockdown

* Trap page tab now comes up when setup defense task becomes available

* Clamped diagonal player movement speed slightly

* Fixed player weapons clipping through walls in many cases, weapon now moves away when in idle position

* Fixed Red Man on yacht not appearing from some angles

* Slightly increased raft movement speed

* Better transition into player drinking water animation

* Performing a flying axe attack now correctly drains stamina instead of restoring it

* World navmesh is now correctly updated when stumps are removed

* Closing walls with E now closes the same as clicking if current position can be locked

* Fixed all walls & fences placing with a slight offset from the placement preview

* Build defenses todo task is now triggered by first enemy hit rather than first enemy sighted

* Slightly increased max allowed slope for procedural stairs

* Now clamping size when making long procedural stairs instead of preventing to lock position (doesn't change the max size of stairs, but makes it a lot easier to place)

* Improved placing structures when there was already a ceiling above, making adding staircases to custom built multi-floor structures easier

* Fire warm whole home system ! Enclosed custom structures with a lit fire on the floor now provide warmth regardless of player distance with the fire (note: only working on custom structures so far, not yet on prefab structures (log cabin) Lowered position of ceiling skull lamp to better match model with in game positioning

* Fixed player feet sinking into sand/snow when above terrain level (i.e.: on buildings)

* Fixed enemies still being attracted to fires when fire shuts down by itself (not destroyed by player)

* Fixed bats moving backwards very quickly after being triggered

* Fixed Grass/Shadows/Low memory settings not saved/restored properly

* Fixed charged swing attack anim glitches, and sometimes registering multiple hits

* Fixed putting out lit fires not properly cleaning up heat status

* Better stick swing animation on player

* New story pickups added to Cave 6

* Fixed some gaps in collision around sinkhole where you could fall in and get stuck

* Fixed player getting stuck if taking damage while entering/exiting a cave

* Player is now woken up after 7 to 8 hours of sleep if starting to sleep at daytime (instead of being woken up by night falling), sleeping anytime at night still brings time all the way to morning as before)

* Player can now run for a second even if stamina is very low

# v0.31 (released January 21th, 2016)

* Player crawling animation added to opening scene

* (Multiplayer) New player clothing texture variations added! New revised camo, relaxed T-shirt and tourist clothing

* Improved map system: increased map granularity and added simple outside cave location map

* New todo task: Condition: have less than 40% air underwater, Completion: Find rebreather

* New todo task: Condition: Find climbable wall, Completion: Find climbing axe

* New todo tasks: explore caves 3, 4, 5, 6, 7, 8, 9 and 10

* Dynamic blood added to player body

* Fixed bug where rapidly opening and closing survival book could cause it to not appear in hands at all.

* Added support for PS4 DualShock controller

* New art added: Second frozen body

* New art added: Re-done player character textures

* (Performance) Amplify motion blur updated to latest release

* (Balance) Slightly reduced health on all creepy mutants

* New bird types added to world

* Cave 9 – adjusted layout and lighting

* New art added: improved crocodile textures

* (Rendering) Cheap far distance shadows added (experimental)

* Fixed grass rendering incorrectly on latest AMD crimson drivers

* Extra turbulence animation added to plane opening scene

* Removed floating stalactites from Cannibal Village cave entrance.

* Fixed burning weapons not emitting light

* (Multiplayer) Fixed timed bomb exploding when dropped from metal tray when full

* Fixed burning player not removing leaves of stealth armor

* Burnt trees now properly destroy attached structures as well

* Tree structures now collapse upon being destroyed

* Added 4 rabbit skins to bed ingredients

* Added colored flag to log sled to make it easier to locate

* Cliffs are now double sided and shadow correctly when sun is behind them

* Fixed rebreather not getting picked up when inventory already full of air canisters

* (Performance) Memory lowered by disabling read/write on meshes that don't need it

* Added ability to chop at leftover stumps to remove them

* Added stump removal to tree types that didn't have it yet

* Blowing up a partially cut down tree no longer removes the stumps (tree needs to first be fully cut down)

* Burnt Armsy texture seams painted out

* Improved arrow behavior with physics objects, it now properly collides with most objects it can be expected to even if it cannot stick in it

* Can no longer equip map while on rope

* Fixed wrong model bow and arrow on crafting mat and brightened bow textures

* Added some tents to cave 9 climb down entrances to make them easier to find

* Added stand up animation when first waking up on the plane

* Fixed breakable flare crate containing soda's instead of flares

* Updated enemy layout in cave 7 & 8

* Added climb out areas to cave 9 sinkhole overlook area

* Fixed pine trunk material not matching between cut and standing versions

* Added option to hide stealth meter

* Added option to turn other player names off in mp

* Added far shadow option to gfx menu

* Removed depth of field from gfx options

* Fixed sunshine occlusion not turning back on after being disabled and enabled again in options

* Rain should last way longer once it starts

* Burning body now yields 2 bones from torso

* Limited max amount of each berry type to 30

* (Multiplayer) Added sleep feature, all currently connected players must use a sleep trigger (regardless of place in world) and sleep will start once everyone is in

* (Multiplayer) Added “current view” icon display to Player List

* (Multiplayer) Added “Sleep” current view, active while waiting for rest of party to join

* You can now skin crocodiles and receive both skin and meat.

* Increased chance of seeing enemies praying at ritual altars

* Raccoons are now nocturnal

* Newly discovered map areas now smoothly reveal over 1s instead of instantaneously

* Fixed rain not cleaning up bloody weapons

* (Optimization) Plane and yacht shaders now use deferred rendering

* You can now cut downwards at stumps without clipping through

* Cave 1 – adjusted stalactites in flooded room, sinkhole walkout hallway walkout added

* (Multiplayer) Added backpack model to player

* Increased dynamic blood effect on enemies

* Inventory can no longer be opened while airborne

* Texture quality setting is now properly saved and restored

* Chocolate bars and soda now give overeating points when used

* Task system messages no longer spam hud

* (Multiplayer) Grabbing backpack no longer auto equips first item in list if hands are empty

* Fixed enemy bodies sometimes at wrong angle when dropped on fires

* (Multiplayer) Fixed enemies sometimes floating in air when killed in MP

* (Multiplayer) Fixed blood not appearing on client players when hit by an enemy

* Building collapsing now destroys triggers of nested buildings (blocks the feature before the end of the physics animation)

* New bone fence tribal look

* (Balance) Slightly lowered time to pull back axe before strike

* Fixed hanging bodies in main cannibal village not dropping items when hit, not counted on passenger list

* Plastic torch made brighter, longer bigger throw. Added brighter fill light

* Fixed various anim glitches when chopping downward with an axe

* Birds no longer land on bodies that have been dropped on a fire

* Fixed fish not receiving damage from regular weapons

* Smoother player rotation while pushing the log sled

* Added animals to parts of the map where there were few/none

* Blocked player rotation during stand up part of hanging cut scene

* There is now a delay at start of game before player can sleep (roughly at first night)

* Crafting anything now closes the crafting tutorial (was closed only by making molotov or closing inventory)

* Increased sled logs max amount to 11

* Stick, ropes and booze now use the multiview feature (can be used with amount > 1 in crafting)

* Walking in snow now sinks feet and slows down player

* New item: Snowshoes! (craft with 5 sticks and 2 ropes, prevents foot sinking and slow down while walking in snow)

* Glass shard upgrade views are now 50% smaller

* Made glass upgrade material more transparent and more reflective

* Flies are now attracted to dead cannibal bodies, once flies are there chopping off limbs may cause infection

* Experimental walls renamed ‘Custom Walls’ in Survival Book

* New image for Log Sled in Survival Book to make it clearer

* You can now cut holes in custom roofs! (using the same tool as floors)

* (Multiplayer) Fixed blood sync issues on dead enemies

* (Multiplayer) hopefully - Fixed enemies sometimes randomly running on spot

* Birds and squirrels now yield 1 meat

* AO fix for Bush 08

* Fixed camera being able to see down neck sometimes when using bow

* Stopped player getting leaves when cutting rope in hanging cutscene

* Added bones & skulls to custom effigy materials

* Now showing the “X climbing axe icon” when climbing axe isn't out while targeting a climb wall

* (Multiplayer) Improved time syncing for clients

* Fixed spawned crocodile head scale

* Dynamite must now be lit before thrown in order to explode

* Fixed player sometimes drifting slowly down if damaged while airborne

* Replaced hanging skull lamp model and replaced cloth requirement with rope

* Staying in a fire now properly keeps burning player until death or getting out

* (Multiplayer) Fixed burning trees

* (Multiplayer) Fixed issue when leaving game while having a backpack pickup in game preventing client from reconnecting if making a new game

* Fixed tangents and normal maps on tree bark

* Optimized touch bending on plants

* Optimized shadows casted by plants and trees

* Fixed material settings of waterfall

## v0.31b (released January 22th, 2016)

* (Multiplayer) Fixed bug with sled where additional logs past 8 would appear to hover in the air until log sled was released

* Dead birds no longer provide meat

# v0.30 (released December 22, 2015)

* (Multiplayer) New item: Metal Tin Tray! Store up to 6 different items in any amount in it using the crafting mat then equip it to share almost everything (Cloth, Skull, Flare and explosives are currently blacklisted)

* (Multiplayer) Improved performance for host when clients are far away

* (Multiplayer) Fixed cliff climbing not working properly when both host and client are holding climbing axe

* (Multiplayer) Revamped gather body workflow after dying. Dead body has been replaced by a backpack. Backpack now has all items you lost on it.

* (Multiplayer) Steal item trigger now requires player to hold the Take button for 0.5s

* (Multiplayer) Lowered kill delay of downed player from 3s to 0.5s

* (Multiplayer) Doubled bone pickup auto destruct delay

* (Multiplayer)Fixed enter cave animation not playing for other players

* Male and female bodies can now be burned by being dropped on a burning fire, after burning with provide 4 bones and 1 skull

* Lowered weapon fire light intensity

* New building: wall weapon rack decoration!

* New building: bone fence! Twice as strong as the stick fence

* New building: bone basket! Stores up to 86 bones

* New art added: Frozen body in snow

* Small camp with frozen body and orange tents added to snow area

* Fixed removing waterskin from crafting mat

* Improved look of subsurface on enemy creatures

* (Balance) Halved amount of meat turtles provide

* (Balance) Standing fires now drain faster/need to be re-lit more often

* Fixed missing collision on plastic panels inside shipping containers

* Passenger manifest is now retrievable from plane in save games if it was not retrieved previously

* Fixed missing home icon on leaf shelter

* Leaf shelter now collapses after sleeping in it, making it a one time use only

* Fixed an issue when having both a XInput gamepad and a Steam Controller connected

* Temp crow art replaced with new crow bird model

* (Audio) Redesigned pale mutant screams to stand out more

* (Audio) Removed some abruptly ending crow samples and added better fading to others

* (Audio) Added snow footsteps

* (Audio) Improved standing fire SFX

* (Audio) Fixed stalagmites sounding like wood when hit

* (Audio) Tent Flaps added

* (Audio) Idle breaths added to cowman

* (Audio) Added burn SFX to armsy and cowman

* (Audio) Added die SFX to cowman and babies

* (Audio) small tin trays now make sound when collided with

* Collision added to cave door pedestal

* Better vertex colours for plants, 10,11 and 13

* More turtles added to beaches and islands around the world

* Dynamic damage added to skin shader!

* Linked creepy mutants to new dynamic damage skin shader to give clearer idea how much damage they have taken

* (Balance) Balanced stealth so hiding is more effective

* (Balance) Lowered range that enemies can hear falling trees

* Vertex Painted Tents so they flap in the wind

* Switched laptop color to grey to make them easier to see

* Fixed missing underside of large cabin floor (visible when it was built high up on foundation)

* (Performance) LOD added for large log cabin,small hunting shelter and gazebo

* Fix for bush 08 exploding when cut

* Fixed plane crash going through water and terrain at some points

* Fixed chocolate bars not spawning properly from dead bodies

* Increased length of player stealth bar

* (balance) Updated enemy layout in cave 10 & cave 1

* Added mud back in game – spawns after rain on dirt terrain only – use mud to decrease your visibility to enemies, improve stealth

* Animals climbing on a tree will fall down now if the tree is cut down

* Trip wire traps are now fully removed when triggered in SP

* Passenger manifest and plane axe are no longer available in hull when already owned

* Bare maples added to snow area

* Snow area tree density balanced

* New snowy grass textures added for snow area

* Wind now grows stronger while up in mountains

* New textures for bush 08 and plant 17

* Brighter snow texture on snow trees

* Bare blueberry bush added to snow area, replacing regular blueberry bush in snow

* Player can no longer chop up bodies with blunt type weapons

* Fixed bug where player being hit by swinging rock trap whilst holding log sled could break game

* New yacht model with access to the inside

* Snow versions of Bush 02,03 08

* Increased fog visibility and exposure compensation while in snow area

* New billboards added for snow area

* Loading screen is now seamless between title screen and in game

* Fixed background mountain lods not matching

* Added condition to complete the explore cave 2 task from todo list (the task triggered after hanging scene)

* Player must now be almost fully submerged to get cleaned up/stop fire in water

* Balanced tree cut down counting in strength formula, it is now easier to gain strength while doing frequent exercising (good nutrition condition still applies) but exercising a lot one day then not doesn't increase strength for a long time

* Underfeeding is now based on time spent below 50% fullness

* If player has been underfed and eats he cannot get overeating points regardless of time with previous meal

* Clean up of some eye level stalactites in Cave 6

* Replaced old white tents with flap in wind versions

* Fixed an issue with stippling not resetting properly

* Fixed food sometimes ending up with “none” status

# v0.29 (released December 10, 2015)

* New survival book page: To Do list

* New survival book page: Stats page

* New “Sanity” system. Sanity goes down when killing an enemy, chopping limbs, a lot when eating an enemy and slowly while in caves. Sanity goes up when sleeping, listening to music, eating fresh non limb meat and slowly while restoring energy on bench. Viewable in stats page of book.

* (Multiplayer) Fixed drowning, player can no longer be revived after dying this way

* (Multiplayer) Fixed trees not always properly updated for clients

* Unlit molotov broken on the ground can now be set alight with another lit molotov for a greater fire effect

* Tennis balls can now trigger trip wire traps

* (Performance) Reduced rendering cost of leaf trap particles

* Fixed some instances of rocks floating and some cave models poking through into terrain

* Enemy held club and club crafted now both get bloody when used

* Fixed some structures not cutting grass when placed

* Reworked fern UVs and textures

* Fixed issues with player getting thrown upwards when jumping off raft into water

* (Balance) Reduced respawn rate of enemies in MP, overall increased randomness of enemy encounters

* (Balance) Made it easier to knock enemies to the ground when attacking with melee weapons

* Improved accuracy of enemy pathfinding, should result in less instances of getting stuck on structures/objects

* Fixed rock pit fire and stick marker ghost using wrong icon

* Crow bird type added to game (placeholder art)

* New art added: improved inventory tarp textures

* New art added: Reworked bird texture (bird land on finger)

* New art added: Revised shipping containers

* New art added: Reworked tortoise texture

* New art added: Far back snow terrain cliff type now has partial grass variation

* (Visuals) Improved moss shader

* New “Currently Feeling” system In stats pages, tells which survival stat is currently of greatest concern

* Birds can now land on and peck at dead bodies

* Pond seaweed is now cuttable and has touch bending

* Fixed enemies sometimes getting stuck on unwalkable terrain when spawned a long way from player

* Reworked Snowberry bush

* (Balance) Reduced health of skinny and pale skinny mutants

* (Balance) Meds added to Cave 2

* Removed the tutorial image that first comes up when book is first opened completely.

* Got rid of book auto opening to tutorial pages. Now shows extended tab and sheen when a page should be checked

* Combined Run & Underwater Breathing silent skills into ‘Athleticism’ stat which goes up from both swimming and running

* Added new “Strength” stat. Goes up every day while eating well and chopping trees. Goes down when over exerted and underfed

* Added “Weight” stat. Goes up and down based on food consumption

* Being overweight lowers Athleticism

* (Balance) Tripwire traps now use cloth instead of rope to make building them early on more viable

* (Balance) Large cloth jumpers in suitcase now give 2-3 pieces of cloth

* (Balance) Some laptops have a chance of being around crash site

* More bats added to caves

* Fixed missing wall in cave 3

* (Balance) Lowered log transportation energy cost

* (Balance) Lowered energy loss while hungry

* (Balance) Lowered both cold and not cold constant energy cost

* (Balance) Halved weapon attack energy cost

* Water areas added to cave map

* (Audio) Fixed SFX for felled trees breaking apart being inaudible to multiplayer clients

* (Multiplayer) Fixed skulls not spawning when cooking head for clients

* Added Food Poisoning: has 20% chance of kicking in when getting damage from food. Can be cured with aloe or by sleeping. Lowers fullness/thirst/health/energy regeneration from consuming edible items

* Added Blood Infection: has 25% chance to happen when receiving physical damage while bloody. Can be cured with aloe or goes away automatically after 2 in game days. Lowers

Strength

* After being out of fuel 2 times, fires are automatically destroyed

* Windows/doors of procedural walls can only be changed when hands are empty of logs

* It is no longer possible to drink from water collector when water isn't visible (amount < 1) and balanced amount of water available to compensate

* Fixed logs sometimes spawning bellow terrain (made some trees look like they didn't provide their full yield)

* Trip wire molotov trap now costs cloth & booze instead of molotov

* (Audio) Crow Sounds added

* Lit fires now have a chance to attract nearby enemies to come and investigate

* Nearby enemies are now attracted by the sound of falling trees

* (Audio) Fire crackle and pop added

* (Multiplayer) Fixed (hopefully for good) logs sometimes getting stuck mid air

* Added stippling to numerous props

* Player now has a chance to gain seeds when harvesting berries

* Maple bark made darker

* New slide into cave system added to cave entrances!

* Fixed some items in cockpit sunken below mesh

* Fixed extra decorative sticks appearing in sinkhole

* Fixed areas in caves where thin lines of light were coming in from above

* Fixed rock partially blocking cave 5 climb out entrance

* Fixed some issues with cave particles flickering off based on camera angle

* Fixed upgrading crafted club not working correctly

* Treesap balance: increased building repair cost and lowered gain from cutting trees down

* (Audio) Wet footsteps tuned

* (Audio) Plane start sequence improved

* (Multiplayer) Fixed fueling fire with leaves/cash not working for client

* Fixed bonfire destruction not working

* Fixed weapons not becoming bloody when hitting enemies (was only getting bloody when chopping up bodies)

* Fixed thrown spear not always killing deer

* (Multiplayer) Fixed fire arrows sometimes kicking clients

* Passenger manifest now auto closes after 3 seconds after it auto opened upon finding first passenger

* Fixed issue where noose trap could not be reset if sprung by player

## v0.29b (released December 10, 2015)

* Fixed some issues with some save games conflicting with latest todo list save system

* Fixed amount of skinny enemies in some games.

## v0.29c (released December 11, 2015)

* Fixed issue with some walls or fences appearing unfinished in older save games even if they were previously completed

* Fixed a bug with stealth icon not operating correctly in some old save games

* Fixed hand icon not showing in book when using a gamepad

# v0.28 (released November 24th, 2015)

* New item: Passenger Manifest! (find all fellow passenger bodies in world to cross their name's off the list)

* New building: Arrow basket! (stores up to 86 arrows)

* New building: Swinging rock trap

* New building: Molotov trip wire trap!

* New building: Leaf pile trap! (costs 50 leaves, once built can be set on fire for 20s

* to fry enemies) (Hint – works well combined with molotov trip wire trap)

* Lit molotov and arrows can now set leaf pile traps alight

* Lit molotov can now set all fire types alight

* Extended molotov fire duration by 2 seconds

* It is now possible to blow tree stumps up by sticking explosive on it !

* Fixed Cave Map not restoring map properly after loading a saved game

* Fixed case of sprint sometimes being unresponsive

* new mutant type added: dynamite mutant

* (Multiplayer) Fixed memory leak when cutting down/blowing up trees

* (Multiplayer) Fixed trees cut far from host or client pop on when approached

* (Multiplayer) The cave map and the passenger manifest are passed on to the respawned player when dying

* (Multiplayer) Improved cases of log staying stuck mid air

* (Multiplayer) Player list now displays properly for clients

* (Multiplayer) Fixed issue where meat from animals would duplicate

* (Multiplayer) Fixed issue where upgrades for weapons would not show up

* (Multiplayer) Fixed issue where raft would become unusable after if person driving it got damaged

* (Multiplayer) Fixed issue where mutant hanging in a noose-trap would vanish if trap was reset while mutant was still trapped

* (Multiplayer) Fixed some issues with receiving invites while in the MP screen

* Bushes & saplings are now properly pooled back when cut down

* (Audio) Improved animation related system memory usage

* Fixed finalized trophies not parenting properly with their supporting wall

* Cut down thin trees are no longer loaded in saved game as tiny floating pine tree stumps

* Reworded information on Garden in survival book

* (Audio) Last Armsy audio

* Increased skull lamp draw distance, and its light now fades in when enabled

* Fixed wrong settings on tree cut causing them to vanish on ultra low draw distance when exploded

* Art added: Camping Light

* More stalagmite/stalactite models can now be broken apart

* (Optimization) Improved performance of cave shadow blockers, and rendering on cave wood panels when not in cave

* (Audio) Cowman breaths events added

* (Audio) Fixed plane crash SFX playing again if you skipped the intro cutscene after the plane had already crashed

* (Performance) New lod added for firestand built and treehouse built

* (Audio) retimed plane crash sequence

* Improved look of molotov explosion and of timedbomb explosion

* AO added to dead trees

* (Audio) Added grunts for Cowman's Belly Flop Attack

* Fixed drawn bow being automatically reset after jumping

* Increased time for falling camera shake to kick in

* Player will no longer be woken by enemies if he is sleeping inside a base that completely blocks enemies from entering

* (Audio) Cowman dodge backwards sounds and recovery breaths

* (Audio) Fixed hitting foliage with club sometimes sounding like sword

* Thicker collider on tennis racket pickup so it falls over rocks better

* Fixed enemy bodies sometimes disappearing when killed at a distance

* New art added: Loose ground sticks

* (Art) Improved all terrain to ocean transitions

* Happy Birthday ghost model now matches built model

* Fixed player getting thrown up in air when standing very close to exploding structures

* New art added: Revised trunks, more detail, more variation

* World mutants no longer instantly despawn when entering a cave

* Cave 5 - improved lighting, removed old purses, many collision and wall fixes, fixed cross pick up fixed, cleaned up stalagmites and replaced with breakable versions. Stalagmites added to geeselake swimout. Cleaned up pick ups and props. Replaced unbreakable tables with proper versions. Made tighter light blocker to prevent light leaks. Removed rock dressing from ground that looked cluttered.

* Caves - upped collision detail on walls for cave 1,5 and 6

* Caves - yellow flare crate should be synced in MP in cave 10

* Caves - fixed missing wall in cave 6

* Caves - lighting fixes in cave 2

* Caves – replaced old lamps in cave 1 and improved cave 1 lighting

* Lowered speed and damage of crafted axe

* Fixed player head collider being disabled when in water

* Added “Map” action icon when holding map

* Cave map pickup no longer unequips after a few seconds when picked up

* Tennis racket is now stashed when pressing the “Drop” button while holding it

* Removed Armsy from bottom of cave 5

* (Audio) added flies sound

* Fixed burnt bodies all aligned same way

* Fixed blood effect repeating after killing fish and effect never being removed from world

* Fixed missing blood on Katanta and climbing axe, improved look of rusty axe blood. Fixed plane axe not bloody when first picked up.

* Moved second modern axe from dead tree to deeper inside cave 2. Moved katana from in front of cave 1 to deeper inside cave 1. Moved rusty axe from early in cave 5 to deeper inside cave 5

* Fixed missing “Lighter” action icon during cave hanging scene

* (Performance) Optimized memory usage of AI's path finding

* Flies added to burnt dead bodies

* Skull Ceiling Lamp drawing added to book

* (Audio) added on fire, hurt and death sounds for Armsy

* Fixed plant bomb on tree not showing when equipping bomb while in another trigger

* Fixed dropping animal heads, then picking it up again quickly causing it to vanish

## v0.28b (released November 25th, 2015)

* (multiplayer) Fixed bug where after dying in a loaded game and being revived you would be unable to interact with some world items

* Fixed plane missing collision in save games

## v0.28c (released November 25th, 2015)

* (balance) Fixed rate of dynamite cannibal type spawning.

* (balance) Lowered amount of ammo and frequency of dynamite man attacks

* Fixed cave map not loading correctly when save was done in the outside world

* Fixed passenger manifest not loading correctly with saves done in previous versions

## v0.28d (released November 29th, 2015)

* Disabled dynamite mutant spawning

* Lowered chance of fire mutant spawning

# v0.27 (released November 11th, 2015)

* New item: Cave map! Once found, visit cave system to reveal it. Replaces piece together map.

* New Weapon added : Tennis racket!

* It is now possible to harvest heads off the following animals: Boar, Crocodile, Deer, Goose, Lizard, Rabbit, Raccoon, Seagull, Shark, Squirrel, Tortoise.

* New building: Trophy Maker, once built you may bring to it an animal head to turn into a trophy !

* New building: rabbit skin rug!

* New building: ceiling skull light!

* (Multiplayer) hits from enemies on player are now calculated locally, reducing appearance of lag

* (Multiplayer) Reviving another player no longer uses meds and restores only a minimum amount of health

* (Multiplayer) Fixed issue of explosions not destroying trees when players were far away from host

* (Multiplayer) Fixed another log-dupe bug (sorry!)

* (Multiplayer) Fixed issue where some of the smaller tree types were not cuttable with explosives

* (Multiplayer) Fixed performance issues with lots of buildings

* (Multiplayer) Fixed an issue where (randomly) some wood planks being destroyed would not replicate out to other players

* (Multiplayer) Fixed issue where client could not kill fish with explosives

* (Multiplayer) Fixed suitcases sometimes jittering back and forth for client when stuck between objects

* (Multiplayer) enemy hit reactions are more varied and closer those in single player

* (Multiplayer) Optimized remote player animator cost

* (Multiplayer) Fixed exploding trees spawning 2 cut tree models

* (Balance) Slightly increased all axe damage

* (Balance) Deer can no longer be killed with 1 arrow

* (Balance) Slightly lowered attack range of plane axe

* (Balance) Lowered crafted club damage

* (Balance) Lowered attack range of mutants when attacking with only hands/claws

* (Balance) Run stamina Cost reduced by 15%

* (Balance) Hunger speed 30% lower (was about 2 full stomachs per in game day, now 1.35 per day)

* (Balance) Hitting an enemy with flying axe attack now does more damage based on height of the jump

* (Balance) Adrenaline rush ! When player's health reaches grey zone because of an enemy hit he gets half his missing stamina back over 1 second. Has a 2 minutes delay.

* (Balance) Player can climb up/down ropes faster now by holding “run”

* (Balance) Warm day no longer triggers in north (the system that makes cold go away when sun rises)

* (Balance) enemy hit that should cause death while player health is above grey zone instead brings player to 1 HP

* (A.I.) enemies can now see player from further away when not surrounded by trees

* (A.I.) prevented enemies targeting downed players in coop

* (A.I.) fire mutant is now immune to fire

* (A.I.) fixed praying behaviour from enemies almost never occurring

* (A.I.) fixed fire mutants almost never choosing to throw firebombs

* (A.I.) fixed Armsy occasionally spinning on the spot for no reason

* (A.I.) enemies will attempt to cut their friends down from rope traps

* (A.I.) Fixed some issues with enemy spawning over days. Should see more variety/amounts of mutants in general

* (A.I.) mutants will break off attacks from structure more often if player is nearby

* (A.I.) fire mutant is now faster and more aggressive

* (Rendering) New SH lighting added! More ambient break up/better looking less flat ambient fill light

* (Visuals) improved look of distant terrain – more break up, more bump

* (Visuals) Ocean white caps will now fade in as players moves closer to ocean instead of popping on

* (Visuals) Sun brightness is now dependent on cloud coverage, giving appearance of overcast days. Weather may now be cloudy without raining at all

* Procedural buildings can no longer be stacked with defensive walls as a support (was causing numerous issues)

* Increased speed terrain dries after raining by 2x

* Added 1 cloth to cost of stick marker

* Reorganized survival book pages and entries in each page

* Held walkman playing music will alert nearby enemies now

* Regular mutants should no longer follow player into water (much)

* Enemies can now jump over and interact with the rock holder

* Jumping onto small objects directly in front of player is now smoother/less glitchy

* Added camera shake when falling a long distance

* Sleeping bag models added to caves

* Hanging body models in caves moved down to stop wobbling

* Slight wobble added to yacht

* 4 types of large cave stalagmites can now be smashed apart

* (Performance) skull lamps particles and light get turned off at a distance from player

* (Performance) optimised cpu usage when building lots of rope traps

* (Performance) cut down trees now use pooled log pickups, limited to 100 instances (oldest ones get removed if new one are created past the limit)

* (Performance) tree wood hit particles are now using a pooled version

* (Performance) optimized cpu usage on log sled

* (Performance) Fixed some object not getting cleaned up when cutting trees

* (Performance) Lowered memory usage of freshly cut down trees remaining stumps

* (Art) New lighter model and textures added!

* (Art) New seaweed clumps added for beach!

* (Art) Added new grass types and visual improvements to foliage

* (Art) New prop added: R.O.V

* (Art) Snow-covered areas have new grass type and new grass placement

* (Art) North and south of the big lake, terrain polish and added grass

* (Art) new sleeping bags (and bloody alternate)

* (Art) Torn version of blue tent added (can't be slept in or used to save game)

* (Audio) Fixed audio bug with windows 10 and some drivers which could cause a weird static sound

* (Audio) added Armsy running breaths and tuned the trees falling sound a little more

* (Audio) Made rain start loud, and then loop a little louder than it used to

* (Audio) Tuned mutant distant cries

* (Audio) Added Armsy Tree Knockdown sound

* (Audio) tuned tree falling and tree hitting ground sounds

* (Audio) Added new Armsy yells

* (Audio) New Snow footsteps added (not yet implemented)

* (Audio) Mixing on: small bird on hand, distant surf, leaves falling, leaf rustles, laptop dragging, hammering, footstep rock, footstep grass, footstep mud, footstep jump

* (Audio) Fixed deadfall trap not playing sound event issue

* (Audio) Fixed footsteps sometimes getting stuck as wood, regardless of what surface the player is walking on

* (Audio) Deadfall Trap Sound Redesigned and added to game

* (Audio) Happy birthday trap sound event timing adjusted

* (Audio) cleaned up mixer objects so audio events don't play when game is paused

* (Audio) Added glass smash for unlit molotovs

* (Audio) improved small birds flying sound

* (Audio) Chopping trees don't duck wind so much

* (Audio) Removed a waterfall audio emitter that was incorrectly placed

* (Audio) Tuned dying sound so first ragged breaths, then heartbeat, then blood in ears. World sounds get affected a little earlier also

* (Audio) Fixed tree bridges triggering incorrect player footstep sound

* Fixed sleep timer broken when having nearby enemies

* Fixed wrong item equipping after having cancelled placing a blueprint by opening book

* Fixed exploded enemy pickup objects icons showing the “Inventory” action key

* Fixed garden blueberry respawn bug

* Fixed dropped katana turning into dynamite

* Fixed issue with custom effigy automatically lighting up

* Fixed dead text having gradient inside it

* Fixed missing sticks on sled ghost model (cost is 21 sticks now)

* Fixed missing 7 leaves cost on rockpit and standing fires

* Fixed tree platform missing 1 rope cost

* Fixed thrown dynamite having sheen effect on material

* Fixed missing collision on drying racks, rock holder, cannibal village old fires, pig head sticks, and hollow logs

* Fixed firestick missing from fire mutant in MP

* Fixed placed distraction device not waking sleeping enemies

* Fixed an edge case issue with cold system causing after being warmed by the sun to never get cold until going nearby a fire

* Fixed hud disappearing when attempting to open book while pushing sled (It is no longer possible to open book while pushing sled)

* Fixed player losing stamina if stationary while holding the run key

* Fixed spears not doing any damage when thrown or aimed downwards

* Fixed spears not sticking into half cut trees

* Lowered health of crocodiles

* Player can no longer perform heavy swing attack if stamina is very low

* (Rendering) Deferred skin shader improved: Subsurface scattering will only be applied on lights casting real time shadows

* (Visuals) Large scale ambient occlusion added to trees and plants

* (Art) Improved the look of snowy area and backdrop cliff transition

* New input action: “Map” Set to M on keyboard and Left shoulder 1 on gamepad (check your settings if you have done custom mappings it won't overwrite it)

* Fixed camera seeing down neck sometimes during plane crash

# v0.26 (released October 23rd, 2015)

* (multiplayer) Fixed combat for clients being easier than in single player games due to enemies not using counterattacks as frequently

* (multiplayer/Balance) Tweaked enemy frequency to work better with multiple players compared to single player

* (multiplayer) All droppable items now sync between players

* (multiplayer) All projectiles are now replicated over the network

* (multiplayer) Fixed swimming sounds of other players being really loud

* (multiplayer) Fixed a bug that was causing mutants killed by happybirthday trap to not fall down for clients when trap was reset

* (multiplayer) Fixed some instances of enemies duplicating when killed

* (multiplayer) Fixed some instances of enemies having wrong material on death, i.e. not burnt material if killed with fire

* (multiplayer) Fixed plane not aligned for clients if host plays crash sequence all the way through

* (multiplayer) Fixed issue with incorrect material on creepy mutant ragdolls

* (multiplayer) Bloody tables are now synced between players

* (multiplayer) Raft now synced between players!

* (multiplayer) Fixed bug where items would remain on pedestal (metal doors) after being placed and taken again

* (multiplayer) Fixed bug where if one player was holding full map, other players would only see them holding a partial map piece

* (multiplayer) Fixed some issues with cooking food for clients

* (multiplayer) Fixed repairing log cabin walls when whole chunk is broken

* (multiplayer) Fixed a case of save failing for clients

* (multiplayer/performance) Reduced cost of processing nearby tree detection for host

* (multiplayer/performance) Optimized animator usage of all creatures in MP

* Fixed bug where hanging scene could break if player had torch equipped instead of lighter

* (performance) Removed some extra unneeded mesh colliders on distant objects

* (performance) Decreased math instructions in ocean shader by 30%

* (performance) New fully deferred version of skin shader

* (performance) New Ocean Quality: Wave Displacement Low (previously existing option is now called Wave Displacement High) – note it doesn't change wave height, just how good it looks and how much strain it has on the hardware

* (performance) Now forcing flat ocean on 32 bits systems

* (performance) Greatly lowered per frame memory usage of ocean waves

* (performance) Tuned down bloom on 32 bits systems to limit memory usage

* (performance) Combined ocean/lake depth passes to save memory

* (performance) Optimized sheen billboard icons distance detection

* (performance) Optimized grass displacement system to use terrain height instead of a raycast to find terrain height

* (Visuals) New art added: Stonewall built models (replaces rock pickup mesh in built walls)

* (Visuals) New plant vface shader added! More accurate lighting on single sided plants. Included new vface billboards which contain sss

* (Visuals) Tiered waterfalls now have working water connecting them down to the sea.

* (Visuals) Cleaned up trees/small plants intersecting sinkhole

* (audio) New flesh, object smash, tree hit and plane impact sounds for mutant limbs

* (audio) Improved armsy arm sounds

* (audio) Added some distant Armsy sounds

* (audio) Improved mutant baby sounds

* (audio) Added more cowman sounds

* (audio) Added garden digging sound

* (audio) Hitting plane with weapons now plays sound

* (audio) sound event now plays when player is attacked by a shark

* (balance) Lowered molotov fire spread duration

* (balance) Halved chances of raining

* (balance) Slightly lowered amount of active animals in the world

* (balance) Pale mutants are now more aggressive when outside of caves

* New winter top heavy tree added!

* New item type: Yellow cave crate containing flares

* New decorative magazine added

* New burn animations added to creepy mutants

* New look at story item animation added

* New add seeds icon for garden

* New change color icon for stick marker

* Small wooden cages are now destructible!

* Fixed plant type that was uncuttable/distorted when hit

* Fixed treehouse ghost meshes containing old stairs mesh instead of rope mesh

* Fixed player getting infinite leaves when hitting explosive caches and improved shading on rock over explosive cache

* Fixed some breakable wood planks in caves not being breakable

* Fixed garden plants popping on too close even on high draw distance settings

* Fixed rope mesh vanishing whilst climbing if player was on low draw distance setting

* Fixed enemies sometimes clipping through walls when jumping over rocks and other objects

* Fixed bug where dragged mutant would not transition to death if killed

* Fixed visible section where terrain ended under ocean and would be darker than other water

* Fixed small (tiny)pine tree having blue outline in far distance

* Fixed dead wood especially on beach all rotated exactly the same angle

* Fixed some props looking too shiny/broken. Hanging body parts, legs, some enemy built art.

* Fixed some trees wind settings not matching for trunks causing leaves to visually break away from trunk at some distances

* Fixed bug where player was able to hit tree's/enemies that were behind him

* Fixed anchorable rope/tree houses/tree platform climb rope icon overlapping with rope model

* Fixed ghost traps placing floating above ground (not retro-active)

* Fixed fish vanishing while running with them on the spear

* Fixed fish sometimes appearing in the air around player

* Fixed cooking on raft causing it to go haywire

* Fixed raft sometimes being unusable after loading a saved game

* Fixed issue with raft's buoyancy when built bellow water or after severe wobbling

* Fixed scale on snow ground sparkles

* Fixed fog height being too low in some snowy areas

* Fixed player sometimes falling down when exiting at top of ropes

* Fixed some navmesh issues when placing happy birthday traps

* Fixed an edge case of rebreather light not turning on underwater

* Fixed armsy being able to fall into water at the bottom of cave 5

* Fixed missing dead tennis team in cannibal village

* Fixed plane axe not getting bloody

* Fixed a bunch of misaligned rocks, flying rocks, gaps between terrain and cliffs and other world errors

* Fixed camera sometimes offset on plane when starting a new game from within a previous game

* Fixed several issues with the rope trap in SP

* Fixed mutants being able to follow player into water in cave 8

* Fixed a case of molotov getting stuck unlightable after a failed lighting attempt

* Fixed medium preset using SMAA by default

* Fixed an issue where lower half of screen could be black after after loading a game in caves

* Garden revamp: Seeds are now added one by one and spawn little dirt piles in the garden. Plants grow visually over time and provide from 1 to 3 of their respective yield based on growth time. Plants die after 1 to 2 days (depending on plant) at max yield. Plants growth timer now properly saves as well as account for slept time.

* Terrain and detail improvements for section above big lake

* Removed ferns and marigold flowers from snow areas

* Added new snow-covered rock, snow covered hollow log, snow covered dead wood

* White rabbits will spawn in snowy parts of the map

* New enemy behaviour: Fire mutants can now throw firebombs at the player

* Tree houses & platform now automatically position their rope above ground like anchorable rope does

* Stick marker now also tints the top cloth piece the color of the flag you set

* Hitting escape while in options in game now saves it

* New sinkhole interior art added – along with enemies – sinkhole can now be accessed via lowest cave

* New blend materials shader (used currently in sinkhole)

* Improved look of cave 1 entrance, better rock materials and fixed running water settings on cave wall molted type

* Resetting traps now require to hold the “Take” button for half a second

* You can now save/Sleep at the tents in world and in caves!

* Cave props – blue buckets and cut old arms are now dynamic and pushable

* Burnt arms/legs in overworld are now dynamic objects

* Orange snow covered tents added to snow section

* Updated enemy layout in Cave 7 & 8

* Cave 8 moved walls near entrance to clear walking ledge

* Cave 8 fixed air pocket in corridor water

* Cave 8 re-exported walls to fix issue with climbing down ropes through rocks

* Cave 8 weights moved down to more easily see what you are placing in them

* Cave 5 added mineral walls to swim up room and added new props

* Cave 2 removed extra cave corpse in dead room

* Cave 2 walls rexported with improved collision

* Cave 2 hole in corridor plugged up

* Cave 10 extra props added

* Removed shiny cave debris

* Less body part debris in caves

* Rope layer changed so you can see it from further away in caves

* Improved enemy nav mesh should result in less instances of mutants getting stuck

* Improved collision on some cliff pieces to stop player poking head through

* Improved draw distance on outdoor old white tents

* Improved draw distance on thrown explosives and on built garden plants

* Improved look for light molotov and light arrow animation

* Improved look of molotov burning cloth – now correctly uses 2 sided material

* Improved garden dirt material/texture

* Improved draw distance on lake lily pads

* Improved ambient reflections on objects

* Improved timmy model/textures during plane crash

* Improved ocean foam lighting at night with torch out

* Improved look of cave water and fixed sharp edge/white outline around cave water

* Improved accuracy of bonfire collision and its fire damage range

* Improved accuracy of plane collision, can no longer crouch/glitch out of plane side doors

* Improved accuracy of bridge collision shape

* Removed some old purses and suitcases from overworld

* Made it easier to light campfires with lighter (lighter does not have to be exactly over the fire any more)

* Raft's driver now automatically unlocks when raft gets out of water

* Added a safety net to bridge saving, to allow recovering it if anchor data gets lost. This isn't retro active, broken bridges are gone but all the new ones as well as working ones from saves will make use of the system after saving

* Food cooking on a fire is now easier to target

* Crafting mat feather/tooth/tree sap piles are now a bit smaller and teeth are more centered to prevent it from being inaccessible under bottles

* Weapon rack, explosive holder and metal door now bring up same item if available after putting down one

## v0.26b (released October 26th, 2015)

* Fixed invisible buttons in MP player list stopping hosts from being able to kick/ban players

* Each ghost rock fence visible model now costs 1 rock and no longer fills the whole chunk at once

* Fixed all ghost walls and fences first locked point position being offset from placing model

* Fixed following area not available message not showing up in sinkhole

* (multiplayer) Fixed loading save file with custom rope sometimes breaking loading

* (multiplayer) Fixed loading save file with fires erroring

* Fixed energy mix staying on crafting mat when closing inventory without removing it first

* Empty save slot can no longer be clicked to load from

## v0.26c (released October 26th, 2015)

* Fixed issue with saving a game if no previous save game existed

* Fixed ghost building rotation speed really high when using a gamepad

## v0.26d (released October 27th, 2015)

* (multiplayer – balance) In general you will now see smaller groups of enemies early on, with size of groups increasing overtime

* (multiplayer) Lowered chance of enemies finding players straight after plane crash

* (multiplayer) Fixed some bugs with enemy spawn amounts, all types of mutants should appear after enough time has passed

* (multiplayer) Fixed player\_net faces looking too shiny and some arms not matching look of face

* (balance) Slightly lowered how much damage enemies do to player

* (balance) Old food that's still edible now gives some health instead of none (previously only fresh food gave any health)

* Increased custom effigy base range and per limb and torso bonus range

* Fixed some glitches in enemy effigy effect reactions

* Slightly higher damage from fire to all mutants

* Fixed player sometimes losing armor even when blocking

* Reduced overall block damage amount slightly

* Fixed a case of save with bridge not loading

* Fixed some bark having incorrectly scaled textures/and overly broken moss look

* Fixed large missing piece in cave1

* Fixed case of partially built treehouses causing issue on loaded games/inability to add items to them or complete them due to them using the old stairs ghost model

# v0.25 (released October 7th, 2015)

* New building: Custom Effigy – replaces ‘Simple Effigy’ in book (once built, use sticks to add to base shape and/or limbs and torsos to create effigies of your own ! Range and duration of the repulsive effect when lit depends on amount of added limbs)

* New Ocean shader! Now has 3d waves and foam! – note – low, ultra low and fastest quality settings default to old ocean. This can be changed in quality settings

* Player will now find themselves hung upside down when waking up in cave and will need to cut themselves free

* New rain shader! \*again – this time runs faster and looks better

* Improved terrain water accumulation

* (multiplayer) Animations now blend more smoothly for client players when attacking enemies.

* (multiplayer) Fixed animation issues for client when mutants would die

* (multiplayer) Fixed bug where cave enemies would sometimes ignore clients if client was far enough away from host player

* (multiplayer) Lowered network interpolation delay for clients to improve responsiveness over network

* (multiplayer) Metal doors are now correctly synced between players!

* (multiplayer) Fixed head bombs not synced between players

* (multiplayer) Fixed issue with grabbing items nearby a sled after looking at the sled picking up whatever is inside

* (multiplayer) Breakable crates in overworld are now synced between players

* (multiplayer) Improved suitcase syncing between players

* (multiplayer) Fires don't give light for players that aren't around when first lit

* (multiplayer) Fixed issue with scale of fire after loading a saved game in multiplayer

* (multiplayer) Fixed some smaller issues with log/rock sled in multiplayer

* (multiplayer) Fixed an issue that would occasionally stop players from connecting to a multiplayer game after already having joined one

* (multiplayer) Fixed issue with effigies not always lighting up for clients or being lightable for clients

* (multiplayer) Fixed animation issue that would happen when you were looking at another player dropping a corpse on the ground

* (multiplayer) Fixed issue where suitcase “lock” icon would always be visible even after suitcase had been opened

* (multiplayer) Fixed Defensive Wall Reinforcement sometimes doubling up

* (multiplayer) Fixed cutting tree sometimes not finalizing properly leaving a floating cut tree

* Fixed bug where fire would sometimes be really big when first lit under some conditions

* (audio) Axe, club and rock weapons now make impact sounds when hitting plane hull

* (audio) Ambient sounds no longer briefly heard before plane crash starts

* (audio) Echo added to sinkhole!

* (audio) Increased footstep volume when running

* (audio) Revised scream sounds to sync better with animations

* (audio) Fixed inaudible drop sound on pre-placed dead mutant bodies. Fixed bat exit cave sound inaudible.

* (audio) Fixed thunder playing effect twice when rain starts

* (audio) Added water drips to rivers during rain

* (audio) Added less full-on inhales for when coming up from underwater

* (audio) Randomised offset to fire start time to stop audio distortion when building lots of fires close to each other

* (audio) Sigh relief sound effect is now played when the player extinguishes being on fire by entering a water volume

* (audio) Weapon clean sound now plays when entering water with a bloody weapon.

* (audio) Suitcases, laptops, small pots, food carts and plane seats all have sounds now when pushed

* (audio) Fixed suitcase smash sound sometimes playing twice when hit and distorting audio  
  (audio) Tuned cliff, item push, and some player sounds

* New art added: Blue tent (replaced placeholder blue tents)

* Terrain shader improvements, faster rendering, better performance when raining and more tweaks

* (balance) Increased lung breathing duration to 25s

* (balance) Rebalanced all weapon speed/damage/block strength

* (balance) Slightly lowered energy drain from swinging an axe

* (balance) Stopped bombs and dynamite sliding as much after being thrown

* (balance) Blocking with weapons no longer drains stamina

* (balance) Bow max charge duration set to 2s (was 5s before) Now, release when visually the bow looks ready and you will fire a straight shot

* (balance) Lowered speed of shell attack

* (performance) New Mid level trees added

* (performance) Mutants now have skinned lod meshes

* (performance) Optimized animator on distant/not visible enemies and bodies

* (performance) Lowered memory usage in render textures by about 200megs

* (performance) Lakes and ponds are now fully disabled when far enough away

* Fixed blood visible on screen during drag away cutscene

* (UI) Added weapon block strength display to inventory item tooltip

* Amount and type of enemies in the world will change over time depending on how many are killed

* More trees now respond to wind!

* Trees when cut no longer switch shaders -improving jump between cut and not cut meshes\*still some improvements needed to make this totally seamless

* Lighting weapons and projectiles now requires to hold the “Lighter” button for half a second

* Fixed suitcases around plane respawning at runtime when going back and forth to the plane

* Fixed enemy placed art often being half underground, having wrong rock texture, or having items not pickupable when destroyed

* Fixed strange shading on fire built model due to wrong occlusion map

* (visuals) Improved look of lakes/ponds. Fixed mip mapping issues causing pixel distortion in distance. Better bump and fog settings. Brightened streams and improved bump/blend and reflections.

* New enemy behaviour – mutants can sometimes be seen feeding on body parts in caves!

* Fixed missing seaweed prefabs under water

* Fixed weapon fire light having a really big range and lighting up entirety of caves!

* Lowered brightness of player\_net lighter

* Blood particle effect made less shiny/metallic

* Brightened colors on edible and spoilt fish, generic meat, rabbit, lizard materials to make difference between states clearer

* Upped max arrow amount in inventory from 12 to 30

* Multiple arrows can now be upgraded at once with a single bottle of booze

* Fire arrows now look red in inventory

* Fixed laptops being too dark and some still having old model linked in

* Lowered chance of birds clumping onto perch targets on built items

* Updated enemy cave layout in some caves

* Improved some areas of cave collision to stop feet poking through

* Fixed fullness not getting consumed while sleeping (so it behaves like thirst)

* While sleeping both fullness and thirst can only be consumed up to a threshold, so that you never wake up on the verge of dying (unless you engaged sleeping in this state)

* Sleeping is now limited to once per day (unless woken by enemies in which case it doesn't count towards this limit)

* Shelter now shows remaining time until next sleep instead of action icon while the feature is locked (display is relative to 1 in game day, i.e. if the bar is 50% filled it means half a day remains before sleeping again)

* Effigies now require to hold the “Take” button for 0.5s to set alight

* Added lighter action icons to all effigies

* Added more fire particles to molotov to make it look spread out more

* Molotovs can now be used to fuel fires

* Molotov no longer leave fire floating in the air when colliding mid air with something

* Fixed Destroyed Tied Tongue effigy parts not being pickupable

* Fixed birds perching on other birds

* Fixed bug where bodies could not be placed in Log Sled when carrying rocks.

* Fixed bug with terrain sand making it look 8-bit around beach area. Balanced look of sand.

* Improved cave reflection cube map for underground lakes

* Sun is now correctly blocked by thick clouds in sky

* Added blend option for clouds and new overcast texture to simulate clouds/storms forming before rain

* New base cloud texture!

* New rope material/textures

* New cave art added: Stalagmites and stalactite types

* Fixed bug where you could open survival book whilst climbing rope

* Fixed some issues with matching props/textures when switching to dummy on death

* Fixed 3 sappling types missing texture on thin trunks

* New gameplay option: “Advanced controller support (XInput)” (required to use the game with a Steam Controller, it is off by default so check out options if you need it)

* New gameplay option: “Show projectile reticle”

* New graphics option: Ocean Quality [Wave Displacement / Flat] Low, Fastest and Ultra Low quality presets use Flat ocean quality by default.

* New texture added for cannibal carry away timmy

* New art added – replacement rocky/dirt ground texture

* It is no longer possible to drink (from ponds/Lakes) while moving

* Ensured better randomness of plane crash site roll

* Cave 1 – fixed seam in floor, fixed distortion in parts of floor. Raised rocks in flooded room. lighting improvements, more walls replaced with mineral wall type

* Graded ground textures to match values in trunks closer

* Less electric green in tree moss

* New fish models and types added!

* Fish are now killable with regular weapons and explosives (hitting them with axe is pretty fun but probably way overpowered currently)

* Fixed spamming the “Lighter” action with a fire arrow equipped creating several fires over time (could eventually cause fire to stay on forever and enemies to get caught on fire when poked with the fire arrow)

* Lighting arrows now requires to hold the “Lighter” button for half a second

* It no longer possible to shoot arrows while lighting it on fire

* Arrow fire now properly shuts down after a few seconds

* Arrow fire now properly burns close by objects

* Lowered big effigy burn duration to 20 minutes (was 40)

* Worked around an issue with some keyboards shooting keydown message repeatedly when holding down a key, preventing from using held input actions

* Player no longer gets cold immediately when entering water at night or in caves, instead there is a chance it happens over time when water level is above ankles

* Player can look down more while climbing cliffs

* Fixed player movement breaking when sitting on a bench and alt attacking with a spear

* Fixed player crouching glitching out whilst holding lit arrows

* Fixed raft row material glowing

* Fixed grabbing rocks from sled while carrying a body bug

* Improved look of dirty pot water and improved look of steam particle when boiled

* Fixed issue causing water pot to have a wrong texture when boiling dirty water on fire

* Increased player swim upwards speed

* Balanced blood amount on screen when suffering damage

* Food cooking on a fire gets destroyed when the fire does, except water pot which you can pick up empty afterwards

* Fixed bug where camera could be sometimes slightly offset after plane crash

* Removed pre-placed dead cannibals in world

* Raft is slightly faster now

## v0.25b (released October 8th, 2015)

* Changed how new ocean behaves at start of game. New ocean will no longer be active at start if ocean is set to ‘Flat’ from title options screen. If playing on an integrated graphics card or having any crashes when starting the game, set ocean quality to ‘Flat’ in options menu. (temporary solution until we find a better fix)

* Possible fix for some players having invisible ponds/lakes

* Fixed issue with scale/blend weight of dead enemies sometimes not applying on client

* Fixed issue with props on mutants sometimes popping in after death for client

* Fixed intermittent issue that could be preventing saving in SP

* Fixed issue with new ocean crashing on some model cards (older ati cards, some integrated laptop cards), let us know if this still happens for anyone

* Fixed sharks missing from ocean!

# v0.24 (released September 17, 2015)

* New input action: Multiplayer > PlayerList (set to Tab by default, not added automatically if custom bindings exists)

* (multiplayer) Fixed host not counting itself in lobby member count displayed in game browser

* (multiplayer) Player list (has ban/kick features)

* (multiplayer) Banned players list (has cancel ban feature)

* (multiplayer) Title scene displays a message when sent back there after being kicked or banned or attempting to join a banned game

* (multiplayer) Fixed weapon damage inconsistency between single player and multiplayer – i.e. modern axe now takes less chops to chop down a tree in multiplayer

* (multiplayer) Fixed bug where enemies would play standing up animation often right after being killed

* (multiplayer) Fixed client unable to finish defensive wall reinforcement

* (multiplayer) Moved back button down to avoid blocking hosting game by Steam for several hours when clicking too fast on create lobby button at some resolutions

* (multiplayer) Fixed mutant babies disappearing for clients when they die

* Inventory camera now moves back to fit whole carpet in view at all aspect ratios

* (performance) Texture resolution options added to options menu!

* Rabbits that are lit on fire turn into edible cooked rabbits when they die

* Fixed gamepad navigation in menus

* Fixed ghost rock fence not saving properly (might require to recreate the ghosts to have the proper shape)

* Fixed distance from water at which fires must be built to be lightable

* (Audio) Added break SFX for wooden objects, cardboard boxes, laptops and effigies

* (Audio) Updated drinking sound for drinking from water sources such as ponds and water collectors, sound now timed to pond drinking animation.

* (Audio) Added bone rattle and cracking atmosphere sounds that react to wind to each of the cannibal art structures.

* (Audio) Added new bone sounds to mutant leader movement, hit reaction and attack animations.

* (Audio) Added SFX for weapons hitting ground, water, rocks and other inanimate objects

* (Audio) Added slide SFX for wooden crates, small cages, tables, rocks, laptops and cardboard boxes

* (Audio) Added moaning wind ambient SFX to cave entrances and built structures

* (Audio) Added burn SFX for female creepy mutants

* (Audio) Rain SFX now responds to wind intensity

* (Audio) Added cracking wood sound to fishing stands, sound responds to wind intensity.

* (Audio) Added creaking ambient sound to Tree House and Tree Platform structures, sound responds to wind intensity.

* (Audio) Fixed female creepy mutant SFX getting left behind as she moves

* (Audio) Seagulls make individual sounds

* (Audio) Large structures now moan in high wind

* (Audio) underwater, swimming sounds, and jumping into water splash made louder

* (Audio) Fixed pale mutants sound being muffled

* (Audio) Log Cart sound intensity lowered

* (Audio) Fixed missing katana air Whoosh sound

* (Audio) New hacking up mutant body sounds and new hitting/killing animal sounds.

* Reduced maximum amount of feathers you can get from hitting dead birds with rocks

* Player can now put out lit fires by hitting them

* Axe should line up to cut point better when chopping trees

* Fixed various animation glitches when transitioning between axe animations

* Fixed enemies not jumping over stick & rock fences

* Fixed dropped upgraded spear turning into dynamite pickup

* Fixed houseboat not floating correctly

* Book open animation added!

* New art – Enemy club remodeled/retextured

* New art – new model for regular crafted club – also now easier to select in inventory

* Fixed some breakable wood planks giving leaves and playing plant hit sound effect

* Fixed dead screen showing action icons

* Fixed big buildings (like the houseboat) flashing out when looking down while placing on slopes

* Molotov tutorial now only shows when a molotov is up, and is deemed done when a molotov has been lit

* Blood now accumulates on screen for longer whilst getting hurt and stays even longer while in grey zone

* Fixed bug with ghost skull decoration when loading a saved game

* Fixed place bomb feature showing place talky icon

* Fixed action icons disappearing when alt tabbing back in game

* Fixed rare case of UI looking doubled

* Lowered swing speed of craft club and held enemy club

* (performance) New lods added for cliff rocks, cliffs, lake rocks

* Fixed suitcases sometimes showing as open but having a locked icon above them.

* New cave tileable wall textures added

* New cave ceiling textures added

* Fixed mutant baby spawning 2 ragdolls when killed with fire

* Fixed some survival settings (starvation/thirst/cold) broken after loading a saved game, causing for example breathing duration to be really small

* Fixed some pathfinding issues with defensive walls

* Fixed action icons of inventory item tooltip breaking their scale and position when switching from mouse to gamepad while it is visible

* Faster transitions into and out of axe attacks

* Thrown molotovs will wake nearby sleeping enemies

* Screaming enemies will attract/wake up nearby enemies

* New player/timmy animations added to opening plane crash

* Hitting hanging bodies now has a chance to spawn cash

* Improved foundation system to better work with explosive destruction and improve destruction performance

* Fixed an occasional bug when using pouch to collect berries causing all icons to stay visible on bushes in range

* Fixed issues with save files date not displaying sometimes

* Fixed several file dates issues, including dates of cloud files (should now properly sync only once)

* Fixed listening to walkman music not regenerating energy (works once per in game day) + the return of the flashing outline !

* Arrows now go through cave doors and can stick to terrain behind !

* Fixed slight fired arrow positioning issue

* Tweaked arrow physics settings so that it falls down more at it flies in distance. With those settings, a fully charged arrow shoot (5s bending) is very accurate while a mid charged one cannot go far in distance and can only be used for close up combat

* Fixed enemies sometimes facing wrong direction when hit with arrows

* Fixed enemies sometimes glitching through walls during combat

* Fixed skinny mutants appearing to damage defensive walls

* Thrown flares should emit more light and be more useful for finding way in dark

* Fixed burnt baby texture looking shiny

* Building distortion now scales with damage proportional to max HP (from 1x to 10x)

* Building distortion now only effective past 0 damage

* Fixed upgrades not spawning renderers when reaching max amount

* Removed upgrade counters in inventory item tooltip

* Now displaying weapon speed & damage values (upgrade bonus included) in inventory item tooltip

* Now displaying preview for weapon speed & damage upgrade bonus when adding ingredients on the crafting mat !

* Improved inventory item tooltip positioning so that it cannot go below bottom of screen

* Lowered penalty of each upgrade type

* Arrows now limited to 12 in inventory

* New upgrade recipe: Fire arrow (1 arrow + 1 booze)

* New upgrade recipe: Bow set ammo (1 bow + 1 arrow, none consumed, sets which arrows are used first by the bow)

* Picking up an item while underwater and dropping it underwater no longer equips previously equipped weapon

* Fixed lighter tut coming up in caves while underwater

* Improved molotov fire particle quality

* Fixed issue causing rocks to stop spawning after collecting a large amount

* Fixed issue where some hidden caches of dynamite were not pickup able

* You can now place rocks in log sled! and switched log sled add to a generic icon

* New close range attack animations added to cowman

* Fixed some swimzones in cave 6 and in other areas around world that shouldn't have been there

* Fixed issues with jumping into water while holding story clues. Also prevented dropping those items

* (performance) Lowered cost of rain particles to render and killed them faster instead of rendering them far under terrain

* Deer run away from player more consistently, and run faster

* Updated cave 8 enemy layout

* Two new story clue pickups added

* Terrain – fixing some areas with holes, fixing some cliffs misaligned. Improving look of area around big lake.

* New terrain shader, renders faster, looks better. Includes improved snow, wetness near water and more

* Improved cave water shader – now easier to see, better reflection and better clearer refractions

## v0.24b (released September 18, 2015)

* Fixed bug where logs could not be added to sled unless you were also carrying a rock along with some other issues related to this and also issues related to sled and saving/loading

* (multiplayer) Fixed issue with lighter behaving strangely if other players had molotovs out

* Fixed new laptop art missing rigidbody and not able to be pushed around

* (multiplayer) Fixed dropped decaying meat missing reference on rabbit

* Fixed small bug with deer decoration rendering on top of inventory

* Fixed arrow getting consumed on crafting mat when used with bow to set ammo type (it now properly goes back in the arrow stack)

* Fixed issue with lighting arrows when having more than 12 arrows in a saved game

# v0.23 (released September 1, 2015)

* Added Run & Breath silent skills, reducing running stamina cost or increasing lung air breathing duration as player practices those activities
* New building: Procedural Stick Fence ! (can be found in bottom right page of shelters)

* New building: Procedural Rock fence ! (can be found in bottom right page of furnitures)

* New building: Defensive wall reinforcement ! (can be found in the decoration page, but nevertheless increases the wall strength by 45%)

* Light fire weapons animation added!

* Lighting a molotov now requires “L” to light

* Molotov dousing – throwing unlit molotovs at enemies will cover them with alcohol, causing increased damage when set alight

* (multiplayer) Game browser now displays amount of players currently in game

* (multiplayer) Stick marker color is now synced

* (multiplayer) Fixed client not properly waiting for building bellow to be loaded before removing black screen, thus causing to fall down below (when game was saved while on a player made structure)

* (multiplayer) Fixed issues with fire replication

* (multiplayer) Players can now see each other fire arrows and other burning projectiles properly

* (multiplayer) Trees will now fall smoothly for clients

* (multiplayer) Fixed several cases where mutant would switch clothes and weapons would switch for clients when killed

* (multiplayer) Suitcases now replicate correctly between players! (previously would only work if players were close together and suitcase not not been physically moved)

* (multiplayer) Fixed issue where logs could be duplicated by juggling them between two players (SORRY!)

* (multiplayer) Fixed bodies sliding when dropped

* (multiplayer) Increased volume of walky talky

* (multiplayer) Fixed Lizards disappearing for client in traps

* (multiplayer) Fixed Clients not getting cold outside of caves

* (multiplayer) Fixed a case of foundation repair trigger vanishing for clients when it shouldn't

* (multiplayer) Fixed an issue where the body of skinny mutants would warp to regular mutants upon death

* (multiplayer) Fixed an issue where cowman would knock clients over when they were outside of his targeting range

* (multiplayer) Fixed Water level in water collectors not in sync between server/client

* (multiplayer) Audio parameters will now replicate over the network to clients

* (multiplayer) ‘Burn Damage’ animation will now properly play on mutants for client

* (multiplayer) Alive rabbits dropped by client will now move aligned to terrain

* (audio) Thrown objects will now distract enemies when hitting any solid object, rather than just trees and terrain

* (audio) Dropped objects will now attract enemies in the same way as thrown objects

* (Audio) Mutants sound clearer

* (Audio) Added player on fire hurt sounds

* (Audio) Fix jumping on ground when raining playing very watery sound

* (Audio) New fireman idle, movement, attack and getting hit sounds.

* (Audio) New female creepy mutant idle, getting hit and death sounds.

* (Audio) Added doppler effect to fireman fire movement and attack sounds.

* (Audio) Fixed missing flashlight flick on/off sound

* (Audio) Added new freakout reaction sounds to regular female mutants.

* (Audio) Increased volume of small boats/raft on water and raft paddling events.

* (Audio) Tuned all aspects of swimming sound

* (Audio) increased level of blood drips

* (Audio) Fixed timing and tuned levels of bow and arrow

* (Audio) Tuned levels of eating and drinking

* (Audio) Added lighting molotov sound and improved its held on fire sound

* (Audio) Optimized memory footprint

* (Audio) Clifftop surf sound now audible

* (Audio) Jumping on rocks plays rock sound

* (Audio) Shipping containers play metal footsteps

* (Audio) Geese have some sounds now

* Fixed anchorable rope not getting destroyed with the building it is anchored to

* Fixed player camera clipping through tree trunks after being chopped

* Player can now set tennis balls on fire !

* Reduced burning weapons memory allocations

* Made underwater breath duration more consistent

* Fixed Sleeping mutants stay frozen if killed before waking up

* Lowered position of stick marker color trigger to make it easier to find

* Player can no longer survive falls by using survival book or inventory

* Holding the “Batch” button while placing a building now automatically brings up the same ghost building to be placed again

* When items placed on the crafting mat match with upgrade recipes it will now be listed in the same fashion as normal recipes !

* Fixed some bugs with fire particle size when fires were re-lit and stocked after loading a saved game

* Fixed animal numbers never going down even when killing lots

* Opening the book while in the air now delays opening till player is grounded again

* New art added: Improved burning log (used for bonfire)

* New art added: Improved bow and arrow

* Improved look of pale cave mutants (resculpted normal map)

* Improved shading of regular and skinny mutants (better sss, less orange skin diffuse, better spec)

* Fixed seam on remote players head

* New shader – toon outline for alpha textures – selecting feathers or other items with an alpha map will now have correct outline

* Branches and leaves are now cut off trees with a built tree structure ! (only works on pine trees with moss currently – rest of trees soon)

* Wood planks in caves can now be blown up with explosives

* Survival book entry for skull lamp needed resources should match blueprint

* Doubled rebreather air capacity

* Can no longer open inventory while underwater

* More underwater sea weed/coral placed. Underwater pickups placed and some hidden caches

* Leaves are now required to build bonfire

* New item added: Oyster. Can be found in ocean, can be stored in backpack and eaten but has limited shelf life

* Terrain/world improvements, adding more detail to edges of some ponds, adding new paths, filling out empty areas, improving look of some areas

* Improved fire particles on creepy mutants

* Replaced/improved enemy necklace model, and enemy prop textures

* Fixed flickering on small pine tree sapling!

* Fixed normals on log spike tip

* Grey zone health threshold now set at 10% (was 5% before)

* While in grey zone, player weapon damage is increased by 30%

* Improved terrain textures and shading

* More plane crash animation added – more debris flying around, especially towards end as plane crashes

* Cave 9 re-work

* Fixed device placer (used by bomb & talky) showing icon too early and on colliders which nothing can be placed on

* Fixed a rare case of weapon lock up after throwing projectiles

* Fixed banding in sky especially at night (Unless on lowest material quality level, which will run slightly faster but still exhibit some banding)

* Drinking a soda will now instantly restore some stamina along with energy

* Improved shading on fat creepy mutant

* Plugged in and fixed burnt materials for all cannibal types

* Targeting a climbable wall now displays a sheen icon while not carrying the climbing axe

* Dead bodies around the world now have a chance to appear as bloody, burnt and with limbs missing

* Placing buildings near a raft no longer places it on top of the raft if it cannot be nested with it

* Fixed issues with fat creepy mutant being able to damage player when not attacking

* Fixed fat creepy able to stun lock player when knocked to the ground

* Eating mutant limbs now hurts player slightly and gives less fullness replenishment

* Halved soda thirst replenishment

* Drinking from a dirty water source (like ponds) now replenishes only half of the total thirst

* All regular mutants health increased by 25%

* Decreased fire damage to all mutant types

* Decreased bomb damage to distorted mutants

* Decreased damage done to all structures by mutants

* Decreased chance for mutants to attack structures

* Increased chance of skinny mutants eating bodies

* Arms & legs can no longer be picked up from exploded mutants

* (performance) New lods made for: Cannibal hut, Cannibal fire details,Massive rock, Background mountains,Plane crash, waterfall, pinetree top heavy

* (performance) Lowered mesh count on randomly placed dead wood and fixed orientation

* (performance) Lowered rendering ranges for all lower draw distance settings (med/low/ultra low)

* Fixed climbing wall icon not using the proper climbing axe icon

* Improved terrain around cave 10 and fixed orange tent sitting crooked on rock

* Fixed some areas where ocean trigger was missing/misaligned and would let you walk underwater or didn't have fog visible

* Switched wall experimental and basic wall positions in book. Wall experimental is now default wall.

* Better matched cliff grass to terrain grass using planar mapping

* Lowered intensity of skull light built

* Small material tweaks: Darkened cave entrances to match albedo of surrounding rocks, brightened ghost experimental material to make it easier to see during day, tweaked clouds, fixed sheen on raft rowing stick, tweaks to plants material/spec settings. Improved look of held molotov. Improved shading on dead sharks and live sharks.

* Tutorials are now hidden while in water

* Rebreather bubbles activate only past 80% screen water coverage

* Player cannot be burnt past 50% screen water coverage anymore

* It is no longer possible to open book while swimming or diving

* Can no longer light fires that are built underwater

* Improved particle effect for standing fire, fire pit and basic fire and bonfire

* Pause in inventory is now delayed by 1s to solve tone mapping issue

* Fixed building not working in both tree houses

* Fixed issue with weapon rack system allowing to duplicate items on rare occasions

* Lowered chance of getting teeth when hitting enemies

* Replaced circuit board spawners with dynamic laptops that need to be smashed open

* Fixed issue where shelters page 2 could be skipped if shelters wasn't viewed through survival book

* Sharks attack player more often now

* Sleeping and being woken by enemies should happen less often, and only when enemies are actually close

* Fixed blood particle effects missing when hitting enemies

* Fixed mutants not facing target sometimes when eating a body

* Fixed some icons (like building repair) staying up when dying

* Fixed issues with stamina calculations when running

## v0.23b (released September 2, 2015)

* Fixed tutorials being off when underwater breaking picking up items underwater and causing their pickup or can't carry anymore messages to stay on screen permanently

* Fixed bug where most oyster spawners were placed too far below sea level and set to wrong terrain texture – making them extremely rare. Also fixed issue where they wouldn't be visible, only the pickup icon in rare case they were found

* (multiplayer) Fixed issue where clients couldn't break wood planks open in some parts of caves

* Fixed bug with arms and legs not spawning bones correctly when overcooked on fire

* Added more protections against rare cases of axe not swinging (if anyone is still getting this, let us know the exact steps and we'll make a fix)

## v0.23c (released September 2, 2015)

* Fixed bug where upgraded walls could kick players when destroyed

## v0.23d (released September 2, 2015)

* Fix for burning arrows kicking clients

# v0.22 (released August 14th, 2015)

* (multiplayer) Massively improved responsiveness of enemies for clients. Should fix issues of them playing wrong animations, stuck in wrong poses or sliding during combat.

* (multiplayer) Fixed bug where mutants could get stuck in burning animation (which could also be mistaken as disco-dancing)

* (multiplayer) Fixed enemies sometimes not acquiring new target after current target is knocked down

* (multiplayer) Revive other player feature now requires to hold the "Take" button for 2.5s

* (multiplayer) Fixed bug where client entering save game would hear multiple building complete sounds

* (multiplayer) Fixed issue where players would sometimes not hear building complete sounds

* (multiplayer) Fixed clients getting kicked when eating leg/arm after it got burnt

* (multiplayer) Fixed clients having lighter stuck after loading a saved game with lighter equipped

* (multiplayer) Fixed clients not being able to repair custom foundations

* (multiplayer) Increased time clients can wait with black screen at start of game to give time to bigger maps to load before enabling gravity (should reduce cases of falling through structures)

* (multiplayer) Fixed client seeing tree stumps host doesn't around plane crash

* (multiplayer) Fixed some inventory sounds audible to other players

* (multiplayer) Fixed fat creepy not attacking client players

* (multiplayer) Other players flashlights now visibly light up on mesh

* (multiplayer) Fixed female enemies sometimes having wrong dead body

* (multiplayer) Fixed issue causing foundation floor to not fully show up for clients when structure isn't closed

* (multiplayer) Breakable pathways in caves are now synced with clients

* (multiplayer) Fixed partially cut down trees saved as cut down in MP

* Plane crash animations added! Draws now fly open, luggage gets sucked out!

* New cave floor variation type added

* Enemies and animals should do a better job of avoiding player built fires

* Improved mutant animation, more death variations

* Smoother overall player movement, hopefully less camera stutter

* More chance of seeing skinny mutants climb trees

* (audio) Impact sfx added to cages crates and wooden table

* (audio) Ambient river now fades in/out on approach

* (audio) Linear emitters for river sfx, sinkhole streams, oceans, some waterfalls and clifftops

* (audio) Events added for all different lake sizes

* (audio) Crocodile sounds added

* (audio) Voice count raised to 128

* (audio) Raft will now play ambient sound when positioned over water

* (audio) Sound effects added to abandoned yacht

* (audio) Mutant baby audio added!

* (audio) River sound improved

* (audio) Clifftop wind added to clifftops

* (audio) Player extinguish sigh

* (audio) Unique sounds added for eating meds, eating meat and drinking water

* (audio) climbing axe on rock sounds added

* (audio) Bat Scare created

* (audio) New events added for breaking laptops,cardboard boxes and effigies

* Improved lichen rock visuals

* Improved enemy burn animations

* Fixed crouch player input sometimes not responding

* Tweaked weapon upgrade stats - making a weapon lighter will now also lower its damage slightly. Lowered all upgrade amounts.

* New faster tonemapping and eye adaptation

* New physical bloom (faster and better looking)

* Fixed fig trees popping off too soon

* Fixed issue with v-sync needing to be disabled in game options menu

* Fixed missing rain particles when raining - new rain particle has fake refraction added

* Book light now only affects book and not rest of world

* Water now accumulates faster on terrain when raining

* Lightning flash now casts shadows!

* Cave 6 major re-work

* Cave 8 rework

* Updated enemy layout in cave 6

* Metal food carts now react to being hit

* New cliff rock art (connects terrain to cliffs)

* Improved cleaning up equipped stuff when dying (drops body, logs...)

* Equipping plastic torch now properly hides lighter tutorial

* Pressing escape while in save screen now properly closes it

* Fixes issue with lighter not working properly when having a bow on a weapon rack

* Fixed icons staying up after exiting item holder triggers

* New cliff shader! Adds grass/moss based on slope. Used on big cliffs and big rock chunks, fallen logs, etc. everything.

* Fixed blown up floor logs on custom foundations not getting respawned when repaired

* Fixed ghost wall defensive not saving properly (retro compatibility hack might cause old saves to have an overlapping log in between chunks)

* Made Ex Floors & Roof closer to supporting walls (not retroactive)

* Reduced power and speed of katana slightly

* It is no longer possible to pick things up while pushing the log sled

* Crafting arrows while having bow equipped and no arrow before now properly equips an arrow automatically

* Cleaned up/reorganized graphics options and added new category for post effects

* Defensive spikes, basic wall with window, basic wall with door, Bonfires, Gazeebo and basic stairs now have proper render distances on the max setting

* Animals should do a better job of avoiding cliffs/walls/trees etc.

* Broken crate bits no longer impede player movement

* Fixed player not aligned to benches sometimes when sitting

* Player now faces the direction they approach benches when sitting

* Material Quality setting now changes water material for a cheaper one when using the low setting

* Improved look of sinkhole transition

* Improved look/layout of cave entrances

* New Art: Replaced large ugly rock

* New image effect: Depth of field (currently blurs player also, this is experimental and not recommended!)

* Fixed player heavy attack sometimes getting stuck on

* Fixed animals not triggering big traps

* Fixed bug causing suitcases to look open but be closed or the other way around

* Fixed bug where carrying an enemy body on fire causes the fire to stay forever after dropping it

* Fixed right arm on dead bodies not choppable

* Fixed player being able to double jump under certain conditions

* Fixed issue with structure anchor not being stored correctly, causing it to accept multiple objects instead of one and destruction to fail working properly for bridges (not retroactive)

* Fixed turtle meat not spawning when already owning a turtle shell while picking it up

* Fixed water partially covering entrance to cave3

* Fixed equipping lizard skin while having plastic torch out breaking its held animation

* Fixed bug where one of the cave climb out entrances would stop terrain loading

* Halved chance of rain

* Standing fire will now also warm players as well as give off light - but has much smaller warmth trigger than regular fires

* Improved foundation destruction logic to prevent some cases of foundation ending without bottom row, flying in the air

# v0.21 (released July 28th, 2015)

* Following features now require to hold their respective button for half a second to be triggered: cancel ghost buildings, drink & gather water, procedural buildings auto fill, eat berries and mushrooms found in world, eat plane food, eat cooked/dried food, light fires, save, sleep

* Dropping a body now properly brings up right hand item instead of both left and right

* Fixed cursor being visible during loading

* Spears no longer fall through terrain or disappear when colliding with animals/enemies

* Spears collide with more solid objects

* When already equipped, lighter no longer needs to be stashed first to light a weapon or arrow

* Fixed lighter toggling

* Timmy's Robot toy can now be fixed on the crafting mat in inventory !

* Flare gun can now be reloaded using flares on the crafting mat

* Can no longer equip utility item when in inventory using keyboard shortcut

* New pedometer art added! Now actually looks like a pedometer instead of a mobile phone

* Pedometer pickup removed from plane and added to tennis player corpses

* Tennis team – improved visuals, added detail maps and better shading. moved to hidden position in caves

* Fixed Walky Talky disappearing when added to the crafting mat

* improved fat creepy mutant, more attack variety, can be staggered by explosions, can dodge close player attacks

* Fixed bugs with log sled when grabbing/letting go while on a foundation

* Birds can now be killed with explosives

* Ocean fixed issue where high detail bump would sharply mix with low detail distance bump

* Water sources now delays showing icon again after the drinking animation

* Fixed both R and Xbox R being visible and overlapping each other in experimental wall toggle addition prompt while using a gamepad

* Fixed button navigation in book (“PreviousPage” & “NextPage” buttons)

* Added action icons to Previous/Next book page buttons when using a gamepad

* Previous/Next book page buttons can be trigger with “Take” button when using a gamepad (A by default)

* Pressing “Drop” button (B by default with Xbox gamepad) while in book now closes it

* Fixed torch getting stashed when equipped from inventory while having lighter equipped

* Fixed fires not being lightable while having torch out

* Flashlight now has longer throw and is less saturated

* New version of smaa added to antialiasing

* Clicking back button of option menu now saves settings (was done in following menus until now)

* Pressing B on Xbox gamepad on a UI with a back/cancel or continue button now triggers it

* Fixed player feet sliding when walking slowly with Xbox controller

* various fixes to swimming animation/movement

* Fixed upgraded stick counters not showing properly when adding ingredients to crafting mat

* Swimming fixes: Player no longer shoots out of the water when breaking surface. Swimming animation turns off faster when exiting water. Fixed bounciness when walking in shallow water. Fixed animation glitch when jumping into shallow water.

* Replaced ugly grass terrain texture and fixed issue where starfish were still spawning on top of it

* New waterfall flowing white water shader!

* New item: Breakable flare box!

* Larger radius on bomb explosions, and larger gib radius for mutants

* Burn animation added to mutants!

* Improvements to cowman mutant a.i.

* Fixed frost post effect (when cold) going a bit too high on occasion (i.e. after a lag spike with the right timing)

* Fixed issue when exiting/entering caves causing massive fps drop

* Cold damage effect made more subtle

* Fixed cold damage message staying up after dying in caves while it was up

* Increased LOD range in caves

* Time is now paused while in inventory in single player mode

* Dropped flares when you have too many now properly drop an unlit flare

* Dropped dynamite when you have too many no longer explodes

* Fixed log holder take/add icon arrows reversed

* (multiplayer) Fixed enemy animation being buggy for client if they died when on fire.

* (multiplayer) Fixed flash light not replicating properly on remote players (would either now light up at all, or be too bright).

* (multiplayer) Fixed an issue where rabbit trap would not always work properly when reset by non-host players.

* (multiplayer) Fixed an issue where rabbits in cages would disappear on load.

* (multiplayer) Made receiving and sending game invites through Steam a lot more reliable.

* (multiplayer) “Press E to respawn” message after dying now uses the proper “Take” action icon instead of the fixed E

* (multiplayer) Fixed remote players name showing while game is loading on their end or during their plane crash sequence

* (multiplayer) Fixed rebreather not showing up on remote players

* (multiplayer) Fixed dropped live rabbit not spawning for other players

* (multiplayer) Fixed map pieces not showing properly for remote players

* (multiplayer) Fixed dropped sticks/rocks/flares/dynamite/skulls not showing for remote players

* (multiplayer) Gardens now replicate for players over network!

* (multiplayer) Fixed an edge case issue where water in water collectors would differ between servers and clients

* (multiplayer) Remote players will now show the correct blood/muddy arm textures depending on if they are bloodied/muddied locally

* (multiplayer) Fixed an issue where large traps would de-sync if host triggered them

* (multiplayer) Fixed loading a game saved in caves as client

* (multiplayer) Fixed parts of players own heads visible at some angles, such as climbing down rope or moving camera fast to one side

* (multiplayer) Revamped build mission system to be more reliable

* (multiplayer) Breakable wood planks are now synced between players

* (multiplayer) Explodable caches are now synced between players!

* (multiplayer) Fixed some issues with cowman over network

* (multiplayer) Fixed repair icon staying visible for client after repairing a building

* (multiplayer) Fixed desync issue with log cabin destruction for client

* Fixed mutant leader skull lights flickering strangely(now has candle light flicker setting)

* Fixed small rock pickup misaligned

* Fixed body parts still sometimes falling through caves when cut

* Fixed suitcases spawning items multiples times when hit

* Fixed heavy swing restoring stamina

* Fixed missing cave nav mesh

* Fixed various issues with wall climbing

* Improved explosion/collapsing visual effects for some buildings

* Fixed shadow blocking partially blocking climb exit in cave1

* Fixed player sliding while opening book whilst jumping

* (hopeful fix) for player occasionally flying into air when running and jumping at enemies.

* world – improved cliff areas and grass placement and thinned out some excess rocks on some cliffs

* Switching batches of textures to crunched compression mode – should improve load times and memory

* Going in water without a weapon no longer brings up default weapon

* Carrying body without having a weapon equipped before no longer brings up default weapon when dropped

* Bed, Log Holder, Rock Holder, Stick Holder, Weapon Rack and Explosive holder can now be jumped by cannibals and destroyed by mutants (Armsy, Virginia, Cow man)

* Buildings that have collapsed logs now require logs to be repaired (1/3 of collapsed logs)

* Fixed bug where foundation would prevent itself from repairing properly and respawn with missing bits at bottom

* All mutants can now interact with swinging bodies, dynamic crates and other objects

* Fixed jump input occasionally not registering

* New building: Extensible Defensive Wall! (replaces legacy one in book)

* New building (kinda): Floor hole cutter! (caution: holes are definitive !) (SP only)

* Gamepad mappings are now properly refreshed when a new one is plugged in and each gamepad has its settings saved independently

* Fixed gamepad mapping icons not getting loaded when gamepad wasn't plugged from the start

* Fixed Ex wall sometimes going below ground when placing

* Volumetric light sample quality settings now hooked up into options menu (turn up for smoother more accurate volumetric light, and turn lower for faster performance)

* Terrain quality now also influences terrain pixel error resulting in less popping on higher settings and faster performance but more popping on lower settings

* Northern mountains are now cut out of ai nav mesh properly

* Cave 7 lighting and props pass

* Clicking on exceeding story clues in book now opens corresponding page of notes

* Fixed enemies sometimes not turning aggressive when attacked

* Fixed enemies in wrong position sometimes when caught in noose trap

* Fixed camera looking down neck on plane crash intro

* Added “Max Frame Rate” setting to option (can prevent camera stutter with some hardware)

* Swinging a lit weapon no longer causes big light to emit during swing, instead light intensity is lessened

* (audio) Setting a weapon alight plays fire start sfx

* (audio) improved waterfall sounds and range and positioned on outside falls along with in caves

* (audio) multiplayer) Fixed inaudible deer startle, animal hit and die sound effects for clients, along with inaudible weapon Swoosh sound effect for client.

* (audio) Increased ambient audio zones in upper areas of world, tweaked hanging rope sounds and player dragged away sounds

* (audio) Sound effects for bird landing on finger added

* (audio) Wood destruction sound effects, owls at night, improved mutant audio.

* (audio) Added hanging rope and dripping blood sound effects to hanging bodies

* (audio) first pass of stream audio added

* (audio) open areas given ambient audio

* (audio) clifftop wind added

* (audio) sinkhole ambient audio added

* (audio) pond audio louder

* (audio) buildings falling down play impact sound

* Fixed enemy dropped club disappearing when trying to add to crafting mat

* Lowered dust area and amount when foundations collapse

* Fixed animals not running away from trap when released

* Fixed some fish above water in top half of map

* Fixed player sometimes not jumping when trying to get out of cave water

## v0.21b (released July 28th, 2015)

* Small fix for users with some peripheral configurations who were unable to move in tonight's update

## v0.21c (released July 29th, 2015)

* Fixed bug where some old saved games wouldn't load

* Fixed bug where equipping some items in left hand in old saved games could break items/cause items to vanish

* Fixed bug when equipping battery based left hand item while out of battery

* Fixed bug where climbing down rope player hands would be offset

* (multiplayer) Fixed issue where players could be teleported to log sled across map in some cases

* Fixed flags/markers action icon visible by default

# v0.20 (released July 15th, 2015)

* New usable item added: Dynamite stick

* New art added: Dynamite crate

* New distorted cannibal creature added!

* Improved skin shader - now supports ambient scattering

* improved crocodile attack animations

* Added more story clue items to note section of book

* (audio) Fixed building complete sound sometimes not playing

* (audio) Body drag sound added to drag away scene

* (audio) Seagull audio improved

* (audio) exertion and cold no longer play underwater

* (audio) Pale male audio added

* (audio) Pick up whoosh sound now plays more consistently

* (audio) New Spike Wall trap sound

* Tree moss added! Always faces north regardless of tree

* orientation, can be used to help navigate

* Removed ‘animal’ layer from inventory camera fixing bugs with animals walking over inventory, blocking view, or viewing fish swim over inventory

* Female mutants will jump on and attack player from tree trunks more often

* Improved balance between mutants being aggressive and stalking player

* Player feet now stick to ground when looking down and turning!

* Fixed some issues with hit direction not being set properly when swinging stick

* Unblocked and fixed entrance to cave 7

* Cave 2 hidden stash room added

* Deer now have motion blur

* Partially cut trees are no longer saved as cut down, instead they are fully restored when loading a saved game

* Decay system added! Meat now ages over time in inventory, going from fresh to edible to spoilt and providing less and less benefits and eventually becoming harmful. (meat appearance as well as inventory tooltip title change to reflect decay state)

* New items added: Old breakable soda crate! Old breakable empty crate, old breakable dynamite crate

* New pickup/craftable item : Upgraded spear!

* spear is now throwable!! - hold right mouse to aim, press left mouse to release

* Removed plastic torch from suitcases, can now only be found in gameworld.

* Fixed fish falling through terrain if dropped by player

* Fixed bug where breaking cave wood doors would give you leaves and play hit plant sound effect.

* Bloody tables are now breakable!

* rough Cave 10 added

* props and pickups added to main cannibal village. Dynamic

* Bodies now hang from dead tree.

* Ultra low draw distance is now more aggressive/culls items closer

* (optimization)Material quality setting in options menu now simplifies some shaders on lower settings

* (optimization)Gpu performance improvement removed unnecessary pre-clamp shader

* (optimization) Water lod added to ponds, previously would calculate refraction for all lakes/ponds now will only do this for screen visible water. Removed second grab pass roughly doubling performance of ocean/lakes when visible.

* (optimization) Bloom performance doubled

* (optimization) reduced memory garbage collection per frame drastically (should reduce stutters)

* Fixed story clue tutorial sometimes being outside of tutorials section on screen

* Small boxes can now be smashed open to recover item inside

* Laptops can now be smashed open to retrieve circuit boards

* better combat layout throughout cave systems

* fixed an issue where baby mutants would not target player properly

* more range of movement when looking around on a rope

* flashlight now follows camera direction when on a rope

* fixed animation popping on mutants when sleeping in a cave and near edge of screen

* New art added: Underwater coral!

* Going back & forth towards berry bush no longer respawns berries

* Eaten berries & some bushes no longer respawn after loading a saved game

* Fixed lighter getting stashed after lighting a fire even if it was previously equipped

* Added distortion to breakable wood planks when hit

* Fixed plastic torch light color not being set properly on startup causing low battery flicker to be not visible before getting bloody or going into water

* Fixed suitcases cloth sheen icon and chocolate bar pickup icon not rendering

* Enemies can now hear explosions and will be woken up/react

* (multiplayer) Fixed not receiving invites after playing a SP game and going back to title screen

* (multiplayer) Fixed bug where logs would sometimes get stuck in air

* (multiplayer) Added display on clients to let them know when server is not responding

* (multiplayer) Fixed log sled grab icon staying up when targeting the trigger while another player grabs it

* (multiplayer) Fixed not being able to continue saves as client

* (multiplayer) Fixed black screen as client when starting a new game

* (multiplayer) Loading a game saved on a building as client should now respawn on top of it

* (multiplayer) Fixed having to walk out of trigger and back in to target a in range building after placing it

* (multiplayer) Fixed client not seeing present ingredients in ghost buildings until some more were added after host loaded a saved game

* (multiplayer) Foundations now use the same destruction system as in SP

* (multiplayer) Not yet available book entries are now clearly shown as such

* (multiplayer) Raw meat dropped by a player is now seen by others too !

* (multiplayer) Clients now place ghost items instantly without a lag delay

* (multiplayer) Fixed issues when dying with inventory or book opened

* (multiplayer) Fixed boar vanishing when killed by client player

* (multiplayer) Fixed enemies falling through ground if host entered a cave without client players

* (multiplayer) Hopefully fixed issue with animals sometimes invisible, and mutants sometimes invisible

* (multiplayer) Fixed bug where if player was killed in a cave (instead of outside) ocean would stop rendering and issues with animals vanishing could occur

* Cave 1 tweaks - added more holes with light streaming in, fixed some stalagmites floating above floor, moved headless body,

* added dynamite pickups near hole to sinkhole. Fixed hole to sinkhole view being blocked. Added more enemies to large room.

* Re-worked dead room with better pickups. Replaced hanging bodies with dynamic hanging bodies. Fixed repeating story pickups, so now only 1 of each is pickupable (i.e. bibles) Cave 1 now connects to Cave 3. Hanging bodies added to armsy room.

* Fixed bird landing on hand if lighter was out

* Fixed lighter staying on in water until you dive a certain depth

* Fixed bug where point or spot lights would cause ocean to glow like a hottub

* Fixed error in story clue folder when loading a saved game

* Fixed (again) bug where picking up a raccoon would give you lizard skin

* New story item added to yacht!

* Overcooking arms or legs on fire will turn them into bones eventually

* New pickup/weapon item: Bone!

* New cave grounds! New cave walls

* New cave wall shader with running water!

* Fixed bunch of overlapping cave shadow objects

* Fixed plane hull not getting cut out of nav mesh on load game

* Fixed tree shadows turning off when coming from behind or side of player camera

* Fixed sharks swimming through sand sometimes

* New game stats: Cooked Food, Burnt Food, Cancelled Structures,

* Built Structures, Destroyed Structures, Repaired Structures, Edible Items Used, Items Crafted, Upgrades Added, Arrows Fired, Lit Arrows, Lit Weapons, Burnt Enemies, Exploded Enemies

* Can no longer build big structures on raft & sled (only small ones like log holder/fires will work)

* Building raft & sled on other structures now works properly

* Fixed cave lights popping on/off too soon

* Cave ambient fill lights added in cave holes

* Forced volume light occlusion to take caves into account

* Picking up mutant bodies now requires to hold the “Take” button for half a second

* Held map is now more readable under lighter

* Fog will now slowly fade away if player is inside a cave

* Fixed fireweed/horsetail plants not being cuttable

* Improved look of save game thumbnails & added date/time (community request)

* Attempting to pick up soda while at max capacity now drops it back on floor instead of destroying the pickup

* Reduced energy drain when cold

* Fixed arrow fire going out when right clicking while aiming

* Getting hit while holding lighter now has a 1 on 4 chance to stash it

* instead of always

* Brightened plastic torch light, increased battery lifetime a bit

* Fixed cut arms falling through cave meshes

* Burning stick now stays lit 4 minutes when not attacking

* Improved burning weapon formula fire scale formula to look better with higher durations

* Fire weapons now emit much more light!

* Massively increased brightness and range of throw flares when held or thrown

* Equipped cold armor (Deer Skin) parts are now visible in armor bar of hud

* Closing inventory while upgrading weapons now properly turns things off instead of breaking craft item positioning

* Loading a save with a bridge not attached to anchors now destroys it instead of erroring (could block loading in mp)

* Bridges are now properly destroyed when the tree structure they were attached to is cut down

* Fixed equipped items switching when exiting rope

* Player can now equip rebreather underwater without dying instantly

* Using air canister while underwater and rebreather isn't in use (if it was out of air) now actually reloads it

* Out of water with rebreather, light stays on for 2 seconds and then dims over 5 seconds

* Fixed bug where falling off some fishing stands would cause player to wake up in cave but not be able to swing axe

* Fixed wrong icon display in inventory item tooltip while using a gamepad

* Fixed fire not playing sounds when lit

* Torch in suitcases replaced with new batteries pickup

* Fixed enemies not reacting to effigies

* Enemies can now jump the log sled!

* Effigies now burn a lot longer but turn into skulls, bones and rocks pickup when done !

* Fixed weird molotov throwing anim when spamming

* Fixed wall placement when below a ceiling

* Fixed rope bottom trigger position in caves (not retro active)

* Improved draw distance on some items

* Dropped item fixes: taking more meds than you can carry will now drop the med instead of vanishing it.

* Circled map cave entrances to make them more clear, and made crosses to blow up caches smaller

* New surprise weapon added. look for some dead tourists in front of a cave.

* Fixed molotov spreading fire not centered on flame position

## v0.20b (released July 16th, 2015)

* Fixed raft not working in single player!

* (multiplayer) Fixed an issue that could cause abnormally long save times or crash game

* (multiplayer) Fixed error where thrown bombs would spam errors and lower framerate for host/client

* (multiplayer) Fixed bug in mutant a.i. where half of the enemies would stop finding player after exiting a cave

* (multiplayer) Fixed issues with building on top of platforms which could break mp completely or just not work

* (multiplayer) Fixed possible drastic performance drop if player was cold as host and loaded a saved game (possibly only relating to 0.19 saves)

* (multiplayer) fixed an issue where half-built bridges would not properly replicate to clients

* (multiplayer) fixed an issue where if you attached a bridge to a tree platform, neither of them would replicate out to clients after loading a save

* (multiplayer) fixed two smaller issues with large traps and standing fire pits on client/server

* Possible fix for issues with logs not visible in lod sled or log holder for older save games (not able to reproduce here, let us know if its still happening)

* Fixed batteries in suitcases having torch icon

* Fixed suitcase spawned items not visible always (folded jumpers, batteries etc.)

* Fixed regular spear turning into upgraded spear when thrown and picked up again

* Fixed bug where it wasn't possible to pull out lighter (or other left hand item) when carrying a log

# v0.19 (released June 25, 2015)

* (multiplayer) Fixed some cases of creepy mutants not targeting remote players correctly

* (multiplayer) Increased priority of mutants, making them smoother/less laggy

* (multiplayer) Fixed issues with log sled after loading a saved multiplayer game

* (multiplayer) Typing in chat no longer triggers in game actions

* (multiplayer) Fixed chatbox being locked when input loses focus

* (multiplayer) Fire now spreads/replicates

* (multiplayer) Rope is now buildable

* (multiplayer) Players will now appear as the correct body type/clothing for everyone

* (multiplayer) Game invites are now properly queued

* (multiplayer) Clients now have a different save per server and respawn after loading where they saved instead of in plane (respawn after dying is still located in plane)

* (multiplayer) Fixed a bug with experimental stairs in saved games which could cause issues for clients loading

* (multiplayer) Added message when alt tabbing as host to warn about risks of disconnecting clients

* (multiplayer) Fixed issues where dead bodies would sometimes not replicate correctly

* (multiplayer) Fixed bug where modern axe would appear as old yellow axe to other players

* (multiplayer) Fixed bug where killed turtles would give infinite shells and no meat for client players

* You can now toggle the color of stick markers (SP only)

* Fixed Stick Marker flying above floor (not retro active)

* Fixed several tree structures which did not properly save which tree they are built on (not retro active)

* Fixed tree structures not getting destroyed when their attached tree is found cut down after loading a saved game

* It is now possible to build small structures (like log holders ;) on top of rafts !

* Added collision box to log holder

* Cut down trees are now accounted for by the tree occlusion system

* Improved building placement formula, now handles better big height variations like you can have near edges of floors

* Deer will react more to being shot with arrows

* Deer can be seen nibbling at bushes sometimes

* Tiered destruction system! Enemies can now only damage certain structures, depending on how strong they are. Only armsy can bring down defensive walls.

* Armsy will attack structures more often and deals more damage

* Improved animation for Armsy behaviours

* Improved animation for Virginia

* Crocodiles can now swim and attack player in water, also have more health and deal more damage

* Fixed player arms not aligned to mutant sometimes during drag away cutscene

* Fixed water vanishing at some angles from the camera

* Fixed pickups looking solid white when viewed underwater

* Fixed some issues with loaded plane prefab/multiplayer plane prefab- flying seats, missing decals, misaligned geo

* Fixed judder when sprinting and low stamina

* Player must stop running now before stamina will recharge

* small delay added to stamina recharge if you run out of stamina while sprinting

* New plane dirt chunk added to plane crash

* New save slot system, you can now have up to 5 SP games and up to 5 mp games (as host)

* Save slots are organized per steam user id to prevent cloud from messing things up when using the game with multiple steam accounts on a single computer

* Saving now archives the previous save file in case you need to restore a backup (local only)

* New save slot selection screen when saving in game

* Save black screen is now in sync with the time saving takes

* Improved cloud save management

* Added “Equiped” status display to rebreather inventory tooltip

* New mutant type “pale skinny” added to caves

* Shadows now fade off to darkness when player is in a cave, and fade to bright when not in a cave

* Sun/Moon are no longer faded out when in caves – making transition from outside to caves more natural and allowing light to bleed in from outside

* Improved terrain around beaches

* New small burial sites added

* Fixed bug where inventory would appear black if an integrated (intel) graphics card was used

* Fixed some winter pine trees sitting on ocean

* Happy birthday trap is now twice as wide

* Noose trap has a wider trigger zone, making it easier to catch enemies

* Lighting camp fires now requires player to hold the lighter over the fire until it is lit

* Enemies will react properly to walkman placed as a distraction device

* Fixed a save/load issue that could cause experimental walls to increase size of save game drastically and crash loading

* Added a 60s delay in between displays of lighter tutorial

* Burning weapons & arrows no longer burn things when not attacking with it

* Burning weapon stay up longer when idle but use fuel quickly when attacking

* Burning arrows no longer damage owner player when fired

* Cave combat layout tweaks for balance

* Player feet sink slightly now when walking through sand and speed is slightly reduced

* Some collected story items are now stored in back of survival book in notes section

* Standing fires are now destroyed upon collision with enemies

* Timmy photo added to backpack as reminder to be a better parent

* Player camera no longer clips through terrain when entering a rope from above

* Better position of exit rope trigger on fishing stands

* Removed weird delay on gravity when exiting a rope

* Pickups added to top of some fishing stands

* Animation added now when player drinks at ponds/lakes

* Balance – removed rebreather pickups from overworld, can now only be found in cave location. Modern axe removed from yacht. Air canister added to yacht location. Removed old axe in wooden door at cave entrance. Changed cave dead to always be in cave 2 location. Removed lights from cave hats. Re-worked pickups in cave 1 dead room.

* Revamped multiplayer start game UI to be compatible with gamepads and save slot system

* Cave mutants can be found sleeping on the ceiling again

* Plastic torch now rotates more in line with camera, making it useful to look up and down

* Pale versions of armsy/vag added to world. Faster, stronger, with more armour

* Underwater fog added!

* Fixed a broken link when navigating in survival book with “prev/next page” gamepad buttons (left & right shoulders by default)

* Repairing buildings now costs 2 treesap plus an amount that increases with damage suffered

* Fixed missing Tooth & Feather upgrade recipes for stick & stick upgraded

* Fixed flare gun sometimes hitting player when firing

* Smaller scale on stealth armor leaves to make things easier to see

* New art added: Boar skull, boar skull on stick, boar decorative statue

* New prop added : Lifesaver

* New prop added : Skull pile

* Cave 9 added

* New usable item added: Compass

* New item added: World Map (torn apart in 4 pieces to find and combine on crafting mat)

* Replaced “pedometer” input action by “Utility” which toggles latest item used from inventory of Pedometer/Walkman/Compass

* New art added: better looking Lichen rock

* Lowered amount of sharks and moved further away from shore to avoid sand sharks

* New props added to cargo crate

* Added physics to (some) hanging bodies, hit them and see them swing around

* North area cold is now only occurring in the higher mountain part and no longer on the beach

* Fixed fires not being lightable after burning out once

* Fixed exploding trees leaking objects

* Aligned turtle shell to upper part of tarp to make it easier to find in inventory

* (audio) Added sound effect to metal door opening/closing

* (audio) Increased FMOD mix buffer size when system sample rate is high to prevent stuttering audio

* (audio) Better balancing of wind, falling leaves and animal footsteps

* (audio) Fixed missing distant calls between mutants

* (audio) Boar attacks and feet sounds added

* fixed dead bodies moving away from player when picked up and dropped repeatedly

* You can now exit room behind metal door, by jumping into pool of water,swimming up, finding rope, jumping into another pool of water, and swimming up and exiting via... geese lake

* Increased tree draw distance for the Ultra High draw distance setting

* Smoothed out work scheduler response to lag spikes to prevent it from inducing stuttering

## v0.19b (released June 30th, 2015)

* Fixed issue with saved games for players using a fresh install of game.

* Fixed missing modern axe pickup! (check main cannibal village dead tree)

* Fixed some issues of player not being able to swing axe after dying

## v0.19c (released July 1st, 2015)

* Fixed issue where multiplayer save game issues would occur if a tree with a tree platform and connecting bridge was partially cut before saving.

# v0.18 (released June 4, 2015)

* More of world opened up/developed

* New background mountains added (replacing old green mountains)

* New sea weed added to underwater areas

* New explodable rock type added. Place explosives near by to destroy rock.

* New cannibal village hut style: Beach hut

* New neon climbing rope texture

* New story related pickups added!

* New Plane interior art and exterior crash art

* New Plane lighting! (more moody, closer to trailer 3)

* Moved boars to only appear in top half of map, tortoises now only around lake zone

* First pass at full gamepad support !

* Re-work of all icons – will now display key set in custom key mappings, will switch automatically to Xbox controls when using controller.

* New player arm model/textures (no more seam on thumb! and better overall looking)

* New inventory backpack model.

* Foundation destruction system ! Foundations can sustain a certain amount of damage up until the point they will completely collapse.

* Building destruction system ! Smaller buildings like wall collapse at once and bigger ones can lose whole chunks before collapsing

* Building explosion system ! Small buildings like built fires are instantly blown apart but bigger ones like log cabins lose bits and suffer damage

* Building repair system ! Costs 1 tree sap to repair all damages done to your building (will eventually increase this amount once balanced)

* Enemies will now try and attack built structures.

* Audio – Over 200 new mutant voice audio events added

* Audio – balance and tweaks on footsteps, animals and other world sounds

* Player can no longer jump climb up steep colliders

* With climbing axe equipped, now \*any\* cliff face can be climbed, and you can move left, right, up and down!!

* Oar mechanism added to raft – press e to enter driving mode, mouse1 to move forward, a/d to steer left and right

* Raft should be pushable while on land now

* Fixed camera jumping to a random angle when exiting sled/rope climbing

* Player can no longer climb a rope whilst pushing a sled

* Procedural buildings in ghost mode are now properly culled

* When pot is filled with clean water, it can be drunk from within the inventory (like the waterskin)

* Some axes now are faster at chopping trees than others (Hint, modern axe is better)

* Sleeping at night in a shelter will keep you asleep now until the sun is up (unless woken by enemies)

* Fixed skull decoration not turning red when impossible to place

* Timed Bombs can now be planted on trees/walls/traps like the walkman

* While placing Foundations, it now shows a log between target position and the floor below before any position has been locked

* Each foundation chunk how has an anchor near the top !

* Fixed Foundation/Floor/Roof ghost collider requiring to move out of collider before it can be targeted

* When exiting swimming & climbing it now properly restores the previously equipped right hand item

* Cold damage now has a more meaningful visual feedback

* Raft now takes 4 rope to build (along with other needed items)

* Cloth can now be combined to craft rope

* A.i./pacing tweaks. Removed a delay before enemies start populating world. In overworld, enemies will sleep at villages and cave entrances during day, whilst some will

patrol world. On dark, all mutants become active. At dawn some mutants will run back to villages to sleep and others will continue patrolling world

* Improved accuracy of a.i. water avoidance

* Fixed mud pickup being bright purple

* After cutting down a tree, spawned logs do not roll as far or as fast

* Fixed falling trees sometimes not turning to cut logs straight away

* Player crouch speed is now set correctly

* Moved cave 4 death position further back so you don't get instantly killed by Virginia

* Made dead tree roots smaller by 30% and added more accurate collider so it can be climbed

* Fixed generic meat pickup icon having stick picture

* Fixed bug where game would sometimes start with player facing wrong direction in plane

* Fixed bug where animals would sometimes dart off at super speed

* Increased speed of deer to make chasing it down less viable

* New bush type added: Blackberry

* Added waypoint system for cave mutants, instead of sleeping some cave mutants will patrol between set points

* Removed speed penalty when swinging weapon while holding lighter (for now, may change with further game balance)

* Lowered friction on dynamic plane chairs so they're less ‘sticky’ when pushed around

* Reduced ‘slippery slope’ effect, player is less likely to slide out of control when moving fast down a hill

* Revamped mouse detection in book to make sure nothing gets in the way and prevent from clicking entries

* New improved ssao with color bleeding

* Fixed missing moon texture!

* Better cloud lighting!

* Trees now fall in the direction of the last cut

* Fixed trees visibly popping in after plane crash sequence

* Graphic settings are now saved when leaving the pause menu in game instead of when exiting the game

* Falling trees now send damage to whatever they hit (including buildings!!)

* Experimental walls are now split into individual buildings when placed (means they can be individually canceled/built/destroyed etc.)

* Stealth kills can now be performed with any axe/rock/stick type weapon

* Rebreather no longer auto equips (open inventory to equip) and light now only comes on when underwater

* Fixed bug where explosives would explode apart some mutants into purple chunks

* Tree billboards now blend instead of popping between angles!

* Improved vegetation updating system with tiling to only refresh objects in player's surroundings (less cpu usage, more accurate updating)

* Fixed some bugs with rope climbing hands not being aligned correctly

* Fixed some instances of player not playing fall to ground animation on dying

* New procedural stairs system !

* New tree occlusion based draw distance calculation system (improves visual quality in open areas)

* You can now trash partially built structures and recover (some) of the items used!

* Removed blocking near big lake

* New dangerous animal type added!

* New discoverable camp added!

* Fixed bug where some particles would be drawn with a black box around them if ssao was disabled

* New dynamic wind system. Wind intensity will change sound and leaf/grass tree rustling. (currently only on 1 tree type)

* Fixed flickering in the transition between procedural building ghost and built states

* Music added to player dragged away scene

* Music (removed horror sting when player is sighted)

* Shadows – Fixed bug where close shadows would flicker/break up even on highest shadow settings

* Torn off cockpit is now findable in world along with the pilots and some supplies

* 2 new cave systems added

* Cave 5 door can now be opened by placing items on weight

* Fires now properly save their fuel amount and lit state

* Improved lod system to reduce amount of objects when using low (66%) or ultra low (33%) draw distance setting

* Improved distorted mutants pacing and navigation in world

* Increased player fall damage, it is now possible to die from a great height

* New building: Tree sap Collector ! Add to a tree (like tree houses) and come back frequently to gather the resource. Use it wisely to repair your fort from mutant attacks !

(can be found beside Bow Target in book)

* Fixed bug where skinning a raccoon would give you lizard skin

* Fixed numerous issues with log sleds!

* Billboards now have translucency, better normal maps, and match the rendered meshes closer

* Bombs now do more damage to enemies.

* Fixed various issues with all built traps

* Various performance improvements (cpu and GPU)

* (multiplayer) Fixed issues with item holders (sticks, rocks, logs etc.)

* (multiplayer) Flare gun now works for clients

* (multiplayer) Player will not get stuck sideways when climbing ropes

* (multiplayer) Added support for throwing flares, bombs and molotovs

* (multiplayer) Bow damage works properly for clients now

* (multiplayer) Experimental building system now works

* (multiplayer) Bridges now work

* (multiplayer) Fixed log duplication bug

* (multiplayer) Fixed raft not working

* (multiplayer) Fixed all issues with log sled

* (multiplayer) Added hit prediction to mutants and other players so attacking them is more fluid

* (multiplayer) fixed bug where mutants would not appear in caves unless player was near server host

* (multiplayer) Armors will now show up on other players

* (multiplayer) Fires should now work reliably for all players

* (multiplayer) Fixed issue where players would sometime receive damage ment for someone else

* (multiplayer) Arrows can now damage other players

## v0.18b (released June 5, 2015)

* Custom buildings (experimental walls, bridges, procedural stairs, roofs, floors, foundations) now all work in multiplayer!

* Increased time until distorted mutants come out, and at first will only come out at night

* Improved enemy pacing, less chance of being found when hidden, less skinnies active in world and less patrolling enemies.

* Improved positioning on some offset pond drink triggers

* Fixed box rendering around explosives on low quality settings

* Fixed bug where anchors on foundations could cause issues and break save games!

* Fixed old plane seat models loaded after loading a saved game

* (multiplayer) Fixed bug where crocodiles would sometimes appear as other animals to client

## v0.18c (released June 10, 2015)

* (multiplayer) Bodies carried by players are now visible to other players!

* (multiplayer) Fixed client players not getting hungry, thirsty or cold

* (multiplayer) Distorted creatures will now pay attention to client players

* (multiplayer) Fixed rain not following players after respawning

* (multiplayer) Fixed player dead body sliding down slopes forever

* (multiplayer) Fixed clients not getting sticks & rocks from cancelling ghosts buildings

* (multiplayer) Fixed fire erroring when targeted by player before being attached to network system

* (multiplayer) Fixed FireStand not properly working

* (multiplayer) New Steal (or Share) feature for food items, hold any of cod/rabbit/lizard/generic meat/arm/leg and other players can grab it from you !

* Metal door now saves items on scale properly (not retro active)

* Metal door now has a trigger on the other side that completely opens the door once crossed (to fix issue if anyone saved behind it)

* Fixed rope climbing not using player input mapping

* Fixed place Timed Bomb icon being active before finding a matching surface

* Slight fill light added when holding torch (should make held items better visible in caves)

* Improved items flying up into air on spawn

* Improved pop in on some items

* New sinkhole art!

* New rocks added around sinkhole perimeter

* New modern axe art added!

* Fixed water looking bad/noisy at distance

* Fixed procedural floor having items spawning on top

* Fixed Ex Wall being offset downwards when using the auto-fill feature to place it on a Foundation + Floor, causing doors to be hard to open (not retro active)

* Fixed cold tutorial staying up when near a fire in the mountain area

* Fixed error when cancelling a ghost building that doesn't have “built” renderers for each ingredient (cancelling raft with stick and log added no longer gives infinite amount of logs ;)

* Plane wing model added!

* Fix bug where moving far away from noose trap with a mutant caught could cause it to glitch

* Fixed some issues with removing dead mutants from noose trap

* Added mourning encounters back in. Groups of mutants can be seen mourning dead family members at times

* Higher chance of seeing enemies pray/feed/mourn/place art near villages and cave entrances

* Better animation when transitioning into praying/mourning

* Further enemy balance tweaks/pacing

* Improved water trigger validation to prevent cases of swimming in random location in cave after having a lag spike when exiting water

* (audio) Lowered amount of voices played at one time to improve cpu performance/fix audio break up

* Fixed bug with raft if player attempted to ride it whilst it was flipped upside down

* Fixed player camera sometimes offset when exiting raft

* Fixed loading a saved game with a plastic torch equipped getting stuck

# v0.17 (released May 1, 2015)

* Fixed volumetric lighting not shadowing through leaves

* New low tree lod added when draw distance is High/Very High/Ultra High, increasing range before trees turn to billboards in distance

* Fixed lake and pond drink locations sometimes having icon in wrong place

* Fixed water not showing up in pot until inventory has been opened once

* Increased minimum fog distance and maximum fog distances and balanced light scattering, and increased time it takes to randomly change fog value (making things less foggy/washed out)

* Fixed beach rocks popping off too soon

* Fixed custom wall being on wrong layer and being culled too soon

* New art added: Small waterfall model

* More cliffs added/re-worked

* Improved shading on some plants

* Arms & legs can now be dried on the drying rack !

* New eye adaptation based on GPU generated histogram

* New filmic tonemapper

* Greeble Zones toggle distance now scales up accordingly with LOD ranges when Draw Distance quality setting is Very High or Ultra

* Improved greebles spawning performance and reduced pop-in

* Increased terrain mip map sharpness (won't blur as soon)

* Fixed missing normal maps on pickup items

* Fixed distant calls from mutants not audible

* Fixed/polished water vision level - now turns on correctly and smoothly

* New art added: Cave in model (used to block dead ends in caves)

* Fixed player death anim not always playing after fall

* Fixed issues with standing up again after a fall

* Fixed camera not locking correctly on player death

* Fixed weapon sometimes becoming unresponsive after heavy axe swing

* Lowered player height in water whilst swimming

* Smoothed transition between swimming and diving

* You now need to tilt camera further down to transition from swimming to diving and added more slack to system to prevent jittering between the two states

* Fixed pine tree leaf texture cut off early

* Tuned rabbit, lizard, squirrel and raccoon audio and added new lizard fast run sounds

* Increased cave ambient leak in lights, and added extra ambient lights to caves

* Less shiny/distracting tarp in inventory

* New art added: Tree stump roots (replaces old half tree log)

* Cave lighting tweaked/improved

* Improved character controller! No longer can climb up trees by jumping smoother walking over rocks, and a bunch of other small tweaks to make player feel better. Added “air control” to jumping, making it easier to make accurate jumps.

* Swimming upwards is now faster than swimming down. Added more drifty movement when swimming to feel more like being in water. Improved swim/dive speeds. Can now jump properly if in water and pressed again an object to get out.

* Tweaked drown death formula: rate & damage were reduced

* Air breathing count down now starts when water covers at least 50% of the screen

* Doubled bare air breathing capacity (without rebreather)

* Various small script optimizations (7-8% CPU freed)

* Foundations now block the player and AIs

* Fixed target missing shader

* Geese lake made deeper, and easier to swim in

* (multiplayer) collision added between players

* Added gasp for air sound effect

* New sound effect for eating poison berries added

* New sound effect added: Player drowning

* Fixed logs shaking like crazy in multiplayer

* Changed name of Level of Detail in options menu to Draw Distance

* Fixed bed using leaves instead of rope as ingredient

* Arm, leg and head now show present amount over total in ghost building ingredients (like all other ingredients)

* Added arm, leg and head to build missions

* Changed drink zones to big unique ones per water area that repositions icons based on player's position

* Can no longer drink while in water and made drinking at edge of pond/lakes easier

* New water drink poison sound effects

* Partially below terrain Foundations no longer go all the way down to the cave below and end up being very expensive

* Fixed foundations log material

* Fixed square leaf in inventory

* Fixed plants not burning away and instead popping off

* New art added: Long log hollow

* Brightened squirrels making them easier to see

* Fixed missing light and particles on held flare

* Fixed bug causing trees to flash on/off during opening cutscene

* Lowered intensity of fire light and added in new fire particle!

* Lowered throw force on molotov

* Improved look of burning tree materials

* New camp fire particle effect for regular fire and fire pit

* Fixed fire built floating above ground

* Lighter stays out now when floating in water, player holds lighter slightly higher when in this mode

* New heavy stick attack! Hold down attack with stick type weapon to do a heavy damage swing

* Object sheen now only visible if there is some ambient light hitting object (won't make cave's look like disco's)

* Improved look of cliff rocks

* Player now respawns in MP with full stamina

* Added new tree stump to beach

* Lowered chat text in MP to not overlap drop icon

* Improved lake water - lakes and ponds now have depth and box projected reflections, and better bump textures

* Fixed some small inventory glitches

* Fixed oversized sticks in some saplings when hit

* New graphics option to tweak reflections on ocean

* (multiplayer) fixed bug where boars could appear as deers on client pcs

* Fixed water & drink icon not visible in water collector

* Fixed item holder being empty when loading a saved game as host

* (multiplayer) Fixed bug where other players couldn't see light from other players lighter or flashlight.

* (multiplayer) Fixed animals sometimes moving without playing animation

## v0.17b (released May 5, 2015)

* Changed fullscreen behaviour from full screen window to exclusive mode (should provide some performance benefits)

* Fixed icons not visible for lower shelves of snack holder

* Fixed loading a game that was saved inside a cave (not retroactive)

* Slightly increased rate enemies populate world as days pass

* (multiplayer) Fixed clients not being able to add fuel (leaves/Cash) to fire

* (multiplayer) Fixed issue where clients would sometimes swim in caves

* (multiplayer) Fixed arrows shot by clients not affecting animals/enemies

# v0.16 (released April 16, 2015)

* New options menu setting ‘Render Type’ will allow you to switch between new deferred renderer (recommended for modern computers) and Legacy renderer (recommended for older computers)

* Full pbr shaders on all items. Reworked most textures to fit new lighting.

* Reflection probes added.

* New ocean shader (work in progress)

* Better bow aiming - sight added to bow. bow tracks better with camera view when aiming up and down. Looks better now when viewed by another player

* Animals will now attempt to dodge trees, obstacles and other animals

* Fixed rebreather's air resetting to 0 after loading a saved game

* **(Multiplayer)** Reworked the network prioritization algorithm to provide more relevant updates of remote entities to players (Smoother, less jittery enemies)

* Upgrade balance: Inverted bonus curve, it now goes from small (10%) to big (100%)

* Fixed booze upgrades still not showing up for some weapons

* Added a small outline to chat text to make it visible in bright lighting conditions

* Fixed issue preventing to lock floors/roofs on multiple walls on the same height level

* Grabber system now turned off when in in inventory/book/pause menu or while placing a building (i.e., placing a building near water will no longer trigger drinking)

* New snapping grid gizmo to help with manual placing of experimental floors & roofs (tip shows the current lock position and is big enough to be seen from either side of a wall)

* Experimental Roofs now snap back to closest edge on current support (i.e. the wall you're putting it on)

* Goose simulator added. Geese will now fly between lakes and swim around acting like geese

* Fixed Bon Fire not lightable

* Fixed flying food on rock fire pit

* Fixed burn lizard scale

* Added generic meat burnt

* Fixed drying generic meat

* Fixed Treehouse + Treehouse Chalet floor not buildable

* Deer will now drink at lakes

* Fixed issue where deer would run right through trees!

* Dead birds now have a chance of spawning feathers when hit

* Revamped cooking to allow eating burnt food but with far lesser gain

* Player will now see himself briefly dragged away into a cave when knocked out but not killed.

* New art added: Improved airline foodcart

* Fixed bug where climbing rope for first time would sometimes cause it to release right after climbing

* New trees! New bark and leaf types.

* New billboard system with lit billboards and rotation

* Unity 5 reflection probe system added

* New clouds/sky

* All shaders switched to use new unity pbr

* Dirtied up and improved regular enemy textures

* New pbr skin shader!

* In game controls remapping, both in Title & Main scene options

* Falling particle leaves now accumulate on ground

* Fixed logs flying up into air when trees were cut

* Fixed physics on some trees not colliding with terrain when falling

* New art added: dead small trunk

* Graphics options: added rendering patch selection

* Graphics options: added new setting to turn off sunshine occlusion

* Graphics options: added new setting to tune Level of Detail

* Graphics options: SSAO setting now also changes sample count

* Graphics Settings now properly show the saved preset name after restarting the game

* Graphics Settings: Renamed “Laptop” level to “Ultra Low”

* Fixed survival book entries not clickable on occasion

* New art added: new version of plane food! plane tray, styrofoam cups and trays

* New bushes - replaced 2 of the worst looking bushes with new type

* New lake shader added! reflective and with murkiness

* New dead trees! Better textures and models, and now all cuttable!

* Better shark ragdoll

* Jump animation added to player

* New combat move - Flying axe attack. Attack downwards with axe while jumping to perform a powerful ground chop.

* When falling from high up, player will briefly stumble to his hands and knees

* You can now cook arms and legs (and ... eat them - but you probably shouldn't)

* Dead trees replaced and now cuttable!

* New log type for buildings that matches carried log

* **(audio)** New player sounds!

* **(audio)** New female skinny audio!

* New blueberry bushes!

* New multiplayer octree based priority calculation

* New art: Re-done plane seats

* Fish and sharks are now also in multiplayer games!

* Touch bending grass added! enemies, rabbits, animals and player will now slightly rustle the grass as they move through it (this is a first pass at this, next version will include better bending)

* You can now climb fishing stands

* Experimental Walls now block AIs (mutant & animals) from going through it

* Fixed fire particles staying up after cutting down a burning tree

* New world art: cliff wall variations.

* Lighter now stays equipped when exiting/entering ropes

* Added some additional optimizations and memory tweaks for 32bit machines that have less than 4gigs of usable ram

* Fixed molotov fire never shutting down

## v0.16b (released April 17, 2015)

* Fixed bug where all volumetric lighting would turn off if windows 32bit was detected

* Fixed water blur vision not turning on when player goes underwater (still a bit buggy in waves, but should work well again in flat water)

* Fixed bug where cave props could stream into scene multiple times if you quickly went in/out of a cave

* Fixed sparkly disco looking cave floors if bloom was enabled

* Fixed rock type in cave with no textures

* Increased grass draw distance at highest settings

* Set high preset to use ‘very high’ level of detail setting (lower this to high or medium if you find it impacts performance)

# v0.15 (released March 17, 2015)

* Fixed bug where raft would no longer float

* Fixed bug where arm effigy wouldn't be lightable

* Lowered damage drinking polluted water does to players

* Added hint text to dying screen about finding pots at camp sites

* Added sheen highlight to pot pickup to make it easier to find

* Turtle Shell now fits in backpack !

* Holding pot while it rains now fills it with water

* Enemy bodies can now be transported via the log holder! (SP only)

* Fixed bug where player could sometimes climb down rope out of world if tree house was placed on a slope

* Spider lady a.i. improvements and additional animations added. Now has more attacks, can jump attack, can dodge players. Will react to explosions and can be killed with 2-3 bombs now.

* Fixed FMOD bug that would cause memory to climb up over time

* Animal footstep sound effects added!

* Fixed held plane axe upgrade visuals positioning

* Fixed booze upgrade visuals

* Fixed loading upgrades from saved games (not retro-active)

* There is now a limit to the total amount of upgrades per item (currently set to 30 for all weapons. You can choose to have either 30 teeth or 10 teeth + 20 Feathers, or 10 teeth + 10 Feathers + 10 booze etc.)

* Visual added to show item upgrades distribution when crafting upgrade recipes

* Bonus per upgrade now decays as you use a single upgrade type

* Dying no longer resets fullness to zero

* Collision fixes/improvements for caves

* New item/weapon added: Climbing axe! (check caves!)

* New climbable (with climbing axe) cliff rock added to overworld (currently limited to only 1 type of cliff rock)

* New climbable area added to cave 2

* Fixed bugs that would sometimes cause log sled to fall through world. log sled should now collide with boulders and cliffs. Fixed log sled audio playing drop noise when in its trigger or being pushed. Log sled now casts a shadow

* New art added: Hanging skull lamp

* New art added: Skull floor pile

* New art added: terrified skeletons (check deep caves)

* New art added: (removed\*SPOILER\* - Check deep caves)

* New art added: Eerie tribal fishing stands

* New art added: Cannibal village props (small cages, fire pits)

* **(multiplayer)** Fixed sitting on bench not lining up correctly

* Tree sap, skulls, blue and orange paints are now part of the construction system

* New buildable item: Skull lamp

* New buildable item: Deer Skin Decoration (as floor carpet or hanging on walls)

* New buildable item: Skull wall Decoration

* New buildable item: Arrow Target - shoot arrows and improve your aim!

* New buildable item: Bed! build inside a custom building to allow saving and sleeping

* New system added (rough) Player point at map. When holding map in cave player will point to his current rough location

* When the game is already started and an MP invite arrives, player can now choose to either start a new game or continue with his saved MP character

* Drowning now causes instant death, without respawn in cave

* Fixed underwater bar appearing before character's head is underwater

* Fixed hydration icon fill values not set properly after loading a saved game at full thirst

* Player can now suffer brief knock down and damage from explosions

* Bow and arrow improvements! will no longer fly through enemies without damaging them. Arrows now stick in trees and other static objects correctly. Arrow pick up icon added and better positioning, and will now turn on pick up trigger when it sticks to any object

* **(multiplayer)** Water Collector now works for clients in MP games

* **(multiplayer)** Fixed infinite item/log from holder buildings in MP

* **(multiplayer)** Fixed bug where Sometimes when someone else completes a build, it says it still needs materials, then just eats the materials.

* **(multiplayer)** Fixed issues with some built buildings not working correctly for all players.

* **(multiplayer)** Fixed bug where clients could be kicked from host after 5–10 minutes

* **(multiplayer)** Fixed bug where after being kicked out by the server, every single door placed in world would duplicate

* **(multiplayer)** Fixed bug where items from cabinet/racks/shelves could vanish when host ends session, at random, or on loading the game.

* Dead bodies around world no longer respawn after being picked up/moved when moving back near them

* New creature added: Wild pig!

## v0.15b (released March 18, 2015)

* Lowered amount of boar in world

* Boar ragdolls now correctly turn off after time

* Killing an animal causes a delay before animal is respawned into world

* Additional visual/performance optimizations to deer and boar ragdolls

* Fixed bug where dying from drowning would be instant instead of gradual

# v0.14 (released February 25, 2015)

* **(Custom Building)** Procedural foundations now auto fill with experimental floor making structures simpler to build.

* **(Custom Building)** Added valid angle & distance gizmo to Foundations, Floors, Walls and Roofs

* **(Custom Building)** Added option to auto fill points of walls, and roofs from in snapping range (press C)

* **(Custom Building)** Added no wall option to experimental walls segment rotation

* **(Custom Building)** New buildable item: Experimental Roof! Once placed aim upwards to select height. This means it is now possible to build complete structures!

* Reduced log cost of foundations for all buildings

* Added monitoring system to alert players if their save game has been corrupted beyond repair

* Save script now uses the grabber system (adding items to item holder next to a shelter no longer saves the game unexpectedly)

* Fix for vanishing items in weapon/explosive rack when picking up items while already having the max amount

* Fixed white log with missing texture in world

* Fixed bug where breaking apart coneflower would spawn a broken chicory plant

* Cave stalagmites now have collision

* Lethal starvation system! Be aware of your food supplies as staying hungry too long will eventually cause you harm.

* Lethal thirst system! Stay hydrated and healthy by finding a clear water source every day, failing this may result in death.

* Lethal frost system! Cold will now eventually kill you. When you feel yourself shaking and the screen frosting over, build a fire!

* New buildable item: Rain Water collector. Requires 4 sticks, 1 turtle shell.

* New item: Carryable pot. Found at campsites around world. Can be used to boil dirty water.

* Can now drink at ponds and lakes. Ponds can be polluted and thus require water to be boiled.

* Blue berries now give small amount of water

* Fixed bug that would block an explosive holder slot when attempting to place a small rock/tennis ball on it

* Fixed bug that caused the full screen to turn frozen after having a lag spike or pressing alt-tab while being cold

* **(audio)** Added timeout before re-triggering ‘Sighted by enemy’ sfx to avoid issue where it's called dozens of times in a row as new enemies see you

* **(audio)** Startle, hit and die sounds added for deer, rabbits, raccoons and squirrels

* **(audio)** Advanced tree wind effect added! Tree leaves will rustle as you move past them.

* Fov slider added to options menu!

* Dead mutants will sometimes have loot (meds, chocolate bars, soda)

* Fixed bug where explosives wouldn't affect distorted enemies

* Rope trap now requires rope to construct

* Improved regular mutant reactions to explosions

* Increased inventory bomb carry limit to 5

* New buildable item: Trip wire explosive!

* Survival book traps pages reorganization. New small traps section (moved rabbit trap here, and renamed to ‘animal trap’ Food section in book renamed to Food and Water and water collector moved to old position of rabbit trap.

* Home & yellow hammer overlay icons now disabled while in caves

* Added option to always disable home & yellow hammer overlay icons to options menu

* Any object that can't be stashed now has G to Drop hint

* **(multiplayer)** Fixed issue where lizard armor wouldn't show up for other players

* **(multiplayer)** Fixed player climb rope animation not showing for other players

* **(multiplayer)** Fixed Log sled position and contents not syncing correctly

* **(multiplayer)** Fixed bug where after time passes player avatar moves away from actual player location, while players name stays with players true location.

* **(multiplayer)** Fixed Issue with screen re-positioning and orientation bugs that could occur after time

* **(multiplayer)** Fixed walls disappearing after too many placed

* Enemies will now switch to a burnt material when set on fire

* New item added: Rebreather! Equip to dive underwater (there are several hidden throughout world)

* New recipe added: Waterskin, 2x deer skin, 1 x rope

* Bombs will now also explode dead bodies

* Optimized fish a.i. and fixed some instances of no fish appearing in ponds

* all animals can be killed with explosives now

* Player can now swim underwater for a brief period of time (look for rebreather to swim underwater longer)

* New item added: Turtle shell! Can be taken from killed beach turtles. May be used in crafting structures or as a makeshift shield to block attacks! (or even as a weapon)

* Turtles now provide 2 delicious pieces of generic meat

* Improved various bugs with noose trap

* Fixed issue that would eventually cause a massive lag after burning trees down

* Optimized a bunch of physics objects over time. Should fix general performance slow down after cutting down hundreds of trees and plants.

* Optimized billboard script to improve cpu usage by roughly 10%

* Improved cave physics use - which was causing some major performance issues even outside caves.

* Optimized work scheduler to reduce lag spikes in greeble intensive areas (areas with large concentration of ferns)

* Timer on title screen switches to yellow text that reads NEW PATCH RELEASING TODAY when time runs out (just in case we miss deadline by a few hours like last patch)

# v0.13 (released February 11th, 2015)

* Armsy combat improvements - can now turn around quickly, attack to left and right and attack from further away. Will swipe at trees more often. Will react to explosions by staggering backwards.

* Armsy will knock down walls and other structures near player, and will now interact better with dynamic logs/props pushing them away

* Lowered throw force on bomb timed and added friction to rigidbody to reduce hockey puck feel

* Added distance based camera shake when bombs explode!

* Improved look of wood plank barriers - better textures, better break apart chunks

* Wooden planks now have a health value and will take longer to be broken down by a stick versus an axe

* **(multiplayer)** Added two new player character model variations

* **(optimization)** Improved Experimental Foundations & Walls memory footprint

* **(building)** Removed Manual Foundations 4 edges limit, improved visual feedback

* **(building)** Added closure snapping to manual foundations

* Improved log sled pushing - less jitter and glitches when pushing sled close to other objects

* Changed gazebo floor collider so items can be built on top of it.

* Player can no longer jump while pushing the sled

* Lowered damage from un-upgraded rock weapon

* Added extra checks to stop player falling through world when climbing ropes

* Lowered damage amount molotovs do to Armsy. Setting Armsy on fire will cause him to become enraged, running around or attacking the player

* New dying sound distortion added when player is in grey-zone state

* **(audio)** rope climbing sound effects added

* **(audio)** Falling Leaves sound effects added and tuned

* **(audio)** Fixed bug where bush rustle sound effect would sometimes not play if player was running full speed and at an angle

* Fixed a rare bug that caused the game to get stuck halfway in the loading process

* Fixed trees initializing after black screen removal when loading a saved game

* Slightly larger hit colliders on birds and stick weapon, makes it easier to kill grounded birds with a stick

* Enemy bodies no longer explode when you hit the body after killing them! You can now chop off individual limbs!

* Tree houses now require rope to build

* Cave 2 crayon map drawing with shiny sticker stars on it added as a collectible item. (hint: try and find locations of stars)

* **(audio)** Music sting added when player is woken up by enemies

* **(audio)** New music sting added when an important item or location is discovered

* **(audio)** First pass at Skinny enemy audio added

* Fixed log wall breaking apart rotated incorrectly

* Cave 1 - major design re-work. More interesting areas, easier to navigate, more secret areas and items, improved collision.

* Player is no longer able to pick up logs while jumping, swimming, sailing raft or pushing sled

* Equipped logs are now dropped when beginning to swim, sail a raft or push a sled

* Standard enemies can now attack built player walls

* **(hopefully)** Fixed bug where enemies would sometime appear in t-pose in multiplayer games

* Improved cave 2 entrance visuals

* Random hint texts added to dead screen!

* Removed starfish from caves and other strange places. Will now only appear on beach.

* **(multiplayer)** New voice chat system! Using microphones/walkie talkies will no longer cause memory allocation and framerate stutters as memory is attempted to be cleaned out.

* **(multiplayer)** Performance improvements!

* **(multiplayer)** Fixed delay where log would remain visible for a short period of time even after being picked up by clients

* **(multiplayer)** Fixed delay between tree falling and breaking into logs for clients

* **(multiplayer)** Craft audio now plays for each player, you should no longer hear other players craft sfx play from far away

* **(multiplayer)** fix a bunch more 2d sounds that could be heard by both players at wrong time

* **(multiplayer)** Major lag improvements for enemies! Enemies will now visually update more often when close to a player

* **(multiplayer)** Fixed fires not replicating

* **(multiplayer)** All enemy types now show up in multiplayer games (distorted, pale creatures etc.)

* Fixed missing collision on orange tents

* Fixed issues where after climbing rope, it would slightly reposition player making it very easy to fall back into hole or off ledge

* New buildable item: Weapon Rack! Store up to 4 non projectile equipment items

* New buildable item: Snack holder

* New buildable item: Explosives/molotov holder

* New buildable item: Medicine cabinet

* Fixed flare gun not setting enemies on fire

* Getting hit while blocking now drains more stamina

* Block will fail now when hit if you have very low stamina

* Birds are no longer active while inside a cave

* Optimized all animal animators to save cpu performance

* **(single player only)** New buildable item: Climbing Rope (needs to be hooked to a single Structure Anchor, a minimum distance with floor is required)

* Added Structure Anchors to: Gazebo (2), Log Cabin (2), Platform (2), Extensible Platform (4), StairCase (2) and Wall (2) [retro-active] **(you can now attach bridges or rope to these items)** **(Single player only)**

* New cheat code added: ‘vegetarianmode’ enemies only come out at night.

* New cheat code added: ‘meatmode’ cancels the other cheats

* Active cheats now saved locally (Hint: Type meatmode on title screen to cancel active cheats)

* **(single player only)** New buildable item: (experimental) Procedural Floor (snap on top of foundations, or to procedural walls that are on foundation + floors)

* Can now rotate tree structures while placing them !

* Improved building placement near structures that can be built upon

## v0.13b (released February 12th, 2015)

* Fix for broken saved games

(dark shadows, no time passing, sleeping at shelters broken and lots of other bugs in corrupt save games, along with low performance due to error spam)

# v0.12 (released January 15th, 2015)

* Steam multiplayer! No more manual ip entering or having to open ports! You can now invite friends to play and they can easily join your game through steam!

* MP Client loading added – will now keep client player stats and inventory when client continues a multiplayer game (buildings are still saved on server)

* Improved craft item multiview placement on crafting mat

* New item added: Rabbit skin

* New item added: Rabbit Pouch (can be crafted with 2 rabbit skins)

* New items added: Collectable blueberries, snowberries and twinberries (approach bushes whilst holding rabbit pouch to collect)

* New item added: Blue Paint (can be crafted by combining 2x blueberries with tree sap)

* New item added: Orange Paint (can be crafted by combining 2x Marigold with tree sap)

* New upgrade recipes: Stick/Upgraded Stick + Blue/Orange paint

* New upgrade recipes: Rock/Upgraded Rock + Blue/Orange paint

* New upgrade recipes: Plane Axe + Blue/Orange paint

* New upgrade recipe: LizardSkin + tree sap + 15 Leaves = Stealth armour!

* **(audio)** New leaf wind rustle and ambient wind sounds zones added

* **(performance)** Optimized collision on cave wall chunks

* **(performance)** Added some optimizations to distant enemies, disabling physics checks etc.

* **(performance)** Improved material memory usage in inventory

* **(performance)** Improved memory usage over time

* Added some small streams to world

* Entering water in caves will now make player cold. **(Hint: Build a fire to warm up)**

* Entering water at night will also make players cold

* **(audio)** New cave 2 waterfall sounds added

* Fixed cassette player overlapping pedometer in inventory making it unselectable

* Fixed tree houses not falling when tree is cut down after loading

* Fixed bug where you could build structures in trees which already have something built

* Fixed crash clearing not removing trees on loading a save game (fixing issue where trees would sometimes block exit from plane or from home you've built near crash site)

* Fixed bug that caused inventory to stay up when dying while in inventory

* Fixed bug that allowed players to craft items for free after closing inventory while having a valid recipe ready on the crafting mat

* Fixed missing material cave dead ground

* Fixed energy mix inventory info

* Fixed generic meat floating above fire

* Fixed some a.i. issues where enemies would find players almost instantly

* Fixed bug where building would sometimes break near standing fires

* Rock and stick pickups added to caves, along with some new body parts

* Crafting progress bar! You can now see if the items you are adding to the crafting mat are building towards something.

* Crafting recipe output images! You can now see what item you are building towards on crafting mat

* Fixed overbright moon

* Enemies will now attempt to jump over small player built items (benches etc.) instead of getting stuck

* Cave 2 – added sky opening to big lake room letting some light in

* Tree attack animations added to armsy

* Mid and close trees can now be torn up by armsy

* **(multiplayer)** After being downed in a multiplayer game, player will enter an injured state. In this state they can choose to restart, or wait to be revived by another player. A kind player with medicine can approach downed player and heal them, or a mean player can hit them with a stick.

* **(multiplayer)** Days survived screen will appear for a few seconds after players are killed and before they can respawn.

* Balanced enemy amounts at night to limit players being swarmed by 15 enemies at a time

* **(multiplayer)** First bash at performance improvements.

* Increased range animals will spawn from player to avoid pop-in

* Fixed some bugs with enemy pathfinding

* Added a repeat delay for enemies spotting player and screaming

* Increased vision range on enemies slightly

* Fixed bug where placing a building near a fallen log could break the placement orientation

* **(multiplayer)** Fixed bug where fire would appear overbright for other players who didn't start fire

* **(multiplayer)** Increased chat log visibility length and history

* WalkyTalky locking feature removed (can now equip another utility item without stashing it first)

* **(audio)** Fixed missing underwater sounds

* **(audio)** Fixed bunch of 2d sounds which could be heard in multiplayer by both players **(hammer audio, enter water etc.)**

* **(Multiplayer)** Can no longer have more than one set of corpse items waiting to be retrieved. Dying will cause your current items and location to be the corpse items.

* **(audio)** cave rock sound will now correctly play when walking in caves

* Added more stick, rock and cash pickups to caves

* Fixed bug where opening inventory would sometimes give you a black screen!!!

* **(audio)** Player jump breath and land sound effects added

* Fixed bug where killing leader of a group could sometimes cause the other members to stand around corpse doing nothing

* Toy robot added to sleeping timmy hand

* Broken toy pickups added to world, along with new examine item animation

* Paper money can now be used in place of leaves to start fires

* Paper money can now be found in some suitcases

* You can now build structures inside caves (although fires are most practical)

# v0.11 (released December 17th, 2014)

* New buildable item : Experimental walls! (single player)

* New buildable item : Custom foundations! (single player)

* Multiplayer save/load added Note : Currently limited to server being able to load the savegame, clients will start game fresh each time but still be able to enter a previously saved hosts game. Server/host will be able to save state of game world/structures.

* Steamworks saving to cloud added - Regular save/load still works however it will now try and load from cloud first and pick most recent file (We’ve just hit the checkbox to enable this, it should be available soon)

* Improved bridge snapping to be more responsive and less chance of it snapping to wrong position and improved visual feedback

* Fixed wooden path blueprint not saving

* You can now use the walkman as a distraction device. Stick it to a tree, confuse your enemies! Attach to a trap and lure them to it.

* Re-worked title screen and cleaned up button animations

* New options menu, with more organized layout

* Added grass density slider to options menu - newer graphics cards can turn this up for better looking grass.

* Player can now attack whilst crouched improving stealth kills

* New animal added : Squirrels

* Fixed bug where some animals wouldn't show up

* Improved look of ponds

* deer now have more health and will attempt to flee if you hit them

* Killing deer will now attract skinny mutants who may attempt to feed on the carcass

* Skin from deer can now be collected and worn

* deer skin will keep players warm if worn, can mix/match lizard Skin and deer skin

* New item added : Generic meat (can be sourced from deer or raccoons)

* New item added : wrist watch (can be found in luggage, or on some dead passengers) - use as crafting ingredient (such as on timed explosive)

* Changed recipe for timed explosive to include watch

* Audio - new cave sound effects added

* Audio - Improved cave ambient audio fade out zones

* Audio - Fixed audio slider in options menu not working correctly

* Audio - Reverb added to cave sound effects

* Audio - All sound effects now fade out on player death

* Audio - Tuned levels of weapons, footsteps

* Audio - Made frog sounds quieter,less frequent and less annoying

* Audio - Lowered chance to cave combat music playing

* Audio - Fixed suitcase open sound using flesh hit sound effect

* Skinny enemies - increased speed, added in some missing animations. Increased health slightly. Will now travel in groups of up to 3 making them more of a threat.

* Pale cave enemies faster, more health and increased hit damage

* Improved geese lake layout, new rocks and details

* New ground textures! - improved parallax mapping, and better blending - switch to relief or lower if there's any slow down with this (via options menu)

* New rock detail textures added to most rocks

* New pine tree and pine tree moss textures and improved look of (some) dead trees

* Major re-work of cave2 environment, more interesting rooms, better layout of rocks, new rock types and better flow through areas. Added small water falls

* Armsy will now sometimes tear down trees

* Reduced chance that regular cannibals will flee after player kills one of their group

* Fixed skinny cannibals sometimes having leader props on dead body

* Fixed some instances of enemies stuck not doing anything

* Fixed bug where player would have issues climbing rope if cold and shaking

* Fixed log duplication bug, where it was possible to spawn multiple logs when picking up up a log (multiplayer)

* Fixed issue where you couldn't pick up rabbits. You can now take rabbits out of traps or out of cages.

## v0.11a (released December 18th, 2014)

* Fixed issue where cave reverb would continue to distort sounds after dying and starting a new game

* Fixed issue where fire sounds wouldn't fade off correctly

## v0.11c (released December 20th, 2014)

* Fixed error with multiplayer save games sometimes breaking due to racing condition with data fetching in gui.

* Fixed issues with traps (noose, spiked wall, happy birthday) not being buildable in multiplayer games.

* Fixed some issues with single and multiplayer save games when a large amount of buildings were built.

# v0.10 (released December 1st, 2014)

* Platforms! Place the log cabin on a slope and procedural platform will be constructed underneath to give it support. No more cabins on side of hills.

* New buildable item: Tree platforms!

* Building height system added Look up to place structures higher (using procedural foundation system) or downwards to place on ground (as in old system)

* Climbing system! Player can now climb rope

* Removed steps from tree houses! Replaced with climbable hanging ropes.

* Added clamp to tonemapper to stop it sometimes turning screen completely black if seeing a very bright pixel. Fixed related issue where bloom would sometimes cause screen to turn black if it found overbright pixels.

* Fixed issue with plastic torch spamming errors, causing a performance drain when using torch light source

* Tweaks to world lighting and fog/ambient colors. Lighter and plastic torch now cast shadows.

* Tweaked enemy density in caves

* Added option to turn off all hud elements in options menu (not recommended!)

* Increased size of rabbit on fire to match world scale

* Small performance optimization on cpu by removing OnGui calls

* Meds will now be auto consumed if health below 20 when picked up

* **(single player only bug)** Fix for pine tree top heavy not being cuttable

* Fixed missing marigold and chicory plants

* Improved ambient audio zones and fixed outside sounds continuing to play when inside a cave

* Improved cave audio ambience

* Lizards can now be caught in cages along with rabbits (and raccoons)

* Fire Arrows! Press L with bow equipped and at least 1 piece of cloth in inventory

* New falling leaf particles (3x) added and improved look of leaf burst (less bright/unlit)

* New fluff particles added and using a new dust shader (bright in light, dark in shadow particle shader)

* Improved look of torch light - now two tone

* Fixed overbright lights on mutant creepy's fires and all bombs/held bombs and better balance on bomb explosion particles

* Balance pass on all mutant textures, improved look of skin and put all into same texture value space

* New improved blood particles!

* Fixed issues with sticky bombs

* Fixed enemy skin and player arms sometimes losing ability to receive shadow and appearing overbright

* Fixed molotovs not exploding on impacting enemies

* Improved transition from cannibal village hole to caves using new generic rock chunks

* Log holder is now pushable using push and hold animations

* Fixed audio issue where some sounds would fade out instantly/abruptly

* New suitcase art (6 textures variations, 2 model variations) added!

* Fixed missing mesh renderer at front of plane crash(animated forward hull)

* Animated passengers added to plane crash! - Don't skip crash!

* Fixed dead lizard normals flipped causing ragdoll to look different than regular model

* Improved look of small shelter (better rocks, better log renders etc.)

* Lighter will always light after a limited amount of attempts (was previously possible to attempt to light 20 plus times if unlucky)

* Fixed lighter animation playing continuously when stashing lighter quickly after getting it out

* Improved held item switching sequence (better use of existing animations)

* Pale enemies no longer attack each other or the distorted creatures

* Removed cave beach entrances -replaced with rope climb out areas in lower caves fixing issues with entering caves near ocean

* New molotov weapon art

* Fixed lighter flame being too small visually

* Fixed flare gun making shooting sound when fired without flares (will now make an empty click sound)

* Improved tree falling sound settings

* Swimming sound effects added!

* Tuned/balanced pick up sound effects, eating sound effects etc.

* Enemies will now always prioritize visible players over other enemies in combat

* Improved instances of small items pushing player and added max velocity to attempt to stop player flying up into sky

* (multiplayer) fixed bug where some shadows would break/change after respawning

* Improved some environment art, started implementing better cliffs in some areas and higher detail rocks. Added new lake zone.

* New art for (some) cave stalagmites and stalactites

* **(hopeful fix)** for players sometimes swimming even when not in water area

* Player will now stash weapon when swimming!

* New creature added! - Check the caves.

* Delay added to combat music so it won't continuously trigger when entering in/out of combat

* (multiplayer) Walkie talkies added! Press Q to communicate in multiplayer games.

* (multiplayer) Fixed issue where items needed would sometimes stay on screen depending on if client/server destroyed a blueprint

* (multiplayer) Fixed issue where returning to start menu would break game and turned back option in menu

* (multiplayer) Fixed Enemies not showing blood particle fx on clients when they are hit.

* (multiplayer) default player cap increased to 8 along with option to go up to 128 players (for adventurous players only! not recommended)

* (multiplayer) Fixed Suitcases not being replicated over the network and existing only locally for each player

* (multiplayer) Fixed Mutant ragdolls not replicated properly on client

* (multiplayer) Fixed Wall built in MP vanishing instead of turning into logs when destroyed

* (multiplayer) Fixed issue where remote players would not alert enemies via sound detection

* (multiplayer) Lizard skin player armor now visible by both client/host

* (multiplayer) Fix for overlapping chat text

* (multiplayer) Fixed some Log duplication bugs

* (multiplayer) Fixed Logs invisible for client in certain spots on the map

* (multiplayer) Fixed issue where only newly built effigies would only be seen by host

* (multiplayer) Fixed client/host sometimes having differently positioned yacht location

* New art added for some of the cave entrances

* Re-worked save game system so future updates will (likely) not erase save games to work!

* Fixed issue with weapon upgrades have no or very little effect

* Improved animal spawning in world- less chance of dead zones where no animals ever show up.

# v0.09 (released November 11th, 2014)

* Slowed down tennis ball throw massively so players can play catch together on beach

* (multiplayer) Server configuration screen - This will automatically tell you your public ip address - This is temp, server browser or better Steam integration coming soon!

* (multiplayer) Chat box - Press enter to type messages to each other - This is temp and may be buggy!! Voice chat is coming soon! (we’re modeling walkie-talkies)

* (multiplayer) Player texture variation, run around with your survivalist buddy!

* (multiplayer) First pass at player respawn system, on dead try and find way back to body to collect your belongings

* Fixed bug where building a bench could cause save games to break

* Fixed female skin being too dark

* Rest of skinny animation variations added

Known issues:

* Saving in a multiplayer game will save over single player save game, allowing you to continue progress but not as a multiplayer game (working on fix for this currently)

* Destroying partially built items can be glitchy! Try not to destroy structures you haven't placed yourself!

## v0.09b (released November 11th 2014)

* (multiplayer) Fixed bug where building a Bonfire/Standing Fire/Fire Pit could cause game to crash

* (multiplayer) Fixed bug where traps wouldn't reset correctly (rabbit trap, 3 enemy trap types)

* (multiplayer) Fixed bug where destroying blueprint/ghosts could cause client or server to be kicked from game

* (multiplayer) Fixed bug where rock holder/log holder/log sled use/construction could cause clients to be kicked from game

* (multiplayer) Fixed bug where if Host alt-tabbed out of game client would be kicked almost instantly

* (multiplayer) Fixed bug where having max rabbits or lizards in inventory and trying to pick more up could cause client to be kicked from game

* (multiplayer) Fixed bug where molotov could crash/kick players from game

* (multiplayer) Hopefully fixed issue where client/server pc camera would intermittently turn completely black - this one is hard to track down, let us know if still occurring.

* (multiplayer) Fixed missing enemy sound effects for client player (may still not appear in some cases if client is very far away from server player)

* (multiplayer) Fixed issue where picking up a fish would destroy player and crash server

# v0.08 (released October 8th, 2014)

* First pass at infinite weapon upgrading! use collected items to upgrade your weapons. Use teeth, feathers and glass shards to improve weapon speed and damage.

* First pass at Cloth/fire upgrading system added - add cloth to your weapons and set them alight

* Stealth gameplay! Lowered vision range on enemies and gave them a smaller cone of vision.

* Bushes will now hide player from enemy vision when crouched!

* Player now less visible to enemies at night - unless lighter is out, making him more visible.

* Covered in Mud will now correctly conceal player making him harder to spot by enemies.

* Lowered range that enemies can hear player when walking/running

* Stealth kills added! If player attacks an enemy from behind with rock or axe type weapon and enemy is unaware of player it will be an instant kill

* Enemies will bash away bushes looking for player when hidden from them

* New cave explorer model added to cave (hanging)

* New cave explorer model added (crushed)

* Better death theme (less grating)

* High detailed plane doors added

* Better looking log held model

* Improved building memory usage

* Improved HUD memory usage

* Heads can now be cooked on fires to create skulls

* New pick up item added: Skull

* New craftable item : Club (skull plus stick)

* You can now pick up and use enemy clubs

* Picking up items in quick succession will now display a number for how many were collected

* All collected items now have message appear

* Improved previous weapon switching system to be more reliable

* New buildable item: Chalet Style Treehouse

* New buildable item: Meat drying rack

* New buildable item: Bonfire

* New buildable item: WalkWay

* New buildable item: Small animal trap!!

* New buildable item: Gazebo

* New buildable item: Defensive spike barrier

* New art for body stumps (decapitated head, leg, arms)

* Cannibals eating dead bodies now takes longer

* Chicory and coneflower plants are now collectable

* New Craftable item: Energy mix (chicory plus coneflower)

* Eating Coneflower will restore a small amount of health

* Eating Chicory will restore a small amount of energy

* Raccoon group behaviours added

* New raccoon animations added, walk, trot, improved idling, overall raccoon animation speed increased

* New craftable item: Headbomb (head plus bomb)

* Fixed door on medium cabin

* New animal added: Deer! Deer will turn towards approaching player, eat grass, run away from player and more

* New crafted axe model

* Crafted axe now requires rope to build (Rock,Stick, Rope)

* Improved motion blur quality,stability and memory usage

* Fur! Raccoons and rabbits now have fur shading

* Improved look of lizard armor

* Improved bird reactions to player, should fly away when you approach

* Increased fog ranges

* Reduced clipping of player arm in body when looking down at self

* Removed deeper cave dead positions. Waking up in cave will now always be reasonably close to surface

* New detailed rope model added, along with new curled rope pick up prefab

* Tweaked pacing of daytime enemies

* Less blue enemies in upper parts of caves

* New lizard skin inventory model (replacing scaled lizard mesh)

* New inventory item : Tree sap! can be collected from trees, can be used in weapon upgrading/crafting

* New tooth model and texture

* Improved pickup system. Will now pick up closest item you are looking at

* Increased chance of meds and torches in suitcases, lowered chance of tennis balls.

* Improved look of alpha selected items in inventory(feather, herbs)

* Torch now displays amount of charge left in inventory tooltip

* Inventory herb models replaced with more realistic versions

* Fixed issue where weapons would swing a second time if you clicked again during early part of swing

* Randomized size of animals

* Cave lakes, collision,lighting and layout improvements

* Added more randomness to plane crash possible locations

* Flashlight no longer auto equips on pick up, needs to be manually selected from inventory

* You can no longer pick up rabbits, you need to catch them in trap first

*Note: Due to changes with how saving works on some items old saved games will no longer work with this version.*

## v0.08b (released October 23th, 2014)

* FMOD audio support added.

* New tree fall and break apart sound effects! fall sound will now play until tree connects with terrain

* New ambient sound effects mix and implementation

* New improved footstep sounds. Running footsteps sounds added. Sand and water depth footsteps. Carpet sounds when in plane

* Raccoons can now climb trees

* New art added, cave explorer bloated

* New art for red plane axe

* New art for crafted timed bomb

* Massively optimized 3d roots model

* Improved collision on gazebo and added in grass cutting to prefab

* Fixed missing collision on spiked defence structure

* Fixed small shelter and gazebo collision not blocking enemy vision

* Energy now drains faster when carrying logs (and faster still if carrying two logs)

* Added bloom option to graphics menu (turning off will improve GPU performance on slower cards)

* Fixed overbright small uncuttable plant

* Items now spin around as upgrade are applied!

* Fixed issue where new upgrades wouldn't appear after loading a saved game

* Fixed timing issues with lighter and walkman stash anims (items would disappear before the hand was off screen)

* Big sapling is now cuttable and collision no longer blocks player movement

* Fixed music in plane sequence off by a few seconds

* Optimized deer model

* Attack improvements : less chance of double swinging when attacking ground with axe. Axe attack at ground will switch to forward attack if player looks up whilst attacking.

* Fixed bug where flare gun would stop working after you put it away/load game

* Fixed body parts rolling (only decapitated heads will roll now)

* Fixed some player stats not being set on load save game (lizard armor, hunger etc.)

* Fixed fish cooking instantly on drying rack

* Improved collision on custom wall piece with window (you can now shoot arrows through window)

* Fixed bug where you could fall through ocean or lake onto dry ground below

* Improved lake swim zones

* Skinny enemy unique animations added!

* Improved physics on small rocks thrown

* Fixed (hopefully) player thrown into air after chopping dead enemy up

* Fixed sprung rabbit traps not resettable after loading a game

* Thrown rocks and tennis balls can now be used to distract enemies. Hitting trees with items will cause noise that enemies can hear.

* Thrown flares will now attract enemies to them, and improved feel of throw

* Cliffs and large rocks will now block building structures instead of letting you build the items underneath them

* Fixed small cabin door and custom wall door getting stuck in terrain

* Axe added to blocked cave room

* Fixed bug that was stopping raft from being buildable via book

* Fixed bug where cut trees were not saved the first time you saved/loaded a game

* Fixed bug with escape key if pressed once in building mode

* Fixed bug where selecting tree houses in book multiple times without actually building them could break building other items

* Fixed suitcases around plane not having working pickups on loading a saved game

* Rabbits should now be saved in rabbit cages on save/load

* Rabbits/raccoons will not disappear from traps if player moves far away

* Poison will no longer take away armor, only health

* Added low memory option to graphics menu - will be on by default if 32bit windows or if you have under 4gigs of ram. Will limit/turn off some of the effects to keep memory down.

* Improved memory usage and performance of skin shading. Introduced new skin wrap textures to control where skin is more translucent.

* Fixed missing audio on weapon fire

* Increased length fire stays on some weapons

* Fixed missing sound effect on eating meds

* More informative text about leaves in inventory

* Increased amount of impact upgrades have on weapons

* Tweaked how and when combat/stress music plays

* Main menu audio now plays throughout loading of game

* Fixed pedometer being slow to open and close

* Fire weapons will no longer be lit when lighting a regular fire

* Disabled player inventory and game pausing if player is dead

* Fixed garden not working with seeds

* Collected seeds are now visible in inventory

* Fixed bug where you couldn't cut aloe vera plant

* Simple leaf sub surface scattering added!

* Improved motion blur performance on enemies and creatures

* Music volume now has its own slider in options menu

* Cassette tapes are now pickups and have unique names/info in inventory. Search caves and other areas to find them.

* Closing inventory now removes items from crafting cog

* Fixed gui messages and icons appearing over pause menu and fixed red cross appearing on load screen

* Added option to return to title screen from pause menu

* Simplified bomb building to use any amount of coins

* Texture and animation memory improvements

* Left hand does not play block animation if using non-stick weapon

* Longer damage trigger added to enemies to fix player ducking from attacks cheat

* Fixed issues with enemies sometimes standing back up instantly if struck

* Fixed issue where enemies would sometimes stand in one place forever

* Less bunching up on turtles

*Note: Some reported bugs may be due to old save games! To ensure your game is fully up to date, start a new save game.*

## v0.08c (released October 26th, 2014)

* Hotfix for subsurface skin on AMD cards

* New skinny enemy animations added

* Out of date saved games will now be ignored, instead of attempted to load if incompatible with latest patch (clicking load on these will start you back on plane)

* Fixed plane crash location that was set too steep and where players would die instantly if they fell out of without eating medicine first

* Fixed issues with some buildings causing load times to increase

* Fixed issue where buildings would disappear from your save game and you would have to load from a fresh game to see them. (this one was hard to track down! let us know if it's still happening for anyone after this update)

## v0.08d (released November 7th, 2014)

* Tree structures (tree houses) are now destroyed when the tree they're on is cut down

* Improved raft and fixed issues with raft and save/load

* Fixed Drying Racks food positioning

* Fixed Bench ghost positioning

* Fixed bug that caused projectiles to be “paid” twice when thrown

* Fixed glass upgrade recipes for most weapons

* Fixed Plane Axe's Cloth on crafting mat (for fire weapon upgrade)

* New upgrade recipe Sticky bomb: Bomb Timed + Tree sap

* Player run animations added!

* Fixed thunder sound being cut off early

* Fire enemies will now sometimes attempt to burn down player built structures again

* New sound effects added - fixed missing underwater sounds, added splash and fall sounds to player. Added transitions between day/nighttime. New improved tree cut sounds.

* Fixed some issues with skylight occlusion option

* Improved bloom performance by 2-3x

* Fixed bug where item would be unequipped after using inventory, then opening book then hitting escape

* Massively reduced amount of memory ghost items take up

* New player textures

* (multiplayer) Player head added! (this also fixed issues with player head shadows in single player)

* New better looking torch cookie

* Fixed destroyed wall logs not being pickupable

* Fixed feathers being hit away by weapon when killing birds making it hard to collect them

* Fixed issue where held weapons would get permanent motion blur on them

* Fixed glitchy shadows break up in distance!

* Fixed some bugs with using lighter and it vanishes/equipping at wrong times and Fixed bug where pressing the ‘O’ Key would attempt to bring up lighter

* Fixed fire on effigies not burning birds or player

* Enemies no longer sleep outside during the day

* You can now destroy enemy built art and effigies!

* Fixed camera position on during plane crash so you can no longer see down your own neck

* Improved performance of held flare

* Tweaked animal density in world

* Improved weapon colliders for more accurate hits

# v0.07 (released September 17th, 2014)

* Rock holder blueprint added

* Moveable log holder blueprint added

* Mid sized cabin blueprint added

* Tree house blueprint added

* Working door added to custom build doorway

* Male version of skinny mutant added

* New animal added: Tortoise

* New animal added: Raccoons!

* Animal numbers will go down over time if you kill a lot of them. Will eventually slowly repopulate

* Different animal types now stay around specific parts of world

* Weapon balancing, all weapons will be slower when holding an item in left hand (Lighter, walkman etc.) faster when held with both hands. New slower axe anim in combat.

* More accurate weapon collider sizes, small axe smaller, stick bigger etc.

* You can now catch rabbits and place them into the rabbit cage

* Better previous weapon switching system

* Improved blueprint placement, items will now turn red and be unplaceable if intersecting trees

* New rock attack animation, more powerful, uses more stamina

* Cave's now only contain blue skinned enemies and distorted mutants

* Better combat theme

* Better lake theme

* Fixed peaceful mode (was accidentally broken in last update)

* Further improved enemy pacing over time, fixed bug that could cause enemies to vanish over time

* Energy now replenishes faster when sitting on bench

* More small props added

* Switching weapons whilst holding molotov will no longer cause it to drop

* Sound effects added for adding sticks/logs and rocks to storage

* Whoosh sound added when items moved around inventory

* Fixed molotov pieces bouncing around causing fire to move in strange ways

* Fire now scales with amount of fuel

* Plants now burn for longer

* Trees will tumble over if burnt now and added new burning material with embers

* Tree leaves will now burn away correctly when on fire

* Energy bar now flashes when playing music to make clear that your stamina is getting a boost

* Crafting info pages unlocked in survival book (rough, missing lots of items)

* Fixed bug where you could get infinite flares by dropping flare gun and picking it up again

* Fixed bug where day count could change when entering/exiting caves

* Fixed yellow axe mesh not visible when equipped

* Terrain texture and shape improvements

* Fires can now cook an unlimited amount of items, food will be placed at random location on fire

* Fixed bug where you could sometimes get infinite sticks/rocks in inventory

* Arrows should now work more effectively against enemies

* Visible lizard skin armour!

# v0.06 (released August 27th, 2014)

* **(A.I.)** New tribe type added - starving cannibal! Will eat fallen comrades

* **(A.I.)** Different tribes will now interact with each other, hunting, stalking, killing and eating each other

* Shadows Improved! Fisheye shadow distortion gives higher resolution shadow up close and now uses a single cascade (experimental, maybe cause some glitches)

* 2 New cave systems added near geese lake

* Fixed missing light on crafted torch

* Real caustics added to water

* Lighting effigies uses the lighter correctly now

* Fixed issue where cannibals could get stuck after being knocked down

* Creepy mutants and animals no longer get stuck in noose trap spinning forever

* Improved look of noose trap when sprung but empty

* All traps can be reset

* Player will set off traps if he touches trigger

* 5x new plant types added

* Fixed **(Unity fix)** issue where grass would cause slight framerate hicks

* Hint to NVIDIA driver that it should use the discrete GPU in Optimus chipsets. (Unity fix - should help laptop performance)

* Added press space to skip tutorial to opening plane crash

* Fixed bug where arrows could get stuck in sky above fires

* Fixed rockpit floating slightly above terrain

* Moving forward, crouching, jumping or pressing e will make player stand up if sitting on bench

* Better bench model

* Fresnel effect applied to specular and fixed specular leak around backside of objects

* New props added: washed up packages and shipping containers

* New prop added : Orange tent

* New improved opening plane crash sound effects

* Fixed marigold and dead rabbits overlapping in inventory

* Improved plane interior textures and resolution

* Added icon to remove ghost structures, fixed issue where add icon could sometimes stay on screen after removing ghost. Limited ghost removal to only if no resources have been added.

* New crunch sound effect for when removing ghost structures

* Wall built can now be destroyed by hitting it with axe, giving you back resources

* Musical sting added to player waking up on plane

* Improved terrain spec and (finally) fixed water accumulation when raining, added new sharp rock terrain texture to under lakes

* Improved pond water distance settings

* **(Crafting)** Fixed issue where you could remove feathers before crafting arrows and still craft the arrows. Fixed issue where you could sometimes not craft items depending on order of items placed.   
  Adding an item to a craft that isn't needed will stop you from crafting until it's removed again.

* Fixed bug where you could lose medicine by crafting the same item multiple times

* Lots of collision issues fixed in caves

* Improved cave lighting! Better looking settings for skull lights and less light popping on/off

* Sped up rabbits

* Lowered brightness of click to place buttons in survival book

* You can now save your game at a shelter without sleeping

* Fixed bug where coins could vanish after adding them to a craftable item

* Fixed bug where day counter wouldn't increase correctly

* Fixed bug where crickets would continue to play during the day

* Fixed issue where cave sounds would sometimes vanish when walking between connecting caves

* More combat balance and a tweak on weapon settings

* Performance and memory improvements

## v0.06b (released September 5th, 2014)

* New spawning system for enemies, better world population, better pacing and progression over time

* A.i has more chance to venture to expected areas (i.e. cannibal villages)

* Optimized sky light occlusion performance

* Fixed fog showing through ocean water

* Improved ssao!

* New camping prop added

* Fixed birds getting faster and faster over time

* Improved ocean sound effects

* Improved Bow and arrow sound effects

* Fixed yacht lod bug where it would vanish for some players
* Added sound effects to timmy dragged away scene

* New improved cave drips and cave wind sound effects

* Fixed some dynamic objects flying up in air on spawning (boxes, suitcases)

* Fixed bug where skinny enemies would switch to default shading when injured

* Cave ambient track added

* Enemy combat theme/suspense themes added (rough)

* Lowered (4x) damage and speed of arms and legs when used as weapons

* New first class passenger model added

* Skinny woman made blood less shiny

* Fixed bug with inventory light at night being too bright

* Balance tweaks : Increased fall damage, lowered how much health meds heal you

* Turtles can now be killed by repeatedly hitting shell (although hitting them in head is much quicker)

* Fixed brightness of standing fire (same as regular fire now)

* Fixed fire stick enemy too bright

# v0.05 (released August 8th, 2014)

* New craftable item added : Bow (Stick plus cloth plus rope)

* New craftable item added : Arrows (Stick plus 5 feathers)

* New craftable item added : Fire torch (Cloth plus Stick)

* New craftable item added : Medicine (Aloe plant plus Marigold flower)

* Fixed staircase built scale being different from ghost scale

* Fixed hunting shelter built scale being different from ghost scale

* Fixed enemies not playing correct death animation

* Enemies no longer get stuck jumping down from trees

* Enemies will dodge around close trees more often, less instances of getting stuck on trunks

* Fixed(removed) weirdly shaped weeds

* Fixed rusty axe duplication bug

* Fixed yellow axe not appearing in inventory

* Lower sound effect tree breaking notification

* Fixed bug where you could throw multiple tennis balls at once

* Added support for more resolutions

* Parry no longer affects burn/poison and other damage to player

* Carry log animation added to player

* Improved enemy collision detection with built walls and structures

* Enemy vision is now properly blocked by player built structures

* ‘check bloody arms’ animation can be cancelled by other actions more reliably

* Fixed enemies sometimes getting stuck and walking backwards forever

* New 3d models added, first class passengers \* 2

* Fixed rope not appearing in inventory when collected

* Added new female texture and hair variations

* Fixed glitch in cave where players could fall through ground

* New cave prop added : Mining hat with light

* Fixed some pathfinding issues in animals and mutants

* Fixed lit fires blocking enemy vision causing weird AI behaviour

* Enemies should set themselves on fire less often

* Fixed an issue where enemies would get stuck on spot while climbing trees

* Fixed counterattacks of cannibals sometimes not registering

* Fixed missing turtles on main beach

* Fixed enemies getting stuck in trees

* Fixed enemies freezing upright after being shot with flare gun or burnt

* Batteries can now be used to restore charge in flashlight and lowered torch battery drain speed to half

* Stick holder now holds 20 sticks!

* New cannibal village art added: Blankets, drying racks

* Rabbits and lizards will navigate around trees and rocks better

* Distorted mutants can now be killed with flare gun/fire

* Improved bloom

* Adaptive photographic tonemapper added

* Fires now drain slightly faster

* Improved sunlight settings

* Motion blur now takes into account HDR

* Improved foliage lighting

* Improved water shader, more refraction as depth increases, more accurate sky reflections

* Raised player fire damage amount

* Rope pick ups added to some cannibal villages

* Pedometer now shows outside temperature

* Logs should no longer fall through rocks

* Fixed plane seats vanishing on loading save game

* Made feathers brighter, made batteries brighter (easier to see in inventory)

* You can now carry 3 dead rabbits and 3 dead lizards (instead of 1 each)

* Fixed plane crash crazy motion blur bug

* Marigold and AloeVera now get stored in backpack when picked up

* Texture resolution option added to options menu (start options menu only) Try lowering this to \* improve memory on lower ram systems and improve performance on lower end cards.

* Fixed issues with taking bombs from inventory

* Birds now spawn feathers when killed

* Day counter now starts at 0 from when you first wake up in plane

* Improved cave items/layout and lighting

* Fixed lizards & birds vanishing when close to edge of screen

* Rainbow will be forced off now if night time

* Tweaked rain chance settings

* Enemies will now push past bloody table instead of getting stuck

* Fixed dead bodies spawning too many chunks when chopped up

* Fixed some missing sound effects, improved night time sound effects

# v0.04 (released July 22nd 2014)

* New A.I. behaviour, mutants will sometimes go home to sleep during day along with other new routines

* Distorted mutants can now be killed with regular weapons

* Distorted mutants more aggressive and deadly in combat and have expanded actions

* Better ambient lighting. Trees and large objects diffusely occlude skylight (experimental)

* Pause menu now actually pauses game

* Enemies use rocks more often to jump attack at player

* New female enemy type added.

* Better distribution of enemies throughout the world.

* Constructed bench now works and players can sit to regain energy or watch sunset

* Increased axe damage against enemies

* More variation to female cannibal models, added procedural breasts size system

* Improved Rabbit/Lizard distribution and optimized CPU usage.

* Improved sky and sun look

* Improved dead cave lighting and cave 2 lighting

* Better cave textures and rock look

* Dead cave prop fixes, fixed some incorrect rock placements

* Improved load times and added loading percentage amount

* Re-balanced hunger drain

* Better cave ground with flowing water and more detailed textures

* Enemies will now push small items out of the way instead of getting stuck on them

* Dead sharks now ragdoll

* Fixed rain sound never going away even after rain stops

* Fixed bug where some partially built structures couldn't be completed after loading a saved game

* Fixed animals sometimes disappearing in regular and vegan mode

* Fixed issue where you could still shoot flare gun or use other weapons when pause menu was open

* Yacht random position won't change now or get lost when saved game is loaded

* Fixed all effigies turning into arm effigy on load

* Fixed E to add icon showing up if holding a rock or stick even if items not needed in building

* Fixed cave drips continuing to play even when not in cave

* Fixed fish swimming outside of pond near cliff section

* Fixed fullness always starting at half when loading a saved game

* Fixed moonlight sometimes missing completely

* Fixed stick marker vanishing on loading saved game

* Fixed missing collision roof of cabin

* Fixed player flying in air after chopping dead bodies

* Rain effigy effect should now work and will wear off after time

* Cannibals spawning in villages no longer ‘pop’ when waking up

* Fixed creepy female model attacks sometimes not hitting player

* Fixed bug where bird landing on hand would sometimes stop axe from working

* Fixed enemy head and leg pickups sometimes appearing as arm pickups

## v0.04b (released July 26th 2014)

* Added graphics options for ambient Skylighting (will be off by default)

* Terrain settings added to graphics options (Parallax, Relief, Simple, Classic)

* Fixed grass distance not changing correctly for different quality levels

* Optimized greeble physics use

* Optimized sound detect system on player weapons (less colliders)

* Fixed issue with shadows light leaking

* Fixed plant rendering glitches

* Fixed missing small rock pickup

* Fixed issue where plant triggers would sometimes make book items impossible to click

* Fixed bug where houseboat blueprint wouldn't appear or couldn't be placed in world

* Fixed held arms/heads registering attack even if not swinging

* Held arms/legs behave like axes not sticks

* Tennis balls no longer infinitely bounce

* Fixed Player sometimes being killed in one hit by enemies

* More Accurate player fall damage

* You can remove placed blueprints by pressing C

* You can press space to skip opening plane crash

# v0.03 (released July 1st, 2014)

* No enemies mode! Type “veganmode” on title screen to activate (without the “”)

* Player head added! And held items now correctly cast shadows

* New surprise item added to plane

* Yacht location is now random

* Bats now correctly fly out of cave entrances

* Partially built structures are now saved

* Fixed water not accumulating on terrain when raining

* Cassette player can now be turned off by clicking it a second time if it's already playing

* Log Cabin now has a floor, a door with hinge and a sleeping/saving spot

* Birds will now land on window ledge of your built log cabin

* Molotov will extinguish if in contact with water

* Improved sunset/sunrise lighting

* Two new effigies buildable, simple head on stick and arms pointing to sky

* House boat buildable (Warning : buggy!! - especially with sharks. Also, may sink)

* Stick marker added to custom building, quickly build yourself waypoints

* Coral and seaweed added under water (rough)

* New buildable item : Stick holder

* Inventory can now carry 1 additional stick (to make shelter construction easier)

* Small texture tweaks/improvements

* Shadow distance increased for High and mid settings

* Improved motion blur on held items

* Hanging rope pick ups added to deep in caves

* New cave lighting prop: Laptop

* 11 new filmic inspired grade options added to graphic options menu

* Bench now buildable via book section ‘Furniture’

* Single bat prefab added to parts of caves

* Improved lilypad pop-in

* Med pickups now go direct to inventory instead of being eaten on pickup

* Improved cannibal village track implementation

* ‘Lake’ track added to Geese Lake

* Bash pass at all ambient sound implementation, better transitions, better positioning, fall off and ranges

* Thunder and rain sounds randomized

* Cave audio pass, adding reverb and echo, better balancing

* Underwater sound filter added

* Water footsteps sounds now play when you walk into water

* More memory optimizations should improve stability

* Lowered memory usage further if 32bit windows is detected, should fix crash on opening if less than 4gbs of usable memory is available **(note: 4gb usable is still recommended)**

* Head no longer pokes through collision!

* Fixed some items missing from inventory when game was loaded

* Fixed collision where you could wall walk out of plane

* Fixed can't carry more raw fish message that would appear when you had too many rocks.

* Fixed pond covered in logs

* Fixed left hand held conflicts between lighter, torch walkman etc.

* Removed gleam on inventory coins and flares

* Fixed floating garden

* Fixed leaf vertex colors on small leaf hut

* Fixed flare gun falling through yacht

* Fixed log going to -1 if you died whilst holding a log

* Fixed small effigy construction shader being too faint

* Removed grass cutting from opening inventory **(was causing crashes on some pc's)**

# v0.02 (released June 16th, 2014)

Version 0.02 Changelog (Saved games from 0.01 won't work with this version)

* Sharks

* Simple raft now buildable via book (No Sail yet!)

* Walls can now snap to form floors and roofs (experimental, can defy gravity)

* New surprise item added to yacht

* When being knocked out for first time you will now wake up in a random cave

* Lowered fall damage amount

* Birds can be killed with fire

* Stamina recharge now takes longer

* You can now block attacks with the red plane axe by holding down right mouse button

* Timmy taken scene a little more dramatic, better lighting, sparks

* Lowered intensity and range of fire light

* Lowered health on turtle

* Improved fish movement

* Increased range of lighter

* Enemies will drag downed friends out of danger again

* Females will sometimes freak out at dying family members

* Improved load times

* Reduced stutter

* Overall performance increases

* Big memory optimizations, should help crashing on some pc's

* Improved cave wall memory usage

* Dropped sticks and rocks are now pooled and shouldn't increase memory over time

* Optimized hud rendering (10% faster on cpu)

* Improved lake water swim zones

* Ocean swim zones now correctly rise and fall with tide

* Underwater visuals improved

* Improved terrain in some areas, reduced lumpiness in rocky area, fixed issues with caves poking through terrain

* Fixed super deep ponds that could kill players by falling into them

* Small old boat collision added

* Plane exterior collision added

* Improved balance on some grass textures (less bright)

* Lowered top heavy pine tree to be easier to cut

* Lots of small material/texture tweaks

* Sunset/sunrise made brighter

* Beach cave entrances made bigger and easier to enter

* Improved world collision in some areas

* Improved low resolution mountain textures

* Improved terrain rendering and missing specular

* Improved cave lighting and details (caves 4,5)

* Fixed countdown timer not taking different time zones into account

* Fixed some spelling mistakes in tutorials and in survival book

* Fixed shelter on fire spawning infinite logs

* Fixed bug where day count was 1 more than it should be

* Fixed issue where sticks,rocks and logs needed could go to -1

* Fixed not switching back to default weapon after holding lizard, rabbit or fish

* Fixed player not colliding with things tagged ‘Prop’

* Fixed light leaking into parts of some caves

* Fixed bug where you couldn't cook multiple times on same campfire

* Fixed spear being able to cut down trees

* Fixed ponds flickering at certain distances

* Fixed some items not being saved in inventory when game is loaded (some might still vanish, expect more saving fixes/improvements soon)

* Fixed log holder not saving logs on load/save

* Fixed twinberries not having eat icon and having wrong leaf texture

* Fixed bloody tables in cave not being cut out of nav mesh

* Fixed lizard and rabbit skin triggers not being connected to ragdoll body

* Removed extra set of teeth and eyes appearing behind Timmy

* Chopping dead bodies no longer results in player flying into the air

* Animals no longer spawn multiple copies if on fire

* Cannibals shouldn't run underwater or follow player out to the boat (they might run a little bit into water however)

* Fixed some bushes missing vertex colors when cut

* Fixed birds landing in sky, improved bird a.i. and performance

# v0.01 (released May 30th, 2014)

First official alpha build is released on Steam.

## version 0.01 patch (released June 2nd, 2014)

This was just a quick patch to address a Steam technical issue.

We're hard at work on getting the save hotfix out along with a couple other critical issues.

-Skunkie

## v0.01b (released June 4th 2014)

* Saving at small shelter now works

* Fixed issue where camera would spin during plane crash if a controller was plugged in

* Fixed enemies sometimes disappearing after a few days

* Improved tree collision

* Fixed log cabin floating

* Fixed some leaves not connected to trunk

* Improved stuttering/performance

* Removed lights from blue cave creatures

* Fixed trees vanishing when exiting caves

* Fixed bug where cave sounds could be heard above ground

* Spelling mistake on shelter ‘warmth’ in book

* Improved collision in some cave areas

* Fixed missing cliff detail texture

* Ocean shouldn't lose render texture on start

* Water visuals improved

* Fixed enemy head duplicating when picked up

* Fixed glitch where you could make infinite flare guns

* Fixed enemy head icon not centered, and showing an arm instead of a head

* Heads/arms and legs now go to inventory instead of being directly equipped
