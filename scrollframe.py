import tkinter as tk
from tkinter import ttk

class ScrollableFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Set the background color to white
        self.configure(bg="white")  # Use `configure` instead of `config` to avoid recursion

        # Create a canvas with a white background
        self.canvas = tk.Canvas(self, bg="white", highlightthickness=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a vertical scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas to work with the scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Create a frame inside the canvas to hold content
        self.content_frame = tk.Frame(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")

        # Bind mousewheel scrolling for Windows and Linux/Mac
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind_all("<Button-4>", self._on_mousewheel)  # Linux/Mac scroll up
        self.canvas.bind_all("<Button-5>", self._on_mousewheel)  # Linux/Mac scroll down

    def _on_mousewheel(self, event):
        """Handle mousewheel scrolling."""
        if event.delta:  # Windows
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif event.num == 4:  # Linux/Mac scroll up
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:  # Linux/Mac scroll down
            self.canvas.yview_scroll(1, "units")

    def config(self, **kwargs):
        """Override the config method to allow resizing and other configurations."""
        if hasattr(self, "content_frame"):  # Ensure content_frame exists before configuring
            self.content_frame.config(**kwargs)
        self.canvas.config(**kwargs)
        super().config(**kwargs)