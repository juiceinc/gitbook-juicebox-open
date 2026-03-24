# Debug

Debug information helps report editors understand what's happening behind the scenes in each slice. It shows slice configuration, the data being returned, the SQL being generated, filtering, variables, and performance information.

{% hint style="info" %}
Debug information is only available to editors. Report viewers will not see it.
{% endhint %}

## Accessing debug information

There are two ways to open the **Debug All Slices** window:

* **While editing a draft report**, click the no-bug icon next to any slice name in the editing panel, or click the no-bug icon that appears on the slice itself in the report.
* **In Preview mode or on a published report**, first toggle debug mode on by clicking the no-bug icon in the upper-right corner of the report header. This makes a no-bug icon appear on each slice. Then click a slice's no-bug icon to open the Debug All Slices window.

The Debug All Slices window shows a list of all slices on the left (with response times) and tabbed debug details on the right. You can select any slice to view its information.

## Debug tabs

The tabs shown depend on the selected slice. Not all tabs appear for every slice — only tabs with available information are shown.

### Config

The full configuration for the slice, showing how the slice is set up and how its data is fetched. This is useful for verifying that your slice is configured as expected.

### Filtering

Shows two types of filters applied to this slice:

* **Automatic filters** based on selections made in slices above this one in the report
* **Data permissions** that limit what the current user is allowed to see

This is helpful for understanding why a slice might be showing unexpected results.

### Ingredients

Ingredients are the SQL expressions used to define the data being fetched. This tab shows each ingredient's name, the SQL field expression, execution time, and whether it is bucketed. This is useful when verifying that your ingredient definitions are producing the expected SQL.

### Phases

Each data request is processed through a series of phases. This tab shows a table with each phase name, how long it took (in milliseconds), and its status. Use this to identify slow phases when troubleshooting performance.

### SQL

Each recipe used by the slice gets its own SQL tab (e.g., "Base SQL", "Summary SQL"). Some slices have a single SQL tab, while others have multiple. Each tab shows:

* **SQL** — The generated SQL query, with syntax highlighting and a copy button
* **Stats** — Execution time, number of rows returned, whether the result came from cache, and which cache region was used

Cached results save a database query and speed up response times. If you see `from_cache: Yes`, the data was served from cache rather than re-querying the database.

### Variables

Shows variables passed to this slice from slices above it in the report. When upstream slices are configured to use [selections as variables](selections-as-variables.md), those selected values appear here. If this tab shows `{}`, either no upstream slices pass variables or nothing has been selected yet.

### Data

The actual data returned for the slice. You can toggle between two views:

* **Code view** — The raw data as JSON
* **Table view** — The data displayed in a table format

For filter slices, a separate Data tab is created for each dimension, so you can inspect the data for each filter independently.

### Error

If an error occurred while fetching data for this slice, this tab appears with details that can help diagnose the issue, including the error status and message.
