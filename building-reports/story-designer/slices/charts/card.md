# Card

The Card slice is used to display selected columns and measures on cards. Users can select cards to filter downstream results. Here's an example of a Card slice:

<figure><img src="../../../../.gitbook/assets/image (545).png" alt=""><figcaption><p>Example Card slice</p></figcaption></figure>



On the **Configure** tab, you can add the following:&#x20;

**Title**. A dimension ingredient with values to display as card titles.

**Long text**. A dimension ingredient with values to display as card text.&#x20;

**Secondary data**. Up to 3 measure ingredients to display on each card.

**Image**. A dimension ingredient with urls to images to display on each card.&#x20;

All configuration fields are optional, but you must make a selection in at least one of the fields. In most cases, you will want to configure at least the **Title** field. There will be a card for each distinct combination of **Title**, **Long text**, and **Image**.&#x20;

Here's the **Configure** tab for the example above:

<figure><img src="../../../../.gitbook/assets/image (546).png" alt=""><figcaption><p>Card slice Configure tab</p></figcaption></figure>

On the **Style** tab, you can adjust how the elements display in the slice. Here's the Style tab for the example above:&#x20;

<figure><img src="../../../../.gitbook/assets/image (547).png" alt=""><figcaption></figcaption></figure>

## Displaying cards with measure gauges

There are two gauge card styles: Detail Gauge and Simple Gauge. These require a special configuration.&#x20;

At least one measure ingredient will need to be added to the Card slice configuration. Each measure ingredient will need to have ranges defined in the Advanced/Ranges section of the measure ingredient editor, like so:

```yaml
- color: lightgray
  label: Poor
  endValue: 0.4
  startValue: 0
- color: gray
  label: Meh
  endValue: 0.7
- color: lightblue
  label: Top Tier
  endValue: 1
```

In this example, we have three ranges: "Poor", "Meh", and "Top Tier". Each range is represented by a different color and has a specific start and end value. The "Poor" range starts at 0 and ends at 0.4, the "Meh" range ends at 0.7, and the "Top Tier" range ends at 1.

Here's a Card slice with the Simple Gauge card style:

<figure><img src="../../../../.gitbook/assets/image (548).png" alt=""><figcaption><p>Card slice using the Simple Gauge card style</p></figcaption></figure>

The Sales measure used in this example has the following ranges defined under Advanced/Ranges in the measure ingredient editor:&#x20;

```yaml
- color: "#ee6055"
  label: Below
  endValue: 4000000
  startValue: 0
- color: "#eaf4f4"
  label: On Target
  endValue: 5500000
- color: "#60d394"
  label: Above
  endValue: 20000000
```

In this example, there are three ranges: "Below", "On Target", and "Above". Each range is represented by a different color using hex codes and has a specific start and end value. The "Below" range starts at 0 and ends at 4 million, the "On Target" range ends at 5.5 million, and the "Above" range ends at 20 million.
