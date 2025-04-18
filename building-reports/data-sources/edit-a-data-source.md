# Managing data

## Replace uploaded data

To update uploaded data, click the **Replace file** button. If there is more than one data table in your report, select the data table that you want to update. (Alternatively, select the data table you want to update, click the gear icon, and select **Replace file** from the menu.) Then, select the new data file (CSV, XLS, or XLSX).&#x20;

![Select the Replace file button to update a data table](<../../.gitbook/assets/image (315).png>)

Once the upload process finishes, refresh the page. The report will then display the updated data.&#x20;

{% hint style="success" %}
It is good practice to share before replacing data. That way, if you select the wrong CSV (or something else goes wrong), you can Discard changes and revert back to where things were before doing the replace.
{% endhint %}

## Clear the data cache

To improve performance, charts display cached data. The cache is cleared periodically (by default, every 2 hours), but the cache can be cleared manually by clicking the **Clear Data Cache** button and selecting **Yes, clear it**. The cache will be cleared for all data tables.&#x20;

<figure><img src="../../.gitbook/assets/image (522).png" alt=""><figcaption></figcaption></figure>

The caching period is set at the database connection level and the current options are: no caching, cleared after 2 hours, cleared after 1 day, or cleared after 1 year. If you would like the caching period adjusted for a particular database connection, [reach out to us](../../getting-started/reach-out-to-us.md).&#x20;

{% hint style="info" %}
If changes to the structure of a database-connected table are not reflected after clearing the data cache, [reach out to us](../../getting-started/reach-out-to-us.md).&#x20;
{% endhint %}

## Delete a data table

If you have data table that you don't plan to use in your report, you may want to delete the data table to declutter the data drawer. To do this, open the data drawer, select the data table you want to delete, click the gear icon, and select **Delete**.

<figure><img src="../../.gitbook/assets/image (524).png" alt=""><figcaption><p>Deleting a data table</p></figcaption></figure>

{% hint style="warning" %}
You will receive a warning message if the data table columns are used in your report.&#x20;
{% endhint %}

If you are sure you want to delete the data table, click **Yes, delete it**.

![A warning message appears if you attempt to delete a data table that is used in the report](<../../.gitbook/assets/image (114).png>)

## Download data

You can download the data in a data table by opening the data drawer, selecting the data table you want to download, clicking the gear icon, and selecting **Download**. The data will download as a CSV.

<figure><img src="../../.gitbook/assets/image (523).png" alt=""><figcaption><p>Downloading data</p></figcaption></figure>

