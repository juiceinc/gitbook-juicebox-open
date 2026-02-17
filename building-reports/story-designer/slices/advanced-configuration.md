---
description: Describe advanced configuration options
---

# Advanced Configuration

{% hint style="danger" %}
Once advanced configuration is set, it can be overwritten but **can not** be removed, even if you remove it from the advanced configuration panel.

To remove all advanced configuration completely, **duplicate** a slice.
{% endhint %}

Some configuration options are not available in the user interface. These can be set by opening the advanced configuration panel. There are two categories of advanced configuration: slice configuration and data configuration.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Opening the configuration panel looks like this.

<figure><img src="../../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

#### Slice configuration options

Here are the available slice configuration options

<table data-full-width="true"><thead><tr><th>Option</th><th width="360.046875">Description</th><th>Required data type</th><th>Slices</th></tr></thead><tbody><tr><td>noDataMessage</td><td>A html message to display when no data has been returned to this slice.</td><td>A string containing valid html.</td><td>All slices</td></tr><tr><td>minSelections</td><td>The minimum number of data selections that must be selected in this slice. These selections will happen automatically. Setting these values in advanced configuration gives you more flexibility than the Selections chooser allows.</td><td>Integer</td><td>All slices</td></tr><tr><td>maxSelections</td><td>The maximum number of data selections possible. Setting these values in advanced configuration gives you more flexibility than the Selections chooser allows.</td><td>Integer</td><td>All slices</td></tr><tr><td>minZoom</td><td>The minimum zoom level that the map can zoom to.</td><td>Integer</td><td>Map</td></tr><tr><td>maxZoom</td><td>The maximum zoom level that the map can zoom to.</td><td>Integer</td><td>Map</td></tr><tr><td>numberOfRows</td><td>The number of rows to show in the leaderboard.</td><td>Integer</td><td>Leaderboard</td></tr><tr><td>includeAppSlugs</td><td>The slugs of apps that a user can link to. Users will only see apps that they have permission to see.</td><td>A list of strings containing valid app slugs.</td><td>Navigator</td></tr><tr><td>invertXAxis</td><td></td><td></td><td></td></tr><tr><td>colorRange</td><td></td><td></td><td></td></tr><tr><td>min_value</td><td></td><td></td><td></td></tr><tr><td>max_value</td><td></td><td></td><td></td></tr><tr><td>x_bounds</td><td></td><td></td><td></td></tr><tr><td>v_lines</td><td></td><td></td><td></td></tr><tr><td>h_lines</td><td></td><td></td><td></td></tr></tbody></table>

#### Data configuration options

Data configuration options affect what data shows up in the slice.&#x20;

<table data-full-width="true"><thead><tr><th>Option</th><th width="359.79833984375">Description</th><th>Required data type</th><th>Slices</th></tr></thead><tbody><tr><td>include_automatic_filter_keys</td><td>A list of strings containing the automatic filters that are allowed. Filters <strong>not on this list</strong> will be ignored.</td><td>A list of strings</td><td>All slices</td></tr><tr><td>exclude_automatic_filter_keys</td><td>A list of strings containing automatic filters to ignore.</td><td>A list of strings</td><td>All slices</td></tr><tr><td>automatic_filters</td><td>A dictionary containing automatic filter keys and values that will be applied to this slice. Using <code>filter_expression</code> is preferred.</td><td>A dictionary</td><td>All slices</td></tr><tr><td>filter_expression</td><td>One or more expressions that customize what you see in this slice. The expressions must evaluate to a boolean value.</td><td>A string, or a list of strings containing valid <strong>boolean</strong> expressions</td><td>All slices</td></tr><tr><td>order_by_expression</td><td>One or more expressions that control the display order of data you see in this slice.</td><td>A string or list of strings containing valid expressions.</td><td>All slices</td></tr><tr><td>cache_region</td><td>Controls how long SQL query results are cached for. Every database connection has a default cache_region that is set by Juicebox support.</td><td>String, must be one of "1-second", "2-hours", "1-day", "1-year"</td><td>All slices</td></tr></tbody></table>

#### Comparison configuration options

The metric chooser slice supports comparisons. The comparison is based on the data shown in the chooser, but this can be adjusted&#x20;

<table data-full-width="true"><thead><tr><th>Option</th><th width="359.79833984375">Description</th><th>Required data type</th><th>Slices</th></tr></thead><tbody><tr><td>comparison_exists</td><td>Ensures a comparison is added even if no other comparison values have been set</td><td>Boolean, true or false</td><td>Chooser</td></tr><tr><td>comparison_label</td><td>What to call the comparison value</td><td>String</td><td>Chooser</td></tr><tr><td>comparison_metrics</td><td>A list of values OR a list of metric ids to display as the comparison. The list must be the same length as the number of metrics in the chooser. The lists will be matched to the metrics in the chooser.</td><td>A list of numbers OR a list of strings that are metric ids.</td><td>Chooser</td></tr><tr><td>comparison_apply_automatic_filters</td><td>Should automatic filtering from slices above be applied to this comparison.</td><td>Boolean, true or false</td><td>Chooser</td></tr><tr><td>comparison_exclude_automatic_filter_keys</td><td>A list of strings containing the automatic filters that are allowed. Filters <strong>on this list</strong> will be ignored.</td><td>A list of strings</td><td>Chooser</td></tr><tr><td>comparison_include_automatic_filter_keys</td><td>A list of strings containing the automatic filters that are allowed. </td><td>A list of strings</td><td>Chooser</td></tr><tr><td>comparison_filter_expression</td><td>One or more expressions that customize what you see in this slice. The expressions must evaluate to a boolean value.</td><td>A string, or a list of strings containing valid boolean expressions</td><td>Chooser</td></tr><tr><td>comparison_cache_region</td><td>Controls how long SQL query results are cached for. Every database connection has a default cache_region that is set by Juicebox support.</td><td>String, must be one of "1-second", "2-hours", "1-day", "1-year"</td><td>All slices</td></tr></tbody></table>





