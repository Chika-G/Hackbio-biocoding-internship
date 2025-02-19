def translate_dna_to_protein(dna_sequence):
    # Codon to amino acid mapping
    codon_table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S', 'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*', 'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W'
    }
    
    # Ensure the DNA sequence length is a multiple of 3
    dna_sequence = dna_sequence.upper()
    protein = []
    
    # Iterate over the DNA sequence in steps of 3 (codons)
    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3]
        if len(codon) == 3:  # Only process full codons
            amino_acid = codon_table.get(codon, '')
            if amino_acid == '*':  # Stop codon
                break
            protein.append(amino_acid)
    
    return ''.join(protein)

#Write a function that simulates and generates a logistic population growth curve
import numpy as np
import matplotlib.pyplot as plt

def logistic_growth(t, P0, K, r, lag_duration_max, exp_duration_max):
    # Randomly vary the lag and exponential durations
    lag_duration = np.random.uniform(0, lag_duration_max)
    exp_duration = np.random.uniform(0, exp_duration_max)
    
    # Calculate the population for each time point using logistic growth equation
    population = []
    for time in t:
        if time < lag_duration:
            # During the lag phase, the population increases slowly
            population.append(P0)  # Start at initial population
        elif time < lag_duration + exp_duration:
            # During the exponential phase, population grows rapidly
            P_exp = P0 * np.exp(r * (time - lag_duration))  # Exponential growth
            population.append(min(P_exp, K))  # Cap the population at K (carrying capacity)
        else:
            # After the exponential phase, the population levels off
            population.append(K)  # Population approaches the carrying capacity
        
    return population

def generate_population_curve(P0=10, K=1000, r=0.1, t_max=100, lag_duration_max=20, exp_duration_max=50):
    # Time points from 0 to t_max (in arbitrary time units)
    t = np.linspace(0, t_max, t_max * 10)
    
    # Simulate the logistic growth
    population = logistic_growth(t, P0, K, r, lag_duration_max, exp_duration_max)
    
    # Plot the growth curve
    plt.figure(figsize=(10, 6))
    plt.plot(t, population, label='Population Size vs Time')
    plt.title('Logistic Population Growth Curve')
    plt.xlabel('Time')
    plt.ylabel('Population Size')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return population

# Example usage:
generate_population_curve(P0=10, K=1000, r=0.1, t_max=100, lag_duration_max=20, exp_duration_max=50)

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
