import subprocess

year = input("What year would you like to write on? ")
word = input("What would you like to write? ")

subprocess.run(["mkdir", "{}-{}".format(year, word)])
 