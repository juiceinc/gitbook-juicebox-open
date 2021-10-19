# Columns and measures

## Columns

Every field in your data will become a column available for use in charts.&#x20;

Each column is displayed as an orange pill like this:

![A column](<../../.gitbook/assets/image (94).png>)

### Special columns: Place and Time

There are two special kinds of columns in Juicebox: [**place**](broken-reference) and [**time**](broken-reference)**.**

* A place column associates a location field with latitude and longitude fields. The [map](../story-designer/charts/map.md) chart requires a place column. You will need to have both latitude and longitude fields in your data in order to create a place column. &#x20;

{% hint style="info" %}
You add a place column when you add a [map](../story-designer/charts/map.md) chart to your data story.&#x20;
{% endhint %}

* A time column is created from a field that has a date or time [data type](the-data-preview.md#data-types). The [trend](../story-designer/charts/trend.md) chart requires a time column.&#x20;

## Column measures

As you add measures to your [charts](../story-designer/charts/), column measures (or measures) will be added. A measure is a value calculated over a group of data records. Average sales, student count, and maximum price are all examples of measures. Under the hood, measures use the following aggregation formulas: `sum()`, `avg()`, `min()`, `max()`, `count()`, and `count_distinct()`.

Measures (except advanced measures) display as orange pills with an aggregation, like so:&#x20;

![Measure with the sum() aggregation](<../../.gitbook/assets/image (97).png>)

From time to time, you may need to create a more complex measure, such as a weighted average, that uses multiple aggregation formulas or field math. You can do this using an advanced measure.&#x20;

Measures that are advanced measures display with a calculator icon, like so:

![An advanced measure](<../../.gitbook/assets/image (95).png>)



You can click on the orange pills at any time to open the [column (or measure) editor](the-column-or-measure-editor/).&#x20;
