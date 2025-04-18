# Map

The map chart displays a [place](../../ingredients/the-ingredient-editor/#place-column-editor) as a bubble on a map. Optionally, the bubble can be sized and colored by measures. Adding a slice with a map chart (i.e., a map slice) is a good choice when users want to see geographic information. &#x20;

## Adding a map slice

To add a map slice:

* select **Map** from the chart list

![Select Map from the dropdown](<../../../../.gitbook/assets/image (411).png>)

* select the [place column](../../ingredients/the-ingredient-editor/#place-column-editor) you want to display as a bubble on the map
* select a measure to use for the bubble size (optional)
* select a measure to use for the bubble color (optional)
* select a map style
* add slice text (optional)

![A map slice](<../../../../.gitbook/assets/image (461).png>)

{% hint style="info" %}
The map slice requires that you have a [place column](../../ingredients/the-ingredient-editor/#place-column-editor).  A place column is a special type of column that has associated latitude and longitude fields.
{% endhint %}

{% embed url="https://www.loom.com/share/ca34647fa6e646d0a8c90c4d4c28cb12" %}
Adding a map slice
{% endembed %}

## Using a map slice

You can hover over a map bubble to see details. Selections made in the map slice will filter downstream slices.&#x20;







### Place column editor

A place column is a special kind of column that has an associated geographic location (i.e., latitude and longitude). A place column is required by the [map](map.md) chart, and you create a place column when you add a map chart to your data story.&#x20;

![Place columns are created when you add a map chart](<../../../../.gitbook/assets/image (342).png>)

To create a place column, your data will need three fields:

1. A field that represents the name of the geographic location (e.g., city, state, country)
2. A field with the latitude value for each location
3. A field with the longitude value for each location

{% hint style="info" %}
The latitude and longitude fields in your data must be numbers, not strings. In other words, your latitudes should look like `38.8977` rather than `38.8977° N`. Likewise, your longitudes should look like `-77.0365`, rather than `77.0365° W`.
{% endhint %}

