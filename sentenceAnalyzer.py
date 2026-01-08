text = """
The programming language Python was conceived in the late 1980s, and its implementation was started in December
1989 by Guido van Rossum at CWI in the Netherlands as a successor to ABC capable of exception handling and 
interfacing with the Amoeba operating system. Van Rossum is Python's principal author, and his continuing central
role in deciding the direction of Pyton is reflected in the title given to him by the Python community, Benevolent
Dictator for Life(BDFL). Python was named for the BBC TV show Monthly Python's Flying Circus
"""

def text_analyzer(text):
    solution = { }
    for c in text:
        c = c.lower()
        if c in solution:
            solution[c] += 1
        else:
            solution[c] = 1
    return solution

letter_frequencies = text_analyzer(text)
for c in letter_frequencies:
    print("The letter",c,"repeats",letter_frequencies[c], "times")
