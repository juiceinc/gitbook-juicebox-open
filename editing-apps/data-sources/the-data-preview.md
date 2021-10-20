# The data preview

From the data preview you can see a sample of your records and see the data types for each field in your data. You can also open the column editor by clicking on the orange pills at the top of each column.&#x20;

To open the data preview, click the **View** button for the data.

![Click the View button to open the data preview](<../../.gitbook/assets/image (323).png>)

To exit the data preview, simply click outside of the data preview window.&#x20;

### Data types

From the data preview, you can see the data types for each column.&#x20;

![Data types for each column can be viewed from the data preview](<../../.gitbook/assets/image (302).png>)

Here are data types that are recognized in Juicebox:

| Data type | Description                                                                                                      | Example                                      |
| --------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| Text      | Variable-length character data                                                                                   | `882d8f4dccdb3d143df3cc06901f3399` or `Joe`  |
| Number    | Numeric values, either with or without decimals                                                                  | `46` or `53.5`                               |
| Boolean   | Values that denote either TRUE or FALSE                                                                          | `True` or `False`                            |
| Date      | A value for a date that includes the year, month, and day                                                        | `2020-10-30`                                 |
| Time      | A value for a date and time that includes the year, month, day, hour, minute, second, and (optionally) subsecond | `2020-10-30 19:35:25.125456`                 |

{% hint style="info" %}
If the data type for a column is not what you expect, that may indicate there is an issue with the data. For example, if you expect a column to have the Number data type, but it instead has a Text data type, there may be values in the column that are not numbers. Here is guidance on [preparing your data](../design-tips/preparing-your-data.md) for use in Juicebox.&#x20;
{% endhint %}
