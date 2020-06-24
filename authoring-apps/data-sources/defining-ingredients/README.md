# Adding ingredients

Ingredients are added using the ingredients editor. To access the ingredients editor for an ingredient, click on the ingredient pill. \(You can select ingredient pills in either the Data Sources or the Story Designer sections of the app editor.\)

![Access the ingredients editor by clicking on an ingredient pill](../../../.gitbook/assets/image%20%2834%29.png)

Below are examples of the ingredients editor for the different ingredient types \(dimension, place, time, and measure\).

## Dimension

A dimension is an ingredient that is used to define a group of data records. Students, states, and years are all examples of dimensions. Here is the `Categories` dimension from the Unhealthy Americans app. 

![Dimension definition](../../../.gitbook/assets/image%20%2846%29.png)

And here are the underlying components:

```text
kind: Dimension
field: StratificationCategory1
singular: Category
plural: Categories
icon: hashtag
```

## Place dimension

A place dimension is a special kind of dimension ingredient that has an associated geographic location \(i.e., latitude and longitude\). A place dimension is required by the [map](../../story-designer/charts/map.md) chart. 

![Place dimension definition](../../../.gitbook/assets/image%20%2853%29.png)

And here are the underlying components:

```text
kind: Dimension
field: LocationDesc
singular: State
plural: States
icon: map-marker-alt
latitude_field: Latitude
longitude_field: Longitude
```

## Time dimension

A time dimension  is a special kind of dimension ingredient that uses a date field. A place dimension is required by the [trend](../../story-designer/charts/trend.md) chart. 

![Time dimension definition](../../../.gitbook/assets/image%20%2851%29.png)

And here are the underlying components:

```text
kind: Dimension
field: Year_Date
singular: Year Date
plural: Year Dates
icon: calendar
format: '%b %d, %Y'
```

## Measure

A measure is a value calculated over a group of data records. Average sales, student count, and maximum price are all examples of measures. 

![Measure definition](../../../.gitbook/assets/image%20%2835%29.png)

And here are the underlying components:

```text
kind: Metric
field: avg(Data_Value)
singular: Data Value
icon: hashtag
format: ',.2f'
```

{% hint style="info" %}
If the options available in the ingredients editor are not sufficient to define your desired ingredient, you will need to add an [advanced ingredient](../advanced-ingredients/). 
{% endhint %}

## 

