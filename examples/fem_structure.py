from anastruct import SystemElements


def anastruct_example():
    # https://anastruct.readthedocs.io/en/latest/
    ss = SystemElements()
    ss.add_element(location=[[0, 0], [3, 4]])
    ss.add_element(location=[[3, 4], [8, 4]])
    ss.add_element(location=[[0, 8], [3, 4]])

    print("nodes:")
    for id, node in ss.node_map.items():
        print(id, node.vertex)

    ss.add_support_hinged(node_id=1)
    ss.add_support_fixed(node_id=3)
    ss.add_support_hinged(node_id=4)
    ss.q_load(element_id=2, q=-10)

    ss.solve()
    ss.show_structure()
    ss.show_reaction_force()
    ss.show_bending_moment()
    ss.show_displacement()


if __name__ == "__main__":
    anastruct_example()

