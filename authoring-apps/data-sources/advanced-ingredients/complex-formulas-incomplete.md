# Complex formulas \[incomplete\]

You can create complex formulas that use field math, combine multiple aggregate functions,  use conditional logic, and reference other ingredients

## Field math

You can add, subtract, multiply and divide numeric data fields. You can also use `+` with text data fields to concatenate. 

### Add, subtract, multiple, and divide

You can perform mathematical operations with data fields and constants. For example, if you have `revenue` and `cost` in your data, you can add a `Profit` measure like so: 

![Measure that subtracts two fields](../../../.gitbook/assets/image%20%2858%29.png)

Here are the underlying components:

```text
kind: Measure
field: sum(revenue - cost)
singular: Profit
plural: Profit
icon: hashtag
format: ',.2f'
```

If you divide by zero, you’ll get a null. If you do not specify an aggregate function, `sum()` will be implied. 

### Concatenate

You can use `+` to concatenate text data fields together. For example, if `LocationDesc` has state names and `LocationAbbr` has state abbreviations, this`States2` dimension will combine state names with state abbreviations to display like `Georgia (GA)`.

![Field math: concatenation](../../../.gitbook/assets/image%20%2856%29.png)

Here are the underlying components:

```text
kind: Dimension
field: LocationDesc + " (" + LocationAbbr + ")"
singular: State2
plural: States2
icon: map-marker-alt
latitude_field: Latitude
longitude_field: Longitude
```

## Multiple aggregate functions

You can combine multiple aggregate functions together. For example, if you have `sales_revenue` and `salesperson_id` in your data, you can add an `Avg Sales per salesperson` measure using the `sum()` and `count()` aggregate functions together like so: 

![Measure uses division and multiple aggregate functions](../../../.gitbook/assets/image%20%2854%29.png)

Here are the underlying components:

```text
kind: Measure
field: sum(total_sales) / count_distinct(salesperson_id)
singular: Avg Sales per salesperson
plural: Avg Sales per salesperson
icon: hashtag
format: ',.2f'
```

## Conditional logic

You can add conditional logic to formulas. Conditions are true/false statements that can be expressed in your formulas. Here are some examples of conditions:

```text
sales > 1000.0

# This uses a list
state IN ("Georgia", "Tennessee", "Virginia", "Texas", "South Carolina")

# You can use ANDs and ORs
sales > 1000.0 OR state = "Texas"

# Use IS NULL to compare for missing values
name IS NULL
```

To use conditions in formulas, use the `IF` function. This function contains pairs of conditions and values. A final value is used if none of your conditions match. Here is the `IF` function pattern:

```text
IF({condition1}, {value1}, {condition2}, {value2}, …, {else_value})
```

Here are examples for formulas that use the `IF` function:

```text
# A simple if  
sum(if(state="Texas", sales_dollars, 0.0))

# Multiple condition/value pairs
sum(if(state="Texas", sales_dollars*0.08, state="Georgia", sales_dollars*0.07, state="Tennessee", sales_dollars*0.0925, sales_dollars*0.055))

# You can use IF functions for both dimensions and metrics
if(last_name IS NULL, first_name, first_name + " " + last_name)
```

Here's an example of an conditional logic in a measure:

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

Here's an example of conditional logic in a dimension:

What if I only want certain calculations to happen conditionally? For instance, to only sum sales if the region is in the northeast.



