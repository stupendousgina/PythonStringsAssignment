"""
1. Product Review Analysis

Task 1: Keyword Highlighter

Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.

    reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."
"""
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
keywords = ["good", "excellent", "bad", "poor", "average"]

for review_string in reviews:
    each_review = [each_word.split(' ') for each_word in review_string.split('. ')]
    for sep_text in each_review:
        for tex in sep_text: 
            if tex.lower() in keywords:
                highlight = tex.upper()
                new_highlighted_review = review_string.replace(tex, highlight)
                print(f"{new_highlighted_review}\n")

"""
Task 2: Sentiment Tally

Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.

    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

"""
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
both = negative_words + positive_words
total = [[],[]]
def counting_words(reviews_list):
    global total
    if reviews_list:
        for review_string in reviews_list:
            each_review = [each_word.split(' ') for each_word in review_string.split('. ')]
            for sep_text in each_review:
                for tex in sep_text:
                    if tex.lower() in positive_words:
                        count_pos = review_string.count(tex)
                        print(f"This review has {count_pos} positive word. \n{review_string}\n")
                        total[0].append(tex)
                    elif tex.lower() in negative_words:
                        count_neg = review_string.count(tex)
                        print(f"This review has {count_neg} negative word. \n{review_string}\n")
                        total[1].append(tex)
        if sep_text[:] not in both:        
            print(f"This review has 0 positive and negative words. \n{review_string[:]}\n")
    return print(f"Total positive words: {len(total[0])}\nTotal negative words: {len(total[1])}\n")
        
counting_words(reviews)

"""

Task 3: Review Summary

Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

Example: "This product is really good. I'm...",


"""
for review_string in reviews:
    each_review = [each_word.split(' ') for each_word in review_string.split('. ')]
    beg = review_string[:30]
    end = review_string[30:]

    if beg.endswith(" "):
        summary = beg.strip() + '...'
    elif end.startswith(" "):
        summary = beg.strip() + '...'

    for sep_text in each_review:    
        for tex in sep_text: 
            if tex not in beg and tex not in end:
                mid = tex
                for char in mid:
                    if char == review_string[30]:
                        i = mid.index(char)
                        ending = mid[i:]
                        summary = beg + ending + '...'
    print(summary)

    