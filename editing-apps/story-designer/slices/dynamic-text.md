# Dynamic text

Slice text can change dynamically based on what a user has selected in slices above. This is done using text templates. The two most commonly used text templates allow you to display selections or embed a filter pill.

{% hint style="info" %}
Dynamic text will only return _selections_ in Slices. It is best to add dynamic text after all charts have been configured as you like. 
{% endhint %}

{% hint style="warning" %}
At this time, selections in individual [Filters](../charts/filters.md) slice ingredients cannot be referenced.
{% endhint %}

## Display selections made above using selectionDisplay\(\)

If you want your slice text to display what was selected in an upstream slice, you can use the `selectionDisplay()` text template. For example, suppose you have a [data chooser](https://juicebox.gitbook.io/juicebox/authoring-apps/story-designer/charts/data-chooser#using-dynamic-ingredients) slice followed by a trend slice, and the measure used in the trend slice is the measure selected in the upstream data chooser slice. Your trend slice title says "Here's the trend for the measure selected above":

![The trend slice has a static title. Let&apos;s make it dynamic.](../../../.gitbook/assets/image%20%28230%29.png)

You want to replace the phrase "the measure selected above" with the label of the measure selected above. For example, If the user selects IMDb Rating in the data card slice, you want the trend slice title to display "Here's the trend for IMDb Rating." Likewise, if the user selects Budget, you want the trend slice title to display "Here's the trend for IMDb Rating" \(and so on\).  

To do this, you would replace "the measure selected above" in the slice text area with  `==sliceslug.selectionDisplay()==`, where `sliceslug` is the "slug" of the data chooser slice. The slug can be found in the chart config header.

![](../../../.gitbook/assets/image%20%28248%29.png)

Here's what that looks like:

{% embed url="https://www.loom.com/share/5e0455cac13341deac414ab5585a8a43" caption="Add dynamic text using selectionDisplay\(\)" %}

## Embed a filter pill using embedFilterPill\(\)

As with the `selectionDisplay()` text template described above, embedding a filter pill will display what was selected in an upstream slice. In addition, embedding a filter pill will enable the user to click the  pill and change the selection. This is done using the `embedFilterPill()` text template. 

Using the example from above, suppose you want to replace the phrase "the measure selected above" with a filter pill that displays what was selected above and allows the user to click the pill and make a different selection. To do this, you would replace "the measure selected above" in the slice text area with  `==sliceslug.embedFilterPill()==`, where `sliceslug` is the "slug" of the data chooser slice. The slug can be found in the slice header.

Here's what that looks like:

{% embed url="https://www.loom.com/share/47fcbd0a4dae4170acbf6f4320cd7605" caption="Add dynamic text using embedFilterPill\(\)" %}



