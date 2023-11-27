import os

import django.apps
import graphviz
from typing import Sequence, TypeVar

from django.db.models.base import ModelBase
from lxml import etree


CustomModel = TypeVar('CustomModel', bound=ModelBase)


def generate_data_model_diagram(models: Sequence[CustomModel], output_file='test_graph', add_labels=True,
                                view_diagram=True):
    # Initialize graph with more advanced visual settings
    dot = graphviz.Digraph(comment='Interactive Data Models', format='svg',
                           graph_attr={'bgcolor': '#EEEEEE', 'rankdir': 'TB', 'splines': 'spline'},
                           node_attr={'shape': 'none', 'fontsize': '12', 'fontname': 'Roboto'},
                           edge_attr={'fontsize': '10', 'fontname': 'Roboto'})

    # Iterate through each Django model
    for model in models:
        opt = model._meta
        name = model.__name__

        # Create an HTML-like label for each model as a rich table
        label = f'''<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="3" BGCOLOR="#3F51B5"><FONT COLOR="white">{name}</FONT></TD></TR>
        '''

        for field in opt.local_fields+opt.local_many_to_many:
            constraints = []
            if field.primary_key:
                constraints.append("PK")
            if field.unique:
                constraints.append("Unique")
            if field.db_index:
                constraints.append("Index")

            constraint_str = ','.join(constraints)
            color = "#BBDEFB"
            label += f'''<TR>
                         <TD BGCOLOR="{color}">{field.name}</TD>
                         <TD BGCOLOR="{color}">{field.verbose_name}</TD>
                         <TD BGCOLOR="{color}">{field.description.rsplit('（',1)[0]}{constraint_str or ''}</TD>
                         </TR>'''
            if field.is_relation:
                target_name = field.related_model.__name__
                tooltip = f"Relation between {name} and {target_name}"
                dot.edge(name, target_name, label=field.name if add_labels else None, tooltip=tooltip, color="#1E88E5",
                         style="dashed")

        label += '</TABLE>>'
        # # Create the node with an added hyperlink to detailed documentation
        dot.node(name, label=label)

    # Render the graph to a file and open it
    dot.render(output_file, view=view_diagram)

if __name__ == '__main__':
  # Change 'django_project.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

    django.setup()
    models = django.apps.apps.get_models()
    output_file_name = 'test_diagram'
    # skip django default models
    generate_data_model_diagram(models[5:], output_file_name, add_labels=True)
