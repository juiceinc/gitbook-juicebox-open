# Advanced formats

The [most commonly used formats](../adding-ingredients/ingredient-formats.md) are available in the ingredient editor. But if you need to use a different format, you can [add an advanced ingredient](../adding-ingredients/#adding-an-advanced-ingredient) and adjust the `format:` component within the advanced ingredient definition.

## Advanced number formats

You can use  [number formats](https://github.com/d3/d3-format) to adjust how numbers display in your story. For example, let's say you want to display `Obese %` with 1 decimal. Because the ingredient editor does not include an option to display a percent with 1 decimal, you will need to do this as an advanced ingredient, like so:

![Set format to a percent with 1 decimal](../../../.gitbook/assets/image%20%28194%29.png)

Number formats in juicebox have the following parts

```text
"<prefix>"<positive_format>;<negative_format>;<zero_format>;<null_format>"<suffix>"
```

Every part of the number format is optional except for the positive\_format . If only the positive\_format is given, it will be used for all numbers.

#### prefix and suffix

`Prefix` can be any text that appears before the number, while `suffix` will appear after the number. **They must be between double quotes.** Prefix and suffix support a special command `pluralize(singular, plural)` which chooses between two strings. If the number being formatted is one, the singular value will be displayed, otherwise the plural value will be displayed.

| Format | Number | Result |
| :--- | :--- | :--- |
| `"Total sales: ".0f` | 1234 | `Total sales: 1234` |
| `,.0f" days until Christmas"` | 1234 | `1,234 days until Christmas` |
| `,.0f"pluralize( student, students)"` | 4 | `4 students` |
| `,.0f"pluralize( student, students)"` | 1 | `1 student` |

#### formats

This format documentation is adapted from [https://github.com/d3/d3-format/blob/master/README.md\#format](https://github.com/d3/d3-format/blob/master/README.md#format)

Formats have the following parts

```text
[[fill]align][sign][symbol][0][width][,][.precision][type]
```

You can optionally provide extra formats for negative, zero, or null values. The `positive_format` will be used when other formats aren’t provided.

**\[fill\[align\]\]**

The fill can be any character. The presence of a fill character is signaled by the align character following it, which must be one of the following:

| `Align character` | Description |
| :--- | :--- |
| `>` | Forces the field to be right-aligned within the available space. \(Default behavior\). |
| `<` | Forces the field to be left-aligned within the available space. |
| `^` | Forces the field to be centered within the available space. |
| `=` | like `>`, but with any sign and symbol to the left of any padding. |

**\[sign\]**

The sign can be:

| `Sign character` | Description |
| :--- | :--- |
| `-` | nothing for positive and a minus sign for negative. \(Default behavior.\) |
| `+` | a plus sign for positive and a minus sign for negative. |
| `(` | nothing for positive and parentheses for negative. |
| `SPACE` | a space for positive and a minus sign for negative. |

**\[symbol\]**

The symbol can be

| `Symbol character` | Description |
| :--- | :--- |
| `$` | apply currency symbols per the locale definition. |
| `#` | for binary, octal, or hexadecimal notation, prefix by 0b, 0o, or 0x, respectively. |

**\[0\]**

The zero `(0)` option enables zero-padding; this implicitly sets fill to 0 and align to =. The width defines the minimum field width; if not specified, then the width will be determined by the content. The comma \(,\) option enables the use of a group separator, such as a comma for thousands.

**\[width\] and \[precision\]**

Depending on the type, the precision either indicates the number of digits that follow the decimal point \(types f and %\), or the number of significant digits \(types ​, e, g, r, s and p\). If the precision is not specified, it defaults to 6 for all types except ​\(none\), which defaults to 12. Precision is ignored for integer formats \(types b, o, d, x, X and c\).

The available type values are:

<table>
  <thead>
    <tr>
      <th style="text-align:left">Format</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left"><code>f</code>
      </td>
      <td style="text-align:left">fixed point notation.</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>s</code>
      </td>
      <td style="text-align:left">
        <p>decimal notation with an SI prefix, rounded to significant digits.</p>
        <p>Note</p>
        <p>Juicebox changes numbers lower than 1 to be formatted with equivalent <code>f</code> notation.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><code>%</code>
      </td>
      <td style="text-align:left">multiply by 100, and then decimal notation with a percent sign.</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>ordinal</code>
      </td>
      <td style="text-align:left">Display as an ordinal number (like 1st, 2nd, 3rd)</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>e</code>
      </td>
      <td style="text-align:left">exponent notation.</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>g</code>
      </td>
      <td style="text-align:left">either decimal or exponent notation, rounded to significant digits.</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>r</code>
      </td>
      <td style="text-align:left">decimal notation, rounded to significant digits.</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>p</code>
      </td>
      <td style="text-align:left">multiply by 100, round to significant digits, and then decimal notation
        with a percent sign.</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>b</code>
      </td>
      <td style="text-align:left">binary notation, rounded to integer.</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>o</code>
      </td>
      <td style="text-align:left">octal notation, rounded to integer.</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>d</code>
      </td>
      <td style="text-align:left">decimal notation, rounded to integer.</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>x</code>
      </td>
      <td style="text-align:left">hexadecimal notation, using lower-case letters, rounded to integer.</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>X</code>
      </td>
      <td style="text-align:left">hexadecimal notation, using upper-case letters, rounded to integer.</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>c</code>
      </td>
      <td style="text-align:left">converts the integer to the corresponding unicode character before printing.</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>(none)</code>
      </td>
      <td style="text-align:left">like g, but trim insignificant trailing zeros.</td>
    </tr>
  </tbody>
</table>

### Number Formatting Examples

This format will show a certain number of digits. If the number is in the thousands, it wil be

#### s, f, $, and % formats

* `.Ns` formats display numbers with `N` digits of precision. This is a good way to display numbers that differ greatly in size.
* `.Nf` displays numbers with a `N` digits after the decimal place.
* Starting your format with a comma will put commas between 000s.

<table>
  <thead>
    <tr>
      <th style="text-align:left">Format</th>
      <th style="text-align:left">Number</th>
      <th style="text-align:left">Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">0.9241</td>
      <td style="text-align:left">0.9</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">0.9123</td>
      <td style="text-align:left">0.9</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">0</td>
      <td style="text-align:left">0.0</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">0.00000000001</td>
      <td style="text-align:left">0.0</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.2s</code>
      </td>
      <td style="text-align:left">0.9123</td>
      <td style="text-align:left">0.91</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.2s</code>
      </td>
      <td style="text-align:left">-0.9123</td>
      <td style="text-align:left">-0.91</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.2s</code>
      </td>
      <td style="text-align:left">0</td>
      <td style="text-align:left">0.00</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.2s</code>
      </td>
      <td style="text-align:left">0.00000000001</td>
      <td style="text-align:left">0.00</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">0.9123</td>
      <td style="text-align:left">0.9</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">0</td>
      <td style="text-align:left">0.0</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">0.00000000001</td>
      <td style="text-align:left">0.0</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.2s</code>
      </td>
      <td style="text-align:left">0</td>
      <td style="text-align:left">0.00</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">0.1234567</td>
      <td style="text-align:left">0.1</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">1.234567</td>
      <td style="text-align:left">1</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">12.34567</td>
      <td style="text-align:left">10</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">123.4567</td>
      <td style="text-align:left">100</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">1234.567</td>
      <td style="text-align:left">1K</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">12345.67</td>
      <td style="text-align:left">10K</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">123456.7</td>
      <td style="text-align:left">100K</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">1234567</td>
      <td style="text-align:left">1M</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">12345678</td>
      <td style="text-align:left">10M</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>$.1s</code>
      </td>
      <td style="text-align:left">12345678</td>
      <td style="text-align:left">$10M</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">123456789</td>
      <td style="text-align:left">100M</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">1234567891</td>
      <td style="text-align:left">1B</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">12345678912</td>
      <td style="text-align:left">10B</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.3s</code>
      </td>
      <td style="text-align:left">0.1234567</td>
      <td style="text-align:left">0.123</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.3s</code>
      </td>
      <td style="text-align:left">1.234567</td>
      <td style="text-align:left">1.23</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>$.3s</code>
      </td>
      <td style="text-align:left">1.234567</td>
      <td style="text-align:left">$1.23</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.3s</code>
      </td>
      <td style="text-align:left">12.34567</td>
      <td style="text-align:left">12.3</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.3s</code>
      </td>
      <td style="text-align:left">123.4567</td>
      <td style="text-align:left">123</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.3s</code>
      </td>
      <td style="text-align:left">1234.567</td>
      <td style="text-align:left">1.23K</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.3s</code>
      </td>
      <td style="text-align:left">12345.67</td>
      <td style="text-align:left">12.3K</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>$.3s</code>
      </td>
      <td style="text-align:left">12345.67</td>
      <td style="text-align:left">$12.3K</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.3s</code>
      </td>
      <td style="text-align:left">123456.7</td>
      <td style="text-align:left">123K</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.3s</code>
      </td>
      <td style="text-align:left">1234567</td>
      <td style="text-align:left">1.23M</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.3s</code>
      </td>
      <td style="text-align:left">12345678</td>
      <td style="text-align:left">12.3M</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.3s</code>
      </td>
      <td style="text-align:left">123456789</td>
      <td style="text-align:left">123M</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.3s</code>
      </td>
      <td style="text-align:left">1234567891</td>
      <td style="text-align:left">1.23B</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.3s</code>
      </td>
      <td style="text-align:left">12345678912</td>
      <td style="text-align:left">12.3B</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">0.9</td>
      <td style="text-align:left">0.9</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">-0.9</td>
      <td style="text-align:left">-0.9</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">0</td>
      <td style="text-align:left">0.0</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">100</td>
      <td style="text-align:left">100</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">1100</td>
      <td style="text-align:left">1K</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1s</code>
      </td>
      <td style="text-align:left">10000</td>
      <td style="text-align:left">10K</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>,.3s</code>
      </td>
      <td style="text-align:left">0.000123</td>
      <td style="text-align:left">0.000</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>,.3s</code>
      </td>
      <td style="text-align:left">0.001234</td>
      <td style="text-align:left">0.001</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>,.2s</code>
      </td>
      <td style="text-align:left">0.012345</td>
      <td style="text-align:left">0.01</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>,.4s</code>
      </td>
      <td style="text-align:left">0.12345</td>
      <td style="text-align:left">0.1235</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>,.3s</code>
      </td>
      <td style="text-align:left">1.2345</td>
      <td style="text-align:left">1.23</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>,.3s</code>
      </td>
      <td style="text-align:left">123</td>
      <td style="text-align:left">123</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>,.2s</code>
      </td>
      <td style="text-align:left">12345.56</td>
      <td style="text-align:left">12K</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>,.2s</code>
      </td>
      <td style="text-align:left">1234567</td>
      <td style="text-align:left">1.2M</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>,.2s</code>
      </td>
      <td style="text-align:left">1234567890</td>
      <td style="text-align:left">1.2B</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>,.2s</code>
      </td>
      <td style="text-align:left">123456789012</td>
      <td style="text-align:left">120B</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>,.2s</code>
      </td>
      <td style="text-align:left">1234567890123</td>
      <td style="text-align:left">1.2T</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.2f</code>
      </td>
      <td style="text-align:left">1203</td>
      <td style="text-align:left">1203.00</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.2f</code>
      </td>
      <td style="text-align:left">-1203</td>
      <td style="text-align:left">-1203.00</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>,.2f</code>
      </td>
      <td style="text-align:left">-1203</td>
      <td style="text-align:left">
        <p>-1,203.00</p>
        <p>Note</p>
        <p>Note the commas between the 000s caused by the starting &#x2018;,&#x2019;</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.2f</code>
      </td>
      <td style="text-align:left">null</td>
      <td style="text-align:left">0.00</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.2f</code>
      </td>
      <td style="text-align:left">NaN</td>
      <td style="text-align:left">NaN</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.1%</code>
      </td>
      <td style="text-align:left">.12345</td>
      <td style="text-align:left">12.3%</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.2%</code>
      </td>
      <td style="text-align:left">.12345</td>
      <td style="text-align:left">12.34%</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.2%</code>
      </td>
      <td style="text-align:left">123.45</td>
      <td style="text-align:left">12345.00%</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>,.2%</code>
      </td>
      <td style="text-align:left">123.45</td>
      <td style="text-align:left">12,345.00%</td>
    </tr>
  </tbody>
</table>

#### Examples of positive, negative, zero and null formats

| Format | Number | Result |
| :--- | :--- | :--- |
| `.2s;.3s` | 1234 | 1.2K |
| `.2s;.3s` | -1234 | -1.23K |
| `.2s;.3s;.4s` | 0 | 0.0000 |
| `,.0f" days from now";|,.0f|" days ago";"today";"--unknown--"` | 1234 | 1,234 days from now |
| `,.0f" days from now";|,.0f|" days ago";"today";"--unknown--"` | -1234 | 1,234 days ago |
| `,.0f" days from now";|,.0f|" days ago";"today";"--unknown--"` | 0 | today |
| `,.0f" days from now";|,.0f|" days ago";"today";"--unknown--"` | null | –unknown– |

#### Absolute values

<table>
  <thead>
    <tr>
      <th style="text-align:left">Format</th>
      <th style="text-align:left">Number</th>
      <th style="text-align:left">Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left"><code>\|.2s\|</code>
      </td>
      <td style="text-align:left">1234</td>
      <td style="text-align:left">1.2K</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>\|.2s\|</code>
      </td>
      <td style="text-align:left">-1234</td>
      <td style="text-align:left">1.2K</td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.2s;&quot;negative &quot;\|.3s\|</code>
      </td>
      <td style="text-align:left">-1234</td>
      <td style="text-align:left">
        <p>negative 1.23K</p>
        <p>Note</p>
        <p>Negative formats can have their own prefixes.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><code>.2s;\|.3s\|</code>
      </td>
      <td style="text-align:left">1234</td>
      <td style="text-align:left">1.2K</td>
    </tr>
  </tbody>
</table>

#### Ordinal values

Using "ordinal" as a format will 

| Format | Number | Result |
| :--- | :--- | :--- |
| `ordinal` | 1 | 1st |
| `ordinal` | 2 | 2nd |
| `ordinal` | 3 | 3rd |
| `ordinal` | 4 | 4th |
| `ordinal` | 23 | 23rd |
| `ordinal` | 24 | 24th |
| `ordinal` | 100 | 100th |
| `ordinal` | 101 | 101st |

## Advanced date formats

You can use [date formats](https://strftime.org/) to adjust how dates display in your story. For example, let's say you want to display `Year Dates` like "January 1, 2018" \(full month and unpadded day\). If the ingredient editor did not include an option to display this date format, could do this as an advanced ingredient, like so:

![Set date format to full month and unpadded day](../../../.gitbook/assets/image%20%28233%29.png)

![Set date format to full month and unpadded day](../../../.gitbook/assets/image%20%28233%29.png)

And here are the underlying components:

```text
kind: Dimension
field: Year_Date
singular: Dates
format: '%B %e, %Y'
```

### Date Formatting Examples

| Format | Number | Result |
| :--- | :--- | :--- |
| `<%Y-%m-%d>` | dt | 2014-01-01 |
| `<%Y-%m-%d>` | dt | 2014-01-01 |
| `<%Y-%m-%d>;;;"NODATA"` | null | NODATA |
| `"prefix"<%Y-%m-%d>` | dt | prefix2014-01-01 |
| `"The "<%Y-%m-%d>" Conundrum"` | dt | The 2014-01-01 Conundrum |
| `<%Y-%m-%d>"suffix"` | dt | 2014-01-01suffix |

#### 

