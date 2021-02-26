# Changelog 🎁

## What's coming soon?

* Manage workspace settings and subscriptions.
* Invite viewers by email.
* An easier sign-in experience.

## February 25, 2021

### 🎁 What's new?

* ✉️  **Invite editors to your workspace**. Now you can add editors to your workspace team more quickly by sharing invite links or sending invitation emails from either the People view or from the Publish & Share section of an app. 

![](.gitbook/assets/screen_recording_2021-02-25_at_3.30.09_pm.gif)

* 🕵️‍♀️ **Find your folks**. The new search bar in the People view lets you find and manage users even more easily.

### 🐛 Bug fixes & other improvements

* ➕ When you create a new app, you'll go directly to the Data Sources section in that app.
* 🎨  When you open an existing app, you'll go directly to the Story Designer section in that app. 
* 🔢  More data about your data. The data preview now shows you when you last loaded your data and the total number of records. 
* 📱 Editors can now _view_ both published and draft apps when on a phone.
* More performance and bug fixes.

## January 18, 2021

### 🎁 What's new?

* \*\*\*\*🌎**Publish as "Public"**.  Apps can now be [viewed by anyone with the URL](editing-apps/publish-and-share/publishing-app-changes.md#publishing-an-app) — even if they don't have a Juicebox account. Now, go create something _great_ and shout it from the mountain tops \(or from your favorite social network\)! 🏔

![Publish as a public app](.gitbook/assets/screen_recording_2021-01-15_at_6.06.57_pm.gif)

* **Better control of who can see what.** Owners and Admins have a new [People view](managing-users/user-management-and-roles.md#managing-users) to see who is using your apps. Friend your friends🥰; change user roles✊; control app access🔐; unfriend your enemies😒. 

### 🐛 Bug fixes & other improvements

* Even more chart layout improvements.
* Faster app and new workspace creation.
* Lots more performance and bug fixes. 

## December 16, 2020

### 🎁 What's new?

* **Sign up for a workspace.** Now you \(and all your friends\) can [create your own __workspace](getting-started/new-workspace.md). Why would you want your own workspace? Perhaps you want to do some data presentation work for that non-profit you're helping out with. Or maybe you have an idea for a data reporting side-gig. Whatever data-prez itch you have, now you can create a separate workspace to put it in. _Juicebox all-the-things!_
* **Duplicate an app.** If you want to create a new app that is similar to an existing app, you can [duplicate it](editing-apps/app-settings.md#duplicating-an-app).

![Duplicate an app](.gitbook/assets/screen_recording_2020-12-16_at_12.23.23_pm.gif)

* **New footer.**🦶Your app footer now shows the name of the app, when it was last published, the Juicebox version, and all the legal stuff. No more wondering if your Juicebox is up to date.

### 🐛 Bug fixes & other improvements

* More polished loading of the apps page and app editor.
* Publishing apps should be celebrated - and now it is! 🎉
* Improved chart layouts.
* Access links shared on Facebook and LinkedIn are more inviting.
* Database connections to Redshift, Snowflake, Postgres, SQL Server, and MySQL are now supported.
* Many, _many_ other things to make Juicebox even better. 

## October 29, 2020

### 🎁 What's new?

* **Editable section names** - Now you can rename your old, confusing [section](editing-apps/story-designer/sections.md#add-a-section) names, like _group\_a8fwcyke,_ to something less confusing like _Rumpelstiltskin_. Or something. This will make them memorable _and_ useful. And don't forget you can collapse and organize your sections to bring more clarity to your data story.

![](.gitbook/assets/jb-feature-sections2.gif)

* **Support for database connections** - Do you want to add a [data source](editing-apps/data-sources/loading-data.md) from a Redshift or Snowflake database? That's now possible! To get started, send us a message by clicking the chat button below.

### 🐛 Bug fixes & other improvements

* **Numerous slice layout improvements** - Whether you are mixing[ text styles](editing-apps/story-designer/slices/#adding-text) or combining slices in [horizontal section layouts](editing-apps/story-designer/sections.md#section-layouts), everything looks👌.
* **Ingredients are easier to find** - In the ingredient pill, measures now show their aggregation, and advanced ingredients get a cute, new calculator icon. Less sleuthing, more finding. 🔎
* **Trend labeling cleaned up** - The x-axis has been improved so that it shows appropriate labels based on the length of time and aggregation. 📈
* Various Story Designer improvements. After all who doesn't like a better story?
* Various performance and bug fixes. A variety of faster, and an anti-variety of broke.

## October 10, 2020

### 🎁 What's new?

* **Automagic color contrast** - Don't be afraid of the dark! **🎃**Now, when you change the background of your slices to a dark color, the slice will automatically invert other colors so that it remains readable. It's a beautiful way to draw attention to the highlights of your data story! 

![Color your story with beautiful Sections.](.gitbook/assets/feature-inverting.gif)

* **Easier to find your way home** 🏠 ****- To get back to the apps page, just click the Apps button in the header of any app. It's a little like Little Red Riding Hood... but without the wolf.

### 🐛 Bug fixes & other improvements

* **Faster loading apps**: Apps built with uploaded CSVs now get faster the more you use them thanks to the magic of enhanced caching. Nobody likes waiting. Now there's less of it.
* **Better labels**: Ok, we know that in some situations, labeling in the [scatterplot chart](editing-apps/story-designer/charts/scatterplot.md) was well... broken. 🤕It's better now. Boo-boo all gone. 
* **Bar charts use bucket order:** [Bar charts](editing-apps/story-designer/charts/bar.md) that use [bucketed dimensions](editing-apps/data-sources/advanced-ingredients/bucketed-dimensions.md) will now show the buckets in the order you defined them. After all, can't we all use a little more order?  
* **Map charts zoom out farther**: The [map chart](editing-apps/story-designer/charts/map.md) now lets you zoom out farther to get a global perspective. 🌍Next step: Mars. Maybe
* Various performance and bug fixes. Much perform. Un-bugged.

## September 17, 2020

### 🎁 What's new?

* **An improved trend chart** 📈 - We did a brain upgrade on the trend chart. The [trend chart](editing-apps/story-designer/charts/trend.md) is now smarter about handling dates and times. You can easily roll up dates by month or year \(see time ingredient improvement below\), see which dates are missing data, and select ranges of dates to filter the story below. Hey, Trend Chart: it's time you were schooled 🎓. 

![](.gitbook/assets/release-trend.gif)

* **Broken ingredients** 🐣- Change is hard, we know that. When you replace a CSV on a data source, sometimes the new data has different names or different data types. This can break data ingredients. You'll see these [broken ingredients](editing-apps/data-sources/edit-a-data-source.md#fixing-broken-ingredients-caused-by-changes-in-column-names) highlighted \(in a style we call "the blushing zebra"\) so you can fix them. Now change isn't so hard. 

### 🐛 Bug fixes & other improvements

* **Roll up time ingredients by month or year**: You can easily roll up time ingredient dates by month or year by choosing a month or year format when [defining the time ingredient](editing-apps/data-sources/adding-ingredients/#time-ingredient). It's time to roll ⏰.
* **New advanced ingredient functions:** There are new options for advanced aggregations. You can calculate [percentiles and ages](editing-apps/data-sources/advanced-ingredients/advanced-formulas.md#aggregation-functions). This improvement is in the top percentile.
* **More docs on formatting:** The advanced ingredients docs now contains lots of examples of how to build [custom number formats](editing-apps/data-sources/advanced-ingredients/advanced-formats.md#advanced-number-formats). `,.0f" days until Christmas"` might not mean anything to you, but it does to Juicebox. And to Santa. 🎁
* Various performance and bug fixes.

## August 27, 2020

### 🎁What's new? 

#### Share your app via a 🔗 link

Invite anyone to create an account and view your app by simply [sharing your access link](editing-apps/publish-and-share/sharing-and-access-controls.md). ![](https://downloads.intercomcdn.com/i/o/239290807/d306c8ab532685085c8bbd63/feature-sharing2.gif)​

#### +New sign in with your existing account

[Sign in](viewing-apps/signing-in.md) or with Google, LinkedIn, or your email address.

 ​![](https://downloads.intercomcdn.com/i/o/239523099/6b98dbf90a20d77bea96a85d/feature-signin.gif)​

### 🐛Bug fixes & other improvements

* **A better new-app template** - Now, when you make a fresh new app, you'll get a nice template with a header, intro, and sections to fill in to make your data story even more envied by your coworkers.
* **Automagically add your data**🎩- When you add a Data Source to an app, press the "[Add Automagically](editing-apps/data-sources/adding-ingredients/#adding-ingredients-automagically)" button to tell Juicebox which data columns you're most interested in.
* **Story designer slice card improvements** - Added emphasis to the "Save" button, added nice hovering touches, and cleaned some dusty corners.
* **No more "null island" ☠️🏝** - The map chart no longer displays Place dimension values where the latitude or longitude are missing \(null\) or are exactly 0,0 \(the location of what we affectionately call null island in the middle of the Atlantic Ocean. We're guessing that's not the location you really wanted 💀\).
* **Table slice column headers now resize** - The table chart no longer cuts off multi-line column headers. Instead, the column header will resize to fit. Nobody likes being squeezed into something that's too small.
* Various performance and bug fixes.

## August 6, 2020

### 🎁What's New?

* **Date improvements** 📅- New Data Ingredients options let you [group dates](editing-apps/data-sources/advanced-ingredients/advanced-formulas.md#conversion-functions) by week, month, quarter or year.

### 🐛Bug Fixes & Other improvements

* Sharing is caring🔨- Lots of behind the scenes work to let you share your data stories.
* Juicebox is more outgoing and informative if there's an issue uploading data.
* Various infrastructure, error handling and warning improvements.

## July 16, 2020

### 🎁What's new?

* **Replace CSV** 🎉- Updating your data just got 💯better. Opening any existing CSV data source now gives you an option to replace its data.
* **Chat support** 🗣- Get quick access to docs and a place to ask your burning questions. Just click the "?" button in the top right to get started. 

### 🐛Bug fixes & other improvements

* Side panel measure formatting didn't work in some cases. We've ironed that out.
* Various data error handling and warning improvements.





