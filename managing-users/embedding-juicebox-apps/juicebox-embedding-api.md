---
description: Here are the relevant API calls
---

# Juicebox Embedding API

To embed Juicebox apps in your own website, follow these steps.

1. Request a JWT token as a client admin user. This token can be reused.
2. Request details about what Juicebox apps are available. This will provide you an app id for the app you want to embed.
3. Create a Juicebox user with the appropriate [**Data permissions object**](../limiting-what-data-users-can-see.md) that limits what the user can see.
4. Request an embed url for this user to see the app.&#x20;
5. Serve the embed url in an iframe on your site.



Let's look at the details for each of these steps.

{% swagger method="get" path="/" baseUrl="https://{domain}.myjuicebox.io/api/v1/jb/api-token-auth" summary="Request a JWT token for a Client Admin user" expanded="true" fullWidth="true" %}
{% swagger-description %}
Request a token that represents a client admin user. This user has permissions to perform user setup and request embed urls for your Juicebox account.
{% endswagger-description %}

{% swagger-parameter in="body" name="email" type="String" required="true" %}
A client admin email
{% endswagger-parameter %}

{% swagger-parameter in="body" name="password" type="String" required="true" %}
A client admin password
{% endswagger-parameter %}

{% swagger-parameter in="header" name="Content-Type" type="String" required="true" %}
application/json
{% endswagger-parameter %}

{% swagger-parameter in="path" required="true" name="domain" %}
Your Juicebox domain
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response will contain a token to use for further requests" %}
```
{
  "token": {client admin token}
}
```
{% endswagger-response %}

{% swagger-response status="400: Bad Request" description="If your email/password combination is invalid you will receive an Json containing error information." %}

{% endswagger-response %}
{% endswagger %}

Find the app you want the user to be able to see.

{% swagger method="get" path="/api/v1/apps/" baseUrl="https://{domain}.myjuicebox.io" summary="Request list of available apps" expanded="true" fullWidth="true" %}
{% swagger-description %}
Get a list of all available apps. Juicebox apps have both a published and draft version. The draft version will only be visible to editors and admins.
{% endswagger-description %}

{% swagger-parameter in="header" name="Authorization" required="true" %}
"JWT {token}"



A JWT token for a client admin user.
{% endswagger-parameter %}

{% swagger-parameter in="path" name="domain" required="true" %}
Your Juicebox domain
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="A Json list of all apps in this workspace." %}

{% endswagger-response %}

{% swagger-response status="403: Forbidden" description="You do not have permission to view the list of apps." %}

{% endswagger-response %}
{% endswagger %}

Create a user with the Juicebox Data Permissions and app access you desire.

{% swagger method="post" path="{domain}.myjuicebox.io/api/v1/jb/users/" baseUrl="https://" summary="Create a user" expanded="true" fullWidth="true" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-parameter in="header" name="Authorization" type="String" required="true" %}
"JWT {token}"



A JWT token for a client admin user.
{% endswagger-parameter %}

{% swagger-parameter in="body" name="email" required="true" %}
The email address of the user you want to create.
{% endswagger-parameter %}

{% swagger-parameter in="body" name="extra" type="Json" %}
A 

**Juicebox Data Permissions**

 object to control what this user can see. If omitted, the user will not have any data permissions applied.
{% endswagger-parameter %}

{% swagger-parameter in="body" name="first_name" %}
The user's first name
{% endswagger-parameter %}

{% swagger-parameter in="body" name="last_name" %}
The user's last name
{% endswagger-parameter %}

{% swagger-parameter in="body" name="apps" type="" %}
A list of app ids to give to this user. 
{% endswagger-parameter %}

{% swagger-parameter in="path" name="domain" required="true" %}
Your Juicebox domain
{% endswagger-parameter %}

{% swagger-response status="201: Created" description="The user was created." %}

{% endswagger-response %}

{% swagger-response status="403: Forbidden" description="You do not have permissions to create a user." %}

{% endswagger-response %}
{% endswagger %}

Now you can request an app embed url.

{% swagger method="post" path="/jb/apps/{appid}/embed/{email}/" baseUrl="https://{domain}.myjuicebox.io/api/v1" summary="Request an app embed url for a user" expanded="true" fullWidth="true" %}
{% swagger-description %}
For security, the default duration of an embed url is 60 seconds. It can only be loaded once. It can be regenerated as many times as needed.
{% endswagger-description %}

{% swagger-parameter in="header" name="Authorization" required="true" %}
"JWT {token}"



A JWT token for a client admin user.
{% endswagger-parameter %}

{% swagger-parameter in="path" name="domain" required="true" %}
Your Juicebox domain
{% endswagger-parameter %}

{% swagger-parameter in="path" name="appid" required="true" %}
An app id for an app this user has access to.
{% endswagger-parameter %}

{% swagger-parameter in="path" name="email" required="true" %}
An email for a user that has already been created.
{% endswagger-parameter %}

{% swagger-parameter in="body" name="show_header" type="Integer" %}
Can by 1 or 0. Should the application header be displayed.
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="The response will contain Json with url and expires_at keys. This url can be embedded in an iframe." %}

{% endswagger-response %}

{% swagger-response status="403: Forbidden" description="The user does not have permission to request app embeds." %}

{% endswagger-response %}
{% endswagger %}



Serving the app in an iframe. To embed the app in your site, use the following html. You can vary height and width as appropriate for your site.

```
<iframe 
  title="{app title}" 
  src="{url}" 
  height="650px" 
  width="100%" 
  frameborder="0" 
  sandbox="allow-scripts allow-downloads allow-same-origin allow-forms allow-popups">
</iframe>
```





