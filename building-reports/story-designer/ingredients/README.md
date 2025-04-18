# Ingredients

Ingredients are used to configure [charts](../slices/charts/) in Juicebox. There are two types of ingredients: [dimensions](./#dimensions) and [measures](./#measures).&#x20;

## Dimensions

When you first load your data, you'll have one dimension ingredient for each column in your data. You can create additional dimensions from those data columns. For example, let's say your data has 3 columns: `First_Name`, `Last_Name`, and `Age`.  After you load your data, you'll have 3 dimension ingredients corresponding to these 3 columns.&#x20;

<figure><img src="../../../.gitbook/assets/image (499).png" alt=""><figcaption><p>Each column in the data becomes a dimension ingredient</p></figcaption></figure>

You can click on the ingredient pill to open the [ingredient editor](the-ingredient-editor/). The ingredient editor is where you can see and modify the ingredient definition.

<figure><img src="../../../.gitbook/assets/image (504).png" alt=""><figcaption><p>Click on the dimension ingredient pill to open the ingredient editor</p></figcaption></figure>

To create a new dimension, you could duplicate the **First Name** ingredient and modify it to add a new dimension ingredient called **Full Name** that concatenates `First_Name` and `Last_Name` together. After that, you'll have 4 dimension ingredients.&#x20;

<figure><img src="../../../.gitbook/assets/image (503).png" alt=""><figcaption><p>A new dimension ingredient called Full Name has been created</p></figcaption></figure>

## Measures

Measures are values calculated over a group of data records. Average sales, student count, and maximum price are all examples of measures. Measures are created using the following aggregation formulas: `sum()`, `avg()`, `min()`, `max()`, and `count_distinct()`.  Additional aggregations can be used as well (see [advanced field formulas](../../../editing-apps/data-sources/advanced-ingredients/advanced-formulas.md#aggregation-functions)) .  Measures are not displayed in the data preview. Instead you see existing measures and add new ones as you configure [charts](../slices/charts/).&#x20;

<figure><img src="../../../.gitbook/assets/image (505).png" alt=""><figcaption><p>New measures are added as you configure charts</p></figcaption></figure>

As with dimensions, you can click on measure ingredient pills to open the [ingredient editor](the-ingredient-editor/).&#x20;

<figure><img src="../../../.gitbook/assets/image (506).png" alt=""><figcaption><p>Click on the measure ingredient pill to open the ingredient editor</p></figcaption></figure>

