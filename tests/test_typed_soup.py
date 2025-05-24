import unittest
from bs4 import BeautifulSoup
from scrapy.http.response.html import HtmlResponse
from typed_soup import TypedSoup, from_response


class TestTypedSoup(unittest.TestCase):
    def test_find(self):
        html = "<div class='example'>Hello</div>"
        soup = BeautifulSoup(html, "html.parser")
        typed_soup = TypedSoup(soup)
        element = typed_soup.find("div", class_="example")
        self.assertIsNotNone(element)
        if element:
            self.assertEqual(element.get_text(), "Hello")

    def test_find_all(self):
        html = "<p>First</p><p>Second</p>"
        soup = BeautifulSoup(html, "html.parser")
        typed_soup = TypedSoup(soup)
        elements = typed_soup.find_all("p")
        self.assertEqual(len(elements), 2)
        self.assertEqual(elements[0].get_text(), "First")
        self.assertEqual(elements[1].get_text(), "Second")

    def test_implicit_find_all(self):
        html = "<p>First</p><p>Second</p>"
        soup = BeautifulSoup(html, "html.parser")
        typed_soup = TypedSoup(soup)
        elements = typed_soup("p")
        self.assertEqual(len(elements), 2)
        self.assertEqual(elements[0].get_text(), "First")
        self.assertEqual(elements[1].get_text(), "Second")

    def test_from_response(self):
        # Create a mock HtmlResponse
        response = HtmlResponse(url="http://example.com",
                                body="<div>Test</div>", encoding="utf-8")
        typed_soup = from_response(response)
        element = typed_soup.find("div")
        self.assertIsNotNone(element)
        if element:
            self.assertEqual(element.get_text(), "Test")


if __name__ == "__main__":
    unittest.main()
