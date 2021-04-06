import turtle
import pandas

screen = turtle.Screen() #creating screen object
screen.title("U.S. States Game") #giving the title
image = "blank_states_img.gif" #adding path of the image
screen.addshape(image) #adding image file shape
turtle.shape(image)

data = pandas.read_csv("50_states.csv") #telling pandas to read csv file
all_states = data.state.to_list() #converting into list of every state name from csv file
guessed_states = []

#as user needs to play for all of the states
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",#giving scores in a title we use guessed states length
                                    prompt="What's another state's name?").title() #taking user's input & .title() so that if user write in lower/upper case it will be ok until they give the wrong spelling
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states: #that means its missing state
                missing_states.append(state) #append to the missing states
        new_data = pandas.DataFrame(missing_states) #new data been created with all missing states &its a one column dataframe
        new_data.to_csv("states_to_learn.csv") #converting into csv
        break #if user writes exit then while loop will end

# if answer_state is one of the state in all states of the 50_states.csv
    if answer_state in all_states:
        guessed_states.append(answer_state) #everytime user adds new answer that will append to the guesssed state
        t = turtle.Turtle() #if they got the right answer then we need to create the title to go with the state name in exact location
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] # to hold the actual row(state,x,y) of corresponds to this state
        t.goto(int(state_data.x), int(state_data.y)) #turtle needs to go correct location..X & Y is going to correspond to the state that user has correctly guessed & the row of data from our 50_states.csv & also make the x & y's value int
        t.write(answer_state) # then turtle will write the state name in yhe image at exact location
