import numpy as np
import matplotlib.pyplot as plt


def monte_carlo_example():
    no_of_simulations = 100_000_000

    # generate material strengths
    # concrete C30/37 properties: https://eurocodeapplied.com/design/en1992/concrete-design-properties
    mu_c, sigma_c = 38, 4.5
    concrete_samples = np.random.normal(mu_c, sigma_c, no_of_simulations)
    print(np.quantile(concrete_samples, 0.05))

    # generate load situations
    mu_l, sigma_l = 20, 6.5
    load_situations = np.random.normal(mu_l, sigma_l, no_of_simulations)
    print(np.quantile(load_situations, 0.95))

    # safety coefficients of material and load
    coef_c = 1.5
    coef_l = 1.5  # 1.35/1.5 (movable/static load)
    design_utilization = 0.95  # navržené procento využití konstrukce
    load_situations_design = load_situations * design_utilization / coef_l / coef_c

    # Monte Carlo simulation generates material and load in pairs: assess failure probability
    failures = concrete_samples < load_situations_design
    result_msg = f"Total failures per {no_of_simulations:,} simulations: {failures.sum()}"
    print(result_msg)
    print(f"Failure probability {100 * failures.sum() / no_of_simulations} %")

    # visualization
    plt.suptitle("Monte Carlo simulation of structure failure")
    plt.title(result_msg)
    plt.hist(load_situations_design, bins=100, color="red", label="Design loads")
    # plt.hist(load_situations, bins=100, color="red")
    plt.hist(concrete_samples, bins=100, color="blue", label="Material strengths")
    plt.xlabel("Strength/load [MPa]")
    plt.ylabel("Number of occurrences [-]")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # https://en.wikipedia.org/wiki/Monte_Carlo_method
    monte_carlo_example()
