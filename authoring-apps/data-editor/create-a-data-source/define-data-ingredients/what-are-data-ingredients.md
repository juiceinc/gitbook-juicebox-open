# What are Data Ingredients?

**Data ingredients** are the data elements that are used to construct your visualizations. There are two main types of ingredients: **measures** and **dimensions**. 

A **measure** is a value calculated over a group of data records. A **dimension** is a value used to define a group of data records. 

{% hint style="info" %}
The word **aggregation** means "a group of data records." So you can also say that a measure is a value calculated for an aggregation, and a dimension is a value used to define an aggregation. 
{% endhint %}

Perfectly clear, right? If not, you're not alone. We find the best way to understand the distinction between measures and dimensions is to work with [some examples](../../../more-about-measures-and-dimension.md). 

## Measures

A **measure** is a value calculated over a group of data records. Average sales, student count, and maximum price are all examples of measures. 

In defining measures, you can use the following formulas: `sum()`, `avg()`, `min()`, `max()`, `count()`, and `count_distinct()`. If you do not specify a formula in the measure definition, then `sum()` will be implied.

You can combine formulas and field math together to create complex measures, such as weighted averages. These are covered in [Advanced Ingredients](v2-syntax.md).

## Dimensions

A **dimension** is a value used to define a group of data records. Students, states, and years are all examples of dimensions.

There are two special kinds of dimensions: **place** dimensions and **time** dimensions. 

A **place** dimension is a dimension that has an associated geographic location \(i.e., latitude and longitude\). Place dimensions can be used with the Map slice. 

A **time** dimension is a dimension that is a date **\[or datetime?**\]. Time dimensions can be used with the Trend slice. 





