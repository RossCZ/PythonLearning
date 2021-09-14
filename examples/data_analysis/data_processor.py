import matplotlib.pyplot as plt
import pandas as pd
import os


def process_data():
    in_dir_name = "Data"
    out_dir_name = "Output"

    processed_rows = 0
    processed_values = 0

    # each file in data directory
    directory_list = os.listdir(in_dir_name)
    for file in directory_list:
        if file.endswith(".TXT"):
            print(f"processing {file} ")

            # output directory
            if not os.path.exists(out_dir_name):
                os.mkdir(out_dir_name)

            # data load
            data_file = f"{in_dir_name}/{file}"
            df = pd.read_csv(data_file, delim_whitespace=True, index_col=0)

            # statistics
            rows = len(df.index)
            processed_rows += rows
            processed_values += rows * len(df.columns)

            # subdirectory
            file_name = file.split(".")[0]
            out_data_dir = f"{out_dir_name}/{file_name}"

            if not os.path.exists(out_data_dir):
                os.mkdir(out_data_dir)

                # figure for each column
                for col in df.columns:
                    print(f"\t column {col}")

                    out_df = df[[col]].copy()
                    out_df.dropna(inplace=True)
                    out_df = out_df.astype(float)

                    image_file_name = f"{out_data_dir}/{col}.png"
                    out_df.plot(legend=None)
                    plt.title(col)
                    plt.savefig(image_file_name)
                    plt.close()

    print("Finished!")
    print(f"{'{:,}'.format(processed_rows).replace(',', ' ')} rows processed")
    print(f"{'{:,}'.format(processed_values).replace(',', ' ')} values processed")


process_data()