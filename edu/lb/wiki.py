import wikipedia
# Search for a page
results = wikipedia.search('Python (programming language)')
# Get the summary of the first result
summary = wikipedia.summary(results[0])
print(summary)