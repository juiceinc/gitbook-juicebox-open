# Add a data source

There are two steps to adding a data source: 

1. upload or connect to your data
2. add your data ingredients

## Upload or connect to your data

You can upload a CSV or \(coming soon!\) connect to a database table or view or a Google Sheet.

### Upload a CSV

To upload a CSV, click **Connect & Upload Data** and select the CSV file. Then wait about 15-30 seconds. Once the CSV has loaded, a modal will pop up confirming that your data was loaded and the [initial ingredients ](add-a-data-source.md#initial-ingredients)were inferred from your data. 

{% hint style="warning" %}
When using CSVs, it is important that your data be nice and clean. Common problem areas include missing data ****and text values in numeric columns. Here are some tips for [preparing your data](../design-tips/preparing-your-data.md). 
{% endhint %}

{% embed url="https://www.loom.com/share/fe33cbc5b95d4e10817f15bcd7f9e4ae" caption="Upload a CSV" %}

{% hint style="success" %}
After loading your data, do a quick review of the [initial ingredients](add-a-data-source.md#initial-ingredients) for anything inferred in an unexpected way. If you spot something unexpected, this usually indicates an issue with the data. Here are some common examples:

* Did a field that should only have numbers get inferred as a Dimension? That likely means you have non-numeric data in the column \(e.g., spaces, commas, "N/A", "null", or "-"\).
* Is a field name showing with unexpected underscores \(e.g., `_column_name_`, rather than `column_name`\)? That likely means there are leading or trailing spaces in your column headings.

Spotting and fixing these issues early and re-loading your data will save you time and frustration down the road.
{% endhint %}

### Connect to a database table or view \(coming soon!\)

### Connect to a Google Sheet \(coming soon!\)

## Add your data ingredients

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

Each ingredient has a set of components:

| component | required by | description |
| :--- | :--- | :--- |
| kind | all | The ingredient type, either `Dimension` or `Measure`. |
| field | all | The instructions for what will display in the app. These instructions can be simple or advanced and are explained in more detail in the next sections.  |
| singular | all | The label displayed for measures or when one dimension value selected. |
| plural | all dimensions  | The label displayed when more than one dimension value is selected. |
| format | measures and time dimensions | The [number or date format](defining-ingredients/ingredient-formats.md) to be displayed. |
| icon | all | The [Font Awesome icon](https://fontawesome.com/icons?d=gallery) to display with your Dimension or Measure. By default, dimensions have `check-square`![](../../.gitbook/assets/check-square-solid.svg), time dimensions have `calendar`![](../../.gitbook/assets/calendar-solid.svg), place dimensions have `map-marker` ![](../../.gitbook/assets/map-marker-alt-solid.svg) , and measures have `hashtag` ![](../../.gitbook/assets/hashtag-solid.svg). |
| latitude\_field | place dimensions | Used in place dimension to set the latitude field. |
| longitude\_field | place dimensions | Used in place dimensions to set the longitude field. |

These components are configured as you [add your ingredients using the ingredients editor](defining-ingredients/). 



