"""
    According to Gary Chapman, marriage counselor and the author of "The Five Love Languages" books, there are five major ways
    to express our love towards someone: words of affirmation, quality time, gifts, acts of service, and physical touch. These
    are called the love languages. Usually, everyone has a main language: the one that he/she "speaks" and understands best. In
    a relationship, it's import to find your partner's main love language, so that you get along better with each other.

    Your task:
    Unfortunately, your relationship got worse lately... After a long discussion with your partner, you agreed to give yourself a few
    weeks to improve it, otherwise you split up... You will be given a partner instance, and n weeks. The partner has a .response method,
    and the responses may be: "positive" or "neutral". You can try to get a response once a day, thus you have n * 7 tries in total to find
    the main love language of your partner!

    The love languages are: "words", "acts", "gifts", "time", "touch" (available predefined as LOVE_LANGUAGES)

    Note: your partner may (and will) sometimes give a positive response to any love language ("false positive"), but the main one has
    a much higher possibility. On the other hand, you may get a neutral response even for the main language, but with a low possibility ("false negative").

    There will be 50 tests. Although it's difficult to fail, in case you get unlucky, just run the tests again. After all, a few weeks may not be enough...

    Examples:
    main love language: "words"

    partner.response("words")  -->  "positive"
    partner.response("acts")   -->  "neutral"
    partner.response("words")  -->  "positive"
    partner.response("time")   -->  "neutral"
    partner.response("acts")   -->  "positive"    # false positive
    partner.response("gifts")  -->  "neutral"
    partner.response("words")  -->  "neutral"     # false negative
    etc.
    
    Happy coding, and DO try this at home! :-)
"""

import numpy as np
import random
def love_language(partner, weeks):
    # Brute Force Attempt
    responses = [0,0,0,0,0] # Make a log 5 entries long (5 love languages). This represents a "score" value
    for i in range(weeks*7): # attempt n * 7 times
        attempt = np.random.randint(0,4) # Choose a random number between 0 and 4 (represents a random index of LOVE_LANGUAGES) and attempt to get partner response
        response = partner.response(LOVE_LANGUAGES[attempt]) # Get the partner's response
        if response == "positive": # if the reponse returned is positive:
            responses[attempt] += 1 # Incriment the "score" value
        else: # Otherwise
            responses[attempt] -= 1 # Decrement the "score" value
    return LOVE_LANGUAGES[responses.index(max(responses))] # return the index containing the highest score within responses and use it as the index of LOVE_LANGUAGES
