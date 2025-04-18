# Time formats

To control how date or time dimensions are displayed in the report, you can specify a format. For example, let's say you have a dimension called **Release Year.** A representative value for **Release Year** in your data is `2019-03-01`. You probably do not want to display the unformatted value in your report. Therefore, you will want to specify a time format in the ingredient editor.&#x20;

<figure><img src="../../../../.gitbook/assets/image (512).png" alt=""><figcaption><p>Select a time format</p></figcaption></figure>

The time format specified will determine how the date or time value will display in your report. The following date formats are available for selection in the column editor:&#x20;

| **format label** | **d3 equivalent** | **How value`2019-03-01`will display** |
| ---------------- | ----------------- | ------------------------------------- |
| month dd, yyyy   | `%B %-d, %Y`      | March 1, 2019                         |
| dd mon yyyy      | `%-d %b %Y`       | 1 Mar 2019                            |
| mm/dd/yyyy       | `%-m/%-d/%Y`      | 3/1/2019                              |
| mm-dd-yyyy       | `%-m-%-d-%Y`      | 3-1-2019                              |
| month yyyy       | `%B %Y`           | March 2019                            |
| yyyy             | %Y                | 2019                                  |

If you want to apply a time format other than one in the dropdown, you can do so by entering the custom format in the **Time format** box using these [codes](https://strftime.org/). For example, let's say you want to display **Release Years** like "Mar 01 2014" (abbreviated month, padded day, and full year with no commas). You can do by entering `%b %d %Y`, like so:

<figure><img src="../../../../.gitbook/assets/image (514).png" alt=""><figcaption><p>Enter a custom time format</p></figcaption></figure>

{% hint style="success" %}
Date or time ingredients will "roll up" in charts to the period selected for the Format. For example, selecting the `month yyyy` format will roll up to the month. Selecting the `yyyy` format will roll up to the year.&#x20;
{% endhint %}
