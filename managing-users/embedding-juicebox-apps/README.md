---
description: >-
  Juicebox apps can be embedded in any website. Choose the approach that fits  
  your needs.
---

# Embedding Juicebox Apps

You can embed a Juicebox app in your website so that users see it directly on your page, inside an iframe. There are two approaches, depending on how much control you need over who sees what.

### Choose your approach

#### Embed a public app

If your app is shared as a "Public link," you can embed it on any webpage using a simple iframe. It doesn't require API calls or user accounts. Just copy the embed code and paste it into your site.

This is the right choice when the data in your app is not sensitive and you want anyone who visits your page to see it.

→ [Embedding a public app](embedding-a-public-app.md)

#### Embed with access views

If you need to control who sees the app or what data they see, use **access views**. An access view is a URL generated through the Juicebox API that lets a specific user or account view a specific app with specific data permissions — without requiring them to sign in to Juicebox.

This is the right choice when you need to restrict data by user, organization, or role, and you want the app embedded seamlessly in your own site.

→ [Embedding with access views](embedding-with-access-views.md)

### Embedding vs. SSO (OIDC)

Embedding and SSO are different ways to give users access to Juicebox apps, and they serve different purposes.

**Embedding with access views** generates a URL via the API for each view, bypasses Juicebox sign-in, and lets you hide the app header and footer so the app blends into your site. Each view requires an API call.

**SSO (OIDC)** also bypasses Juicebox sign-in by using your platform's existing authentication, but it gives users the full Juicebox experience — including the workspace homepage and the ability to navigate between apps. No API call is needed for each view.

{% hint style="info" %}
If you are interested in SSO/OIDC integration, [reach out to us](../../getting-started/reach-out-to-us.md).
{% endhint %}
