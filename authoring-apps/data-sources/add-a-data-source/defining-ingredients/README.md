# Defining ingredients

## \[Do not move or rename this page\]

Ingredients are defined using the ingredient editor. To access the ingredient editor for an ingredient, click on the ingredient pill. \(You can select ingredient pills in either the Data Sources or the Story Designer sections of the app editor.\)

![Access ingredient editor by clicking on ingredient pill](../../../../.gitbook/assets/image%20%2834%29.png)

You can define ingredients using the basic ingredient editor or the advanced ingredient editor. Ingredients defined using the basic ingredient editor are called basic ingredients. Ingredients defined using the advanced ingredient editor are called advanced ingredients. 

## Basic ingredients

Basic ingredients are defined using the basic ingredient editor. Basic ingredients look like this:

### Basic dimension

![A basic dimension](../../../../.gitbook/assets/image%20%2846%29.png)

### Basic measure

![A basic measure](../../../../.gitbook/assets/image%20%2835%29.png)

Sometimes the options available in the basic ingredient editor will not be sufficient to define your desired ingredient. In those cases, you will need to add an advanced ingredient. 

## Advanced ingredients

In cases where you need to do something more than the basic ingredient editor allows, you can use advanced ingredients. 

### Adding an advanced ingredient

To create an advanced ingredient, click on the ingredient pill for a field you will use in your definition. From there, click the menu icon \(![](../../../../.gitbook/assets/ellipsis-h-solid.svg)\), and select **Duplicate as Advanced**. 

![Select Duplicate as Advanced to create an advanced ingredient](../../../../.gitbook/assets/image%20%2836%29.png)

This will make a copy of the ingredient and open the advanced ingredient editor. The advanced ingredient editor is essentially a text editor. Modify the ingredient definition in the text editor as needed. 

![Duplicate ingredient created with text editor](../../../../.gitbook/assets/image%20%2843%29.png)

### What you can do with advanced ingredients

Advanced ingredients allow you to define the [ingredient components](../#ingredient-components) in a text editor. Advanced ingredients allow you to use--

* Dimensions that [display a lookup value](lookup-dimensions.md) rather than the field value
* Dimensions that [group values into "buckets"](bucketed-dimensions.md) based on conditions 
* Filters that [group values into frequently-used filter ranges](quickselect-filters-incomplete.md) based on conditions
* Measures that [use field math](complex-formulas-incomplete.md#field-math)
* Measures that [use multiple aggregation functions](complex-formulas-incomplete.md#multiple-aggregate-functions)
* Measures and dimensions that [reference other measures and dimensions](complex-formulas-incomplete.md#references-to-other-measures-and-dimensions)
* Measures and dimensions that [include conditional logic](complex-formulas-incomplete.md#conditional-logic)
* Measures or numeric dimensions formatted using any d3 number format
* Date dimensions formatted using any d3 date format

