import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


# Functions
def calc_APW(nc: float, enh: float, delayed: float) -> float:
    """
    Calculate APW (Absolute Percentage Washout)

    Parameters:
        nc (float): Non-contrast HU
        enh (float): Enhanced HU
        delayed (float): Delayed HU

    Returns: APW (float)
    """
    APW = (enh - delayed) / (enh - nc)
    return APW

# Input Frame
class InputFrame(ctk.CTkFrame):
    """Input Frame for NC, Enhanced, Delayed in HU"""

    def __init__(self, *args, header_name="InputFrame", **kwargs):
        super().__init__(*args, **kwargs)
        
        ## Header
        self.header = ctk.CTkLabel(self, text=header_name, font=ctk.CTkFont(weight="bold"))
        self.header.grid(row=0, columnspan = 2)

        # NC
        ## NC Label
        self.label_nc = ctk.CTkLabel(self, text="Non Contrast (HU):", font=ctk.CTkFont(weight="bold"))
        self.label_nc.grid(row=1, column=0, pady=10, padx=(10, 5), sticky=tk.E)
        ## NC Entry
        self.entry_nc = ctk.CTkEntry(master=self, placeholder_text="(HU)", width=100)
        #self.entry_nc.pack(padx=20, pady=10)
        self.entry_nc.grid(row=1, column=1, pady=10, padx=(0, 10) )

        # Enhanced
        ## Enhanced Label
        self.label_enh = ctk.CTkLabel(self, text="Enhanced (HU):", font=ctk.CTkFont(weight="bold"))
        self.label_enh.grid(row=2, column=0, pady=(0, 10), padx=(10, 5), sticky=tk.E)
        ## Enhanced Entry
        self.entry_enh = ctk.CTkEntry(master=self, placeholder_text="(HU)", width=100)
        #self.entry_enh.pack(padx=20, pady=10)
        self.entry_enh.grid(row=2, column=1, pady=(0, 10), padx=(0, 10) )

        # Delayed
        ## Delayed Label
        self.label_delayed = ctk.CTkLabel(self, text="Delayed (HU):", font=ctk.CTkFont(weight="bold"))
        self.label_delayed.grid(row=3, column=0, pady=(0, 10), padx=(10, 5), sticky=tk.E)
        ## Delayed Entry
        self.entry_delayed = ctk.CTkEntry(master=self, placeholder_text="(HU)", width=100)
        #self.entry_delayed.pack(padx=20, pady=10)
        self.entry_delayed.grid(row=3, column=1, pady=(0, 10), padx=(0, 10) )

    # Get Input Parameter
    def get_input(self):
        input = {"nc": float(self.entry_nc.get()),
                 "enh": float(self.entry_enh.get()),
                 "delayed": float(self.entry_delayed.get())}
        return input

    # Get APW
    def get_apw(self):
        nc = float(self.entry_nc.get())
        enh = float(self.entry_enh.get())
        delayed = float(self.entry_delayed.get())
        APW = calc_APW(nc, enh, delayed)
        return(APW)

# Output Frame
# class OutputFrame(customtkinter.CTkFrame):
#     """Output Frame"""
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def show(self, APW=""):
#         text = f"""APW: {APW}"""
#         self.show_text = customtkinter.CTkLabel(self, text="Haha")
#         self.show_text.pack()

# Main App
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.minsize(500, 300)
        # App Title (Outside)
        self.title("Adrenal CT Washout Calculator App")

        # App Title (Inside)
        self.logo_label = ctk.CTkLabel(self, text="Adrenal CT Washout Calculator", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(pady = 10)

        # Input Frame for HU
        self.inputframe = InputFrame(self, header_name="Input HU")
        self.inputframe.pack()

        # Output Frame
        # self.outputframe = OutputFrame(self)
        # self.outputframe.pack()

        # Output TextBox
        self.output_textbox = ctk.CTkTextbox(self, height = 150, width = 300) 
        self.output_textbox.pack(padx=20, pady=20)
        

        # Button: Calculate
        self.button_calc = ctk.CTkButton(self, text="Calculate", command=self.calc_APW_app)
        self.button_calc.pack(padx=20, pady=20)

    # Calculate
    def calc_APW_app(self):
        APW = self.inputframe.get_apw()
        input = self.inputframe.get_input()
        print(f"Absolute Washout: {APW}") # To console
        # self.output = customtkinter.CTkLabel(self, text = f"APW: {APW}")
        # self.output.pack()
        APW_pretty = round(APW*100, 2)
        self.output_textbox.delete("0.0", "end")  # delete all text
        self.output_textbox.insert("0.0", 
                                   "Result\n\n" +

                                   f"APW = {APW_pretty}%\n\n" +

                                   f"- NC: {input['nc']} HU\n" +
                                   f"- Enhanced: {input['enh']} HU\n" +
                                   f"- Delayed: {input['delayed']} HU"
                                                         
                                   )




if __name__ == "__main__":
    app = App()
    app.mainloop()