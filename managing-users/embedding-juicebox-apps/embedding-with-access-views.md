---
description: >-
  Use the Juicebox API to create access views that embed apps with per-user
  data   permissions.
---

# Embedding with access views

An **access view** is a URL generated through the Juicebox API that gives a user access to a specific app with specific settings — without requiring them to sign in to Juicebox. Access views are designed to be embedded in iframes on your website.

With access views, you can control what data each user sees (data permissions), what selections are pre-set, whether the Juicebox header and footer are visible, and how many times the link can be used.

### How it works

1. Authenticate with the Juicebox API using a client admin account to get a Bearer token.
2. Create an access view by POSTing to the API with the app slug, user email, and any desired settings (data permissions, selections, display options).
3. The API returns an access view object that includes a `url` field.
4. Load that URL in an iframe on your page.

Each access view URL is typically short-lived and limited-use. You generate a fresh one each time a user needs to see the app.

### Step 1: Authenticate

The Juicebox API uses JWT Bearer token authentication. You'll need a Juicebox user account with the **Admin** role that is set up for password login. To get a token, POST those credentials to the auth endpoint:

```
POST https://your-workspace.myjuicebox.io/api/v2/auth/
Content-Type: application/json

{
  "username": "your-admin@example.com",
  "password": "your-password"
}
```

The response includes a `token` field. Use this token in subsequent requests:

```
Authorization: Bearer <token>
```

{% hint style="info" %}
Here's how to [set a password for API access](../adding-users.md#setting-up-a-password-for-api-access). If you need help setting up an Admin account for API access, [reach out to us](../../getting-started/reach-out-to-us.md).
{% endhint %}

Tokens expire after a period of time. You can refresh a token by POSTing to `/api/v2/auth/refresh/` with the current token, or verify a token with `/api/v2/auth/verify/`.

### Step 2: Create an access view

To create an access view, POST to the access views endpoint:

```
POST https://your-workspace.myjuicebox.io/api/v2/accessviews/
Authorization: Bearer <token>
Content-Type: application/json

{
  "app_slug": "my_app",
  "user_email": "viewer@example.com",
  "data_permissions": {
    "automatic_filters": {
      "[region]": ["Northeast", "Southeast"]
    }
  },
  "selections": {
    "Filters1:region": ["Northeast"],
    "Filters1:year": ["2025"]
  },
  "allowed_uses_cnt": 1,
  "show_header": false,
  "show_footer": false
}
```

The only always-required field is `app_slug`. The `user_email` field is required if the app's access is set to "Sign-in required." All other fields are optional.

#### Access view fields

| Field              | Type     | Description                                                                                                                                               |
| ------------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `app_slug`         | string   | **Required.** The slug of the app to display.                                                                                                             |
| `user_email`       | string   | The email address of an existing Juicebox user who will view the app. Required if the app's access is set to "Sign-in required."                          |
| `data_permissions` | object   | Restricts what data the viewer can see. See [Data permissions](embedding-with-access-views.md#data-permissions) below.                                    |
| `selections`       | object   | Pre-sets filter selections in the app. Keys use the format s`lice_slug:ingredient_id`. See [Selections](embedding-with-access-views.md#selections) below. |
| `show_header`      | boolean  | Whether to show the Juicebox app header. Default: `true`.                                                                                                 |
| `show_footer`      | boolean  | Whether to show the Juicebox app footer. Default: `true`.                                                                                                 |
| `allowed_uses_cnt` | integer  | How many times the URL can be loaded. `0` = unlimited. Default: `0`.                                                                                      |
| `expires_at`       | datetime | When the access view expires (ISO 8601 format). `null` = no expiration.                                                                                   |
| `is_active`        | boolean  | Whether the access view can be used. Default: `true`.                                                                                                     |
| `stack_slug`       | string   | An optional stack slug. If set, the app opens to this specific stack / page.                                                                              |

#### Data permissions

Data permissions control what rows of data the viewer can see. They work by applying filters to every database query the app makes. Here's a brief example:

```json
{
  "data_permissions": {
    "automatic_filters": {
      "[region]": ["Northeast", "Southeast"],
      "[status]": ["active"]
    }
  }
}
```

In this example, the viewer only sees rows where the `region` column is "Northeast" or "Southeast" AND the `status` column is "active."

For full details on data permission syntax — including ingredient vs. raw column references, filter operators, and per-app permissions — see [Limiting what data users can see](../limiting-what-data-users-can-see.md).

If the access view includes `data_permissions`, they **override** the user account's data permissions entirely (they do not merge). If the access view has no `data_permissions`, the user account's data permissions apply.

#### Selections

Selections pre-set the filter state of the app when it loads. Each key in the selections object uses the format `slice_slug:ingredient_id`, where `slice_slug` is the slug of the slice (e.g., Filters1) and `ingredient_id` is the id of the ingredient being filtered. The value is a list of selected values.

```json
{
  "selections": {
    "Filters1:region": ["Northeast", "Southeast"],
    "Filters1:year": ["2025"]
  }
}
```

In this example, the app opens with two filters pre-set on the `Filters1` slice: `region` set to "Northeast" and "Southeast", and `year` set to "2025".

{% hint style="info" %}
Selections determine what the user initially _sees_ in the app's filters. Data permissions determine what data is _available_. A user can change their selections, but they can never see data outside their data permissions.
{% endhint %}

#### Shortcut: one-time-use access views

If you just need a quick, one-time-use access view without custom data permissions or selections, you can use the shortcut endpoint:

```
GET https://your-workspace.myjuicebox.io/api/v2/embed/{app_slug}/{user_email}/
Authorization: Bearer <token>
```

This creates an access view with `allowed_uses_cnt: 1` that expires after 60 seconds. It's equivalent to POSTing to the access views endpoint with minimal settings.

### Step 3: Get the response

The response includes the same fields plus several read-only fields:

```json
{
  "key": "abc123def456",
  "url": "https://your-workspace.myjuicebox.io/a/my_app/view/abc123def456/",
  "app_slug": "my_app",
  "user_email": "viewer@example.com",
  "data_permissions": { ... },
  "selections": { ... },
  "show_header": false,
  "show_footer": false,
  "allowed_uses_cnt": 1,
  "usages_cnt": 0,
  "expires_at": null,
  "created": "2026-01-15T10:30:00Z",
  "modified": "2026-01-15T10:30:00Z",
  "is_active": true
}
```

The `url` field is what you embed in your iframe.

### Step 4: Embed the \`url\` in an iframe

Take the `url` from the access view response and load it in an iframe:

```html
<iframe
  src="https://your-workspace.myjuicebox.io/a/my_app/view/abc123def456/"
  width="100%"
  height="800"
  frameborder="0"
></iframe>
```

Since access view URLs are typically short-lived, you should generate a new access view each time a user loads your page and inject the URL into the iframe `src` dynamically.

### Putting it all together

In production, your backend handles the API calls and injects the access view URL into the page dynamically. Here's a complete example using Python and Flask:

```python
import requests
from flask import Flask, render_template_string

app = Flask(__name__)

JB_WORKSPACE = "https://your-workspace.myjuicebox.io"
JB_USERNAME = "your-admin@example.com"
JB_PASSWORD = "your-password"

def get_token():
    """Authenticate and return a Bearer token."""
    resp = requests.post(f"{JB_WORKSPACE}/api/v2/auth/", json={
        "username": JB_USERNAME,
        "password": JB_PASSWORD,
    })
    resp.raise_for_status()
    return resp.json()["token"]

def create_access_view(token, app_slug, user_email, data_permissions=None):
    """Create an access view and return its URL."""
    payload = {
        "app_slug": app_slug,
        "user_email": user_email,
        "allowed_uses_cnt": 1,
        "show_header": False,
        "show_footer": False,
    }
    if data_permissions:
        payload["data_permissions"] = data_permissions

    resp = requests.post(
        f"{JB_WORKSPACE}/api/v2/accessviews/",
        json=payload,
        headers={"Authorization": f"Bearer {token}"},
    )
    resp.raise_for_status()
    return resp.json()["url"]

PAGE_TEMPLATE = """
<!DOCTYPE html>
<html>
<body>
  <iframe src="{{ embed_url }}" width="100%" height="800" frameborder="0"></iframe>
</body>
</html>
"""

@app.route("/dashboard")
def dashboard():
    token = get_token()
    embed_url = create_access_view(
        token,
        app_slug="my_app",
        user_email="viewer@example.com",
        data_permissions={
            "automatic_filters": {
                "[region]": ["Northeast"]
            }
        },
    )
    return render_template_string(PAGE_TEMPLATE, embed_url=embed_url)
```

When a user visits `/dashboard`, the backend authenticates with Juicebox, creates a one-time-use access view, and serves a page with the embedded app. In a real application, you'd look up the current user's identity and set the `user_email` and `data_permissions` accordingly.

{% hint style="warning" %}
Store your Juicebox credentials securely (e.g., in environment variables), not in your source code. The example above uses hardcoded values for clarity.
{% endhint %}

### Example: per-user embedding

A common pattern is to create an access view each time a user visits your site:

1. The user logs in to your application.
2. You look up the user's role or organization.
3. You call the Juicebox API to create an access view with data permissions matching that user's access level.
4. You render the page with the access view URL in an iframe.

For example, a school district portal might create access views where each school administrator only sees data for their school:

```json
{
  "app_slug": "student_outcomes",
  "user_email": "jane.doe@lincoln-elementary.edu",
  "data_permissions": {
    "automatic_filters": {
      "[school_id]": ["lincoln_elem"]
    }
  },
  "allowed_uses_cnt": 1,
  "show_header": false,
  "show_footer": false
}
```

### Example: shared organizational account

Access views don't require individual user accounts. You can use a single email to represent an organization, and multiple people can use access views associated with that email:

```json
{
  "app_slug": "sales_dashboard",
  "user_email": "sales@acme-corp.com",
  "data_permissions": {
    "automatic_filters": {
      "[organization]": ["Acme Corp"]
    }
  },
  "allowed_uses_cnt": 10,
  "show_header": false,
  "show_footer": false
}
```

In this pattern, the email identifies the organization rather than an individual person.

### API reference

For the complete API specification — including all endpoints, request/response schemas, filtering, pagination, and rate limits — see the interactive API documentation:

→ [Juicebox Developer API Reference](https://myjuicebox.io/api/schema/redoc/)
