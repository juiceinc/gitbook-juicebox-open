# Number formats

To control how numbers are displayed in the report, you can specify a format. For example, let's say you have the following measure:

![Select a number format from the list](<../../../.gitbook/assets/image (430).png>)

Representative values for `Budget` in your data are `3231.447` and `0.5264`. You probably do not want to display the unformatted value in your report. Therefore, you will want to specify a number format in the `Budget` definition.&#x20;

The format specified in the measure editor will determine how the value will display in your report. The following standard formats are available for measures:&#x20;

<table data-header-hidden><thead><tr><th width="200">format label</th><th width="150">d3 equivalent</th><th width="199.2591605596269">How value3231.447will display</th><th>How value 0.5264 will display</th></tr></thead><tbody><tr><td><strong>format label</strong></td><td><strong>d3 equivalent</strong></td><td><strong>How value<code>3231.447</code> will display</strong></td><td><strong>How value <code>0.5264</code> will display</strong></td></tr><tr><td># 2 Decimals</td><td><code>,.2f</code></td><td>3,231.45</td><td>0.53</td></tr><tr><td># Rounded</td><td><code>,.0f</code></td><td>3,231</td><td>1</td></tr><tr><td># 3 Sig figs</td><td><code>.3s</code></td><td>3.23K</td><td>0.526</td></tr><tr><td>$ 2 Decimals</td><td><code>$.2f</code></td><td>$3,231.45</td><td>$0.53</td></tr><tr><td>$ Rounded</td><td><code>$,.0f</code></td><td>$3,231</td><td>$1</td></tr><tr><td>$ 3 Sig figs</td><td><code>$.3s</code></td><td>$3.23K</td><td>$0.526</td></tr><tr><td>% 2 Decimals</td><td><code>,.2%</code></td><td>323,144.70%</td><td>52.64%</td></tr><tr><td>% Rounded</td><td><code>,.0%</code></td><td>323,145%</td><td>53%</td></tr></tbody></table>

If you want to apply a number format other than one of the standard formats, you can do so by creating an [advanced ingredient](../advanced-ingredients/advanced-formats.md).&#x20;
