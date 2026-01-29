import random
import gradio as gr


def game(user_choice):

    if user_choice is None:
        return "Please select Rock, Paper, or Scissor first!"

    comp_choice = random.choice(['rock', 'paper', 'scissor'])
    comp_win_combo = {"rock":"scissor", "paper" : "rock",  "scissor" : "paper"}

    if user_choice in comp_win_combo:
        if comp_win_combo[comp_choice] == user_choice:
            return f"You chose {user_choice.title()} while computer chose {comp_choice.title()}!\nComputer Wins"
        
        elif comp_choice == user_choice:
            return f"You chose {user_choice.title()} while computer chose {comp_choice.title()}!\nIts draw"
        
        else:
            return f"You chose {user_choice.title()} while computer chose {comp_choice.title()}!\nYou Win"
        
    else:
        print("Invalid input. Please enter 'r' or 'p' or 's'")


with gr.Blocks (title="Day 2: Rock Paper Scissor") as demo:
    gr.Markdown("# Rock Paper Scissor Game")
    
    with gr.Column():
        input_area=gr.Radio(choices=["rock", "paper", "scissor"], label="Choose any option below", )
        submit_btn= gr.Button("Play", variant="primary")
        output_area= gr.Textbox(label="Game Result", lines=2)

    submit_btn.click(
        fn=game,
        inputs=input_area,
        outputs=output_area
    )

demo.launch()