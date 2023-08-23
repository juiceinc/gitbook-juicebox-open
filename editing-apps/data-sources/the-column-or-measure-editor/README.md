# The column (or measure) editor

The **column editor** is a form used to edit a column. The **measure editor** is a form used to edit a measure. To access either editor, simply click on the pill for the column or measure you want to edit. &#x20;

![Access the column editor by clicking the column pill](<../../../.gitbook/assets/Column editor.gif>)

{% hint style="info" %}
If the options available in the column or measure editor are not sufficient to define your desired ingredient, you may need to add an [advanced column or measure](../advanced-ingredients/).&#x20;
{% endhint %}

## The column editor

Every column editor lets you modify the column's icon and labels (plural and singular). Depending on the [data type](../the-data-preview.md#data-types) of the underlying data field, you may also be able to modify the [number format](ingredient-formats.md) or [time format](time-formats.md). The column editor looks like this for most columns:

![The column editor](<../../../.gitbook/assets/image (458).png>)

{% hint style="info" %}
The editor for an [advanced column](../advanced-ingredients/) will look very different.
{% endhint %}

### Time column editor

A time column is a special kind of column that is automatically created from [date or time fields](../the-data-preview.md#data-types) in your data. The [trend](../../story-designer/charts/trend.md) chart requires a time column. You can modify the [time format](time-formats.md) for time columns. Here is an example of a time column labeled `Years` :

![The time column editor](<../../../.gitbook/assets/image (269).png>)

{% hint style="info" %}
If you do not have a time column for a date or time field in your data, the field may not be [formatted correctly](../../design-tips/preparing-your-data.md).
{% endhint %}

{% hint style="success" %}
Time ingredients will "roll up" in charts to the period selected for the Format. For example, selecting the `month yyyy` format will roll up to the month. Selecting the `yyyy` format will roll up to the year.&#x20;
{% endhint %}

### Place column editor

A place column is a special kind of column that has an associated geographic location (i.e., latitude and longitude). A place column is required by the [map](../../story-designer/charts/map.md) chart, and you create a place column when you add a map chart to your data story.&#x20;

![Place columns are created when you add a map chart](<../../../.gitbook/assets/image (342).png>)

Here is an example of a place column labeled `Countries` :

![The place column editor](<../../../.gitbook/assets/image (428).png>)

To create a place column, your data will need three fields:

1. A field that represents the name of the geographic location (e.g., city, state, country)
2. A field with the latitude value for each location
3. A field with the longitude value for each location

{% hint style="info" %}
The latitude and longitude fields in your data must be numbers, not strings. In other words, your latitudes should look like `38.8977` rather than `38.8977° N`. Likewise, your longitudes should look like `-77.0365`, rather than `77.0365° W`.
{% endhint %}

## The measure editor

The measure editor lets you modify the measure's icon, label, and [number format](ingredient-formats.md):

![The measure editor](<../../../.gitbook/assets/image (243).png>)

{% hint style="info" %}
The editor for an [advanced measure](../advanced-ingredients/) will look very different.
{% endhint %}

## Duplicating or deleting columns or measures

You can duplicate an existing column or measure from the editor by clicking the menu icon (<img src="../../../.gitbook/assets/ellipsis-h-solid.svg" alt="" data-size="line">) and selecting **Duplicate**.

![Duplicating a column or measure](<../../../.gitbook/assets/image (469).png>)

You can delete an existing column or measure from the editor by clicking the menu icon (<img src="../../../.gitbook/assets/ellipsis-h-solid.svg" alt="" data-size="line">) and selecting **Delete**.

![Deleting a column or measure](<../../../.gitbook/assets/image (120).png>)

{% hint style="info" %}
The **Duplicate as Advanced** menu option is used to create [advanced columns or measures](../advanced-ingredients/).
{% endhint %}
