# Advanced field formulas

You can create advanced formulas that use field math, combine multiple aggregate functions, and use conditional logic.

## Field math

You can add, subtract, multiply and divide numeric data fields; apply conversion functions to values; and concatenate text fields.&#x20;

### Add, subtract, multiple, and divide

You can perform mathematical operations with data fields and constants. For example, if you have `sale_amount` and `cost_amount` in your data, you can add a **Profits** dimension like so:&#x20;

<figure><img src="../../../.gitbook/assets/image (530).png" alt=""><figcaption><p>A dimension that uses field math</p></figcaption></figure>

If you divide by zero, you’ll get a null.&#x20;

### Conversion functions

Conversion functions change the value for a field. It might change to a different type or to a different time period.

| Function                                             | Examples                                                                                     |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Round to the nearest week (requires a date field)    | `week(sales_date)`                                                                           |
| Round to the nearest month (requires a date field)   | `month(sales_date)`                                                                          |
| Round to the nearest quarter (requires a date field) | `quarter(sales_date)`                                                                        |
| Round to the nearest year (requires a date field)    | `year(sales_date)`                                                                           |
| Convert a numeric value to a string                  | `string(zipcode)`                                                                            |
| Convert a string value to an integer                 | `int(age)`                                                                                   |
| Calculate an age at the current date.                | `age(birth_date)`                                                                            |
| Calculate the difference between dates               | `datediff(end_date, start_date)`                                                             |
| Extract a component of a date                        | `extract(YEAR, birth_date)`                                                                  |
| Return the last date in a period                     | `lastday(sales_date, MONTH)` note: this can be used only on bigquery and snowflake databases |

### Date parts in datediff and extract

When using the `datediff` and `extract` functions, you can supply a datepart. This will determine the units that are counted or extracted. Possible values are

| Date part                         | Description                                                                                                                            |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| day                               |                                                                                                                                        |
| week                              | This begins on Sunday                                                                                                                  |
| week(weekday)                     | This date part begins on weekday. Valid weekdays are "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", and "saturday". |
| month                             |                                                                                                                                        |
| quarter                           |                                                                                                                                        |
| year                              |                                                                                                                                        |
| isoweek                           | Uses ISO 8601 week boundaries. ISO weeks begin on Monday                                                                               |
| isoyear                           | Uses ISO 8601 week-numbering year boundary.                                                                                            |
| dayofweek (extract function only) | Sunday=1, Monday=2, etc.                                                                                                               |
| dayofyear (extract function only) |                                                                                                                                        |

### Concatenating text fields

You can use `+` to concatenate text data fields together. For example, you can concatenate `first_name` and `last_name` to create a **Full name** dimension.&#x20;

<figure><img src="../../../.gitbook/assets/image (531).png" alt=""><figcaption><p>Concatenate text fields</p></figcaption></figure>

{% hint style="warning" %}
You must use double quotes in field expressions to define string constants. Single quotes will not work.&#x20;
{% endhint %}

If you want to concatenate fields that do not have a Text data type, you'll need to first convert the field to a string using the [conversion function](advanced-formulas.md#conversion-functions) `string()`. For example, if you want to concatenate `address`, `state`, `city`, and `zip` together, but `zip` is not a string, you'll need to use `string(zip)`.

## Aggregation functions

Aggregation functions are used in measure ingredients to perform a calculation across multiple rows. If no aggregation function is provided for a measure ingredient, `sum()` will be used.&#x20;

<table data-header-hidden><thead><tr><th width="416">Function</th><th>Examples</th></tr></thead><tbody><tr><td>Function</td><td>Examples</td></tr><tr><td>Sum</td><td><code>sum(sales_dollars)</code> or <code>sum(revenue - expenses)</code></td></tr><tr><td>Minimum</td><td><code>min(age)</code></td></tr><tr><td>Maximum</td><td><code>max(age)</code></td></tr><tr><td>Average</td><td><code>avg(home_value)</code></td></tr><tr><td>Count</td><td><code>count(student_name)</code> or <code>count(*)</code></td></tr><tr><td>Count only distinct items</td><td><code>count_distinct(student_name)</code></td></tr><tr><td>Median</td><td><code>median(sales_dollars)</code></td></tr><tr><td>Percentiles expressed as <code>percentileN</code> where N can be between 1 and 99.</td><td><code>percentile1(age)</code> or <code>percentile75(sales_dollars)</code></td></tr><tr><td>Percentiles can also be expressed as an expression and a desired percentile. </td><td><code>percentile(age, 0.25)</code></td></tr><tr><td>Standard Deviation. Calculates the sample standard deviation for an expression.</td><td><code>stddev(age)</code></td></tr></tbody></table>

{% hint style="danger" %}
When you upload a CSV file, percentiles and medians are calculated as approximate values. The statistically exact value may be slightly different.
{% endhint %}

You can combine multiple aggregation functions together. For example, if you have `sales_amount` and `salesperson_id` in your data, you can add a **Sales per Salesperson** measure using the `sum()` and `count_distinct()` aggregation functions together like so:&#x20;

<figure><img src="../../../.gitbook/assets/image (533).png" alt=""><figcaption><p>Combine multiple aggregation functions</p></figcaption></figure>

## Conditional logic

You can add conditional logic to formulas. Conditions are true/false statements that can be expressed in your formulas. Here are some examples of conditions:

```
sales > 1000

# This uses a list
state IN ("Georgia", "Tennessee", "Virginia", "Texas", "South Carolina")

# You can use ANDs and ORs
sales > 1000 OR state = "Texas"

# Use IS NULL to compare for missing values
name IS NULL
```

To use conditions in formulas, use the `if` function. This function contains pairs of conditions and values. A final value is used if none of your conditions match. Here is the `if` function pattern:

```
if([condition1], [value1], [condition2], [value2], …, [else_value])
```

Here are examples for formulas that use the `if` function:

```
# A simple if  
sum(if(state="Texas", sales_dollars, 0.0))

# Multiple condition/value pairs
sum(if(state="Texas", sales_dollars*0.08, state="Georgia", sales_dollars*0.07, state="Tennessee", sales_dollars*0.0925, sales_dollars*0.055))

# You can use if() functions for both dimensions and measures
if(last_name IS NULL, first_name, first_name + " " + last_name)
```

### Defining conditions in IF statements

Conditions are defined as \[field] \[comparison] \[values]. These comparisons can be ANDed or ORed together.&#x20;

| Conditions                                                                                                                                                                                             | Examples                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| Greater than a number                                                                                                                                                                                  | `sales > 20` or `sales > 20.5`                                                                        |
| Greater than or equal to                                                                                                                                                                               | `sales >= 20`                                                                                         |
| Equal to a number or a string (strings must be surrounded by double quotes)                                                                                                                            | `age=20` or `state="Tennessee"`                                                                       |
| Not equal to a number or string                                                                                                                                                                        | `age != 20` or `state != "Tennessee"`                                                                 |
| Checking if a value is null                                                                                                                                                                            | `state IS NULL`                                                                                       |
| Checking if a value is in a list of values                                                                                                                                                             | `state IN ("TN", "GA", "FL")`                                                                         |
| Checking if a value is True or False                                                                                                                                                                   | `flag = "True"`or `flag = "False"`                                                                    |
| Comparing dates.                                                                                                                                                                                       | `sales_date BETWEEN "ONE WEEK AGO" and "TODAY"` or `sales_date BETWEEN "2020-01-01" AND "2020-06-30"` |
| Intelligent date ranges (use PREVIOUS, THIS, or NEXT to define an offset and DAY, MONTH, MTD, QTR, YEAR, or YTD to define the period).                                                                 | `sales_date IS THIS MONTH` or `sales_date IS LAST MONTH`                                              |
| ANDing two conditions                                                                                                                                                                                  | `sales > 1000 AND sales_date IS THIS MONTH`                                                           |
| ORing two conditions                                                                                                                                                                                   | `sales > 1000 OR sales IS NULL`                                                                       |
| Check if a value contains a string using `%` as a wildcard. If `%` is not provided, it will be inserted at the beginning and end of the value. `LIKE` is case-sensitive, `ILIKE` is case-insensitive.  | <p><code>state LIKE "Te%"</code><br><code>state ILIKE "m%"</code></p>                                 |
