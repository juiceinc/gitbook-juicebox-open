# Lookup columns

If the values in a field are not what you want displayed in your report, you can create a lookup column to change them. For example, let's say your data has a Country field with the full name of each country, but you only want to display an abbreviation. To do that, you could create an advanced ingredient like so:

![Advanced column using lookup](<../../../.gitbook/assets/image (475).png>)

To create a lookup dimension, you add the `lookup:` component to the column definition. The lookup values need to be indented consistently.

```
kind: Dimension
field: [field]
singular: [singular label]
lookup:
  [value to lookup]: [value to display]
  [value to lookup]: [value to display]
  [value to lookup]: [value to display]
```

If there is a value in the field that is not added to the list of values to lookup, then the original value in your data will be displayed.&#x20;
