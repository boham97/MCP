# This Ruby script generates the Fibonacci sequence up to a certain number of terms.

def fibonacci(n)
  return [0] if n == 1
  return [0, 1] if n == 2

  fib_sequence = [0, 1]
  (2...n).each do |i|
    next_value = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence << next_value
  end

  fib_sequence
end

# Example usage:
terms = 10
puts "Fibonacci sequence up to #{terms} terms:"
puts fibonacci(terms)
