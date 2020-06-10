# Ingredient formats

Often you will want to control how number and date values are formatted in your apps. You can do this by specifying a format in your ingredient definition. 

## Number formatting

To control how numbers are displayed in the app, you can specify a format. For example, let's say you have the following ingredient definition for `Data_Value`:

![Measure with &quot;\# 2 Decimals&quot; format ](../../../.gitbook/assets/image%20%2840%29.png)

Representative values for `Data_Value` in your data are `3231.447` and `0.5264`. You probably do  not want to display the unformatted value in your app. Therefore, you will want to specify a format in the `Data_Value` ingredient definition. 

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

If you want to apply a number format other than one of the standard formats, you can do so by creating an [advanced ingredient](defining-ingredients/#advanced-ingredients). 

## Date formatting

To control how dates are displayed in the app, you can specify a format. For example, let's say you have the following ingredient definition for `Year_Date`:

![Time dimension with &quot;month day, yyyy&quot; format](../../../.gitbook/assets/image%20%2825%29.png)

A representative values for`Year_Date` in your data is `2019-03-01`. You probably do  not want to display the unformatted value in your app. Therefore, you will want to specify a format in the `Year_Date` ingredient definition. 

The format specified in the ingredient definition will determine how the value will display in your app. The following standard formats are available for dates: 

| format label | d3 equivalent | How value`2019-03-01`will display |
| :--- | :--- | :--- |
| month day, yyyy | `%b %d, %Y` | Mar 1, 2019 |
| day month yyyy | `%d %b %Y` | 1 Mar 2019 |
| mm/dd/yyyy | `%m/%d/%Y` | 03/01/2019 |
| mm-dd-yyyy | `%m-%d-%Y` | 03-01-2019 |
| month yyyy | `%b %Y` | Mar 2019 |

If you want to apply a date format other than one of the standard formats, you can do so by creating an [advanced ingredient](defining-ingredients/#advanced-ingredients). 

