import gradio as gr
import re

custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Poppins:wght@300;400;600&display=swap');
body, html { margin: 0 !important; height: 100vh !important; background: #0f0c29; }
.gradio-container { max-width: 100% !important; margin: 0 !important; height: 100vh !important; background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%) !important; }
.sidebar-panel {
    background: rgba(0, 0, 0, 0.2) !important;
    backdrop-filter: blur(20px) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
    height: 100vh !important;
    padding: 25px !important;
}
.title-text {
    font-family: 'Orbitron', sans-serif;
    background: linear-gradient(90deg, #00d4ff, #f5576c, #ffffff, #00d4ff);
    background-size: 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3.2rem;
    font-weight: 700;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 5px;
    animation: gradientMove 8s linear infinite;
}
@keyframes gradientMove { 0% { background-position: 0% 50%; } 100% { background-position: 300% 50%; } }
"""

with gr.Blocks(css=custom_css, title="Session Normale 2 Master 2 IABD") as interface:
    with gr.Row(equal_height=True):
        with gr.Column(scale=1, elem_classes="sidebar-panel"):
            gr.HTML("""
                <div style='text-align: center; margin-bottom: 20px;'>
                    <h1 style='color:#00d4ff; font-family:Orbitron; margin: 10px 0 0 0; font-size:1.5em;'>Hello World!</h1>
                </div>
            """)
            gr.Markdown("---")

if __name__ == "__main__": interface.launch(show_api=False)