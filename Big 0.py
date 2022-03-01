def findNemo(array):
    for i in array:
      if i == 'nemo':
        print("Found NEMO!")
      else:
        print("Unfound NEMO!")
    return array
  

everyone = ["dory", "bruce", "marlin","nemo"]
findNemo(everyone)
