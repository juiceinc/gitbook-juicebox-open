# Preparing your data

Data preparation is tedious and time-consuming. We get it. But unless the data is properly prepared, your app building process is likely to be frustrating and unsuccessful. Time spent preparing your data will be worth it.

## What does properly prepared data look like?

* Organized. Data values are organized in columns and rows in a single table. No merged cells, and no titles or notes that span multiple columns. 
* Complete. All the values you need are in the data. 
* Consistent. Data in a column should be of the same type. Number columns should contain only numbers. Date columns should contain only dates. 
* Clean. Number formatting, leading and trailing spaces, carriage returns, and other weird values \(e.g., "\#N/A" and "\#ERROR"\) are removed. 
* Column headers. The first row of your data should be your column header row. Column names should have letters, spaces, or underscores, and nothing else. 

![An example of properly prepared data](../../.gitbook/assets/image%20%28127%29.png)

## Let's take it step-by-step

Your goal here is a single sheet containing all data organized into columns and rows, with the first row containing the column headers and each column containing values of the correct data type. 

### 1. Review and understand your data

Interrogate your data early on. Do you know what the column headings mean? Do the values in the columns make sense? Are there any columns you need that are missing? If the data is not quite right, fix it before going to the next step. 

### 2. Make a working copy of your data

As you are preparing your data, you may need to refer or revert to the original state of data. Therefore, it is **very important** that you make a working copy of your data and only make changes to the working copy.

### 3. Un-merge cells

Values should not span multiple columns or rows. Un-merge any merged cells.

### 4. Remove extra rows and sheets

Remove any rows above your column header row. Remove any other rows that do not contain data organized into columns \(e.g., footnotes\). If there are any sheets other than the one with your data, remove those. 

### 5. Remove columns you don't need \(optional\)

Columns you don't need can be distracting during data preparation and app building, so it's a good idea to just remove them. \(If you're not sure whether you need a particular column, just leave it in.\)

### 6. Add a numeric column to your data \(if you don't already have one\)

At this time, your data upload will fail if you don't have at least one numeric column in your data. Therefore, if your data does not already have at least one column with numeric data only \(i.e., numbers, with or without decimals, or NULL\), you will need to add one. The numeric data doesn't need to be meaningful. For example, adding a column of all 1s will do the trick.

### 7. Remove rows you don't need

Sometimes your data will contain rows you don't need. For example, let's say your data contains values broken out by state as well as values for the US. Because you can aggregate the state-level values to get the US values, you do not need the US records. Removing unneeded rows will simplify your ingredient definitions later on. 

### 8. Revise column names as needed

Your column names should be readable, brief, and contain only letters, spaces, and underscores. For example, if the column name is `Student.First.Last.Name`, you could change it to `Student Name`; if the column name is `Revenue (per Proposal)`, you could change it to `Revenue per proposal`.  Your column names will be used as labels in the ingredients you [add automagically](../data-sources/adding-ingredients/#adding-ingredients-automagically), so better column names mean less work for you when defining ingredients. 

### 9. Remove number formatting

Any column with numeric data should be free of formatting that adds thousands separators, $, %, USD, EUR, etc. You should just have numbers, either with or without decimals. A period `.` should be used as the decimal separator. Negative numbers should be indicated by a `-` before the number, e.g., `-2567.4`. 

### 10. Confirm numeric columns contain only numeric data \(or nulls\)

Numeric columns should only contain numbers or nulls. Anything else will prevent you from using the column in measures that use sum\(\), avg\(\), min\(\), or max\(\) aggregation functions. You'll want to remove things like spaces, "--", "N/A", "\#N/A", "NULL", and "\#ERROR". While true nulls \(i.e., empty cells\) are ok, words like "null" or "blank" are not. A period `.` should be used as the decimal separator. Negative numbers should be indicated by a `-` before the number, e.g., `-2567.4`. 

### 11. Confirm date columns contain only dates with date formatting \(or nulls\)

Date columns should only contain dates or nulls. Dates should be formatted like MM-DD-YYYY, MM/DD/YYYY, or YYYY-MM-DD. While true nulls \(i.e., empty cells\) are ok, words like "null" or "blank" are not.

### 12. Add latitude and longitude

If you want to use the [map](../story-designer/charts/map.md) slice, you will need to have latitude and longitude columns in your data. If you need to add them, we recommend using [this process in Google Sheets](https://discourse.looker.com/t/get-latitude-longitude-for-any-location-through-google-sheets-and-plot-these-in-looker/5402). 

### 13. Do a final check

You're almost there! Do a final check to make everything looks ok. Should null values be null? Do values contain carriage returns, leading or trailing spaces, or anything else odd? The `TRIM()` function is useful for dealing with large numbers of leading and trailing spaces.

### 14. Download your data as a CSV file

Download your prepared data as a CSV file, with commas `,` separating the values. Give it a meaningful but brief name and save it in a location you can easily find.

Congratulations! You're now ready to [add a data source](../data-sources/loading-data.md).

