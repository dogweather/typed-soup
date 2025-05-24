# typed-soup

A type-safe wrapper around BeautifulSoup and utilities for parsing HTML/XML with robust return types and error handling.

## Installation

```bash
pip install typed-soup
```

## Usage

```python
from typed_soup import from_response
from scrapy.http.response.html import HtmlResponse

# Assume 'response' is an HtmlResponse object
soup = from_response(response)

# Find an element
element = soup.find("div", class_="example")
if element:
    print(element.get_text())

# Find all elements
elements = soup.find_all("p")
for elem in elements:
    print(elem.get_text())
```

## License

This project is licensed under the MIT License.
