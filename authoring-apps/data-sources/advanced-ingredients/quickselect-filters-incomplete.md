# Quickselect filters \[incomplete\]



#### 

{% hint style="info" %}
Both bucketed dimensions and quickselects can be used for in filter slices. But quickselects can **only** be used in filter slices, whereas bucketed dimensions can be used in other slices. You would use quickselects vs buckets if a single data value should be associated with more than one filter option.  For example, if you want filters for ages `18 and older` and `45 and older` , you must use a quickselect because some age values \(e.g., 46\) will be associated with both filters. Buckets will not work because each age value can only belong to one bucket.
{% endhint %}

