# Trend

The trend chart displays a measure plotted over time. Adding a slice with a trend chart (i.e., a trend slice) is a good choice when users want to see how a measure changes over time.

<figure><img src="../../../../.gitbook/assets/The Business of Movies - Trend1 - Mon Feb 16 2026 (1).png" alt=""><figcaption></figcaption></figure>

### Adding a trend slice

To add a trend slice, select **Trend** from the chart list.

#### Configuring the trend slice

The CONFIG section has the following fields:

* **Dates**: Select a Date or Time column for the x-axis.&#x20;
* **Breakout** (optional): Select a category dimension to split the trend into separate lines, one per category value. Breakout requires exactly one measure — remove any extra Y Axis measures and clear the Second Y Axis before adding a breakout. The maximum number of breakout lines is configurable in STYLE settings (default: 10).
* **Y Axis**: Select up to 5 measures for the primary y-axis.
* **Second Y Axis** (optional): Select 1 measure for a secondary y-axis. This measure gets an independent scale on the right side of the chart, which is useful when measures have very different ranges.
* **Hide if no data**: Toggle to hide the slice when no data is available.
* **Selections**: Controls how many selections a user can make and how those selections affect downstream slices.

{% hint style="info" %}
The trend chart requires a time column. A time column is created from date or time fields in your data. The time format selected for the time column will determine how your dates "roll up" in your trend chart. For example, if you select the format `month yyyy`, the trend chart will roll up by month. If you select the format `yyyy`, the trend chart will roll up by year.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (602).png" alt=""><figcaption></figcaption></figure>

#### Style options

The STYLE section includes several options for customizing the chart appearance:

* **Accumulate measures**: Switches the chart from showing per-period values to cumulative running totals. Each data point shows the sum of all values up to that point.
* **Show gridlines**: Adds horizontal gridlines for readability.
* **Date format** (DATES X AXIS): Override the ingredient-level time format at the slice level.
* **Y-axis options** (PRIMARY Y AXIS / SECONDARY Y AXIS): "Use nice numbers" rounds axis labels, "Start at zero" anchors the axis, "Maximum Value" sets an upper bound.
* **Max breakout lines** (BREAKOUT): Controls how many category lines appear when using breakout (default: 10).

### Using a trend slice

#### Hover tooltips

Hovering over a point on the trend line shows the time period and all measure values. Each measure is color-coded to match its corresponding line in the legend.

#### Selecting date ranges

Click or drag on the chart to select a date range. The selection appears as a filter pill above the chart (e.g., "Year 1990 to 2000"). How selections affect downstream slices depends on the Selections configuration — "as Filters" filters downstream slices to that date range, while "as Variables" saves the date range in variables.

#### Missing data

Dates in the data that are missing values will show a break in the trend line.
