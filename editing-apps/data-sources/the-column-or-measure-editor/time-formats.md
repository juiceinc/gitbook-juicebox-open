# Time formats

To control how time columns are displayed in the app, you can specify a format. For example, let's say you have the following time column definition for `Years`:

![Select a time format from the list](<../../../.gitbook/assets/image (308).png>)

Let's say a representative value for the `Year` field in your data is `2019-03-01`. You probably do  not want to display the unformatted value in your app. Therefore, you will want to specify a format in the `Years` column editor.&#x20;

The format specified will determine how the date or time value will display in your app. The following date formats are available for selection in the column editor:&#x20;

| **format label** | **d3 equivalent** | **How value`2019-03-01`will display** |
| ---------------- | ----------------- | ------------------------------------- |
| month day, yyyy  | `%b %d, %Y`       | Mar 01, 2019                          |
| day month yyyy   | `%d %b %Y`        | 01 Mar 2019                           |
| mm/dd/yyyy       | `%m/%d/%Y`        | 03/01/2019                            |
| mm-dd-yyyy       | `%m-%d-%Y`        | 03-01-2019                            |
| month yyyy       | `%b %Y`           | Mar 2019                              |
| yyyy             | %Y                | 2019                                  |

If you want to apply a date format other than one of these formats, you can do so by creating an [advanced column](../advanced-ingredients/) using an [advanced time format](../advanced-ingredients/advanced-formats.md#advanced-time-formats).&#x20;
