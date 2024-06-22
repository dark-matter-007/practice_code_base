import cx_Freeze
import sys

sys.argv.append('build')

My_exe = [cx_Freeze.Executable('ScriptFile.py')]

cx_Freeze.setup (
    name = 'particle DOdger',
    options = {
        'build_exe' :\
             {'packages' : ['pygame', 'random'],
        \
        'include_files' : \
            [\
            "Alchemy.mp3",
            "Arrow.png",
            "Beside Me.mp3",
            "Carnage.mp3",
            "Darkside.mp3",
            "Falling Deeper.mp3",
            "Focus.mp3",
            "Hunter.mp3",
            "ICON.ico",
            "Ignite.mp3",
            "LOGO.png",
            "My Feelings.mp3",
            "Needed You.mp3",
            "Not Alone.mp3",
            "Particle.png"\
                ]}},
    executables = My_exe
)