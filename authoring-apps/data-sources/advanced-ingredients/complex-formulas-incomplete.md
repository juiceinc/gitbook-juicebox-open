# Complex formulas \[incomplete\]

## 

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

## Multiple aggregate functions

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

## References to other measures and dimensions

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



