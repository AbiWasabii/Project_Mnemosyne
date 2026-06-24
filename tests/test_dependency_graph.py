from services.core.dependency_graph import DEPENDENCY_GRAPH


for module, dependencies in DEPENDENCY_GRAPH.items():

    print()

    print(module)

    print("depends on")

    print(dependencies)