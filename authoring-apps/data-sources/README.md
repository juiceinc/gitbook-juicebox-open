# Data Sources

The Data Sources section of the app editor is where you set up your data sources. To access the Data Sources section, select the **Data** button at the top of the app editor. 

![Select Data to access Data Sources section](../../.gitbook/assets/image%20%2821%29.png)

You must set up at least one data source before you can design your story. A data source is made up of two things: 

1. data
2. data ingredients

## Data

The data can be a CSV, a table or view in a database, or \(coming soon!\) a Google Sheet. If your data is in a CSV, you upload the CSV. If your data is in a database, you connect to the database and select the table or view that should be used. 

## Data ingredients

**Data ingredients** \(or just **ingredients**\) are the basic building blocks used to build the charts in your story. There are two main types of ingredients: **measures** and **dimensions**. 

A **measure** is a value calculated over a group of data records. A **dimension** is a value used to define a group of data records. 

{% hint style="info" %}
The word **aggregation** means "a group of data records." So you can also say that a measure is a value calculated for an aggregation, and a dimension is a value used to define an aggregation. 
{% endhint %}

Perfectly clear, right? If not, you're not alone. We find the best way to understand the distinction between measures and dimensions is to just start building apps. Pretty soon, you'll get the hang of it. 

{% hint style="success" %}
A good rule of thumb is that measures are calculated numbers and dimensions are categories of things. 
{% endhint %}

### Measures

Measures are a type of data ingredient. A measure is a value calculated over a group of data records. Average sales, student count, and maximum price are all examples of measures. 

In defining measures, you can use the following formulas: `sum()`, `avg()`, `min()`, `max()`, `count()`, and `count_distinct()`. If you do not specify a formula in the measure definition, then `sum()` will be implied.

You can combine formulas and field math together to create complex measures, such as weighted averages. See [Defining advanced ingredients](create-a-data-source/advanced-ingredients.md).

### Dimensions

Dimensions are a type of data ingredient. A dimension is a value used to define a group of data records. Students, states, and years are all examples of dimensions.

There are two special kinds of dimensions: **place** dimensions and **time** dimensions. 

A place dimension is a dimension that has an associated geographic location \(i.e., latitude and longitude\). Place dimensions are used in the the [Map](../story-designer/charts/map.md) chart. 

A time dimension is a dimension that is a date **\[or datetime?**\]. Time dimensions are used in the [Trend](../story-designer/charts/trend.md) chart. 

