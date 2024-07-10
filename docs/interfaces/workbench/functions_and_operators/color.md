## Color functions

### **`bar()`**
| Function                           | Description                                                                                                                               | Return Type |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| `bar(x, width)`                    | Renders a single bar in an ANSI bar chart using a default low_color of red and a high_color of green.                                     | `varchar`   |
| `bar(x, width, low_color, high_color)` | Renders a single line in an ANSI bar chart of the specified width. The parameter x is a double value between 0 and 1. Values of x that fall outside the range [0, 1] will be truncated to either a 0 or a 1 value. The low_color and high_color capture the color to use for either end of the horizontal bar chart. | `varchar`   |


### **`color()`**
| Function                                    | Description                                                                                                    | Return Type |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------|-------------|
| `color(string)`                            | Returns a color capturing a decoded RGB value from a 4-character string of the format “#000”. The input string should be varchar containing a CSS-style short rgb string or one of `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`. | `color`     |
| `color(x, low, high, low_color, high_color)`| Returns a color interpolated between `low_color` and `high_color` using the double parameters `x`, `low`, and `high` to calculate a fraction which is then passed to the `color(fraction, low_color, high_color)` function shown below. If `x` falls outside the range defined by `low` and `high` its value is truncated to fit within this range. | `color`     |
| `color(x, low_color, high_color)`           | Returns a color interpolated between `low_color` and `high_color` according to the double argument `x` between 0 and 1. The parameter `x` is a double value between 0 and 1. Values of `x` that fall outside the range [0, 1] will be truncated to either a 0 or a 1 value. | `color`     |

### **`render()`**

| Function                   | Description                                                                                                 | Return Type |
|----------------------------|-------------------------------------------------------------------------------------------------------------|-------------|
| `render(x, color)`          | Renders value `x` using the specific color using ANSI color codes. `x` can be either a double, bigint, or varchar. | `varchar`   |
| `render(b)`                | Accepts boolean value `b` and renders a green true or a red false using ANSI color codes.                      | `varchar`   |


### **`rgb()`**


| Function                   | Description                                                                                                              | Return Type |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------|-------------|
| `rgb(red, green, blue)`    | Returns a color value capturing the RGB value of three component color values supplied as int parameters ranging from 0 to 255: `red`, `green`, `blue`. | `color`     |
