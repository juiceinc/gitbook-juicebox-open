---
hidden: true
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

# Connecting to Redshift

To set up a connection to a Redshift database, you'll need to provide us the following information:

1. **Hostname or Endpoint**. This identifies your Redshift cluster. You can find it in the AWS Management Console by navigating to your Redshift cluster details and looking under "Properties". It often looks like this: `your-cluster-name.abcdefghijkl.us-east-1.redshift.amazonaws.com`  &#x20;
2. **Port**. The port Redshift uses for connections. This is usually `5439`.
3. **Database Name**. The name of the specific database within your Redshift cluster that you want to connect to.
4. **Username**. The username of a user with permission to access the database. This might be a master user or an IAM user you've created.
5. **Password**. The password associated with the specified username.

**Optional but recommended:**

* **SSL Mode:** It's highly recommended to enable SSL for secure connections. You'll usually choose "Require" to enforce SSL.  &#x20;
* **Schema:** If you want to connect to a specific schema within the database, you'll need to provide its name.

**Where to find this information:**

* **AWS Management Console:** Most of these details are available in the Redshift console within your AWS account.
* **Redshift Cluster Properties:** The hostname, port, and database name can be found in your cluster's properties.  &#x20;
* **IAM User Management:** If you're using IAM users, you'll manage their usernames and passwords in the IAM section of the AWS console.

Once we have this information, we can use it to connect to your Redshift database to your Juicebox workspace.
