import io
import gradio as gr
import matplotlib.pyplot as plt
from PIL import Image
from metrics import apply_entropy, plot_histogram

inp1 = Image.open("images/image1.png").convert("L")
inp2 = Image.open("images/image2.png").convert("L")

with gr.Blocks() as demo:
    with gr.Row():
            gr.Label("Entropy", show_label=False)
    with gr.Row():
        with gr.Column(scale=2):
            with gr.Row():
                input_image_1 = gr.Image(value=inp1, label="Image 1", type="pil", interactive=True, height=600)
                input_image_2 = gr.Image(value=inp2, label="Image 2", type="pil", interactive=True, height=600)
            with gr.Row():
                hist_1 = gr.Image(label="Histogram of Image 1", type="pil", interactive=False)
                hist_2 = gr.Image(label="Histogram of Image 2", type="pil", interactive=False)
        with gr.Column(scale=1):
            with gr.Row():
                button1 = gr.Button("Show Histogram")
                button2 = gr.Button("Calculate Enropy")
            with gr.Row():
                entropy1 = gr.Number("0", label="Entropy of Image 1")
                entropy2 = gr.Number("0", label="Entropy of Image 2")


    button1.click(plot_histogram, inputs=[input_image_1, input_image_2], outputs=[hist_1, hist_2])
    button2.click(apply_entropy, inputs=[input_image_1, input_image_2], outputs=[entropy1, entropy2])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, debug=True)