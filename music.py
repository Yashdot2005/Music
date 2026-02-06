import time
import sys

def print_lyrics():
    lyrics = [
        "Haathon ko sambhale mere haathon mein",
        "Kaise haathon ko sambhale mere haathon mein",
        "Kab tak neend na aaye, inn lakeeron mein",
        "Baatein ho..."
    ]
    delays = [1.0, 0.1, 1.12, 0.9, 0.8] 

    print("Arz kya hai...")
    time.sleep(1.4)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1) 
        time.sleep(delays[i]) 
        print()

if __name__ == "__main__":
    print_lyrics()