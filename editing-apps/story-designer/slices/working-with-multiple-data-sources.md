# Multiple data sources

While each slice is limited to ingredients from a single data source, slices within a story do not have to use the same data source. 

While you _can_ do this, you should know that selections in slices using different data sources will **only filter for simple ingredients that are defined using fields that have the same name**.

Here's an example: Imagine you have a first data source uses a csv that contains a column named `state`. Let's say this column contains United States state name abbreviations. If you have another data source that also has a column named state that contains matching US state name abbreviations then selections of these states will filter the other data source.

{% hint style="info" %}
In the future, Juicebox will support more extensive filtering across slices with different data sources.
{% endhint %}

