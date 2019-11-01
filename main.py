from classifier.Naive_Bayes import classify
from producer import Producer
import time

if __name__ == "__main__":
    tweets = ["301733794770190336 RT @aliwilgus: @tweetsoutloud How serious is NASA's commitment to the SLS and Orion programs, and the future of human space flight beyon ...", "301576909517619200 RT @FardigJudith: This line in the President's State of the Union Address spoke to me. Check it out &amp; share your #SOTU #CitizenRespo ...", "305052368305790976 Did you know we're also on @Facebook? This week we welcomed our 300,000th fan. Join us! http://t.co/nvFSQOXZYn http://t.co/0DbAj61aQT"]
    #classify(tweets)

    with open('tweets.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            message = line.split(' ', 1)[1]
            topic = classify([line])

            Producer(topic, message)
            time.sleep(2)
