from random import random
import gradio as gr

number = 0
attempts = 0

def reset_game_logic():
    global number, attempts
    number = random.randint(1, 100)
    attempts = 1

def restart_game():
    reset_game_logic()
    return "Game restarted! I've picked a new number"


def number_guessing(guess_number):
    global number, attempts
    guess = guess_number

    response = f"Attempt:{attempts} Enter your guess : "
    attempts += 1

    if guess.isdigit():
        if int(guess) > 100:
            return "Please enter number below 100"
            
        elif int(guess) < 0:
            return "Please enter number greater than 0"

        elif int(guess) == number:
            reset_game_logic()
            return "Congratulations! Your guess is correct"
            

        elif int(guess) < number:
            return "Your guess is too low"

        else:
            return "Your guess is too high"

    else:
        return "Enter Integer only"
    
reset_game_logic()


with gr.Blocks (title="Number Guessing Game") as demo:
    gr.Markdown("## Number Guessing Game")
    gr.Markdown("### Guess a number between 1 and 100!")
    
    with gr.Row():
        input_area = gr.Textbox(label="Enter your guess")
        output_area = gr.Textbox(label="Result")
    
    with gr.Row():
        submit_btn = gr.Button("Submit", variant="primary")
        restart_btn = gr.Button("Restart", variant="stop")

    submit_btn.click(
        fn=number_guessing,
        inputs=input_area,
        outputs=output_area
    )
    restart_btn.click(
        fn=restart_game,
        inputs=None,
        outputs=output_area
    )
    
demo.launch()