import os  # Importing the OS module for working with file paths

from renamer_logic import rename_files  # Importing a function from renamer_logic module
import customtkinter  # Importing customtkinter module
from CTkMessagebox import CTkMessagebox  # Importing CTkMessagebox class from CTkMessagebox module


class SubtitleRenamerApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()  # Initializing the custom Tkinter application
        
        # Setting up the main window title and size
        self.title("Subtitle Renamer")
        self.geometry("600x380")

        # Initializing variables for user choices and subtitle format
        self.choice_var = customtkinter.IntVar(value=1)  # Default choice is Different directory
        self.sub_format_var = customtkinter.StringVar(value=".srt")  # Default subtitle format is .srt

        # Creating GUI widgets
        self.create_widgets()

    def create_widgets(self):
        # Creating a frame for organizing widgets
        frame = customtkinter.CTkFrame(self)
        frame.pack(pady=20)  # Packing the frame with padding

        # Creating radio buttons for choosing directory options
        customtkinter.CTkLabel(frame, text="Choose option:").pack(side=customtkinter.LEFT, padx=15)
        choices = [("Different directory", 1), ("Current directory", 2)]
        for text, mode in choices:
            customtkinter.CTkRadioButton(frame, text=text, variable=self.choice_var, value=mode).pack(side=customtkinter.LEFT, padx=10)

        # Creating entry fields for video directory, subtitle directory, and subtitle format
        customtkinter.CTkLabel(self, text="Video directory:").pack()
        self.vid_path_entry = customtkinter.CTkEntry(self, width=500)
        self.vid_path_entry.pack()

        customtkinter.CTkLabel(self, text="Subtitle directory:").pack()
        self.sub_path_entry = customtkinter.CTkEntry(self, width=500)
        self.sub_path_entry.pack()

        customtkinter.CTkLabel(self, text="Subtitle format (e.g., .sub, .srt):").pack()
        customtkinter.CTkEntry(self, textvariable=self.sub_format_var, width=50).pack()

        # Creating a button to trigger file renaming
        customtkinter.CTkButton(self, text="Rename Files", command=self.on_submit).pack(pady=10)

        # Adding GitHub and website information frames
        githubInfo = customtkinter.CTkFrame(self)
        githubInfo.pack(side=customtkinter.LEFT)
        websiterInfo = customtkinter.CTkFrame(self)
        websiterInfo.pack(side=customtkinter.RIGHT)

        customtkinter.CTkLabel(githubInfo, text="GitHub : AbdallaNassar").pack(pady=5, padx=10)
        customtkinter.CTkLabel(websiterInfo, text="Website : abdallanassar.me").pack(pady=5, padx=10)

    def on_submit(self):
        # Function to handle the file renaming process
        
        # Getting user input values
        choice = self.choice_var.get()  # Get the chosen directory option
        sub_format = self.sub_format_var.get().strip()  # Get and strip the entered subtitle format

        vid_path = self.vid_path_entry.get().strip()  # Get and strip the entered video directory path
        sub_path = self.sub_path_entry.get().strip()  # Get and strip the entered subtitle directory path

        # If choice is 2, set video and subtitle paths to current working directory
        if choice == 2:
            vid_path = os.getcwd()
            sub_path = os.getcwd()

        # Calling the function to rename files, capturing success and message
        success, message = rename_files(vid_path, sub_path, sub_format)

        # Handling success or failure of file renaming
        if success:
            # Display success message using CTkMessagebox
            CTkMessagebox(message=message, icon="check", option_1="Thanks")
        else:
            # Display error message using CTkMessagebox
            CTkMessagebox(title="Error", message=message, icon="cancel")


if __name__ == "__main__":
    # Running the SubtitleRenamerApp if this script is executed directly
    app = SubtitleRenamerApp()
    app.mainloop()  # Start the Tkinter main loop
