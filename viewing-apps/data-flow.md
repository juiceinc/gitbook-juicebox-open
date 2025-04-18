# Focus and Filter

Selections made in a story automatically drive how the story progresses in two ways:&#x20;

* focusing
* filtering

### Selections that focus

Selections in [chooser](../building-reports/story-designer/slices/charts/data-card.md) charts let you focus in on a particular thing. In the example below, a user can select a measure (like Happiness or Family) using the measure chooser. The [bar](../building-reports/story-designer/slices/charts/bar.md) chart below shows  only the selected measure.

![Selections in choosers let the user focus in on a particular measure](../.gitbook/assets/data_flow_dim.gif)

### Selections that filter

Selections in a slice will automatically filter downstream slices. This allows users to drill down on the data that is relevant to their problem.&#x20;

In the example below, there are two slices. The top slice has a [bar](../building-reports/story-designer/slices/charts/bar.md) chart that shows regions ranked by a Happiness measure, and the bottom slice has a [leaderboard](../building-reports/story-designer/slices/charts/leaderboard.md) chart that shows which countries lead across multiple measures. Notice that when nothing is selected in the bar chart, the leaderboard shows the leaders across all countries. But when a particular region is selected in the bar chart (i.e., Western Europe), the leaderboard only ranks countries within the selected region.&#x20;

![Selections in slices above filter slices below](../.gitbook/assets/data_flow_viz.gif)

