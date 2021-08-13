---
description: >-
  Summarize measures, and allow user selections to configure other charts
  dynamically.
---

# Chooser

A data chooser chart can be used to for the following:

* Show a summary of measures
* Let a user choose which measure to explore 
* Let a user choose which dimension to explore

Choices made in a chooser chart can drive the filtering narrative of the story that follows [using dynamic ingredients](data-card.md#using-dynamic-ingredients). There are two types: measure chooser and dimension chooser.

## Chooser chart with measures

A chooser chart with measures \(i.e., a measure chooser slice\) will display a high-level summary that provides context for users as they make their selections. The selection made in a measure chooser slice can be used as a [dynamic measure](data-card.md#using-dynamic-ingredients) ingredient in other charts, allowing for user-driven exploration.

#### To add a measure chooser slice:

* select  **Chooser** from the chart list

![](../../../.gitbook/assets/image%20%28282%29.png)

* select the measures you want to add in the order you want them displayed
* add slice text \(optional\)
* click **Save**

![](../../../.gitbook/assets/image%20%28212%29.png)

{% hint style="info" %}
The type of chooser is determined by the first ingredient you add. Once you select a measure, any additional ingredients must be measures. 
{% endhint %}

## Chooser chart with dimensions

A chooser chart with dimensions \(i.e., a dimension chooser slice\) lets users select one dimension from a group of dimensions. The selection made in a dimension chooser can be used as a [dynamic dimension](data-card.md#using-dynamic-ingredients) ingredient in other charts, allowing for user-driven exploration.

#### To add a dimension chooser slice:

* select **Chooser** from the chart list

![](../../../.gitbook/assets/image%20%28281%29.png)

* select the dimensions you want to add in the order you want them displayed

![](../../../.gitbook/assets/image%20%28205%29.png)

* add slice text \(optional\)

{% hint style="info" %}
The type of chooser is determined by the first ingredient you add. Once you select a dimension, any additional ingredients must be dimensions. 
{% endhint %}

## Using dynamic ingredients

Chooser slices are particularly powerful when slices further down the app refer to the selections in the chooser.

{% hint style="info" %}
Chooser values will be "display only" \(i.e., unselectable\) unless a downstream slice includes a dynamic ingredient referring to the chooser.
{% endhint %}

To reference the selection made in a chooser slice**:** 

* Create a dimension chooser or measure chooser using the above instructions
* In a slice that is below the chooser slice that should be referenced, select the chooser's slice slug in the dimension drop down and/or measure drop down

{% hint style="info" %}
A slice can reference both a dimension chooser and a measure chooser in the respective dimension and measure drop downs.
{% endhint %}

![Select a dynamic ingredient to your chart to make it interactive ](../../../.gitbook/assets/image%20%28249%29.png)

Here's how to make your charts dynamic:

{% embed url="https://www.loom.com/share/460990e6e0464d369bb0f717ec2bfb3c" %}

After making your chart dynamic, you may want to make your slice text dynamic as well. To learn how, go [here](../slices/dynamic-text.md). 

