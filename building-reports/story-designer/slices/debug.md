# Debug

The Debug panel helps report editors understand what's happening behind the scenes in each slice. It shows slice configuration, the data being returned, the SQL being generated, filtering, variables, and performance information.

{% hint style="info" %}
The Debug panel is only available to editors. Report viewers will not see it.
{% endhint %}

## Opening the Debug panel

When editing a draft report, the Debug panel is available from the editor side panel. Click on any slice to see its debug information.

You can also access the Debug panel on a published report by clicking the bug icon in the report header. This toggles debug mode on and off.

## Debug tabs

When you select a slice in the Debug panel, you'll see a set of tabs with different types of information. Not all tabs appear for every slice — only tabs with available information are shown.

### Config

The full configuration for the slice, showing how the slice is set up and how its data is fetched. This is useful for verifying that your slice is configured as expected.

### Variables

Shows variables passed to this slice from slices above it in the report. When upstream slices are configured to use [selections as variables](selections-as-variables.md), those selected values appear here. If this tab shows `{}`, either no upstream slices pass variables or nothing has been selected yet.

### Filtering

Shows two types of filters applied to this slice:

* **Automatic filters** based on selections made in slices above this one in the report
* **Data permissions** that limit what the current user is allowed to see

This is helpful for understanding why a slice might be showing unexpected results.

### Phases

Each data request is processed through a series of phases. This tab shows a table with each phase name, how long it took (in milliseconds), and its status. Use this to identify slow phases when troubleshooting performance.

### Ingredients

Ingredients are the SQL expressions used to define the data being fetched. This tab shows each ingredient's name, the SQL field expression, execution time, and whether it is bucketed. This is useful when verifying that your ingredient definitions are producing the expected SQL.

### Recipe SQL

Each recipe used by the slice gets its own tab (e.g., "Default SQL", "Summary SQL"). Each tab shows:

* **SQL** — The generated SQL query, with syntax highlighting and a copy button
* **Stats** — Execution time, number of rows returned, whether the result came from cache, and which cache region was used

Cached results save a database query and speed up response times. If you see `from_cache: Yes`, the data was served from cache rather than re-querying the database.

### Data

The actual data returned for the slice. You can toggle between two views:

* **Code view** — The raw data as JSON
* **Table view** — The data displayed in a table format

For filter slices, a separate Data tab is created for each dimension, so you can inspect the data for each filter independently.

### AI

When available, this tab shows AI-generated insights or suggestions related to the slice. This tab only appears when AI analysis has been generated.

### Error

If an error occurred while fetching data for this slice, this tab appears with details that can help diagnose the issue, including the error status and message.
