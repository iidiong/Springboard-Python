### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  - **Python:** Uses indentation to define code block
  - **JavaScript:** Uses curly bracket to define code block

  - **Python:** Variable is defined with no keyword
  - **JavaScript:** Variable is defined with keyword (let, var, const)

  - **Python:** Uses snake_case variable naming style
  - **JavaScript:** Uses camelCase variable naming style

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.

- What is a unit test?

  - **Unit test:** Validates each unit (function) of the software code performs as expected.

- What is an integration test?

  - **Unit test:** Validates the interaction between multiple software modules of the software code performs as expected.

- What is the role of web application framework, like Flask?

  - **Flask:** Provides the necessary components for web development, such as ****routing**,** ****request handling**,** ****sessions**,**. Also, provides development server and debugger.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

- How do you collect data from a URL placeholder parameter using Flask?

- How do you collect data from the query string using Flask?

  - **response.data.args[field name]**

- How do you collect data from the body of the request using Flask?

  - **response.data.form[field name]**

- What is a cookie and what kinds of things are they commonly used for?

  - **Cookies:** Are name/string-value pair stored by the browser. They are commonly use to save "state"

- What is the session object in Flask?

  - **Session object:** Flask uses session object to remember state information

- What does Flask's `jsonify()` do?
  - **jsonify()** serializes data to JavaScript Object Notation(JSON) format.
