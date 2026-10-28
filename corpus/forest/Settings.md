# Settings
Source: https://theforest.fandom.com/wiki/Settings
Categories: The Forest
Revision: 72376

# Terrain

### Update History

| Version | Changes |
| --- | --- |
| v1.0 | Fixed big gap at top of mappings table |
| v0.71 | (Performance) Shorter trunks on trees (previously some would extend far below terrain even though they were not visible) Fixed player occasionally getting stuck underneath terrain when letting go of a climb out rope near the very top |
| v0.70 | (Performance) Terrain pixel error no longer takes screen height into consideration |
| v0.68 | Fixed some holes in world where cliffs connected to terrain Added a fail safe when loading a save saying player is in caves to ensure he is actually above terrain, this should work around rare/edge cases or bugs that could lead to save with the wrong in-cave data and wrongly drop player below terrain upon loading the save |
| v0.64 | Fixed terrain quality not applied when starting game |
| v0.63 | Fixed grabbing rope in sinkhole sending player high up above terrain level |
| v0.62 | Fixed some areas in world with incorrect collision allowing players to float/walk above terrain |
| v0.57 | Fixed arrows sometimes going underneath terrain if shot directly downwards |
| v0.55 | Fixed arrows sometimes floating when shot into terrain Fixed log sled glitching through terrain if grabbed and holding logs at the same time |
| v0.53 | Fixed some holes in terrain where former hidden caches were |
| v0.51 | Fixed a case of player not properly climbing rope if there was something around the bottom trigger (like a cliff or bumpy terrain) |
| v0.47b | Improved procedural wall terrain detection which was in some cases not switching to manual placement |
| v0.47 | Fixed some cases of buildings placing bellow terrain while player isn't in caves Improved ghost building placer staying above floors instead of constantly snapping to terrain |
| v0.43 | It is no longer possible to be brought under terrain by the climbing down top of rope animation. |
| v0.38 | Player now conforms to the angle of terrain when dying and injured |
| v0.37 | Cleaned up/improved some areas around beach cliff terrain (multiplayer) Fixed animals not aligning to terrain correctly as client |
| v0.36b | (multiplayer)Fixed platform cost being higher than it should be in some circumstances depending where placed on terrain |
| v0.34 | Fixed a bunch of holes in terrain/cliffs in snow area of map |
| v0.32 | Fixed player feet sinking into sand/snow when above terrain level (i.e.: on buildings) |
| v0.30 | Fixed plane crash going through water and terrain at some points |
| v0.29 | Fixed some instances of rocks floating and some cave models poking through into terrain New art added: Far back snow terrain cliff type now has partial grass variation  Fixed enemies sometimes getting stuck on unwalkable terrain when spawned a long way from player  Fixed logs sometimes spawning below terrain (made some trees look like they didn't provide their full yield) |
| v0.28 | (Art) Improved all terrain to ocean transitions |
| v0.27 | (Visuals) improved look of distant terrain – more break up, more bump Increased speed terrain dries after raining by 2x  (Art) North and south of the big lake, terrain polish and added grass |
| v0.26 | (performance) Optimized grass displacement system to use terrain height instead of a raycast to find terrain height Fixed visible section where terrain ended under ocean and would be darker than other water  Fixed a bunch of misaligned rocks, flying rocks, gaps between terrain and cliffs and other world errors  Terrain and detail improvements for section above big lake |
| v0.25 | Improved terrain water accumulation Terrain shader improvements, faster rendering, better performance when raining and more tweaks  Fixed bug with terrain sand making it look 8-bit around beach area. Balanced look of sand. |
| v0.24 | Arrows now go through cave doors and can stick to terrain behind ! Terrain – fixing some areas with holes, fixing some cliffs misaligned. Improving look of area around big lake.  New terrain shader, renders faster, looks better. Includes improved snow, wetness near water and more  (performance) Lowered cost of rain particles to render and killed them faster instead of rendering them far under terrain |
| v0.23 | Terrain/world improvements, adding more detail to edges of some ponds, adding new paths, filling out empty areas, improving look of some areas Improved terrain textures and shading  Improved terrain around cave 10 and fixed orange tent sitting crooked on rock  Better matched cliff grass to terrain grass using planar mapping |
| v0.22 | Water now accumulates faster on terrain when raining New cliff rock art (connects terrain to cliffs)  Fixed bug where one of the cave climb out entrances would stop terrain loading |
| v0.21 | Spears no longer fall through terrain or disappear when colliding with animals/enemies Replaced ugly grass terrain texture and fixed issue where starfish were still spawning on top of it  Terrain quality now also influences terrain pixel error resulting in less popping on higher settings and faster performance but more popping on lower settings |
| v0.20 | Fixed fish falling through terrain if dropped by player |
| v0.19 | Improved terrain around beaches Player camera no longer clips through terrain when entering a rope from above |
| v0.17 | Increased terrain mip map sharpness (won't blur as soon) Partially below terrain Foundations no longer go all the way down to the cave below and end up being very expensive |
| v0.16 | Fixed physics on some trees not colliding with terrain when falling |
| v0.08b | New tree fall and break apart sound effects! fall sound will now play until tree connects with terrain Fixed small cabin door and custom wall door getting stuck in terrain |
| v0.07 | Terrain texture and shape improvements |
| v0.06 | Fixed rockpit floating slightly above terrain Improved terrain spec and (finally) fixed water accumulation when raining, added new sharp rock terrain texture to under lakes |
| v0.04b | **Terrain settings added to graphics options (Parallax, Relief, Simple, Classic)** |
| v0.03 | Fixed water not accumulating on terrain when raining |
| v0.02 | Improved terrain in some areas, reduced lumpiness in rocky area, fixed issues with caves poking through terrain Improved terrain rendering and missing specular |

# Renderer

### Update History

| Version | Changes |
| --- | --- |
| v0.56 | Switched rendering BRDF to GGX |
| v0.27 | (Rendering) New SH lighting added! More ambient break up/better looking less flat ambient fill light |
| v0.16 | New options menu setting ‘Render Type’ will allow you to switch between new deferred renderer(recommended for modern computers) and Legacy renderer (recommended for older computers) Graphics options: added rendering patch selection |

# Resolution

### Update History

| Version | Changes |
| --- | --- |
| v1.0 | New base fire effect. New molotov fire effect. Replaced also player on fire and enemies on fire with new fire effects! |
| v0.69 | Improved fire on enemies and player texture resolution |
| v0.66 | Higher resolution textures on turtle shell |
| v0.56 | New burnt creepy enemy textures, and new graded textures/better resolution and better balanced regular, blue and dead textures Targeting quick select assignment cogs on backpack now works the same regardless of monitor resolution |
| v0.54 | Added back in experimental support for 5:4 and 4:3 resolutions |
| v0.48 | Improved resolution on plane seats/tray |
| v0.46 | Fixed next update part of title scene blurry at some resolutions |
| v0.41 | Option menu now updates its centering after resolution changed |
| v0.38 | Fixed pressing escape while having the input mapping conflict resolution popup, it now has same effect as pressing the cancel button |
| v0.37 | Enabled popups for resolution & preset options settings (should help setting things up on lower end hardware) |
| v0.24 | (multiplayer) Moved back button down to avoid blocking hosting game by Steam for several hours when clicking too fast on create lobby button at some resolutions |
| v0.05 | Added support for more resolutions |

# Keyboard

### Update History

| Version | Changes |
| --- | --- |
| v0.68d | Fixed hotkeyed items not appearing in player shadow |
| v0.63 | Fixed issue where you could sprint infinitely by spamming the sprint key |
| v0.62 | (Translation) Improved support for missing keys in translations files, labels now retain previous value for missing keys, if a font for a language isn't installed (or the game cannot reach it) the language won't be listed in options |
| v0.61 | Device management screen no longer displays keyboard and mouse |
| v0.55c | Fixed saving game with flashlight equipped and ignitable item in hotkey breaking lighter on load |
| v0.55b | Fixed issues with hot key items being visible whilst swimming or climbing ropes |
| v0.55 | New item quick select feature. Combine weapons on the crafting mat with the backpack to assign. Default keys are 1, 2, 3 and 4 on keyboard. Holding “AltFire” (block) while playing on a gamepad now switches the D-pad to quick select item slots |
| v0.47 | The escape key (on keyboard) or back button (on gamepad, either B or Circle) can now be used to navigate back to previous menu location |
| v0.43 | (Multiplayer) Fixed gamepad not having same restrictions as keyboard when using chat, causing issues such as allowing to double jump and possibly breaking all input |
| v0.37 | Fixed having a movement key pressed bringing mouse back to center of screen while in menu |
| v0.27 | Fixed exploded enemy pickup objects icons showing the “Inventory” action key Fixed player losing stamina if stationary while holding the run key New input action: “Map” Set to M on keyboard and Left shoulder 1 on gamepad (check your settings if you have done custom mappings it won't overwrite it) |
| v0.25 | Worked around an issue with some keyboards shooting keydown message repeatedly when holding down a key, preventing from using held input actions |
| v0.21 | Can no longer equip utility item when in inventory using keyboard shortcut |
| v0.18 | Re-work of all icons – will now display key set in custom key mappings, will switch automatically to Xbox controls when using controller. |
| v0.13 | Lowered throw force on bomb timed and added friction to rigidbody to reduce hockey puck feel |
| v0.08d | Fixed some bugs with using lighter and it vanishes/equipping at wrong times and fixed bug where pressing the ‘O’ Key would attempt to bring up lighter |
| v0.08b | Fixed bug with escape key if pressed once in building mode |

# Mouse

### Update History

| Version | Changes |
| --- | --- |
| v0.67 | Fixed camera snap when opening book with very low mouse smoothing setting UI – Fixed ‘Mouse X Sensitivity’ saying ‘Mouse sensitivity’ |
| v0.66 | It is now possible to bind mouse buttons to axis actions such as movement Added mouse smoothing setting with option to set this to zero |
| v0.61 | Device management screen no longer displays keyboard and mouse |
| v0.46 | When using a gamepad, cursor now snaps to buttons instead of moving freely mouse style, thus making navigating book easier. |
| v0.37 | Fixed having a movement key pressed bringing mouse back to center of screen while in menu |
| v0.34 | Fixed falling from a height sometimes causing mouse rotation speed to decrease |
| v0.32 | Increased range of mouse sensitivity slider in gameplay options |
| v0.24 | Fixed action icons of inventory item tooltip breaking their scale and position when switching from mouse to gamepad while it is visible |
| v0.18 | Revamped mouse detection in book to make sure nothing gets in the way and prevent from clicking entries |

# Translation

### Update History

| Version | Changes |
| --- | --- |
| v0.71 | (Translations) Setup the various loading and error message in the MP screen to be translated, currently translated to: french |
| v0.69 | (Translations) Updated translations with some of recently added texts as well as some translation fixes |
| v0.69 | (Translations) Fixed regression with book camera management that prevented translation tags from being visible |
| v0.65 | (Translations) Fixed case of “added to backpack” dynamic text not translating |
| v0.65 | (Translations) Updated Finnish translation |
| v0.64 | (Translations) Added Czech, Italian, Polish, Finnish, Swedish and Turkish |
| v0.64 | (Translations) Updated German, Spanish, Portuguese, Russian, Korean, Chinese and Japanese |
| v0.64 | (Translations) Improved error detection in languages, notably with popup texts which could retain the last selected language value if current one was wrong |
| v0.64 | Fixed translations positioning in stats page of book |
| v0.63 | (Translation) Added missing translations keys in title scene, options menu, MP Screen, Hints, pause menu, items/meats inventory tooltips, todo list, tick off system, available recipes list |
| v0.63 | (Translation) Fixed texts missing/capitalisation/formating in title scene, options menu, MP Screen, book for the French language |
| v0.63 | (Translation) Added Spanish, Simplified Chinese an updated Portuguese |
| v0.62 | (Translation) Improved support for missing keys in translations files, labels now retain previous value for missing keys, if a font for a language isn't installed (or the game cannot reach it) the language won't be listed in options |
| v0.62 | (Translation) Added Chinese, German and Russian (all keys) |
| v0.62 | (Translation) Added Japanese, Korean, Portuguese (WIP, only 284 first keys) |
| v0.61 | (Translations) Fixed all HUD elements anchoring to allow proper positioning regardless of text size |
| v0.61 | (Translations) Setup translation as overlay in most of the book |
| v0.60 | Added first pass of translation system. This currently includes french language only. It is possible to copy translation files and replace the text values to create new translations – however more official translations will be coming in upcoming patch releases. |

# Occlusion

### Update History

| Version | Changes |
| --- | --- |
| v1.0 | Improved the look of ambient occlusion |
| v0.31 | Fixed sunshine occlusion not turning back on after being disabled and enabled again in options |
| v0.27 | (Visuals) Large scale ambient occlusion added to trees and plants |
| v0.25 | Fixed strange shading on fire built model due to wrong occlusion map |
| v0.20 | Forced volume light occlusion to take caves into account |
| v0.19 | Cut down trees are now accounted for by the tree occlusion system |
| v0.18 | New tree occlusion based draw distance calculation system (improves visual quality in open areas) |
| v0.16 | Graphics options: added new setting to turn off sunshine occlusion |
| v0.08d | Fixed some issues with skylight occlusion option |
| v0.06b | Optimized sky light occlusion performance |

# Shadows

### Update History

| Version | Changes |
| --- | --- |
| v1.0 | Fixed far shadow option still calculating even when disabled |
| v0.70 | (Performance) Animal shadows are now disabled at distance from the player |
| v0.69 | (Performance) Setting shadow quality to low or lower now disables shadow casting from the lighter (Performance) Far shadows are now always disabled while in caves (Performance) Now scaling down shadows at dawn and sunset to prevent it from stretching far away and causing excessive amount of objects being rendered and hindering performances |
| v0.68d | Fixed hotkeyed items not appearing in player shadow |
| v0.68 | (Performance) Tactical light turns off shadow when shadow quality setting is set to Low, Fastest or UltraLow |
| v0.60 | Fixed player hair not visible in player shadow! |
| v0.53 | Fixed flintlock gun smoke appearing overly bright in shadows or in caves |
| v0.48 | Improved far shadow and offscreen particles performance |
| v0.39 | Fixed soil in gardens not casting shadows and darkened dirt piles to make them easier to see |
| v0.36 | Improved shadows inside sinkhole |
| v0.32 | Fixed Grass/Shadows/Low memory settings not saved/restored properly |
| v0.31 | (Rendering) Cheap far distance shadows added (experimental) Cliffs are now double sided and shadow correctly when sun is behind them Added far shadow option to gfx menu Optimized shadows casted by plants and trees |
| v0.28 | (Optimization) Improved performance of cave shadow blockers, and rendering on cave wood panels when not in cave |
| v0.27 | (Rendering) Deferred skin shader improved: Subsurface scattering will only be applied on lights casting real time shadows |
| v0.22 | Lightning flash now casts shadows! |
| v0.21 | Fixed shadow blocking partially blocking climb exit in cave1 |
| v0.20 | Fixed bunch of overlapping cave shadow objects Fixed tree shadows turning off when coming from behind or side of player camera |
| v0.19 | Shadows now fade off to darkness when player is in a cave, and fade to bright when not in a cave |
| v0.18 | Shadows – Fixed bug where close shadows would flicker/break up even on highest shadow settings |
| v0.17 | Fixed volumetric lighting not shadowing through leaves |
| v0.15 | Fixed bugs that would sometimes cause log sled to fall through world. log sled should now collide with boulders and cliffs. Fixed log sled audio playing drop noise when in its trigger or being pushed. Log sled now casts a shadow |
| v0.13b | Fix for broken saved games (dark shadows, no time passing, sleeping at shelters broken and lots of other bugs in corrupt save games, along with low performance due to error spam) Note: Any new saved games started last night or early this morning will possibly be corrupted. If you notice dark shadows, no ambient light or other weird glitches, start a fresh save to make sure your game is up to date. |
| v0.10 | Tweaks to world lighting and fog/ambient colors. Lighter and plastic torch now cast shadows. New fluff particles added and using a new dust shader (bright in light, dark in shadow particle shader) Fixed enemy skin and player arms sometimes losing ability to receive shadow and appearing overbright (multiplayer) fixed bug where some shadows would break/change after respawning |
| v0.08d | (multiplayer)Player head added! (this also fixed issues with player head shadows in single player) Fixed glitchy shadows break up in distance! |
| v0.06 | Shadows Improved! Fisheye shadow distortion gives higher resolution shadow up close and now uses a single cascade (experimental, maybe cause some glitches) |
| v0.04b | Fixed issue with shadows light leaking |
| v0.03 | Player head added! And held items now correctly cast shadows |

# Draw Distance

### Update History

| Version | Changes |
| --- | --- |
| v0.40 | (Performance) Heavily optimized cost of stippling system for objects that aren't in viewing range (when using high draw distance it can lead to up to 2-3% FPS increase) |
| v0.28 | Increased skull lamp draw distance, and its light now fades in when enabled Fixed wrong settings on tree cut causing them to vanish on ultra low draw distance when exploded |
| v0.26 | Fixed garden plants popping on too close even on high draw distance settings Fixed rope mesh vanishing whilst climbing if player was on low draw distance setting Improved draw distance on outdoor old white tents Improved draw distance on thrown explosives and on built garden plants Improved draw distance on lake lily pads |
| v0.23 | (performance) Lowered rendering ranges for all lower draw distance settings (med/low/ultra low) |
| v0.20 | Ultra low draw distance is now more aggressive/culls items closer Improved draw distance on some items |
| v0.19 | Increased tree draw distance for the Ultra High draw distance setting |
| v0.18 | New tree occlusion based draw distance calculation system (improves visual quality in open areas) Improved lod system to reduce amount of objects when using low (66%) or ultra low (33%) draw distance setting |
| v0.17 | New low tree lod added when draw distance is High/Very High/Ultra High, increasing range before trees turn to billboards in distance Greeble Zones toggle distance now scales up accordingly with LOD ranges when Draw Distance quality setting is Very High or Ultra Changed name of Level of Detail in options menu to Draw Distance |
| v0.16b | Increased grass draw distance at highest settings |

# Depth of Field

### Update History

| Version | Changes |
| --- | --- |
| v0.32 | Re-enabled depth of field in graphics options |
| v0.31 | Removed depth of field from gfx options |
| v0.22 | New image effect: Depth of field (currently blurs player also, this is experimental and not recommended!) |

# Color Grading

### Update History

| Version | Changes |
| --- | --- |
| v1.0 | AA, bloom, dof, motion blur, chromatic aberration, grain, all are now using unity post processing. |
| v0.64 | Fixed Temporary shelter, Log Cabin, and Skull lamp ghosts appearing as white outlines regardless of color setting in options |
| v0.03 | 11 new filmic inspired grade options added to graphic options menu |

# Motion Blur

### Update History

| Version | Changes |
| --- | --- |
| v1.0 | Added new improved camera image effects for aa, bloom, motionblur chromatic aberration, eye adaptation and grain AA, bloom, dof, motion blur, chromatic aberration, grain, all are now using unity post processing. |
| v0.64 | Fixed issue with enemy motion blur sometimes not correctly enabling |
| v0.63b | Fixed player clothing variations missing correct motion blur setting |
| v0.63 | (Multiplayer) Fixed motion blur missing on some enemy types |
| v0.60 | (Optimization) Completely removed motion blur cpu cost when running a dedicated server (Optimization)Reduced cpu usage when motion blur is disabled in options |
| v0.52b | Fixed end game characters using excessive motion blur memory |
| v0.42 | Fixed bird on hand not motion blurring correctly |
| v0.39 | (Multiplayer) Added motion blur to items on metal tray |
| v0.34 | Fixed missing motion blur on mutant baby Fixed lighter flame breaking when camera moved due to motion blur! |
| v0.31 | (Performance) Amplify motion blur updated to latest release |
| v0.20 | Deer now have motion blur |
| v0.08d | Fixed issue where held weapons would get permanent motion blur on them |
| v0.08b | Improved motion blur performance on enemies and creatures |
| v0.08 | Improved motion blur quality,stability and memory usage |
| v0.05 | Motion blur now takes into account HDR Fixed plane crash crazy motion blur bug |
| v0.03 | Improved motion blur on held items |

# Bloom

### Update History

| Version | Changes |
| --- | --- |
| v1.0 | Added new improved camera image effects for aa, bloom, motionblur chromatic aberration, eye adaptation and grain AA, bloom, dof, motion blur, chromatic aberration, grain, all are now using unity post processing. |
| v0.56 | Changed order of offscreen particle rendering to account for image effects on main camera such as tone mapping and bloom |
| v0.26 | (performance) Tuned down bloom on 32 bits systems to limit memory usage |
| v0.22 | New physical bloom (faster and better looking) |
| v0.20 | (optimization) Bloom performance doubled |
| v0.16b | Fixed sparkly disco looking cave floors if bloom was enabled |
| v0.10 | Added clamp to tonemapper to stop it sometimes turning screen completely black if seeing a very bright pixel. Fixed related issue where bloom would sometimes cause screen to turn black if it found overbright pixels. |
| v0.08d | Improved bloom performance by 2-3x |
| v0.08b | Added bloom option to graphics menu (turning off will improve GPU performance on slower cards) |
| v0.05 | Improved bloom |

# Antialiasing, SSAO & HBAO

NVIDIA explanation on both these settings

### Update History

| Version | Changes |
| --- | --- |
| v1.0 | Added new improved camera image effects for aa, bloom, motionblur chromatic aberration, eye adaptation and grain AA, bloom, dof, motion blur, chromatic aberration, grain, all are now using unity post processing. |
| v0.65 | Replaced fxaa with a working version |
| v0.41 | Fixed issue with HBAO artifacts on ati cards Added low SSAO quality (effective with HBAO only) |
| v0.37 | New graphics option: SSAO Type ! Option are SESSAO (legacy) and the new HBAO (should render faster) New improved FXAA added! |
| v0.26 | Fixed medium preset using SMAA by default |
| v0.21 | New version of smaa added to antialiasing |
| v0.18 | New improved ssao with color bleeding Fixed bug where some particles would be drawn with a black box around them if ssao was disabled |
| v0.16 | Graphics options: SSAO setting now also changes sample count |
| v0.06b | Improved ssao! |

# Performance

### Update History

| Version | Changes |
| --- | --- |
| v1.08 | Fixed issue where some PC's could get stuck on R to load in Forest due to shader warm-up taking an extremely long time |
| v1.0 | Performance: Cleaned up a bunch of unused resources that were being kept in memory Performance: Optimized a bunch of textures, and fixed and removed a ton of old referenced textures and models that were no longer in game  Performance - removed deprecated items from the action icon atlas  Performance - improved cull grid performance  Performance - fixed some always on dynamic objects falling out of world at game start  Improved game start times!  Major memory improvements/reduction by removing unused assets and older duplicates of plants that were no longer being used |
