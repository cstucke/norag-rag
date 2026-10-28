# Module:ProcessArgs/doc
Source: https://theforest.fandom.com/wiki/Module:ProcessArgs/doc
Categories: Wiki test pages
Revision: 64365

Template:Documentation header
This module allows arguments to be merged and normalised. This also has the side-effect of making the arguments a real table instead of an empty table with a metatable to access the args. This allows the `#` operator to work, as well as allowing new values to be added to the table, without being ignored when iterating.

The `norm` function will normalise the arguments passed to it, trimming whitespace and setting empty arguments to `nil`. If a table isn't passed to the function, it will automatically get the current frame's parent arguments table.

The `merge` function will merge two tables together, overwriting duplicate values from the first table with the second table's value, as well as doing the same as the `norm` function if the norm parameter is `true`.
If the first parameter isn't a table, it is used as the value for the norm parameter, and it will automatically get the current frame's directly passed arguments table and merge it with the current frame's parent arguments table.
