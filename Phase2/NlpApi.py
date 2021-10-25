import argparse

from google.cloud import language_v1



def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print(
            "Sentence {} has a sentiment score of {}".format(index, sentence_sentiment)
        )

    print(
        "Overall Sentiment: score of {} with magnitude of {}".format(score, magnitude)
    )
    return 0




def analyze(tweets):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language_v1.LanguageServiceClient()

    with open(tweets, "r") as review_file:
        # Instantiates a plain text document.
        content = review_file.read()

    document = language_v1.Document(content=content, type_=language_v1.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(request={'document': document})

    # Print the results
    print_result(annotations)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("tweets", help="The filename of the movie review you'd like to analyze.")
    args = parser.parse_args()

    analyze(args.tweets)