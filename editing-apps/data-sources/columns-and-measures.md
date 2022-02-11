# Columns and measures

## Columns

Every field in your data will become a column available for use in charts. Each column is displayed as a pill in the data preview like this:

![A column pill](<../../.gitbook/assets/image (386).png>)

### Special columns: Place and Time

There are two special kinds of columns in Juicebox: **place** and **time.**

* A place column associates a location field with latitude and longitude fields. The [map](../story-designer/charts/map.md) chart requires a place column. You will need to have both latitude and longitude fields in your data in order to create a place column. &#x20;

{% hint style="info" %}
You [add a place column](the-column-or-measure-editor/#place-column-editor) when you add a [map](../story-designer/charts/map.md) chart to your data story.&#x20;
{% endhint %}

* A time column is created from a field that has a date or time [data type](the-data-preview.md#data-types). The [trend](../story-designer/charts/trend.md) chart requires a time column.&#x20;

## Measures

As you add measures to your [charts](../story-designer/charts/), measures (also called "column measures") are created. A measure is a value calculated over a group of data records. Average sales, student count, and maximum price are all examples of measures. Under the hood, measures use the following aggregation formulas: `sum()`, `avg()`, `min()`, `max()`, `count()`, and `count_distinct()`.

Measures (except advanced measures) display as pills with an aggregation badge, like so:&#x20;

![Measure with the sum() aggregation](<../../.gitbook/assets/image (347).png>)

From time to time, you may need to create a more complex measure, such as a weighted average, that uses multiple aggregation formulas or combines aggregations with conditional logic, field math, or other things. You can do this using an [advanced measure](advanced-ingredients/).&#x20;

Measures that are advanced measures display with a calculator icon, like so:

![An advanced measure](<../../.gitbook/assets/image (312).png>)



You can click on the pill at any time to open the [column (or measure) editor](the-column-or-measure-editor/).&#x20;
