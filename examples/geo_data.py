import pandas as pd
import os
import matplotlib.pyplot as plt

# different venv: installed by conda
import geopandas
import contextily as cx  # conda install contextily --channel conda-forge


def get_geo_df(df):
    # create geo data frame
    gdf = geopandas.GeoDataFrame(geometry=df.geometry)
    # fix the coordinate system
    gdf = gdf.to_crs("epsg:3857")
    return gdf


def geopandas_example():
    data_folder = "geo_data"

    df_vrty = geopandas.read_file(os.path.join(data_folder, "horizontalni_vrty.geojson"))
    df_pomery = geopandas.read_file(os.path.join(data_folder, "slozite_pomery.geojson"))
    df_casti = geopandas.read_file(os.path.join(data_folder, "mestske_casti.geojson"))
    # print(df_casti.columns)

    gdf_vrty = get_geo_df(df_vrty)
    gdf_pomery = get_geo_df(df_pomery)
    gdf_casti = get_geo_df(df_casti)

    # plot the result
    # gdf.plot()
    fig, ax = plt.subplots(figsize=(8, 8))
    gdf_vrty.plot(ax=ax, color="khaki")
    gdf_pomery.plot(ax=ax, color="slateblue")
    gdf_casti.plot(ax=ax, color="none", edgecolor="red")

    # add a base map
    cx.add_basemap(ax, source=cx.providers.Stamen.TonerLite)  # zoom -> map detail (e.g. 12)

    # add labels - district names
    for id, polygon in gdf_casti.iterrows():
        mestska_cast = df_casti.loc[id]
        label = mestska_cast.nazev.split("-")[1]
        # print(mestska_cast)
        # print(polygon.geometry.centroid)
        plt.annotate(s=label, xy=polygon.geometry.centroid.coords[:][0], horizontalalignment="center")

    plt.axis("off")
    plt.title("Brno - geodata")
    # plt.xlim(1.84e6, 1.85e6)
    # plt.ylim(6.303e6, 6.31e6)
    plt.tight_layout()
    plt.show()


# opendata:
# https://data.brno.cz/pages/data-na-vyzadani
# https://data.gov.cz/datov%C3%A9-sady
if __name__ == "__main__":
    geopandas_example()

