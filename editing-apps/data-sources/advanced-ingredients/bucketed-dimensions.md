# Bucketed columns

A bucketed column is a column that groups field values into buckets based on conditions. For example, let's say your data includes a `Score` field with user scores, and you want to use the scores to group users into different roles:&#x20;

* Detractor
* Passive
* Promoter

To do that, you could create an advanced column like so--

![Advanced column using buckets](<../../../.gitbook/assets/image (342).png>)

\--with the following components:

```
kind: Dimension
field: score
singular: Role
buckets:
  - label: Detractor
    condition: <= 6
  - label: Passive
    condition: <= 8
  - label: Promoter
    condition: <= 10
buckets_default_label: Other
```

To create a bucketed column, you add the `buckets:` and (optionally) `buckets_default_label:` components to the column definition. Within `buckets`, define a list, with each list item containing a `label` and `condition`. If the `condition` is met, your `label` will be displayed. If you don't define a `buckets_default_label` and none of your conditions match, "Not found" will be displayed.

```
kind: Dimension
field: [field]
singular: [singular label]
buckets:
  - label: [bucket1label]
    condition: [bucket1condition]
  - label: [bucket2label]
    condition: [bucket2condition]
  - label: [bucket3label]
    condition: [bucket3condition]
buckets_default_label: [defaultbucketlabel]
```

### Defining conditions

Conditions are defined like \[(optional) field] \[comparison] \[values]. These comparisons can be ANDed or ORed together.&#x20;

| Conditions                                                                                                                             | Examples                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Greater than a number                                                                                                                  | `>20` or `>20.5`                                                              |
| Greater than or equal to                                                                                                               | `>=20`                                                                        |
| Equal to a number or a string (strings must be surrounded by double quotes.                                                            | `=20` or `="Tennessee"`                                                       |
| Not equal to a number or string                                                                                                        | `!=20` or `!="Tennessee`                                                      |
| Checking if a value is null                                                                                                            | `IS NULL`                                                                     |
| Checking if a value is in a list of values                                                                                             | `IN ("TN", "GA", "FL")`                                                       |
| Comparing dates.                                                                                                                       | `BETWEEN "A WEEK AGO" and "TODAY"` or `BETWEEN "2020-01-01" AND "2020-06-30"` |
| Intelligent date ranges (use PREVIOUS, THIS, or NEXT to define an offset and DAY, MONTH, MTD, QTR, YEAR, or YTD to define the period). | `IS THIS MONTH` or `IS LAST MONTH`                                            |
| ANDing two conditions                                                                                                                  |  `sales > 1000 AND sales_date IS THIS MONTH`                                  |
| ORing two conditions                                                                                                                   | `sales > 1000 OR sales IS NULL`                                               |

### Providing an explicit field for the condition

By default, each condition will be compared against the main `field`. Let's look at a sample ingredient--

```
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

```
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

```
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

```
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

```
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
