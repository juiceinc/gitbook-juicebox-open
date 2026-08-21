---
hidden: true
---

# Connecting to BigQuery

To connect to BigQuery, you'll grant Juicebox read access to the datasets you want to share, and then send us your project and dataset details.

[Reach out to us](../../../getting-started/reach-out-to-us.md) to get our service account addresses. There are two: a development account, used for initial access testing, and a production account, used once your project is in production. **Grant the permissions in both steps below to both accounts.**

### Step 1. Grant dataset permissions

In the BigQuery console, for each dataset you want to share with Juicebox, grant both service accounts the **BigQuery Data Viewer** role.

This gives Juicebox read-only access to that dataset. Datasets you don't grant access to remain invisible to us.

### Step 2. Grant project permissions

Dataset access on its own is not enough. In your project's **IAM** settings, grant both service accounts these two roles:

* **BigQuery Job User**
* **BigQuery Read Session User**

**Job User** is required because BigQuery runs every query as a job in the project the connection points at. Without it, the connection fails as soon as Juicebox runs its first query, with an error like:

```
403 Access Denied: Project your-project-id: User does not have
bigquery.jobs.create permission in project your-project-id.
```

**Read Session User** is required because Juicebox uses the BigQuery Storage Read API to retrieve larger result sets. Without it, the connection may work for smaller queries but return `403 Forbidden` on queries returning larger results.

{% hint style="info" %}
Both of these are project-level grants made in IAM, not dataset-level grants made in the BigQuery console. This is the most common setup mistake — granting Data Viewer alone looks correct but produces the error above.
{% endhint %}

### Step 3. Send us your project and dataset details

Provide the following:

1. **Project ID**. The unique identifier for the Google Cloud project where your BigQuery data resides.
2. **Dataset ID** for each dataset you've shared.&#x20;

The fully-qualified form includes both, for example `my-project-prod.my_dataset`.

**Where to find this information:**

* **Google Cloud Console:** You can find your project ID and dataset IDs in the Google Cloud Console.
* **BigQuery Web UI:** The BigQuery web UI also displays your project ID, datasets, and each dataset's location.
* **`bq` Command-line Tool:** The `bq show` command can display information about your project and datasets.

Once we have this information, we can connect your BigQuery database to your Juicebox workspace.

### What we don't need

Juicebox never requires BigQuery service account keys, credentials, or write access of any kind. We read only the datasets you explicitly share, using the read-only roles listed above.
