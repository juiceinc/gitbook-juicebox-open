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

## Request a JWT token for a Client Admin user

<mark style="color:blue;">`GET`</mark> `https://{domain}.myjuicebox.io/api/v1/jb/api-token-auth/`

Request a token that represents a client admin user. This user has permissions to perform user setup and request embed urls for your Juicebox account.

#### Path Parameters

| Name                                     | Type   | Description          |
| ---------------------------------------- | ------ | -------------------- |
| domain<mark style="color:red;">\*</mark> | String | Your Juicebox domain |

#### Headers

| Name                                           | Type   | Description      |
| ---------------------------------------------- | ------ | ---------------- |
| Content-Type<mark style="color:red;">\*</mark> | String | application/json |

#### Request Body

| Name                                       | Type   | Description             |
| ------------------------------------------ | ------ | ----------------------- |
| email<mark style="color:red;">\*</mark>    | String | A client admin email    |
| password<mark style="color:red;">\*</mark> | String | A client admin password |

{% tabs %}
{% tab title="200: OK Response will contain a token to use for further requests" %}
```
{
  "token": {client admin token}
}
```
{% endtab %}

{% tab title="400: Bad Request If your email/password combination is invalid you will receive an Json containing error information." %}

{% endtab %}
{% endtabs %}

Find the app you want the user to be able to see.

## Request list of available apps

<mark style="color:blue;">`GET`</mark> `https://{domain}.myjuicebox.io/api/v1/jb/apps/`

Get a list of all available apps. Juicebox apps have both a published and draft version. The draft version will only be visible to editors and admins.

#### Handling Pagination

If the number of available apps exceeds 100, the list of apps will be paginated. Response headers will contain the following values.

* `X-Count` The total number of apps available.
* `X-Page`The current page number
* `X-PageSize` The number of apps on each page.
* `X-Next` A link to fetch the next page of data. This will be "None" when on the last page of data.
* `X-Previous` A link to fetch the previous page of data. This will be "None" when on the first page of data.

#### Path Parameters

| Name                                     | Type   | Description          |
| ---------------------------------------- | ------ | -------------------- |
| domain<mark style="color:red;">\*</mark> | String | Your Juicebox domain |

#### Headers

| Name                                            | Type   | Description                                                            |
| ----------------------------------------------- | ------ | ---------------------------------------------------------------------- |
| Authorization<mark style="color:red;">\*</mark> | String | <p>"JWT {token}"</p><p></p><p>A JWT token for a client admin user.</p> |

{% tabs %}
{% tab title="200: OK A Json list of all apps in this workspace." %}

{% endtab %}

{% tab title="403: Forbidden You do not have permission to view the list of apps." %}

{% endtab %}
{% endtabs %}

Create a user with the Juicebox Data Permissions and app access you desire.

## Create a user

<mark style="color:green;">`POST`</mark> `https://{domain}.myjuicebox.io/api/v1/jb/users/`

#### Path Parameters

| Name                                     | Type   | Description          |
| ---------------------------------------- | ------ | -------------------- |
| domain<mark style="color:red;">\*</mark> | String | Your Juicebox domain |

#### Headers

| Name                                            | Type   | Description                                                            |
| ----------------------------------------------- | ------ | ---------------------------------------------------------------------- |
| Authorization<mark style="color:red;">\*</mark> | String | <p>"JWT {token}"</p><p></p><p>A JWT token for a client admin user.</p> |

#### Request Body

| Name                                    | Type   | Description                                                                                                                                |
| --------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| email<mark style="color:red;">\*</mark> | String | The email address of the user you want to create.                                                                                          |
| extra                                   | Json   | A **Juicebox Data Permissions** object to control what this user can see. If omitted, the user will not have any data permissions applied. |
| first\_name                             | String | The user's first name                                                                                                                      |
| last\_name                              | String | The user's last name                                                                                                                       |
| apps                                    |        | A list of app ids that this user is allowed to see.                                                                                        |

{% tabs %}
{% tab title="201: Created The user was created." %}

{% endtab %}

{% tab title="403: Forbidden You do not have permissions to create a user." %}

{% endtab %}
{% endtabs %}

Now you can request an app embed url.

## Request an app embed url for a user

<mark style="color:green;">`POST`</mark> `https://{domain}.myjuicebox.io/api/v1/jb/apps/{appid}/embed/{email}/`

For security, the default duration of an embed url is 60 seconds. It can only be loaded once. It can be regenerated as many times as needed.

#### Path Parameters

| Name                                     | Type   | Description                                        |
| ---------------------------------------- | ------ | -------------------------------------------------- |
| domain<mark style="color:red;">\*</mark> | String | Your Juicebox domain                               |
| appid<mark style="color:red;">\*</mark>  | String | An app id for an app this user has access to.      |
| email<mark style="color:red;">\*</mark>  | String | An email for a user that has already been created. |

#### Query Parameters

| Name         | Type   | Description                                                                                                                                                                                                           |
| ------------ | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| show\_header | String | <p>If this parameter is present in the query string, the application header (which allows export as png and pdf) will be displayed. </p><p></p><p>Turn off display of the header with <code>?show_header=0</code></p> |
| show\_footer | String | <p>If this parameter is present in the query string, the application footer will be displayed.</p><p></p><p>Turn off display of the header with <code>?show_footer=0</code></p>                                       |

#### Headers

| Name                                            | Type   | Description                                                            |
| ----------------------------------------------- | ------ | ---------------------------------------------------------------------- |
| Authorization<mark style="color:red;">\*</mark> | String | <p>"JWT {token}"</p><p></p><p>A JWT token for a client admin user.</p> |

{% tabs %}
{% tab title="200: OK The response will contain Json with url and expires_at keys. This url can be embedded in an iframe." %}

{% endtab %}

{% tab title="403: Forbidden The user does not have permission to request app embeds." %}

{% endtab %}
{% endtabs %}



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





