
class UsageTracker:

    def __init__(self):
        self.total_requests = 0
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_cost = 0.0

    def record(
        self,
        input_tokens=0,
        output_tokens=0,
        cost=0.0
    ):
        self.total_requests += 1
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        self.total_cost += cost

    def show(self):
        print("\n----- USAGE REPORT -----")
        print("Requests:", self.total_requests)
        print("Input tokens:", self.total_input_tokens)
        print("Output tokens:", self.total_output_tokens)
        print("Total tokens:",
              self.total_input_tokens +
              self.total_output_tokens)
        print("Estimated cost: $",
              round(self.total_cost, 6))