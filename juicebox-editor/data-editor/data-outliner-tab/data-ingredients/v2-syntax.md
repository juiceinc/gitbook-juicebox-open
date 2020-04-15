# V2 Syntax



```text
_version: "2"
state:
    kind: Dimension
    field: state
    lookup:
        Vermont: "The Green Mountain State"
        Tennessee: "The Volunteer State"
    quickselects:
        - name: younger
          condition: "age<40"
        - name: vermontier
          condition: "state='Vermont'"
pop2000:
    kind: Metric
    field: "if(age > 40, pop2000)"
pop2008:
    kind: Metric
    field: pop2008
allthemath:
    kind: Metric
    field: pop2000+pop2008   - pop2000 * pop2008 / @pop2000
```

* Field is defined as a string that contains math, potential aggregations, and conditions. An `if(cond1, value1, cond2, value2)` syntax supports conditions.
* Dimension buckets are supported. These will get transformed into an appropriate`if(cond1, value1, cond2, value2)` expression with an extra order\_by\_field to support the original ordering.
* Referencing other dimensions or metrics is supported using the "@" syntax.

```text
# a basic summing metric

active:
  kind: Metric
  field: sum(active)
  singular: 'Active Cases'
  plural: 'Active Cases'
  format: ',0f'
```

```text
# a conditional metric. If the column is a datetype (like last_update) 
# you can use readable syntax to check dates

previous_active:
  kind: Metric
  field: 'if(last_update = "two days ago", active)'
  singular: 'Active'
  plural: 'Active'
  format: ',0f'
```

```text
# recovered_change references existing metrics 
# @current_recovered and @previous_recovered to calculate change

recovered_change:
  kind: Metric
  field: 'sum(@current_recovered) - sum(@previous_recovered)'
  singular: 'Change in Deaths'
  plural: 'Change in Deaths'
  format: '"+",0f; ,0f'
```

