import re

def solve(feedbacks):
    # Use regular expression to split by any non-word character (like ; or ,)
    # This handles "positive;negative" and "positive,negative" equally
    feedback_list = re.split(r'[^a-zA-Z0-9]+', feedbacks)

    net_score = 0

    for item in feedback_list:
        sentiment = item.strip().lower()

        if sentiment == "positive":
            net_score += 1
        elif sentiment == "negative":
            net_score -= 1
        elif sentiment == "neutral":
            net_score += 0

    return net_score

print(solve("neutral;negative;positive;negative"))