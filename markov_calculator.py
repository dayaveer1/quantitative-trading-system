# Import numpy and ESFuturesCollector class
import numpy as np
from futures_collector import ESFuturesCollector
collector = ESFuturesCollector()


class Markov:
    def __init__(self, type):
        if type == "daily":
            # Max period for daily candles
            data = collector.fetch_data("ytd", "1d") 

        elif type == "hourly":
            # 2 years of hourly candles
            data = collector.fetch_data("2y", "1h")  

        elif type == "minute":
            # 1 week of minute candles
            data = collector.fetch_data("7d", "1m")  

        else:
            # Error handling
            raise ValueError(f"Invalid mode '{type}' — choose 'daily', 'hourly', or 'minute''") 

        self.data = collector.clean(data)  # Clean data for when volume = 0
        
    """Calculate the percentage change between the closing price of subsequent rows of data"""
    def percentage_change(self):
        data = self.data
        percentages = []

        if collector.validate_data(data):
            for i in range(len(data)-1):  # Iterate through rows
                 # Calculate percentage change and append to array
                percent = ((float(data["Close"].iloc[i]) - float(data["Close"].iloc[i+1])) / float(data["Close"].iloc[i])) * 100 
                percentages.append(percent)

            print(f"{len(percentages)} percentage changes were calculated")
            return percentages 

        else:
            return None  # Error handling
        
    """Calculate transition probabilities between states"""
    def transition_probability(self, percentages):
        try:   
            # Convert to numpy array
            percentages = np.array(percentages)
            mean = np.mean(percentages)
            std_dev = np.std(percentages)

            # Define 6 bins: (-∞, μ−2σ], (μ−2σ, μ−σ], (μ−σ, μ], (μ, μ+σ], (μ+σ, μ+2σ], (μ+2σ, ∞)
            bins = [-np.inf, (mean-(2*std_dev)), (mean-std_dev), mean, (mean+std_dev), (mean+(2*std_dev)), np.inf]
            labels = ['very big drop', 'big drop', 'small drop', 'small rise', 'big rise', 'very big rise']

            # Discretize changes into states and find the most recent state
            states = np.digitize(percentages, bins) - 1
            recent_state = states[-1]

            # Count transitions between states
            n_states = len(labels)
            transition_counts = np.zeros((n_states, n_states))  # Initialize NumPy matrix
            for (current_state, next_state) in zip(states[:-1], states[1:]):
                transition_counts[current_state, next_state] += 1

            # Calculate transition probabilities by normalizing counts
            transition_probabilities = transition_counts / transition_counts.sum(axis=1, keepdims=True)

            print("Probability Matrix created")
            return transition_probabilities, recent_state, mean, std_dev
        
        except Exception as e:
            # Return possible errors
            print(f"Error fetching data: {e}")
            return None


# Test the markov calculator
if __name__ == "__main__":
    minute = Markov("minute")
    percentages = Markov("minute").percentage_change()
    probabilities = minute.transition_probability(percentages)
    print(probabilities)
