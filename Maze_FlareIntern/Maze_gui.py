# Author: Shivang Chaudhary
# Education: King's College London - University of London (2023-2024)
# Date: 26/06/2024
# ----
# Using python kivy to effectively produce the working GUI for generating mazes.
# Can be packaged for IOS and Android applications.
# The following code deploys the GUI on local machine's window.
# ----

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from Maze_algorithm import prim_maze
from kivy.config import Config

# Setting the window size
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '650')
Config.set('graphics', 'resizable', False)


# Main function to run the GUI for the maze application: -
class MazeApp(App):
    def build(self):
        #layout = BoxLayout(orientation='vertical')
        layout = FloatLayout()

        # Adding background image
        background = Image(source='images/grass_Back.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        # Creating a grid layout for the maze
        self.grid = GridLayout(cols=21, size_hint=(1, 1), pos_hint={'center_x': .5, 'center_y': .5})

        # Button to generate a new maze
        self.button = Button(size_hint=(0.08, 0.1), pos_hint={'x':.46, 'y':0.9}, background_normal='images/stop-button.png')
        self.button.bind(on_press=self.generate_maze)

        # Add the grid layout and the button to the main layout
        layout.add_widget(self.grid)
        layout.add_widget(self.button)

        # Generating the initial maze
        self.generate_maze(None)

        return layout

    def generate_maze(self, instance):
        self.grid.clear_widgets()
        # Specifying dimensions for the maze
        maze = prim_maze(21, 21)
        # Following is the array of 1s and 0s specifying arrangement in a grid
        maze_data = maze

        # The following is add images to maze elements respectively.
        for row in maze_data:
            for cell in row:
                if cell == '#' :
                    image_source = 'images/wall.png'
                if cell == ' ':
                    image_source = 'images/grass.png'
                if cell == '0':
                    image_source = 'images/location.png'
                # Add image to grid layout, making sure it fits within the grid
                self.grid.add_widget(Image(source=image_source, size_hint=(.7, .7), size=(30, 30)))


# Run the application: -
if __name__ == '__main__':
    MazeApp().run()
