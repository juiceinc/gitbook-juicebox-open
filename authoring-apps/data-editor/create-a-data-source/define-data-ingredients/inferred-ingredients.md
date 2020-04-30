# Inferred Ingredients

Juicebox will create an initial set of ingredients from your loaded data that you can then revise according to your needs. It does this by taking the first \[1000\] records \(i.e., rows\), reviewing the values in each column, and creating an ingredient for each column as follows:

* If the column contains only numeric values \(either integers or floats\), a Measure ingredient will be inferred.
* If the column contains only date values \(formatted like MM/DD/YYYY or YYYY-MM-DD\), a Time ingredient will be inferred.
* If the column contains values other than numeric or date values, a Dimension ingredient will be inferred. 

The name of each inferred ingredient will be the associated column name, with spaces and hyphens converted to underscores. For example, if the column name in your date is `Organization Name`, the ingredient name will be `Organization_Name`.   


