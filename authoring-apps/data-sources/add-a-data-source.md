# Add a data source

There are two steps to adding a data source: 

1. upload or connect to your data
2. add your data ingredients

## Upload or connect to your data

You can upload a CSV or \(coming soon!\) connect to a database table or view or a Google Sheet.

### Upload a CSV

To upload a CSV, click **Connect & Upload Data Sources**, select **CSV**, and then select the CSV file to be uploaded. In about 15-30 seconds, the **table view** will pop up, confirming that your data was loaded and providing a preview of your data. When you click out of the table view, you will see the [**initial ingredients** ](add-a-data-source.md#initial-ingredients)that have been inferred from your data. 

{% hint style="warning" %}
When using CSVs, it is important that your data be nice and clean. Common problem areas include missing data ****and text values in numeric columns. Here are some tips for [preparing your data](../design-tips/preparing-your-data.md). 
{% endhint %}

{% embed url="https://www.loom.com/share/242f7cfe0e5c4c54b6ee6f8b9ffe3eaa" caption="Upload a CSV" %}

{% hint style="success" %}
After loading your data, do a quick review of the table view for anything unexpected. If you spot something unexpected, this usually indicates an issue with the data. Here are some common examples:

* Do any numeric fields have a`string`data type? That likely means you have non-numeric data in the column \(e.g., spaces, commas, "N/A", "null", "-"\). Any field you plan to use in a sum or average calculation must have the`number`data type. 
* Do any data fields have a`string`data type? That likely means you have non-date data in the column. Any date fields you want to use in a [trend](../story-designer/charts/trend.md) chart must have the`date`data type. 
* Does a field name have unexpected underscores \(e.g., `_column_name_`, rather than `column_name`\)? That likely means there are leading or trailing spaces in your column headings.

Spotting and fixing these issues early and re-loading your data will save you time and frustration down the road.
{% endhint %}

#### Replace CSV

When previewing a CSV Data Source table view, there is a button top right in the modal to "Replace CSV". This allows you to update your rows/values, and add more columns. However, keep in mind that changing previously existing column field names in the data source may break connections with your existing ingredients.

### Connect to a database table or view \(coming soon!\)

### Connect to a Google Sheet \(coming soon!\)

## Add your data ingredients

Data ingredients are the basic building blocks for every chart in your app. So before you can add charts to your app, you'll need ingredients.

### Initial ingredients

When you load or connect to your data, Juicebox will inspect a sample of your data and create an ingredient for each column in your data based on its best guess. These initial ingredients are also called **inferred ingredients** and follow these rules:

* If the column contains only numeric values, a **measure** ingredient will be inferred.
* If the column contains only date values, a **time** dimension ingredient will be inferred.
* If the column contains values other than numeric or date values, a **dimension** ingredient will be inferred. 

The initial ingredients are just a starting point. You can revise them or add new ones using the **ingredients editor**.  

### Ingredients editor

Adding or revising ingredients is done using the ingredients editor. The ingredients editor is a form that you fill out to define your ingredient. The form varies somewhat by type of ingredient because different ingredient types require somewhat different [components](defining-ingredients/ingredient-components.md). 

To access the ingredients editor for an ingredient, click on the ingredient pill. You can click on an ingredient pill in either the Data Sources or the Story Designer sections of the app editor.

![Access ingredients editor by clicking ingredient pill](../../.gitbook/assets/open-ingredients-editor.gif)

Below are examples of the ingredient editor for the different ingredient types \(dimension, place, time, and measure\) as well as the underlying components for each ingredient.

### Dimension Ingredient

A dimension is an ingredient that is used to define a group of data records. Students, states, and years are all examples of dimensions. Here is the `Categories` dimension from the Unhealthy Americans app.:

![Dimension definition](../../.gitbook/assets/image%20%2846%29.png)

And here are the underlying components:

```text
kind: Dimension
field: StratificationCategory1
singular: Category
plural: Categories
icon: hashtag
```

### Place Ingredient

A place dimension is a special kind of dimension ingredient that has an associated geographic location \(i.e., latitude and longitude\). A place dimension is required by the [map](../story-designer/charts/map.md) chart. Here is the `States` place dimension from the Unhealthy Americans app:

![Place dimension definition](../../.gitbook/assets/image%20%2853%29.png)

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

A time dimension  is a special kind of dimension ingredient that uses a date field. A Time dimension is required by the [trend](../story-designer/charts/trend.md) chart. Here is the `Year Dates` time dimension from the Unhealthy Americans app:

![Time dimension definition](../../.gitbook/assets/image%20%2851%29.png)

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

![Measure definition](../../.gitbook/assets/image%20%2835%29.png)

And here are the underlying components:

```text
kind: Metric
field: avg(Data_Value)
singular: Data Value
icon: hashtag
format: ',.2f'
```

#### Advanced Ingredient

If the options available in the ingredients editor are not sufficient to define your desired ingredient, you will need to add an [advanced ingredient](advanced-ingredients/). 

