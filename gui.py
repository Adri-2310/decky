import ttkbootstrap as ttk

def screen_init(title : str, size : str,):
    root = ttk.Window(themename='superhero')
    root.title(title)
    root.geometry(size)
    #root.resizable(False, False)
    root.place_window_center()

    # configure grid root
    root.columnconfigure(0, weight=1)
    root.rowconfigure(3, weight=1)

    screen_widget(root)
    return root


def play_game():
    pass


def replay_game():
    pass


def screen_widget(window:ttk.Window):
    # frame
    frame_top = ttk.Frame(window)
    frame_top.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    frame_bottom = ttk.Frame(window, padding=10)

    # create widgets top frame
    ttk.Label(frame_top,text="Timer").pack(side="left",padx=10,pady=2)
    ttk.Spinbox(frame_top, from_=0, to=100,width=5).pack(side="left",padx=10,pady=2)
    ttk.Label(frame_top,text="s.").pack(side="left")
    ttk.Spinbox(frame_top, from_=0, to=100,width=5).pack(side="left",padx=10,pady=2)
    ttk.Label(frame_top,text="lettres").pack(side="left",padx=10,pady=2)
    ttk.Button(frame_top,text="Jouer",command=play_game).pack(side="right",padx=10,pady=2)

    # creat widgets bottom frame
    ttk.Button(frame_bottom,text="Rejouer",command=replay_game).pack(side="left")
    ttk.Button(frame_bottom,text="Quitter",command=window.destroy).pack(side="right")

    # input
    ttk.Entry(window).grid(row=1, column=0, sticky="ew")
    ttk.Label(window, text="0",anchor="center").grid(row=2, column=0,sticky="ew")
    ttk.Canvas(window).grid(row=3, column=0, sticky="nsew")
    ttk.Label(window, text="Label",anchor="center").grid(row=4, column=0,sticky="ew")
    frame_bottom.grid(row=5, column=0, sticky="ew")

