# Advanced formats \[incomplete\]

The [most commonly used formats](../defining-ingredients/ingredient-formats.md) are available in the basic ingredient editor. But if you need to use a different format, you can [add an advanced ingredient](../defining-ingredients/#adding-an-advanced-ingredient) and adjust the `format:` component within the advanced ingredient definition.

## Advanced number formats

You can use  [d3 number formats](https://github.com/d3/d3-format) to adjust how numbers display in your story. For example, let's say you want to display `Overweight %` with 1 decimal. Because the basic ingredient editor does not include an option to display a percent with 1 decimal, you will need to do this as an advanced ingredient, like so:

![Set format to a percent with 1 decimal](../../../.gitbook/assets/image%20%2848%29.png)

## Advanced date formats

You can use [d3 date formats](https://github.com/d3/d3-time-format) to adjust how dates display in your story. For example, let's say you want to display `Year Dates` like \[\]. Because the basic ingredient editor does not include an option to display a date like \[\], you will need to do this as an advanced ingredient, like so:

