# Custom Floor
Source: https://theforest.fandom.com/wiki/Custom_Floor
Categories: Building, Pages with image sizes containing extra px
Revision: 72239

**Infobox: Custom Floor**
**Description**
- **Also known as:** Procedural floor; Ex floor; Calibrated floor; Foundation floor
- **Added in:** v0.13
- **Building Type:** Custom
- **Upgradable:** No
- **Custom:** Yes
- **Variations:** Custom Foundation
- **Attachments:** Custom Walls; Custom Roofs; Rock Walls; Stick Fences; Bone Fences
- **Uses:** For building custom buildings; Has distributed damage
- **Restrictions:** Requires other structures to attach to
- **Other Effects:** Does not provide protection from rain
- **Stackable:** Somewhat
- **Buildable on:** Custom Walls; Rock Walls; Platform
- **Durability:** Very Strong

**Custom floors** are custom buildings that were added in update v0.13 of ***The Forest***.

## Gameplay

**Custom floors** can be used in custom buildings, they can be placed on top on custom walls to create a second floor. They can also be cut to create a hole for stairs by utilizing the Hole Cutter. As by v 1.12, custom floor can not prevent rain from entering the building. When placing custom floors, only the last point counts. What this means is where you place the last point of a custom floor, is the point that needs to be destroyed to destroy the **custom floor**. Custom floors have many uses and are highly customizable. They can make bridges, replace Custom Foundations as floors, create walk ways, balconies and more.

## Building

| ∞ | **=** | ∞ |
| --- | --- | --- |
| **Custom Floor** |  | Log |

## Known Bugs

* Custom floors built near each other can often support each other floating mid-air after the ACTUAL supports have been cut out
* When moving blueprints of Custom Floor over/into existing Defensive Walls, the blueprint will freeze in mid-air, and you have to restart usually.

## Trivia

* When released, **custom floors** were called **Experimental Procedural Floors**. Throughout the patch notes they are also referred to as ex floor, calibrated floor, and foundation floors

## Gallery

## Bridge Guide

## Important

* v0.48 - **(Building) Each floor and roof now has a 20 holes limit, this works around an issue in multiplayer causing clients to no longer receive holes past a certain amount, also prevents escalating computation costs due to inappropriate use of the hole cutter**
* v0.42 - **Added new cheat code: “woodpaste”. Can be used to reset floor & roof holes in a saved game. Cheat works once when game is started then gets reset when going back to title screen. Does nothing for MP clients**
* v0.38 - **Merged walkway and procedural floor in a single placement tool, bring near terrain to swap to walkway or bring it back up to swap to extensible floor which can be added to a custom structure**
* v0.32 - **Fire warm whole home system ! Enclosed custom structures with a lit fire on the floor now provide warmth regardless of player distance with the fire (note: only working on custom structures so far, not yet on prefab structures (log cabin)**

## Update history

| Version | Changes |
| --- | --- |
| v1.0 | Fixed procedural floor and roof sometimes not parenting correctly with its supporting structure |
| v0.72 | Log cabin,small cabin, gazebo, garden, bonfire, rock side platform, defensive spikes, tree platforms, floor platform, wood target, procedural roof all use new log model/texture type now |
| v0.57 | Fixed enemy bodies not falling down if floor was destroyed/removed |
| v0.50b | (Multiplayer) Fixed bug when attempting to load and play an old saved game with more than 20 holes in a floor |
| v0.49 | (Building) Floor & Roofs ghost triggers now better conform with the visible model (prevents the new system from not allowing to complete it when standing bellow) |
| v0.48 | (Building) Fixed aiming back and forth between fences and floors breaking wall & fences placement in autofill mode **(Building) Each floor and roof now has a 20 holes limit, this works around an issue in multiplayer causing clients to no longer receive holes past a certain amount, also prevents escalating computation costs due to inappropriate use of the hole cutter** |
| v0.47b | Fixed issue preventing to use manual floor & roofs placement to function as expected in some cases |
| v0.47 | Improved ghost building placer staying above floors instead of constantly snapping to terrain Procedural foundations, floors and roofs now have a new dot and line gizmo when placing it in manual mode to fully visualize what is going on within  Revamped procedural floors & roofs manual placement in a similar way to bridge anchor locking, except that instead of targeting a single point it is possible to slide along the supporting structure shape (i.e. edge of wall)  Added edge intersection check when placing floors and roofs |
| v0.46 | Procedural Floor/Walkway swap system can no longer place walkway below terrain when not in caves Floors & roofs no longer show the autofill/manual mode toggle action icon when not in direct vicinity of a supporting structure  Floor now shows a preview starting after the first locked point instead of after the second locked point  Fixed floor ghost color code not matching exactly rest of building system |
| v0.44 | Walls/Fences and Floors/Roofs each save and restore the latest autofill/manual mode |
| v0.43c | Toggling between autofill and manual placement for walls, floors and roofs is now done with a simple press of the “Craft” button (instead of hold), fixes issues with other trigger breaking the toggling such as drink trigger when building over a lake |
| v0.43 | Revamped procedural wall auto fill: in the same fashion as floors & roofs, walls now show a preview of the result of “auto fill” feature. By default it tries to guess what mode is desired and toggles between manual and auto fill depending on ghost touching terrain or a player made structure, holding the “Craft” button (C by default) allows to toggle between modes manually. After doing so it no longer switches mode automatically until a new wall is being made Placing a procedural wall on a foundation with floor will now cover the floor area instead of matching the foundation shape (so if foundations have an open side the ghost wall will cover that part as well instead of leaving it open, note that as all constructions it can be cancelled if not wanted) |
| v0.42 | (Multiplayer) Floor/Roof hole cutter is now available ! Clients cannot cut holes in ironforest mode to prevent griefing Fixed excessive random jitter sometimes occurring on floors after cutting holes  Bigger structures that can't be placed on houseboat floor can no longer be placed on its walls  Fixed extremities of foundation's floor not perfectly overlapping the area, eventually causing foundation to be visible on the sides, also fixes some weirdness with holes on sides of floors and roofs not perfectly conforming with hole area. Might have an impact on look of previously made buildings/holes  **Added new cheat code: “woodpaste”. Can be used to reset floor & roof holes in a saved game. Cheat works once when game is started then gets reset when going back to title screen. Does nothing for MP clients** |
| v0.41b | Calibrated floor & foundation floor log cost with new log size to match old cost for a given area coverage Floor hole cutter now only cuts structure within the visible white rectangle area and no longer those that have been targeted and are above or below  (Multiplayer) Fixed bombs exploding over a foundation floor not distorting for client |
| v0.41 | Fixed walls sometimes snapping below when placing on custom floor Hole cutter can now cut several buildings at once, whether side by side, at different heights and/or overlapping each other, making it a lot easier to edit complex/composed structures. Watch out for side effects of this change when trying to cut a single floor  Ghost floor is now red when it cannot be placed  hybrid ragdoll system added – enemies will conform better to the floor when dead or dropped from carried.  Ex Floors now accepts log model variations + setup 3 variations  Fixed foundation's floor position locking possibly going out of sync with foundation's one  Slightly lowered randomisation of floor logs (was giving bad result sometimes and it's far less necessary now that we have variations)  (Performance) Revamped floor hole cutter preview, instead of cutting the actual floor or roof it shows a ghost overlaying it with no physics/navigation cost involved |
| v0.38 | Fixed switching floor between autofill and manual placement when there's a preview floor displayed causing preview structure to remain visible and eventually causing improper icons to be displayed **Merged walkway and procedural floor in a single placement tool, bring near terrain to swap to walkway or bring it back up to swap to extensible floor which can be added to a custom structure** |
| v0.37 | Rock fences can now be used as support for floors and roofs ! Fixed some issues with placing floors/roofs on non-flat walls, it now tries to cancel positions that are too far from the rest to try preventing floors from floating mid air, eventually cancelling autofill if not enough points remain  Revamped floors to toggle between autofill and manual placement mode, by default in autofill floors will now show the ghost of whatever support is currently targeted and can be placed with E (or switch to manual placement with C to cherry pick each point like in legacy) |
| v0.32 | Revamped procedural wall door physics settings, doors are now easier to go through, always go back in position, and in the event of shady placement (i.e. with a floor going through the bottom log row) door should work anyways Improved placing structures when there was already a ceiling above, making adding staircases to custom built multi-floor structures easier  **Fire warm whole home system ! Enclosed custom structures with a lit fire on the floor now provide warmth regardless of player distance with the fire (note: only working on custom structures so far, not yet on prefab structures (log cabin)** |
| v0.22 | Made Ex Floors & Roof closer to supporting walls (not retroactive) |
| v0.21 | New building (kinda): Floor hole cutter ! (caution: holes are definitive !) (SP only) |
| v0.19 | Improved building placement formula, now handles better big height variations like you can have near edges of floors |
| v0.18c | Fixed Ex Wall being offset downwards when using the auto-fill feature to place it on a Foundation + Floor, causing doors to be hard to open (not retro active) |
| v0.18b | Custom buildings (experimental walls, bridges, procedural stairs, roofs, floors, foundations) now all work in multiplayer! |
| v0.18 | While placing Foundations, it now shows a log between target position and the floor below before any position has been locked Fixed Foundation/Floor/Roof ghost collider requiring to move out of collider before it can be targeted |
| v0.16 | Fixed issue preventing to lock floors/roofs on multiple walls on the same height level New snapping grid gizmo to help with manual placing of experimental floors & roofs (tip shows the current lock position and is big enough to be seen from either side of a wall) |
| v0.14 | (Custom Building)Procedural foundations now auto fill with experimental floor making structures simpler to build. (Custom Building)Added valid angle & distance gizmo to Foundations, Floors, Walls and Roofs |
| v0.13 | **Custom Floor added to the game** (single player only)New buildable item: (experimental)Procedural Floor (snap on top of foundations, or to procedural walls that are on foundation + floors) |
