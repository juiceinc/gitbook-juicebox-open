---
description: >-
  Access Views combine data permissions, selections, security, and app features
  into a view that you can embed or share with users.
---

# Access Views

### How to set selections on an Access View

You can preselect items for your users on the Access View. A selections object contains keys that are a colon delimited pair of the Slice Slug and the Ingredient Id of the Ingredient used in the slice.

```
{
   "{Slice Slug}:{Ingredient Id for Slice 1}": [{List of values}],
   "{Slice 2 Slug}:{Ingredient Id for Slice 2}": [{List of values}]
}
```

You can find the **Slice Slug** in the editor.&#x20;

<figure><img src="../.gitbook/assets/image (403).png" alt=""><figcaption><p>The Slice Name</p></figcaption></figure>

The **Ingredient Id** can be found by selecting the Ingredient grouping used in the slice, then selecting "Copy Ingredient Id" in the ingredient editor.

<figure><img src="../.gitbook/assets/image (404).png" alt=""><figcaption><p>Getting the Ingredient Id</p></figcaption></figure>

### Making selections in a chooser

Choosers can just include the chooser slice name.

```
{ 
   "{Chooser Slice Name}": [{Ingredient Id to select}]
}
```

For choosers, you need to get the Ingredient Id for the Ingredient you want to select

<figure><img src="../.gitbook/assets/image (405).png" alt=""><figcaption><p>Finding Ingredient Ids for a Chooser</p></figcaption></figure>

To select the third "Count of Date and Time" ingredient in the chooser above, you'd use this selections object.

```
{
   "Choice1": ["metric_dateandtime_z936yh2d"]
}
```

### Making selections in the Access View URL.

You can also make selections using the url. To do so, pass the data like this:

```
{url}?Choice1=metric_dateandtime_z936yh2d
```

Here's an example of a complex selection that selects one choice and two items on a leaderboard. All of this would appear on a single line, but we're splitting it to make it easier to read. Note that spaces need to be [url-encoded ](https://www.wikiwand.com/en/URL\_encoding)by replacing them with a "+" sign or "%20".

```
{url}?Choice1=metric_num_5fta5sgd
&Leaderboard1:title=Beginning+of+2020
&Leaderboard1:title=End+of+Aug+15
```

The result looks like this:

<figure><img src="../.gitbook/assets/image (406).png" alt=""><figcaption><p>One choice and two leaderboard selections</p></figcaption></figure>
