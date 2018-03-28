# Level 1: Easy questions
Easy_questions = '''A__1__ (CLI)is a __2__ interface in which you can give the computer commands and receive some output.__3__has been used in__4__projects And often used for natural language processing.'''
Easy_answer=["command line interface","text based", "python","artificial intelligence"]

# Level 2: Medium questions
Medium_questions = '''__1__ is a high-level programming language designed to be easy to read and simple to implement python
features a dynamic type system and __2__ management. It supports multiple programming paradigms,
 including __3__,imperative,__4__ and procedural,and has a large and comprehensive standard library.'''
Medium_answer= ["python", "automatic memory","object-oriented","functional"]

# Level 3: Hard Questions
Hard_questions = '''Python uses__1__ typing, and a combination of __2__ and a cycle-detecting garbage collector for __3__. It also features dynamic 
 name resolution (late binding), which binds method and __4__ names during program execution.'''
Hard_answer=["dynamic","reference counting","memory management","variable"]


# Function used to prompt a player to choose a level of difficulty.
def choose_a_level():
    # The string player chooses to answer questions depending on level chosen
    print "Please Select a Difficulty Level for the game!!!"
    print "Enter in upper case only,check your CAPS LOCK key"
    level_name=raw_input(["Enter your difficulty level: Easy,Medium, or Hard :"])
    if level_name=="Easy":
        print "\nEasy level has been selected.\n" + Easy_questions
        return right_wrong_ans(Easy_questions,Easy_answer)
    elif level_name=="Medium":
        print "\nMedium level has been selected.\n" + Medium_questions
        return right_wrong_ans(Medium_questions,Medium_answer)
    elif level_name =="Hard":
        print "\nHard level has been selected.\n" + Hard_questions
        return right_wrong_ans(Hard_questions,Hard_answer)
    else:
        print "Try again!You Typed incorrectly." 
        choose_a_level()


# Function that loops through right or wrong answers of a given question
# and prints out whether answer chosen was correct or not.
def right_wrong_ans(questions,answer):    
    blank=0
    while blank<len(answer):
        user_input=raw_input("\nWhat is your answer to __" + str(blank + 1) + "?")
        if user_input==answer[blank]:
            print "Your answer was correct.\n"
            blank+=1
            questions=questions.replace("__" + str(blank) + "__", user_input)
            print(questions)
        else:
            print "Wrong Answer,Please try again.\n"
            print raw_input("\n Reenter the Correct answer,You got one more chances")
       
       
#Main Function that prompts the user to play,continue playing, or exixt the game.
def main():
    
     print "Let's play a game!\n"
     print  choose_a_level()
     print raw_input("\n Your knowledge is good,Thanks for Playing")
     print raw_input("\n Press the enter key to Exit.")
main()



