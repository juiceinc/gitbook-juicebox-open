---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Connecting to BigQuery

To connect to BigQuery, you'll need to give Juicebox service accounts permission on the BigQuery datasets that you want to share. [Reach out to us](../../../getting-started/reach-out-to-us.md) to get our service accounts.&#x20;

In addition, you'll need to provide us the following information:

1. **Project ID**. This is the unique identifier for your Google Cloud Project where your BigQuery data resides. You can find it in the Google Cloud Console.
2. **Dataset ID**. The name of the dataset within your project that contains the tables you want to access.

**Where to find this information:**

* **Google Cloud Console:** You can find your project ID and dataset IDs in the Google Cloud Console.  &#x20;
* **BigQuery Web UI:** The BigQuery web UI also displays your project ID and datasets.  &#x20;
* **`bq` Command-line Tool:** The `bq show` command can display information about your project and datasets.

Once we have this information, we can use it to connect to your BigQuery database to your Juicebox workspace.
