# Advanced formats \[incomplete\]

Juicebox uses d3 for number and date formatting. The [most commonly used formats](ingredient-formats.md) are available in the basic ingredient editor. But if you need to use a different format, you can adjust the `format:` component within an advanced ingredient definition.

## Advanced number formats

You can use any [d3 number format](https://github.com/d3/d3-format) to adjust how numbers display in your story. For example, let's say you want to display Overweight % and Obesity % with 1 decimal. Because the basic ingredient editor does not include an option to display a percent with 1 decimal, you will need to do this as an advanced ingredient, like so:

![Set format to a percent with 1 decimal](../../../.gitbook/assets/image%20%2848%29.png)

## Advanced date formats

