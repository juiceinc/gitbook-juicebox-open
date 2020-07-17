# Dynamic text

Slice text can change dynamically based on what a user has selected in slices above. This is done using text templates. The two most commonly used text templates allow you to display selections or embed a filter pill.

{% hint style="info" %}
Dynamic text will only return _selections_ in Slices. It is best to add dynamic text after all charts have been configured as you like. 

Also, currently selections in individual [Filters](../charts/filters.md) slice ingredients cannot be referenced but that is coming soon.
{% endhint %}

## Display selections made above using selectionDisplay\(\)

If you want your slice text to display what was selected in an upstream slice, you can use the `selectionDisplay()` text template. For example, suppose you have a data card slice followed by a trend slice, and the measure used in the trend slice is the measure selected in the upstream data card slice. Your trend slice title says "See how the measure selected above changes over time":

![Trend slice has a static title](../../../.gitbook/assets/image%20%2873%29.png)

You want to replace the phrase "the measure selected above" with the label of the measure selected above. For example, If the user selects Overweight % in the data card slice, you want the trend slice title to display "See how Overweight % changes over time." Likewise, if the user selects Obese %, you want the trend slice title to display "See how Obese % changes over time." 

To do this, you would replace "the measure selected above" in the slice text area with  `==sliceslug.selectionDisplay()==`, where `sliceslug` is the "slug" of the data card slice. The slug can be found in the slice header.

![The slice slug is in the slice header](../../../.gitbook/assets/image%20%2872%29.png)

Here's what that looks like:

{% embed url="https://www.loom.com/share/7bb61e6e71b94983a0aea3a462691122" caption="Add dynamic text using selectionDisplay\(\)" %}

## Embed a filter pill using embedFilterPill\(\)

As with the `selectionDisplay()` text template described above, embedding a filter pill will display what was selected in an upstream slice. In addition, embedding a filter pill will enable the user to click the  pill and change the selection. This is done using the `embedFilterPill()` text template. 

Using the example from above, suppose you want to replace the phrase "the measure selected above" with a filter pill that displays what was selected above and allows the user to click the pill and make a different selection. To do this, you would replace "the measure selected above" in the slice text area with  `==sliceslug.embedFilterPill()==`, where `sliceslug` is the "slug" of the data card slice. The slug can be found in the slice header.

Here's what that looks like:

{% embed url="https://www.loom.com/share/c8509f862e0c4b6a99bce53c716f3422" caption="Add dynamic text using embedFilterPill\(\)" %}

{% hint style="warning" %}
At this time, you cannot use dynamic text that refers to selections made in filter slices.
{% endhint %}

