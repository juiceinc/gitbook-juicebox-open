# Preparing Your Data



What to avoid? \(i.e. what breaks an upload?\)

* column naming tips
* Supported data types:
  * string
  * integer?
  * float
  * boolean?
  * date
* Supported formats, especially for dates \(how do dates need to be formatted? can we include seconds?\)
* Things not to do, like empty cells \(why can't we have empty cells?\), and changing data structures, carriage returns, leading and trailing spaces in values and column names, weird formatting, strings in numeric fields, 
* and more

{% hint style="success" %}
After loading your data, do a quick review of the [initial ingredients](../create-a-data-source/#initial-ingredients) for anything inferred in an unexpected way. If you spot something unexpected, this indicates an issue with the data. Here are some common examples:

* Did a field that should only have numbers get inferred as a Dimension? That likely means you have non-numeric data in the column \(e.g., spaces, commas, "N/A", "null", or "-"\).
* Is a field name showing with unexpected underscores \(e.g., `_column_name_`, rather than `column_name`\)? That likely means there are leading or trailing spaces in your column headings.

Spotting, fixing, and re-loading these issues early will save you time and frustration down the road.
{% endhint %}

