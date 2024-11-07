# Loading data

You must load data before you can configure charts. There are three ways to load data:

1. Upload a data file
2. Connect to sample data
3. Connect to a database table

## Upload a data file

To upload the report's first data file, open the data drawer and drag a flat file (CSV, XLS, or XLSX) containing your data onto the data upload box or click **Upload CSV or Excel** and select the file to be uploaded. The file will be loaded to a BigQuery table and connected to the report.&#x20;

<figure><img src="../../.gitbook/assets/image (11).png" alt=""><figcaption><p>Add data by uploading a CSV or Excel file</p></figcaption></figure>

To load additional data files, first click the + and then drag-and-drop or select your CSV or Excel file.

<figure><img src="../../.gitbook/assets/image (13).png" alt=""><figcaption><p>Click the "+" in the data drawer to add additional data files</p></figcaption></figure>

{% hint style="warning" %}
When loading data files, it is important that your data be nice and clean. Here are some tips for [preparing your data](../design-tips/preparing-your-data.md).&#x20;
{% endhint %}

## Connect to sample data

Juicebox also provides a selection of sample data tables if you want to start exploring before you have your own data. To load sample data, open the data drawer, select the **Sample Data** button, and choose one of the available datasets.&#x20;

<figure><img src="../../.gitbook/assets/image (14).png" alt=""><figcaption><p>Load sample data</p></figcaption></figure>

Choose a sample data table and select **Add Table**.

The sample data includes the following tables.&#x20;

| Sample Data                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| lego\_sets                     |  **🎛 LEGO sets** ([CSV download](https://docs.google.com/spreadsheets/d/10lJ-WWUvI8A1ezdzK0NWvGp5hjKT73Nj2N9eccLQIqY/export?format=csv\&gid=0) or see the data in a [Google Sheet](https://docs.google.com/spreadsheets/d/10lJ-WWUvI8A1ezdzK0NWvGp5hjKT73Nj2N9eccLQIqY/edit#gid=0)). Source: [Kaggle](https://www.kaggle.com/mterzolo/lego-sets)                                                                                                                                                                           |
| movie\_trends                  |  **🎬 Movie Trends** ([CSV download](https://docs.google.com/spreadsheets/d/1FyPKMdoHskUyDLJzo66fq5LBZxwIcot-JWGakXz9D\_o/export?format=csv) or see the data in a [Google Sheet](https://docs.google.com/spreadsheets/d/1FyPKMdoHskUyDLJzo66fq5LBZxwIcot-JWGakXz9D\_o/)). Source: [Kaggle](https://www.kaggle.com/)                                                                                                                                                                                                         |
| olympic\_medals                |  **🥇Olympic Medals 1896-2012** ([CSV download](https://docs.google.com/spreadsheets/d/1t5VH3Psl2O-ooo8vYPLkDplIWvUiYcQNeyJzVyiun98/export?format=csv\&gid=0) or see the data in a [Google Sheet](https://docs.google.com/spreadsheets/d/1t5VH3Psl2O-ooo8vYPLkDplIWvUiYcQNeyJzVyiun98/edit#gid=0)). Source: International Olympic Committee, The Guardian Datablog, and [Kaggle](https://www.kaggle.com/the-guardian/olympic-games)                                                                                         |
| video\_game\_sales             |  **🎮 Video Game Sales** ([CSV download](https://docs.google.com/spreadsheets/d/1HGTdSQF62dQMwyTCq71XcN5lO4cI9WzNIRthT1Uh\_eE/export?format=csv) or see the data in a [Google Sheet](https://docs.google.com/spreadsheets/d/1HGTdSQF62dQMwyTCq71XcN5lO4cI9WzNIRthT1Uh\_eE)). Source: [Kaggle](https://www.kaggle.com/gregorut/videogamesales). A helpful getting started [article and video](https://intercom.help/juiceboxdata/en/articles/4720121-simple-apps-dynamic-bar-chart-and-table) to create a dynamic bar chart. |
| world\_happiness\_report\_2020 | **😀 World Happiness Report 2020** ([CSV download](https://docs.google.com/spreadsheets/d/1UuRe1YL79gi8eeNDBM\_oHMFiXUDvw4F2IJ6p9SNtZXI/export?format=csv\&gid=6513579) or see the data in a [Google Sheet](https://docs.google.com/spreadsheets/d/1UuRe1YL79gi8eeNDBM\_oHMFiXUDvw4F2IJ6p9SNtZXI/edit#gid=6513579)). Source: [World Happiness Report](https://worldhappiness.report/ed/2020/) and [Data.World](https://data.world/makeovermonday)                                                                           |

## Connect to a database table or view

If your report is connected to a database, you can select the schema and table (or view) to use as the data source. If you are interested in connecting your report to a database, please reach out to us by emailing us at help@myjuicebox.io or by starting a chat from the Help menu (click the Help icon at the top right of the report header or workspace home page).  The following databases are supported:

* Redshift
* Snowflake
* Postgres
* BigQuery
* SQL Server

For databases that are not maintained on a cloud platform, we support the latest two release versions. Earlier versions may work with Juicebox, but are not supported.
