# Adding ingredients

Ingredients are added in two ways: 

1. by adding a new ingredient from the table view
2. by duplicating an existing ingredient from within the ingredients editor

## Adding a new ingredient from the table view

You can add a new ingredient from the table view. To access the table view, click on the table view button for the data source: 

![Click the table view button to access the table view](../../../.gitbook/assets/image%20%2879%29.png)

To create a new ingredient form the table view:

* click the **+** next to the field that relates to the ingredient you want to add
* select the type of ingredient you want to create from the available options
* define the ingredient in the [ingredients editor](../add-a-data-source.md#ingredients-editor)

For example, here's how to create a new place dimension based on the `address` field in the `testdata` table view:

{% embed url="https://www.loom.com/share/7124db831b0445ecb13d9383677295f4" caption="Adding an ingredient from the table view" %}

## Duplicating an existing ingredient from within the ingredients editor

You can add a new ingredient by duplicating an existing ingredient. To do this, open the ingredients editor by clicking the ingredient pill for the ingredient you want to duplicate. From there, select the menu icon \(![](../../../.gitbook/assets/ellipsis-h-solid.svg)\) and select **Duplicate**. 

![Duplicating an ingredient](../../../.gitbook/assets/image%20%2877%29.png)

This will duplicate the ingredient and open the ingredients editor for the duplicated ingredient. Revise the ingredient definition as needed.  

![Ingredients editor for the duplicated ingredient](../../../.gitbook/assets/image%20%2878%29.png)

{% hint style="warning" %}
You cannot change the ingredient type when using the duplicate method. For example, you cannot create a place dimension ingredient from a measure ingredient. Therefore, the ingredient you select for duplication will need to be of the desired ingredient type. Alternatively, you can add a new ingredient of the desired type using the [table view method](./#adding-a-new-ingredient-from-the-table-view). 
{% endhint %}

