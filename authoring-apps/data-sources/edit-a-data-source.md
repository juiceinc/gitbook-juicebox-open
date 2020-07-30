# Edit or delete a data source

## Replace data

From time to time, you may want to update the data for a data source. For example, you may want to correct data in existing rows, add or remove rows, or add or remove columns. To do this, open the table view for the data source you want to update. Select Replace and select the CSV containing the replacement data to begin the upload process. Once the upload process finishes, refresh the page. The app will then display the updated data. 

![Use Replace to replace the data underlying the data source](../../.gitbook/assets/image%20%2882%29.png)

{% hint style="info" %}
The Replace functionality only updates the data underlying the data source. It does not update the name of the data source or the data ingredient definitions. 
{% endhint %}

### Fixing "sick ingredients" caused by changes in column names

So long as the column names in the new CSV are the same as in the old CSV, no further changes are needed. But if the column names have changed, you will need to point any affected ingredients to the new fields.  For example, suppose you have a `Student Name` dimension ingredient that points to the `student_name` field. Later, you replace the original data with a CSV that has column `studentname`, instead of `student_name`. Your app will display a "couldn't get the data" message for any slices that use the `Student Name` ingredient because that ingredient is pointing to a field that no longer exists in the data. This is called a "sick ingredient." To fix the ingredient, click on the `Student Name` ingredient pill and select the updated field name `studentname` from the dropdown. 

{% hint style="info" %}
If you see the "Couldn't get the data" error message in your app, this means there is one or more sick ingredient. To locate the sick ingredients, go to the slice in the app editor where you first see "Couldn't get the data" instead of the expected chart. This is the slice that has the first sick ingredient. After identifying and fixing the sick ingredient, refresh the page. Continue this process \(finding the slice with the first "Couldn't get the data" message, identifying the sick ingredient, and fixing the sick ingredient\), until the entire app loads without error. 
{% endhint %}

### Adding new ingredients from new columns

When you first add a data source, the [initial ingredients](add-a-data-source.md#initial-ingredients) are inferred. But ingredients are not inferred when replacing data. Therefore, if your updated CSV has additional columns, you will need to [add those ingredients](defining-ingredients/#adding-a-new-ingredient-from-the-table-view). 

## Update ingredient definitions

To make a change to an ingredient definition, click on the ingredient pill in either the Data Sources or Story Designer sections of the app editor. This will open up the ingredients editor.  From there, make the desired changes to the ingredient. Keep in mind that some changes may require that you [add an advanced ingredient](advanced-ingredients/).

## Delete a data source

If you have a data source that you don't plan to use in your app, you may want to delete the data source to declutter the Data Sources section of the app editor. To do this, open the table view for the data source you want to delete and select the ![](../../.gitbook/assets/trash-alt-regular.svg) button, then select **Yes, delete it**. 

{% hint style="warning" %}
You will receive a warning message if the data source ingredients are used in your app. In general, you should not delete a data source that is being used by an app. Doing so will cause all ingredients from the data source to become "sick." 
{% endhint %}

![A warning message appears if you attempt to delete a data source that is used in the app](../../.gitbook/assets/image%20%2883%29.png)

