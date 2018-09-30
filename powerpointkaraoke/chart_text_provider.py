import csv
import random


class TextChartProvider(object):
    def next_titles(self):
        with open('charts.csv', 'r') as csv_file:
            rows = []
            chart_values = csv.reader(csv_file, delimiter=',')
            for row in chart_values:
                rows.append(row)
            return random.choice(rows)
