# Map

The map chart displays a place dimension as a bubble on a map. Optionally, the bubble can be sized and colored by measures. Adding a slice with a map chart \(i.e., a map slice\) is a good choice when users want to see geographic information.  

## Adding a map slice

To add a map slice:

* select **Map** from the chart list
* select the place dimension you want to display as a bubble on the map
* \(optional\) select a measure to use for the bubble size
* \(optional\) select a measure to use for the bubble color
* select a map style
* \(optional\) add a title

{% hint style="info" %}
The map slice requires that one of your dimensions be a [place dimension](../../data-sources/#dimensions).  A place dimension has associated latitude and longitude fields.
{% endhint %}

{% hint style="warning" %}
For best results, each distinct value of a place dimension should have a distinct latitude-longitude combination. For example, suppose your data contains both`city and state`.  To use the map slice for both cities and states, you will need two place dimensions: 1\) a `Cities` place dimension with`city_latitude and city_longitude`,  and 2\) a `States` place dimension with`state_latitude` and `state_longitude`. Using `city_latitude` and `city_longitude` for the `States` place dimension will show slices aggregated at the city-level because there will be more than one distinct latitude-longitude combination for each state. This is generally not the desired result. 
{% endhint %}

{% embed url="https://www.loom.com/share/f55bf2012b2048219403160c4758f1a8" caption="Adding a map slice" %}

## Using a map slice

You can hover over a map bubble to see details. Selections made in the map slice will filter downstream slices. 



