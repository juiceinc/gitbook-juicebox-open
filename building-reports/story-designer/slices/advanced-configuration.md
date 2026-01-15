---
description: Describe advanced configuration options
---

# Advanced Configuration

{% hint style="danger" %}
Once advanced configuration is set, it can be overwritten but **can not** be removed, even if you remove it from the advanced configuration panel.

To remove all advanced configuration completely, **duplicate** a slice.
{% endhint %}

Some configuration options are not available in the user interface. These can be set by opening the advanced configuration panel. There are two categories of advanced configuration: slice configuration and data configuration.

<figure><img src="../../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

Opening the configuration panel looks like this.

<figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### Slice configuration options

Slice configuration options can either appear at the top level or within a config object.

Like this:

```
config:
  option1: value1
  option2: value2
```

or like this

```
option1: value1
option2: value2
```

<table><thead><tr><th>Option</th><th width="245.8245849609375">Description</th><th>Required data type</th><th>Slices</th></tr></thead><tbody><tr><td>noDataMessage</td><td>A html message to display when no data has been returned to this slice.</td><td>A string containing valid html.</td><td>All slices</td></tr><tr><td>minSelections</td><td>The minimum number of data selections that must be selected in this slice. These selections will happen automatically.</td><td>Integer</td><td>All slices</td></tr><tr><td>maxSelections</td><td>The maximum number of data selections poissible</td><td>Integer</td><td>All slices</td></tr><tr><td>minZoom</td><td>The minimum zoom level that the map can zoom to</td><td>Integer</td><td>Map</td></tr><tr><td>maxZoom</td><td>The maximum zoom level that the map can zoom to</td><td>Integer</td><td>Map</td></tr><tr><td>numberOfRows</td><td>The number of rows to show in the leaderboard.</td><td>Integer</td><td>Leaderboard</td></tr><tr><td>includeAppSlugs</td><td>The slugs of apps that a user can link to. Users will only see apps that they have permission to see.</td><td>A list of strings containing valid app slugs.</td><td>Navigator</td></tr></tbody></table>

#### Data configuration options

Data configuration options affect what data shows up in the slice. These can either be configured under a data key, or at the top level.

Like this:

```
data:
  option1: value1
  option2: value2
```

or like this

```
option1: value1
option2: value2
```

<table><thead><tr><th>Option</th><th width="245.8245849609375">Description</th><th>Required data type</th><th>Slices</th></tr></thead><tbody><tr><td>include_automatic_filter_keys</td><td>A list of strings containing the automatic filters that are allowed. Filters not on this list will be ignored.</td><td>A list of strings</td><td>All slices</td></tr><tr><td>exclude_automatic_fitler_keys</td><td>A list of strings containing automatic filters to ignore.</td><td>A list of strings</td><td>All slices</td></tr><tr><td>automatic_filters</td><td>A dictionary containing automatic filter keys and values that are</td><td>A dictionary</td><td>All slices</td></tr><tr><td>filter_expression</td><td>One or more expressions that customize what you see in this slice. The expressions must evaluate to a boolean value.</td><td>A string, or a list of strings containing valid boolean expressions</td><td>All slices</td></tr><tr><td>order_by_expression</td><td>One or more expressions that control the display order of data you see in this slice.</td><td>A string or list of strings containing valid expressions.</td><td>All slices</td></tr></tbody></table>

