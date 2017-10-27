def main():
  exchange_rate = float(input("What's the current Euro to USD exchange rate?  "))
  starting_euros = float(input("How many Euros do you have to exchange?  "))
  final_usd = exchange_rate * starting_euros - 3
  print("Here's %f dollars!" % final_usd)

main()
