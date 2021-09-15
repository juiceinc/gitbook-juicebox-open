# Data

The Data section of the editing panel is where you set up your data sources. To access the Data section, select the **Data** tab at the top of the editing panel. 

![Select the Data button to set up and manage data sources](../../.gitbook/assets/image%20%28228%29.png)

You must [add a data source](loading-data.md) before you can design your story. A data source is made up of two things: **data** and **data ingredients**. 

## Data

The data can be a CSV or a table in a database. [Load your data](loading-data.md) by either uploading the CSV or, if your data is in a database, selecting the schema and table to connect to. \(Connecting to data in databases will be enabled in a future release. For now, if you want to connect to a database, please reach out to us by clicking the chat button below. \)

### Supported data types

Here are data types that are supported:

| Data type | Description | Example |
| :--- | :--- | :--- |
| string | Variable-length character data | `882d8f4dccdb3d143df3cc06901f3399` |
| number | Numeric values, either with or without decimals | `46` or `53.5` |
| boolean | Values that denote either TRUE or FALSE | `True` or `False` |
| date | A value for a date that includes the year, month, and day | `2020-10-30` |
| timestamp | A value for a date and time that includes the year, month, day, hour, minute, second, and \(optionally\) subsecond | `2020-10-30 19:35:25.125456` |

## Data ingredients

Data ingredients \(or just **ingredients**\) are the basic building blocks used to build the charts in your story. There are two main types of ingredients: **measures** and **dimensions**. 

A **measure** is a value calculated over a group of data records. A **dimension** is used to define a group of data records.

{% hint style="success" %}
A good rule of thumb is that measures are calculated numbers and dimensions are categories of things. 
{% endhint %}

### Measures

Measures are a type of data ingredient. A measure is a value calculated over a group of data records. Average sales, student count, and maximum price are all examples of measures. 

Under the hood, measures use the following aggregation formulas: `sum()`, `avg()`, `min()`, `max()`, `count()`, and `count_distinct()`. If you do not specify an aggregation formula in the measure definition, then `sum()` will be implied. 

You can combine aggregation formulas and field math together to create complex measures, such as weighted averages. See [advanced ingredients](adding-ingredients/#advanced-ingredients).

Measure ingredients that are not advanced ingredients display as an orange pill with an aggregation, like so: 

![Measure ingredient with the sum\(\) aggregation](../../.gitbook/assets/image%20%2897%29.png)

Measure ingredients that are advanced ingredients display with a calculator icon, like so:

![Measure ingredient that is an advanced ingredient](../../.gitbook/assets/image%20%2895%29.png)

To review and edit a measure ingredient definition, click on its orange pill. This will open the [**ingredient editor**](adding-ingredients/#ingredient-editor). From there, you can change the measure's field, aggregation formula, label, format, or icon. 

### Dimensions

Dimensions are a type of data ingredient. A dimension is used to define a group of data records. Students, states, and years are all examples of dimensions.

There are two special kinds of dimensions in Juicebox: [**place**](adding-ingredients/#place-ingredient) dimension and [**time**](adding-ingredients/#time-ingredient) dimension:

* A place dimension is a dimension that has an associated geographic location \(i.e., latitude and longitude\). Place dimensions are used in the [map](../story-designer/charts/map.md) chart. 
* A time dimension is a dimension that is a date. Time dimensions are used in the [trend](../story-designer/charts/trend.md) chart. 

Dimension ingredients display as a pill like so:

![Dimension ingredient](../../.gitbook/assets/image%20%2894%29.png)

To review and edit a dimension ingredient definition, click on its orange pill. This will open the [ingredient editor](https://app.gitbook.com/@juicebox/s/juicebox-open/~/drafts/-Ma8Bt7dTu7rysKLxD5V/editing-apps/data-sources/adding-ingredients#ingredient-editor). From there, you can change the field, labels, or icon.

