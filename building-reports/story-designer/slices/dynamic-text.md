# Dynamic text

Slice text can change dynamically based on what a user has selected in slices above.

{% hint style="info" %}
It is best practice to add dynamic text after configuring charts. Dynamic text will only return selections in charts.&#x20;
{% endhint %}

For example, suppose you have a [chooser](charts/data-card.md) slice followed by a [trend](charts/trend.md) slice, and the measure used in the trend slice is the measure selected in the upstream chooser slice. Your trend slice title says "Here's the trend for **the measure selected above**":

![The trend slice has a static title. Let's make it dynamic.](<../../../.gitbook/assets/image (151).png>)

You want to replace the phrase "the measure selected above" with the label of the measure selected above. For example, If the user selects **IMDb Rating** in the chooser slice, you want the trend slice title to display "Here's the trend for **IMDb Rating**." Likewise, if the user selects **Budget**, you want the trend slice title to display "Here's the trend for **Budget**" (and so on). &#x20;

To do this, you would replace "the measure selected above" in the slice text area with dynamic text that references the chooser slice. Clicking the "@" button in the chooser slice will copy the dynamic text reference (also called the "slice slug"), which you can then paste into the downstream slice text.

![The trend slice now has dynamic text that displays the selection made in the measure chooser slice](<../../../.gitbook/assets/image (287).png>)

Here's what that looks like:

{% embed url="https://www.loom.com/share/5e0455cac13341deac414ab5585a8a43" %}
Add dynamic text
{% endembed %}

### More dynamic text shortcuts

You can access other details about a slice with the following shortcuts.

| Shortcut      | Description                                                            |
| ------------- | ---------------------------------------------------------------------- |
| @Slice.pill   | Display a selectable pill that lets you change the selection in Slice. |
| @Slice.label  | Show a label for what kind of item is being selected in Slice.         |
| @Slice.list   | List the selections in Slice.                                          |
| @Slice.count  | Show the total number of unique items in  Slice.                       |
| @Slice.number | Show the total number of selected items in Slice                       |

Here's an example

We have a slice that lets you look at a leaderboard of Directors using the Movie Trends data.&#x20;

<figure><img src="../../../.gitbook/assets/image (26).png" alt=""><figcaption><p>This slice is Leaderboard1</p></figcaption></figure>

We can use the dynamic text below to show and change details about what is selected. Here's the text

_@Leaderboard1.number selected out of @Leaderboard1.count @Leaderboard1.label_

_The selections are @Leaderboard1.list_

_Change them yourself here @Leaderboard1.pill_



Here's what this looks like.

<figure><img src="../../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>
