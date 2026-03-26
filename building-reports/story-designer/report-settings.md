---
description: >-
  Configure your report's description, pages, theme, header, and editor
  behavior.
---

# Report Settings

Report Settings is a panel that opens from the **Report Settings** button in the editor header. It contains settings that apply to the entire report.

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

## Description

The description appears on the home page and in the report header. Aim for a sentence or a few short phrases that tell viewers what the report is about.

## Table of Contents

Toggle this on to include a dropdown in the published report that lets viewers jump directly to a section. This is helpful for longer reports with multiple sections.

## Manage Pages

A report can have one or more pages. Each page has its own sections and slices. Reports with multiple pages show page navigation links below the Home button in the report header, and the current page appears highlighted in the navigation.

{% hint style="info" %}
Pages are currently available by request. [Reach out to us](../../getting-started/reach-out-to-us.md) to enable multi-page support for your workspace.
{% endhint %}

### Adding, renaming, and deleting pages

**Add a page**. Click **+ Add Page**, enter a page title (keep it short — 2 to 4 words), and click **+ Create**. The new page will start with default sections.

**Rename a page**. Click the pencil icon next to the page name to edit the title.

**Delete a page**. Click the trash icon next to the page name. You will be asked to confirm, because deleting a page permanently removes all of its sections and slices. A published report is not affected until you share the changes.

{% hint style="danger" %}
Deleting a page cannot be undone. All sections and slices on that page will be permanently removed.
{% endhint %}

**Reorder pages**. Drag and drop pages in the list to change their order. The order here determines the order of the navigation links in the report header.

### Linking between pages

When editing text in a slice, you can create links that navigate to other pages in the same report. In the text editor link dialog, select a page from the **Link to a Page** list. These links navigate within the report without a full page reload and carry forward any active filter selections. See [Linking to a page](slices/#linking-to-a-page) for details.

### Passing filters between pages

When viewers navigate between pages, slices on the target page can automatically apply matching filter selections from the page they came from. This is controlled by a per-slice toggle called **Receive filters from another Page**. See [Common slice configuration options](slices/#configure-tab) for details.

## Theme

### Color Theme

Choose the color theme for your report. The primary color (shown in the circle) is used in charts. The additional colors are used automatically as header and section backgrounds and are available for selection as background colors throughout the report.

You can switch color themes at any time. If theme colors are used as backgrounds, they will update to the new theme colors. Non-theme background colors are not affected by theme changes.

Click **Customize** to define or modify a custom color theme. Changes to a customized theme affect all sections and slices using those theme colors.

### Font Theme

Choose a font theme for your report. Font themes control the fonts used in text, headers, and chart labels. You can switch font themes at any time.

## Header Style

Select a header style preset or choose **No Header** to remove the header entirely. The header displays the report icon, title, and description.

Click the paint drop icon to adjust the header background color or image.

* **Customize** — define or modify a custom color theme. Any other section or slice using the original theme colors will change to the new colors.
* **Custom** — add a color outside of the color theme. Using a custom color will not affect sections or slices using a theme color.

{% hint style="info" %}
If you want to create a more custom header, set the Header Style to "No Header" and use the [Headline slice](slices/charts/headline.md) to design a custom header.
{% endhint %}

## Editor controls

By default, changes you make in the editing panel are automatically loaded to the draft report. Toggle **Editor controls** off to disable this behavior. When turned off, you will need to click Reload Changes in the draft report before your changes appear.

{% hint style="info" %}
Changes to report settings must be shared before they will appear on the home page or in the published report.
{% endhint %}
