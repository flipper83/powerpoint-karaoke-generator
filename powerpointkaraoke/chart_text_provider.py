import csv
import random


class TextChartProvider(object):
    def next_titles(self):
        with open('charts.csv', encoding='utf-8', mode='r') as csv_file:
            rows = []
            chart_values = csv.reader(csv_file, delimiter=',')
            for row in chart_values:
                rows.append(row)
            return random.choice(rows)
