# Advanced formats

The [most commonly used formats](../adding-ingredients/ingredient-formats.md) are available in the ingredient editor. But if you need to use a different format, you can [add an advanced ingredient](../adding-ingredients/#adding-an-advanced-ingredient) and adjust the `format:` component within the advanced ingredient definition.

## Advanced number formats

You can use  [number formats](https://github.com/d3/d3-format) to adjust how numbers display in your story. For example, let's say you want to display `Overweight %` with 1 decimal. Because the ingredient editor does not include an option to display a percent with 1 decimal, you will need to do this as an advanced ingredient, like so:

![Set format to a percent with 1 decimal](../../../.gitbook/assets/image%20%2848%29.png)

Here are the underlying components:

```text
kind: Metric
field: >-
  sum(if(Question="Percent of adults aged 18 years and older who have an
  overweight classification", Data_Value * Sample_Size *.01)) /
  sum(if(Question="Percent of adults aged 18 years and older who have an
  overweight classification", Sample_Size))
singular: Overweight %
plural: Overweight %
format: ',.1%'
icon: hashtag
```

## Advanced date formats

You can use [date formats](https://github.com/d3/d3-time-format) to adjust how dates display in your story. For example, let's say you want to display `Year Dates` like "January 1, 2018" \(full month and unpadded day\). Because the ingredient editor does not include an option to display this date format, you will need to do this as an advanced ingredient, like so:

![Set date format to full month and unpadded day](../../../.gitbook/assets/image%20%2849%29.png)

Here are the underlying components:

```text
kind: Dimension
field: Year_Date
singular: Year Date2
plural: Year Dates2
format: '%B %e, %Y'
icon: calendar
```

