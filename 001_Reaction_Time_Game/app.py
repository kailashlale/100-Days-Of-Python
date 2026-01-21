import gradio as gr
import time
from random import random

def start_game(state):
    time.sleep(random.uniform(1, 8))
    start_time = time.perf_counter()
    return "GO!", {"start_time": start_time}

def stop_game(state):
    start_time = state.get("start_time", 0)
    if start_time == 0:
        return "You must press Start first & wait for Game message 'GO'!", "", state
    end_time = time.perf_counter()
    total_time = end_time - start_time

    return "Click 'Start Game' to play again", f"You took {total_time*1000:.0f} milliseconds to react", {"start_time": 0}

with gr.Blocks(title="Reflex Game") as app:
    gr.Markdown("## Reflex Game")
    
    game_state = gr.State({"start_time": 0})
    
    with gr.Row():
        start_btn = gr.Button("Start Game", variant="primary")
        stop_btn = gr.Button("Stop Timer", variant="stop")
    with gr.Row():
        message_area = gr.Textbox(label="Game Message")
        result_area = gr.Textbox(label="Reflex Time")
    start_btn.click(
        fn=start_game, 
        inputs=game_state, 
        outputs=[message_area, game_state]
    )
    
    stop_btn.click(
        fn=stop_game, 
        inputs=game_state, 
        outputs=[message_area, result_area, game_state]
    )

app.launch()
