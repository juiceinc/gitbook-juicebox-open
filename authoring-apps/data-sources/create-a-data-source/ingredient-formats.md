# Ingredient formats

Often you will want to control how number and date values are formatted in your apps. You can do this by specifying a format in your ingredient definition. 

## Number formatting

To control how numbers are displayed in the app, you can specify a format. For example, let's say you have the following ingredient definition for `price`:

```text
price:
  kind: Measure
  field: avg(price)
  singular: Price
  plural: Price
```

**\[TODO: Replace with image of ingredient UI\]**

Representative values for `price` in your data are `3231.447` and `0.5264`. You probably do  not want price to display the unformatted value your app. Therefore, you will want to specify a format in the `price` ingredient definition. 

The format specified in the ingredient definition will determine how the value will display in your app. The following standard formats are available for numbers: 

| format label | d3 equivalent | How value`3231.447`will display | How value `0.5264` will display |
| :--- | :--- | :--- | :--- |
| \# 2 Decimals | `,.2f` | 3,231.45 | 0.53 |
| \# Rounded | `,.0f` | 3,231 | 1 |
| \# 3 Sig figs | `.3s` | 3.23K | 0.526 |
| $ 2 Decimals | `$.2f` | $3,231.45 | $0.53 |
| $ Rounded | `$,.0f` | $3,231 | $1 |
| $ 3 Sig figs | `$.3s` | $3.23K | $0.526 |
| % 2 Decimals | `,.2%` | 323,144.70% | 52.64% |
| % Rounded | `,.0%` | 323,145% | 53% |

**\[TODO: Confirm changes from JB-3101 have been made.\]**

If you want to apply a number format other than one of the standard formats, you can do so by creating an [Advanced Ingredient](advanced-ingredients.md). **\[TODO: Confirm\]**

## Date formatting

To control how dates are displayed in the app, you can specify a format. For example, let's say you have the following ingredient definition for `start_date`:

```text
start_date:
  kind: Dimension
  field: start_date
  singular: Start Date
  plural: Start Dates
```

**\[TODO: Replace with image of ingredient UI\]**

A representative values for `start_date` in your data is `2019-03-01`. You probably do  not want dates to display the unformatted value your app. Therefore, you will want to specify a format in the `start_date` ingredient definition. 

The format specified in the ingredient definition will determine how the value will display in your app. The following standard formats are available for dates: 

| format label | d3 equivalent | How value`2019-03-01`will display |
| :--- | :--- | :--- |
| month day, yyyy | `%b %d, %Y` | Mar 1, 2019 |
| day month yyyy | `%d %b %Y` | 1 Mar 2019 |
| mm/dd/yyyy | `%m/%d/%Y` | 03/01/2019 |
| mm-dd-yyyy | `%m-%d-%Y` | 03-01-2019 |
| month yyyy | `$,.0f` | Mar 2019 |

If you want to apply a date format other than one of the standard formats, you can do so by creating an [Advanced Ingredient](advanced-ingredients.md). **\[TODO: Confirm\]**

