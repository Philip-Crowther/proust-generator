import pandas as pd

# open book
file = open("InSearchOfLostTime.txt", "r")

# save book as string
full_text = file.read()

# close file
file.close()

# split text into paragraphs
full_text = full_text.split("\n\n")

# attach empty prompts
full_text = [("", paragraph) for paragraph in full_text]

# put into dataframe 
df = pd.DataFrame(full_text, columns=["prompt", "completion"])

# save dataframe as csv
df.to_csv("training_data.csv", index=False)
