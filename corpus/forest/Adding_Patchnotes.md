# Adding Patchnotes
Source: https://theforest.fandom.com/wiki/Adding_Patchnotes
Categories: Help
Revision: 63564

Patchnotes Formatted - Link to the patch notes that are formatted.

One of the easiest ways to help The Forest Wiki is to update the patchnotes on relevant pages, this will also score you HEAPS of wiki points and it's VERY easy!

## Using The Find Function On Your Browser

Each browser is different has to how to find the search function.

* Firefox - Pressing  `CTRL + F`  will open up the search function on the bottom left by default
* Chrome - Pressing  `CTRL + F`  will open up the search function on the top right by default
* Internet Explorer - Pressing  `CTRL + F`  will open up the search function on the top left by default
* Edge - Pressing  `CTRL + F`  will open up the search function on the top left by default

### Example of Search

For example: Searching 'Oyster' will provide all these results

```
| [[v0.56]] || (Multiplayer) Fixed dropping spoilt oysters
| [[v0.55]] || Fixed spoilt oysters not drop-able from the inventory
| [[v0.50]] || Fixed eating spoilt oysters not having the spoilt meat poison effect
| [[v0.47]] || Fixed eating oysters not working
| [[v0.35]] || Fixed oysters starting with the “none” decay state
| [[v0.23b]] || Fixed bug where most oyster spawners were placed too far below sea level and set to wrong terrain texture – making them extremely rare. Also fixed issue where they wouldn’t be visible, only the pickup icon in rare case they were found
| [[v0.23]] || New item added: Oyster. Can be found in ocean, can be stored in backpack and eaten but has limited shelf life
```

You can then add the notes to their relevant page by using copy and paste:

* Copy:  `CTRL + C`
* Paste:  `CTRL + V`

## Patch Note Template Formatting

### Formatting Between Different Patches

Ensure there is a `|-` between each patch line.

**CORRECT**

```
== Update history==
{| class="wikitable"
|-
! Version !! Changes
| [[v0.56]] || (Multiplayer) Fixed dropping spoilt oysters
|-
| [[v0.55]] || Fixed spoilt oysters not drop-able from the inventory
|-
|}
```

**INCORRECT**

```
==Update history==
{| class="wikitable"
|-
! Version !! Changes
| [[v0.56]] || (Multiplayer) Fixed dropping spoilt oysters
| [[v0.55]] || Fixed spoilt oysters not drop-able from the inventory
|-
|}
```

### Formatting With The Same Patch

If a patch has two changes then remove the patch number at the front and move it to the next line like this:

**CORRECT**

```
== Update history==
{| class="wikitable"
|-
! Version !! Changes
| [[v0.67]] || Fixed log on zipline offsetting from the zipline rope if placed while standing too close from the zipline and within collision range of player
(Multiplayer) Improved log on zipline movement smoothing
|-
|}
```

**INCORRECT**

```
== Update history==
{| class="wikitable"
|-
! Version !! Changes
| [[v0.67]] || Fixed log on zipline offsetting from the zipline rope if placed while standing too close from the zipline and within collision range of player
| [[v0.67]] || (Multiplayer) Improved log on zipline movement smoothing
|-
|}
```

## Patch Note Template

Some pages don't have the patch note table added to them. Once a page lists an element of the game that has had a patch change, then this table should be added:

```
==Update History==
{| class="wikitable"
|-
! Version !! Changes
|-
| 
|-
|}
```

The patch note section should be at the bottom of page, after the gallery section but before the category.
