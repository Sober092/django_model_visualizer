# SQLAlchemy Data Model Visualizer

## Overview

This Python-based utility generates high-quality, readable visualizations of your SQLAlchemy ORM models. With a focus on clarity and detail, it uses Graphviz to render each model as a directed graph, making it easier to understand the relationships between tables in your database schema.

## Features

- Automatically maps SQLAlchemy ORM models to a directed graph.
- Table-like representation of each model with fields, types, and constraints.
- Visual cues for primary keys, unique fields, and indexed fields.
- Export diagrams to SVG format for high-quality viewing and printing.

## Installation

To get started, clone the repository and install the required packages.

```bash
git clone https://github.com/Dicklesworthstone/sqlalchemy_data_model_visualizer.git
cd sqlalchemy_data_model_visualizer
pip install -r requirements.txt
```

## Requirements

- Python 3.x
- SQLAlchemy
- Graphviz
- lxml

## Usage

### Generate Data Model Diagram

First, paste in your SQLAlchemy models. A set of fairly complex data models are provided in the code directly as an example-- just replace these with your own from your application.

Then, simply call the `generate_data_model_diagram` function. This will generate an SVG file with the name `my_data_model_diagram.svg`.

## API Documentation

### `generate_data_model_diagram(models, output_file='my_data_model_diagram')`

- `models`: List of SQLAlchemy models you want to visualize.
- `output_file`: Name of the output SVG file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
