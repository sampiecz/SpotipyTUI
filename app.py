from command import CommandHandler
import time
import curses



class MusicPlayer(object):

    def __init__(self, stdscreen):
        self.run(stdscreen)

    def run(self, stdscreen):
        self.runLoop(stdscreen)

    def runLoop(self, stdscreen):

        command_handler = CommandHandler(stdscreen)
        search_key = 115
        select_key = ord('\n')
        client_key = 99
        quit_key = 113
        goto_index_key = 105
        move_up_key = curses.KEY_UP
        move_down_key = curses.KEY_DOWN
        next_song_key = curses.KEY_RIGHT
        prev_song_key = curses.KEY_LEFT

        command_dict = {
                        move_up_key : command_handler.moveUp,
                        move_down_key : command_handler.moveDown,
                        next_song_key : command_handler.nextSong,
                        prev_song_key : command_handler.prevSong,
                        search_key : command_handler.searchContent,
                        select_key : command_handler.currentSong,
                        client_key : command_handler.showClient,
                        goto_index_key : command_handler.playAtIndex,
                      }

        self.intro(stdscreen)

        while True:
                char_input = stdscreen.getch()

                if char_input == quit_key:
                    break;
                elif char_input in command_dict:
                    command_dict.get(char_input)()


    def intro(self, stdscreen):
        intro_text = '''


                .d88888b                      dP   oo                            d888888P dP     dP dP
                88.    "'                     88                                    88    88     88 88
                `Y88888b. 88d888b. .d8888b. d8888P dP 88d888b. dP    dP             88    88     88 88
                      `8b 88'  `88 88'  `88   88   88 88'  `88 88    88 88888888    88    88     88 88
                d8'   .8P 88.  .88 88.  .88   88   88 88.  .88 88.  .88             88    Y8.   .8P 88
                 Y88888P  88Y888P' `88888P'   dP   dP 88Y888P' `8888P88             dP    `Y88888P' dP
                          88                          88            .88
                          dP                          dP        d8888P

                ~Spotify-TUI (Spotify Terminal User Interface)
                    Control the Spotify Desktop Client from this text-based interface
                    Python 3.0+

                ~ Key Commands:
                    Up-Arrow and Down-Arrow: Traverse Search Results
                    Left-Arrow: Play Previous Song (Based on current cursor position)
                    Right-Arrow: Play Next Song (Based on current cursor position)
                    S: Search for music
                    I: Jump to song at index within search results
                    H: Help (Shows list of commands)
                    C: Show Spotify Client
                    Q: Quit
                   '''

        intro_x = int(stdscreen.getmaxyx()[1]/2)
        intro_y = int(stdscreen.getmaxyx()[0]/10)

        stdscreen.addstr(intro_y, intro_x, intro_text)






def run():
    player = MusicPlayer
    curses.wrapper(player)


run()
