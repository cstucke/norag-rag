# Blueprints
Source: https://theforest.fandom.com/wiki/Blueprints
Categories: Gameplay
Revision: 74749

**Blueprints**, also known as *ghosts* are semi-transparent ghost models of buildings. They appear before their building is completed, and resources are added to these blueprints in order to add on to the building while it is being built.

## Blueprint Variations

Pressing the R key on certain placed blueprints will change their type:

* Small Stick Holder becomes a Large Stick Holder
* Small Rock Holder becomes a Large Rock Holder
* Small Log Holder becomes a Large Log Holder
* Tree House, Alpine Tree House, and Tree Platform have the option to remove, or keep the climbing rope
* Defensive Wall can have doors added to the wall
* Custom Wall can have wall sections changed to a door or window

## Positional Variations

Some blueprints change type automatically when placed in certain positions:

* Wall Weapon Rack becomes a Ground Weapon Holder if aimed at the ground
* Platform becomes a Cliff Side Platform when placed against a cliff
* Animal Trap becomes a Fish Trap when placed in water

## Controls

| Action | Button Assignment | Description |
| --- | --- | --- |
| Rotate | `R` | Rotates building around if relevant |
| Change Type | `R` | Once placed, changes certain building types, like small and large stick holders |
| Build | `E` | Places blueprint/places materials |
| Cancel Blueprint | HOLD `C` | Cancels the blueprint |
| Place Multiple Buildings | HOLD  `L CTRL` | Allows you to place multiple blueprints of the same building repeatedly. |
| Auto/Custom Mode | `C` | Switches between custom & auto mode with custom buildings |
| Place Custom Point | `LMB` | Places a custom point of a custom building blueprint, such as a custom wall or stick fence. |
| Remove Custom Point | `RMB` | Removes last custom point of a custom building blueprint. |

## Changing Blueprint Colors

In the *options* menu under *gameplay* you can change the color of **blueprints** as well as their opacity. The colors you can select are white, blue, green, and purple.

## Known Bugs

* Very rarely when a blueprint is placed, it may completely vanish and the marker as well. This can be irritating because in the bottom left of the HUD shows resources needed for that specific blueprint that disappeared.
* When building near the big hole, defensive wall blueprints can glitch, making them rise 20+ logs high, and be unremovable by usual means (tested near small river at direct crater side)
* When you set a blueprint on the bottom of the ocean below the yacht the blueprint may be "stuck", you can't build on it or delete the blueprint.

## Update history

| Version | Changes |
| --- | --- |
| v1.06 | Fixed canceling some ghost structures with a single log added dropping 2 pickups to the ground |
| v1.0 | Fixed procedural wall & derived structures showing place icon while not possible to place due for example to having a tree in the way Setup ghost foundations to turn last edge red if not lockable  Ghost models now use the same geometry and the final build versions, making the models line up perfectly.  Fixed ghost structures appearing stuttery if moving left or right while placing  Improved positioning of hammer icon on ghost structures and fixed some cases of icon visible before ghost position was placed  Fixed houseboat ghost building too high above water  Procedural buildings point locking logic now properly check for permission to build on dynamic structure, thus effectively preventing doing so with current state of the features  Added new outline ghost shader. A thin outline will appear around outlines giving them more of a drawn appearance and making them easier to see in various lighting conditions.  Fixed gazebo built not lining up with gazebo ghost |
| v0.72b | Fixed an issue with having multiple ghost basic walls in game causing parts of the game to not work correctly |
| v0.72 | Looking down while placing a structure now brings the ghost closer to the player instead of remaining always at the same distance Added a 0.05s delay before showing ghost buildings after selecting it in book to prevent it appearing to drop down from sky when first placed  Fixed following ghost objects not lining up closely with the built model: Basic wall, wall with window, Wall with door  Fixed stick fence ghost being offset from the built one  (Multiplayer) Fixed ghost cranes not synced properly upon loading a saved game |
| v0.71 | Fixed current book entry not properly selected itself after placing a ghost and going back in book when using a gamepad It is now possible to close book and cancel ghost placement with Xbox gamepad B button or dualshock Circle button |
| v0.68 | Stand & rockpit fires are no longer destroyed after burning out and don't turn into a half built ghost after being hit when lit |
| v0.65 | Ghosts and building requirements updated for raft and houseboat Ghosts updated for small and large holders to match finished log visuals  Fixed ghost leaf shelter rendering over book |
| v0.64 | Fixed zipline ghost rope not fully covering entire length of the structure Fixed Temporary shelter, Log Cabin, and Skull lamp ghosts appearing as white outlines regardless of color setting in options |
| v0.63 | Hole cutter now properly clears out the yellow hammer on ghost structures Added “Ghost building tint” option in gameplay/interface, allows picking one of white, blue, purple or green  Added “Ghost building opacity” option in gameplay/interface |
| v0.62 | Fixed tree sap collector ghost construction hammer position It is now possible to jump when placing ghost buildings with a gamepad  Fixed proximity check for several structures ghosts (so it cannot be placed within trees)  Fixed deer and rabbit skin ghosts becoming invisible if placed on ground |
| v0.61b | Fixed issue with foundation ghosts not working correctly for clients |
| v0.61 | Added the yellow hammer overlay icon to all building ghosts that didn't have it yet Ghost dock now performs an accurate presence check to prevent players from completing it while inside the model  Fixed ghost Wall Planter, Wall Weapon Rack, Head Trophy, Ceiling Skull Lamp, Wood Bench and Sap Collector not turning red when not placeable |
| v0.58 | Roof ghost now turns red during the lock height phase while height isn't valid |
| v0.56 | Lowered place distance of the rock swing trap, fixed ghost being away from completed trap position |
| v0.54 | (Multiplayer) Extended player in ghost building check to prevent completion to other players in game Hole cutter no longer has any effect on ghost procedural buildings (which was making it non completable) |
| v0.53 | Ghost foundations now check more accurately if player is below/within to prevent completion Fixed ghost rabbit cage sticks having sheen |
| v0.52 | Ghost wall type switch is no longer concurrent with the regular ghost interaction trigger (both can be used at the same time, regardless of holding log or not) |
| v0.51 | Ghost tree structures no longer prevent completing it when standing below it Changed default distance from player for ghost rabbit cage, water collector, weapon rack, stick marker, bench |
| v0.49 | (Building) Ghost structures now prevent adding the very last ingredient until the player exits the premises – fixes players getting stuck inside foundations or flying into air when completing raft (Building) Floor & Roofs ghost triggers now better conform with the visible model (prevents the new system from not allowing to complete it when standing bellow) |
| v0.48 | (Building) Fixed a bug with hole cutter causing some buildings to leave a broken ghost behind when targeted, increased amount of buildings it can remove, and fixed some errors/crashes with removing some structures |
| v0.47b | Fixed unlocking all ghost foundation points leaving a floating ghost behind |
| v0.47 | Fixed ghost procedural stairs trigger not matching shape and environment well enough to always be reachable. Improved ghost building placer staying above floors instead of constantly snapping to terrain  While placing a ghost wall or fence, parts that cannot be locked and wont be placed by pressing the place button now have a red tint to differentiate it from the rest of the structure  Removed all ghost procedural buildings placement legacy gizmos (round half circle, grid)  Fixed ghost bridge being red after locking first anchor  Fixed red ghost material visibility  Fixed wrong material on ghost log holder sticks, ghost basket sticks, raft built sticks and wrong layer settings for ghost weapon rack and floor hole cutter |
| v0.46 | (Multiplayer) Fixed a bug causing built logs from a ghost procedural roof to not be visible until structure is completed Rotating ghosts buildings now speeds up after half a second  Fixed floor ghost color code not matching exactly rest of building system |
| v0.45b | Fixed bright purple stick visible in ghost rockpit |
| v0.45 | Fixed material icons not visible when building a structure nested with a dynamic one (like houseboat) that has moved after ghost was placed New building: Large Log Holder ! Once placed, the ghost regular log holder can be toggled into a large holder. Holds up to 12 logs  New building: Large Rock Holder ! Once placed, the ghost regular rock holder can be toggled into a large holder. Holds up to 40 rocks  Fixed placing several buildings ghost with the Batch feature blocking opening inventory |
| v0.44c | (Multiplayer) Fixed swapping ghost tree structure as client causing it to be grabbed by host even if far away |
| v0.44b | Fixed selecting ghost in book with a gamepad using “Build” or “Take” action instead of “Fire1” wrongly placing ghost even if not meeting requirements, allowing for example to place rope on ground |
| v0.44 | It is now possible to rotate ceiling skull lamps and decorations in ghost mode Fixed ghost skull light placing floating above ground  Tree house, Tree House Chalet and Tree Platform can now be toggled with the “Rotate” button after being placed on a tree (but still in ghost mode) to a version in which rope has been replaced by an anchor !  New casting based anchoring for single anchor structures (currently climbing ropes only), grabs anchor in view near center of screen instead of within range of ghost, thus requiring less accuracy in aiming and being a lot easier to lock with anchors  Fixed ghost procedural stairs bug preventing from locking perfectly fine short stairs (within constraints)  (Multiplayer) Now returning extra ingredients added to ghost building by going faster than syncing speed to complete the required amount |
| v0.43 | Fixed ghost roof default visual not centered and weirdly offset Revamped procedural wall auto fill: in the same fashion as floors & roofs, walls now show a preview of the result of “auto fill” feature. By default it tries to guess what mode is desired and toggles between manual and auto fill depending on ghost touching terrain or a player made structure, holding the “Craft” button (C by default) allows to toggle between modes manually. After doing so it no longer switches mode automatically until a new wall is being made  Placing a procedural wall on a foundation with floor will now cover the floor area instead of matching the foundation shape (so if foundations have an open side the ghost wall will cover that part as well instead of leaving it open, note that as all constructions it can be cancelled if not wanted)  Now checking against existing wall chunks (or derivatives such as fences) when placing a ghost wall (or derivatives) and skip placing new chunks over existing chunks that share exact same position and size (for example, after autofilling a wall and cancelling a chunk, autofill can be used a second time to fill the gap without spawning doubled up wall chunks overlapping the existing ones) |
| v0.42 | (Multiplayer) Fixed ghost tree structures loaded from a saved game not getting removed if tree is cut down Ghost foundations can now be snapped back at first locked point regardless of what height is currently aimed at |
| v0.41b | Fixed completing ghost tree structure causing trees of this type to keep the cut leaves when pooled/reused across the world Fixed loading saves with buildings ghost past ingredient requirements, it now automatically completes it (to fix rare cases of this occurring) |
| v0.41 | Ghost floor is now red when it cannot be placed Ghost raft now stays above water  Ghost house boat now stays above water and can only be placed above water  Fixed ghost tree structures not going down when tree is cut down  (Performance) Revamped floor hole cutter preview, instead of cutting the actual floor or roof it shows a ghost overlaying it with no physics/navigation cost involved |
| v0.40 | Fixed ghost walkway not buildable Fixed stairs ghost mode's built stilt having a collider before being finalized  Fixed opening book immediately after entering place ghost mode causing player camera to lock up |
| v0.39 | Fixed wrong darker material on one of the built stick from simple and rockpit fires ghost |
| v0.38 | Ghost stairs now use a half log as default mesh Fixed ghost custom effigy rendering issues  Fixed ghost rock holder loading from save file as a stick holder  Fixed ghost sometimes rotating automatically |
| v0.37 | Improved positioning when placing ghost medicine cabinet Revamped floors to toggle between autofill and manual placement mode, by default in autofill floors will now show the ghost of whatever support is currently targeted and can be placed with E (or switch to manual placement with C to cherry pick each point like in legacy) |
| v0.36 | Fixed top part of ghost Ex-Platform looking different color than rest of building Fixed black line passing through ghost objects against horizon at night!  (Multiplayer) Fixed ghost rock fence looking filled when placed  (Multiplayer) Fixed loading save as host sometimes causing duplicate ghost bridge to show up client side |
| v0.35 | Rock based fires that are destroyed now spawn a partially filled ghost after showing the broken apart model (you have to put sticks & leaves in to restore the fire) Toggling partially filled Defensive wall and defensive wall Gate now drops back same amount it would have if ghost had been cancelled  Cutting down a tree that has a ghost building attached to it now properly destroys it in Single player  Tree structure ghost destroyed through removal of the tree now drops back same amount it would have if ghost had been cancelled  Added door visual to legacy wall doorway ghost |
| v0.34 | New procedural Defensive Wall addition: Defensive Wall Gate ! Ghost DW chunks can be turned into standalone one-sided gates (same fashion as regular wall window/doors) and 2 concomitant one-sided gates will automatically merge into a 2 sided gate, you may then toggle the gate again to switch orientation, or again to go back to DW chunks |
| v0.33 | (Multiplayer) Fixed ghost vanishing for a second when placing buildings as client for all but custom building types |
| v0.32 | Ghost wall with door addition now displays ghost door (to show orientation) |
| v0.29 | Fixed rock pit fire and stick marker ghost using wrong icon |
| v0.28 | Happy Birthday ghost model now matches built model |
| v0.27 | Fixed wrong item equipping after having cancelled placing a blueprint by opening book Fixed missing sticks on sled ghost model (cost is 21 sticks now) |
| v0.26d | Fixed case of partially built treehouses causing issue on loaded games/inability to add items to them or complete them due to them using the old stairs ghost model |
| v0.26c | Fixed ghost building rotation speed really high when using a gamepad |
| v0.26b | Each ghost rock fence visible model now costs 1 rock and no longer fills the whole chunk at once Fixed all ghost walls and fences first locked point position being offset from placing model |
| v0.26 | Fixed ghost traps placing floating above ground (not retro-active) Fixed treehouse ghost meshes containing old stairs mesh instead of rope mesh |
| v0.24 | Fixed bug with ghost skull decoration when loading a saved game Fixed ghost rock fence not saving properly (might require to recreate the ghosts to have the proper shape) |
| v0.23 | Survival book entry for skull lamp needed resources should match blueprint Small material tweaks: brightened ghost experimental material to make it easier to see during day  Holding the “Batch” button while placing a building now automatically brings up the same ghost building to be placed again |
| v0.22 | Fixed ghost wall defensive not saving properly (retro compatibility hack might cause old saves to have an overlapping log in between chunks) |
| v0.21 | Following features now require to hold their respective button for half a second to be triggered: cancel ghost buildings, drink & gather water, procedural buildings auto fill, eat berries and mushrooms found in world, eat plane food, eat cooked/dried food, light fires, save, sleep |
| v0.20 | (multiplayer) Clients now place ghost items instantly without a lag delay (multiplayer) Fixed client not seeing present ingredients in ghost buildings until some more were added after host loaded a saved game |
| v0.18c | Fixed error when cancelling a ghost building that doesn't have “built” renderers for each ingredient (cancelling raft with stick and log added no longer gives infinite amount of logs ;) (multiplayer) Fixed clients not getting sticks & rocks from cancelling ghosts buildings |
| v0.18 | Fixed flickering in the transition between procedural building ghost and built states Fixed Foundation/Floor/Roof ghost collider requiring to move out of collider before it can be targeted  Procedural buildings in ghost mode are now properly culled |
| v0.17 | Arm, leg and head now show present amount over total in ghost building ingredients (like all other ingredients) |
| v0.11 | Fixed wooden path blueprint not saving |
| v0.10 | (multiplayer) Fixed issue where items needed would sometimes stay on screen depending on if client/server destroyed a blueprint |
| v0.09b | (multiplayer) Fixed bug where destroying blueprint/ghosts could cause client or server to be kicked from game |
| v0.08d | Fixed Bench ghost positioning |
| v0.08d | Massively reduced amount of memory ghost items take up |
| v0.07 | Rock holder blueprint added Moveable log holder blueprint added  Mid sized cabin blueprint added  Tree house blueprint added  Improved blueprint placement, items will now turn red and be unplaceable if intersecting trees |
| v0.06 | Added icon to remove ghost structures, fixed issue where add icon could sometimes stay on screen after removing ghost. Limited ghost removal to only if no resources have been added. New crunch sound effect for when removing ghost structures |
| v0.05 | Fixed staircase built scale being different from ghost scale Fixed hunting shelter built scale being different from ghost scale |
| v0.04b | Fixed bug where houseboat blueprint wouldn't appear or couldn't be placed in world You can remove placed blueprints by pressing C |
| v0.01 | **Blueprints/Ghosts added to the game** |
