from scapy.layers.inet import traceroute

# Define the target
target = ["www.google.com"]

# Run the traceroute with a maximum TTL of 32
result, unans = traceroute(target, maxttl=32, verbose=0)

# Print the results
print(result.show())  # Display the result in a readable format
print(unans.show())   # Display unanswered packets, if any
