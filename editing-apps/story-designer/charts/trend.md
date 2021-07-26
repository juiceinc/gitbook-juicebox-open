# Trend

The trend chart displays a measure plotted over a time dimension. Adding a slice with a trend chart \(i.e., a trend slice\) is a good choice when users want to see how a measure changes over time.  

## Adding a trend slice

To add a trend slice:

* select **Trend** from the chart list

![](../../../.gitbook/assets/image%20%28256%29.png)

* select the [time ingredient](../../data-sources/adding-ingredients/#time-ingredient) to use for the x-axis
* select up to 5 measures to display on a single y-axis
* optionally, select 1 measure to display on a second y-axis
* add slice text \(optional\)
* click **Save**

![](../../../.gitbook/assets/image%20%28251%29.png)

{% hint style="info" %}
Because the trend chart requires a [time ingredient](../../data-sources/adding-ingredients/#time-ingredient), at least one of your dimensions must be a time ingredient. A time ingredient is an ingredient defined using a date or timestamp field. The format selected for the time ingredient will determine how your dates roll up in your trend chart. For example, if you select the format `month yyyy`, the trend chart will roll up by month. If you select the format `yyyy`, the trend chart will roll up by year. 
{% endhint %}

{% embed url="https://www.loom.com/share/b5520e0548fa4ab59d3284efd3f792ae" caption="Adding a trend slice" %}

## Using a trend slice

You can hover over individual points to see more detail. Date range selections made in the trend slice will filter downstream slices. 

Dates in the data that are missing values will show a break in the trend line, like so:

![The trend line has a break because household\_size is null for all 1973 dates](../../../.gitbook/assets/image%20%2891%29.png)



### 

### 

