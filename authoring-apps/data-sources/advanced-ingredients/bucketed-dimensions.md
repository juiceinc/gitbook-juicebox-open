# Bucketed dimensions

A bucketed dimension is a dimension that groups field values into buckets based on conditions. For example, the Unhealthy Americans data includes the `LocationAbbr` field with state abbreviation values. Let's say you want to groups these state abbreviation values into different regions: Southeast, Northeast, Midwest, Southwest, and West. To do that, you would create an advanced ingredient like so--

![Advanced ingredient: bucketed dimension](../../../.gitbook/assets/image%20%2839%29.png)

--with the following components:

```text
kind: Dimension
field: LocationAbbr
singular: Region
plural: Regions
buckets:
  - label: Southeast
    condition: 'IN ("AR", "AL", "GA", "MS", "TN", "KY", "SC", "NC", "VA", "WV", "DC", "FL")'
  - label: Northeast
    condition: 'IN ("ME","VT","NH","CT","NY","NJ","DE","MD","PA","MA","RI")'
  - label: Midwest
    condition: 'IN ("IA","MI","WI","MN","NE","MO","IN","IL","OH","KS","ND","SD")'
  - label: Southwest
    condition: 'IN ("TX","OK","AZ","NM")'
  - label: West
    condition: 'IN ("CA","NV","CO","UT","OR","WA","HI","WY","MT","ID","AK")'
buckets_default_label: Other
```

To create a bucketed dimension, you add the `buckets:` and `bucket_default_label:` components to the dimension definition. Within `buckets`, you define the `label`, `condition`, and \(optional\) `field`. 

```text
kind: Dimension
field: [field]
singular: [singular label]
plural: [plural label]
icon: [icon]
buckets:
  - label: [bucket1label]
    condition: [bucket1condition]
  - label: [bucket2label]
    condition: [bucket2condition]
  - label: [bucket3label]
    condition: [bucket3condition]
bucket_default_label: [defaultbucketlabel]
```

By default, each condition will be evaluated against the main `field`, but you can provide an alternative field in the condition itself, like so:

```text
kind: Dimension
field: grade
singular: Sales Group
plural: Sales Groups
buckets:
  # This first condition does not use the field because it contains its own
  - label: In-state
    condition: 'state = "Tennessee"'
  - label: Small
    condition: '<100.0'
  - label: Medium
    condition: '<1000.0'
buckets_default_label: Large
```

The conditions within buckets are evaluated in the order they are defined, which makes defining buckets for continuous values convenient:

```text
kind: Dimension
field: age
singular: Age Range
plural: Age Bands
buckets:
  - label: "Under 5"
    condition: '<5'
  - label: "5-17"
    condition: '<18'
  - label: "18-64"
    condition: '<65'
buckets_default_label: 65 and over
```

