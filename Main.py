import threading 
import matplotlib
import pandas as pd
import tkinter as tk
from pandasgui import show
matplotlib.use('TkAgg')
from tkinter import ttk
import MetaTrader5 as mt5
from datetime import datetime
from mplfinance.original_flavor import candlestick_ohlc
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tabulate import tabulate
# === Styles === #
import mplcyberpunk
from matplotlib import style

# === For Graph Updates === #
import matplotlib.animation as animation
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker

# === Get data from utils de engine sem impacto de performance === #
from Trade_Engine.App_v2 import Agent_TA
from Trade_Engine.utils import Utils

LARGE_FONT = ('Verdana', 12)
NORM_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)


style.use('seaborn-v0_8-darkgrid') 
# seaborn-v0_8-dark
# seaborn-v0_8
# cyberpunk
# dark_background
# Solarize_Light2

mt5.initialize()
mt5.login(51116412,'39sz2vL3', 'ICMarketsSC-Demo')


# === Graph Plot === #
f = plt.figure()

exchange = 'EURUSD'
marketType = 'CAMBIAL'
forceupdate = 9000
programName = 'eurusd' 
resampleSize = '15Min'
dataPace = 'tick'
candleWidth = 0.008

paneCount = 1

topIndicator = 'None'
middleIndicator = 'None'
bottomIndicator = 'None'
chartLoad = True
decisionLoad = True

EMAs = []
SMAs = []




def tutorial():

    def page2():
        tut.destroy()
        tut2 = tk.Tk()

        def page3():
            tut2.destroy()
            tut3 = tk.Tk()

            tut3.wm_title("Part 3!")

            label = ttk.Label(tut3, text="Part 3", font=NORM_FONT)
            label.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(tut3, text="Done!", command= tut3.destroy)
            B1.pack()
            tut3.mainloop()

        tut2.wm_title("Part 2!")
        label = ttk.Label(tut2, text="Part 2", font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(tut2, text="Next", command= page3)
        B1.pack()
        tut2.mainloop()
    
    tut = tk.Tk()
    tut.wm_title("Tutorial")
    label = ttk.Label(tut, text="What do you need help with?", font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)

    B1 = ttk.Button(tut, text="Overview of the application", command=page2 )
    B1.pack()
    B2 = ttk.Button(tut, text="How do i trade with this client?", command=lambda: popupmsg("Not yet completed"))
    B2.pack()
    B3 = ttk.Button(tut, text="Indicator Questions/Help", command=lambda: popupmsg("Not yet completed"))
    B3.pack()

    tut.mainloop()

def loadChart(run):
    global chartLoad

    if run == 'Start':
        chartLoad = True

    elif run == 'Stop':
        chartLoad = False

def DecisionLoad(run):
    global decisionLoad

    if run == 'Start':
        decisionLoad = True

    elif run == 'Stop':
        decisionLoad = False

def addMiddleIndicator(what):
    global middleIndicator
    global forceupdate

    if dataPace == 'tick':
        popupmsg("Indicators in Tick Data not available")

    if what != 'None':
        if middleIndicator == 'None':
            if what == 'sma':
                midIQ = tk.Tk()
                midIQ.wm_title('Periods?')
                label = ttk.Label(midIQ, text="Choose Periods of SMA")
                label.pack(side='top', fill='x', pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global forceupdate

                    middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append('sma')
                    group.append(int(periods))
                    middleIndicator.append(group)
                    forceupdate = 9000
                    print('middle indicator set to:', middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()
            
            if what == 'ema':
                midIQ = tk.Tk()
                midIQ.wm_title('Periods?')
                label = ttk.Label(midIQ, text="Choose Periods of EMA")
                label.pack(side='top', fill='x', pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global forceupdate

                    middleIndicators = []
                    periods = (e.get())
                    group = []
                    group.append('ema')
                    group.append(int(periods))
                    middleIndicator.append(group)
                    forceupdate = 9000
                    print('middle indicator set to:', middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()

        else:
            if what == 'sma':
                midIQ = tk.Tk()
                midIQ.wm_title('Periods?')
                label = ttk.Label(midIQ, text="Choose Periods of SMA")
                label.pack(side='top', fill='x', pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global forceupdate

                    periods = (e.get())
                    group = []
                    group.append('sma')
                    group.append(int(periods))
                    middleIndicator.append(group)
                    forceupdate = 9000
                    print('middle indicator set to:', middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()

            if what == 'ema':
                midIQ = tk.Tk()
                midIQ.wm_title('Periods?')
                label = ttk.Label(midIQ, text="Choose Periods of EMA")
                label.pack(side='top', fill='x', pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global forceupdate

                    periods = (e.get())
                    group = []
                    group.append('ema')
                    group.append(int(periods))
                    middleIndicator.append(group)
                    forceupdate = 9000
                    print('middle indicator set to:', middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()
    else:
        middleIndicator = 'None'

def addTopIndicator(what):
    global topIndicator 
    global forceupdate

    if dataPace == 'tick':
        popupmsg("Indicators in Tick Data not available")
    
    elif what == 'None':
        topIndicator = what
        forceupdate = 9000
    elif what == 'rsi':
        rsiQ = tk.Tk()
        rsiQ.wm_title('Periods?')
        label = ttk.Label(rsiQ, text= "Choose how many periods you want each RSI calculation to consider.")
        label.pack(side='top', fill='x', pady=10)

        e = ttk.Entry(rsiQ)
        e.insert(0,14)
        e.pack()
        e.focus_get()

        def callback():
            global topIndicator
            global forceupdate

            periods = (e.get())
            group = []
            group.append('rsi')
            group.append(periods)

            topIndicator = group
            forceupdate = 9000
            print("Set top indicator to", group)
            rsiQ.destroy()

        b = ttk.Button(rsiQ, text="Submit", width=10, command=callback)
        b.pack()
        tk.mainloop()
    
    elif what == 'macd':
        topIndicator = "macd"
        forceupdate = 9000

def addBottomIndicator(what):
    global bottomIndicator 
    global forceupdate

    if dataPace == 'tick':
        popupmsg("Indicators in Tick Data not available")
    elif what == 'None':
        bottomIndicator = what
        forceupdate = 9000
    elif what == 'rsi':
        rsiQ = tk.Tk()
        rsiQ.wm_title('Periods?')
        label = ttk.Label(rsiQ, text= "Choose how many periods you want each RSI calculation to consider.")
        label.pack(side='top', fill='x', pady=10)

        e = ttk.Entry(rsiQ)
        e.insert(0,14)
        e.pack()
        e.focus_get()

        def callback():
            global bottomIndicator
            global forceupdate

            periods = (e.get())
            group = []
            group.append('rsi')
            group.append(periods)

            bottomIndicator = group
            forceupdate = 9000
            print("Set top indicator to", group)
            rsiQ.destroy()

        b = ttk.Button(rsiQ, text="Submit", width=10, command=callback)
        b.pack()
        tk.mainloop()
    
    elif what == 'macd':
        bottomIndicator = "macd"
        forceupdate = 9000

def changeTimeFrame(tf):
    global dataPace
    global forceupdate
    if tf == '7d' and resampleSize == '1Min':
        popupmsg("Too much data chosen, choose a smaller time frame or higher OHLC interval")
    else:
        dataPace = tf
        forceupdate = 9000

def changeSampleSize(size, width):
    global resampleSize
    global forceupdate
    global candleWidth
    if dataPace == '7d' and resampleSize == '1Min':
        popupmsg("Too much data chosen, choose a smaller time frame or higher OHLC interval")
    
    if dataPace == 'tick':
        popupmsg("You're currently viewing tick data, not OHLC.")
    
    else:
        resampleSize = size
        forceupdate = 9000
        candleWidth = width

def changeExchange(toWhat, pn):
    global exchange
    global forceupdate
    global programName

    exchange = toWhat
    programName = pn
    forceupdate = 9000

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side='top', fill='x', pady=10)
    B1 = ttk.Button(popup, text='Okay', command=popup.destroy)
    B1.pack()
    popup.mainloop()

# === Periferico Dados Time Close Para Graph Base=== #
def animate(i):
    global refreshRate
    global forceupdate

    if chartLoad:
        if paneCount == 1:
            if dataPace == 'tick':

                a= plt.subplot2grid((6,4), (0,0), rowspan=5, colspan=4)
                a2= plt.subplot2grid((6,4), (5,0), rowspan=1, colspan=4, sharex = a)
                # Set the ticker
                ticker = exchange
                # Hourly
                data = pd.DataFrame(mt5.copy_rates_from_pos(ticker, mt5.TIMEFRAME_H1, 0, 1000))[['time', 'open', 'high', 'low', 'close','tick_volume']]
                data.rename(columns={'tick_volume': 'volume'}, inplace=True)
                # Convert time
                def unix_to_datetime(timestamp):
                    return datetime.utcfromtimestamp(timestamp)
                # Apply the function to the 'time' column
                data['time'] = data['time'].apply(unix_to_datetime)
                a.clear()
                a.plot_date(data['time'], data['close'], label='Closing Price')
                a2.fill_between(data['time'], 0, data['volume'], facecolor = "#183A54")
                a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
                title = '{} Live'.format(ticker)
                a.set_title(title)
            
            else:
                if forceupdate > 12:
                    if topIndicator != 'None' and bottomIndicator !='None':
                        # Main Graph
                        a = plt.subplot2grid((6,4),(1,0), rowspan=3, colspan=4)
                        # Volume
                        a2 = plt.subplot2grid((6,4),(4,0), sharex=a, rowspan=1, colspan=4)
                        # Bottom Indicator
                        a3 = plt.subplot2grid((6,4),(5,0), sharex=a, rowspan=1, colspan=4)
                        # Top Indicator
                        a0 = plt.subplot2grid((6,4),(0,0), sharex=a, rowspan=1, colspan=4)
                        a.remove()
                        a2.remove()
                        a3.remove()
                        a0.remove()
                    
                    elif topIndicator != 'None':
                        # Main Graph
                        a = plt.subplot2grid((6,4),(1,0), rowspan=4, colspan=4)
                        # Volume
                        a2 = plt.subplot2grid((6,4),(5,0), sharex=a, rowspan=1, colspan=4)
                        # Top Indicator
                        a0 = plt.subplot2grid((6,4),(0,0), sharex=a, rowspan=1, colspan=4)
                        a.remove()
                        a2.remove()
                        a0.remove()
                    
                    elif bottomIndicator != 'None':
                        # Main Graph
                        a = plt.subplot2grid((6,4),(0,0), rowspan=4, colspan=4)
                        # Volume
                        a2 = plt.subplot2grid((6,4),(4,0), sharex=a, rowspan=1, colspan=4)
                        # Bottom Indicator
                        a3 = plt.subplot2grid((6,4),(5,0), sharex=a, rowspan=1, colspan=4)
                        a.remove()
                        a2.remove()
                        a3.remove()
                    
                    else:
                        # Main Graph
                        a = plt.subplot2grid((6,4),(0,0), rowspan=5, colspan=4)
                        # Volume
                        a2 = plt.subplot2grid((6,4),(5,0), sharex=a, rowspan=1, colspan=4)
                        a.remove()
                        a2.remove()
        
                    if topIndicator != 'None' and bottomIndicator != 'None':
                        a3.remove()
                        a0.remove()
                    elif topIndicator != 'None':
                        a0.remove()
                    elif bottomIndicator != 'None':
                        a3.remove()
                    
                    forceupdate +=1

class TabulateLabel(tk.Label):
    def __init__(self, parent, data, **kwargs):
        super().__init__(parent, 
                         font=('Consolas', 10), 
                         justify=tk.LEFT, anchor='nw', **kwargs)

        text = tabulate(data, headers='keys', tablefmt='github', showindex=False)
        self.configure(text=text)

# === MAIN === # 

class Matrisapp(tk.Tk):
   
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand= True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # == Settings == #
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Save settings', command = lambda: popupmsg("Not Supported Just Yet!"))
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=quit)
        menubar.add_cascade(label='File', menu=filemenu)

        # == Exchange == #
        exchangeChoice =  tk.Menu(menubar, tearoff=1)
        exchangeChoice.add_command(label='EURUSD',
                                   command=lambda: changeExchange('EURUSD','eurusd'))
        exchangeChoice.add_command(label='EURJPY',
                                   command=lambda: changeExchange('EURJPY','eurjpy'))
        exchangeChoice.add_command(label='USDJPY',
                                   command=lambda: changeExchange('USDJPY','usdjpy'))
        exchangeChoice.add_command(label='EURCHF',
                                   command=lambda: changeExchange('EURCHF','eurchf'))
        menubar.add_cascade(label='Exchange', menu=exchangeChoice)

        # == Data Time Frame == #
        dataTimeFrame = tk.Menu(menubar, tearoff=1)
        dataTimeFrame.add_command(label = 'Tick',
                                  command=lambda: changeTimeFrame('tick'))
        dataTimeFrame.add_command(label = '30 Min',
                                  command=lambda: changeTimeFrame('30min'))
        dataTimeFrame.add_command(label = '1 Hour',
                                  command=lambda: changeTimeFrame('1hour'))
        menubar.add_cascade(label='Data Time Frame', menu=dataTimeFrame)

        # == OHLCI interval == #
        OHLCI = tk.Menu(menubar, tearoff=1)
        OHLCI.add_command(label='Tick',
                          command=lambda: changeTimeFrame('tick'))
        OHLCI.add_command(label='1 Minute',
                          command=lambda: changeSampleSize('1 M', 0.0005))
        OHLCI.add_command(label='5 Minutes',
                          command=lambda: changeSampleSize('5 M', 0.003))
        OHLCI.add_command(label='15 Minutes',
                          command=lambda: changeSampleSize('15 M', 0.008))
        OHLCI.add_command(label='30 Minutes',
                          command=lambda: changeSampleSize('30 M', 0.016))
        OHLCI.add_command(label='1 Hour',
                          command=lambda: changeSampleSize('1 H', 0.032))
        OHLCI.add_command(label='3 Hours',
                          command=lambda: changeSampleSize('3 H', 0.096))
        OHLCI.add_command(label='1 Day',
                          command=lambda: changeSampleSize('1 D', 0.096))
        menubar.add_cascade(label='OHLC Interval ', menu=OHLCI)

        # == Indicators == #
        # = Top indicators -> Over graph
        topIndi = tk.Menu(menubar, tearoff=1)
        topIndi.add_command(label='None',
                          command=lambda: addTopIndicator('None'))
        topIndi.add_command(label='RSI',
                          command=lambda: addTopIndicator('rsi'))
        topIndi.add_command(label='MACD',
                          command=lambda: addTopIndicator('macd'))
        menubar.add_cascade(label='Top Indicator ', menu=topIndi)
        filemenu.add_separator()
        
        # = Main indicators -> Over graph
        mainI = tk.Menu(menubar, tearoff=1)
        mainI.add_command(label='None',
                          command=lambda: addMiddleIndicator('None'))
        mainI.add_command(label='SMA',
                          command=lambda: addMiddleIndicator('sma'))
        mainI.add_command(label='EMA',
                          command=lambda: addMiddleIndicator('ema'))
        menubar.add_cascade(label='Main Indicator ', menu=mainI)

        # = Bottom indicators -> Over graph
        bottomI = tk.Menu(menubar, tearoff=1)
        bottomI.add_command(label='None',
                          command=lambda: addBottomIndicator('None'))
        bottomI.add_command(label='RSI',
                          command=lambda: addBottomIndicator('rsi'))
        bottomI.add_command(label='MACD',
                          command=lambda: addBottomIndicator('macd'))
        menubar.add_cascade(label='Bottom Indicator ', menu=bottomI)

        startStop = tk.Menu(menubar, tearoff=1)
        startStop.add_command(label = 'Auto-Trading System',
                                command=lambda: popupmsg("This is not live yet"))        
        startStop.add_separator()
        startStop.add_command(label = "Resume",
                              command=lambda: loadChart('start'))
        startStop.add_command(label = "Pause",
                              command=lambda: loadChart('stop'))
        menubar.add_cascade(label="Execute", menu= startStop)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Tutorial", command=tutorial)

        menubar.add_cascade(label="Help", menu = helpmenu)

        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (StartPage, HomePage, PageOne, PageTwo, PageThree):
                
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky='nsew')

        # tk.Tk.iconbitmap(self, default='') ## APP ICON
        self.show_frame(StartPage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# == Disclaimer == #
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Welcome to Matris Software', font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text='Agree', 
                            command=lambda: controller.show_frame(HomePage)) # Adição de variaveis por commands
        button1.pack()

        button2 = ttk.Button(self, text='Disagree', 
                    command=quit)
        button2.pack()

# == Home Page == #
class HomePage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Home Page', font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text='Decision', 
                            command=lambda: controller.show_frame(PageOne)) # Adição de variaveis por commands
        button1.pack()

        button2 = ttk.Button(self, text='Backtesting & Results', 
                            command=lambda: controller.show_frame(PageTwo)) # Adição de variaveis por commands
        button2.pack()

        button3 = ttk.Button(self, text='Auto Trading System', 
                            command= lambda: controller.show_frame(PageThree))      
        button3.pack()
    
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()  # Use draw instead of show
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # === Add a toolbar === # 
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# == Decision == #
class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Decision', font=('Helvetica', 16))
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text='Home Page', 
                            command=lambda: controller.show_frame(HomePage))  # Adição de variáveis por comandos
        button.pack()    

        button2 = ttk.Button(self, text='Backtesting & Results', 
                            command=lambda: controller.show_frame(PageTwo))  # Adição de variáveis por comandos
        button2.pack()

        button3 = ttk.Button(self, text='Auto Trading System', 
                            command= lambda: controller.show_frame(PageThree))      
        button3.pack()
 
# == Backtesting & Results == #
class PageTwo(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Backtesting & Results', font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text='Home Page', 
                            command=lambda: controller.show_frame(HomePage)) # Adição de variaveis por commands
        button.pack()

        button2 = ttk.Button(self, text='Decision', 
                            command=lambda: controller.show_frame(PageOne)) # Adição de variaveis por commands
        button2.pack()

        button3 = ttk.Button(self, text='Auto Trading System', 
                            command= lambda: controller.show_frame(PageThree))      
        button3.pack()

# == Auto Trading System == #
class PageThree(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Auto Trading System', font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text='Home Page', 
                            command=lambda: controller.show_frame(HomePage)) # Adição de variaveis por commands
        button.pack()

        button1 = ttk.Button(self, text='Decision', 
                            command=lambda: controller.show_frame(PageOne)) # Adição de variaveis por commands
        button1.pack()

        button2 = ttk.Button(self, text='Backtesting & Results', 
                            command=lambda: controller.show_frame(PageTwo))  # Adição de variáveis por comandos
        button2.pack()

        # Create Start and Stop buttons
        optimizer_button = ttk.Button(self, text='Start Trading', command=self.parameter_optimizer)
        optimizer_button.pack()

        # Create Start and Stop buttons
        start_button = ttk.Button(self, text='Start Trading', command=self.start_trading)
        start_button.pack()

        stop_button = ttk.Button(self, text='Stop Trading', command=self.stop_trading)
        stop_button.pack()

        # Flag to control the trading loop
        self.is_trading = False

        # Thread for trading
        self.trading_thread = None

        # Labels for displaying information
        self.label_tm = TabulateLabel(self, data="", bg='white')
        self.label_tm.pack()

        self.label_cp = TabulateLabel(self, data="", bg='white')
        self.label_cp.pack()

        self.label_sr = TabulateLabel(self, data="", bg='white')
        self.label_sr.pack()

        self.label_fb = TabulateLabel(self, data="", bg='white')
        self.label_fb.pack()

        self.label_decision = TabulateLabel(self, data="", bg='white')
        self.label_decision.pack()


    def start_trading(self):
        # Check if the trading thread is already running
        if self.trading_thread and self.trading_thread.is_alive():
            print("Trading is already in progress.")
            return

        self.is_trading = True
        self.trading_thread = threading.Thread(target=self.run_trading_loop)
        self.trading_thread.start()

    def stop_trading(self):
        self.is_trading = False
        if self.trading_thread and self.trading_thread.is_alive():
            self.trading_thread.join()


    def run_trading_loop(self):
        agent = Agent_TA()

        while self.is_trading:
            # Your trading logic goes here
            tm, cp, sr, fb, bg = agent.main(ut=Utils(exchange, marketType), ticker=exchange)

            # Update the labels with information from the results
            self.update_label(self.label_tm, tm.result_df)
            self.update_label(self.label_cp, cp.result_df)
            self.update_label(self.label_sr, sr.result_df)
            self.update_label(self.label_fb, fb.result_df)
            self.update_label(self.label_decision, bg.decision_df)

            # Show tables using pandasgui
            self.show_tables(tm.result_df, cp.result_df, sr.result_df, fb.result_df, bg.decision_df)

    def update_label(self, label, data):
        # Convert data to a string representation (adjust based on your data structure)
        data_str = str(data)
        # Update the label text
        label.config(text=data_str)

    def show_tables(self, tm_df, cp_df, sr_df, fb_df, decision_df):
        # Update TabulateLabel instances with new data
        self.label_tm.configure(data=tm_df)
        self.label_cp.configure(data=cp_df)
        self.label_sr.configure(data=sr_df)
        self.label_fb.configure(data=fb_df)
        self.label_decision.configure(data=decision_df)

    

app = Matrisapp()
app.geometry('1280x720')
ani = animation.FuncAnimation(f, animate, interval=1000, cache_frame_data=False)
app.mainloop()


