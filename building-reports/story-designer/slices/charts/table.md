# Table

The table chart displays selected dimensions and measures as columns in a table. Adding a slice with a table chart (i.e., a table slice) is a good choice when users want to see, search, sort, and download detailed data. By default, selecting rows will filter downstream results.

<figure><img src="../../../../.gitbook/assets/image (564).png" alt=""><figcaption><p>Example Table slice</p></figcaption></figure>

#### Adding a table slice

To add a table slice, select **Table** from the chart list.

**Configuring the table slice**

The CONFIG section has the following fields:

* **Table columns**: Select the dimension and measure ingredients to show in the table. They will appear in the order selected. You can drag ingredients to reorder them.

{% hint style="info" %}
Dimensions and measures with a number data type will be right-aligned within the table column; all other data types will be left-aligned.
{% endhint %}

* **Optionally add a breakout**: You can add breakout columns to your table to pivot a measure by a dimension. Pick a column to break out by (the breakout dimension) and a measure to break out. The table will show a column for each of the top values in the breakout dimension, with the measure calculated for each value. When a breakout is configured, additional options appear:
  * _Max breakout values_ — Set how many breakout columns to show (1–20). If there are more values than the maximum, an "Other" column aggregates the remaining values.
  * _Show "Other" column_ (default: on) — Toggle whether the "Other" aggregation column appears. This column is only relevant when there are more values than the max.
  * _Show all breakout values_ (default: off) — When enabled, breakout columns include values for all items in the breakout dimension, even those excluded by active filters.
  * _Sort breakout columns by measure_ (default: off) — When enabled, breakout columns are sorted in descending order of the aggregate measure value, so the highest-value columns appear first.
* **Enable download**: If enabled, users will be able to download the data.
* **File type**: If downloads are enabled, select Excel, CSV, or JSON for the download file type.
* **Hide if no data**: Toggle to hide the slice when no data is available.
* **Selections**: Controls how many selections a user can make and how those selections affect downstream slices.
* **Convert row selections into individual selections by dimension**: When a table uses multiple dimensions, row selections are sent downstream as compound selections by default (the full combination of dimension values is treated as a single filter). Enable this toggle to break compound selections into individual dimension filters. For example, if a table groups by Hospital and Department, enabling this toggle sends separate selections for Hospital and Department rather than a combined pair.

**Style options**

The STYLE section includes several options for customizing the table appearance. Key Table-specific options:

* **Max rows per load**: Enter the number of rows to load. The default value is 250.
* **Hide column icons**: If enabled, icons for all columns will be hidden.
* **Cell coloring**: Choose how measure cells are colored. The options are:
  * _None_ — No cell coloring (default).
  * _Measure Range Colors_ — Color cells based on the value ranges defined in the measure's ingredient editor. Each range maps to a specific color.
  * _Measure Pos/Neg Colors_ — Apply solid colors based on whether the value is positive or negative, using the measure's positive and negative color settings.
  * _Measure Colors Gradient_ — Apply a color gradient across cell values, scaling from the column's lowest to highest value. Uses the measure's positive and negative color settings for the gradient endpoints.

{% hint style="info" %}
Cell coloring colors are configured in the measure ingredient editor under the **Positive values** and **Negative values** color settings. When breakout columns are present, coloring is applied consistently across all breakout columns using a shared scale.
{% endhint %}

* **Sort column**: Set which column to sort on and the sort order for the initial sort. Users can override the sort order by clicking on a column header.
* **Spacing**: Choose between Default and Condensed row spacing.
* **Sticky header**: If enabled, the table header row stays visible as users scroll down through the table rows.
* **Striped rows**: If enabled, alternating rows have a subtle background color for readability.
* **Horizontal borders**: Toggle horizontal row borders.
* **Vertical borders**: Toggle vertical column borders.
* **Column widths**: Opens a popover where you can set a custom width for each column. Click **Reset** to return all columns to their default widths.

#### Using a table slice

**Searching**

Click the filter pill and search for any value in the table.

**Sorting**

Click on a column header to sort the data by the values in that column. Click again to reverse the sort order.

**Selecting rows**

Click a row to select it. Selections filter downstream slices based on the table's dimension values. Click a selected row to deselect it, or click the ✕ on the filter pill to clear all selections.

**Downloading data**

If data download is enabled, click on the **Data** button to download the data as the configured file type (Excel or CSV).
