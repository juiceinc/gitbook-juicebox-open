# Data Ingredients

The Data Ingredients section of the Data Outliner defines the measures and dimensions that you will use to create your visualizations. \(For now, the data ingredients are expressed in yaml, but a more user-friendly interface will be coming soon!\) 

When your data is loaded, JBO will create an initial set of ingredients based on some assumptions. If a field is numeric, JBO will create a measure for that field using the sum aggregation. If a field is text, JBO will create a dimension for that field. These will give an initial set of ingredients that you can then revise according to your needs.

