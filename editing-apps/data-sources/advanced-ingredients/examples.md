---
description: A collection of Advanced Ingredient examples by use case
---

# Examples

**Hide dimension labels**

You could use `id_field` on an Advanced Dimension column to preserve selection filtering while also providing the `field` with an empty string:

```
field: string(" ")
id_field: last_name
```
