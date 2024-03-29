---
description: >-
  You can request content from Juicebox tables in embedded apps and check if the
  report is fully loaded.
---

# Requesting data from embedded apps

You can request the current filtered state of a Juicebox table. This can return either a downloadable file for your user or a json object that can be used to for other automations.&#x20;

Juicebox uses the [postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) javacsript api to safely allow cross origin communication between window objects. Juicebox listens for postMessage events. Juicebox filters postMessage messages to an allowed origin page (currently all Juicebox servers). Your Juicebox representative can ensure your site or test site is whitelisted.

The messages can call **is-report-ready**, **export-data**, or **download-data**.

### Checking the report is fully loaded

In order to export or download data, you must confirm that the Juicebox report is fully loaded. To do so, you can poll the Juicebox report with **is-report-ready**. A javascript sample looks like this.

```javascript
function checkIfReportIsReady() {
  const isReady = event => {
    if (event.data.type == "is-report-ready") {
      window.removeEventListener("message", isReady);
      if (event.data.data === true) {
        // Enable or perform the download or export action
      } else {
        setTimeout(checkIfReportIsReady, 500);
      }
    }
  };
  window.addEventListener("message", isReady, false);
  document.getElementById("juicebox-iframe").contentWindow.postMessage(
    { type: "is-report-ready" }, "*"
  );
};
```

### Receiving the callback

Your page should register an event listener to receive the callback.

```javascript
window.addEventListener("message", event => {
    // Ideally you want to check where the event originated from before responding to it.
    // But for this demo page it has been commented out.
    // if (event.origin !== "http://localhost:8000") {
    //   console.log("Do not trust the sender of this message");
    //   return;
    // }
    console.log("Sender is trusted", event);
    console.log("Received event", event.data, "from", event.origin);
  }, false);
});
```

### Downloading data with download-data

Once the report is [fully loaded](requesting-data-from-embedded-apps.md#checking-the-report-is-fully-loaded), you can request downloadable data. This will return a time-limited url that can be used to download the content. The download data request looks like:

```javascript
document.getElementById("juicebox-iframe").contentWindow.postMessage({
    type: "download-data",
    "download-data": {
       slug: Table1
    }
});
```

In this example, the Juicebox app is iframed in an iframe with id **#juicebox-iframe**. **Table1** is the identifier for the table you want to download.

### Exporting data with export-data

Alternatively, once a report is fully loaded, use **export-data** to return data from a table as a json object.&#x20;

```javascript
document.getElementById("juicebox-iframe").contentWindow.postMessage({
    type: "export-data",
    "export-data": {
       slug: Table1
    }
});
```

As with downloading data, the Juicebox app is iframed in an iframe with id **#juicebox-iframe**. **Table1** is the identifier for the table you want to export.

### Export data response format

The response will be a json object containing the following keys.

* `columns`: A list of columns objects in the order that they appear with column metadata. The properties of each column are:
  * `name`: The display name of the column as it appears in the header of the table.
  * `field`: The property on each row that contains the value.
  * `format`: A juicebox formatting string. For dates and datetimes, these correspond to strftimes. For numbers, the formats are an extension of d3.format [https://observablehq.com/@d3/d3-format](https://observablehq.com/@d3/d3-format) which supports different formats for positive, negative, null, and zero values, as well as prefix and suffix support.
  * `dtype`: The datatype of the column. One of the following
    * `str`: String
    * `num`: Numeric
    * `date`: Date, the values will be formatted as ISO-8601 formatted strings
    * `datetime`: Datetimes, the values will be formatted as ISO-8601 formatted strings
    * `bool`: Boolean values
* `data`: A list of rows. Each row will contain all the columns in the column list.

Here is a sample response:

```
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
       },
   ],
   "data": [
       {
           "Campaign_Start": "2023-10-22T00:00:00",
           "Campaign": "Fall Sale",
           "metric_Total_Delivered": 500,
       },
       {
           "Campaign_Start": "2023-12-22T00:00:00",
           "Campaign": "Winter Sale",
           "metric_Total_Delivered": 1254,
       }
   ]
}
```

### Receiving the callback

**download-data** or **export-data** request may take several seconds to return. Your page should register an event listener to receive the callback containing the data, like this example. The callback will be a message event with origin matching the Juicebox server.

```
window.addEventListener("message", event => {
    // Ideally you want to check where the event originated from before responding to it.
    // But for this demo page it has been commented out.
    // if (event.origin !== "http://localhost:8000") {
    //   console.log("Do not trust the sender of this message");
    //   return;
    // }
   console.log("Sender is trusted", event);
   console.log("Received event", event.data, "from", event.origin);
}, false);

```

### An example

This html file provides a sample implementation of how to communicate with a Juicebox app in an iframe. You should view the source of this file to see how the communication works.

[https://myjuicebox.io/static/embedaccessview.html](https://myjuicebox.io/static/embedaccessview.html)

To use this file, you'll need:

1. Your juicebox servername, typically "https://MYSITE.myjuicebox.io" which you will enter in the site URL.
2. A Juicebox Access View key. Your Juicebox representative can help you get this.
3. Click "Embed It!" to first create an embedded Juicebox iframe.
4. Next you need the slug of a table in the app you've embedded.
5. Choose either "Export Data" or "Download Data".&#x20;
   1. Choosing "Export Data" will log the returned data in the browser console.
   2. Choosing "Download Data" will perform the download.
