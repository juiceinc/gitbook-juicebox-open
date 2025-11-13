---
hidden: true
---

# Connecting to Snowflake

To set up a connection to a Snowflake database, you'll need to provide us the following information:

1. **Account Identifier**. This is a unique identifier for your Snowflake account. It often looks like this: `xy12345.snowflakecomputing.com` or, if you have a custom domain, `xy12345.myorganization.snowflakecomputing.com`. Sometimes you might need to include the region code in the account identifier (e.g., `xy12345.us-east-1.snowflakecomputing.com`).
2. **Username**. The username to be used to log in to Snowflake.
3. **Password**. The password associated with the specified username.
4. **Role**. The role to be assumed by the user.&#x20;
5. **Warehouse**. The virtual warehouse that will be used for your queries.
6. **Database**. The database to connect to.&#x20;

**Optional:**&#x20;

* **Schema:** If you want to connect to a specific schema within the database, you'll need to provide its name.

**Where to find this information:**

* **Snowflake Web Interface:** You can find your account identifier in the URL when logged into the Snowflake web interface.
* **SnowSQL Client:** The SnowSQL command-line client allows you to configure connection parameters and store them for future use.
* **Connection Strings:** Snowflake provides flexible connection strings where you can embed much of this information directly.

Once we have this information, we can use it to connect to your Snowflake database to your Juicebox workspace.
