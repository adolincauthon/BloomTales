import json

with open('model_responses.json') as file:
    data = json.load(file)
    for entry in data:
        name = list(entry.keys())[0]
        print(name)
        model = entry.get(name)
        print('--------------------')
        for metric, details in model.items():
            print(metric)
            print(f'Mean Perplexity: {details.get("mean_perplexity")}')
            print(f'Mean TTR: {details.get("mean_ttr")}')
            print('-----------')
