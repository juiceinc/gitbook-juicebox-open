# Number formats

To control how numbers are displayed in the report, you can specify a format. For example, let's say you have a dimension called **Budget**. Representative values for **Budget** in your data are `3231.447` and `0.5264`. You probably do not want to display the unformatted values in your report. Therefore, you will want to specify a number format in the ingredient editor.&#x20;

<figure><img src="../../../../.gitbook/assets/image (517).png" alt=""><figcaption><p>Select a number format</p></figcaption></figure>

The format specified in the ingredient editor will determine how the value will display in your report. The following standard formats are available:&#x20;

<table data-header-hidden><thead><tr><th width="200">format label</th><th width="150">d3 equivalent</th><th width="199.2591605596269">How value3231.447will display</th><th>How value 0.5264 will display</th></tr></thead><tbody><tr><td><strong>format label</strong></td><td><strong>d3 equivalent</strong></td><td><strong>How value<code>3231.447</code> will display</strong></td><td><strong>How value <code>0.5264</code> will display</strong></td></tr><tr><td># 2 Decimals</td><td><code>,.2f</code></td><td>3,231.45</td><td>0.53</td></tr><tr><td># Rounded</td><td><code>,.0f</code></td><td>3,231</td><td>1</td></tr><tr><td># 3 Sig figs</td><td><code>.3s</code></td><td>3.23K</td><td>0.526</td></tr><tr><td>$ 2 Decimals</td><td><code>$.2f</code></td><td>$3,231.45</td><td>$0.53</td></tr><tr><td>$ Rounded</td><td><code>$,.0f</code></td><td>$3,231</td><td>$1</td></tr><tr><td>$ 3 Sig figs</td><td><code>$.3s</code></td><td>$3.23K</td><td>$0.526</td></tr><tr><td>% 2 Decimals</td><td><code>,.2%</code></td><td>323,144.70%</td><td>52.64%</td></tr><tr><td>% Rounded</td><td><code>,.0%</code></td><td>323,145%</td><td>53%</td></tr></tbody></table>

If you want to apply a number format other than one in the dropdown, you can do so by entering the custom format in the Number format box. For example, let's say you want to display **Average Rating** with 1 decimal. You can do this by entering `.1f`, like so:&#x20;

<figure><img src="../../../../.gitbook/assets/image (518).png" alt=""><figcaption><p>Enter a custom number format</p></figcaption></figure>

Number formats in Juicebox have the following parts

```
"<prefix>"<positive_format>;<negative_format>;<zero_format>;<null_format>"<suffix>"
```

Every part of the number format is optional except for the positive\_format . If only the positive\_format is given, it will be used for all numbers.

#### prefix and suffix

`Prefix` can be any text that appears before the number, while `suffix` will appear after the number. **They must be between double quotes.** Prefix and suffix support a special command `pluralize(singular, plural)` which chooses between two strings. If the number being formatted is one, the singular value will be displayed, otherwise the plural value will be displayed.

| Format                                | Number | Result                       |
| ------------------------------------- | ------ | ---------------------------- |
| `"Total sales: ".0f`                  | 1234   | `Total sales: 1234`          |
| `,.0f" days until Christmas"`         | 1234   | `1,234 days until Christmas` |
| `,.0f"pluralize( student, students)"` | 4      | `4 students`                 |
| `,.0f"pluralize( student, students)"` | 1      | `1 student`                  |

#### formats

This format documentation is adapted from [d3 formats](https://d3js.org/d3-format).

Formats have the following parts:

```
[[fill]align][sign][symbol][0][width][,][.precision][type]
```

You can optionally provide extra formats for negative, zero, or null values. The `positive_format` will be used when other formats aren’t provided.

**\[fill\[align]]**

The fill can be any character. The presence of a fill character is signaled by the align character following it, which must be one of the following:

| `Align character` | Description                                                                          |
| ----------------- | ------------------------------------------------------------------------------------ |
| `>`               | Forces the field to be right-aligned within the available space. (Default behavior). |
| `<`               | Forces the field to be left-aligned within the available space.                      |
| `^`               | Forces the field to be centered within the available space.                          |
| `=`               | like `>`, but with any sign and symbol to the left of any padding.                   |

**\[sign]**

The sign can be:

| `Sign character` | Description                                                             |
| ---------------- | ----------------------------------------------------------------------- |
| `-`              | nothing for positive and a minus sign for negative. (Default behavior.) |
| `+`              | a plus sign for positive and a minus sign for negative.                 |
| `(`              | nothing for positive and parentheses for negative.                      |
| `SPACE`          | a space for positive and a minus sign for negative.                     |

**\[symbol]**

The symbol can be

| `Symbol character` | Description                                                                        |
| ------------------ | ---------------------------------------------------------------------------------- |
| `$`                | apply currency symbols per the locale definition.                                  |
| `#`                | for binary, octal, or hexadecimal notation, prefix by 0b, 0o, or 0x, respectively. |

**\[0]**

The zero `(0)` option enables zero-padding; this implicitly sets fill to 0 and align to =. The width defines the minimum field width; if not specified, then the width will be determined by the content. The comma (,) option enables the use of a group separator, such as a comma for thousands.

**\[width] and \[precision]**

Depending on the type, the precision either indicates the number of digits that follow the decimal point (types f and %), or the number of significant digits (types ​, e, g, r, s and p). If the precision is not specified, it defaults to 6 for all types except ​(none), which defaults to 12. Precision is ignored for integer formats (types b, o, d, x, X and c).

The available type values are:

| Format    | Description                                                                                                                                                                               |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `f`       | fixed point notation.                                                                                                                                                                     |
| `s`       | <p>decimal notation with an SI prefix, rounded to significant digits.</p><p>Note</p><p>Juicebox changes numbers lower than 1 to be formatted with equivalent <code>f</code> notation.</p> |
| `%`       | multiply by 100, and then decimal notation with a percent sign.                                                                                                                           |
| `ordinal` | Display as an ordinal number (like 1st, 2nd, 3rd)                                                                                                                                         |
| `e`       | exponent notation.                                                                                                                                                                        |
| `g`       | either decimal or exponent notation, rounded to significant digits.                                                                                                                       |
| `r`       | decimal notation, rounded to significant digits.                                                                                                                                          |
| `p`       | multiply by 100, round to significant digits, and then decimal notation with a percent sign.                                                                                              |
| `b`       | binary notation, rounded to integer.                                                                                                                                                      |
| `o`       | octal notation, rounded to integer.                                                                                                                                                       |
| `d`       | decimal notation, rounded to integer.                                                                                                                                                     |
| `x`       | hexadecimal notation, using lower-case letters, rounded to integer.                                                                                                                       |
| `X`       | hexadecimal notation, using upper-case letters, rounded to integer.                                                                                                                       |
| `c`       | converts the integer to the corresponding unicode character before printing.                                                                                                              |
| `(none)`  | like g, but trim insignificant trailing zeros.                                                                                                                                            |

### Number Formatting Examples

This format will show a certain number of digits. If the number is in the thousands, it wil be

#### s, f, $, and % formats

* `.Ns` formats display numbers with `N` digits of precision. This is a good way to display numbers that differ greatly in size.
* `.Nf` displays numbers with a `N` digits after the decimal place.
* Starting your format with a comma will put commas between 000s.

| Format | Number        | Result                                                                                        |
| ------ | ------------- | --------------------------------------------------------------------------------------------- |
| `.1s`  | 0.9241        | 0.9                                                                                           |
| `.1s`  | 0.9123        | 0.9                                                                                           |
| `.1s`  | 0             | 0.0                                                                                           |
| `.1s`  | 0.00000000001 | 0.0                                                                                           |
| `.2s`  | 0.9123        | 0.91                                                                                          |
| `.2s`  | -0.9123       | -0.91                                                                                         |
| `.2s`  | 0             | 0.00                                                                                          |
| `.2s`  | 0.00000000001 | 0.00                                                                                          |
| `.1s`  | 0.9123        | 0.9                                                                                           |
| `.1s`  | 0             | 0.0                                                                                           |
| `.1s`  | 0.00000000001 | 0.0                                                                                           |
| `.2s`  | 0             | 0.00                                                                                          |
| `.1s`  | 0.1234567     | 0.1                                                                                           |
| `.1s`  | 1.234567      | 1                                                                                             |
| `.1s`  | 12.34567      | 10                                                                                            |
| `.1s`  | 123.4567      | 100                                                                                           |
| `.1s`  | 1234.567      | 1K                                                                                            |
| `.1s`  | 12345.67      | 10K                                                                                           |
| `.1s`  | 123456.7      | 100K                                                                                          |
| `.1s`  | 1234567       | 1M                                                                                            |
| `.1s`  | 12345678      | 10M                                                                                           |
| `$.1s` | 12345678      | $10M                                                                                          |
| `.1s`  | 123456789     | 100M                                                                                          |
| `.1s`  | 1234567891    | 1B                                                                                            |
| `.1s`  | 12345678912   | 10B                                                                                           |
| `.3s`  | 0.1234567     | 0.123                                                                                         |
| `.3s`  | 1.234567      | 1.23                                                                                          |
| `$.3s` | 1.234567      | $1.23                                                                                         |
| `.3s`  | 12.34567      | 12.3                                                                                          |
| `.3s`  | 123.4567      | 123                                                                                           |
| `.3s`  | 1234.567      | 1.23K                                                                                         |
| `.3s`  | 12345.67      | 12.3K                                                                                         |
| `$.3s` | 12345.67      | $12.3K                                                                                        |
| `.3s`  | 123456.7      | 123K                                                                                          |
| `.3s`  | 1234567       | 1.23M                                                                                         |
| `.3s`  | 12345678      | 12.3M                                                                                         |
| `.3s`  | 123456789     | 123M                                                                                          |
| `.3s`  | 1234567891    | 1.23B                                                                                         |
| `.3s`  | 12345678912   | 12.3B                                                                                         |
| `.1s`  | 0.9           | 0.9                                                                                           |
| `.1s`  | -0.9          | -0.9                                                                                          |
| `.1s`  | 0             | 0.0                                                                                           |
| `.1s`  | 100           | 100                                                                                           |
| `.1s`  | 1100          | 1K                                                                                            |
| `.1s`  | 10000         | 10K                                                                                           |
| `,.3s` | 0.000123      | 0.000                                                                                         |
| `,.3s` | 0.001234      | 0.001                                                                                         |
| `,.2s` | 0.012345      | 0.01                                                                                          |
| `,.4s` | 0.12345       | 0.1235                                                                                        |
| `,.3s` | 1.2345        | 1.23                                                                                          |
| `,.3s` | 123           | 123                                                                                           |
| `,.2s` | 12345.56      | 12K                                                                                           |
| `,.2s` | 1234567       | 1.2M                                                                                          |
| `,.2s` | 1234567890    | 1.2B                                                                                          |
| `,.2s` | 123456789012  | 120B                                                                                          |
| `,.2s` | 1234567890123 | 1.2T                                                                                          |
| `.2f`  | 1203          | 1203.00                                                                                       |
| `.2f`  | -1203         | -1203.00                                                                                      |
| `,.2f` | -1203         | <p>-1,203.00</p><p>Note</p><p>Note the commas between the 000s caused by the starting ‘,’</p> |
| `.2f`  | null          | 0.00                                                                                          |
| `.2f`  | NaN           | NaN                                                                                           |
| `.1%`  | .12345        | 12.3%                                                                                         |
| `.2%`  | .12345        | 12.34%                                                                                        |
| `.2%`  | 123.45        | 12345.00%                                                                                     |
| `,.2%` | 123.45        | 12,345.00%                                                                                    |

#### Examples of positive, negative, zero and null formats

| Format                                                           | Number | Result              |
| ---------------------------------------------------------------- | ------ | ------------------- |
| `.2s;.3s`                                                        | 1234   | 1.2K                |
| `.2s;.3s`                                                        | -1234  | -1.23K              |
| `.2s;.3s;.4s`                                                    | 0      | 0.0000              |
| `,.0f" days from now";\|,.0f\|" days ago";"today";"--unknown--"` | 1234   | 1,234 days from now |
| `,.0f" days from now";\|,.0f\|" days ago";"today";"--unknown--"` | -1234  | 1,234 days ago      |
| `,.0f" days from now";\|,.0f\|" days ago";"today";"--unknown--"` | 0      | today               |
| `,.0f" days from now";\|,.0f\|" days ago";"today";"--unknown--"` | null   | –unknown–           |

#### Absolute values

| Format                     | Number | Result                                                                               |
| -------------------------- | ------ | ------------------------------------------------------------------------------------ |
| `\\|.2s\\|`                | 1234   | 1.2K                                                                                 |
| `\\|.2s\\|`                | -1234  | 1.2K                                                                                 |
| `.2s;"negative "\\|.3s\\|` | -1234  | <p>negative 1.23K</p><p>Note</p><p>Negative formats can have their own prefixes.</p> |
| `.2s;\\|.3s\\|`            | 1234   | 1.2K                                                                                 |

#### Ordinal values

Using "ordinal" as a format will&#x20;

| Format    | Number | Result |
| --------- | ------ | ------ |
| `ordinal` | 1      | 1st    |
| `ordinal` | 2      | 2nd    |
| `ordinal` | 3      | 3rd    |
| `ordinal` | 4      | 4th    |
| `ordinal` | 23     | 23rd   |
| `ordinal` | 24     | 24th   |
| `ordinal` | 100    | 100th  |
| `ordinal` | 101    | 101st  |
