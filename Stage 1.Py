codon_to_aa = {
    'AUG': 'M',  'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 
    'CUU': 'L',  'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'AUU': 'I', 
    'AUC': 'I',  'AUA': 'I', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 
    'ACG': 'T',  'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 
    'GCU': 'A',  'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'UUU': 'F', 
    'UUU': 'F', 'CCU': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P', 
    'AGU': 'S', 'AGS': 'S', 'GGA': 'G', 'GGC': 'G', 'GGG': 'G'
}
def dna_to_rna(dna_sequence):
    """Convert DNA sequence to RNA (replace T with U)."""
    return dna_sequence.replace('T', 'U')

def translate_rna_to_protein(rna_sequence):
    """Translate RNA sequence into a protein sequence."""
    protein = ""
    
    # Split RNA into codons (3 nucleotides per codon)
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
      
        # Ensure we have a valid codon of length 3
        if len(codon) == 3:
            # Check if codon is in codon_to_aa dictionary
            if codon in codon_to_aa:
                protein += codon_to_aa[codon]
            else:
                protein += '?'  # Or use 'X' for an unknown codon
        else:
            # Handle incomplete codons (less than 3 nucleotides)
            protein += '?'  # Or use 'X' for incomplete codons
    
    return protein
#Write a function that simulates and generates a logistic population growth curve
import numpy as np
import matplotlib.pyplot as plt
import random

def logistic_growth(t, K, P0, r, lag_random_factor, exp_random_factor):
    """
    Simulate logistic population growth with randomized lag and exponential phases.
    
    Parameters:
    t : numpy array of time points
    K : carrying capacity (max population size)
    P0 : initial population size
    r : growth rate
    lag_random_factor : random factor to adjust the lag phase duration
    exp_random_factor : random factor to adjust the exponential phase duration
    
    Returns:
    Population size at each time point.
    """
    # Randomize the lag and exponential phases
    lag_phase_duration = random.uniform(lag_random_factor[0], lag_random_factor[1])
    exp_phase_duration = random.uniform(exp_random_factor[0], exp_random_factor[1])
    
    population = np.zeros_like(t)
    
    for i, time in enumerate(t):
        # If within lag phase, use an almost constant population
        if time < lag_phase_duration:
            population[i] = P0
        # If within exponential phase, calculate using logistic growth
        elif time < lag_phase_duration + exp_phase_duration:
            population[i] = K / (1 + ((K - P0) / P0) * np.exp(-r * (time - lag_phase_duration)))
        # After exponential phase, population starts leveling off
        else:
            population[i] = K

    return population

# Parameters
K = 1000      # Carrying capacity
P0 = 10       # Initial population
r = 0.1       # Growth rate
t = np.linspace(0, 50, 500)  # Time array

# Randomization ranges for the lag and exponential phases
lag_random_factor = (5, 10)    # Randomize lag phase duration between 5 and 10 time units
exp_random_factor = (10, 20)   # Randomize exponential growth phase between 10 and 20 time units

# Get the logistic growth curve
population = logistic_growth(t, K, P0, r, lag_random_factor, exp_random_factor)

# Plotting the results
plt.plot(t, population, label="Logistic Growth")
plt.xlabel('Time')
plt.ylabel('Population Size')
plt.title('Logistic Population Growth with Randomized Phases')
plt.legend()
plt.grid(True)
#generate a dataframe with 100 different growth curves
def generate_growth_curves(num_curves, t, K, P0, r, lag_random_factor, exp_random_factor):
    data = {}
    
    for i in range(num_curves):
        # Generate a random curve
        population = logistic_growth(t, K, P0, r, lag_random_factor, exp_random_factor)
        data[f'Curve_{i+1}'] = population
    
    # Convert to a DataFrame
    df = pd.DataFrame(data, index=t)
    return df

# Parameters
K = 1000      # Carrying capacity
P0 = 10       # Initial population
r = 0.1       # Growth rate
t = np.linspace(0, 50, 500)  # Time array

# Randomization ranges for the lag and exponential phases
lag_random_factor = (5, 10)    # Randomize lag phase duration between 5 and 10 time units
exp_random_factor = (10, 20)   # Randomize exponential growth phase between 10 and 20 time units

# Generate 100 different growth curves
num_curves = 100
df_growth_curves = generate_growth_curves(num_curves, t, K, P0, r, lag_random_factor, exp_random_factor)

# Display the DataFrame
print(df_growth_curves.head())

plt.show()
#Write a function for determining the time to reach 80% of the maximum growth;
def time_to_reach_80_percent(K, P_0, r):
    """
    Function to calculate the time when the population reaches 80% of the carrying capacity
    using the logistic growth model.
    
    Parameters:
    - K (float): Carrying capacity (maximum population or value).
    - P_0 (float): Initial population or value.
    - r (float): Growth rate.
    
    Returns:
    - t (float): Time to reach 80% of the carrying capacity.
    """
    # Solving the equation for t
    target_population = 0.8 * K  # 80% of carrying capacity
    term = (K - P_0) / P_0
    exponent = math.log((K / target_population - 1) / term)
    t = exponent / r
    
    return t

# Example usage
K = 1000  # carrying capacity
P_0 = 10  # initial population
r = 0.1   # growth rate

time = time_to_reach_80_percent(K, P_0, r)
print(f"Time to reach 80% of carrying capacity: {time:.2f} units of time")
#write a function for calculating the hamming distance between your Slack username and twitter/X handle
def hamming_distance(str1, str2):
    # Pad the shorter string with spaces to make both strings the same length
    max_len = max(len(str1), len(str2))
    str1 = str1.ljust(max_len)
    str2 = str2.ljust(max_len)
    
    # Count the number of positions where the characters are different
    return sum(a != b for a, b in zip(str1, str2))

# Your Slack username and Twitter/X handle
slack_username = "Onyedikachukwu"
twitter_handle = "Chika Chika"

# Calculate and print the Hamming distance
distance = hamming_distance(slack_username, twitter_handle)
print(f"The Hamming distance is: {distance}")
