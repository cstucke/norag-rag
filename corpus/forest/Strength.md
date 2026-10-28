# Strength
Source: https://theforest.fandom.com/wiki/Strength
Categories: Stats
Revision: 72400

**Strength** is a player stat that was added in v0.29 update along with weight, athleticism, and sanity. As of V0.71, the system for raising **strength** has been completely over hauled. It now runs on a calories and exercise system.

## Gameplay Effects

**Strength** affects the damage of melee weapons, the higher your strength, the more damage you can do. It increases weapon damage by `% of bonus damage = (Strength * 100 / 140)`.
For example, if you have 70 Strength: `70 * 100 / 140` = +50% bonus damage. This calculator can show you exactly how much bonus damage you can get with your current strength:

**Strength** has no effect on thrown or ranged weapons, such as the flintlock pistol, crafted bow, modern bow, and throwing spears.

Having the blood infection status effect will lower the player's strength until the player consumes aloe to heal it.

## Raising Strength

Certain actions affect raising **strength** depending on your current net calorie count.

As of V0.73, when performing an attack (regular or power), `ΔStrength = ±(Calories Eaten - Calories Burnt) * 0.0047`. Meaning you gain or lose 0.0047 depending on whether you had surplus calories (gain) or lost calories (lose) when you performed the attack.

For example, if you ate 2800 calories, and burnt 3000: `(2800 - 3000) * 0.0047`, your `ΔStrength = -0.94`.

* You can only gain or lose 2 **strength** per day. However, this count can be reset with saving and exiting. This will allow the player gain as much strength as they can in one day. Once the cap has been reached, calories will continue to burn though no gains or losses will be made to strength.
* Calories are required for strength to be gained. If calories burnt are higher than calories consumed, you will lose strength.
* The only way to raise strength is by swinging a weapon. There is no other way to currently raise strength.
* Console Commands can provide an on screen HUD display of your stats, this can make raising strength much easier as you don't have to check your survival guide.

Key:
`ΔStrength` = Change in strength.

`±` = Plus or minus.

## Guide

## Farket's Tips and Tricks

These tips and tricks are provided by Farket on YouTube:

* "Calorie loading" is the method I recommend for raising strength and maintaining weight. You need 3000 calories to raise 2 strength which takes 426 swings of a weapon. As soon as you wake, consume about 3000 to 4000 calories. This will last you the entire day and you won't have to worry about checking your stats throughout the day. Once the sun is starting to set, start swinging a bone to burn the rest of the calories and raise strength. You can either stand still and do it (use an auto hotkey if you know how to assign one). Or you can use the bone on stick trees. This will gather hundreds of leaves as well as a lot of sticks, whilst raising strength.
* Using a bone as a method of raising strength is currently the best way. Bones only use 3 stamina per swing. The amount that it uses is so low, that you can swing indefinitely without running out of stamina, even with 0 athleticism.
* Calories are calories, it doesn't matter if you use 10 cans of soda or eating meat. As long as you have calories, you will raise strength.
* Keep your weight between 200 and 210. If your weight goes under 200, you will receive penalties towards strength. If it goes over 210, you will receive penalties towards athleticism. The more it goes above or below these ranges, the higher the penalty.
* Avoid gaining weight as weight is much harder to lose than it is to gain, just like in real life.
* Your weight only changes ONCE per day. Ignore the arrow until that time comes. The exact time is just as the sun rises. You will see a bright glow of the sun, then it will disappear. This is the exact time that your calories reset and your weight changes. If you have excess calories, you will gain weight. If you have more burnt calories, you will lose weight. The higher the difference, the more the weight change.
* Swinging a bone for 4 minutes and 10 seconds burns about 3000 calories and gains two strength. There are 36 minutes and 34 seconds in a day. Based on this, you would be able to gain 14 to 15 strength in one day, if you save and exit after reaches 2 strength each time. If you were to do this for 15 strength, you would need over 23444 calories and you would need to take 3192 swings with a bone. This method would drive someone insane if they did not have an auto attack key assigned (look into macros). The ideal place to do this is in the main cannibal village's cave. Drop down into the cave, build a temporary shelter, swing and raise your strength, save and exit. Once you return, go up the rope in the cannibal village and get all the soda boxes, there's over 7 boxes which would provide over 7000 calories each time. Keep doing this and you could max your strength out in under 7 days. Though this would be VERY boring in that span of time.

### Myths

* Increasing strength does not allow you to carry more than 2 logs, you can only carry 2 logs no matter your strength.
* Strength does not increase blocking effects
* You do not need to sleep to raise **strength**. Though this will speed up the process but you will need to be more active with eating.

## Important VR problems

* VR players can not gain any strength through chopping trees and/or enemies

## Gallery

## Update History

| Version | Changes |
| --- | --- |
| v1.0 | Calories are now always considered positive and lead to gaining strength unless in hard survival difficulty mode. |
| v0.71b | Fixed old saves resetting the strength stat value (if not saved over) |
| v0.71 | We did an almost total re-work of the strength and stats system. Calories are now displayed in the inventory for each food item when you hover over them, and gaining strength, or weight or improving athleticism should seem more natural. Previously you could become overweight and it would take many in game days of barely eating to get back to a reasonable weight. Nutrition System Revamp: Consuming edible items now yields calories on top of fullness, doing physical activities counts as burnt calories and strength, excess calories are resolved and transformed in weight and strength gain or loss Nutrition System Revamp: Consuming edible items now yields calories on top of fullness, doing physical activities counts as burnt calories and strength, excess calories are resolved and transformed in weight and strength gain or loss Calories are now listed in the food and drinks when hovered over in inventory |
| v0.68 | Strength now updates 100 times per in game day instead of once per day. This makes changes to strength easier to track. (UI) Better looking up & down arrows in stats page for Strength and Weight Added trend display to strength in stats page Removed strength and athleticism red cross icons when having food & blood infection Stats page now displays an approximation of the Athleticism skill level progress as a decimal value Athleticism is now displayed on a 1-99 scale to match strength (underlying values remain the same) Removed strength and athleticism red cross icons when having food & blood infection Stats page now displays an approximation of the Athleticism skill level progress as a decimal value Athleticism is now displayed on a 1-99 scale to match strength (underlying values remain the same) |
| v0.46 | Physical exercise is now taken into account in the character weight formula so that exercising a lot slows down gaining weight when over fed and speeds up loosing weight if underfed |
| v0.42 | New poisoned effect: when shot with poisoned arrows enemy movement is slowed and damage output is reduced for a short time |
| v0.37 | When having a healthy diet, weight now goes towards base value at a very slow rate (player no longer stays at a bad weight when being healthy and instead goes back to normal) |
| v0.31 | Chocolate bars and soda now give overeating points when used |
| v0.29 | Added new “Strength” stat. Goes up every day while eating well and chopping trees. Goes down when over exerted and underfed Being overweight lowers Athleticism Combined Run & Underwater Breathing silent skills into ‘Athleticism’ stat which goes up from both swimming and running New “Sanity” system. Sanity goes down when killing an enemy, chopping limbs, a lot when eating an enemy and slowly while in caves. Sanity goes up when sleeping, listening to music, eating fresh non limb meat and slowly while restoring energy on bench. Viewable in stats page of book. |
