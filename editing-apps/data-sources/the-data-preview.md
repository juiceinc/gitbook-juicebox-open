# The data preview

From the data preview you can see the data table's columns, each column's data type, and the first 100 rows in the data table. You can also open the column editor by clicking on the pill at the top of each column.&#x20;

To open the data preview, first open the Data Tables drawer and then select the data table you want to view. To exit the data preview, close the Data Tables drawer.&#x20;

![The data preview](<../../.gitbook/assets/open data preview.gif>)

### Data types

From the data preview, you can see each column in your data and the data types for each column.

![Data types for each column can be viewed from the data preview](<../../.gitbook/assets/image (398).png>)

Here are data types that are recognized in Juicebox:

| Data type | Description                                                                                                      | Example                                      |
| --------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| Text      | Variable-length character data                                                                                   | `882d8f4dccdb3d143df3cc06901f3399` or `Joe`  |
| Number    | Numeric values, either with or without decimals                                                                  | `46` or `53.5`                               |
| Boolean   | Values that denote either TRUE or FALSE                                                                          | `True` or `False`                            |
| Date      | A value for a date that includes the year, month, and day                                                        | `2020-10-30`                                 |
| Time      | A value for a date and time that includes the year, month, day, hour, minute, second, and (optionally) subsecond | `2020-10-30 19:35:25.125456`                 |

Certain things in Juicebox require particular data types. For example, creating a sum or average measure only works with number columns, and the [trend](../story-designer/charts/trend.md) chart requires a date or time column. **Bottom line: Don't mix-and-match data types within the same column in your data file.** Number columns should contain only numbers, date columns should contain only dates, and so on. If a column has more than one type of data, it will get the text data type.&#x20;

{% hint style="info" %}
If the data type for a column is not what you expect, that may indicate there is an issue with the data. For example, if you expect a column to have the number data type, but it instead has a text data type, there may be values in the column that are not numbers. Here is guidance on [preparing your data](../design-tips/preparing-your-data.md) for use in Juicebox.&#x20;
{% endhint %}
