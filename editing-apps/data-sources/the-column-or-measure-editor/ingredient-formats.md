# Number formats

To control how numbers are displayed in the app, you can specify a format. For example, let's say you have the following measure:

![Measure with "# 2 Decimals" format](<../../../.gitbook/assets/image (250).png>)

Representative values for `Data_Value` in your data are `3231.447` and `0.5264`. You probably do not want to display the unformatted value in your app. Therefore, you will want to specify a number format in the `Data_Value` ingredient definition.&#x20;

The format specified in the measure editor will determine how the value will display in your app. The following standard formats are available for measures:&#x20;

| format label | d3 equivalent | How value`3231.447`will display | How value `0.5264` will display |
| ------------ | ------------- | ------------------------------- | ------------------------------- |
| # 2 Decimals | `,.2f`        | 3,231.45                        | 0.53                            |
| # Rounded    | `,.0f`        | 3,231                           | 1                               |
| # 3 Sig figs | `.3s`         | 3.23K                           | 0.526                           |
| $ 2 Decimals | `$.2f`        | $3,231.45                       | $0.53                           |
| $ Rounded    | `$,.0f`       | $3,231                          | $1                              |
| $ 3 Sig figs | `$.3s`        | $3.23K                          | $0.526                          |
| % 2 Decimals | `,.2%`        | 323,144.70%                     | 52.64%                          |
| % Rounded    | `,.0%`        | 323,145%                        | 53%                             |

If you want to apply a number format other than one of the standard formats, you can do so by creating an [advanced ingredient](../advanced-ingredients/advanced-formats.md).&#x20;
