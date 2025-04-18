# The dimension ingredient editor

## Header

In the ingredient editor header, you can set the icon and label, view the source data table, and access perform various actions from the gear menu.&#x20;

<figure><img src="../../../../.gitbook/assets/image (510).png" alt=""><figcaption><p>The dimension ingredient header</p></figcaption></figure>

**Icon**. This is a [FontAwesome](https://fontawesome.com/) icon associated with the dimension ingredient.  By default, text dimensions have `check-square`<img src="../../../../.gitbook/assets/check-square-solid.svg" alt="" data-size="line">, time dimensions have `calendar`<img src="../../../../.gitbook/assets/calendar-solid.svg" alt="" data-size="line">, place dimensions have `map-marker-alt` <img src="../../../../.gitbook/assets/map-marker-alt-solid.svg" alt="" data-size="line"> , and number dimensions and measures have `hashtag` <img src="../../../../.gitbook/assets/hashtag-solid.svg" alt="" data-size="line">. The default icon can be changed, or the icon can be removed.&#x20;

**Label**. This is the ingredient label. It is the same as the Plural label.&#x20;

**Data table**. This displays the name of the source data table.&#x20;

**Gear menu**. Provides access to the following actions:&#x20;

* **Duplicate column**. Creates a new dimension ingredient with the same definition. This is used to [add new ingredients](adding-new-ingredients.md).&#x20;
* **Duplicate as Advanced**. Creates a new dimension ingredient with the same definition expressed in yaml. This is used in cases where the UI does not yet support a particular configuration option. In most cases, you should not need to duplicate as Advanced.
* **Copy ingredient ID**. Copies the underlying ingredient ID for use in complex ingredient field formulas.&#x20;
* **Delete column**. Deletes the ingredient.&#x20;

## Basics

The Basics section of the ingredient editor contains the options that are required or used most frequently.&#x20;

<figure><img src="../../../../.gitbook/assets/image (511).png" alt=""><figcaption><p>The dimension ingredient Basics section</p></figcaption></figure>

**Field formula**. This is where the ingredient logic is defined. It could be the name of a single column or it could involve [complex logic](advanced-formulas.md).&#x20;

**Plural label**. This is the label that will be used when the user selects multiple dimension values or no dimension values in the report.&#x20;

**Singular label**. This is the label that will be used when the user selects a single dimension value in the report.&#x20;

**Number format**. Only for dimensions with a number data type. Select how values should be formatted from the dropdown, or enter a custom [number format](ingredient-formats.md).&#x20;

**Time format**. Only for date or time dimensions. Select how values should be formatted from the dropdown, or enter in a custom [time format](time-formats.md).&#x20;

{% hint style="success" %}
Date or time ingredients will "roll up" in charts to the period selected for the **Time format**. For example, selecting the `month yyyy` format will roll up to the month. Selecting the `yyyy` format will roll up to the year.&#x20;
{% endhint %}

**Latitude**. Only for place dimensions. Enter the column associated with latitude value.&#x20;

**Longitude**. Only for place dimensions. Enter the column associated with the longitude value.&#x20;

**Geometry Field**. Only for place dimensions. Enter the column associated with the geojson geometry field.&#x20;

## Styling

Description

Color

Color when negative

Image url

**Hide count**. By default, filter pills will display the count of distinct dimension values. Enable this option if you want to hide the count.&#x20;

## Advanced

#### Buckets

A bucketed dimension groups field values into buckets based on [conditions](advanced-formulas.md#conditional-logic) in the **Buckets** box, like so:

```
- label: [label 1]
  condition: [condition 1]
- label: [label 2]
  condition: [condition 2]
- label: [label 3]
  condition: [condition 3]
```

For example, let's say your data includes a `score` field with customer scores, and you want to use the scores to group customers into different roles: Detractor, Passive, and Promoter. Here's what you would enter in the **Buckets** box:

<figure><img src="../../../../.gitbook/assets/image (566).png" alt=""><figcaption><p>Adding buckets</p></figcaption></figure>

Conditions are evaluated in the order they are defined, which makes defining buckets for continuous values convenient:&#x20;

```
- label: Under 25k
  condition: <25000
- label: 25k-49k
  condition: <50000
- label: 50k-99k
  condition: <99000
```

The **Buckets default label** is the label to display if a value does not meet any of the conditions.&#x20;

#### Lookups

If the values in a field are not what you want displayed in your report, you can create lookups to change them by entering a list of values to lookup with their associated value to display in the **Lookups** box, like so:

```
[value to lookup]: [value to display]
[value to lookup]: [value to display]
[value to lookup]: [value to display]
```

For example, let's say the Country field has "United States" values that you want to display as "USA", and it has null values that you want to display as "Unknown".  Here's what you would enter in the **Lookups** box:

<figure><img src="../../../../.gitbook/assets/image (521).png" alt=""><figcaption><p>Adding Lookups</p></figcaption></figure>

If there is a value in the field that is not added to the list of values to lookup, then the original value in your data will be displayed.&#x20;

Id Field. Specify a custom unique identifier for columns. Especially useful for selections and filtering in unique cases. {I don't really understand what this means}

**Hide dimension labels**

You could use `id_field` on an Advanced Dimension column to preserve selection filtering while also providing the `field` with an empty string:

```
field: string(" ")
id_field: last_name
```

Order By

Filter

**Reverse**. By default, higher numbers are deemed "better." To flip this, turn on Reverse. {Why is this in the dimension ingredient? Doesn't it only impact measures?}
