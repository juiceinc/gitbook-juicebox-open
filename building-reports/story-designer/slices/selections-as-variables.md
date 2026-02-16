---
description: Slice selections don't always have to filter down the page
---

# Selections as Variables

By default, selections in a slice filter the data in downstream slices. You can change this default behavior by configuring slice selections.

You can configure the slice selections to act as:

1. **Filters**. Slice selections will filter downstream slices. (This is the default configuration.)
2. **Variables**. Slice selections will not filter downstream slices but will be available for use in defining ingredients.&#x20;
3. **Filters and Variables**. Slices selections will filter downstream slices and be available for use in defining ingredients.&#x20;

<div data-full-width="false"><figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure></div>

## Finding Available Variables <a href="#variables-use-the-id-of-the-dimension-that-the-slice-is-showing" id="variables-use-the-id-of-the-dimension-that-the-slice-is-showing"></a>

To see what variables are available to a slice, open the Debug panel, select the slice, and click on the **Variables** tab. This shows you:

* The variable names you can reference in formulas
* The current selected values
* The structure of the data (especially important for date ranges)

<figure><img src="../../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

When a slice is configured to use selections as "Variables" or "Filters and Variables", you'll see selected values here. If the Variables tab shows `{}`, it means either:

* The slice isn't filtered to use selections as variables, or&#x20;
* Nothing has been selected yet

## Using Variables

Variables are most useful when you need to reference selections within your ingredient definitions rather than relying on automatic filtering. A common use case is comparing data across two different time periods.&#x20;

### Example: Comparing Sales Across Quarters

Let's say you want to compare sales between two quarters that users can select. You can't accomplish this with regular filtering because you need to reference both quarters simultaneously.&#x20;

**Setup**:

1. Create two dimension ingredients, both with the field definition `quarter`:
   1. Label the first "Baseline Quarter"
   2. Label the second "Comparison Quarter"
2. Create slice(s) to display these dimensions. For example, two Tables slices (one for each dimension)
3. Configure each Table slice to require a selection ("Select one required") and to use selections as "Variables"

{% hint style="warning" %}
**Important:** For this comparison example, you must use "Variables" only, not "Filters and Variables". If you used "Filters and Variables", selecting a baseline quarter would filter the data and prevent you from seeing other quarters in the comparison selection. Variables-only mode keeps the selections independent.
{% endhint %}

4. Add a Chooser slice after the second Table slice and open the Debug panel for the Chooser slice. Navigate to the Variables tab in the Debug panel. You'll see something like:

```
{
  ...
  "baseline_quarter": "2023 Q1",
  "comparison_quarter": "2023 Q4",
  ...
}
```

The variable names (like `baseline_quarter` and `comparison_quarter`) are the ingredient IDs that Juicebox generates. You'll use the ingredient IDs when using variables in your measure formulas.

{% hint style="info" %}
**Note:** Your actual ingredient IDs will look different (e.g., `quarter_gqo74qoi`) but for this example we'll use `baseline_quarter` and `comparison_quarter` for clarity.
{% endhint %}

5. Create new Sales Delta and Sales % Change measures and add them to the Chooser slice.

#### Creating the Sales Delta Measure

Create a new measure ingredient with this field definition:

```
sum(if(quarter = "{{comparison_quarter}}", sales, 0)) 
- sum(if(quarter = "{{baseline_quarter}}", sales, 0))
```

This formula:

* Calculates sales for the comparison quarter
* Subtracts sales for the baseline quarter
* Returns the absolute change in sales

**Optional:** Add a dynamic label to make it clearer:

```
Change from {{baseline_quarter}} to {{comparison_quarter}}
```

#### Creating the Sales % Change Measure

Create another measure to calculate the percent change:

```
(sum(if(quarter = "{{comparison_quarter}}", sales, 0)) - 
sum(if(quarter = "{{baseline_quarter}}", sales, 0))) / 
sum(if(quarter = "{{baseline_quarter}}", sales, 0))
```

With a dynamic label:

```
% Change from {{baseline_quarter}} to {{comparison_quarter}}
```

{% hint style="success" %}
**Tip:** You don't need to wrap the division in `safe_divide()` - Juicebox automatically handles division by zero for you.
{% endhint %}

{% hint style="info" %}
**Note:** In this example, we configured the slices to require selections, so the formulas will always have values to work with. If you're using variables in a scenario where selections might be empty (optional filters), you'll need to handle empty states using the `default()` function - see the section on handling empty selection states below.
{% endhint %}

### Range Variables

Range selections (date ranges, number ranges) return an array with two elements: a start value and an end value. You can access these using array indexing:

**Basic syntax (when you know a range will always be selected):**

```
sum(if(joined_date BETWEEN 
  date("{{campaign_date__between_raw[0]['id']}}") AND 
  date("{{campaign_date__between_raw[1]['id']}}"), 
  revenue))
```

* `[0]` gets the start value
* `[1]` gets the end value
* `['id']` extracts the value
* `date()` wraps the value to ensure proper date type conversion (for date ranges)

### Handling Empty Selection States

If a selection might be empty, your formula will break when trying to reference an undefined variable. Use the `default()` function to provide fallback values:

**For string variables:**

```
sum(if(category = "{{category_filter|default('All')}}", sales, 0))
```

**For range variables (date ranges, number ranges):**

```
sum(if(joined_date BETWEEN 
  date("{{(campaign_date__between_raw|default([{'id':'1970-01-01'}], true)|first).id}}") AND 
  date("{{(campaign_date__between_raw|default([{'id':'2099-12-31'}], true)|last).id}}"), 
  revenue))
```

Breaking down the range syntax:

* `campaign_date__between_raw` - the base variable name
* `|default([{'id':'1970-01-01'}], true)` - provides a fallback value if nothing is selected
* `|first` - gets the start value (similar to `[0]`, but works within the filter chain)
* `|last` - gets the end value (similar to `[1]`, but works within the filter chain)
* `.id` - extracts the value
* `date()` - converts to proper date type (for date ranges)

{% hint style="info" %}
**Why use `|first` and `|last` instead of `[0]` and `[1]`?**\
When you use the `default()` function, you're using Jinja template syntax (the `|` pipe operator chains operations together). Within this syntax, you need to use `|first` and `|last` instead of array indexing. If you're NOT using `default()`, you can use the simpler `[0]` and `[1]` syntax.
{% endhint %}

### Limitations

* For multi-select slices, the variable contains only the **first** selected value. If multiple values are selected, only the first will be available in the variable.
* You can use variables in ingredient formulas, labels, and many other places throughout Juicebox. However, variable support isn't available everywhere yet. If you need variables in a location that's not currently supported, please [let us know](../../../getting-started/reach-out-to-us.md)!
