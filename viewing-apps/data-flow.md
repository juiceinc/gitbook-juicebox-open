# Data Flow

Selections made in a story automatically drive how the story progresses in two ways: 

* applying filters \(drilling down\)
* setting direction \(moving across\)

### Selections that apply filters

Selections in a slice will automatically filter downstream slices. This allows users to drill down on the data that is relevant to their problem. 

In the example below, there are two slices. The top slice has a [bar](../authoring-apps/story-designer/charts/ranked-list.md) chart that shows regions ****ranked by **\[Y\]**, and the bottom slice has a [leaderboard](../authoring-apps/story-designer/charts/leaderboard.md) chart that shows which countries lead across multiple measures. Notice that when nothing is selected in the bar chart, the leaderboard shows the leaders across all countries. But when a particular region is selected in the bar chart \(i.e., Western Europe\), the leaderboard only ranks countries within the selected region. 

![Selections in slices above filter slices below](../.gitbook/assets/data_flow_viz.gif)

### Selections that set direction

Selections in [data card](../authoring-apps/story-designer/charts/data-chooser.md) charts determine which direction the story will go.  In the example below, a user can select a measure \(like Happiness or Family\) using the measure chooser ****data card. This selection drives what measure will be used to in the [bar](../authoring-apps/story-designer/charts/ranked-list.md) chart below. 

![Selections in data cards set story direction](../.gitbook/assets/data_flow_dim.gif)



