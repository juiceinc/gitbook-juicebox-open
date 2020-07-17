# Bucketed dimensions

A bucketed dimension is a dimension that groups field values into buckets based on conditions. For example, the Unhealthy Americans data includes the `LocationAbbr` field with state abbreviation values. Let's say you want to groups these state abbreviation values into different regions: Southeast, Northeast, Midwest, Southwest, and West. To do that, you would create an advanced ingredient like so--

![Advanced ingredient: bucketed dimension](../../../.gitbook/assets/image%20%2839%29.png)

--with the following components:

```text
kind: Dimension
field: LocationAbbr
singular: Region
plural: Regions
buckets:
  - label: Southeast
    condition: 'IN ("AR", "AL", "GA", "MS", "TN", "KY", "SC", "NC", "VA", "WV", "DC", "FL", "LA")'
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

To create a bucketed dimension, you add the `buckets:` and \(optionally\) a `bucket_default_label:` components to the dimension definition. Within `buckets`, define a list of`label` and `condition`. If the `condition` is met, your `label` will be displayed.

```text
kind: Dimension
field: [field]
singular: [singular label]
plural: [plural label]
icon: [icon]
buckets:
  - label: [bucket1label]
    condition: [bucket1condition]
  - label: [bucket2label]
    condition: [bucket2condition]
  - label: [bucket3label]
    condition: [bucket3condition]
bucket_default_label: [defaultbucketlabel]
```

### Defining conditions

Conditions are defined like \[\(optional\) field\] \[comparison\] \[values\]. These comparisons can be ANDed or ORed together. 

| Conditions | Examples |
| :--- | :--- |
| Greater than a number | `>20` or `>20.5` |
| Equal to a number or a string \(strings must be surrounded by double quotes. | `=20` or `="Tennessee"` |
| Checking if a value is null | `IS NULL` |
| Checking if a value is in a list of values | `IN ("TN", "GA", "FL")` |
| Comparing dates.  | `BETWEEN "ONE WEEK AGO" and "TODAY"` or `BETWEEN "2020-01-01" AND "2020-06-30"` |
| Intelligent date ranges \(use PREVIOUS, THIS, or NEXT to define an offset and DAY, MONTH, MTD, QTR, YEAR, or YTD to define the period\). | `IS THIS MONTH` or `IS LAST MONTH` |
| ANDing two conditions |  `sales > 1000 AND sales_date IS THIS MONTH` |
| ORing two conditions | `sales > 1000 OR sales IS NULL` |

### Providing an explicit field for the condition

By default, each condition will be compared against the main `field`. Let's look at a sample ingredient--

```text
kind: Dimension
field: sales_dollars
singular: Sales Group
plural: Sales Groups
buckets:
  - label: Small
    condition: '<100.0'
  - label: Medium
    condition: '<1000.0'
buckets_default_label: Large
```

You can provide an alternative field in the condition itself. This is the **same definition** with the field provided explicitly.

```text
kind: Dimension
field: sales_dollars
singular: Sales Group
plural: Sales Groups
buckets:
  - label: Small
    condition: 'sales_dollars<100.0'
  - label: Medium
    condition: 'sales_dollars<1000.0'
buckets_default_label: Large
```

By providing an alternative field, you can create complex buckets that look at multiple values

```text
kind: Dimension
field: sales_dollars
singular: Sales Group
plural: Sales Groups
buckets:
  # This first condition does not use sales_dollars because it contains its own field
  - label: In-state
    condition: 'state = "Tennessee"'
  - label: Small
    condition: '<100.0'
  - label: Medium
    condition: '<1000.0'
buckets_default_label: Large
```

### Conditions are evaluated in order

Conditions within buckets are evaluated in the order they are defined, which makes defining buckets for continuous values convenient:

```text
kind: Dimension
field: age
singular: Age Range
plural: Age Bands
buckets:
  - label: Under 5
    condition: <5
  - label: 5-17
    condition: <18
  - label: 18-64
    condition: <65
buckets_default_label: 65 and over
```

```text
kind: Dimension
field: household_income
singular: Income Range
plural: Income Ranges
buckets:
  - label: Under 25k
    condition: <25000
  - label: 25k-49k
    condition: <50000
  - label: 50k-99k
    condition: <99000
buckets_default_label: 100k and over
icon: money-bill-alt
```

