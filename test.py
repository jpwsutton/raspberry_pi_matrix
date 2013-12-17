import raspberry_pi_matrix
myDriver = raspberry_pi_matrix.driver(A=4)
myDefaultDriver = raspberry_pi_matrix.driver()
print("Joke Test: " + myDriver.joke())
myDriver.listPins()

