import csv
import os
import unittest
from collections import defaultdict
from unittest.mock import MagicMock, patch

from solution import WikipediaAnimalsParser


class TestWikipediaAnimalsParser(unittest.TestCase):

    def setUp(self):
        self.parser = WikipediaAnimalsParser(
            api_url="https://ru.wikipedia.org/w/api.php",
            category="Категория:Животные_по_алфавиту",
            output_file="test_beasts.csv",
        )

    @patch.object(WikipediaAnimalsParser, "fetch_data")
    def test_parse_category(self, mock_fetch_data):
        mock_fetch_data.side_effect = [
            {
                "query": {
                    "categorymembers": [{"title": "Акула"}, {"title": "Бабочка"}]
                },
                "continue": {"cmcontinue": "1"},
            },
            {"query": {"categorymembers": [{"title": "Верблюд"}, {"title": "Голубь"}]}},
        ]

        self.parser.parse_category()

        self.assertEqual(self.parser.animals_count["А"], 1)
        self.assertEqual(self.parser.animals_count["Б"], 1)
        self.assertEqual(self.parser.animals_count["В"], 1)
        self.assertEqual(self.parser.animals_count["Г"], 1)

    def tearDown(self):
        if os.path.exists(self.parser.output_file):
            os.remove(self.parser.output_file)


if __name__ == "__main__":
    unittest.main()
