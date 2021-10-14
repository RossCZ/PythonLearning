from anastruct import SystemElements
import sectionproperties.pre.sections as sections
from sectionproperties.analysis.cross_section import CrossSection
# https://sectionproperties.readthedocs.io/en/latest/rst/installation.html


def sectionproperties_example():
    # https://sectionproperties.readthedocs.io/
    # parameters of bridge section
    h = 1.0
    b = 2.0
    w = 1.0
    t = 0.1

    # build the lists of points, facets, holes and control points
    points = [[b / 2, h], [b / 2, h - t], [w / 2, h - t], [w / 2, 0],
              [-w / 2, 0], [-w / 2, h - t], [-b / 2, h - t], [-b / 2, h],
              [w / 2 - t, h - t], [w / 2 - t, t], [-w / 2 + t, t], [-w / 2 + t, h - t]]
    facets = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [8, 9], [9, 10], [10, 11], [11, 8]]
    holes = [[0, h / 2]]
    control_points = [[0, h - t / 2]]

    # define the CSS
    geometry = sections.CustomSection(points, facets, holes, control_points)
    geometry.clean_geometry()
    geometry.plot_geometry()

    # mesh the CSS
    print("meshing...")
    mesh = geometry.create_mesh(mesh_sizes=[0.001])
    # print(len(mesh.points))
    section = CrossSection(geometry, mesh)
    section.plot_mesh()

    # CSS properties
    print("calculating CSS properties...")
    section.calculate_geometric_properties()
    section.calculate_warping_properties()
    section.display_mesh_info()
    section.display_results()

    section.plot_centroids()

    # define a load case
    print("stress analysis...")
    load_case = section.calculate_stress(Mxx=10e6, Vx=20e3, Mzz=5e6)

    # stress analysis
    stresses = load_case.get_stress()
    print('Material: {0}'.format(stresses[0]['Material']))
    print('Axial Stresses: {0}'.format(stresses[0]['sig_zz_n']))
    print(len(stresses[0]['sig_zz_n']))

    # plot results
    load_case.plot_stress_m_zz()  # bending stress
    load_case.plot_vector_mzz_zxy()  # torsion vectors
    load_case.plot_stress_v_zxy()  # shear stress
    load_case.plot_stress_vm()  # von mises stress


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
    sectionproperties_example()
    # anastruct_example()

