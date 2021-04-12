---
description: The first step in adding a data source is loading data.
---

# Loading data

There are two steps to adding a data source: 

1. upload or connect to your data
2. add your data ingredients

This section covers the first step. \(The second step is covered [here](adding-ingredients/).\) You can upload a CSV or, in a future release, connect to a database table or view or a Google Sheet.

## Upload a CSV

To upload a CSV, click **Connect & Upload Data Sources**, select **CSV**, and then select the CSV file to be uploaded. 

{% hint style="warning" %}
When using CSVs, it is important that your data be nice and clean. Common problem areas include missing data ****and text values in numeric columns. Here are some tips for [preparing your data](../design-tips/preparing-your-data.md). 
{% endhint %}

{% embed url="https://www.loom.com/share/d54b4b43aa194b76a4057d713963f4d1" caption="Add a data source by uploading a CSV" %}

### The data preview

After the data loads, the **data preview** will pop up, providing a preview of your data. The preview will only show a sample of your data records.  

![](../../.gitbook/assets/image%20%28131%29.png)

{% hint style="success" %}
After loading your data, do a quick review of the data preview for anything unexpected. If you spot something unexpected, this usually indicates an issue with the data. Here are some common examples:

* Do any numeric fields have a`string`data type? That likely means you have non-numeric data in the column \(e.g., spaces, commas, "N/A", "null", "-"\). Any field you plan to use in a sum or average calculation must have the`number`data type. 
* Do any date fields have a`string`data type? That likely means you have non-date data in the column. Any date fields you want to use in a [trend](../story-designer/charts/trend.md) chart must have the`date`data type. 
* Does a field name have unexpected underscores \(e.g., `_column_name_`, rather than `column_name`\)? That likely means there are leading or trailing spaces in your column headings.

Spotting and fixing these issues early and re-loading your data will save you time and frustration down the road. 
{% endhint %}

To exit the data preview, simply click outside of the data preview window. To return to the data preview, select the the data source button from the list of data sources.

![Click the data preview button to access the data preview](../../.gitbook/assets/image%20%28130%29.png)

## Connect to Sample Data

Juicebox also provides a selection of sample data tables if you want to start exploring before you have your own data. You can start by selecting **Connect & Upload Data Sources** then **Sample Data**.

![Choosing the Sample Data connection](../../.gitbook/assets/sample-data%20%281%29.jpg)

Choose a table to get started and select **Add Table**.

![](../../.gitbook/assets/choose-a-table.jpg)

The sample data includes the following tables. 

| Sample Data | Description |
| :--- | :--- |
| lego\_sets |  **🎛 LEGO sets** \([CSV download](https://docs.google.com/spreadsheets/d/10lJ-WWUvI8A1ezdzK0NWvGp5hjKT73Nj2N9eccLQIqY/export?format=csv&gid=0) or see the data in a [Google Sheet](https://docs.google.com/spreadsheets/d/10lJ-WWUvI8A1ezdzK0NWvGp5hjKT73Nj2N9eccLQIqY/edit#gid=0)\). Source: [Kaggle](https://www.kaggle.com/mterzolo/lego-sets) |
| movie\_trends |  **🎬 Movie Trends** \([CSV download](https://docs.google.com/spreadsheets/d/1FyPKMdoHskUyDLJzo66fq5LBZxwIcot-JWGakXz9D_o/export?format=csv) or see the data in a [Google Sheet](https://docs.google.com/spreadsheets/d/1FyPKMdoHskUyDLJzo66fq5LBZxwIcot-JWGakXz9D_o/)\). Source: [Kaggle](https://www.kaggle.com/) |
| olympic\_medals |  **🥇Olympic Medals 1896-2012** \([CSV download](https://docs.google.com/spreadsheets/d/1t5VH3Psl2O-ooo8vYPLkDplIWvUiYcQNeyJzVyiun98/export?format=csv&gid=0) or see the data in a [Google Sheet](https://docs.google.com/spreadsheets/d/1t5VH3Psl2O-ooo8vYPLkDplIWvUiYcQNeyJzVyiun98/edit#gid=0)\). Source: International Olympic Committee, The Guardian Datablog, and [Kaggle](https://www.kaggle.com/the-guardian/olympic-games) |
| video\_game\_sales |  **🎮 Video Game Sales** \([CSV download](https://docs.google.com/spreadsheets/d/1HGTdSQF62dQMwyTCq71XcN5lO4cI9WzNIRthT1Uh_eE/export?format=csv) or see the data in a [Google Sheet](https://docs.google.com/spreadsheets/d/1HGTdSQF62dQMwyTCq71XcN5lO4cI9WzNIRthT1Uh_eE)\). Source: [Kaggle](https://www.kaggle.com/gregorut/videogamesales). A helpful getting started [article and video](https://intercom.help/juiceboxdata/en/articles/4720121-simple-apps-dynamic-bar-chart-and-table) to create a dynamic bar chart. |
| world\_happiness\_report\_2020 | **😀 World Happiness Report 2020** \([CSV download](https://docs.google.com/spreadsheets/d/1UuRe1YL79gi8eeNDBM_oHMFiXUDvw4F2IJ6p9SNtZXI/export?format=csv&gid=6513579) or see the data in a [Google Sheet](https://docs.google.com/spreadsheets/d/1UuRe1YL79gi8eeNDBM_oHMFiXUDvw4F2IJ6p9SNtZXI/edit#gid=6513579)\). Source: [World Happiness Report](https://worldhappiness.report/ed/2020/) and [Data.World](https://data.world/makeovermonday) |

If you want more ideas on data to start with, check [https://help.myjuicebox.io/en/articles/4346552-sample-data-to-get-started](https://help.myjuicebox.io/en/articles/4346552-sample-data-to-get-started) 

## Connect to a database table

If your app is connected to a database, you can select the schema and table to use in the data source. If you are interested in connecting your app to a database, please reach out to us by clicking the chat button below. The following databases are supported:

* Redshift
* Snowflake
* Postgres
* SQL Server
* MySQL

## Connect to a Google Sheet \(future release\)

## Next step: Adding ingredients

After loading your data, the next step is [adding ingredients](adding-ingredients/). 

