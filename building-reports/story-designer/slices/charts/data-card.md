---
description: >-
  Summarize measures, and allow user selections to configure other charts
  dynamically.
---

# Chooser

A chooser chart can be used to:

* Show a summary of measures
* Let a user choose which measure to use in downstream charts&#x20;
* Let a user choose which column to use in downstream charts

Choices made in a chooser chart can drive the narrative of the story that follows [using dynamic columns or measures](data-card.md#using-dynamic-ingredients). There are two types: measure chooser and dimesnion chooser.

## Measure chooser

A chooser chart with measures (i.e., a measure chooser) will display a high-level summary of  measures. The selection made in a measure chooser can be used as a [dynamic measure](data-card.md#using-dynamic-ingredients)  in one or more downstream charts, allowing for user-driven exploration.&#x20;

#### To add a measure chooser slice:

* select **Chooser** from the chart list

![Select Chooser from the dropdown](<../../../../.gitbook/assets/image (470).png>)

* select the measures you want to add in the order you want them displayed
* add slice text (optional)

![A measure chooser slice](<../../../../.gitbook/assets/image (374).png>)

{% hint style="info" %}
The type of chooser is determined by whether you add a column or measure first. Once you select the first measure, only measures can be added.&#x20;
{% endhint %}

## Dimension chooser

A chooser chart with dimensions (i.e., a dimension chooser) lets users select one dimension from a group of dimensions for use as a [dynamic dimension](data-card.md#using-dynamic-ingredients) in one or more downstream charts, allowing for user-driven exploration.

{% hint style="warning" %}
A dimension chooser slice should always be connected to at least one downstream chart. See the [dynamic dimensions](data-card.md#using-dynamic-columns-or-measures) section below.
{% endhint %}

#### To add a dimension chooser:

* select **Chooser** from the chart list

![Select Chooser from the dropdown](<../../../../.gitbook/assets/image (281).png>)

* select the dimensions you want to add in the order you want them displayed

![A column chooser slice](<../../../../.gitbook/assets/image (455).png>)

* add slice text (optional)
* click **Save changes**

{% hint style="info" %}
The type of chooser is determined by whether you add a dimension or measure first. Once you select the first dimension, only dimensions can be added.&#x20;
{% endhint %}

## Using dynamic dimensions or measures

Chooser slices are particularly powerful when slices further down the report refer to the selections in the chooser.

{% hint style="info" %}
Chooser values will be "display only" (i.e., unselectable) unless a downstream slice includes a dynamic dimensions or measure referring to the chooser.
{% endhint %}

To reference the selection made in a chooser slic&#x65;**:**&#x20;

* Create a dimension chooser or measure chooser using the instructions in the sections above
* In a downstream slice, select the chooser's slice slug in the column dropdown and/or measure dropdown

![Use dynamic ingredients in your charts to make them interactive](<../../../../.gitbook/assets/image (425).png>)

Here's how to make your charts dynamic:

{% embed url="https://www.loom.com/share/460990e6e0464d369bb0f717ec2bfb3c" %}

After making your chart dynamic, you may want to make your slice text dynamic as well. To learn how, go [here](../dynamic-text.md).&#x20;
