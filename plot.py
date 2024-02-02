import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json

# Load data from JSON file
with open('model_responses_pk.json', 'r') as file:
    data = json.load(file)


# Define the number of columns (3 subplots per row)
num_cols = 3

# Calculate the number of rows based on the number of models
num_models = len(data)
# Ceiling division to ensure all models are included
num_rows = -(-num_models // num_cols)
model_names = [list(model.keys())[0] for model in data]
# Create subplots for Mean TTR
fig_ttr = make_subplots(rows=num_rows, cols=num_cols, subplot_titles=model_names,
                        shared_xaxes=True, shared_yaxes=True)

# Create subplots for Mean Perplexity
fig_perplexity = make_subplots(rows=num_rows, cols=num_cols, subplot_titles=model_names,
                               shared_xaxes=True, shared_yaxes=True)

# Loop through each model
for i, model_data in enumerate(data, start=1):
    model_name, responses = list(model_data.items())[0]

    categories = ['top_p', 'top_k', 'top_pk']
    mean_values_ttr = [responses[category]['mean_ttr']
                       for category in categories]
    mean_values_perplexity = [responses[category]
                              ['mean_perplexity'] for category in categories]

    # Calculate position in the subplot grid
    subplot_position = (i - 1) % num_cols + 1 + (i - 1) // num_cols * num_cols

    # Add line plot for Mean TTR
    fig_ttr.add_trace(go.Scatter(x=categories, y=mean_values_ttr, mode='lines+markers',
                                 name=f'{model_name}'),
                      row=(i - 1) // num_cols + 1, col=subplot_position % num_cols + 1)

    # Add line plot for Mean Perplexity
    fig_perplexity.add_trace(go.Scatter(x=categories, y=mean_values_perplexity, mode='lines+markers',
                                        ),
                             row=(i - 1) // num_cols + 1, col=subplot_position % num_cols + 1)

# Update layout for Mean TTR
fig_ttr.update_layout(height=500 * num_rows, width=1200, title_text='Mean TTR Line Plot for Models',
                      xaxis_title='Categories', yaxis_title='Mean TTR')

# Update layout for Mean Perplexity
fig_perplexity.update_layout(height=500 * num_rows, width=1200, title_text='Mean Perplexity Line Plot for Models',
                             xaxis_title='Categories', yaxis_title='Mean Perplexity')

# Show the plots
fig_ttr.show()
fig_perplexity.show()
