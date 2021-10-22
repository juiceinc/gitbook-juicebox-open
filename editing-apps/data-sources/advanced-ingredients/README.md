# Advanced columns and measures

If you need to do something more advanced with your column or measure, you can create an advanced column or measure.&#x20;

Advanced columns and measures allow you to define--

* Columns that [display a lookup value](lookup-dimensions.md) rather than the field value
* Columns that [group values into "buckets"](bucketed-dimensions.md) based on conditions&#x20;
* Measures and columns that [use field math](advanced-formulas.md#field-math)
* Measures that [use multiple aggregation functions](advanced-formulas.md#multiple-aggregate-functions)
* Measures and columns that [include conditional logic](advanced-formulas.md#conditional-logic)
* Measures or number columns formatted to [use any d3 number format](advanced-formats.md#advanced-number-formats)
* Time columns formatted to [use any d3 date format](advanced-formats.md#advanced-date-formats)

To create an advanced column or measure click on the orange pill for a related column or measure, select the menu icon (![](../../../.gitbook/assets/ellipsis-h-solid.svg)), and select **Duplicate as Advanced**. This will open the advanced column and measure editor (or advanced editor). In the advanced editor, you define your new column or measure [components](../adding-ingredients/ingredient-components.md) using yaml.&#x20;

![Select Duplicate as Advanced to create an advanced column or measure](<../../../.gitbook/assets/image (331).png>)

This will make a copy of the column or measure and open the advanced editor. Modify the components in the advanced editor as needed.&#x20;

![After duplicating as advanced, you can modify the column or measure as needed](<../../../.gitbook/assets/image (336).png>)

{% hint style="info" %}
The advanced column and measure editor lets you build complex and powerful columns and measures. But it is also more susceptible to typos or syntax errors. Please reach out to us if you need help building your advanced column or measure by clicking Help in the top right of your workspace and starting a chat with us.&#x20;
{% endhint %}

The sections that follow demonstrate how to define those ingredient components based on what you want to do:

{% content-ref url="lookup-dimensions.md" %}
[lookup-dimensions.md](lookup-dimensions.md)
{% endcontent-ref %}

{% content-ref url="bucketed-dimensions.md" %}
[bucketed-dimensions.md](bucketed-dimensions.md)
{% endcontent-ref %}

{% content-ref url="advanced-formulas.md" %}
[advanced-formulas.md](advanced-formulas.md)
{% endcontent-ref %}

{% content-ref url="advanced-formats.md" %}
[advanced-formats.md](advanced-formats.md)
{% endcontent-ref %}
