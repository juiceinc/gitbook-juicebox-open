# Bar

The bar chart displays dimension values ranked by one or more measures. Each bar's length represents the value of a measure, making it easy to compare values across categories. Adding a slice with a bar chart (i.e., a bar slice) is a good choice when users want to compare measures between categories.

<figure><img src="../../../../.gitbook/assets/The Business of Movies - Bar1 - Mon Feb 16 2026.png" alt=""><figcaption></figcaption></figure>

#### Adding a bar slice

To add a bar slice, select **Bar** from the chart list.

**Configuring the bar slice**

The CONFIG section has the following fields:

* **Label**: Select a dimension to use as the bar categories (e.g., Genre, Region, Department).
* **Bars**: Select one or more measures. Each measure appears as a separate bar for each category. When multiple measures are present, the Visual style setting (in STYLE) controls whether bars are grouped side by side or stacked end to end.
* **Second dimension** (optional): Adds a sub-grouping within each bar category. For example, if your primary dimension is Genre and second dimension is Content Rating, each genre shows separate bars for each rating. A legend automatically appears for the second dimension values.
* **Hide if no data**: Toggle to hide the slice when no data is available.
* **Selections**: Controls how many selections a user can make and how those selections affect downstream slices.

{% hint style="info" %}
The **Positive values** and **Negative values** colors set in the measure ingredient editor directly control bar colors. Setting these overrides the default system-assigned colors.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

**Style options**

The STYLE section includes several options for customizing the chart appearance. Key Bar-specific options:

* **Visual style**: Controls how multiple measures or second-dimension values are displayed — "Grouped Bars" (side by side) or "Stacked Bars" (end to end).
* **Orientation**: Horizontal Bars (default) or Vertical Bars. Use horizontal when category labels are long.
* **Sort by**: Order bars by Label (alphabetical) or Value (by measure, descending).
* **Label width**: Controls the width of the label column — Narrow (1/8), Default (1/6), Medium (1/4), or Wide (1/3). Useful when category labels are being truncated.
* **Max bars per load**: Limits how many bars are shown initially. Enable "Show button to load more" to let users load additional bars.
* **Show data as**: Changes how bar values are displayed — # Value (default), % Percent of whole, or % Percent of sum.
* **Hide nulls**: Hides bars with null or missing values.
* **Value range options** (Minimum Value / Maximum Value): Set a fixed axis scale, useful when comparing multiple bar charts for consistent baselines.

{% hint style="info" %}
**Understanding "Show data as" options:**

* **# Value** (default): Shows the raw aggregated value for each bar.
* **% Percent of whole**: Each bar's value is compared to the global average across all categories, expressed as a percentage. A bar showing 150% means its value is 1.5× the overall average. The baseline is 100%.
* **% Percent of sum**: Each bar's value is shown as its share of the sum of all visible bar values. All bars add up to approximately 100%.

Percent of sum is only accurate when all bars are loaded (no "Load more" pagination). When a second dimension is present, percentage options are not available.
{% endhint %}

#### Using a bar slice

**Hover tooltips**

Hovering over a bar displays a tooltip showing the category name and all measure values, with color indicators matching the legend.

**Selecting bars**

Click a bar to select that category. Click additional bars to add to the selection. The filter pill updates to show the selection — a specific value for single selections (e.g., "Genre: Action") or a count for multiple selections (e.g., "2 Genres"). Click a selected bar to deselect it, or click the ✕ on the filter pill to clear all selections.

You can also click the search icon on the filter pill to open a dropdown with a search field and checkboxes for each category, which is useful when there are many values.

**Scrolling and pagination**

When there are more categories than fit in the chart area, users can scroll to see all bars. If Max bars per load is set, a "Load more" button appears to load additional bars.
