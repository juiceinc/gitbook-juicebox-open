# Embedding Juicebox Apps

Juicebox apps can be embedded in any website you control.

### Overview of Embedding

Delivering a Juicebox story requires:

1. A Juicebox application.
2. Juicebox users that may have [data permissions](../limiting-what-data-users-can-see.md).
3. A website where your story will be displayed.

Embedding gives you control of items 2) and 3). For these examples, we’ll call you **HealthyCo 🧃**.  You sell organic juices and have developed several reports for internal and external use to show how your juices are performing. &#x20;

### What is embedding?

Embedding allows Juicebox stories to be delivered in any webpage by generating a one-time use url that represents a user viewing a report.

This url can be displayed in an iFrame on HealthyCo’s website.

### When should I use embedding?

There are several ways to use Juicebox. \


| Approach                                                                                                                                                                   | How to setup users                                                                                                                        | The user experience                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| <p><strong>Invite users with access keys</strong><br></p><p>This is easiest for small numbers of users as it requires no integration or development work by HealthyCo.</p> | <p><br>Use the app sharing view to create  </p>                                                                                           | Apps are displayed on a subdomain of the Juicebox website. For instance, healthyco.myjuicebox.io.  |
| <p><strong>Embedding</strong></p><p><br>This is the most flexible approach and presents the Juicebox report directly in the HealthyCo website.</p>                         | <p><br><br>Use Juicebox APIs to set up users with the correct data permissions. This can be fully customized by HealthyCo developers.</p> | <p><br>The Juicebox story is embedded seamlessly in an iFrame on HealthyCo’s webpage.</p>          |

### How embedding works

Use the Juicebox API to perform user setup and request an embeddable url to show a user an app. That embeddable url can be used as an iFrame src to display the Juicebox in your website. [Here is the flow](./#how-embedding-works).

\
