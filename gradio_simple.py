import gradio as gr
from dotenv import load_dotenv
from research_manager import run

load_dotenv(override=True)

async def run_all(query:str):
    async for status_update in run(query):
        yield status_update

with gr.Blocks() as ui:
    query_textbox = gr.Textbox(label = "What topic would you like to research?")
    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")
    
    run_button.click(run_all, inputs=query_textbox, outputs=report)
    query_textbox.submit(run_all, inputs=query_textbox, outputs=report)

ui.launch(theme=gr.themes.Default(primary_hue="sky"))