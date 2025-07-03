import numpy as np
from scipy.stats import norm

# Constants
u = 84.17
threshold = 40 * u / 19

def calculate_ai_models(paper_count, normalize_to=15, reference_variance=2000):
    std_dev = np.sqrt(paper_count)
    z_score = (threshold - u) / std_dev
    probability = 1 - norm.cdf(z_score)
    
    reference_std = np.sqrt(reference_variance)
    ref_prob = 1 - norm.cdf((threshold - u) / reference_std)
    scaling_factor = normalize_to / ref_prob
    
    return probability * scaling_factor

# Example usage:
if __name__ == "__main__":
    papers = float(input("Enter number of AI papers: "))
    models = calculate_ai_models(papers)
    print(f"Estimated AI models: {models:.2f}")
