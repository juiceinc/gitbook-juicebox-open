# Defining ingredients

## Basic ingredients

After uploading or connecting your data, a set of [initial ingredients](./#initial-ingredients) will be created. Here’s an example of what you might get.

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

```text
# a basic summing metric

active:
  kind: Metric
  field: sum(active)
  singular: 'Active Cases'
  plural: 'Active Cases'
  format: ',.0f'
```

These are just a starting point. You can add additional ingredients by.... You will be able to.... You will not be able to.... **\[TODO: insert based on ingredients editor UI\]**.

## Advanced ingredients

Most of your ingredients will be basic ingredients. But in cases where you need to do something more with the `field` and `format` than the basics, you can use advanced ingredients. Advanced ingredients allow you to use--

* Dimensions that group values into "buckets" based on conditions **\[TODO: What is the difference between buckets and quickselects?\]**
* Dimensions that display a lookup value rather than the field value
* Measures that use field math
* Measures that combine multiple formulas
* Measures and dimensions that reference other measures and dimensions
* Measures and dimensions that include conditional logic
* Measures formatted using any d3 number format
* Date dimensions formatted using any d3 date format

## Bucketed dimensions

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

## Quickselect filtering

## Lookup dimensions

## Field math

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

## Combining multiple formulas

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

## Referencing other measures and dimensions

Referencing other dimensions or metrics is supported using the "@" syntax.

```text
# recovered_change references existing metrics 
# @current_recovered and @previous_recovered to calculate change

recovered_change:
  kind: Metric
  field: 'sum(@current_recovered) - sum(@previous_recovered)'
  singular: 'Change in Deaths'
  plural: 'Change in Deaths'
  format: '"+",0f; ,0f'
```

## Conditional logic

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



```text
# a conditional metric. If the column is a datetype (like last_update) 
# you can use readable syntax to check dates

previous_active:
  kind: Metric
  field: 'if(last_update = "two days ago", active)'
  singular: 'Active'
  plural: 'Active'
  format: ',0f'
```

## Advanced number formats

## Advanced date formats







