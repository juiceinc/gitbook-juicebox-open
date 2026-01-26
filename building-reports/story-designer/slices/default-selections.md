# Default Selections

You can configure slices to have default selections that are automatically applied when users first open your report. Default selections can be set on any slice type that allows selections, including Filter, Bar, Trend, Leaderboard, and other chart slices.

This is useful for:

* Setting a default date range so users immediately see relevant recent data
* Pre-selecting common filter values to reduce clicks for your audience
* Guiding users to start with a recommended view of the data
* Improving query performance by limiting the initial data scope

{% hint style="info" %}
**Performance tip:** Default selections can significantly improve report load times. When a report opens without any filters applied, queries may need to scan your entire dataset. By setting sensible defaults (like "last 30 days" for date filters), you reduce the data volume and speed up the initial load. This is especially important for large datasets—queries that take longer than 60 seconds will timeout, and even queries over 5 seconds can feel sluggish to users.
{% endhint %}

## **Date Selections**

#### **Rolling Date Ranges**

For date-based filters, you can set either a **rolling date range** or a **fixed date range** as the default.

**Rolling date ranges** automatically update each day, so "last 30 days" always shows the most recent 30-day window:

| Option   | Description                                          |
| -------- | ---------------------------------------------------- |
| `last30` | Rolling last 30 days from today                      |
| `last90` | Rolling last 90 days from today                      |
| `mtd`    | Month to date (first of current month through today) |
| `ytd`    | Year to date (January 1 through today)               |

**Configuration syntax:**

```yaml
config:
  selectionPolicy:
    SentDate:
      defaultSelections: last30
```

{% hint style="info" %}
Note: Replace `SentDate` with your ingredient ID.&#x20;
{% endhint %}

#### **Fixed Date Ranges**

**Fixed date ranges** use specific start and end dates that don't change over time. This is useful when you want users to always start with a specific historical period (e.g., a particular fiscal year or campaign period).

**Configuration syntax:**

```yaml
config:
  selectionPolicy:
    Year:
      defaultSelections:
        min: "2020-01-01"
        max: "2024-01-01"
```

{% hint style="info" %}
Note: Date values must be in `"YYYY-MM-DD"` format and enclosed in quotes.
{% endhint %}

## **Number Selections**

#### **Number Ranges**

For number-based range filters (such as age ranges, price ranges, or score ranges), you can set a default min and max value. This works similarly to fixed date ranges.

**Configuration syntax:**

```yaml
config:
  selectionPolicy:
    Age:
      defaultSelections:
        min: 18
        max: 65
```

## **Text Selections**

#### **Single Value**

For text dimensions (such as regions, categories, products, or status values), you can set a specific value as the default selection.

**Configuration syntax:**

```yaml
config:
  selectionPolicy:
    Status:
      defaultSelections:
        - Active
```

#### Multiple Values

You can also default to multiple values for a text filter.

**Configuration syntax:**

```yaml
config:
  selectionPolicy:
    State:
      defaultSelections:
        - Georgia
        - Connecticut
```

## **How to Request Default Selections**

Default selections are currently configured by Juice Analytics staff through custom configurations. Soon all editors will have access to apply custom configurations. In addition, we will soon have new UI options that allow editors to set default selections without using custom configurations.&#x20;

In the meantime, follow these steps to request a default selection for your report:

1. Identify which slice(s) need default selections
2. Determine what default value(s) you want:
   * For dates: specify which rolling option (`last30`, `last90`, `mtd`, or `ytd`)
   * For other dimensions: specify the exact value(s) to pre-select
3. Contact Juice Analytics support at [**help@myjuicebox.io**](mailto:help@myjuicebox.io) with your request

Include the following in your request:

* The report name and URL
* The slice slug (e.g., `Filters1`, visible in the editing panel)
* The ingredient/field name
* The default value(s) you want applied
