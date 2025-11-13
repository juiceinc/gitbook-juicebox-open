---
description: Slice selections don't always have to filter down the page
---

# Selections as Variables

By default, selections in a slice filter the data in downstream slices. You can change this default behavior by configuring slice selections.

You can configure the slice selections to act as:

1. Filters. Slice selections will filter downstream slices. (This is the default configuration.)
2. Variables. Slice selections will not filter downstream slices but will be available for use in defining ingredients.&#x20;
3. Filters and Variables. Slices selections will filter downstream slices and be available for use in defining ingredients.&#x20;

<figure><img src="../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>



#### How to use Variables <a href="#variables-use-the-id-of-the-dimension-that-the-slice-is-showing" id="variables-use-the-id-of-the-dimension-that-the-slice-is-showing"></a>

If you configure slice selections to act as Variables, the selected values will be saved. You can use the saved values in ingredient definitions. For example, let's say you have a Filter slice with two dimesions: Genres and Directors.&#x20;

#### Using variables in your ingredients labels <a href="#using-variables-in-your-ingredients-labels" id="using-variables-in-your-ingredients-labels"></a>

You can use variables to make dynamic ingredient labels. To start you need to know the ingredient id of the selected variable. You can open the ingredient and click the "..." and select "Copy Ingredient Id".

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FLqYT7hDGyGIUtziD3T8T%2Fuploads%2FW0pBVddQzrZZfNHEnybU%2FScreen%20Shot%202023-08-16%20at%2011.26.18%20AM.png?alt=media&#x26;token=a5918753-0e6b-4075-bb62-052e3ce4b0e8" alt=""><figcaption></figcaption></figure>

Use the id of the ingredient being used as a variable in the label by surrounding it with brackets like this “\{{ingredient\_id\}}“. You can also other text in your label too, so "Budget of \{{Director\}}" would work if an ingredient with id of Director was a variable.The variable **must** be selected above. Otherwise you'll just get the label without the variable substituted.

#### Using variables in your ingredient's field expressions <a href="#using-variables-in-your-ingredients-field-expressions" id="using-variables-in-your-ingredients-field-expressions"></a>

You can use variables in your field definition. For instance, if you have selected a director in a variable, you can refer to the selected director in your field like this: field:&#x20;

`sum(if(Director="{{Director}}", Budget, 0))`&#x20;

Note the double quotes around \{{Director\}} because it's a string.

#### Using variables to define constants <a href="#using-variables-to-define-constants" id="using-variables-to-define-constants"></a>

You can use variables in your datasource constants. Just refer to the variable to get the first movie released by the selected director.firstMovieReleaseDate: min(if(Director="\{{Director\}}", ReleaseDate))

#### Limitations <a href="#limitations" id="limitations"></a>

Here are two things to keep in mind. We plan on improving these later.

* We only substitute variables in `fields`, `singular`, and `plural` for ingredients. We aren't substituting in buckets. We are substituting in optional fields like id\_field or latitude\_field.
* The variable is the **first** selected value. If you have multiple values selected, only the first will be available.

​
