import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math

class GraphingCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Graphing Calculator")
        self.root.geometry("1000x700")
        
        # Variables
        self.expression = tk.StringVar()
        self.x_min = tk.DoubleVar(value=-10)
        self.x_max = tk.DoubleVar(value=10)
        self.y_min = tk.DoubleVar(value=-10)
        self.y_max = tk.DoubleVar(value=10)
        
        self.setup_ui()
        self.fig = None
        self.canvas = None
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Control panel (left side)
        control_frame = ttk.Frame(main_frame, width=250)
        control_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 10))
        
        # Title
        title_label = ttk.Label(control_frame, text="Graphing Calculator", 
                               font=("Arial", 14, "bold"))
        title_label.pack(pady=10)
        
        # Expression input
        ttk.Label(control_frame, text="Enter function f(x):").pack(anchor=tk.W)
        ttk.Entry(control_frame, textvariable=self.expression, width=25).pack(fill=tk.X, pady=5)
        ttk.Label(control_frame, text="Examples: x**2, sin(x), sqrt(x), 1/x").pack(anchor=tk.W, 
                                                                                     font=("Arial", 8))
        
        # X-axis range
        ttk.Label(control_frame, text="X-axis range:").pack(anchor=tk.W, pady=(15, 5))
        range_frame = ttk.Frame(control_frame)
        range_frame.pack(fill=tk.X, pady=5)
        ttk.Label(range_frame, text="Min:").pack(side=tk.LEFT)
        ttk.Entry(range_frame, textvariable=self.x_min, width=8).pack(side=tk.LEFT, padx=5)
        ttk.Label(range_frame, text="Max:").pack(side=tk.LEFT)
        ttk.Entry(range_frame, textvariable=self.x_max, width=8).pack(side=tk.LEFT)
        
        # Y-axis range
        ttk.Label(control_frame, text="Y-axis range:").pack(anchor=tk.W, pady=(15, 5))
        range_frame2 = ttk.Frame(control_frame)
        range_frame2.pack(fill=tk.X, pady=5)
        ttk.Label(range_frame2, text="Min:").pack(side=tk.LEFT)
        ttk.Entry(range_frame2, textvariable=self.y_min, width=8).pack(side=tk.LEFT, padx=5)
        ttk.Label(range_frame2, text="Max:").pack(side=tk.LEFT)
        ttk.Entry(range_frame2, textvariable=self.y_max, width=8).pack(side=tk.LEFT)
        
        # Buttons
        ttk.Button(control_frame, text="Plot Graph", command=self.plot_graph).pack(fill=tk.X, pady=10)
        ttk.Button(control_frame, text="Clear", command=self.clear_graph).pack(fill=tk.X, pady=5)
        
        # Calculator section
        ttk.Label(control_frame, text="Quick Calculator", 
                 font=("Arial", 12, "bold")).pack(pady=(20, 10))
        
        calc_frame = ttk.Frame(control_frame)
        calc_frame.pack(fill=tk.X)
        
        self.calc_expression = tk.StringVar()
        ttk.Entry(calc_frame, textvariable=self.calc_expression, width=25).pack(fill=tk.X)
        ttk.Button(calc_frame, text="Calculate", command=self.calculate).pack(fill=tk.X, pady=5)
        
        self.calc_result = tk.StringVar(value="Result: ")
        ttk.Label(calc_frame, textvariable=self.calc_result, 
                 foreground="blue", wraplength=200).pack(anchor=tk.W, pady=5)
        
        # Info section
        info_text = """Supported Functions:
• sin, cos, tan
• asin, acos, atan
• sinh, cosh, tanh
• sqrt, log, log10, exp
• abs, ceil, floor
• Operators: +, -, *, /, **"""
        
        ttk.Label(control_frame, text=info_text, font=("Arial", 8), 
                 justify=tk.LEFT).pack(anchor=tk.W, pady=(20, 0))
        
        # Graph panel (right side)
        graph_frame = ttk.Frame(main_frame)
        graph_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.graph_canvas_frame = graph_frame
        self.create_empty_plot()
        
    def create_empty_plot(self):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        
        self.fig = Figure(figsize=(6.5, 6.5), dpi=100)
        ax = self.fig.add_subplot(111)
        ax.text(0.5, 0.5, "Enter a function and click 'Plot Graph'", 
               horizontalalignment='center', verticalalignment='center',
               transform=ax.transAxes)
        ax.set_xlim(self.x_min.get(), self.x_max.get())
        ax.set_ylim(self.y_min.get(), self.y_max.get())
        ax.grid(True, alpha=0.3)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_canvas_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    def plot_graph(self):
        expr = self.expression.get().strip()
        if not expr:
            messagebox.showwarning("Input Error", "Please enter a function")
            return
        
        try:
            x_min = self.x_min.get()
            x_max = self.x_max.get()
            y_min = self.y_min.get()
            y_max = self.y_max.get()
            
            # Generate x values
            x = np.linspace(x_min, x_max, 1000)
            
            # Create safe namespace for eval
            safe_dict = {
                'x': x,
                'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
                'asin': np.arcsin, 'acos': np.arccos, 'atan': np.arctan,
                'sinh': np.sinh, 'cosh': np.cosh, 'tanh': np.tanh,
                'sqrt': np.sqrt, 'log': np.log, 'log10': np.log10,
                'exp': np.exp, 'abs': np.abs, 'ceil': np.ceil,
                'floor': np.floor, 'pi': np.pi, 'e': np.e,
                'np': np
            }
            
            # Evaluate expression
            y = eval(expr, {"__builtins__": {}}, safe_dict)
            
            # Create plot
            if self.canvas:
                self.canvas.get_tk_widget().destroy()
            
            self.fig = Figure(figsize=(6.5, 6.5), dpi=100)
            ax = self.fig.add_subplot(111)
            
            # Plot with handling for discontinuities
            ax.plot(x, y, 'b-', linewidth=2, label=f'f(x) = {expr}')
            ax.set_xlim(x_min, x_max)
            ax.set_ylim(y_min, y_max)
            ax.set_xlabel('x', fontsize=10)
            ax.set_ylabel('f(x)', fontsize=10)
            ax.set_title('Graph', fontsize=12, fontweight='bold')
            ax.grid(True, alpha=0.3)
            ax.legend(fontsize=9)
            ax.axhline(y=0, color='k', linewidth=0.5)
            ax.axvline(x=0, color='k', linewidth=0.5)
            
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_canvas_frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        except Exception as e:
            messagebox.showerror("Plotting Error", f"Error: {str(e)}")
    
    def clear_graph(self):
        self.expression.set("")
        self.calc_expression.set("")
        self.calc_result.set("Result: ")
        self.create_empty_plot()
    
    def calculate(self):
        expr = self.calc_expression.get().strip()
        if not expr:
            messagebox.showwarning("Input Error", "Please enter an expression")
            return
        
        try:
            safe_dict = {
                'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
                'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
                'sinh': math.sinh, 'cosh': math.cosh, 'tanh': math.tanh,
                'sqrt': math.sqrt, 'log': math.log, 'log10': math.log10,
                'exp': math.exp, 'abs': abs, 'ceil': math.ceil,
                'floor': math.floor, 'pi': math.pi, 'e': math.e
            }
            
            result = eval(expr, {"__builtins__": {}}, safe_dict)
            self.calc_result.set(f"Result: {result:.6f}")
        except Exception as e:
            messagebox.showerror("Calculation Error", f"Error: {str(e)}")

def main():
    root = tk.Tk()
    app = GraphingCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()


