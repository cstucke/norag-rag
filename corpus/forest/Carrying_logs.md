# Carrying logs
Source: https://theforest.fandom.com/wiki/Carrying_logs
Categories: Gameplay
Revision: 74883

**Carrying logs** is when the player carries one or two logs, collecting them and dropping them. It has effects on the player that are often unnoticed.

## Gameplay

**Carrying logs** will prevent the player from entering combat. They will need to drop the logs to fight. If the player enters water while **carrying logs**, they will drop the logs. Generally the player cannot collect logs on water while they are swimming. If the logs are under the water, the player is able to collect them, though it is rather bugged.
When the player is **carrying logs**, they will burn more energy. **Carrying Logs** will burn 1 calories Per Second. The energy consumption is increase when the player is carrying two logs instead of one. When the player drops logs, they will drop at their right side. If the player jumps while dropping logs, the logs will be more likely to roll away as they have collected speed on the fall. This can be used to drop logs down a hill to a specific location.

## Effects

* Burns 1 calories Per Second.
* Increases energy consumption, 2 logs carried will burn more than 1

## Controls

* Collecting logs - `E`
* Dropping logs - `G`
* Storing logs - `C`

## Actions

* **Actions that will drop logs**
  + Opening the survival guide
  + Entering water
  + Picking up animal heads
  + Death
  + Activating boat controls
  + Activating a log sled
* **Prevented actions when carrying logs**
  + Combat
  + Blocking
  + Cutting down trees
* **Actions that can be performed while carrying logs**
  + Use left hand items
  + Walking
  + Sprinting
  + Jumping
* **Actions prevent collecting logs**
  + Swimming (unless under water - might be a bug)
  + Operating a boat
  + Pushing a log sled

## Update history

| Version | Changes |
| --- | --- |
| v0.69 | Fixed held logs colliding awkwardly when quickly dropped by player |
| v0.67 | Fixed UI widget staying visible if grabbing log quickly from log holder after it gets destroyed |
| v0.66 | Looking at a damaged structure (not needing logs for repair) while holding a log no longer shows the repair widget and instead shows the missing repair tool icon |
| v0.58 | (Multiplayer) Fixed dropping logs as client sometimes shooting the player up into the air Fixed cases of dropped logs flying off when dropped close to other physics objects |
| v0.57 | Fixed held log hand animation sometimes being slow to respond after picking up a log Fixed dropped logs not colliding with log sleds |
| v0.55 | Player dropped logs now spawn slightly away from player to prevent physics interaction issues |
| v0.53 | Fixed player not grabbing log sled correctly if a bird is landing on his finger at the same time |
| v0.52 | Ghost wall type switch is no longer concurrent with the regular ghost interaction trigger (both can be used at the same time, regardless of holding log or not) |
| v0.47 | Fixed player/player\_net held log still using old model and textures |
| v0.46 | Fixed player movement slowing down when trying to open survival book while carrying a log |
| v0.45 | Picking up small rocks/tennis balls when holding logs no longer drops the logs |
| v0.41 | Setup new log model on wall, foundations, log pickup (Multiplayer) Enabled physics on log pickups for clients so that they may push logs |
| v0.37 | (Multiplayer) Fixed picking up logs in holder while jumping causing it to vanish, it now properly drops the log |
| v0.35 | **Player now drops held logs when swimming** Fixed log pickups sometimes having the E action icon visible from far away Fixed picking up held only item (i.e.: small rock) while holding logs causing the small rock to vanish, now logs will be dropped and the item equipped |
| v0.34 | (Audio) Added exertion sound when a log is dropped |
| v0.32 | Fixed logs dropped in caves spawning above terrain |
| v0.29 | **(Balance) Lowered log transportation energy cost** |
| v0.27 | **(Multiplayer) Fixed another log-dupe bug (sorry!)** **(Performance) cut down trees now use pooled log pickups, limited to 100 instances (oldest ones get removed if new one are created past the limit)** |
| v0.22 | Improved cleaning up equipped stuff when dying (drops body, logs...) |
| v0.20b | Fixed bug where it wasn't possible to pull out lighter (or other left hand item) when carrying a log |
| v0.18 | (multiplayer) Fixed log duplication bug |
| v0.13 | **Player is no longer able to pick up logs while jumping, swimming, sailing raft or pushing sled** **Equipped logs are now dropped when beginning to swim, sail a raft or push a sled** (multiplayer)Fixed delay where log would remain visible for a short period of time even after being picked up by clients |
| v0.11 | (multiplayer) Fixed log duplication bug, where it was possible to spawn multiple logs when picking up up a log |
| v0.10 | (multiplayer)Fixed some Log duplication bugs |
| v0.08b | Energy now drains faster when carrying logs (and faster still if carrying two logs) |
| v0.08 | Better looking log held model |
| v0.06 | Carry log animation added to player |
| v0.03 | Fixed log going to -1 if you died whilst holding a log |
