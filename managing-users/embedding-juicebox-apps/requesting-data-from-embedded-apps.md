---
description: >-
  Request data from Juicebox tables in embedded apps using the browser's  
  postMessage API.
---

# Requesting data from embedded apps

## Requesting Data from Embedded Apps

Once a Juicebox app is embedded in an iframe, your page can communicate with it to request data from tables in the app. You can either download data as a file or export it as a JSON object for use in your own code.

Juicebox uses the browser's [postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) API for cross-origin communication between your page and the embedded app. The supported message types are **is-report-ready**, **export-data**, and **download-data**.

{% hint style="info" %}
Your site must be whitelisted for postMessage communication with Juicebox. Reach out to us to have your domain added.
{% endhint %}

### Checking that the app is fully loaded

Before requesting data, you need to confirm the app has finished loading. Poll the app with **is-report-ready**:

```javascript
function checkIfReportIsReady() {
  const isReady = event => {
    if (event.data.type === "is-report-ready") {
      window.removeEventListener("message", isReady);
      if (event.data.data === true) {
        // The app is ready — you can now export or download data
      } else {
        setTimeout(checkIfReportIsReady, 500);
      }
    }
  };
  window.addEventListener("message", isReady, false);
  document.getElementById("juicebox-iframe").contentWindow.postMessage(
    { type: "is-report-ready" }, "*"
  );
}
```

### Downloading data

Once the app is ready, you can request a downloadable file using **download-data**. This returns a time-limited URL that can be used to download the table contents.

```javascript
document.getElementById("juicebox-iframe").contentWindow.postMessage({
  type: "download-data",
  "download-data": {
    slug: "Table1"
  }
}, "*");
```

Replace `Table1` with the identifier (slug) of the table you want to download.

### Exporting data as JSON

Use **export-data** to get the table data as a JSON object, which you can then use in your own code:

```javascript
document.getElementById("juicebox-iframe").contentWindow.postMessage({
  type: "export-data",
  "export-data": {
    slug: "Table1"
  }
}, "*");
```

#### Export response format

The response is a JSON object with two keys:

**`columns`** — A list of column objects in display order. Each column has:

| Property | Description                                                            |
| -------- | ---------------------------------------------------------------------- |
| `name`   | Display name as shown in the table header                              |
| `field`  | Property name on each data row                                         |
| `format` | Formatting string (strftime for dates, extended d3.format for numbers) |
| `dtype`  | Data type: `str`, `num`, `date`, `datetime`, or `bool`                 |

**`data`** — A list of row objects. Each row contains properties matching the `field` values from the columns list.

Example response:

```json
{
  "columns": [
    {
      "name": "Campaign Start",
      "field": "Campaign_Start",
      "format": "%b %-d, %Y",
      "dtype": "datetime"
    },
    {
      "name": "Campaign",
      "field": "Campaign",
      "format": null,
      "dtype": "str"
    },
    {
      "name": "Total Delivered",
      "field": "metric_Total_Delivered",
      "format": ",.0f;,.0f;,.0f;\"---\"",
      "dtype": "num"
    }
  ],
  "data": [
    {
      "Campaign_Start": "2023-10-22T00:00:00",
      "Campaign": "Fall Sale",
      "metric_Total_Delivered": 500
    },
    {
      "Campaign_Start": "2023-12-22T00:00:00",
      "Campaign": "Winter Sale",
      "metric_Total_Delivered": 1254
    }
  ]
}
```

### Receiving callbacks

Both **download-data** and **export-data** may take several seconds to return. Register an event listener on your page to receive the response:

```javascript
window.addEventListener("message", event => {
  // In production, verify the event origin matches your Juicebox server:
  // if (event.origin !== "https://your-workspace.myjuicebox.io") return;

  console.log("Received event", event.data, "from", event.origin);
}, false);
```

### Try it out

Juicebox provides a sample HTML page that demonstrates how to communicate with an embedded app:

[https://myjuicebox.io/static/embedaccessview.html](https://myjuicebox.io/static/embedaccessview.html)

To use it, you'll need your Juicebox workspace URL (e.g., `https://your-workspace.myjuicebox.io`), an access view key from the API, and the slug of a table in the app.
