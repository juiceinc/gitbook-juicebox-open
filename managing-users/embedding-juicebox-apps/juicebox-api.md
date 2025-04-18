---
description: >-
  The Juicebox API can be used for generating urls to embed apps in your
  webpage.
---

# Juicebox API

### Handling Pagination

The maximum pagination size is limited by object. Apps are limited to page sizes of 100, other objects will return 10000 objects. If the number of available objects exceeds the limit, the list will be paginated. Response headers will contain the following values.

* `X-Count` The total number of objects available.
* `X-Page`The current page number
* `X-PageSize` The number of objects on each page.
* `X-Next` A link to fetch the next page of data. This will be "None" when on the last page of data.
* `X-Previous` A link to fetch the previous page of data. This will be "None" when on the first page of data.

{% openapi src="../../.gitbook/assets/Juicebox API (6).yaml" path="/api/v1/access_views/" method="get" expanded="true" fullWidth="true" %}
[Juicebox API (6).yaml](<../../.gitbook/assets/Juicebox API (6).yaml>)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/Juicebox API (6).yaml" path="/api/v1/access_views/" method="post" expanded="true" fullWidth="true" %}
[Juicebox API (6).yaml](<../../.gitbook/assets/Juicebox API (6).yaml>)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/Juicebox API (6).yaml" path="/api/v1/access_views/{key}/" method="get" expanded="true" fullWidth="true" %}
[Juicebox API (6).yaml](<../../.gitbook/assets/Juicebox API (6).yaml>)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/Juicebox API (6).yaml" path="/api/v1/access_views/{key}/" method="put" expanded="true" fullWidth="true" %}
[Juicebox API (6).yaml](<../../.gitbook/assets/Juicebox API (6).yaml>)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/Juicebox API (6).yaml" path="/api/v1/access_views/{key}/" method="delete" expanded="true" fullWidth="true" %}
[Juicebox API (6).yaml](<../../.gitbook/assets/Juicebox API (6).yaml>)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/Juicebox API (6).yaml" path="/api/v1/access_views/{key}/" method="patch" expanded="true" fullWidth="true" %}
[Juicebox API (6).yaml](<../../.gitbook/assets/Juicebox API (6).yaml>)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/Juicebox API (6).yaml" path="/api/v1/access_views/{key}/usage/" method="get" expanded="true" fullWidth="true" %}
[Juicebox API (6).yaml](<../../.gitbook/assets/Juicebox API (6).yaml>)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/Juicebox API (6).yaml" path="/api/v1/jb/api-token-auth/" method="post" expanded="true" fullWidth="true" %}
[Juicebox API (6).yaml](<../../.gitbook/assets/Juicebox API (6).yaml>)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/Juicebox API (6).yaml" path="/api/v1/jb/apps/" method="get" expanded="true" fullWidth="true" %}
[Juicebox API (6).yaml](<../../.gitbook/assets/Juicebox API (6).yaml>)
{% endopenapi %}

{% openapi src="../../.gitbook/assets/Juicebox API (7).yaml" path="/api/v1/jb/apps/{id}/clear_cache/" method="delete" %}
[Juicebox API (7).yaml](<../../.gitbook/assets/Juicebox API (7).yaml>)
{% endopenapi %}
