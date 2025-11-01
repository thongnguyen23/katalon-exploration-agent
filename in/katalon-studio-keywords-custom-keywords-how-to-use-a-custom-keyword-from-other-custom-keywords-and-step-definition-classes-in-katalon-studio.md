---
hide_title: true
title: How to use a custom keyword from other custom keywords and step definition classes in Katalon Studio
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>How to use a custom keyword from other custom keywords and step definition classes in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<div xmlns="http://www.w3.org/1999/xhtml" className="p">Besides built-in keywords, Katalon Studio also allows users to create custom keywords for these purposes:<ul className="ul"><li className="li"><p className="p">Creating reusable scripts</p></li><li className="li"><p className="p">Extending testing capability</p></li><li className="li"><p className="p">Setting up testing projects with a specific pattern</p></li></ul> </div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Initially, custom keywords are designed use in test cases. Combined with built-in keywords, custom keywords can help perform a complete test scenario.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Here is an example of a custom keyword, which prints out a parameter.</p> 

```jsx
class ParamTypes {
  @Keyword
  def map_variables(Map <String, String> my_map) {
    println my_map
  }
}
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The keyword can be used in a test case via <strong className="ph b">CustomKeywords</strong> class</p> 

```jsx
CustomKeywords.'ParamTypes.map_variables'([('last name') : 'smith', ('first name') : 'john'])
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In Katalon Studio, the test case Script is not the only place that allows users to script. Users can script at the custom keyword class and the BDD step definition class. Unfortunately, you will get the following error message when calling the custom keyword in these classes:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>Test Cases/Tips and Tricks/Custom Keywords/Params - Map FAILED because (of) (Stack trace: {"\n"}groovy.lang.MissingPropertyException: No such property: CustomKeywords for class: com.common.types.ParamTypes{"\n"}</code></pre> 

In the custom keyword class and the BDD step definition class, custom keywords cannot be called directly as in test case via CustomKeywords class. They can be called as methods of a groovy class. Here are two options you can choose to get it work:

- Option 1: Create a new instance of the class and call the method
```jsx
def param_types = new ParamTypes()
param_types.map_variables([('last name') : 'smith', ('first name') : 'john'])
```

- Option 2: Declare the custom keyword as static
  ```jsx
  class ParamTypes {
    @Keyword
    def static map_variables(Map <String, String> my_map) {
      println my_map
    }
  }
  ```
  and call the method
  ```jsx
  ParamTypes.map_variables([('last name') : 'smith', ('first name') : 'john'])
  ```