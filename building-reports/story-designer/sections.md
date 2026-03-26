---
description: Sections group slices and control layout, spacing, and backgrounds.
---

# Sections

Sections are groups of slices within a report. Each section has its own layout, spacing, and background settings. You manage sections from the editing panel on the left side of the editing view.

## Adding a section

Click the **+New Section** button in the editing panel. You will be prompted to add a slice to the new section — select any chart type to get started. You can always change or delete the slice later.

## Section Config

Click a **section badge** (the section name button in the editing panel) to open the Section Config panel. From here you can:

**Rename the section**. Click the pencil icon next to the section name at the top of the panel.

**Show or hide the section**. Use the **Show this section** toggle. When toggled off, the section will not display in the published report.

## Section Style

The Section Config panel also includes **Section Style** settings that control how slices are arranged within the section.

### Layout

The **Layout** dropdown determines how slices are positioned within the section:

* **Stacked** (default) — each slice occupies its own row, one on top of the next.
* **Columns** — all slices are placed side by side in a single row with equal widths.
* **Large Slides** — each slice takes up the full viewport height, creating a scroll-through presentation effect.
* **First as header, then columns** — the first slice spans the full width as a header, and the remaining slices are arranged in equal-width columns below it.
* **First on left, then stacked** — the first slice occupies the left column spanning all rows, and the remaining slices are stacked in the right column.
* **Custom layout** — define a custom CSS grid layout. See [Custom layout](#custom-layout) below.

### Custom layout <a href="#custom-layout" id="custom-layout"></a>

When you select **Custom layout**, a code editor appears where you can enter a CSS `grid-template` value. This gives you full control over how slices are positioned and sized within the section.

Use **chart reference names** (the slice names shown in the editing panel, e.g., `Headline1`, `Filters1`) as grid area names. Each slice is placed in the grid area that matches its reference name.

For example, to place a headline spanning the full width with two charts side by side below it:

```
"Headline1 Headline1" auto
"Bar1 Trend1" 1fr
/ 1fr 1fr
```

You can control:

* **Column spans** — repeat a name across columns in a row (e.g., `"Headline1 Headline1"`)
* **Row spans** — repeat a name across rows
* **Row heights** — specify sizes after row definitions (e.g., `auto`, `1fr`, `100px`, `100vh`)
* **Column widths** — specify sizes after `/` (e.g., `/ 2fr 1fr`)

The editor starts with a default template based on your current slices. Click **Save** to apply your changes.

{% hint style="info" %}
Custom layout uses CSS grid-template syntax. [Learn more about CSS grid layouts on MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template).
{% endhint %}

### Spacing style

The **Spacing style** dropdown controls the gap between slices within the section:

* **No space** — slices are flush against each other with no gap.
* **Dense** — a small gap between slices.
* **Spacious** — a larger gap between slices.

When spacing is set to Dense or Spacious, a **Shadows** toggle appears. Turn this on to add a subtle shadow around each slice.

### Independent section

Toggle **Independent section** on to isolate this section from the rest of the report. When enabled:

* Selections made in this section do **not** affect slices in other sections.
* Selections made in other sections do **not** affect slices in this section.
* Slices **within** the independent section still filter each other normally.

This is useful when you want to show different views of the data side by side without having them interfere with each other.

## Section Background

Click the **paint drop icon** next to the section badge in the editing panel to adjust the section background.

**Background image**. Drag and drop a `.jpg` or `.png` file into the media area, or click **Add Media** to upload an image.

**Background color**. Choose from theme background colors, preset colors, or add a custom color.

* **Customize** — define or modify a custom color theme. Any other section or slice using the original theme colors will change to the new colors.
* **Custom** — add a color outside of the color theme. Using a custom color will not affect sections or slices using a theme color.

If you choose a dark background, Juicebox will invert the visualization and text colors automatically.

## Deleting a section

Click the **...** menu next to the section badge and select **Delete Section**.

## Collapsing and reordering sections

To reorder a section, drag it by the handle next to the section badge and drop it where you want it. Because sections can get long, it helps to collapse sections first — click the section header arrow to collapse or expand it.
