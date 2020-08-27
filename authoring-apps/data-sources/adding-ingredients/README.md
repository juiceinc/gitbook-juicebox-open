---
description: The second step in adding a data source is adding ingredients.
---

# Adding ingredients

There are two steps to adding a data source: 

1. upload or connect to your data
2. add your data ingredients

This section covers the second step.  \(The first step is covered [here](../add-a-data-source.md).\)

After loading data, you're ready to add data ingredients. Data ingredients are the basic building blocks for every chart in your app. So before you can add charts to your app, you'll need ingredients. 

There are three ways to add ingredients: add ingredients "automagically", add ingredients one at a time, or duplicate existing ingredients. You can use all three methods to create the ingredients you need for your data story. 

## Adding ingredients "automagically"

Adding ingredients "automagically" allows you to quickly add ingredients so you can dive into designing your story. To add ingredients automagically,

1. navigate to the [table view](../add-a-data-source.md#the-table-view) 
2. select the **Add Automagically** button
3. select the the fields you want to add as data ingredients
4. select the **Add Selected** button. 

Juicebox will inspect the selected fields and create an ingredient for each based on its best guess, according to these rules:

* If the field contains only numeric values, a **measure** ingredient will be created.
* If the field contains only date values, a **time** dimension ingredient will be created.
* If the field contains values other than numeric or date values, a **dimension** ingredient will be created. 

The automagically added ingredients are just a starting point. You can revise them using the [**ingredient editor**](./#ingredient-editor).  

{% hint style="warning" %}
You cannot convert from one ingredient type to another. For example, you cannot create a place dimension ingredient from a measure ingredient. Therefore, the ingredient you select for duplication will need to be of the desired ingredient type. Alternatively, you can add a new ingredient of the desired type using the [this method](./#adding-ingredients-one-at-a-time). 
{% endhint %}

{% embed url="https://www.loom.com/share/1bb19adb302444ea8a7302b778997b8f" caption="Adding ingredients using Add Automagically button" %}

## Adding ingredients manually

Sometimes the ingredients created through the automagic method will not be what you need. For example, let's say you have `year`  in your data. Because the `year` values are integers, the automagic method will create a new measure ingredient. But you will probably want a dimension ingredient instead.

To have more control over the type of ingredient that is created, you can add the ingredient manually from the [table view](../add-a-data-source.md#the-table-view), 

1. click the **+** next to the field you want to use in the new ingredient
2. select the type of ingredient you want to create from the available options
3. define the ingredient in the [ingredient editor](../add-a-data-source.md#ingredients-editor)

{% embed url="https://www.loom.com/share/68e5589825f44dca960da8897b7f08f0" caption="Adding ingredients manually from the table view" %}

### Ingredient editor

The ingredient editor is a form that you fill out to define your ingredient. The form varies somewhat by type of ingredient because different ingredient types require somewhat different [components](ingredient-components.md). 

To access the ingredient editor for an existing ingredient, click on the ingredient pill. You can click on an ingredient pill in either the Data Sources or the Story Designer sections of the app editor.

![Access the ingredient editor by clicking ingredient pill](../../../.gitbook/assets/open-ingredients-editor.gif)

Below are examples of the ingredient editor for the different ingredient types \(dimension, place, time, and measure\) as well as the underlying components for each ingredient.

### Dimension Ingredient

A dimension is an ingredient that is used to define a group of data records. Students, states, and years are all examples of dimensions. Here is the `Categories` dimension from the Unhealthy Americans app.:

![Dimension definition](../../../.gitbook/assets/image%20%2846%29.png)

And here are the underlying components:

```text
kind: Dimension
field: StratificationCategory1
singular: Category
plural: Categories
icon: hashtag
```

### Place Ingredient

A place ingredient is a special kind of dimension ingredient that has an associated geographic location \(i.e., latitude and longitude\). A place ingredient is required by the [map](../../story-designer/charts/map.md) chart. Here is the `States` place ingredient from the Unhealthy Americans app:

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

### Time Ingredient

A time ingredient is a special kind of dimension ingredient that uses a date field. A Time ingredient is required by the [trend](../../story-designer/charts/trend.md) chart.  Time ingredients are automatically created from data fields with the proper [formatting](../../design-tips/preparing-your-data.md#10-confirm-date-columns-contain-only-dates-with-date-formatting-or-nulls).

{% hint style="warning" %}
At this time, the trend chart requires that dates be on the [first day of the month](../../design-tips/preparing-your-data.md#11-add-first-day-of-the-month-dates). 
{% endhint %}

Here is the `Year Dates` time ingredient from the Unhealthy Americans app:

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

### Measure Ingredient

A measure is a value calculated over a group of data records. Average sales, student count, and maximum price are all examples of measures. Here is the `Data Value` measure from the Unhealthy Americans app:

![Measure definition](../../../.gitbook/assets/image%20%2835%29.png)

And here are the underlying components:

```text
kind: Metric
field: avg(Data_Value)
singular: Data Value
icon: hashtag
format: ',.2f'
```

#### Advanced Ingredient

If the options available in the ingredient editor are not sufficient to define your desired ingredient, you will need to add an [advanced ingredient](../advanced-ingredients/). 

## Duplicating an existing ingredient from within the ingredient editor

You can add a new ingredient by duplicating an existing ingredient. To do this, open the ingredient editor for the ingredient you want to duplicate. From there, select the menu icon \(![](../../../.gitbook/assets/ellipsis-h-solid.svg)\) and select **Duplicate**. 

![Duplicating an ingredient](../../../.gitbook/assets/image%20%2877%29.png)

This will duplicate the ingredient and open the ingredient editor for the duplicated ingredient. Revise the ingredient definition as needed and save.

![Ingredient editor for the duplicated ingredient](../../../.gitbook/assets/image%20%2878%29.png)

