# Table

The table chart displays selected columns and measures as columns in a table. Users can search, sort, and download the data. To search, click the filter pill and search for any value in the table. To sort the data by the values in a column, click on the column header. If data download is enabled, click on the **Data** button to download the data as a CSV or Excel file. By default, selecting rows will filter downstream results.&#x20;

<figure><img src="../../../../.gitbook/assets/image (564).png" alt=""><figcaption><p>Example Table slice</p></figcaption></figure>

## Configure

The **Configure** tab has the following options (in addition to the [common slice configuration options](../#common-slice-configuration-options)):&#x20;

**Pick columns for your table**. Select the dimension and measure ingredients to show in the table. They will appear in the order selected.&#x20;

{% hint style="info" %}
Selected dimension and measures with a number data type will be right-aligned within the table column; all other data types will be left-aligned.&#x20;
{% endhint %}

**Enable download**. If enabled, users will be able to download the data.&#x20;

**File type**. If downloads are enabled, select either Excel or CSV for the download file type.&#x20;

## Style

The **Style** tab has the following options (in addition to the [common slice configuration options](../#common-slice-configuration-options)):

**Max rows per load**. Enter the number of rows to load. The default value is \[250].

**Show button to load more**. If enabled, a **Load more** button will display if the number of rows exceeds the **max rows per load** value. \[Why wouldn't this always be enabled?]

**Hide column icons**. If enabled, icons for all columns will be hidden.&#x20;

**Measure range coloring**. If enabled, ranges defined for measures in the the Advanced/Ranges section of the measure ingredient editor will be used to color the measure table cells. For example, in the example above, the **Avg Sales** measure has the following ranges defined:

<figure><img src="../../../../.gitbook/assets/image (565).png" alt=""><figcaption></figcaption></figure>

**Sort column**. Set which column to sort on and the sort order for the initial sort. (The user can override the sort order by clicking on the column header.)
