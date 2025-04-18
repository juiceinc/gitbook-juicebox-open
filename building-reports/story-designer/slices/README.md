# Slices

Slices are the basic building blocks of your story. Slices are added to [sections](../#sections). Each slice can have text either by itself or with media (image or video) or a [chart](charts/).

## Adding, duplicating, and deleting slices

To add a slice to an empty section, click on the section header and select the slice type from the list. To add a slice to a section that has one or more slices, click the **+** button where you want the new slice to appear and select the slice type from the dropdown.

<figure><img src="../../../.gitbook/assets/image (571).png" alt=""><figcaption><p>Add a new slice</p></figcaption></figure>

Rather than adding a brand new slice, it may be easier to duplicate and modify an existing slice. To duplicate a slice, select the gear icon and then select **Duplicate**. The duplicated slice will appear directly below the original slice.&#x20;

<figure><img src="../../../.gitbook/assets/image (572).png" alt=""><figcaption><p>Duplicate a slice</p></figcaption></figure>

To delete a slice, select the gear icon and then select **Delete**.&#x20;

<figure><img src="../../../.gitbook/assets/image (573).png" alt=""><figcaption><p>Delete a slice</p></figcaption></figure>

## Adding slice content

Every slice can have text and either a chart or media (i.e., image or video). To add text to a slice, type in the draft report where you want the text to appear and use the text editor to style the text.

<figure><img src="../../../.gitbook/assets/image (574).png" alt=""><figcaption><p>Text is added and styled directly in the draft report</p></figcaption></figure>

To add a chart to a Text slice, select the **Add Chart** button and select the desired [chart](charts/) from the list.&#x20;

<figure><img src="../../../.gitbook/assets/image (575).png" alt=""><figcaption><p>Click <strong>Add Chart</strong> to add a chart to a Text slice</p></figcaption></figure>

Until you configure your chart, the chart will display an error message.

<figure><img src="../../../.gitbook/assets/image (576).png" alt=""><figcaption><p>An error message will display if the chart has not been configured</p></figcaption></figure>

To add an image or video to a slice, select the **Add Media** button and upload your own image, find an image on Unsplash, or a paste a URL to a YouTube or Vimeo video.&#x20;

If you want to delete the chart or media content in a slice and go back to a Text slice, click the trash can icon.

<figure><img src="../../../.gitbook/assets/image (577).png" alt=""><figcaption><p>Click the trash can icon to delete the chart or media content</p></figcaption></figure>

## Common slice configuration options

Each slice type has a specific set of configuration options, but the following options are shared by multiple slice types:&#x20;

### Configure tab

**Data Table**. A dropdown will display if there is more than one data source connected to the report. The slice will use the selected data source.

**Hide if no data**. If turned on, the entire slice will be hidden if all data has been filtered out. If turned off, the slice will display with a message notifying the viewer that all data has been filtered out.&#x20;

**Selections**. You can select whether user selections are allowed and, if so, how many. You can also specify how selected items will be used. The options are:

* _as Filters_. This is the default. Selections will filter downstream slices.&#x20;
* _as Variables_. Selections will not filter downstream slices. Instead, the selected values will be saved as variables that can be used in defining ingredients.&#x20;
* _as Filters and Variables_. Selections will both filter downstream slices and be saved as variables that can be used in defining ingredients.&#x20;

{% hint style="success" %}
Variables are very powerful. Learn more here.&#x20;
{% endhint %}

### Style tab

**Display**. You can select which elements of a slice should display.&#x20;

{% hint style="info" %}
One of the options is **Hide all**. This option can be used together with Variables and Dynamic text. \[Link to a page with examples.]&#x20;
{% endhint %}

**Chart/Media position.** If a slice has a chart (or media), there are four layout options that control how the chart (or media) will appear in relation to the slice text.&#x20;

<table data-header-hidden><thead><tr><th width="169.88425660364788">Layout button</th><th>Description</th></tr></thead><tbody><tr><td><img src="../../../.gitbook/assets/arrow-down-solid.svg" alt="" data-size="line">  Below text</td><td>The slice text will display above the chart/media. This is the default layout.</td></tr><tr><td><img src="../../../.gitbook/assets/arrow-up-solid.svg" alt="" data-size="line">  Above text</td><td>The chart/media will display above the slice text. </td></tr><tr><td><img src="../../../.gitbook/assets/arrow-right-solid.svg" alt="" data-size="line">  Right of text</td><td>The slice text will display on the left, and the chart/media will display on the right. </td></tr><tr><td><img src="../../../.gitbook/assets/arrow-left-solid.svg" alt="" data-size="line">  Left of text </td><td>The chart/media will display on the left, and the slice text will display on the right. </td></tr></tbody></table>

**Show legend**. Some charts have legends. Turn this off to hide the legend.

**Show notes**. Some charts have notes. Turn this off to hide the notes.&#x20;

**Filters applied footnote**. If turned on, a footnote will display in each slice showing which filters are being applied to the slice.&#x20;

### Slice slugs

Each slice has a unique id that is called a "slug". Slices with text only or media will have a slug like **Text1** or **Text5**. Slices with charts will have a slug like **Table1** or **Scatterplot2**. You can see the slice slug in the draft app as a badge in the top-left corner of the slice on hover. Clicking the badge in the draft app will scroll the slice into view in the editing panel.&#x20;

<figure><img src="../../../.gitbook/assets/image (590).png" alt=""><figcaption></figcaption></figure>

Slices with charts also show their slug in the editing panel as a badge. The slug for charts is often used in dynamic text \[and other places]. To copy the slug, click the @ button next to the badge.&#x20;

<figure><img src="../../../.gitbook/assets/image (589).png" alt=""><figcaption><p>Click the <strong>@</strong> button to copy the slice slug</p></figcaption></figure>

### Slice backgrounds

By default, slices have a transparent background (revealing the section background color). To adjust the slice background color, click the paint drop icon, and select the desired theme color. If you have a specific color in mind, you can enter the hex code for that color after clicking the **Custom** button. You can also click the **Customize** button to modify the color theme.&#x20;

## Reordering slices

To reorder slices, drag and drop the slice where you want it to display. You can reorder slices within a section and move slices to different sections.
