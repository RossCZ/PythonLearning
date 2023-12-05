import numpy as np
import pandas as pd
import plotly.express as px


def bootstrap_example():
    # generate random samples with arbitrary distribution
    sample_size = 10000
    np.random.seed(3)

    # numpy random distributions: https://numpy.org/doc/1.16/reference/routines.random.html
    # samples = np.random.uniform(low=1, high=10, size=sample_size)
    # samples = np.random.normal(loc=3.14, scale=5, size=sample_size)
    samples = np.random.gamma(shape=3.14, scale=5, size=sample_size)
    # samples = np.random.exponential(scale=5, size=sample_size)

    # bootstrap (random selection with replacement)
    # means are normally distributed
    # useful e.g. for hypothesis testing
    bootstrap_repeats = 500
    bootstrap_samples = 100  # larger -> more confident mean estimation
    bootstrap = np.array([np.mean(np.random.choice(samples, size=bootstrap_samples)) for i in range(bootstrap_repeats)])
    bootstrapped_mean = float(np.mean(bootstrap))
    q_05 = float(np.quantile(bootstrap, 0.05))
    q_95 = float(np.quantile(bootstrap, 0.95))

    print(f"Bootstrapped mean: {bootstrapped_mean:.3f}")
    print(f"Quantile 0.05: {q_05:.3f}")
    print(f"Quantile 0.95: {q_95:.3f}")

    # visualize
    df = pd.DataFrame(dict(
        series=np.concatenate((["samples"]*len(samples), ["bootstrap"]*len(bootstrap))),
        data=np.concatenate((samples, bootstrap))
    ))

    fig = px.histogram(df, nbins=200, x="data", color="series", barmode="overlay", marginal="rug", title="Population distribution")
    fig.update_traces(opacity=0.75)
    fig.add_vline(x=bootstrapped_mean, line_width=1, line_dash="dash", line_color="black", annotation_text="Bootstrapped mean with 90% confidence intervals")
    fig.add_vline(x=q_05, line_width=1, line_dash="dash", line_color="grey")
    fig.add_vline(x=q_95, line_width=1, line_dash="dash", line_color="grey")
    # fig.write_html("bootstrap.html")
    fig.show()


bootstrap_example()
