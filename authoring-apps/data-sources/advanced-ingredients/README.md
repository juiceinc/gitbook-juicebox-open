# Advanced ingredients

In cases where you need to do something more than the ingredient editor allows, you can use advanced ingredients. Advanced ingredients are added in two ways: 

1. by adding a new advanced ingredient from the table view
2. by duplicating an existing ingredient as advanced from within the ingredients editor

Advanced ingredients are defined using the advanced ingredients editor. In the advanced ingredients editor, you define your ingredient using YAML. This allows for [more complex ingredient definitions](./#what-you-can-do-with-advanced-ingredients), but is also more susceptible to syntax errors. 

## Adding a new advanced ingredient from the table view

You can add a new advanced ingredient from the table view. To access the table view, click on the table view button for the data source: 

![Click the table view button to access the table view](../../../.gitbook/assets/image%20%2879%29.png)

To create a new advanced ingredient from the table view, click the **+ Add Advanced** button. This will open the advanced ingredients editor where you can enter the ingredient components using a text editor. 

![](../../../.gitbook/assets/image%20%2881%29.png)

## Duplicating an existing ingredient as advanced from within the ingredients editor

You can add a new advanced ingredient by duplicating an existing ingredient as advanced. To do this, open the ingredients editor by clicking the ingredient pill for the ingredient you want to duplicate. From there, select the menu icon \(![](../../../.gitbook/assets/ellipsis-h-solid.svg)\) and select **Duplicate as Advanced**. 

![Select Duplicate as Advanced to create an advanced ingredient](../../../.gitbook/assets/image%20%2836%29.png)

This will make a copy of the ingredient and open the advanced ingredient text editor. Modify the ingredient definition in the text editor as needed. 

![Duplicate ingredient created with text editor](../../../.gitbook/assets/image%20%2843%29.png)

## What you can do with advanced ingredients

Advanced ingredients allow you to define the [ingredient components](../defining-ingredients/ingredient-components.md) in a text editor. Advanced ingredients allow you to use--

* Dimensions that were incorrectly interpreted as a measure
* Dimensions that [display a lookup value](lookup-dimensions.md) rather than the field value
* Dimensions that [group values into "buckets"](bucketed-dimensions.md) based on conditions 
* Measures and dimensions that [use field math](complex-formulas-incomplete.md#field-math)
* Measures that [use multiple aggregation functions](complex-formulas-incomplete.md#multiple-aggregate-functions)
* Measures and dimensions that [include conditional logic](complex-formulas-incomplete.md#conditional-logic)
* Measures or numeric dimensions formatted to [use any d3 number format](advanced-formats-incomplete.md#advanced-number-formats)
* Date dimensions formatted to [use any d3 date format](advanced-formats-incomplete.md#advanced-date-formats)

