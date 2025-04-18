# Connecting to Databricks

Juicebox supports connections to Databricks across all major cloud providers: AWS, Google Cloud Platform (GCP) and Microsoft Azure.&#x20;

## Prerequisites

Before connecting Juicebox to Databricks, ensure you have:

1. A Databricks workspace with:
   * An active SQL warehouse (a SQL-optimized compute resource for data warehousing)
   * Tables or views in Unity Catalog with the relevant data
   * A user or service principal with appropriate data access permissions and compute resource access to query the relevant data sources:
     * `USE CATALOG` on the catalog(s) containing the tables or views
     * `USE SCHEMA` on the schema(s) containing the tables or views
     * `SELECT` on the tables or views
     * `Can use` permissions for a SQL warehouse compute resource
   * A Premium or Enterprise plan (recommended for optimized performance)
2. A Juicebox workspace with:
   * &#x20;A Business or Unlimited subscription. Database connections are only available on these subscription levels. Reach out to help@myjuicebox.io to learn more about subscription options.
   * A Juicebox user account with Owner or Admin privileges.
3. The connection details (see [Connection Methods](connecting-to-databricks.md#connection-methods) below)
4. A secure method to share connection details (such as 1Password's one-time sharing feature)

## Connection Methods

There are two authentication methods available to connect to Databricks from a Juicebox workspace: Personal Access Token (PAT) and OAuth. PAT is suitable for testing and development, but is not recommended for production. OAuth is the recommended method for use in production.&#x20;

Connection details for either method need to be shared with Juice Analytics by a user having Admin or higher privileges in the Juicebox workspace. To start this process, reach out to help@myjuicebox.io.

### Connect Using PAT Authentication

PAT authentication can be generated for a Databricks user account and will have the same permissions as the associated user account. It is suitable for testing and development, but is not recommended for production.&#x20;

1. Create a Personal Access Token in Databricks:
   * In your Databricks workspace, click on the user profile button in the upper-right and select **Settings**
   * In the **Settings** side bar, select the **Developer** tab
   * Click the **Manage** button in the **Access tokens** section&#x20;
   * Click the **Generate new token** button
   * Provide a description and set expiration
   * Copy the generated personal access token (it will only be shown once)
2. Provide Connection Details to Juice Analytics (see [Finding Connection Details](connecting-to-databricks.md#finding-connection-details-in-databricks) section for more information):
   * Use a secure sharing method like 1Password's [one-time sharing](https://support.1password.com/share-items/?mac) feature
   * Share the following information:
     * hostname: The Databricks server hostname&#x20;
     * http\_path: The HTTP path to the Databricks SQL endpoint
     * catalog: The catalog to use for the connection
     * schema: The schema to use for the connection (optional)
     * access\_token: Your Databricks personal access token copied from Step 1 (this will be stored securely)

### Connect Using OAuth Authentication

OAuth authentication requires a service principal with appropriate permissions. OAuth is suitable for all environments and recommended for production.&#x20;

1. Create a Service Principal in Databricks (you must be an Admin to do this):
   * In your Databricks workspace, click on the user profile button in the upper-right and select **Settings**
   * In the **Settings** side bar, select the **Identity and access** tab under **Workspace admin**
   * Click the **Manage** button in the **Service principals** section&#x20;
   * Click the **Add service principal** button
   * Click the **Add new** button
   * Enter a service principal name and click **Add**
2. Generate an OAuth Secret for the Service Principal
   * On the service principal's details page, click the **Secrets** tab
   * Under OAuth secrets, click **Generate secret**
   * Set the secret's lifetime in days (maximum 730 days)
   * Copy the displayed **Secret** (it will only be shown once) and **Client ID**, then click Done
3. Provide Connection Details to Juice Analytics (see [Finding Connection Details](connecting-to-databricks.md#finding-connection-details-in-databricks) section for more information):
   * Use a secure sharing method like 1Password's [one-time sharing](https://support.1password.com/share-items/?mac) feature
   * Share the following information:
     * hostname: The Databricks server hostname&#x20;
     * http\_path: The HTTP path to the Databricks SQL warehouse
     * catalog: The catalog to use for the connection
     * schema: The schema to use for the connection (optional)
     * account\_id: The OAuth account ID
     * client\_id: The OAuth client ID (also called the service principal application ID)
     * secret: Your OAuth client secret from Step 2 (this will be stored securely)

{% hint style="info" %}
Juicebox will automatically generate the access tokens, which are used for secure authentication with your Databricks workspace. This eliminates the need for you to manage access token rotation.&#x20;
{% endhint %}

## Finding Connection Details in Databricks

### hostname and http\_path

* In your Databricks workspace, navigate to **SQL Warehouses**
* Select the SQL warehouse you want to connect to
* Click on **Connection details**
* Copy the **Server hostname** and **HTTP path** values

{% hint style="info" %}
The format of the server hostname differs between cloud providers:

* AWS: Server hostname typically follows the pattern dbc-\<id>.\<region>.databricks.com
* Azure: Server hostname typically follows the pattern adb-\<workspace-id>.\<random-number>.azuredatabricks.net
* GCP: Server hostname typically follows the pattern \<workspace-name>.\<region>.gcp.databricks.com
{% endhint %}

### catalog and schema

* In your Databricks workspace, navigate to Catalog
* The top-level container is the catalog. Each connection requires a single catalog.
* The containers within the catalog are the schemas. Schemas contain tables and views. Specifying the schema is optional. &#x20;

### account\_id (for OAuth only)

* In your Databricks workspace, click on the workspace dropdown to the left of the user profile button
* Click **Manage account**. This will open the account console.&#x20;
* Click the user profile button in the upper-right of the account console.
* Copy the **Account ID**.

### client\_id (for OAuth only)

* In your Databricks workspace, click on the user profile button in the upper-right and select **Settings**
* In the **Settings** side bar, select the **Identity and access** tab under **Workspace admin**
* Click the **Manage** button in the **Service principals** section&#x20;
* Click the service principal name to access its details
* Copy the Application ID (also called the Client ID)

## Adding a Databricks Data Source to a Juicebox Report

After sending the connection details to the Juice Analytics team, the Databricks connection will be set up in your workspace. After it is set up, a new Databricks connection button will appear in the data drawer of each draft report in your Juicebox workspace like this:

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXf4dJww3T0w22lx6Zu-_aI6WtJv9bczTp52CwO5t6KmAC-2taA7b7cEAyVjLRHNSXhutVOTeo1wLGhHZAKLcvsZHXYVhgIt5nKzaczpsE43DMB2Yb4AFkaqepvoUxPsAjtuInnl?key=DC8iFrXKhF8GLSQbp4-fJBCD" alt=""><figcaption><p>Two Databricks connections have been set up for this workspace: Databricks Workspace and Databricks Samples</p></figcaption></figure>

To add a data source using the Databricks connection, click on the connection button, select the schema, and select the table or view to add.&#x20;

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXd2JZUicMhQmVGa-oqjj2bbr-0EjHGJYdTT2EJbK3qUJj1661tB95CDbTEoL4tbUo5o5EMj5cuHBPPwhKr069-NsPwo6gJ-jM8ulDDpfI4vW2EMayr7o_jY425GGp1s1-rY1fRD?key=DC8iFrXKhF8GLSQbp4-fJBCD" alt=""><figcaption><p>After clicking on the Databricks connection button, select the data source to add to the Juicebox report</p></figcaption></figure>

Once the data source has been added to the Juicebox report, you can use it to configure slices.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeNdqtuIcBJuoh__JcHmQYac_I8Aw_wXZuoQOrR_IIdrZ4E9nQNIWeAkeWUKVEzrbfOgYDls0sJ3eqAMXrQABJu3MZfJarRYCrV6ru7KIqNWad95cMT8eb8VeDITokAFGD5Vs0?key=DC8iFrXKhF8GLSQbp4-fJBCD" alt=""><figcaption><p>Newly added Databricks data source now available to configure Juicebox slices</p></figcaption></figure>

## User-level permissions within Juicebox

Additional access controls can be configured within Juicebox at the user level. This allows for granular control over who can see which Juicebox reports and what filters are applied for the user within each report. These permissions are managed separately from Databricks permissions. See [Managing Users](broken-reference).

## Support

For help setting up a Databricks connection in Juicebox, reach out to us at help@myjuicebox.io.

\
