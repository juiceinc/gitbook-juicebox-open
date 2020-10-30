# Data Sources

The Data Sources section of the app editor is where you set up your data sources. To access the Data Sources section, select the **Data** button at the top of the app editor. 

![Select Data to access Data Sources section](../../.gitbook/assets/image%20%2821%29.png)

You must [add a data source](loading-data.md) before you can design your story. A data source is made up of two things:  **data** and **data ingredients**.

## Data

The data can be a CSV or \(future release\) a table or view in a database or a Google Sheet. If your data is in a CSV, you upload the CSV. \(In a future release, if your data is in a database, you connect to the database and select the table or view that should be used. \)

### Supported data types

Here are Data types that are supported:

| data type | description |  |
| :--- | :--- | :--- |
| string | Variable-length character data | `882d8f4dccdb3d143df3cc06901f3399` |
| integer | Numeric values that do not have decimals | `46` |
| float | Numeric values that have decimal values | `53.5` |
| boolean | Values that denote either TRUE or FALSE | `True` or `False`  |
| date | A value for a date that includes the year, month, and day | `2020-10-30` |
| datetime | A value for a date and time that includes the year, month, day, hour, minute, second, and \(optionally\) subsecond | `2020-10-30 19:35:25.125456` |

## Data ingredients

Data ingredients \(or just **ingredients**\) are the basic building blocks used to build the charts in your story. There are two main types of ingredients: **measures** and **dimensions**. 

A **measure** is a value calculated over a group of data records. A **dimension** is used to define a group of data records.

{% hint style="info" %}
The word **aggregation** means "a group of data records." So you can also say that a measure is a value calculated over an aggregation, and a dimension is used to define an aggregation. 
{% endhint %}

{% hint style="success" %}
A good rule of thumb is that measures are calculated numbers and dimensions are categories of things. 
{% endhint %}

### Measures

Measures are a type of data ingredient. A measure is a value calculated over a group of data records. Average sales, student count, and maximum price are all examples of measures. 

Under the hood, measures use the following aggregation formulas: `sum()`, `avg()`, `min()`, `max()`, `count()`, and `count_distinct()`. If you do not specify an aggregation formula in the measure definition, then `sum()` will be implied. 

You can combine aggregation formulas and field math together to create complex measures, such as weighted averages. See [advanced ingredients](adding-ingredients/#advanced-ingredients).

Measure ingredients that are not advanced ingredients display as a pill with an aggregation, like so: 

![Measure ingredient with the sum\(\) aggregation](../../.gitbook/assets/image%20%2897%29.png)

Measure ingredients that are advanced ingredients display with a calculator icon, like so:

![Measure ingredient that is an advanced ingredient](../../.gitbook/assets/image%20%2895%29.png)

### Dimensions

Dimensions are a type of data ingredient. A dimension is used to define a group of data records. Students, states, and years are all examples of dimensions.

There are two special kinds of dimensions in Juicebox: [**place**](https://juicebox.gitbook.io/juicebox/authoring-apps/data-sources/add-a-data-source#place-ingredient) dimensions and [**time**](https://juicebox.gitbook.io/juicebox/authoring-apps/data-sources/add-a-data-source#time-ingredient) dimensions:

* A place dimension is a dimension that has an associated geographic location \(i.e., latitude and longitude\). Place dimensions are used in the [map](../story-designer/charts/map.md) chart. 
* A time dimension is a dimension that is a date. Time dimensions are used in the [trend](../story-designer/charts/trend.md) chart. 

Dimension ingredients display as a pill like so:

![Dimension ingredient](../../.gitbook/assets/image%20%2894%29.png)

