import time
import random

SENTENCES = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "porta lorem mollis aliquam ut porttitor leo a diam sollicitudin tempor id eu nisl nunc mi ipsum faucibus vitae aliquet",
    "Montes nascetur ridiculus mus mauris vitae ultricies leo integer malesuada. Tortor posuere ac ut consequat semper viverra nam libero",
    "Ut diam quam nulla porttitor. Dignissim sodales ut eu sem integer vitae justo. Mi ipsum faucibus vitae aliquet nec. Cursus risus at ultrices mi.",
    "Tristique nulla aliquet enim tortor. Etiam sit amet nisl purus in mollis nunc sed. At augue eget arcu dictum varius duis"
]

def calculate_accuracy(typed_sentence, original_sentence):
    typed_chars = list(typed_sentence)
    original_chars = list(original_sentence)

    matches = sum(1 for a, b in zip(typed_chars, original_chars) if a == b)

    return round((matches / len(original_chars)) * 100, 2)

def speed_test():
    sentence = random.choice(SENTENCES)
    print("Type this: '" + sentence + "'")

    input("Press enter when you are ready to start")

    start_time = time.time()
    typed_sentence = input("\nGo!\n")
    end_time = time.time()

    time_elapsed = round(end_time - start_time, 2)
    words_per_minute = round((len(typed_sentence.split()) / time_elapsed) * 60, 2)

    accuracy = calculate_accuracy(typed_sentence, sentence)

    print("Total time elapsed: {:.2f} seconds".format(time_elapsed))
    print("Your average typing speed was {:.2f} words per minute".format(words_per_minute))
    print("Your accuracy was {:.2f}%".format(accuracy))

    if typed_sentence == sentence:
        print("Well done! You typed the sentence correctly.")
    else:
        print("You made a mistake. Try again.")

if __name__ == "__main__":
    speed_test()
