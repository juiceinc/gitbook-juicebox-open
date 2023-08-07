---
description: Juicebox apps have integrated data permissions.
---

# Limiting what data users can see

{% hint style="warning" %}
Data permissions are only available for Juice Design+ clients with a billing plan that allows user filters.
{% endhint %}

**Data permissions objects** create filters that are applied to every database query. If the database table does not contain the column or ingredient referenced, the data permission will be ignored.

Data permission objects reference ingredients which are named expressions that can use more than one database column. Data permission objects will soon be able to reference raw table columns by surrounding the column name with square bracket.

* `ingredient: [list of values]` Show only rows where the ingredient expression evaluates to one of the list of values.

{% hint style="info" %}
Soon, Juicebox will also support acccessing raw column values like this

`[column]: [list of values]`Show only rows where the database column is in the list of values.
{% endhint %}

For all the following examples an `[column]` can be used in any place where an `ingredient`is used.

* `ingredient__notin: [list of values]` Show only rows where the ingredient expression does not contain a value in the list of values.
* `ingredient__eq: value` Show only rows where the ingredient expression is equal to a value.
* `ingredient__ne: value` Show only rows where the ingredient expression is not equal to a value.
* `ingredient__like: value` Show only rows where the ingredient expression is like the value expression. Use `%` to represent wildcards.
* `ingredient__gt: value` Show only rows where the ingredient expression is greater than a value.
  * You can use `lt`, `lte`, `gt` and `gte` for less than, less than or equal, greater than or greater than or equal respectively.
* `ingredient__between: [value1, value2]` Show only rows where the ingredient expression is between value1 and value2

### Examples of data permissions

```jsx
{ 
  "state": ["New Hampshire", "Vermont", "Maine", "Massachusetts"], 
  "age__gt": 30 
}
```

This user can only see rows where the state ingredient is in the list of four states AND the age ingredient is greater than 30.

```jsx
{
  "[Student Name]": "Maria Hill",
  "[Organization]": 101
}
```

This user can see rows where the database table contains a column named “Student Name” which is equal to “Maria Hill” and the column named “Organization” is equal to 101.

### Making data permissions affect all apps

```jsx
{
   automatic_filters: {Data Permission Object}
}
```

### Making data permissions that affect individual apps

```jsx
{
   app_filters: {
     {app_slug}: {Data Permission Object}
     {app_slug2}: {Data Permission Object}
   }
}
```

