# Data Sources

Before you can design your data story, you need to set up at least one data source. A data source is a combination of two things: \(1\) data and \(2\) data ingredients.  

## Data

The data itself can be a CSV, a table or view in a database, or \(coming soon!\) a Google Sheet. If your data is in a CSV, you upload the CSV. If your data is in a database, you connect to the database and select the table or view that should be used. 

## Data ingredients

**Data ingredients** are the data elements that are used to construct the charts in your data story. There are two main types of ingredients: **measures** and **dimensions**. 

A **measure** is a value calculated over a group of data records. A **dimension** is a value used to define a group of data records. 

{% hint style="info" %}
The word **aggregation** means "a group of data records." So you can also say that a measure is a value calculated for an aggregation, and a dimension is a value used to define an aggregation. 
{% endhint %}

Perfectly clear, right? If not, you're not alone. We find the best way to understand the distinction between measures and dimensions is to just start building apps. Pretty soon, you'll get the hang of it. But a good rule of thumb is that measures are calculated numbers and dimensions are categories. 

### Measures

A **measure** is a value calculated over a group of data records. Average sales, student count, and maximum price are all examples of measures. 

In defining measures, you can use the following formulas: `sum()`, `avg()`, `min()`, `max()`, `count()`, and `count_distinct()`. If you do not specify a formula in the measure definition, then `sum()` will be implied.

You can combine formulas and field math together to create complex measures, such as weighted averages. These are covered in [Advanced Ingredients](create-a-data-source/define-data-ingredients/advanced-ingredients.md).

### Dimensions

A **dimension** is a value used to define a group of data records. Students, states, and years are all examples of dimensions.

There are two special kinds of dimensions: **place** dimensions and **time** dimensions. 

A **place** dimension is a dimension that has an associated geographic location \(i.e., latitude and longitude\). Place dimensions can be used with the [Map](../story-designer/charts/map.md) chart. 

A **time** dimension is a dimension that is a date **\[or datetime?**\]. Time dimensions can be used with the [Trend](../story-designer/charts/trend.md) chart. 

