# import libraries
import networkx as nx
import matplotlib.pyplot as plt

# create directed graph
DG = nx.DiGraph()

# define relationships (edges)
edges = [
    # Students → Lecturer
    ("Samuel Kameta", "Lecturer"),
    ("Ernest", "Lecturer"),
    ("Princilla", "Lecturer"),
    ("Stephen Narh", "Lecturer"),
    ("Yeboah Jnr", "Lecturer"),
    ("Charles Ahorsu", "Lecturer"),
    ("Mac-Anthony", "Lecturer"),
    ("Lydia", "Lecturer"),
    ("Prince Obeng", "Lecturer"),
    ("Prince Tawiah", "Lecturer"),
    ("Stephen Diaba", "Lecturer"),
    ("Abiboye Philip", "Lecturer"),
    ("Raphael", "Lecturer"),
    ("Emmanuel", "Lecturer"),
    ("Frederick", "Lecturer"),
    ("Gilbert Adjei", "Lecturer"),
    ("Abdul Alhassan", "Lecturer"),
    ("Daniel", "Lecturer"),

    # Students → Supervisor
    ("Samuel Kameta", "Supervisor"),
    ("Ernest", "Supervisor"),
    ("Princilla", "Supervisor"),
    ("Stephen Narh", "Supervisor"),
    ("Yeboah Jnr", "Supervisor"),

    # Study partners (bidirectional)
    ("Samuel Kameta", "Princilla"),
    ("Princilla", "Samuel Kameta"),
]

# add edges
DG.add_edges_from(edges)

# compute and print network metrics
print("Number of nodes:", DG.number_of_nodes())
print("Number of edges:", DG.number_of_edges())

degrees = dict(DG.degree())
print("Degree distribution:", degrees)

isolated_nodes = list(nx.isolates(DG))
print("Isolated nodes:", isolated_nodes)

# draw network
plt.figure(figsize=(12, 9))

pos = nx.circular_layout(DG)

nx.draw(
    DG,
    pos,
    with_labels=True,
    node_color="skyblue",
    node_size=1800,
    font_size=9,
    arrows=True,
    arrowstyle="->",
    arrowsize=15
)

plt.title("Department Relationship Network for Social Network Class at UG", fontsize=14)
plt.show()