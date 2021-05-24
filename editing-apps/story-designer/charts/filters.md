# Filters

The filters chart displays pills \(i.e., filter pills\) that allow users to filter story data by dimension values. When a user clicks on a filter pill, all of the dimension values are displayed in a side panel. Selecting one or more of the values will filter the downstream slices. Adding a slice with a filters chart \(i.e., a filter slice\) is a good choice when you want to let your users focus the story on what is most important to them. 

## Adding a filter slice

To add a filter slice:

* select **Filters** from the chart list

![](../../../.gitbook/assets/image%20%28177%29.png)

* select the dimensions you want to add as filters in the order you want them displayed
* add slice text \(optional\)
* click **Save**

![](../../../.gitbook/assets/image%20%28232%29.png)

{% embed url="https://www.loom.com/share/79dc53c9b59e446987b15ec043a8d566" caption="Adding a filter slice" %}

{% hint style="info" %}
The order of your filter pills may be important, because selections made in a filter pill will filter "downstream" filter pills. For example, say you have three filter pills in this order: Organization, Cohort, and Student Name. Values selected for Organization will filter Cohort and Student Name. Values selected for Cohort, will filter Student Name but not filter Organization. Values selected in Student Name will not filter either Organization or Cohort. 
{% endhint %}

## Using a filter slice

To use a filter slice, click on the filter pill and select the values that you want to filter on. 

