---
description: How to use formulas to create advanced data ingredients.
---

# Creating Advanced Data Ingredients \(Chris\)

As of Juicebox 3.49, When you upload a CSV you will get a version 2 data source.

What’s new in version 2? "Automagically" defined data ingredients get singular, plural, icon and format added. If the field is a string, date or boolean, it will get created as a Dimension, otherwise as Measure. In version 2 data sources, the terms Metric and Measure are interchangable.

Here’s an example of what you might get.

```text
facility:
  kind: Dimension
  singular: Facility
  plural: Facilities
  icon: check-square
sales_dollars:
  kind: Measure
  field: sum(sales_dollars)
  singular: "Sales Dollar"
  plural: "Sales Dollars"
  format: "$,.0f"
  icon: "usd"
total:
  kind: Measure
  field: sum(total)
  singular: "Total"
  plural: "Totals"
  format: ",.2f"
  icon: "hashtag"  
```

With version 2 you get a better starting point and can write functions in the field.

### An overview of defining ingredients with yaml

Ingredients.yaml is a way of defining ingredients that are connected to a SQLAlchemy selectable \(which can be a database table a query or another recipe\) when the query runs. **In Juicebox Open, the ingredients are connected to a csv you uploaded to bigquery.**

Here’s a sample 

```text
facility:
  kind: Dimension
  singular: Facility
  plural: Facilities
  icon: check-square
sales_dollars:
  kind: Measure
  field: sum(sales_dollars)
  singular: "Sales Dollar"
  plural: "Sales Dollars"
  format: "$,.0f"
  icon: "usd"
total:
  kind: Measure
  field: sum(total)
  singular: "Total"
  plural: "Totals"
  format: ",.2f"
  icon: "hashtag"  
```

If this was connected to the table definition MyTable, the above will create the same objects as this python code.

```text
shelf = {
    'zip': Dimension(MyTable.zip, singular='Zipcode', plural='Zipcodes'),
    'total_const_cost': Metric(func.sum(MyTable.const_cost),
      singular='Total Construction Cost',
      format='$,.0f')
    'avg_const_cost': Metric(func.avg(MyTable.const_cost),
      singular='Avg Construction Cost',
      format='$,.0f')
    'avg_issue_time': DivideMetric(func.sum(MyTable.date_issued 
             - MyTable.date_entered),
       func.count(MyTable.permit),
       singular='Avg Issue Time (Days)',
       format=',.0f')
}
```

### What’s new? Formulas 

Database columns are always referenced by a string. You can perform math on these columns as well as use aggregation functions like **count**, **count\_distinct**, **sum**, **min**, and **max**. If your database backend is Redshift \(or postgres\), you can also calculate percentiles and median with functions. If you divide two values; you’ll get a SQL-safe division \(which prevents divide by zeros\). If you divide by zero, you’ll get a null.

You can also define strings, using double quotes, numbers and lists.

Let’s look at some examples:

```text
full_name:
  kind: Dimension
  field: first_name + " " + last_name
avg_sales:
  kind: Measure
  field: avg(sales_dollars)
sales_tax:
  kind: Measure
  field: sum(total_revenue*0.0725)
avg_sales_per_salesperson:
  kind: Measure
  field: sum(total_sales) / count_distinct(salesperson_id)
```

### What about conditions? 

What if I only want certain calculations to happen conditionally? For instance, to only sum sales if the region is in the northeast.

Conditions are true/false statements that can be expressed in your formulas. Here are some examples.

```text
sales > 1000.0

# This uses a list
state IN ("Georgia", "Tennessee", "Virginia", "Texas", "South Carolina")

# You can use ANDs and ORs
sales > 1000.0 OR state = "Texas"

# Use IS NULL to compare for missing values
name IS NULL
```

### Using conditions in your formulas 

To use conditions in formulas, use the `IF` function. This function contains pairs of conditions and values.

`IF({condition1}, {value1}, {condition2}, {value2}, …, {else_value})`

A final value is used if none of your conditions match.

```text
# A simple if  
sum(if(state="Texas", sales_dollars, 0.0))

# Multiple condition/value pairs
sum(if(state="Texas", sales_dollars*0.08, state="Georgia", sales_dollars*0.07, state="Tennessee", sales_dollars*0.0925, sales_dollars*0.055))

# You can use IF functions for both dimensions and metrics
if(last_name IS NULL, first_name, first_name + " " + last_name)c
```

### Defining buckets in Dimensions 

Buckets are a convenient way of defining Dimensions using continuous variables. **In Juicebox Open; you’ll do this by making an advanced ingredient.** 

```text
grades:
  kind: Dimension
  field: grade
  buckets:
    - label: "Grade School"
      condition: 'in ("K", "1", "2", "3", "4", "5")'
    - label: "Middle School"
      condition: 'in ("6", "7", "8")'
    - label: "Grade School"
      condition: 'in ("9", "10", "11", "12")'
  buckets_default_label: Otherc
```

Buckets will evaluate their condition against the “field” but you can supply a full condition.

```text
sales_group:
  kind: Dimension
  field: grade
  buckets:
    # This first condition does not use the field because it contains its own
    - label: In-state
      condition: 'state = "Tennessee"'
    - label: Small
      condition: '<100.0'
    - label: Medium
      condition: '<1000.0'
  buckets_default_label: Large
```

The conditions within buckets are evaluated in the order they are defined.

