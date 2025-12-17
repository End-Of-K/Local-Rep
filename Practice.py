import gradio as gr

with gr.Blocks() as demo:
    with gr.Tab("Calculator Test"):
        a = gr.Number(label="Input A")
        b = gr.Number(label="Input B")
        
        with gr.Row():
            add_button = gr.Button("Add")
            times_button = gr.Button("Multiply")
            minus_button = gr.Button("Subtract")
            split_button = gr.Button("Divide")
        
        # Consistent naming: lowercase for variable names is standard
        res_add = gr.Number(label="Sum Result")
        res_mul = gr.Number(label="Times Result")
        res_sub = gr.Number(label="Minus Result")
        res_div = gr.Number(label="Split Result")
        
        # Logic Functions
        def add(num1, num2):
            return num1 + num2

        def multiply(num1, num2):
            return num1 * num2

        def subtract(num1, num2):
            return num1 - num2

        def divide(num1, num2):
            if num2 == 0:
                return 0 # Avoid division by zero error
            return num1 / num2

        # Event Listeners
        add_button.click(add, inputs=[a, b], outputs=res_add)
        times_button.click(multiply, inputs=[a, b], outputs=res_mul)
        minus_button.click(subtract, inputs=[a, b], outputs=res_sub)
        split_button.click(divide, inputs=[a, b], outputs=res_div)

demo.launch()