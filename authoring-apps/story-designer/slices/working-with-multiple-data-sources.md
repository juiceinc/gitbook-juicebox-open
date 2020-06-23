# Multiple data sources

While each slice is limited to ingredients from a single data source, slices within a story do not have to use the same data source. For example, suppose you have two data sources \(A and  B\) and two slices \(1, 2\). The following combinations are all options:

| Slice | Option 1 | Option 2 | Option 3 | Option 4 |
| :--- | :--- | :--- | :--- | :--- |
| Slice 1 | Data Source A | Data Source A | Data Source B | Data Source B |
| Slice 2 | Data Source A | Data Source B | Data Source A | Data Source B |

Notice that options 2 and 3 combine more than one data source. While you _can_ do this, it is generally not recommended because selections in slices using Data Source A will not filter slices using Data Source B, and vice versa. \(In the future, Juicebox will allow filtering across slices with different data sources.\)

