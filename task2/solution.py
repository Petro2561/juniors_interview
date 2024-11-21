import csv
import json
import urllib.parse
import urllib.request
from collections import defaultdict


class WikipediaAnimalsParser:
    def __init__(self, api_url, category, output_file="beasts.csv"):
        self.api_url = api_url
        self.category = category
        self.output_file = output_file
        self.animals_count = defaultdict(int)

    def fetch_data(self, params):
        query_string = urllib.parse.urlencode(params)
        full_url = f"{self.api_url}?{query_string}"

        with urllib.request.urlopen(full_url) as response:
            print(response)
            return json.loads(response.read().decode("utf-8"))

    def parse_category(self):
        continue_param = None

        while True:
            params = {
                "action": "query",
                "format": "json",
                "list": "categorymembers",
                "cmtitle": self.category,
                "cmlimit": 500,
            }

            if continue_param:
                params.update(continue_param)

            data = self.fetch_data(params)

            for member in data["query"]["categorymembers"]:
                title = member["title"]
                first_letter = title[0].upper()
                if "А" <= first_letter <= "Я":
                    self.animals_count[first_letter] += 1

            if "continue" in data:
                continue_param = data["continue"]
            else:
                break

    def save_to_csv(self):
        with open(self.output_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            for letter, count in sorted(self.animals_count.items()):
                writer.writerow([letter, count])

    def run(self):
        self.parse_category()
        self.save_to_csv()
        print(f"Результаты сохранены в {self.output_file}")


if __name__ == "__main__":
    print("Погнали")
    parser = WikipediaAnimalsParser(
        api_url="https://ru.wikipedia.org/w/api.php",
        category="Категория:Животные_по_алфавиту",
    )
    parser.run()
