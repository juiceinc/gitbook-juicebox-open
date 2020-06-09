# Defining ingredients

## \[Do not move or rename this page\]

## Basic ingredients

Basic ingredients are defined using the basic ingredient editor. To access the ingredient editor for an ingredient, click on the ingredient pill. \(You can select ingredient pills in either in Data Sources or the Story Designer sections of the app editor.\)

![Access ingredient editor by clicking on ingredient pill](../../../.gitbook/assets/image%20%2834%29.png)

The basic ingredients will look like this:

### Basic dimension

![A basic dimension](../../../.gitbook/assets/image%20%2844%29.png)

### Basic measure

![A basic measure](../../../.gitbook/assets/image%20%2835%29.png)

Sometimes the options available in the basic ingredient editor will not be sufficient to define your desired ingredient. In those cases, you will need to add an advanced ingredient. 

## Advanced ingredients

Most of your ingredients will be basic ingredients. But in cases where you need to do something more than the basic ingredient editor allows, you can use advanced ingredients. 

### Adding an advanced ingredient

To create an advanced ingredient, click on the ingredient pill for a field you will use in your definition. From there, click the menu icon \(![](../../../.gitbook/assets/ellipsis-h-solid.svg)\), and select **Duplicate as Advanced**. Modify the ingredient definition in the text editor as needed. 

### What you can do with advanced ingredients

Advanced ingredients allow you to define the ingredient components in a text editor. Advanced ingredients allow you to use--

* Dimensions that display a lookup value rather than the field value
* Dimensions that group values into "buckets" based on conditions 
* Filters that group values into frequently-used ranges based on conditions
* Measures that use field math
* Measures that combine multiple formulas
* Measures and dimensions that reference other measures and dimensions
* Measures and dimensions that include conditional logic
* Measures formatted using any d3 number format
* Date dimensions formatted using any d3 date format

#### Lookup dimensions

If the dimension values in your data are not what you want displayed in your app, you can create a lookup dimension to change them. For example, the Unhealthy Americans data has a Question field with two distinct, very long values: "Percent of adults aged 18 years and older who have obesity" and "Percent of adults aged 18 years and older who have an overweight classification." You want to display "Obese" and "Overweight" instead.  To do that, you would create an advanced ingredient like so:

![Advanced ingredient: lookup dimension](../../../.gitbook/assets/image%20%2836%29.png)

To create a lookup dimension, you add the `lookup:` component to the dimension definition.

```text
kind: Dimension
field: [field]
singular: [singular label]
plural: [plural label]
icon: [icon]
lookup:
  [value to lookup]:[value to display]
  [value to lookup]:[value to display]
  [value to lookup]:[value to display]
```

If there is a value in your data that is not added to the list of values to lookup, then the value in the data will be displayed. 

#### Bucketed dimensions

A bucketed dimension is a dimension that groups field values into buckets based on conditions. For example, the Unhealthy Americans data includes the `LocationAbbr` field with state abbreviation values. Let's say you want to groups these state abbreviation values into different regions: Southeast, Northeast, Midwest, Southwest, and West. To do that, you would create an advanced ingredient like so--

![Advanced ingredient: bucketed dimension](../../../.gitbook/assets/image%20%2838%29.png)

--with the following components:

```text
kind: Dimension
field: LocationAbbr
singular: Region
plural: Regions
buckets:
  - label: Southeast
    condition: 'IN ("AR", "AL", "GA", "MS", "TN", "KY", "SC", "NC", "VA", "WV", "DC", "FL")'
  - label: Northeast
    condition: 'IN ("ME","VT","NH","CT","NY","NJ","DE","MD","PA","MA","RI")'
  - label: Midwest
    condition: 'IN ("IA","MI","WI","MN","NE","MO","IN","IL","OH","KS","ND","SD")'
  - label: Southwest
    condition: 'IN ("TX","OK","AZ","NM")'
  - label: West
    condition: 'IN ("CA","NV","CO","UT","OR","WA","HI","WY","MT","ID","AK")'
buckets_default_label: Other
```

By default, each condition will be evaluated against the main `field`, but you can provide an alternative field in the condition itself, like so:

```text
kind: Dimension
field: grade
singular: Sales Group
plural: Sales Groups
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

The conditions within buckets are evaluated in the order they are defined, which makes defining buckets for continuous values convenient:

```text
kind: Dimension
field: age
singular: Age Range
plural: Age Bands
buckets:
  - label: "Under 5"
    condition: '< 5'
  - label: "5-17"
    condition: '< 18'
  - label: "18-64"
    condition: '< 65'
buckets_default_label: 65 and over
```

#### Quickselect filtering

{% hint style="info" %}
Both bucketed dimensions and quickselects can be used for filtering. But quickselects can **only** be used in filter slices, whereas bucketed dimensions can be used in other slices. You would use quickselects vs buckets if a single data value should be associated with more than one filter option.  For example, if you want filters for ages `18 and older` and `45 and older` , you must use a quickselect because some age values \(e.g., 46\) will be associated with both filters. Buckets will not work because each age value can only belong to one bucket.
{% endhint %}

#### Field math

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

#### Combining multiple formulas

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

#### Referencing other measures and dimensions

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

#### Conditional logic

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

#### Advanced number formats

#### Advanced date formats







