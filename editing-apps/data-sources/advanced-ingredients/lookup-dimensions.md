# Lookup columns

If the values in a field are not what you want displayed in your app, you can create a lookup column to change them. For example, let's say your data has a Question field with two distinct, very long values:&#x20;

* "Percent of adults aged 18 years and older who have obesity"&#x20;
* "Percent of adults aged 18 years and older who have an overweight classification"&#x20;

Instead of those long values, you want to display "Obese" and "Overweight," respectively.  To do that, you could create an advanced ingredient like so:

![Advanced ingredient: lookup dimension ](<../../../.gitbook/assets/image (247).png>)

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
