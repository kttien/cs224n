# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import model
import trainer
import utils
import argparse

def main():
    argp = argparse.ArgumentParser()
    argp.add_argument('--eval_corpus_path',
        help="Path of the corpus to evaluate on", default=None)
    args = argp.parse_args()
    prediction = ["London" for i in range(len(open(args.eval_corpus_path).readlines()))]
    print(len(prediction))
    total, correct = utils.evaluate_places(args.eval_corpus_path, prediction)
    print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))


if __name__ == "__main__":
    main()
