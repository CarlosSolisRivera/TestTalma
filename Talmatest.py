import json
from collections import defaultdict

def load_input(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def group_cities_by_weather(data):
    grouped_data = defaultdict(lambda: {"wheater": None, "cities": []})

    for city in data['cities']:
        weather_condition = city['weather'][0]['main']
        if not grouped_data[weather_condition]['wheater']:
            grouped_data[weather_condition]['wheater'] = city['weather'][0]
        grouped_data[weather_condition]['cities'].append(city)

    return [{"wheater": v['wheater'], "cities": v['cities']} for v in grouped_data.values()]

def save_output(output_data, output_path):
    with open(output_path, 'w') as f:
        json.dump(output_data, f, indent=2)

input_file = 'C:\\Users\\Usuario\\PycharmProjects\\TalmaTest\\input.json'
output_file = 'C:\\Users\\Usuario\\PycharmProjects\\TalmaTest\\output.json'

data = load_input(input_file)
grouped_data = group_cities_by_weather(data)
save_output(grouped_data, output_file)

