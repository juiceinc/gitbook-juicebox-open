# Advanced ingredients

In cases where you need to do something more than the [ingredient editor](../adding-ingredients/#ingredient-editor) allows, you can use advanced ingredients. Advanced ingredients are defined using the **advanced ingredient editor**. In the advanced ingredient editor, you define your ingredient using a text editor. This allows for [more complex ingredient definitions](./#what-you-can-do-with-advanced-ingredients), but is also more susceptible to typos or syntax errors. 

Advanced ingredients are added by [duplicating an existing ingredient as advanced](./#duplicating-an-existing-ingredient-as-advanced-from-within-the-ingredients-editor) from within the ingredient editor. To do this, open the ingredient editor by clicking the ingredient pill for the ingredient you want to duplicate. From there, select the menu icon \(![](../../../.gitbook/assets/ellipsis-h-solid.svg)\) and select **Duplicate as Advanced**. 

![Select Duplicate as Advanced to create an advanced ingredient](../../../.gitbook/assets/image%20%28213%29.png)

This will make a copy of the ingredient and open the advanced ingredient editor. Modify the ingredient components in the advanced ingredient editor as needed. 

![Duplicate ingredient created with advanced ingredient editor](../../../.gitbook/assets/image%20%28216%29.png)

## What you can do with advanced ingredients

Advanced ingredients have [ingredient components](../adding-ingredients/ingredient-components.md) that are defined in a text editor. The sections that follow demonstrate how to define those ingredient components based on what you want to do. Advanced ingredients allow you to define--

* Dimensions that [display a lookup value](lookup-dimensions.md) rather than the field value
* Dimensions that [group values into "buckets"](bucketed-dimensions.md) based on conditions 
* Measures and dimensions that [use field math](advanced-formulas.md#field-math)
* Measures that [use multiple aggregation functions](advanced-formulas.md#multiple-aggregate-functions)
* Measures and dimensions that [include conditional logic](advanced-formulas.md#conditional-logic)
* Measures or numeric dimensions formatted to [use any d3 number format](advanced-formats.md#advanced-number-formats)
* Date dimensions formatted to [use any d3 date format](advanced-formats.md#advanced-date-formats)

