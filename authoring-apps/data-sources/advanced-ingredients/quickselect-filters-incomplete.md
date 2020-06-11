# Quickselect filters

Quickselect filters \(or just quickselects\) are pre-set filter ranges for a dimension. For example, say your data contains records for an online course that lists `student_name`, `course_name`, and `completion_date`.  You would like users of your app to be able to quickly find all the students that have completed a course within pre-set date ranges, such as `Last 30 days`, `Last 60 days`, and `Year to date`. To do this, you would add quickselects to your `Completion Date` dimension ingredient, like so--

![Advanced ingredient: dimension with quickselects](../../../.gitbook/assets/image%20%2850%29.png)

-- with the following components:

```text
kind: Dimension
field: completion_date
singular: Completion Date
plural: Completion Dates
quickselects:
  - label: 'Last 30 days'
    condition: 'is last 30 days'
  - label: 'Last 60 days'
    condition: 'is last 90 days'
  - label: 'Year to date'
    condition: 'is ytd'
```

Then you would add `Completion Date` to a [filter](../../story-designer/charts/filters.md) slice. 

{% hint style="info" %}
Both bucketed dimensions and quickselects can be used for in filter slices. But quickselects can **only** be used in filter slices, whereas bucketed dimensions can be used in other slices. You would use quickselects instead of buckets if a single data value should be associated with more than one filter option.  For example, if you want filters for ages `18 and older` and `45 and older` , you must use quickselects because some age values \(e.g., 46\) will be associated with both filters. Buckets will not work because each age value can only belong to one bucket.
{% endhint %}



