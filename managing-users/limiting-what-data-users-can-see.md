---
description: Juicebox apps have integrated data permissions.
---

# Limiting what data users can see

**Data permissions** create filters that are applied to every database query. If the database table does not contain the column or ingredient referenced, the data permission is ignored.

Data permission objects can reference **ingredients** by their ID or **raw database columns** (by wrapping the column name in square brackets). You can find an ingredient's ID by opening the ingredient in the ingredient editor and clicking **Copy ID** at the bottom.

#### Syntax

| Syntax                    | Example                            | Description                        |
| ------------------------- | ---------------------------------- | ---------------------------------- |
| `ingredient_id: [values]` | `"state": ["NH", "VT"]`            | Filter using an ingredient         |
| `[column]: [values]`      | `"[Student Name]": ["Maria Hill"]` | Filter using a raw database column |

Anywhere an `ingredient_id` is used below, you can substitute `[column]` to reference a raw database column instead.

#### Filter operators

| Operator                 | Example                    | Description                                |
| ------------------------ | -------------------------- | ------------------------------------------ |
| `ingredient_id`          | `"state": ["NH", "VT"]`    | Values must be in the list                 |
| `ingredient_id__notin`   | `"state__notin": ["CA"]`   | Values must NOT be in the list             |
| `ingredient_id__eq`      | `"age__eq": 30`            | Must equal the value                       |
| `ingredient_id__ne`      | `"status__ne": "inactive"` | Must not equal the value                   |
| `ingredient_id__like`    | `"name__like": "Jo%"`      | Must match the pattern (`%` is a wildcard) |
| `ingredient_id__gt`      | `"age__gt": 30`            | Greater than                               |
| `ingredient_id__gte`     | `"age__gte": 30`           | Greater than or equal                      |
| `ingredient_id__lt`      | `"age__lt": 65`            | Less than                                  |
| `ingredient_id__lte`     | `"age__lte": 65`           | Less than or equal                         |
| `ingredient_id__between` | `"age__between": [18, 65]` | Between two values (inclusive)             |

#### How multiple filters combine

When you include multiple keys in a single data permission object, they are combined with **AND** logic. Values within a single key use **OR** logic.

```json
{
  "state": ["California", "New York"],
  "status": ["active"]
}
```

This means: (state is California OR New York) AND (status is active). A row is only visible if it matches at least one value for **every** key.

This works well when keys are independent. But sometimes you need to grant access to specific **combinations** of values across dimensions — for example, a user who should see Horror films by certain directors, but all Action films regardless of director. For this, use compound filters.

**Compound filters**

Compound filters let you define a set of valid combinations that are OR'd together. To create one, join the key names with commas and provide a list of value groups:

```json
{
  "genre,director": [
    ["Horror", ["Mike Flanagan", "Ole Bornedal"]],
    ["Action"],
    ["Comedy", ["Adam Carolla", "Bonnie Hunt"]]
  ]
}
```

This generates:

```
(genre = 'Horror' AND director IN ('Mike Flanagan','Ole Bornedal'))
OR (genre = 'Action')
OR (genre = 'Comedy' AND director IN ('Adam Carolla','Bonnie Hunt'))
```

Each item in the outer list is a **combination** (OR'd together). Within a combination, values are matched to keys by position. A single value becomes an equality check; a list becomes an IN clause. If a combination has fewer values than keys, the extra keys are simply not applied to that combination.

Compound filters also support operators on the last key. For example, `"state,age__gte"` would apply the `>=` operator to the age values.

{% hint style="info" %}
Compound filters with a large number of combinations can generate very large SQL queries. Use them when you need OR logic across dimensions, but be mindful of scale.
{% endhint %}

#### Scoping data permissions

Data permissions can be scoped at three levels. When multiple levels are present, they are all applied together (AND logic).

**All apps: `automatic_filters`**

Wrap data permissions in `automatic_filters` to apply them across all apps the user can access:

```json
{
  "automatic_filters": {
    "[region]": ["Northeast", "Southeast"],
    "status": ["active"]
  }
}
```

**Specific apps: `app_filters`**

Use `app_filters` to apply different data permissions per app. Each key is an app slug:

```json
{
  "app_filters": {
    "sales_dashboard": {
      "[region]": ["Northeast"]
    },
    "hr_report": {
      "[department]": ["Engineering", "Design"]
    }
  }
}
```

**Specific data sources: `datasource_filters`**

Use `datasource_filters` to apply data permissions to a specific data source. Each key is a data source name or ID:

```json
{
  "datasource_filters": {
    "student_records": {
      "[school_id]": ["lincoln_elem"]
    }
  }
}
```

**Combining scopes**

You can combine all three scopes. For example, the following applies a global region filter to all apps, plus an additional department filter only on the HR report:

```json
{
  "automatic_filters": {
    "[region]": ["Northeast"]
  },
  "app_filters": {
    "hr_report": {
      "[department]": ["Engineering", "Design"]
    }
  }
}
```

When viewing the HR report, this user would see only rows where the region is "Northeast" AND the department is "Engineering" or "Design." When viewing other apps, only the region filter applies.

#### Where data permissions are set

Data permissions can be set in two places:

* **On a user account** — via the People page or the Users API. These apply whenever the user views any app.
* **On an access view** — via the Access Views API. These apply only when the app is loaded through that access view.

If an access view has data permissions, they **override** the user account's data permissions entirely (they do not merge). If the access view has no data permissions, the user account's data permissions apply.

See [Embedding with access views](embedding-juicebox-apps/embedding-with-access-views.md) for how data permissions work in the context of embedding.
