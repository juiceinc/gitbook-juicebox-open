# Ingredient components

Each ingredient has a set of components that are configured as you [add your ingredients using the ingredients editor](./). 

| component | required by | description |
| :--- | :--- | :--- |
| kind | all | The ingredient type, either `Dimension` or `Metric`. |
| field | all | The instructions for what will display in the app. These instructions can be simple or advanced and are explained in more detail in the next sections.  |
| singular | all | The label displayed for measures or when a single dimension value is selected. |
| plural | all dimensions  | The label displayed when more than one dimension value is selected. |
| format | measures and time dimensions | The [number or date format](ingredient-formats.md) to be displayed. |
| icon | all | The [Font Awesome icon](https://fontawesome.com/icons?d=gallery) to display with your Dimension or Measure. By default, dimensions have `check-square`![](../../../.gitbook/assets/check-square-solid.svg), time dimensions have `calendar`![](../../../.gitbook/assets/calendar-solid.svg), place dimensions have `map-marker-alt` ![](../../../.gitbook/assets/map-marker-alt-solid.svg) , and measures have `hashtag` ![](../../../.gitbook/assets/hashtag-solid.svg). |
| latitude\_field | place dimensions | Used in place dimensions to set the latitude field. |
| longitude\_field | place dimensions | Used in place dimensions to set the longitude field. |
| lookup | none | See [lookup dimensions](../advanced-ingredients/lookup-dimensions.md) section. |
| buckets | none | See [bucketed dimensions](../advanced-ingredients/bucketed-dimensions.md) section. |
| buckets\_default\_label | none | See [bucketed dimensions](../advanced-ingredients/bucketed-dimensions.md) section. |



