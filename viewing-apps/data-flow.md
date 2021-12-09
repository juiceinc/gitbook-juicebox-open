# Understanding Data Flow

Selections made in a story automatically drive how the story progresses in two ways:&#x20;

* applying filters (drilling down)
* setting direction

### Selections that apply filters

Selections in a slice will automatically filter downstream slices. This allows users to drill down on the data that is relevant to their problem.&#x20;

In the example below, there are two slices. The top slice has a [bar](../editing-apps/story-designer/charts/bar.md) chart that shows regions **** ranked by **** a Happiness measure, and the bottom slice has a [leaderboard](../editing-apps/story-designer/charts/leaderboard.md) chart that shows which countries lead across multiple measures. Notice that when nothing is selected in the bar chart, the leaderboard shows the leaders across all countries. But when a particular region is selected in the bar chart (i.e., Western Europe), the leaderboard only ranks countries within the selected region.&#x20;

![Selections in slices above filter slices below](../.gitbook/assets/data\_flow\_viz.gif)

### Selections that set direction

Selections in [chooser](../editing-apps/story-designer/charts/data-card.md) charts determine which direction the story will go.  In the example below, a user can select a measure (like Happiness or Family) using the measure chooser. This selection drives what measure will be used to in the [bar](../editing-apps/story-designer/charts/bar.md) chart below.&#x20;

![Selections in data cards set story direction](../.gitbook/assets/data\_flow\_dim.gif)

