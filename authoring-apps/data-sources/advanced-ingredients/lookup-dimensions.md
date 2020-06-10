# Lookup dimensions

If the dimension values in your data are not what you want displayed in your app, you can create a lookup dimension to change them. For example, the Unhealthy Americans data has a Question field with two distinct, very long values: "Percent of adults aged 18 years and older who have obesity" and "Percent of adults aged 18 years and older who have an overweight classification." Instead, you want to display "Obese" and "Overweight," respectively.  To do that, you would create an advanced ingredient like so:

![Advanced ingredient: lookup dimension](../../../.gitbook/assets/image%20%2837%29.png)

To create a lookup dimension, you add the `lookup:` component to the dimension definition.

```text
kind: Dimension
field: [field]
singular: [singular label]
plural: [plural label]
icon: [icon]
lookup:
  [value to lookup]:[value to display]
  [value to lookup]:[value to display]
  [value to lookup]:[value to display]
```

If there is a value in your data that is not added to the list of values to lookup, then the value in the data will be displayed. 

