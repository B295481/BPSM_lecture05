#!/usr/bin/python3
import os
os.chdir("/localdisk/home/s2903949/exercises/lecture15")
import amino
try:
  assert round(amino.amino("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
  assert round(amino.amino("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
  assert round(amino.amino("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
  assert round(amino.amino("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)
except:
  print("Failed assertions in part 1")
try:
  assert round(amino.aminos("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
  assert round(amino.aminos("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
  assert round(amino.aminos("MSRSLLLRFLLFLLLLPPLP")) == 65
except:
  print("Failed assertions in part 2")
  