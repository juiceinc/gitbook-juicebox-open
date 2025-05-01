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

# Connecting to Postgres

To set up a connection to a Postgres database, you'll need to provide us the following information:

1. **Hostname or IP Address**. This identifies the server where your Postgres database is running. It could be a domain name (e.g., `mypostgresdb.example.com`) or an IP address (e.g., `192.168.1.100`).
2. **Port**. The port number that Postgres is listening on. The default port is usually `5432`.
3. **Database Name**. The name of the specific database you want to connect to.
4. **Username**. The username of a Postgres user account with permission to access the database.
5. **Password**. The password associated with the specified username.

**Optional but recommended:**

* **SSL Mode:** It's highly recommended to enable SSL for secure connections. You'll typically have options like "require" (enforce SSL), "verify-ca" (verify the server's certificate), or "disable" (not recommended).  &#x20;
* **Schema:** If you want to connect to a specific schema within the database, you'll need to provide its name.

**Where to find this information:**

* **Postgres Configuration Files:** The `postgresql.conf` file (usually located in the Postgres data directory) contains settings like the port number and SSL configuration.
* **`psql` Command-line Tool:** You can use the `psql` tool to connect to the database and then use commands like `\conninfo` to display connection information.
* **Database Administration Tools:** Tools like pgAdmin can provide details about your Postgres server and databases.

Once we have this information, we can use it to connect to your Postgres database to your Juicebox workspace.
