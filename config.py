# List of owned games, 1 per line. Game name must match lookup.
# Defaults to inside the plugin directory unless changed. To change, put the path inside the "", for example: game_list = r"G:\My Games\PSP\PSP-list.txt"
game_list = r""

# .DAT file for lookup.
# Defaults to inside the plugin directory unless changed. To change, put the path inside the "", for example: game_dat = r"G:\My Games\PSP\PSP.dat"
game_dat = r""

# Location of 'installed' local games, which are a possible subset of owned games.
# As an example, it could look like this: roms_path = r"G:\My Games\PSP"
roms_path = r"REQUIRED_FOR_LOCAL_GAMES"

# Path to emulator executable.
# As an example, it could look like this: emu_path = r"G:\My Emulator\myemulator.exe"
emu_path = r"REQUIRED_FOR_LOCAL_GAMES"
# Optional. Example: emu_args = [ r"--fullscreen", r"-l" ]
emu_args = []

# Optional - pick a username, if desired. This is what will be displayed on the Settings Integrations list screen. 
username = "Username"