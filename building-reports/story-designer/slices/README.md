# Slices

Slices are the basic building blocks of your story. Slices are added to [sections](../sections.md). Each slice can have text either by itself or with media (image or video) or a [chart](charts/).

## Adding, duplicating, and deleting slices

To add a slice to an empty section, hover where you want the slice to be added, click the + button, and select the slice type from the dropdown list.

<div><figure><img src="../../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure></div>

Rather than adding a brand new slice, it may be easier to duplicate and modify an existing slice. To duplicate a slice, select the three-dot icon next to the slice and then select **Duplicate**. The duplicated slice will appear directly below the original slice.

To delete a slice, select the three-dot icon and then select **Delete**.

<figure><img src="../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

## Adding slice content

Every slice can have text and either a chart or media (i.e., image or video). To add text to a slice, type in the draft report where you want the text to appear and use the text editor to style the text.

<figure><img src="../../../.gitbook/assets/image (574).png" alt=""><figcaption><p>Text is added and styled directly in the draft report</p></figcaption></figure>

Until you configure your chart, the chart will display a "This slice has potential" message.

<figure><img src="../../../.gitbook/assets/image (4).png" alt=""><figcaption><p>This message will display if the chart has not been configured</p></figcaption></figure>

### Linking to a page

For reports with [multiple pages](../report-settings.md#manage-pages), you can create links in slice text that navigate to another page in the same report. In the text editor, open the link dialog and look for the **Link to a Page** section, which lists all pages in the report. Click a page name to create the link.

**\[Screenshot: The link editor dialog showing the "Link to a Page" section with page names listed]**

Links created this way navigate to the target page without a full browser reload and carry forward any active filter selections. This means viewers keep their current context as they move between pages.

{% hint style="info" %}
If you manually add query parameters or hash fragments to the link URL, the link will open in a new browser tab instead of navigating within the report.
{% endhint %}

## Common slice configuration options

Each slice type has a specific set of configuration options, but the following options are shared by multiple slice types:

### Configure tab

**Data Table**. A dropdown will display if there is more than one data source connected to the report. The slice will use the selected data source.

**Hide if no data**. If turned on, the entire slice will be hidden if all data has been filtered out. If turned off, the slice will display with a message notifying the viewer that all data has been filtered out.

**Selections**. You can select whether user selections are allowed and, if so, how many. You can also specify how selected items will be used. The options are:

* _as Filters_. This is the default. Selections will filter downstream slices.
* _as Variables_. Selections will not filter downstream slices. Instead, the selected values will be saved as variables that can be used in defining ingredients.
* _as Filters and Variables_. Selections will both filter downstream slices and be saved as variables that can be used in defining ingredients.

{% hint style="success" %}
Variables are very powerful. Learn more [here](selections-as-variables.md).
{% endhint %}

**Receive filters from another Page**. For reports with [multiple pages](../report-settings.md#manage-pages), this toggle controls whether the slice applies matching filter selections from the page the viewer navigated from. When turned on, selections from the source page are automatically applied if the filter dimensions match. This toggle only appears for reports with more than one page.

### Style tab

**Display options**. These toggles control which parts of a slice are visible to viewers.

* **Hidden**. Hides the entire slice from viewers. When this is turned on, all other display toggles are hidden. This is useful when you want a slice to set [variables](selections-as-variables.md) without showing anything in the report.
* **Show Title**. Shows or hides the slice header. On by default.
* **Show Chart**. Shows or hides the chart or main content. On by default. The label varies by slice type — for example, it reads "Show Filters" on a Filter slice.
* **Show Filter Pill**. Shows or hides a filter pill for the slice. On by default for most chart types. When you want filter behavior without displaying the full chart, turn off **Show Chart** and leave **Show Filter Pill** on. This option is not available on Chooser, Filter, or Report Navigation slices.
* **Show as Download Button**. Available on Table slices only. Replaces the table with a download button that lets viewers export the data. Turning this on automatically hides the chart and filter pill.

{% hint style="info" %}
Combining **Hidden** with [variables](selections-as-variables.md) and [dynamic text](dynamic-text.md) is a powerful pattern — use a hidden slice to capture selections as variables, then reference those variables in dynamic text or ingredient formulas elsewhere in the report.
{% endhint %}

**Chart/Media position.** If a slice has a chart (or media), there are four layout options that control how the chart (or media) will appear in relation to the slice text.

<table data-header-hidden><thead><tr><th width="169.88425660364788">Layout button</th><th>Description</th></tr></thead><tbody><tr><td><img src="../../../.gitbook/assets/arrow-down-solid.svg" alt="" data-size="line"> Below text</td><td>The slice text will display above the chart/media. This is the default layout.</td></tr><tr><td><img src="../../../.gitbook/assets/arrow-up-solid.svg" alt="" data-size="line"> Above text</td><td>The chart/media will display above the slice text.</td></tr><tr><td><img src="../../../.gitbook/assets/arrow-right-solid.svg" alt="" data-size="line"> Right of text</td><td>The slice text will display on the left, and the chart/media will display on the right.</td></tr><tr><td><img src="../../../.gitbook/assets/arrow-left-solid.svg" alt="" data-size="line"> Left of text</td><td>The chart/media will display on the left, and the slice text will display on the right.</td></tr></tbody></table>

**Show legend**. Some charts have legends. Turn this off to hide the legend.

**Show notes**. Some charts have notes. Turn this off to hide the notes.

**Filters applied footnote**. If turned on, a footnote will display in each slice showing which filters are being applied to the slice.

### Slice slugs

Each slice has a unique id that is called a "slug". Slices with text only or media will have a slug like **Text1** or **Text5**. Slices with charts will have a slug like **Table1** or **Scatterplot2**. You can see the slice slug in the draft app as a badge in the top-left corner of the slice on hover. Clicking the badge in the draft app will scroll the slice into view in the editing panel.

<figure><img src="../../../.gitbook/assets/image (590).png" alt=""><figcaption></figcaption></figure>

Slices with charts also show their slug in the editing panel as a badge. The slug for charts is often used in dynamic text \[and other places]. To copy the slug, click the @ button next to the badge.

<figure><img src="../../../.gitbook/assets/image (5).png" alt=""><figcaption><p>Click the <strong>@</strong> button to copy the slice slug</p></figcaption></figure>

### Slice backgrounds

By default, slices have a transparent background (revealing the section background color). To adjust the slice background color, click the paint drop icon, and select the desired theme color. If you have a specific color in mind, you can enter the hex code for that color after clicking the **Custom** button. You can also click the **Customize** button to modify the color theme.

## Reordering slices

To reorder slices, drag and drop the slice where you want it to display. You can reorder slices within a section and move slices to different sections.
