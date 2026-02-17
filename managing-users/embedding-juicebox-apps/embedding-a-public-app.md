---
description: Embed a public Juicebox app on any webpage using a simple iframe.
---

# Embedding a public app

If your Juicebox app is shared as a **Public link**, you can embed it on any webpage without needing the API or user accounts.

### How to get the embed code

1. Open your app in the Juicebox editor.
2. Click **Share** (or **Sharing**) in the upper-right.
3. Make sure the app access is set to **Public link**.
4. Select **Copy Embed Code**.&#x20;
5. Paste the embed code into your webpage's HTML. It will look something like this:

```html
<iframe
  src="https://your-workspace.myjuicebox.io/a/your-app-slug/embed/"
  width="100%"
  height="800"
  frameborder="0"
></iframe>
```

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

### When to use this approach

Public embedding works well when the data is not sensitive and you want the broadest possible access. Anyone who can view the webpage will be able to see the app.

If you need to control who can see the app or limit what data different users see, use access views instead.

{% hint style="warning" %}
**Public apps do not require authentication.** Anyone with the URL can view the data. Do not use public embedding for sensitive or restricted data.
{% endhint %}

### Customizing the iframe

You can adjust the `width`, `height`, and other standard iframe attributes to fit your page layout. For a responsive embed, you can wrap the iframe in a container with CSS:

```html
<div style="position: relative; width: 100%; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe
    src="https://your-workspace.myjuicebox.io/a/your-app-slug/embed/"
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
    frameborder="0"
  ></iframe>
</div>
```
