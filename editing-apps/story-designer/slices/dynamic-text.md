# Dynamic text

Slice text can change dynamically based on what a user has selected in slices above.

{% hint style="info" %}
It is best practice to add dynamic text after configuring charts. Dynamic text will only return selections_ _in charts.&#x20;
{% endhint %}

For example, suppose you have a [chooser](../charts/data-card.md) slice followed by a [trend](../charts/trend.md) slice, and the measure used in the trend slice is the measure selected in the upstream chooser slice. Your trend slice title says "Here's the trend for **the measure selected above**":

![The trend slice has a static title. Let's make it dynamic.](<../../../.gitbook/assets/image (307).png>)

You want to replace the phrase "the measure selected above" with the label of the measure selected above. For example, If the user selects **IMDb Rating** in the chooser slice, you want the trend slice title to display "Here's the trend for **IMDb Rating**." Likewise, if the user selects **Budget**, you want the trend slice title to display "Here's the trend for **Budget**" (and so on). &#x20;

To do this, you would replace "the measure selected above" in the slice text area with dynamic text that references the chooser slice. Clicking the "@" button in the chooser slice will copy the dynamic text reference, which you can then paste into the downstream slice text.

![The trend slice now has dynamic text that displays the selection made in the measure chooser slice](<../../../.gitbook/assets/image (304).png>)

Here's what that looks like:

{% embed url="https://www.loom.com/share/5e0455cac13341deac414ab5585a8a43" %}
Add dynamic text using selectionDisplay()
{% endembed %}

