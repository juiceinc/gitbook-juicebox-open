# Add a data source

There are two steps to adding a data source: 

1. upload or connect to your data, and 
2. define your data ingredients.

## Upload or connect to your data

You can upload a CSV or connect to database table or view. \(Coming soon, you can connect to a Google Sheet.\)

### Upload a CSV

To upload a CSV, click **Connect & Upload Data** and select the CSV file. Then wait about 15-30 seconds. Once the CSV has loaded, a modal will pop up that confirms the [ingredients that were inferred from your data](define-data-ingredients/inferred-ingredients.md). 

{% hint style="warning" %}
When using CSVs, it is important that your data be nice and clean. Common problem areas include missing data, text values in numeric columns, and leading or trailing spaces. Here are some tips for [preparing your data](../data-outliner-tab/preparing-your-data.md). 
{% endhint %}

### Connect to a database table or view

To connect to a database table or view, click **Connect & Upload Data** and **\[TODO\]**.

### Connect to a Google Sheet \(coming soon!\)

**\[To come\]**

## Define your data ingredients

Data ingredients are the basic building block for every chart in your app. So before you can add charts to your app, you'll need ingredients.

### Initial ingredients

When you load or connect to your data, Juicebox will inspect a sample of your data and create an ingredient for each column in your data based on its best guess. 

* If the column contains only numeric values, a **measure** ingredient will be inferred.
* If the column contains only date **\[or datetime?\]** values, a **time** dimension ingredient will be inferred.
* If the column contains values other than numeric or date values, a **dimension** ingredient will be inferred. 

These initial ingredients are just a starting point for you. You can revise them or add new ones. 

### Ingredient components

Each ingredient has the following components:

* name
* kind
* field
* singular
* plural
* icon \(dimension only?\)
* format \(metric only?\)



