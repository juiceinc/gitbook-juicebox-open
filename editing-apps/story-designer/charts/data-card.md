---
description: >-
  Summarize measures, and allow user selections to configure other charts
  dynamically.
---

# Data Chooser

A data chooser chart can be used to for the following:

* Show a summary of measures
* Let a user choose which measure to explore 
* Let a user choose which dimension to explore

Choices made in a data chooser chart can drive the filtering narrative of the story that follows [using dynamic ingredients](data-card.md#using-dynamic-ingredients). There are two types: measure data chooser and dimension data chooser.

## Data chooser chart with measures

A data chooser chart with measures \(i.e., a measure data chooser slice\) will display a high-level summary that provides context for users as they make their selections. The selection made in a measure data chooser slice can be used as a [dynamic measure](data-card.md#using-dynamic-ingredients) ingredient in other charts, allowing for user-driven exploration.

#### To add a measure data chooser slice:

* select **Data Chooser** from the chart list

![](../../../.gitbook/assets/image%20%28264%29.png)

* select the measures you want to add in the order you want them displayed
* add slice text \(optional\)
* click **Save**

![](../../../.gitbook/assets/image%20%28212%29.png)

{% hint style="info" %}
The type of data chooser is determined by the first ingredient you add. Once you select a measure, any additional ingredients must be measures. 
{% endhint %}

## Data chooser chart with dimensions

A data chooser chart with dimensions \(i.e., a dimension data chooser slice\) lets users select one dimension from a group of dimensions. The selection made in a dimension data chooser can be used as a [dynamic dimension](data-card.md#using-dynamic-ingredients) ingredient in other charts, allowing for user-driven exploration.

#### To add a dimension data card slice:

* select **Data Chooser** from the chart list

![](../../../.gitbook/assets/image%20%28263%29.png)

* select the dimensions you want to add in the order you want them displayed

![](../../../.gitbook/assets/image%20%28205%29.png)

* add slice text \(optional\)

{% hint style="info" %}
The type of data chooser is determined by the first ingredient you add. Once you select a dimension, any additional ingredients must be dimensions. 
{% endhint %}

## Using dynamic ingredients

Data chooser slices are particularly powerful when slices further down the app refer to the selections in the data card.

{% hint style="info" %}
Data chooser values will be "display only" \(i.e., unselectable\) unless a downstream slice includes a dynamic ingredient referring to the data chooser.
{% endhint %}

To reference the selection made in a data chooser slice**:** 

* Create a dimension data chooser or measure data chooser using the above instructions
* In a slice that is below the data chooser slice that should be referenced, select the data chooser's slice slug in the dimension drop down and/or measure drop down

{% hint style="info" %}
A slice can reference both a dimension data chooser and a measure data chooser in the respective dimension and measure drop downs.
{% endhint %}

![Select a dynamic ingredient to your chart to make it interactive ](../../../.gitbook/assets/image%20%28249%29.png)

Here's how to make your charts dynamic:

{% embed url="https://www.loom.com/share/460990e6e0464d369bb0f717ec2bfb3c" %}

After making your chart dynamic, you may want to make your slice text dynamic as well. To learn how, go [here](../slices/dynamic-text.md). 

