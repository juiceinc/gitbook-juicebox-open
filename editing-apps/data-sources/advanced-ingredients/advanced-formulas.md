# Advanced formulas

You can create advanced formulas that use field math, combine multiple aggregate functions, and use conditional logic.

## Field math

You can add, subtract, multiply and divide numeric data fields. You can also use `+` with text data fields to concatenate. 

### Add, subtract, multiple, and divide

You can perform mathematical operations with data fields and constants. For example, if you have `revenue` and `cost` in your data, you can add a `Profit` measure like so: 

![Measure ingredient using subtraction](../../../.gitbook/assets/image%20%28215%29.png)

Here are the underlying components:

```text
field: sum(revenue - cost)
kind: Measure
format: '$,.0f'
```

If you divide by zero, you’ll get a null. If you do not specify an aggregate function, `sum()` will be implied. 

### Aggregation functions

Aggregation functions let you add up values for a field. If no aggregation function is provided for a  measure, `sum()` will be used. 

| Function | Examples |
| :--- | :--- |
| Sum | `sum(sales_dollars)` or `sum(revenue - expenses)` |
| Minimum | `min(age)` |
| Maximum | `max(age)` |
| Average | `avg(home_value)` |
| Count | `count(student_name)` or `count(*)` |
| Count only distinct items | `count_distinct(student_name)` |
| Median | `median(sales_dollars)` |
| Percentiles expressed as `percentileN`. Allowed values of N are 1, 5, 10, 25, 50, 75, 90, 95, and 99. | `percentile1(age)` or `percentile75(sales_dollars)` |

{% hint style="danger" %}
When you upload a CSV file, percentiles and medians are calculated as approximate values. The statistically exact value may be slightly different.
{% endhint %}

### Conversion functions

Conversion functions change the value for a field. It might change to a different type or to a different time period.

| Function | Examples |
| :--- | :--- |
| Round to the nearest week \(requires a date field\) | `week(sales_date)` |
| Round to the nearest month \(requires a date field\) | `month(sales_date)` |
| Round to the nearest quarter \(requires a date field\) | `quarter(sales_date)` |
| Round to the nearest year \(requires a date field\) | `year(sales_date)` |
| Convert a numeric value to a string | `string(zipcode)` |
| Convert a string value to an integer | `int(age)` |
| Calculate an age at the current date.  | `age(birth_date)` |

### Concatenating text fields

You can use `+` to concatenate text data fields together. For example, if `LocationDesc` has state names and `LocationAbbr` has state abbreviations, this`States2` dimension will combine state names with state abbreviations to display like `Georgia (GA)`.  

![Dimension ingredient using concatenation](../../../.gitbook/assets/image%20%28227%29.png)

Here are the underlying components:

```text
kind: Dimension
field: LocationDesc + " (" + LocationAbbr + ")"
singular: State
latitude_field: Latitude
longitude_field: Longitude
```

{% hint style="warning" %}
You must use double quotes in field expressions to define string constants. Single quotes will not work. 
{% endhint %}

If you want to concatenate fields that do not have the `string` data type, you'll need to first convert the field to a string using the [conversion function](advanced-formulas.md#conversion-functions) `string()`. For example, if you want to concatenate `address`, `state`, `city`, and `zip` together, but `zip` is not a string, you'll need to define the ingredient like so:

![Using string\(\) to convert number to string](../../../.gitbook/assets/image%20%28245%29.png)

## Using multiple aggregation functions

You can combine multiple aggregate functions together. For example, if you have `sales_revenue` and `salesperson_id` in your data, you can add an `Avg Sales per salesperson` measure using the `sum()` and `count()` aggregate functions together like so: 

![Measure using division and multiple aggregation functions](../../../.gitbook/assets/image%20%28217%29.png)

Here are the underlying components:

```text
kind: Measure
field: sum(total_sales) / count_distinct(salesperson_id)
format: ',.2f'
```

## Conditional logic

You can add conditional logic to formulas. Conditions are true/false statements that can be expressed in your formulas. Here are some examples of conditions:

```text
sales > 1000

# This uses a list
state IN ("Georgia", "Tennessee", "Virginia", "Texas", "South Carolina")

# You can use ANDs and ORs
sales > 1000 OR state = "Texas"

# Use IS NULL to compare for missing values
name IS NULL
```

To use conditions in formulas, use the `IF` function. This function contains pairs of conditions and values. A final value is used if none of your conditions match. Here is the `IF` function pattern:

```text
IF([condition1], [value1], [condition2], [value2], …, [else_value])
```

Here are examples for formulas that use the `IF` function:

```text
# A simple if  
sum(if(state="Texas", sales_dollars, 0.0))

# Multiple condition/value pairs
sum(if(state="Texas", sales_dollars*0.08, state="Georgia", sales_dollars*0.07, state="Tennessee", sales_dollars*0.0925, sales_dollars*0.055))

# You can use IF functions for both dimensions and measures
if(last_name IS NULL, first_name, first_name + " " + last_name)
```

Here's an example of an conditional logic in a measure:

```text
kind: Measure
field: 'avg(if(race = "White", household_income))'
singular: Avg Income per White household
plural: Avg Income per White household
format: '$,.0f'
icon: hashtag
```

Here's an example of conditional logic in a dimension:

```text
kind: Dimension
field: if(gender = "F" AND household_income > 50000, "Campaign A", gender = "M" AND
  household_income > 50000, "Campaign B", "Campaign C")
singular: Campaign
plural: Campaign
icon: envelope
```

### Defining conditions in IF statements

Conditions are defined as \[field\] \[comparison\] \[values\]. These comparisons can be ANDed or ORed together. 

| Conditions | Examples |
| :--- | :--- |
| Greater than a number | `sales > 20` or `sales > 20.5` |
| Greater than or equal to | `sales >= 20` |
| Equal to a number or a string \(strings must be surrounded by double quotes. | `age=20` or `state="Tennessee"` |
| Not equal to a number or string | `age != 20` or `state != "Tennessee"` |
| Checking if a value is null | `state IS NULL` |
| Checking if a value is in a list of values | `state IN ("TN", "GA", "FL")` |
| Checking if a value is True or False | `flag = True`or `flag = False` |
| Comparing dates.  | `sales_date BETWEEN "ONE WEEK AGO" and "TODAY"` or `sales_date BETWEEN "2020-01-01" AND "2020-06-30"` |
| Intelligent date ranges \(use PREVIOUS, THIS, or NEXT to define an offset and DAY, MONTH, MTD, QTR, YEAR, or YTD to define the period\). | `sales_date IS THIS MONTH` or `sales_date IS LAST MONTH` |
| ANDing two conditions |  `sales > 1000 AND sales_date IS THIS MONTH` |
| ORing two conditions | `sales > 1000 OR sales IS NULL` |

