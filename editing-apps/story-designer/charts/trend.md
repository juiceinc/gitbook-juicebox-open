# Trend

The trend chart displays a measure plotted over time. Adding a slice with a trend chart (i.e., a trend slice) is a good choice when users want to see how a measure changes over time. &#x20;

## Adding a trend slice

To add a trend slice:

* select **Trend** from the chart list

![](<../../../.gitbook/assets/image (327).png>)

* select the [time column](../../data-sources/columns-and-measures.md#special-columns-place-and-time) to use for the x-axis
* select up to 5 measures to display on a single y-axis
* select 1 measure to display on a second y-axis (optional)
* add slice text (optional)
* click **Save**

![](<../../../.gitbook/assets/image (251).png>)

{% hint style="info" %}
Because the trend chart requires a [time column](../../data-sources/columns-and-measures.md#special-columns-place-and-time). A time column is created from date or time fields in your data. The [time format](../../data-sources/the-column-or-measure-editor/time-formats.md) selected for the time column will determine how your dates "roll up" in your trend chart. For example, if you select the format `month yyyy`, the trend chart will roll up by month. If you select the format `yyyy`, the trend chart will roll up by year.&#x20;
{% endhint %}

{% embed url="https://www.loom.com/share/b5520e0548fa4ab59d3284efd3f792ae" %}
Adding a trend slice
{% endembed %}

## Using a trend slice

You can hover over individual points to see more detail. Date range selections made in the trend slice will filter downstream slices.&#x20;

Dates in the data that are missing values will show a break in the trend line, like so:

![The trend line has a break because household\_size is null for all 1973 dates](<../../../.gitbook/assets/image (91).png>)



###

###
