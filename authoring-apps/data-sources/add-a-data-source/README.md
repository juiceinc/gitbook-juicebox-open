# Add a data source

There are two steps to adding a data source: 

1. upload or connect to your data
2. define your data ingredients

## Upload or connect to your data

You can upload a CSV or \(coming soon!\) connect to a database table or view. \(Coming soon, you can connect to a Google Sheet.\)

### Upload a CSV

To upload a CSV, click **Connect & Upload Data** and select the CSV file. Then wait about 15-30 seconds. Once the CSV has loaded, a modal will pop up confirming that your data was loaded and the [initial ingredients ](./#initial-ingredients)were inferred from your data. 

{% hint style="warning" %}
When using CSVs, it is important that your data be nice and clean. Common problem areas include missing data, text values in numeric columns, and leading or trailing spaces. Here are some tips for [preparing your data](../../design-tips/preparing-your-data.md). 
{% endhint %}

Here's a video showing how to upload a CSV:

**\[TODO: insert video\]**

\*\*\*\*

{% hint style="success" %}
After loading your data, do a quick review of the [initial ingredients](./#initial-ingredients) for anything inferred in an unexpected way. If you spot something unexpected, this usually indicates an issue with the data. Here are some common examples:

* Did a field that should only have numbers get inferred as a Dimension? That likely means you have non-numeric data in the column \(e.g., spaces, commas, "N/A", "null", or "-"\).
* Is a field name showing with unexpected underscores \(e.g., `_column_name_`, rather than `column_name`\)? That likely means there are leading or trailing spaces in your column headings.

Spotting and fixing these issues early and re-loading your data will save you time and frustration down the road.
{% endhint %}

### Connect to a database table or view \(coming soon!\)

### Connect to a Google Sheet \(coming soon!\)

## Define your data ingredients

Data ingredients are the basic building blocks for every chart in your app. So before you can add charts to your app, you'll need ingredients.

### Initial ingredients

When you load or connect to your data, Juicebox will inspect a sample of your data and create an ingredient for each column in your data based on its best guess. These initial ingredients are also called **inferred ingredients** and follow these rules:

* If the column contains only numeric values, a **measure** ingredient will be inferred.
* If the column contains only date values, a **time** dimension ingredient will be inferred.
* If the column contains values other than numeric or date values, a **dimension** ingredient will be inferred. 

The initial ingredients are just a starting point. You can revise them or add new ones. 

{% hint style="warning" %}
If you delete the inferred ingredient for a field in your data without adding another ingredient for that field, the deleted ingredient will be inferred again when you save your ingredients. 
{% endhint %}

### Ingredient components

Each ingredient has the following components:

* **kind**. The ingredient type, either `Dimension` or `Measure`. 
* **field**. The instructions for what will display in the app. These definitions can be basic or advanced and are explained in more detail in the next sections. 
* **singular**. The label displayed for the dimension or measure. 
* **plural**. The label displayed when more than one dimension value is selected in the app. The `plural`component is only used by dimensions.
* **format**. The number or date format to be used. The `format` component is only used to format numbers and dates. 
* **icon**. The Font Awesome icon to display with your Dimension or Measure. By default, measures will have `hashtag` \(![](../../../.gitbook/assets/hashtag-solid.svg)\) and dimensions will have `check-square`\( ![](../../../.gitbook/assets/check-square-solid.svg) \). 

These components are configured as you [define your ingredients](defining-ingredients.md). 



