# The measure ingredient editor

## The measure ingredient editor

### Header

Icon

Label (this is the same as the Label under Basics).&#x20;

Data table

Menu

* Duplicate
* Duplicate as Advanced
* Copy ingredient ID
* Delete

### Basics

Field formula

Label

**Number format**. Select how values should be formatted from the dropdown, or enter a custom [number format](../ingredient-formats.md).&#x20;

Date format. (For min(date) or max(date))

### Styling

Description

Color

Color when negative

Image url

### Advanced

Filter

**Reverse**. By default in the [Leaderboard](../../slices/charts/leaderboard.md), higher numbers are deemed "better." To flip this for a particular measure, turn on **Reverse**.&#x20;

**Ranges**. To show [Measure Chooser](../../slices/charts/data-card.md#chooser-chart-with-measures) or [Card](../../slices/charts/card.md) gauges or to colorize measure cells in a [Table](../../slices/charts/table.md), ranges will need to be defined. Here's an example of ranges defined for a **Sales** measure:

```yaml
- color: "#ee6055"
  label: Below
  endValue: 4000000
  startValue: 0
- color: "#eaf4f4"
  label: On Target
  endValue: 5500000
- color: "#60d394"
  label: Above
  endValue: 20000000
```

In this example, there are three ranges: "Below", "On Target", and "Above". Each range is represented by a different color using hex codes and has a specific start and end value. The "Below" range starts at 0 and ends at 4 million, the "On Target" range ends at 5.5 million, and the "Above" range ends at 20 million.
