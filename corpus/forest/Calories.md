# Calories
Source: https://theforest.fandom.com/wiki/Calories
Categories: Stats
Revision: 74926

**Calories** are stat and game mechanic that was fully implemented in v0.71. It has replaced the point system and it is designed to regulate weight and strength. As of v1.0, it is only used in Hard Survival Mode.

# Gameplay

On the release of v0.71, the developers did an almost total re-work of the strength and stats system. **Calories** are now displayed in the inventory for each food item when you hover over them, and gaining strength, or weight or improving athleticism should seem more natural. Previously you could become overweight and it would take many in game days of barely eating to get back to a reasonable weight.

# Calorie Consumed

The following items and their **calorie** amounts.

## Meats

| State | Arm | Leg | Lizard Meat | Rabbit Meat | Meat | Fish | Small Meat |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Listed | 600 | 600 | 600 | 600 | 600 | 500 | 300 |
| Fresh Cooked | 600 | 600 | 600 | 600 | 600 | 500 | 300 |
| Edible Cooked | 600 | 600 | 600 | 600 | 600 | 500 | 300 |
| Spoiled Cooked | 600 | 600 | 600 | 600 | 600 | 300 | 300 |
| Fresh Dried | 600 | 600 | 600 | 600 | 600 | 600 | N/A |
| Edible Dried | 600 | 600 | 600 | 600 | 600 | 600 | N/A |
| Spoiled Dried | 300 | 300 | 300 | 300 | 300 | 150 | N/A |
| ALL Burnt | 300 | 300 | 300 | 300 | 300 | 250 | 150 |
| ALL Stewed | 600 | 600 | 600 | 600 | 600 | 600 | 600 |

## All other foods

| Food | Listed Calories | Actual Calories | Stew Calories | Stew IF meat is added |
| --- | --- | --- | --- | --- |
| Blueberries | 1 | 1 | 0 | 1 |
| Snowberries | 1 | 1 | N/A | N/A |
| Twinberries | 1 | 1 | N/A | N/A |
| Blackberries | 1 | 1 | N/A | N/A |
| Aloe Vera | 1 | 1 | 0 | 5 |
| Chicory | 1 | 1 | 0 | 5 |
| Coneflower | 1 | 1 | 0 | 5 |
| Marigold | 1 | 10 | 0 | 5 |
| Amanita Mushroom | 10 | 10 | 0 | 10 |
| Chanterelle Mushroom | 10 | 10 | 0 | 10 |
| Deer Mushroom | 10 | 10 | 0 | 10 |
| Jack Mushroom | 10 | 10 | 0 | 10 |
| Liberty Cap Mushroom | 10 | 10 | 0 | 10 |
| Puff Mushroom | 10 | 10 | 0 | 10 |
| Oyster | 10 | 10 | 0 | 0 |
| Snack | 400 | 400 | N/A | N/A |
| Soda | 400 | 400 | N/A | N/A |
| Booze | 400 | 400 | N/A | N/A |
| Plane Meal | N/A | 200 | N/A | N/A |
| Head | N/A | N/A | 600 | 600 |

# Mechanics

This is a list of actions that burn calories and their amounts:

| Action | Amount | Explanation |
| --- | --- | --- |
| Jumping | 2 Per Second | Jumping burns 2 calories per second |
| Fight Action Calories | 7 Per Action | Swinging a weapon burns 7 calories per swing |
| Stationary | 0.06 Per Second | Standing still burns 0.06 calories per second |
| Walking | 0.5 Per Second | Walking burns 0.5 calories per second |
| Sprinting | 1 Per Second | Sprinting/Running burns 1 calorie per second |
| Swimming | 1.5 Per Second | Swimming burns 1.5 calories per second |
| Carrying logs | 0.5 Per Second | Carrying logs burns 0.5 calories per second. This will stack on top of sprinting and walking if applicable |
| Weight Gain | 0.00015 Per EXCESS Calories | For every calorie that the player is in excess, they will gain 0.00015 weight when the weight timer resets (in the morning on single player) |
| Weight Loss | 0.00015 Per MISSING Calories | For every calorie that the player is missing, they will loss 0.00015 weight when the weight timer resets (in the morning on single player) |
| Strength Gain | 0.0010 Per Calorie | ? |
| Strength Loss | 0.0001 Per Calorie | ? |
| Fight Action Strength | 0.0047 Per Action | You gain 0.0047 strength every time you swing your weapon. Swinging you weapon is the only way you can gain strength. |

## Update history

| Version | Changes |
| --- | --- |
| v1.0 | Calories text in stats pages and inventory item tooltip is hidden unless in a hard survival game Calories are now always considered positive and lead to gaining strength unless in hard survival difficulty mode. |
| v0.72 | Fixed herbs not having calorie stat |
| v0.71b | Calories system balance pass, should make weight and strength more manageable Fixed dried meat eaten from inventory having the calories applied twice  Added calories display in stats page  Fixed blue berries, soda, fish, meat and oysters yielding wrong calories amount or having wrong displayed amount |
| v0.71 | Nutrition System Revamp: Consuming edible items now yields calories on top of fullness, doing physical activities counts as burnt calories and strength, excess calories are resolved and transformed in weight and strength gain or loss Calories are now listed in the food and drinks when hovered over in inventory |
