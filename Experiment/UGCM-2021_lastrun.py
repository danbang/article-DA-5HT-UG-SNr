#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.1),
    on September 03, 2024, at 13:37
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from visual_setup
txt_size = 0.05
title_size = 0.1

#text position log
txt_low = (0,-0.4)
txt_upright = (0.4,0.4)
# Run 'Before Experiment' code from code_13
ins1_main = 'In each round of this game, you will play with another person who will make an offer on how to split $20 with you.'
# Run 'Before Experiment' code from code_14
ins1_main = 'In each round of this game, you will play with another person who will make an offer on how to split $20 with you.'
# Run 'Before Experiment' code from code_15
ins1_main = 'In each round of this game, you will play with another person who will make an offer on how to split $20 with you.'
# Run 'Before Experiment' code from prc_code
dollarYp = "$ 5"
dollarOp = "$ 15"

dollarYpr = "$ 0"
dollarOpr = "$ 0"

# Run 'Before Experiment' code from code_16
ins1_main = 'In each round of this game, you will play with another person who will make an offer on how to split $20 with you.'
# Run 'Before Experiment' code from code_18
ins1_main = 'In each round of this game, you will play with another person who will make an offer on how to split $20 with you.'
# Run 'Before Experiment' code from code_17
ins1_main = 'In each round of this game, you will play with another person who will make an offer on how to split $20 with you.'
# Run 'Before Experiment' code from main_code
import random

txt_size = 0.04
txt_small = 0.035
title_size = 0.1
image_Yloc = [-0.13,0]
image_Ploc = [0.13,0]
Accbox_loc = [-0.11,-0.17]
Rejbox_loc = [0.09, -0.17]

#no control offer debug version
#noControl = [3,2,3]
#random.shuffle(noControl)

#offer list
nc_first = [5]
nc_offer = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9]

#mood sample
mood_set = [[0,1],[0,1],[0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]
#mood_set = [[0,0,1]]
random.shuffle(mood_set)
mood = [item for l in mood_set for item in l]

#trigger key listen
kb = keyboard.Keyboard()
trigger_list = []

#condition folder directory
conditionfolder = ''

#fixation
jitter = [1.8, 1.6, 2.1, 1.9, 2.2, 1.9, 2.3, 1.5, 2.2, 1.5, 1.6, 1.8, 2.1, 2.4, 2.3, 2.0, 1.5, 1.7, 2.0, 2.2, 1.5, 1.8, 2.4, 2.2, 2.4, 2.5, 2.0, 1.8, 1.9, 2.3]
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.1'
expName = 'UG2-mood'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '00',
    'condition': '',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1920, 1080]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\fuq01\\Downloads\\UGC-mood-OR\\UGCM-2021_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=(1.0000, 1.0000, 1.0000), colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = (1.0000, 1.0000, 1.0000)
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('ins_key') is None:
        # initialise ins_key
        ins_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ins_key',
        )
    if deviceManager.getDevice('ins1_key') is None:
        # initialise ins1_key
        ins1_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ins1_key',
        )
    if deviceManager.getDevice('ins1_key_2') is None:
        # initialise ins1_key_2
        ins1_key_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ins1_key_2',
        )
    if deviceManager.getDevice('ins1_key_3') is None:
        # initialise ins1_key_3
        ins1_key_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ins1_key_3',
        )
    if deviceManager.getDevice('ins1_key_4') is None:
        # initialise ins1_key_4
        ins1_key_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ins1_key_4',
        )
    if deviceManager.getDevice('choice_key_2') is None:
        # initialise choice_key_2
        choice_key_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='choice_key_2',
        )
    if deviceManager.getDevice('ins1_key_5') is None:
        # initialise ins1_key_5
        ins1_key_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ins1_key_5',
        )
    if deviceManager.getDevice('choice_key_3') is None:
        # initialise choice_key_3
        choice_key_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='choice_key_3',
        )
    if deviceManager.getDevice('ins1_key_6') is None:
        # initialise ins1_key_6
        ins1_key_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ins1_key_6',
        )
    if deviceManager.getDevice('ExpStart_key') is None:
        # initialise ExpStart_key
        ExpStart_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ExpStart_key',
        )
    if deviceManager.getDevice('team_key') is None:
        # initialise team_key
        team_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='team_key',
        )
    if deviceManager.getDevice('choice_key') is None:
        # initialise choice_key
        choice_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='choice_key',
        )
    if deviceManager.getDevice('slider_choose') is None:
        # initialise slider_choose
        slider_choose = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='slider_choose',
        )
    if deviceManager.getDevice('slider_move') is None:
        # initialise slider_move
        slider_move = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='slider_move',
        )
    if deviceManager.getDevice('expEnd_key') is None:
        # initialise expEnd_key
        expEnd_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='expEnd_key',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "ins_open" ---
    title = visual.TextStim(win=win, name='title',
        text='Deal Making Game',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    lowMid_open = visual.TextStim(win=win, name='lowMid_open',
        text='Press SPACE or UP to begin',
        font='Open Sans',
        pos=(0, -0.3), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='grey', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ins_key = keyboard.Keyboard(deviceName='ins_key')
    
    # --- Initialize components for Routine "ins1" ---
    upperRight = visual.TextStim(win=win, name='upperRight',
        text='Game Rules',
        font='Open Sans',
        pos=(0.4, 0.4), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='gray', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    main_txt = visual.TextStim(win=win, name='main_txt',
        text=ins1_main,
        font='Open Sans',
        pos=(0, 0), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    lowMid = visual.TextStim(win=win, name='lowMid',
        text='Press SPACE or UP to continue',
        font='Open Sans',
        pos=(0, -0.3), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='grey', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ins1_key = keyboard.Keyboard(deviceName='ins1_key')
    
    # --- Initialize components for Routine "ins2" ---
    upperRight_2 = visual.TextStim(win=win, name='upperRight_2',
        text='Game Rules',
        font='Open Sans',
        pos=(0.4, 0.4), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='gray', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    main_txt_2 = visual.TextStim(win=win, name='main_txt_2',
        text='If you choose to accept, both of you will receive the offered amounts.',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    lowMid_2 = visual.TextStim(win=win, name='lowMid_2',
        text='Press SPACE or UP to continue',
        font='Open Sans',
        pos=(0, -0.3), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='grey', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ins1_key_2 = keyboard.Keyboard(deviceName='ins1_key_2')
    
    # --- Initialize components for Routine "ins3" ---
    upperRight_3 = visual.TextStim(win=win, name='upperRight_3',
        text='Game Rules',
        font='Open Sans',
        pos=(0.4, 0.4), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='gray', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    main_txt_3 = visual.TextStim(win=win, name='main_txt_3',
        text='If you reject, neither of you will receive anything.',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    lowMid_3 = visual.TextStim(win=win, name='lowMid_3',
        text='Press SPACE or UP to begin PRACTICE',
        font='Open Sans',
        pos=(0, -0.3), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='grey', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ins1_key_3 = keyboard.Keyboard(deviceName='ins1_key_3')
    
    # --- Initialize components for Routine "prc_prep" ---
    
    # --- Initialize components for Routine "prc_ins1" ---
    upperRight_4 = visual.TextStim(win=win, name='upperRight_4',
        text='Practice round',
        font='Open Sans',
        pos=(0.4, 0.4), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='gray', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    main_txt_4 = visual.TextStim(win=win, name='main_txt_4',
        text='',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    lowMid_4 = visual.TextStim(win=win, name='lowMid_4',
        text='Press SPACE or UP to continue',
        font='Open Sans',
        pos=(0, -0.3), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='grey', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ins1_key_4 = keyboard.Keyboard(deviceName='ins1_key_4')
    
    # --- Initialize components for Routine "prc_present_acc" ---
    avatar_2 = visual.ImageStim(
        win=win,
        name='avatar_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.05), draggable=False, size=(0.25,0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    offer_txt_2 = visual.TextStim(win=win, name='offer_txt_2',
        text='Hannah proproses',
        font='Open Sans',
        pos=[0,-0.17], draggable=False, height=0.06, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    upperRight_5 = visual.TextStim(win=win, name='upperRight_5',
        text='Practice round',
        font='Open Sans',
        pos=(0.4, 0.4), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='gray', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "prc_offer_acc" ---
    you_txt_4 = visual.TextStim(win=win, name='you_txt_4',
        text='You',
        font='Open Sans',
        pos=[-0.10,0.2], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    partner_txt_4 = visual.TextStim(win=win, name='partner_txt_4',
        text='Hannah',
        font='Open Sans',
        pos=[0.10,0.2], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    dollar_Ytxt_4 = visual.TextStim(win=win, name='dollar_Ytxt_4',
        text=dollarYp,
        font='Open Sans',
        pos=[-0.10,0.15], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    dollar_Ptxt_4 = visual.TextStim(win=win, name='dollar_Ptxt_4',
        text=dollarOp,
        font='Open Sans',
        pos=[0.10,0.15], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    you_image_4 = visual.ImageStim(
        win=win,
        name='you_image_4', 
        image='cash/d5.png', mask=None, anchor='center',
        ori=0.0, pos=image_Yloc, draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-4.0)
    partner_image_4 = visual.ImageStim(
        win=win,
        name='partner_image_4', 
        image='cash/d15.png', mask=None, anchor='center',
        ori=0.0, pos=image_Ploc, draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-5.0)
    acc_txt_3 = visual.TextStim(win=win, name='acc_txt_3',
        text='Accept',
        font='Open Sans',
        pos=[-0.11,-0.17], draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    rej_txt_3 = visual.TextStim(win=win, name='rej_txt_3',
        text='Reject',
        font='Open Sans',
        pos=[0.09,-0.17], draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    acc_box_3 = visual.Rect(
        win=win, name='acc_box_3',
        width=(0.17, 0.1)[0], height=(0.17, 0.1)[1],
        ori=0.0, pos=Accbox_loc, draggable=False, anchor='center',
        lineWidth=4.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-8.0, interpolate=True)
    rej_box_3 = visual.Rect(
        win=win, name='rej_box_3',
        width=(0.17, 0.1)[0], height=(0.17, 0.1)[1],
        ori=0.0, pos=Rejbox_loc, draggable=False, anchor='center',
        lineWidth=4.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-9.0, interpolate=True)
    choice_key_2 = keyboard.Keyboard(deviceName='choice_key_2')
    acc_img = visual.ImageStim(
        win=win,
        name='acc_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.3, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-12.0)
    upperRight_6 = visual.TextStim(win=win, name='upperRight_6',
        text='Practice round',
        font='Open Sans',
        pos=(0.4, 0.4), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='gray', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    
    # --- Initialize components for Routine "prc_choice_acc" ---
    you_txt_5 = visual.TextStim(win=win, name='you_txt_5',
        text='You',
        font='Open Sans',
        pos=[-0.10,0.2], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    partner_txt_5 = visual.TextStim(win=win, name='partner_txt_5',
        text='Hannah',
        font='Open Sans',
        pos=[0.10,0.2], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    dollar_Ytxt_5 = visual.TextStim(win=win, name='dollar_Ytxt_5',
        text=dollarYp,
        font='Open Sans',
        pos=[-0.10,0.15], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    dollar_Ptxt_5 = visual.TextStim(win=win, name='dollar_Ptxt_5',
        text=dollarOp,
        font='Open Sans',
        pos=[0.10,0.15], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    you_image_5 = visual.ImageStim(
        win=win,
        name='you_image_5', 
        image='cash/d5.png', mask=None, anchor='center',
        ori=0.0, pos=image_Yloc, draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-5.0)
    partner_image_5 = visual.ImageStim(
        win=win,
        name='partner_image_5', 
        image='cash/d15.png', mask=None, anchor='center',
        ori=0.0, pos=image_Ploc, draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-6.0)
    acc_txt_4 = visual.TextStim(win=win, name='acc_txt_4',
        text='Accept',
        font='Open Sans',
        pos=[-0.11,-0.17], draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    rej_txt_4 = visual.TextStim(win=win, name='rej_txt_4',
        text='Reject',
        font='Open Sans',
        pos=[0.09,-0.17], draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    acc_box_4 = visual.Rect(
        win=win, name='acc_box_4',
        width=(0.17, 0.1)[0], height=(0.17, 0.1)[1],
        ori=0.0, pos=Accbox_loc, draggable=False, anchor='center',
        lineWidth=4.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-9.0, interpolate=True)
    rej_box_4 = visual.Rect(
        win=win, name='rej_box_4',
        width=(0.17, 0.1)[0], height=(0.17, 0.1)[1],
        ori=0.0, pos=Rejbox_loc, draggable=False, anchor='center',
        lineWidth=4.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-10.0, interpolate=True)
    upperRight_7 = visual.TextStim(win=win, name='upperRight_7',
        text='Practice round',
        font='Open Sans',
        pos=(0.4, 0.4), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='gray', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-12.0);
    
    # --- Initialize components for Routine "prc_reveal_acc" ---
    you_txt_6 = visual.TextStim(win=win, name='you_txt_6',
        text='You get:',
        font='Open Sans',
        pos=[-0.13,0.2], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    partner_txt_6 = visual.TextStim(win=win, name='partner_txt_6',
        text='Hannah gets:',
        font='Open Sans',
        pos=[0.13,0.2], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    dollar_Ytxt_6 = visual.TextStim(win=win, name='dollar_Ytxt_6',
        text=dollarYp,
        font='Open Sans',
        pos=[-0.10,0.15], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    dollar_Ptxt_6 = visual.TextStim(win=win, name='dollar_Ptxt_6',
        text=dollarOp,
        font='Open Sans',
        pos=[0.10,0.15], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    you_image_6 = visual.ImageStim(
        win=win,
        name='you_image_6', 
        image='cash/d5.png', mask=None, anchor='center',
        ori=0.0, pos=image_Yloc, draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-5.0)
    partner_image_6 = visual.ImageStim(
        win=win,
        name='partner_image_6', 
        image='cash/d15.png', mask=None, anchor='center',
        ori=0.0, pos=image_Ploc, draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-6.0)
    upperRight_8 = visual.TextStim(win=win, name='upperRight_8',
        text='Practice round',
        font='Open Sans',
        pos=(0.4, 0.4), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='gray', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    
    # --- Initialize components for Routine "prc_ins2" ---
    upperRight_9 = visual.TextStim(win=win, name='upperRight_9',
        text='Practice round',
        font='Open Sans',
        pos=(0.4, 0.4), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='gray', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    main_txt_5 = visual.TextStim(win=win, name='main_txt_5',
        text='Let’s see what happens when you reject.',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    lowMid_5 = visual.TextStim(win=win, name='lowMid_5',
        text='Press SPACE or UP to continue',
        font='Open Sans',
        pos=(0, -0.3), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='grey', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ins1_key_5 = keyboard.Keyboard(deviceName='ins1_key_5')
    
    # --- Initialize components for Routine "prc_present_rej" ---
    avatar_3 = visual.ImageStim(
        win=win,
        name='avatar_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.05), draggable=False, size=(0.25,0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    offer_txt_3 = visual.TextStim(win=win, name='offer_txt_3',
        text='Hannah proproses',
        font='Open Sans',
        pos=[0,-0.17], draggable=False, height=0.06, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    upperRight_10 = visual.TextStim(win=win, name='upperRight_10',
        text='Practice round',
        font='Open Sans',
        pos=(0.4, 0.4), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='gray', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "prc_offer_rej" ---
    you_txt_7 = visual.TextStim(win=win, name='you_txt_7',
        text='You',
        font='Open Sans',
        pos=[-0.10,0.2], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    partner_txt_7 = visual.TextStim(win=win, name='partner_txt_7',
        text='Hannah',
        font='Open Sans',
        pos=[0.10,0.2], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    dollar_Ytxt_7 = visual.TextStim(win=win, name='dollar_Ytxt_7',
        text=dollarYp,
        font='Open Sans',
        pos=[-0.10,0.15], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    dollar_Ptxt_7 = visual.TextStim(win=win, name='dollar_Ptxt_7',
        text=dollarOp,
        font='Open Sans',
        pos=[0.10,0.15], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    you_image_7 = visual.ImageStim(
        win=win,
        name='you_image_7', 
        image='cash/d5.png', mask=None, anchor='center',
        ori=0.0, pos=image_Yloc, draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-4.0)
    partner_image_7 = visual.ImageStim(
        win=win,
        name='partner_image_7', 
        image='cash/d15.png', mask=None, anchor='center',
        ori=0.0, pos=image_Ploc, draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-5.0)
    acc_txt_5 = visual.TextStim(win=win, name='acc_txt_5',
        text='Accept',
        font='Open Sans',
        pos=[-0.11,-0.17], draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    rej_txt_5 = visual.TextStim(win=win, name='rej_txt_5',
        text='Reject',
        font='Open Sans',
        pos=[0.09,-0.17], draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    acc_box_5 = visual.Rect(
        win=win, name='acc_box_5',
        width=(0.17, 0.1)[0], height=(0.17, 0.1)[1],
        ori=0.0, pos=Accbox_loc, draggable=False, anchor='center',
        lineWidth=4.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-8.0, interpolate=True)
    rej_box_5 = visual.Rect(
        win=win, name='rej_box_5',
        width=(0.17, 0.1)[0], height=(0.17, 0.1)[1],
        ori=0.0, pos=Rejbox_loc, draggable=False, anchor='center',
        lineWidth=4.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-9.0, interpolate=True)
    choice_key_3 = keyboard.Keyboard(deviceName='choice_key_3')
    rej_img = visual.ImageStim(
        win=win,
        name='rej_img', 
        image='development/UG-Mood_Instruction/Slide10.jpg', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.3, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-12.0)
    upperRight_11 = visual.TextStim(win=win, name='upperRight_11',
        text='Practice round',
        font='Open Sans',
        pos=(0.4, 0.4), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='gray', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    
    # --- Initialize components for Routine "prc_choice_rej" ---
    you_txt_8 = visual.TextStim(win=win, name='you_txt_8',
        text='You',
        font='Open Sans',
        pos=[-0.10,0.2], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    partner_txt_8 = visual.TextStim(win=win, name='partner_txt_8',
        text='Hannah',
        font='Open Sans',
        pos=[0.10,0.2], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    dollar_Ytxt_8 = visual.TextStim(win=win, name='dollar_Ytxt_8',
        text=dollarYp,
        font='Open Sans',
        pos=[-0.10,0.15], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    dollar_Ptxt_8 = visual.TextStim(win=win, name='dollar_Ptxt_8',
        text=dollarOp,
        font='Open Sans',
        pos=[0.10,0.15], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    you_image_8 = visual.ImageStim(
        win=win,
        name='you_image_8', 
        image='cash/d5.png', mask=None, anchor='center',
        ori=0.0, pos=image_Yloc, draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-5.0)
    partner_image_8 = visual.ImageStim(
        win=win,
        name='partner_image_8', 
        image='cash/d15.png', mask=None, anchor='center',
        ori=0.0, pos=image_Ploc, draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-6.0)
    acc_txt_6 = visual.TextStim(win=win, name='acc_txt_6',
        text='Accept',
        font='Open Sans',
        pos=[-0.11,-0.17], draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    rej_txt_6 = visual.TextStim(win=win, name='rej_txt_6',
        text='Reject',
        font='Open Sans',
        pos=[0.09,-0.17], draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    acc_box_6 = visual.Rect(
        win=win, name='acc_box_6',
        width=(0.17, 0.1)[0], height=(0.17, 0.1)[1],
        ori=0.0, pos=Accbox_loc, draggable=False, anchor='center',
        lineWidth=4.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-9.0, interpolate=True)
    rej_box_6 = visual.Rect(
        win=win, name='rej_box_6',
        width=(0.17, 0.1)[0], height=(0.17, 0.1)[1],
        ori=0.0, pos=Rejbox_loc, draggable=False, anchor='center',
        lineWidth=4.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-10.0, interpolate=True)
    upperRight_12 = visual.TextStim(win=win, name='upperRight_12',
        text='Practice round',
        font='Open Sans',
        pos=(0.4, 0.4), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='gray', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-12.0);
    
    # --- Initialize components for Routine "prc_reveal_rej" ---
    you_txt_9 = visual.TextStim(win=win, name='you_txt_9',
        text='You get:',
        font='Open Sans',
        pos=[-0.13,0.2], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    partner_txt_9 = visual.TextStim(win=win, name='partner_txt_9',
        text='Hannah gets:',
        font='Open Sans',
        pos=[0.13,0.2], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    dollar_Ytxt_9 = visual.TextStim(win=win, name='dollar_Ytxt_9',
        text=dollarYpr,
        font='Open Sans',
        pos=[-0.10,0.15], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    dollar_Ptxt_9 = visual.TextStim(win=win, name='dollar_Ptxt_9',
        text=dollarYpr,
        font='Open Sans',
        pos=[0.10,0.15], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    you_image_9 = visual.ImageStim(
        win=win,
        name='you_image_9', 
        image='cash/d0.png', mask=None, anchor='center',
        ori=0.0, pos=image_Yloc, draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-5.0)
    partner_image_9 = visual.ImageStim(
        win=win,
        name='partner_image_9', 
        image='cash/d0.png', mask=None, anchor='center',
        ori=0.0, pos=image_Ploc, draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-6.0)
    upperRight_13 = visual.TextStim(win=win, name='upperRight_13',
        text='Practice round',
        font='Open Sans',
        pos=(0.4, 0.4), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='gray', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    
    # --- Initialize components for Routine "ins6" ---
    upperRight_14 = visual.TextStim(win=win, name='upperRight_14',
        text='Game Rules',
        font='Open Sans',
        pos=(0.4, 0.4), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='gray', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    main_txt_6 = visual.TextStim(win=win, name='main_txt_6',
        text='Now you’re ready to get started playing the game. You will play with either a team of people or a computer, and you will be prompted to rate your feelings.',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    lowMid_6 = visual.TextStim(win=win, name='lowMid_6',
        text='Press SPACE or UP to BEGIN',
        font='Open Sans',
        pos=(0, -0.3), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='grey', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ins1_key_6 = keyboard.Keyboard(deviceName='ins1_key_6')
    
    # --- Initialize components for Routine "exp_prep" ---
    # Run 'Begin Experiment' code from main_code
    if expInfo.get('condition') == '1':
        conditionfolder = 'experiment/block.xlsx'
    
    if expInfo.get('condition') == '2':
        conditionfolder = 'experiment/block2.xlsx'
    ExpStart_key = keyboard.Keyboard(deviceName='ExpStart_key')
    trigger_txt = visual.TextStim(win=win, name='trigger_txt',
        text='Waiting to start...',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "team" ---
    team_img = visual.ImageStim(
        win=win,
        name='team_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.1), draggable=False, size=(0.75, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=64.0, interpolate=False, depth=0.0)
    team_txt1 = visual.TextStim(win=win, name='team_txt1',
        text='For this set of rounds you will be playing with\n\n',
        font='Open Sans',
        pos=(0, 0.2), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    team_key = keyboard.Keyboard(deviceName='team_key')
    text = visual.TextStim(win=win, name='text',
        text='Press SPACE or UP to continue',
        font='Open Sans',
        pos=(0, -0.35), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    team_txt2 = visual.TextStim(win=win, name='team_txt2',
        text='',
        font='Open Sans',
        pos=(0, 0.15), draggable=False, height=0.07, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_prep" ---
    
    # --- Initialize components for Routine "avatar_present" ---
    avatar = visual.ImageStim(
        win=win,
        name='avatar', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.05), draggable=False, size=(0.25,0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    offer_txt = visual.TextStim(win=win, name='offer_txt',
        text='',
        font='Open Sans',
        pos=[0,-0.17], draggable=False, height=0.06, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "offer_present" ---
    you_txt = visual.TextStim(win=win, name='you_txt',
        text='You',
        font='Open Sans',
        pos=[-0.10,0.2], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    partner_txt = visual.TextStim(win=win, name='partner_txt',
        text='',
        font='Open Sans',
        pos=[0.10,0.2], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    dollar_Ytxt = visual.TextStim(win=win, name='dollar_Ytxt',
        text='',
        font='Open Sans',
        pos=[-0.10,0.15], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    dollar_Ptxt = visual.TextStim(win=win, name='dollar_Ptxt',
        text='',
        font='Open Sans',
        pos=[0.10,0.15], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    you_image = visual.ImageStim(
        win=win,
        name='you_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=image_Yloc, draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-4.0)
    partner_image = visual.ImageStim(
        win=win,
        name='partner_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=image_Ploc, draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-5.0)
    acc_txt = visual.TextStim(win=win, name='acc_txt',
        text='Accept',
        font='Open Sans',
        pos=[-0.11,-0.17], draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    rej_txt = visual.TextStim(win=win, name='rej_txt',
        text='Reject',
        font='Open Sans',
        pos=[0.09,-0.17], draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    acc_box = visual.Rect(
        win=win, name='acc_box',
        width=(0.17, 0.1)[0], height=(0.17, 0.1)[1],
        ori=0.0, pos=Accbox_loc, draggable=False, anchor='center',
        lineWidth=4.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-8.0, interpolate=True)
    rej_box = visual.Rect(
        win=win, name='rej_box',
        width=(0.17, 0.1)[0], height=(0.17, 0.1)[1],
        ori=0.0, pos=Rejbox_loc, draggable=False, anchor='center',
        lineWidth=4.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-9.0, interpolate=True)
    choice_key = keyboard.Keyboard(deviceName='choice_key')
    
    # --- Initialize components for Routine "offer_choice" ---
    you_txt_2 = visual.TextStim(win=win, name='you_txt_2',
        text='You',
        font='Open Sans',
        pos=[-0.10,0.2], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    partner_txt_2 = visual.TextStim(win=win, name='partner_txt_2',
        text='',
        font='Open Sans',
        pos=[0.10,0.2], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    dollar_Ytxt_2 = visual.TextStim(win=win, name='dollar_Ytxt_2',
        text='',
        font='Open Sans',
        pos=[-0.10,0.15], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    dollar_Ptxt_2 = visual.TextStim(win=win, name='dollar_Ptxt_2',
        text='',
        font='Open Sans',
        pos=[0.10,0.15], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    you_image_2 = visual.ImageStim(
        win=win,
        name='you_image_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=image_Yloc, draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-5.0)
    partner_image_2 = visual.ImageStim(
        win=win,
        name='partner_image_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=image_Ploc, draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-6.0)
    acc_txt_2 = visual.TextStim(win=win, name='acc_txt_2',
        text='Accept',
        font='Open Sans',
        pos=[-0.11,-0.17], draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    rej_txt_2 = visual.TextStim(win=win, name='rej_txt_2',
        text='Reject',
        font='Open Sans',
        pos=[0.09,-0.17], draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    acc_box_2 = visual.Rect(
        win=win, name='acc_box_2',
        width=(0.17, 0.1)[0], height=(0.17, 0.1)[1],
        ori=0.0, pos=Accbox_loc, draggable=False, anchor='center',
        lineWidth=4.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-9.0, interpolate=True)
    rej_box_2 = visual.Rect(
        win=win, name='rej_box_2',
        width=(0.17, 0.1)[0], height=(0.17, 0.1)[1],
        ori=0.0, pos=Rejbox_loc, draggable=False, anchor='center',
        lineWidth=4.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-10.0, interpolate=True)
    
    # --- Initialize components for Routine "offer_reveal" ---
    you_txt_3 = visual.TextStim(win=win, name='you_txt_3',
        text='You get:',
        font='Open Sans',
        pos=[-0.13,0.2], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    partner_txt_3 = visual.TextStim(win=win, name='partner_txt_3',
        text='',
        font='Open Sans',
        pos=[0.13,0.2], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    dollar_Ytxt_3 = visual.TextStim(win=win, name='dollar_Ytxt_3',
        text='',
        font='Open Sans',
        pos=[-0.10,0.15], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    dollar_Ptxt_3 = visual.TextStim(win=win, name='dollar_Ptxt_3',
        text='',
        font='Open Sans',
        pos=[0.10,0.15], draggable=False, height=txt_small, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    you_image_3 = visual.ImageStim(
        win=win,
        name='you_image_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=image_Yloc, draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-5.0)
    partner_image_3 = visual.ImageStim(
        win=win,
        name='partner_image_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=image_Ploc, draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-6.0)
    
    # --- Initialize components for Routine "mood" ---
    slider_2 = visual.Slider(win=win, name='slider_2',
        startValue=None, size=(0.8, 0.05), pos=(0, 0), units=win.units,
        labels=['Bad', 'Good'], ticks=(0, 50, 100), granularity=0.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='black', markerColor='deepskyblue', lineColor='black', colorSpace='rgb',
        font='Open Sans', labelHeight=txt_size,
        flip=False, ori=0.0, depth=0, readOnly=False)
    surveyQ1_txt_2 = visual.TextStim(win=win, name='surveyQ1_txt_2',
        text='How do you feel?',
        font='Open Sans',
        pos=(0, 0.3), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ins_txt_2 = visual.TextStim(win=win, name='ins_txt_2',
        text='Use LEFT or RIGHT to move slider\nPress SPACE or UP to confirm\n',
        font='Open Sans',
        pos=(0, -0.2), draggable=False, height=txt_size, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    slider_choose = keyboard.Keyboard(deviceName='slider_choose')
    good_img = visual.ImageStim(
        win=win,
        name='good_img', 
        image='mood image/HappyFace.png', mask=None, anchor='center',
        ori=0.0, pos=(0.4, 0.1), draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    bad_img = visual.ImageStim(
        win=win,
        name='bad_img', 
        image='mood image/SadFace.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.4, 0.1), draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    ok_img = visual.ImageStim(
        win=win,
        name='ok_img', 
        image='mood image/JustFace.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.1), draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    slider_move = keyboard.Keyboard(deviceName='slider_move')
    
    # --- Initialize components for Routine "fixation" ---
    fix_txt = visual.TextStim(win=win, name='fix_txt',
        text='',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.2, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "end" ---
    text_9 = visual.TextStim(win=win, name='text_9',
        text='Game end\n\nThank you for your time',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    expEnd_key = keyboard.Keyboard(deviceName='expEnd_key')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "ins_open" ---
    # create an object to store info about Routine ins_open
    ins_open = data.Routine(
        name='ins_open',
        components=[title, lowMid_open, ins_key],
    )
    ins_open.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for ins_key
    ins_key.keys = []
    ins_key.rt = []
    _ins_key_allKeys = []
    # store start times for ins_open
    ins_open.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ins_open.tStart = globalClock.getTime(format='float')
    ins_open.status = STARTED
    thisExp.addData('ins_open.started', ins_open.tStart)
    ins_open.maxDuration = None
    # keep track of which components have finished
    ins_openComponents = ins_open.components
    for thisComponent in ins_open.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ins_open" ---
    ins_open.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *title* updates
        
        # if title is starting this frame...
        if title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            title.frameNStart = frameN  # exact frame index
            title.tStart = t  # local t and not account for scr refresh
            title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(title, 'tStartRefresh')  # time at next scr refresh
            # update status
            title.status = STARTED
            title.setAutoDraw(True)
        
        # if title is active this frame...
        if title.status == STARTED:
            # update params
            pass
        
        # *lowMid_open* updates
        
        # if lowMid_open is starting this frame...
        if lowMid_open.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lowMid_open.frameNStart = frameN  # exact frame index
            lowMid_open.tStart = t  # local t and not account for scr refresh
            lowMid_open.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lowMid_open, 'tStartRefresh')  # time at next scr refresh
            # update status
            lowMid_open.status = STARTED
            lowMid_open.setAutoDraw(True)
        
        # if lowMid_open is active this frame...
        if lowMid_open.status == STARTED:
            # update params
            pass
        
        # *ins_key* updates
        waitOnFlip = False
        
        # if ins_key is starting this frame...
        if ins_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ins_key.frameNStart = frameN  # exact frame index
            ins_key.tStart = t  # local t and not account for scr refresh
            ins_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins_key.started')
            # update status
            ins_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ins_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ins_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ins_key.status == STARTED and not waitOnFlip:
            theseKeys = ins_key.getKeys(keyList=['space','4'], ignoreKeys=["escape"], waitRelease=False)
            _ins_key_allKeys.extend(theseKeys)
            if len(_ins_key_allKeys):
                ins_key.keys = _ins_key_allKeys[-1].name  # just the last key pressed
                ins_key.rt = _ins_key_allKeys[-1].rt
                ins_key.duration = _ins_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ins_open.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ins_open.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ins_open" ---
    for thisComponent in ins_open.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ins_open
    ins_open.tStop = globalClock.getTime(format='float')
    ins_open.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ins_open.stopped', ins_open.tStop)
    # check responses
    if ins_key.keys in ['', [], None]:  # No response was made
        ins_key.keys = None
    thisExp.addData('ins_key.keys',ins_key.keys)
    if ins_key.keys != None:  # we had a response
        thisExp.addData('ins_key.rt', ins_key.rt)
        thisExp.addData('ins_key.duration', ins_key.duration)
    thisExp.nextEntry()
    # the Routine "ins_open" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ins1" ---
    # create an object to store info about Routine ins1
    ins1 = data.Routine(
        name='ins1',
        components=[upperRight, main_txt, lowMid, ins1_key],
    )
    ins1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for ins1_key
    ins1_key.keys = []
    ins1_key.rt = []
    _ins1_key_allKeys = []
    # store start times for ins1
    ins1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ins1.tStart = globalClock.getTime(format='float')
    ins1.status = STARTED
    thisExp.addData('ins1.started', ins1.tStart)
    ins1.maxDuration = None
    # keep track of which components have finished
    ins1Components = ins1.components
    for thisComponent in ins1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ins1" ---
    ins1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *upperRight* updates
        
        # if upperRight is starting this frame...
        if upperRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            upperRight.frameNStart = frameN  # exact frame index
            upperRight.tStart = t  # local t and not account for scr refresh
            upperRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upperRight, 'tStartRefresh')  # time at next scr refresh
            # update status
            upperRight.status = STARTED
            upperRight.setAutoDraw(True)
        
        # if upperRight is active this frame...
        if upperRight.status == STARTED:
            # update params
            pass
        
        # *main_txt* updates
        
        # if main_txt is starting this frame...
        if main_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            main_txt.frameNStart = frameN  # exact frame index
            main_txt.tStart = t  # local t and not account for scr refresh
            main_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            main_txt.status = STARTED
            main_txt.setAutoDraw(True)
        
        # if main_txt is active this frame...
        if main_txt.status == STARTED:
            # update params
            pass
        
        # *lowMid* updates
        
        # if lowMid is starting this frame...
        if lowMid.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lowMid.frameNStart = frameN  # exact frame index
            lowMid.tStart = t  # local t and not account for scr refresh
            lowMid.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lowMid, 'tStartRefresh')  # time at next scr refresh
            # update status
            lowMid.status = STARTED
            lowMid.setAutoDraw(True)
        
        # if lowMid is active this frame...
        if lowMid.status == STARTED:
            # update params
            pass
        
        # *ins1_key* updates
        waitOnFlip = False
        
        # if ins1_key is starting this frame...
        if ins1_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ins1_key.frameNStart = frameN  # exact frame index
            ins1_key.tStart = t  # local t and not account for scr refresh
            ins1_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins1_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins1_key.started')
            # update status
            ins1_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ins1_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ins1_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ins1_key.status == STARTED and not waitOnFlip:
            theseKeys = ins1_key.getKeys(keyList=['space','4'], ignoreKeys=["escape"], waitRelease=False)
            _ins1_key_allKeys.extend(theseKeys)
            if len(_ins1_key_allKeys):
                ins1_key.keys = _ins1_key_allKeys[-1].name  # just the last key pressed
                ins1_key.rt = _ins1_key_allKeys[-1].rt
                ins1_key.duration = _ins1_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ins1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ins1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ins1" ---
    for thisComponent in ins1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ins1
    ins1.tStop = globalClock.getTime(format='float')
    ins1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ins1.stopped', ins1.tStop)
    thisExp.nextEntry()
    # the Routine "ins1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ins2" ---
    # create an object to store info about Routine ins2
    ins2 = data.Routine(
        name='ins2',
        components=[upperRight_2, main_txt_2, lowMid_2, ins1_key_2],
    )
    ins2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for ins1_key_2
    ins1_key_2.keys = []
    ins1_key_2.rt = []
    _ins1_key_2_allKeys = []
    # store start times for ins2
    ins2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ins2.tStart = globalClock.getTime(format='float')
    ins2.status = STARTED
    thisExp.addData('ins2.started', ins2.tStart)
    ins2.maxDuration = None
    # keep track of which components have finished
    ins2Components = ins2.components
    for thisComponent in ins2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ins2" ---
    ins2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *upperRight_2* updates
        
        # if upperRight_2 is starting this frame...
        if upperRight_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            upperRight_2.frameNStart = frameN  # exact frame index
            upperRight_2.tStart = t  # local t and not account for scr refresh
            upperRight_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upperRight_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            upperRight_2.status = STARTED
            upperRight_2.setAutoDraw(True)
        
        # if upperRight_2 is active this frame...
        if upperRight_2.status == STARTED:
            # update params
            pass
        
        # *main_txt_2* updates
        
        # if main_txt_2 is starting this frame...
        if main_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            main_txt_2.frameNStart = frameN  # exact frame index
            main_txt_2.tStart = t  # local t and not account for scr refresh
            main_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_txt_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            main_txt_2.status = STARTED
            main_txt_2.setAutoDraw(True)
        
        # if main_txt_2 is active this frame...
        if main_txt_2.status == STARTED:
            # update params
            pass
        
        # *lowMid_2* updates
        
        # if lowMid_2 is starting this frame...
        if lowMid_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lowMid_2.frameNStart = frameN  # exact frame index
            lowMid_2.tStart = t  # local t and not account for scr refresh
            lowMid_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lowMid_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            lowMid_2.status = STARTED
            lowMid_2.setAutoDraw(True)
        
        # if lowMid_2 is active this frame...
        if lowMid_2.status == STARTED:
            # update params
            pass
        
        # *ins1_key_2* updates
        waitOnFlip = False
        
        # if ins1_key_2 is starting this frame...
        if ins1_key_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ins1_key_2.frameNStart = frameN  # exact frame index
            ins1_key_2.tStart = t  # local t and not account for scr refresh
            ins1_key_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins1_key_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins1_key_2.started')
            # update status
            ins1_key_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ins1_key_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ins1_key_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ins1_key_2.status == STARTED and not waitOnFlip:
            theseKeys = ins1_key_2.getKeys(keyList=['space','4'], ignoreKeys=["escape"], waitRelease=False)
            _ins1_key_2_allKeys.extend(theseKeys)
            if len(_ins1_key_2_allKeys):
                ins1_key_2.keys = _ins1_key_2_allKeys[-1].name  # just the last key pressed
                ins1_key_2.rt = _ins1_key_2_allKeys[-1].rt
                ins1_key_2.duration = _ins1_key_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ins2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ins2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ins2" ---
    for thisComponent in ins2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ins2
    ins2.tStop = globalClock.getTime(format='float')
    ins2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ins2.stopped', ins2.tStop)
    thisExp.nextEntry()
    # the Routine "ins2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ins3" ---
    # create an object to store info about Routine ins3
    ins3 = data.Routine(
        name='ins3',
        components=[upperRight_3, main_txt_3, lowMid_3, ins1_key_3],
    )
    ins3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for ins1_key_3
    ins1_key_3.keys = []
    ins1_key_3.rt = []
    _ins1_key_3_allKeys = []
    # store start times for ins3
    ins3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ins3.tStart = globalClock.getTime(format='float')
    ins3.status = STARTED
    thisExp.addData('ins3.started', ins3.tStart)
    ins3.maxDuration = None
    # keep track of which components have finished
    ins3Components = ins3.components
    for thisComponent in ins3.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ins3" ---
    ins3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *upperRight_3* updates
        
        # if upperRight_3 is starting this frame...
        if upperRight_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            upperRight_3.frameNStart = frameN  # exact frame index
            upperRight_3.tStart = t  # local t and not account for scr refresh
            upperRight_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upperRight_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            upperRight_3.status = STARTED
            upperRight_3.setAutoDraw(True)
        
        # if upperRight_3 is active this frame...
        if upperRight_3.status == STARTED:
            # update params
            pass
        
        # *main_txt_3* updates
        
        # if main_txt_3 is starting this frame...
        if main_txt_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            main_txt_3.frameNStart = frameN  # exact frame index
            main_txt_3.tStart = t  # local t and not account for scr refresh
            main_txt_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_txt_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            main_txt_3.status = STARTED
            main_txt_3.setAutoDraw(True)
        
        # if main_txt_3 is active this frame...
        if main_txt_3.status == STARTED:
            # update params
            pass
        
        # *lowMid_3* updates
        
        # if lowMid_3 is starting this frame...
        if lowMid_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lowMid_3.frameNStart = frameN  # exact frame index
            lowMid_3.tStart = t  # local t and not account for scr refresh
            lowMid_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lowMid_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            lowMid_3.status = STARTED
            lowMid_3.setAutoDraw(True)
        
        # if lowMid_3 is active this frame...
        if lowMid_3.status == STARTED:
            # update params
            pass
        
        # *ins1_key_3* updates
        waitOnFlip = False
        
        # if ins1_key_3 is starting this frame...
        if ins1_key_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ins1_key_3.frameNStart = frameN  # exact frame index
            ins1_key_3.tStart = t  # local t and not account for scr refresh
            ins1_key_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins1_key_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins1_key_3.started')
            # update status
            ins1_key_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ins1_key_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ins1_key_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ins1_key_3.status == STARTED and not waitOnFlip:
            theseKeys = ins1_key_3.getKeys(keyList=['space','4'], ignoreKeys=["escape"], waitRelease=False)
            _ins1_key_3_allKeys.extend(theseKeys)
            if len(_ins1_key_3_allKeys):
                ins1_key_3.keys = _ins1_key_3_allKeys[-1].name  # just the last key pressed
                ins1_key_3.rt = _ins1_key_3_allKeys[-1].rt
                ins1_key_3.duration = _ins1_key_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ins3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ins3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ins3" ---
    for thisComponent in ins3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ins3
    ins3.tStop = globalClock.getTime(format='float')
    ins3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ins3.stopped', ins3.tStop)
    thisExp.nextEntry()
    # the Routine "ins3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "prc_prep" ---
    # create an object to store info about Routine prc_prep
    prc_prep = data.Routine(
        name='prc_prep',
        components=[],
    )
    prc_prep.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for prc_prep
    prc_prep.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    prc_prep.tStart = globalClock.getTime(format='float')
    prc_prep.status = STARTED
    thisExp.addData('prc_prep.started', prc_prep.tStart)
    prc_prep.maxDuration = None
    # keep track of which components have finished
    prc_prepComponents = prc_prep.components
    for thisComponent in prc_prep.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prc_prep" ---
    prc_prep.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from prc_code
        keys = kb.getKeys(['t'])
        if 't' in keys:
            time = core.getTime()
            trigger_list.append(time)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            prc_prep.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prc_prep.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prc_prep" ---
    for thisComponent in prc_prep.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for prc_prep
    prc_prep.tStop = globalClock.getTime(format='float')
    prc_prep.tStopRefresh = tThisFlipGlobal
    thisExp.addData('prc_prep.stopped', prc_prep.tStop)
    # Run 'End Routine' code from prc_code
    thisExp.addData('trigger down', trigger_list)
    thisExp.nextEntry()
    # the Routine "prc_prep" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "prc_ins1" ---
    # create an object to store info about Routine prc_ins1
    prc_ins1 = data.Routine(
        name='prc_ins1',
        components=[upperRight_4, main_txt_4, lowMid_4, ins1_key_4],
    )
    prc_ins1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    main_txt_4.setText('Let’s see what happens when you accept.\n')
    # create starting attributes for ins1_key_4
    ins1_key_4.keys = []
    ins1_key_4.rt = []
    _ins1_key_4_allKeys = []
    # store start times for prc_ins1
    prc_ins1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    prc_ins1.tStart = globalClock.getTime(format='float')
    prc_ins1.status = STARTED
    thisExp.addData('prc_ins1.started', prc_ins1.tStart)
    prc_ins1.maxDuration = None
    # keep track of which components have finished
    prc_ins1Components = prc_ins1.components
    for thisComponent in prc_ins1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prc_ins1" ---
    prc_ins1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *upperRight_4* updates
        
        # if upperRight_4 is starting this frame...
        if upperRight_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            upperRight_4.frameNStart = frameN  # exact frame index
            upperRight_4.tStart = t  # local t and not account for scr refresh
            upperRight_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upperRight_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            upperRight_4.status = STARTED
            upperRight_4.setAutoDraw(True)
        
        # if upperRight_4 is active this frame...
        if upperRight_4.status == STARTED:
            # update params
            pass
        
        # *main_txt_4* updates
        
        # if main_txt_4 is starting this frame...
        if main_txt_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            main_txt_4.frameNStart = frameN  # exact frame index
            main_txt_4.tStart = t  # local t and not account for scr refresh
            main_txt_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_txt_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            main_txt_4.status = STARTED
            main_txt_4.setAutoDraw(True)
        
        # if main_txt_4 is active this frame...
        if main_txt_4.status == STARTED:
            # update params
            pass
        
        # *lowMid_4* updates
        
        # if lowMid_4 is starting this frame...
        if lowMid_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lowMid_4.frameNStart = frameN  # exact frame index
            lowMid_4.tStart = t  # local t and not account for scr refresh
            lowMid_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lowMid_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            lowMid_4.status = STARTED
            lowMid_4.setAutoDraw(True)
        
        # if lowMid_4 is active this frame...
        if lowMid_4.status == STARTED:
            # update params
            pass
        
        # *ins1_key_4* updates
        waitOnFlip = False
        
        # if ins1_key_4 is starting this frame...
        if ins1_key_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ins1_key_4.frameNStart = frameN  # exact frame index
            ins1_key_4.tStart = t  # local t and not account for scr refresh
            ins1_key_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins1_key_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins1_key_4.started')
            # update status
            ins1_key_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ins1_key_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ins1_key_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ins1_key_4.status == STARTED and not waitOnFlip:
            theseKeys = ins1_key_4.getKeys(keyList=['space','4'], ignoreKeys=["escape"], waitRelease=False)
            _ins1_key_4_allKeys.extend(theseKeys)
            if len(_ins1_key_4_allKeys):
                ins1_key_4.keys = _ins1_key_4_allKeys[-1].name  # just the last key pressed
                ins1_key_4.rt = _ins1_key_4_allKeys[-1].rt
                ins1_key_4.duration = _ins1_key_4_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            prc_ins1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prc_ins1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prc_ins1" ---
    for thisComponent in prc_ins1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for prc_ins1
    prc_ins1.tStop = globalClock.getTime(format='float')
    prc_ins1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('prc_ins1.stopped', prc_ins1.tStop)
    thisExp.nextEntry()
    # the Routine "prc_ins1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "prc_present_acc" ---
    # create an object to store info about Routine prc_present_acc
    prc_present_acc = data.Routine(
        name='prc_present_acc',
        components=[avatar_2, offer_txt_2, upperRight_5],
    )
    prc_present_acc.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    avatar_2.setImage('practice/Hannah.png')
    # store start times for prc_present_acc
    prc_present_acc.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    prc_present_acc.tStart = globalClock.getTime(format='float')
    prc_present_acc.status = STARTED
    thisExp.addData('prc_present_acc.started', prc_present_acc.tStart)
    prc_present_acc.maxDuration = None
    # keep track of which components have finished
    prc_present_accComponents = prc_present_acc.components
    for thisComponent in prc_present_acc.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prc_present_acc" ---
    prc_present_acc.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *avatar_2* updates
        
        # if avatar_2 is starting this frame...
        if avatar_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            avatar_2.frameNStart = frameN  # exact frame index
            avatar_2.tStart = t  # local t and not account for scr refresh
            avatar_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(avatar_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            avatar_2.status = STARTED
            avatar_2.setAutoDraw(True)
        
        # if avatar_2 is active this frame...
        if avatar_2.status == STARTED:
            # update params
            pass
        
        # if avatar_2 is stopping this frame...
        if avatar_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > avatar_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                avatar_2.tStop = t  # not accounting for scr refresh
                avatar_2.tStopRefresh = tThisFlipGlobal  # on global time
                avatar_2.frameNStop = frameN  # exact frame index
                # update status
                avatar_2.status = FINISHED
                avatar_2.setAutoDraw(False)
        
        # *offer_txt_2* updates
        
        # if offer_txt_2 is starting this frame...
        if offer_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            offer_txt_2.frameNStart = frameN  # exact frame index
            offer_txt_2.tStart = t  # local t and not account for scr refresh
            offer_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(offer_txt_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            offer_txt_2.status = STARTED
            offer_txt_2.setAutoDraw(True)
        
        # if offer_txt_2 is active this frame...
        if offer_txt_2.status == STARTED:
            # update params
            pass
        
        # if offer_txt_2 is stopping this frame...
        if offer_txt_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > offer_txt_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                offer_txt_2.tStop = t  # not accounting for scr refresh
                offer_txt_2.tStopRefresh = tThisFlipGlobal  # on global time
                offer_txt_2.frameNStop = frameN  # exact frame index
                # update status
                offer_txt_2.status = FINISHED
                offer_txt_2.setAutoDraw(False)
        # Run 'Each Frame' code from code_7
        keys = kb.getKeys(['t'])
        if 't' in keys:
            time = core.getTime()
            trigger_list.append(time)
        
        # *upperRight_5* updates
        
        # if upperRight_5 is starting this frame...
        if upperRight_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            upperRight_5.frameNStart = frameN  # exact frame index
            upperRight_5.tStart = t  # local t and not account for scr refresh
            upperRight_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upperRight_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            upperRight_5.status = STARTED
            upperRight_5.setAutoDraw(True)
        
        # if upperRight_5 is active this frame...
        if upperRight_5.status == STARTED:
            # update params
            pass
        
        # if upperRight_5 is stopping this frame...
        if upperRight_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > upperRight_5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                upperRight_5.tStop = t  # not accounting for scr refresh
                upperRight_5.tStopRefresh = tThisFlipGlobal  # on global time
                upperRight_5.frameNStop = frameN  # exact frame index
                # update status
                upperRight_5.status = FINISHED
                upperRight_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            prc_present_acc.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prc_present_acc.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prc_present_acc" ---
    for thisComponent in prc_present_acc.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for prc_present_acc
    prc_present_acc.tStop = globalClock.getTime(format='float')
    prc_present_acc.tStopRefresh = tThisFlipGlobal
    thisExp.addData('prc_present_acc.stopped', prc_present_acc.tStop)
    # Run 'End Routine' code from code_7
    thisExp.addData('trigger down', trigger_list)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if prc_present_acc.maxDurationReached:
        routineTimer.addTime(-prc_present_acc.maxDuration)
    elif prc_present_acc.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "prc_offer_acc" ---
    # create an object to store info about Routine prc_offer_acc
    prc_offer_acc = data.Routine(
        name='prc_offer_acc',
        components=[you_txt_4, partner_txt_4, dollar_Ytxt_4, dollar_Ptxt_4, you_image_4, partner_image_4, acc_txt_3, rej_txt_3, acc_box_3, rej_box_3, choice_key_2, acc_img, upperRight_6],
    )
    prc_offer_acc.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for choice_key_2
    choice_key_2.keys = []
    choice_key_2.rt = []
    _choice_key_2_allKeys = []
    # Run 'Begin Routine' code from code_8
    keys = kb.getKeys(['t'])
    if 't' in keys:
        time = core.getTime()
        trigger_list.append(time)
    acc_img.setPos([-0.4, -0.15])
    acc_img.setImage('development/UG-Mood_Instruction/Slide8.jpg')
    # store start times for prc_offer_acc
    prc_offer_acc.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    prc_offer_acc.tStart = globalClock.getTime(format='float')
    prc_offer_acc.status = STARTED
    thisExp.addData('prc_offer_acc.started', prc_offer_acc.tStart)
    prc_offer_acc.maxDuration = None
    # keep track of which components have finished
    prc_offer_accComponents = prc_offer_acc.components
    for thisComponent in prc_offer_acc.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prc_offer_acc" ---
    prc_offer_acc.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *you_txt_4* updates
        
        # if you_txt_4 is starting this frame...
        if you_txt_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            you_txt_4.frameNStart = frameN  # exact frame index
            you_txt_4.tStart = t  # local t and not account for scr refresh
            you_txt_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(you_txt_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            you_txt_4.status = STARTED
            you_txt_4.setAutoDraw(True)
        
        # if you_txt_4 is active this frame...
        if you_txt_4.status == STARTED:
            # update params
            pass
        
        # *partner_txt_4* updates
        
        # if partner_txt_4 is starting this frame...
        if partner_txt_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            partner_txt_4.frameNStart = frameN  # exact frame index
            partner_txt_4.tStart = t  # local t and not account for scr refresh
            partner_txt_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(partner_txt_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            partner_txt_4.status = STARTED
            partner_txt_4.setAutoDraw(True)
        
        # if partner_txt_4 is active this frame...
        if partner_txt_4.status == STARTED:
            # update params
            pass
        
        # *dollar_Ytxt_4* updates
        
        # if dollar_Ytxt_4 is starting this frame...
        if dollar_Ytxt_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dollar_Ytxt_4.frameNStart = frameN  # exact frame index
            dollar_Ytxt_4.tStart = t  # local t and not account for scr refresh
            dollar_Ytxt_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dollar_Ytxt_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            dollar_Ytxt_4.status = STARTED
            dollar_Ytxt_4.setAutoDraw(True)
        
        # if dollar_Ytxt_4 is active this frame...
        if dollar_Ytxt_4.status == STARTED:
            # update params
            pass
        
        # *dollar_Ptxt_4* updates
        
        # if dollar_Ptxt_4 is starting this frame...
        if dollar_Ptxt_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dollar_Ptxt_4.frameNStart = frameN  # exact frame index
            dollar_Ptxt_4.tStart = t  # local t and not account for scr refresh
            dollar_Ptxt_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dollar_Ptxt_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            dollar_Ptxt_4.status = STARTED
            dollar_Ptxt_4.setAutoDraw(True)
        
        # if dollar_Ptxt_4 is active this frame...
        if dollar_Ptxt_4.status == STARTED:
            # update params
            pass
        
        # *you_image_4* updates
        
        # if you_image_4 is starting this frame...
        if you_image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            you_image_4.frameNStart = frameN  # exact frame index
            you_image_4.tStart = t  # local t and not account for scr refresh
            you_image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(you_image_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            you_image_4.status = STARTED
            you_image_4.setAutoDraw(True)
        
        # if you_image_4 is active this frame...
        if you_image_4.status == STARTED:
            # update params
            pass
        
        # *partner_image_4* updates
        
        # if partner_image_4 is starting this frame...
        if partner_image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            partner_image_4.frameNStart = frameN  # exact frame index
            partner_image_4.tStart = t  # local t and not account for scr refresh
            partner_image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(partner_image_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            partner_image_4.status = STARTED
            partner_image_4.setAutoDraw(True)
        
        # if partner_image_4 is active this frame...
        if partner_image_4.status == STARTED:
            # update params
            pass
        
        # *acc_txt_3* updates
        
        # if acc_txt_3 is starting this frame...
        if acc_txt_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            acc_txt_3.frameNStart = frameN  # exact frame index
            acc_txt_3.tStart = t  # local t and not account for scr refresh
            acc_txt_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(acc_txt_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            acc_txt_3.status = STARTED
            acc_txt_3.setAutoDraw(True)
        
        # if acc_txt_3 is active this frame...
        if acc_txt_3.status == STARTED:
            # update params
            pass
        
        # *rej_txt_3* updates
        
        # if rej_txt_3 is starting this frame...
        if rej_txt_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rej_txt_3.frameNStart = frameN  # exact frame index
            rej_txt_3.tStart = t  # local t and not account for scr refresh
            rej_txt_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rej_txt_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            rej_txt_3.status = STARTED
            rej_txt_3.setAutoDraw(True)
        
        # if rej_txt_3 is active this frame...
        if rej_txt_3.status == STARTED:
            # update params
            pass
        
        # *acc_box_3* updates
        
        # if acc_box_3 is starting this frame...
        if acc_box_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            acc_box_3.frameNStart = frameN  # exact frame index
            acc_box_3.tStart = t  # local t and not account for scr refresh
            acc_box_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(acc_box_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            acc_box_3.status = STARTED
            acc_box_3.setAutoDraw(True)
        
        # if acc_box_3 is active this frame...
        if acc_box_3.status == STARTED:
            # update params
            pass
        
        # *rej_box_3* updates
        
        # if rej_box_3 is starting this frame...
        if rej_box_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rej_box_3.frameNStart = frameN  # exact frame index
            rej_box_3.tStart = t  # local t and not account for scr refresh
            rej_box_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rej_box_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            rej_box_3.status = STARTED
            rej_box_3.setAutoDraw(True)
        
        # if rej_box_3 is active this frame...
        if rej_box_3.status == STARTED:
            # update params
            pass
        
        # *choice_key_2* updates
        waitOnFlip = False
        
        # if choice_key_2 is starting this frame...
        if choice_key_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_key_2.frameNStart = frameN  # exact frame index
            choice_key_2.tStart = t  # local t and not account for scr refresh
            choice_key_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_key_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            choice_key_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(choice_key_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(choice_key_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if choice_key_2.status == STARTED and not waitOnFlip:
            theseKeys = choice_key_2.getKeys(keyList=['left','3'], ignoreKeys=["escape"], waitRelease=False)
            _choice_key_2_allKeys.extend(theseKeys)
            if len(_choice_key_2_allKeys):
                choice_key_2.keys = _choice_key_2_allKeys[-1].name  # just the last key pressed
                choice_key_2.rt = _choice_key_2_allKeys[-1].rt
                choice_key_2.duration = _choice_key_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *acc_img* updates
        
        # if acc_img is starting this frame...
        if acc_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            acc_img.frameNStart = frameN  # exact frame index
            acc_img.tStart = t  # local t and not account for scr refresh
            acc_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(acc_img, 'tStartRefresh')  # time at next scr refresh
            # update status
            acc_img.status = STARTED
            acc_img.setAutoDraw(True)
        
        # if acc_img is active this frame...
        if acc_img.status == STARTED:
            # update params
            pass
        
        # *upperRight_6* updates
        
        # if upperRight_6 is starting this frame...
        if upperRight_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            upperRight_6.frameNStart = frameN  # exact frame index
            upperRight_6.tStart = t  # local t and not account for scr refresh
            upperRight_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upperRight_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            upperRight_6.status = STARTED
            upperRight_6.setAutoDraw(True)
        
        # if upperRight_6 is active this frame...
        if upperRight_6.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            prc_offer_acc.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prc_offer_acc.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prc_offer_acc" ---
    for thisComponent in prc_offer_acc.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for prc_offer_acc
    prc_offer_acc.tStop = globalClock.getTime(format='float')
    prc_offer_acc.tStopRefresh = tThisFlipGlobal
    thisExp.addData('prc_offer_acc.stopped', prc_offer_acc.tStop)
    # Run 'End Routine' code from code_8
    keys = kb.getKeys(['t'])
    if 't' in keys:
        time = core.getTime()
        trigger_list.append(time)
    thisExp.nextEntry()
    # the Routine "prc_offer_acc" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "prc_choice_acc" ---
    # create an object to store info about Routine prc_choice_acc
    prc_choice_acc = data.Routine(
        name='prc_choice_acc',
        components=[you_txt_5, partner_txt_5, dollar_Ytxt_5, dollar_Ptxt_5, you_image_5, partner_image_5, acc_txt_4, rej_txt_4, acc_box_4, rej_box_4, upperRight_7],
    )
    prc_choice_acc.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from box_change_2
    if choice_key_2.keys == 'left' or choice_key_2.keys == '3': #accept
        #time = core.getTime()
        acc_box_4.lineColor = 'black'
        resp = 1
    elif choice_key_2.keys == 'right' or choice_key_2.keys == '1': #reject
        #time = core.getTime()
        rej_box_4.lineColor = 'black'
        resp = 0
    # store start times for prc_choice_acc
    prc_choice_acc.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    prc_choice_acc.tStart = globalClock.getTime(format='float')
    prc_choice_acc.status = STARTED
    thisExp.addData('prc_choice_acc.started', prc_choice_acc.tStart)
    prc_choice_acc.maxDuration = None
    # keep track of which components have finished
    prc_choice_accComponents = prc_choice_acc.components
    for thisComponent in prc_choice_acc.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prc_choice_acc" ---
    prc_choice_acc.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from box_change_2
        keys = kb.getKeys(['t'])
        if 't' in keys:
            time = core.getTime()
            trigger_list.append(time)
        # wait for keypresses here
        #keys = kb.getKeys()
        #for thisKey in keys:
        #    if thisKey == 't':  # it is equivalent to the string 'q'
        #        time = core.getTime()
        #        print(time)
        #    else:
        #        print(thisKey.name, thisKey.tDown, thisKey.rt)
        
        #keys = kb.getKeys(['t'])
        #if 't' in keys:
        #    time = core.getTime()
        #    print(time)
        
        # *you_txt_5* updates
        
        # if you_txt_5 is starting this frame...
        if you_txt_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            you_txt_5.frameNStart = frameN  # exact frame index
            you_txt_5.tStart = t  # local t and not account for scr refresh
            you_txt_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(you_txt_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            you_txt_5.status = STARTED
            you_txt_5.setAutoDraw(True)
        
        # if you_txt_5 is active this frame...
        if you_txt_5.status == STARTED:
            # update params
            pass
        
        # if you_txt_5 is stopping this frame...
        if you_txt_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > you_txt_5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                you_txt_5.tStop = t  # not accounting for scr refresh
                you_txt_5.tStopRefresh = tThisFlipGlobal  # on global time
                you_txt_5.frameNStop = frameN  # exact frame index
                # update status
                you_txt_5.status = FINISHED
                you_txt_5.setAutoDraw(False)
        
        # *partner_txt_5* updates
        
        # if partner_txt_5 is starting this frame...
        if partner_txt_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            partner_txt_5.frameNStart = frameN  # exact frame index
            partner_txt_5.tStart = t  # local t and not account for scr refresh
            partner_txt_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(partner_txt_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            partner_txt_5.status = STARTED
            partner_txt_5.setAutoDraw(True)
        
        # if partner_txt_5 is active this frame...
        if partner_txt_5.status == STARTED:
            # update params
            pass
        
        # if partner_txt_5 is stopping this frame...
        if partner_txt_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > partner_txt_5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                partner_txt_5.tStop = t  # not accounting for scr refresh
                partner_txt_5.tStopRefresh = tThisFlipGlobal  # on global time
                partner_txt_5.frameNStop = frameN  # exact frame index
                # update status
                partner_txt_5.status = FINISHED
                partner_txt_5.setAutoDraw(False)
        
        # *dollar_Ytxt_5* updates
        
        # if dollar_Ytxt_5 is starting this frame...
        if dollar_Ytxt_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dollar_Ytxt_5.frameNStart = frameN  # exact frame index
            dollar_Ytxt_5.tStart = t  # local t and not account for scr refresh
            dollar_Ytxt_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dollar_Ytxt_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            dollar_Ytxt_5.status = STARTED
            dollar_Ytxt_5.setAutoDraw(True)
        
        # if dollar_Ytxt_5 is active this frame...
        if dollar_Ytxt_5.status == STARTED:
            # update params
            pass
        
        # if dollar_Ytxt_5 is stopping this frame...
        if dollar_Ytxt_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dollar_Ytxt_5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                dollar_Ytxt_5.tStop = t  # not accounting for scr refresh
                dollar_Ytxt_5.tStopRefresh = tThisFlipGlobal  # on global time
                dollar_Ytxt_5.frameNStop = frameN  # exact frame index
                # update status
                dollar_Ytxt_5.status = FINISHED
                dollar_Ytxt_5.setAutoDraw(False)
        
        # *dollar_Ptxt_5* updates
        
        # if dollar_Ptxt_5 is starting this frame...
        if dollar_Ptxt_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dollar_Ptxt_5.frameNStart = frameN  # exact frame index
            dollar_Ptxt_5.tStart = t  # local t and not account for scr refresh
            dollar_Ptxt_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dollar_Ptxt_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            dollar_Ptxt_5.status = STARTED
            dollar_Ptxt_5.setAutoDraw(True)
        
        # if dollar_Ptxt_5 is active this frame...
        if dollar_Ptxt_5.status == STARTED:
            # update params
            pass
        
        # if dollar_Ptxt_5 is stopping this frame...
        if dollar_Ptxt_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dollar_Ptxt_5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                dollar_Ptxt_5.tStop = t  # not accounting for scr refresh
                dollar_Ptxt_5.tStopRefresh = tThisFlipGlobal  # on global time
                dollar_Ptxt_5.frameNStop = frameN  # exact frame index
                # update status
                dollar_Ptxt_5.status = FINISHED
                dollar_Ptxt_5.setAutoDraw(False)
        
        # *you_image_5* updates
        
        # if you_image_5 is starting this frame...
        if you_image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            you_image_5.frameNStart = frameN  # exact frame index
            you_image_5.tStart = t  # local t and not account for scr refresh
            you_image_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(you_image_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            you_image_5.status = STARTED
            you_image_5.setAutoDraw(True)
        
        # if you_image_5 is active this frame...
        if you_image_5.status == STARTED:
            # update params
            pass
        
        # if you_image_5 is stopping this frame...
        if you_image_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > you_image_5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                you_image_5.tStop = t  # not accounting for scr refresh
                you_image_5.tStopRefresh = tThisFlipGlobal  # on global time
                you_image_5.frameNStop = frameN  # exact frame index
                # update status
                you_image_5.status = FINISHED
                you_image_5.setAutoDraw(False)
        
        # *partner_image_5* updates
        
        # if partner_image_5 is starting this frame...
        if partner_image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            partner_image_5.frameNStart = frameN  # exact frame index
            partner_image_5.tStart = t  # local t and not account for scr refresh
            partner_image_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(partner_image_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            partner_image_5.status = STARTED
            partner_image_5.setAutoDraw(True)
        
        # if partner_image_5 is active this frame...
        if partner_image_5.status == STARTED:
            # update params
            pass
        
        # if partner_image_5 is stopping this frame...
        if partner_image_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > partner_image_5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                partner_image_5.tStop = t  # not accounting for scr refresh
                partner_image_5.tStopRefresh = tThisFlipGlobal  # on global time
                partner_image_5.frameNStop = frameN  # exact frame index
                # update status
                partner_image_5.status = FINISHED
                partner_image_5.setAutoDraw(False)
        
        # *acc_txt_4* updates
        
        # if acc_txt_4 is starting this frame...
        if acc_txt_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            acc_txt_4.frameNStart = frameN  # exact frame index
            acc_txt_4.tStart = t  # local t and not account for scr refresh
            acc_txt_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(acc_txt_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            acc_txt_4.status = STARTED
            acc_txt_4.setAutoDraw(True)
        
        # if acc_txt_4 is active this frame...
        if acc_txt_4.status == STARTED:
            # update params
            pass
        
        # if acc_txt_4 is stopping this frame...
        if acc_txt_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > acc_txt_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                acc_txt_4.tStop = t  # not accounting for scr refresh
                acc_txt_4.tStopRefresh = tThisFlipGlobal  # on global time
                acc_txt_4.frameNStop = frameN  # exact frame index
                # update status
                acc_txt_4.status = FINISHED
                acc_txt_4.setAutoDraw(False)
        
        # *rej_txt_4* updates
        
        # if rej_txt_4 is starting this frame...
        if rej_txt_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rej_txt_4.frameNStart = frameN  # exact frame index
            rej_txt_4.tStart = t  # local t and not account for scr refresh
            rej_txt_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rej_txt_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            rej_txt_4.status = STARTED
            rej_txt_4.setAutoDraw(True)
        
        # if rej_txt_4 is active this frame...
        if rej_txt_4.status == STARTED:
            # update params
            pass
        
        # if rej_txt_4 is stopping this frame...
        if rej_txt_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rej_txt_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                rej_txt_4.tStop = t  # not accounting for scr refresh
                rej_txt_4.tStopRefresh = tThisFlipGlobal  # on global time
                rej_txt_4.frameNStop = frameN  # exact frame index
                # update status
                rej_txt_4.status = FINISHED
                rej_txt_4.setAutoDraw(False)
        
        # *acc_box_4* updates
        
        # if acc_box_4 is starting this frame...
        if acc_box_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            acc_box_4.frameNStart = frameN  # exact frame index
            acc_box_4.tStart = t  # local t and not account for scr refresh
            acc_box_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(acc_box_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            acc_box_4.status = STARTED
            acc_box_4.setAutoDraw(True)
        
        # if acc_box_4 is active this frame...
        if acc_box_4.status == STARTED:
            # update params
            pass
        
        # if acc_box_4 is stopping this frame...
        if acc_box_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > acc_box_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                acc_box_4.tStop = t  # not accounting for scr refresh
                acc_box_4.tStopRefresh = tThisFlipGlobal  # on global time
                acc_box_4.frameNStop = frameN  # exact frame index
                # update status
                acc_box_4.status = FINISHED
                acc_box_4.setAutoDraw(False)
        
        # *rej_box_4* updates
        
        # if rej_box_4 is starting this frame...
        if rej_box_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rej_box_4.frameNStart = frameN  # exact frame index
            rej_box_4.tStart = t  # local t and not account for scr refresh
            rej_box_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rej_box_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            rej_box_4.status = STARTED
            rej_box_4.setAutoDraw(True)
        
        # if rej_box_4 is active this frame...
        if rej_box_4.status == STARTED:
            # update params
            pass
        
        # if rej_box_4 is stopping this frame...
        if rej_box_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rej_box_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                rej_box_4.tStop = t  # not accounting for scr refresh
                rej_box_4.tStopRefresh = tThisFlipGlobal  # on global time
                rej_box_4.frameNStop = frameN  # exact frame index
                # update status
                rej_box_4.status = FINISHED
                rej_box_4.setAutoDraw(False)
        
        # *upperRight_7* updates
        
        # if upperRight_7 is starting this frame...
        if upperRight_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            upperRight_7.frameNStart = frameN  # exact frame index
            upperRight_7.tStart = t  # local t and not account for scr refresh
            upperRight_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upperRight_7, 'tStartRefresh')  # time at next scr refresh
            # update status
            upperRight_7.status = STARTED
            upperRight_7.setAutoDraw(True)
        
        # if upperRight_7 is active this frame...
        if upperRight_7.status == STARTED:
            # update params
            pass
        
        # if upperRight_7 is stopping this frame...
        if upperRight_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > upperRight_7.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                upperRight_7.tStop = t  # not accounting for scr refresh
                upperRight_7.tStopRefresh = tThisFlipGlobal  # on global time
                upperRight_7.frameNStop = frameN  # exact frame index
                # update status
                upperRight_7.status = FINISHED
                upperRight_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            prc_choice_acc.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prc_choice_acc.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prc_choice_acc" ---
    for thisComponent in prc_choice_acc.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for prc_choice_acc
    prc_choice_acc.tStop = globalClock.getTime(format='float')
    prc_choice_acc.tStopRefresh = tThisFlipGlobal
    thisExp.addData('prc_choice_acc.stopped', prc_choice_acc.tStop)
    # Run 'End Routine' code from box_change_2
    thisExp.addData('trigger down', trigger_list)
    # Run 'End Routine' code from box_clear_2
    acc_box_2.lineColor = 'white'
    rej_box_2.lineColor = 'white'
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if prc_choice_acc.maxDurationReached:
        routineTimer.addTime(-prc_choice_acc.maxDuration)
    elif prc_choice_acc.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "prc_reveal_acc" ---
    # create an object to store info about Routine prc_reveal_acc
    prc_reveal_acc = data.Routine(
        name='prc_reveal_acc',
        components=[you_txt_6, partner_txt_6, dollar_Ytxt_6, dollar_Ptxt_6, you_image_6, partner_image_6, upperRight_8],
    )
    prc_reveal_acc.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    if resp == 0: #reject: no offer
        dollarY = "$ 0"
        dollarO = "$ 0"
        dollarImageY = 'cash/d0.png'
        dollarImageO = 'cash/d0.png'
    # store start times for prc_reveal_acc
    prc_reveal_acc.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    prc_reveal_acc.tStart = globalClock.getTime(format='float')
    prc_reveal_acc.status = STARTED
    thisExp.addData('prc_reveal_acc.started', prc_reveal_acc.tStart)
    prc_reveal_acc.maxDuration = None
    # keep track of which components have finished
    prc_reveal_accComponents = prc_reveal_acc.components
    for thisComponent in prc_reveal_acc.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prc_reveal_acc" ---
    prc_reveal_acc.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_2
        keys = kb.getKeys(['t'])
        if 't' in keys:
            time = core.getTime()
            trigger_list.append(time)
        
        # *you_txt_6* updates
        
        # if you_txt_6 is starting this frame...
        if you_txt_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            you_txt_6.frameNStart = frameN  # exact frame index
            you_txt_6.tStart = t  # local t and not account for scr refresh
            you_txt_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(you_txt_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            you_txt_6.status = STARTED
            you_txt_6.setAutoDraw(True)
        
        # if you_txt_6 is active this frame...
        if you_txt_6.status == STARTED:
            # update params
            pass
        
        # if you_txt_6 is stopping this frame...
        if you_txt_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > you_txt_6.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                you_txt_6.tStop = t  # not accounting for scr refresh
                you_txt_6.tStopRefresh = tThisFlipGlobal  # on global time
                you_txt_6.frameNStop = frameN  # exact frame index
                # update status
                you_txt_6.status = FINISHED
                you_txt_6.setAutoDraw(False)
        
        # *partner_txt_6* updates
        
        # if partner_txt_6 is starting this frame...
        if partner_txt_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            partner_txt_6.frameNStart = frameN  # exact frame index
            partner_txt_6.tStart = t  # local t and not account for scr refresh
            partner_txt_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(partner_txt_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            partner_txt_6.status = STARTED
            partner_txt_6.setAutoDraw(True)
        
        # if partner_txt_6 is active this frame...
        if partner_txt_6.status == STARTED:
            # update params
            pass
        
        # if partner_txt_6 is stopping this frame...
        if partner_txt_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > partner_txt_6.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                partner_txt_6.tStop = t  # not accounting for scr refresh
                partner_txt_6.tStopRefresh = tThisFlipGlobal  # on global time
                partner_txt_6.frameNStop = frameN  # exact frame index
                # update status
                partner_txt_6.status = FINISHED
                partner_txt_6.setAutoDraw(False)
        
        # *dollar_Ytxt_6* updates
        
        # if dollar_Ytxt_6 is starting this frame...
        if dollar_Ytxt_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dollar_Ytxt_6.frameNStart = frameN  # exact frame index
            dollar_Ytxt_6.tStart = t  # local t and not account for scr refresh
            dollar_Ytxt_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dollar_Ytxt_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            dollar_Ytxt_6.status = STARTED
            dollar_Ytxt_6.setAutoDraw(True)
        
        # if dollar_Ytxt_6 is active this frame...
        if dollar_Ytxt_6.status == STARTED:
            # update params
            pass
        
        # if dollar_Ytxt_6 is stopping this frame...
        if dollar_Ytxt_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dollar_Ytxt_6.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                dollar_Ytxt_6.tStop = t  # not accounting for scr refresh
                dollar_Ytxt_6.tStopRefresh = tThisFlipGlobal  # on global time
                dollar_Ytxt_6.frameNStop = frameN  # exact frame index
                # update status
                dollar_Ytxt_6.status = FINISHED
                dollar_Ytxt_6.setAutoDraw(False)
        
        # *dollar_Ptxt_6* updates
        
        # if dollar_Ptxt_6 is starting this frame...
        if dollar_Ptxt_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dollar_Ptxt_6.frameNStart = frameN  # exact frame index
            dollar_Ptxt_6.tStart = t  # local t and not account for scr refresh
            dollar_Ptxt_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dollar_Ptxt_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            dollar_Ptxt_6.status = STARTED
            dollar_Ptxt_6.setAutoDraw(True)
        
        # if dollar_Ptxt_6 is active this frame...
        if dollar_Ptxt_6.status == STARTED:
            # update params
            pass
        
        # if dollar_Ptxt_6 is stopping this frame...
        if dollar_Ptxt_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dollar_Ptxt_6.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                dollar_Ptxt_6.tStop = t  # not accounting for scr refresh
                dollar_Ptxt_6.tStopRefresh = tThisFlipGlobal  # on global time
                dollar_Ptxt_6.frameNStop = frameN  # exact frame index
                # update status
                dollar_Ptxt_6.status = FINISHED
                dollar_Ptxt_6.setAutoDraw(False)
        
        # *you_image_6* updates
        
        # if you_image_6 is starting this frame...
        if you_image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            you_image_6.frameNStart = frameN  # exact frame index
            you_image_6.tStart = t  # local t and not account for scr refresh
            you_image_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(you_image_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            you_image_6.status = STARTED
            you_image_6.setAutoDraw(True)
        
        # if you_image_6 is active this frame...
        if you_image_6.status == STARTED:
            # update params
            pass
        
        # if you_image_6 is stopping this frame...
        if you_image_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > you_image_6.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                you_image_6.tStop = t  # not accounting for scr refresh
                you_image_6.tStopRefresh = tThisFlipGlobal  # on global time
                you_image_6.frameNStop = frameN  # exact frame index
                # update status
                you_image_6.status = FINISHED
                you_image_6.setAutoDraw(False)
        
        # *partner_image_6* updates
        
        # if partner_image_6 is starting this frame...
        if partner_image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            partner_image_6.frameNStart = frameN  # exact frame index
            partner_image_6.tStart = t  # local t and not account for scr refresh
            partner_image_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(partner_image_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            partner_image_6.status = STARTED
            partner_image_6.setAutoDraw(True)
        
        # if partner_image_6 is active this frame...
        if partner_image_6.status == STARTED:
            # update params
            pass
        
        # if partner_image_6 is stopping this frame...
        if partner_image_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > partner_image_6.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                partner_image_6.tStop = t  # not accounting for scr refresh
                partner_image_6.tStopRefresh = tThisFlipGlobal  # on global time
                partner_image_6.frameNStop = frameN  # exact frame index
                # update status
                partner_image_6.status = FINISHED
                partner_image_6.setAutoDraw(False)
        
        # *upperRight_8* updates
        
        # if upperRight_8 is starting this frame...
        if upperRight_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            upperRight_8.frameNStart = frameN  # exact frame index
            upperRight_8.tStart = t  # local t and not account for scr refresh
            upperRight_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upperRight_8, 'tStartRefresh')  # time at next scr refresh
            # update status
            upperRight_8.status = STARTED
            upperRight_8.setAutoDraw(True)
        
        # if upperRight_8 is active this frame...
        if upperRight_8.status == STARTED:
            # update params
            pass
        
        # if upperRight_8 is stopping this frame...
        if upperRight_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > upperRight_8.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                upperRight_8.tStop = t  # not accounting for scr refresh
                upperRight_8.tStopRefresh = tThisFlipGlobal  # on global time
                upperRight_8.frameNStop = frameN  # exact frame index
                # update status
                upperRight_8.status = FINISHED
                upperRight_8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            prc_reveal_acc.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prc_reveal_acc.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prc_reveal_acc" ---
    for thisComponent in prc_reveal_acc.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for prc_reveal_acc
    prc_reveal_acc.tStop = globalClock.getTime(format='float')
    prc_reveal_acc.tStopRefresh = tThisFlipGlobal
    thisExp.addData('prc_reveal_acc.stopped', prc_reveal_acc.tStop)
    # Run 'End Routine' code from code_2
    thisExp.addData('trigger down', trigger_list)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if prc_reveal_acc.maxDurationReached:
        routineTimer.addTime(-prc_reveal_acc.maxDuration)
    elif prc_reveal_acc.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "prc_ins2" ---
    # create an object to store info about Routine prc_ins2
    prc_ins2 = data.Routine(
        name='prc_ins2',
        components=[upperRight_9, main_txt_5, lowMid_5, ins1_key_5],
    )
    prc_ins2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for ins1_key_5
    ins1_key_5.keys = []
    ins1_key_5.rt = []
    _ins1_key_5_allKeys = []
    # store start times for prc_ins2
    prc_ins2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    prc_ins2.tStart = globalClock.getTime(format='float')
    prc_ins2.status = STARTED
    thisExp.addData('prc_ins2.started', prc_ins2.tStart)
    prc_ins2.maxDuration = None
    # keep track of which components have finished
    prc_ins2Components = prc_ins2.components
    for thisComponent in prc_ins2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prc_ins2" ---
    prc_ins2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *upperRight_9* updates
        
        # if upperRight_9 is starting this frame...
        if upperRight_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            upperRight_9.frameNStart = frameN  # exact frame index
            upperRight_9.tStart = t  # local t and not account for scr refresh
            upperRight_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upperRight_9, 'tStartRefresh')  # time at next scr refresh
            # update status
            upperRight_9.status = STARTED
            upperRight_9.setAutoDraw(True)
        
        # if upperRight_9 is active this frame...
        if upperRight_9.status == STARTED:
            # update params
            pass
        
        # *main_txt_5* updates
        
        # if main_txt_5 is starting this frame...
        if main_txt_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            main_txt_5.frameNStart = frameN  # exact frame index
            main_txt_5.tStart = t  # local t and not account for scr refresh
            main_txt_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_txt_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            main_txt_5.status = STARTED
            main_txt_5.setAutoDraw(True)
        
        # if main_txt_5 is active this frame...
        if main_txt_5.status == STARTED:
            # update params
            pass
        
        # *lowMid_5* updates
        
        # if lowMid_5 is starting this frame...
        if lowMid_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lowMid_5.frameNStart = frameN  # exact frame index
            lowMid_5.tStart = t  # local t and not account for scr refresh
            lowMid_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lowMid_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            lowMid_5.status = STARTED
            lowMid_5.setAutoDraw(True)
        
        # if lowMid_5 is active this frame...
        if lowMid_5.status == STARTED:
            # update params
            pass
        
        # *ins1_key_5* updates
        waitOnFlip = False
        
        # if ins1_key_5 is starting this frame...
        if ins1_key_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ins1_key_5.frameNStart = frameN  # exact frame index
            ins1_key_5.tStart = t  # local t and not account for scr refresh
            ins1_key_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins1_key_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins1_key_5.started')
            # update status
            ins1_key_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ins1_key_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ins1_key_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ins1_key_5.status == STARTED and not waitOnFlip:
            theseKeys = ins1_key_5.getKeys(keyList=['space','4'], ignoreKeys=["escape"], waitRelease=False)
            _ins1_key_5_allKeys.extend(theseKeys)
            if len(_ins1_key_5_allKeys):
                ins1_key_5.keys = _ins1_key_5_allKeys[-1].name  # just the last key pressed
                ins1_key_5.rt = _ins1_key_5_allKeys[-1].rt
                ins1_key_5.duration = _ins1_key_5_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            prc_ins2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prc_ins2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prc_ins2" ---
    for thisComponent in prc_ins2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for prc_ins2
    prc_ins2.tStop = globalClock.getTime(format='float')
    prc_ins2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('prc_ins2.stopped', prc_ins2.tStop)
    thisExp.nextEntry()
    # the Routine "prc_ins2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "prc_present_rej" ---
    # create an object to store info about Routine prc_present_rej
    prc_present_rej = data.Routine(
        name='prc_present_rej',
        components=[avatar_3, offer_txt_3, upperRight_10],
    )
    prc_present_rej.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    avatar_3.setImage('practice/Hannah.png')
    # store start times for prc_present_rej
    prc_present_rej.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    prc_present_rej.tStart = globalClock.getTime(format='float')
    prc_present_rej.status = STARTED
    thisExp.addData('prc_present_rej.started', prc_present_rej.tStart)
    prc_present_rej.maxDuration = None
    # keep track of which components have finished
    prc_present_rejComponents = prc_present_rej.components
    for thisComponent in prc_present_rej.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prc_present_rej" ---
    prc_present_rej.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *avatar_3* updates
        
        # if avatar_3 is starting this frame...
        if avatar_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            avatar_3.frameNStart = frameN  # exact frame index
            avatar_3.tStart = t  # local t and not account for scr refresh
            avatar_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(avatar_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            avatar_3.status = STARTED
            avatar_3.setAutoDraw(True)
        
        # if avatar_3 is active this frame...
        if avatar_3.status == STARTED:
            # update params
            pass
        
        # if avatar_3 is stopping this frame...
        if avatar_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > avatar_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                avatar_3.tStop = t  # not accounting for scr refresh
                avatar_3.tStopRefresh = tThisFlipGlobal  # on global time
                avatar_3.frameNStop = frameN  # exact frame index
                # update status
                avatar_3.status = FINISHED
                avatar_3.setAutoDraw(False)
        
        # *offer_txt_3* updates
        
        # if offer_txt_3 is starting this frame...
        if offer_txt_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            offer_txt_3.frameNStart = frameN  # exact frame index
            offer_txt_3.tStart = t  # local t and not account for scr refresh
            offer_txt_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(offer_txt_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            offer_txt_3.status = STARTED
            offer_txt_3.setAutoDraw(True)
        
        # if offer_txt_3 is active this frame...
        if offer_txt_3.status == STARTED:
            # update params
            pass
        
        # if offer_txt_3 is stopping this frame...
        if offer_txt_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > offer_txt_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                offer_txt_3.tStop = t  # not accounting for scr refresh
                offer_txt_3.tStopRefresh = tThisFlipGlobal  # on global time
                offer_txt_3.frameNStop = frameN  # exact frame index
                # update status
                offer_txt_3.status = FINISHED
                offer_txt_3.setAutoDraw(False)
        # Run 'Each Frame' code from code_9
        keys = kb.getKeys(['t'])
        if 't' in keys:
            time = core.getTime()
            trigger_list.append(time)
        
        # *upperRight_10* updates
        
        # if upperRight_10 is starting this frame...
        if upperRight_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            upperRight_10.frameNStart = frameN  # exact frame index
            upperRight_10.tStart = t  # local t and not account for scr refresh
            upperRight_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upperRight_10, 'tStartRefresh')  # time at next scr refresh
            # update status
            upperRight_10.status = STARTED
            upperRight_10.setAutoDraw(True)
        
        # if upperRight_10 is active this frame...
        if upperRight_10.status == STARTED:
            # update params
            pass
        
        # if upperRight_10 is stopping this frame...
        if upperRight_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > upperRight_10.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                upperRight_10.tStop = t  # not accounting for scr refresh
                upperRight_10.tStopRefresh = tThisFlipGlobal  # on global time
                upperRight_10.frameNStop = frameN  # exact frame index
                # update status
                upperRight_10.status = FINISHED
                upperRight_10.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            prc_present_rej.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prc_present_rej.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prc_present_rej" ---
    for thisComponent in prc_present_rej.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for prc_present_rej
    prc_present_rej.tStop = globalClock.getTime(format='float')
    prc_present_rej.tStopRefresh = tThisFlipGlobal
    thisExp.addData('prc_present_rej.stopped', prc_present_rej.tStop)
    # Run 'End Routine' code from code_9
    thisExp.addData('trigger down', trigger_list)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if prc_present_rej.maxDurationReached:
        routineTimer.addTime(-prc_present_rej.maxDuration)
    elif prc_present_rej.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "prc_offer_rej" ---
    # create an object to store info about Routine prc_offer_rej
    prc_offer_rej = data.Routine(
        name='prc_offer_rej',
        components=[you_txt_7, partner_txt_7, dollar_Ytxt_7, dollar_Ptxt_7, you_image_7, partner_image_7, acc_txt_5, rej_txt_5, acc_box_5, rej_box_5, choice_key_3, rej_img, upperRight_11],
    )
    prc_offer_rej.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for choice_key_3
    choice_key_3.keys = []
    choice_key_3.rt = []
    _choice_key_3_allKeys = []
    # Run 'Begin Routine' code from code_10
    keys = kb.getKeys(['t'])
    if 't' in keys:
        time = core.getTime()
        trigger_list.append(time)
    rej_img.setPos([0.4, -0.15])
    # store start times for prc_offer_rej
    prc_offer_rej.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    prc_offer_rej.tStart = globalClock.getTime(format='float')
    prc_offer_rej.status = STARTED
    thisExp.addData('prc_offer_rej.started', prc_offer_rej.tStart)
    prc_offer_rej.maxDuration = None
    # keep track of which components have finished
    prc_offer_rejComponents = prc_offer_rej.components
    for thisComponent in prc_offer_rej.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prc_offer_rej" ---
    prc_offer_rej.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *you_txt_7* updates
        
        # if you_txt_7 is starting this frame...
        if you_txt_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            you_txt_7.frameNStart = frameN  # exact frame index
            you_txt_7.tStart = t  # local t and not account for scr refresh
            you_txt_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(you_txt_7, 'tStartRefresh')  # time at next scr refresh
            # update status
            you_txt_7.status = STARTED
            you_txt_7.setAutoDraw(True)
        
        # if you_txt_7 is active this frame...
        if you_txt_7.status == STARTED:
            # update params
            pass
        
        # *partner_txt_7* updates
        
        # if partner_txt_7 is starting this frame...
        if partner_txt_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            partner_txt_7.frameNStart = frameN  # exact frame index
            partner_txt_7.tStart = t  # local t and not account for scr refresh
            partner_txt_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(partner_txt_7, 'tStartRefresh')  # time at next scr refresh
            # update status
            partner_txt_7.status = STARTED
            partner_txt_7.setAutoDraw(True)
        
        # if partner_txt_7 is active this frame...
        if partner_txt_7.status == STARTED:
            # update params
            pass
        
        # *dollar_Ytxt_7* updates
        
        # if dollar_Ytxt_7 is starting this frame...
        if dollar_Ytxt_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dollar_Ytxt_7.frameNStart = frameN  # exact frame index
            dollar_Ytxt_7.tStart = t  # local t and not account for scr refresh
            dollar_Ytxt_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dollar_Ytxt_7, 'tStartRefresh')  # time at next scr refresh
            # update status
            dollar_Ytxt_7.status = STARTED
            dollar_Ytxt_7.setAutoDraw(True)
        
        # if dollar_Ytxt_7 is active this frame...
        if dollar_Ytxt_7.status == STARTED:
            # update params
            pass
        
        # *dollar_Ptxt_7* updates
        
        # if dollar_Ptxt_7 is starting this frame...
        if dollar_Ptxt_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dollar_Ptxt_7.frameNStart = frameN  # exact frame index
            dollar_Ptxt_7.tStart = t  # local t and not account for scr refresh
            dollar_Ptxt_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dollar_Ptxt_7, 'tStartRefresh')  # time at next scr refresh
            # update status
            dollar_Ptxt_7.status = STARTED
            dollar_Ptxt_7.setAutoDraw(True)
        
        # if dollar_Ptxt_7 is active this frame...
        if dollar_Ptxt_7.status == STARTED:
            # update params
            pass
        
        # *you_image_7* updates
        
        # if you_image_7 is starting this frame...
        if you_image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            you_image_7.frameNStart = frameN  # exact frame index
            you_image_7.tStart = t  # local t and not account for scr refresh
            you_image_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(you_image_7, 'tStartRefresh')  # time at next scr refresh
            # update status
            you_image_7.status = STARTED
            you_image_7.setAutoDraw(True)
        
        # if you_image_7 is active this frame...
        if you_image_7.status == STARTED:
            # update params
            pass
        
        # *partner_image_7* updates
        
        # if partner_image_7 is starting this frame...
        if partner_image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            partner_image_7.frameNStart = frameN  # exact frame index
            partner_image_7.tStart = t  # local t and not account for scr refresh
            partner_image_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(partner_image_7, 'tStartRefresh')  # time at next scr refresh
            # update status
            partner_image_7.status = STARTED
            partner_image_7.setAutoDraw(True)
        
        # if partner_image_7 is active this frame...
        if partner_image_7.status == STARTED:
            # update params
            pass
        
        # *acc_txt_5* updates
        
        # if acc_txt_5 is starting this frame...
        if acc_txt_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            acc_txt_5.frameNStart = frameN  # exact frame index
            acc_txt_5.tStart = t  # local t and not account for scr refresh
            acc_txt_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(acc_txt_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            acc_txt_5.status = STARTED
            acc_txt_5.setAutoDraw(True)
        
        # if acc_txt_5 is active this frame...
        if acc_txt_5.status == STARTED:
            # update params
            pass
        
        # *rej_txt_5* updates
        
        # if rej_txt_5 is starting this frame...
        if rej_txt_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rej_txt_5.frameNStart = frameN  # exact frame index
            rej_txt_5.tStart = t  # local t and not account for scr refresh
            rej_txt_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rej_txt_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            rej_txt_5.status = STARTED
            rej_txt_5.setAutoDraw(True)
        
        # if rej_txt_5 is active this frame...
        if rej_txt_5.status == STARTED:
            # update params
            pass
        
        # *acc_box_5* updates
        
        # if acc_box_5 is starting this frame...
        if acc_box_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            acc_box_5.frameNStart = frameN  # exact frame index
            acc_box_5.tStart = t  # local t and not account for scr refresh
            acc_box_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(acc_box_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            acc_box_5.status = STARTED
            acc_box_5.setAutoDraw(True)
        
        # if acc_box_5 is active this frame...
        if acc_box_5.status == STARTED:
            # update params
            pass
        
        # *rej_box_5* updates
        
        # if rej_box_5 is starting this frame...
        if rej_box_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rej_box_5.frameNStart = frameN  # exact frame index
            rej_box_5.tStart = t  # local t and not account for scr refresh
            rej_box_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rej_box_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            rej_box_5.status = STARTED
            rej_box_5.setAutoDraw(True)
        
        # if rej_box_5 is active this frame...
        if rej_box_5.status == STARTED:
            # update params
            pass
        
        # *choice_key_3* updates
        waitOnFlip = False
        
        # if choice_key_3 is starting this frame...
        if choice_key_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_key_3.frameNStart = frameN  # exact frame index
            choice_key_3.tStart = t  # local t and not account for scr refresh
            choice_key_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_key_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            choice_key_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(choice_key_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(choice_key_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if choice_key_3.status == STARTED and not waitOnFlip:
            theseKeys = choice_key_3.getKeys(keyList=['right','1'], ignoreKeys=["escape"], waitRelease=False)
            _choice_key_3_allKeys.extend(theseKeys)
            if len(_choice_key_3_allKeys):
                choice_key_3.keys = _choice_key_3_allKeys[-1].name  # just the last key pressed
                choice_key_3.rt = _choice_key_3_allKeys[-1].rt
                choice_key_3.duration = _choice_key_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *rej_img* updates
        
        # if rej_img is starting this frame...
        if rej_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rej_img.frameNStart = frameN  # exact frame index
            rej_img.tStart = t  # local t and not account for scr refresh
            rej_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rej_img, 'tStartRefresh')  # time at next scr refresh
            # update status
            rej_img.status = STARTED
            rej_img.setAutoDraw(True)
        
        # if rej_img is active this frame...
        if rej_img.status == STARTED:
            # update params
            pass
        
        # *upperRight_11* updates
        
        # if upperRight_11 is starting this frame...
        if upperRight_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            upperRight_11.frameNStart = frameN  # exact frame index
            upperRight_11.tStart = t  # local t and not account for scr refresh
            upperRight_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upperRight_11, 'tStartRefresh')  # time at next scr refresh
            # update status
            upperRight_11.status = STARTED
            upperRight_11.setAutoDraw(True)
        
        # if upperRight_11 is active this frame...
        if upperRight_11.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            prc_offer_rej.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prc_offer_rej.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prc_offer_rej" ---
    for thisComponent in prc_offer_rej.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for prc_offer_rej
    prc_offer_rej.tStop = globalClock.getTime(format='float')
    prc_offer_rej.tStopRefresh = tThisFlipGlobal
    thisExp.addData('prc_offer_rej.stopped', prc_offer_rej.tStop)
    # Run 'End Routine' code from code_10
    keys = kb.getKeys(['t'])
    if 't' in keys:
        time = core.getTime()
        trigger_list.append(time)
    thisExp.nextEntry()
    # the Routine "prc_offer_rej" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "prc_choice_rej" ---
    # create an object to store info about Routine prc_choice_rej
    prc_choice_rej = data.Routine(
        name='prc_choice_rej',
        components=[you_txt_8, partner_txt_8, dollar_Ytxt_8, dollar_Ptxt_8, you_image_8, partner_image_8, acc_txt_6, rej_txt_6, acc_box_6, rej_box_6, upperRight_12],
    )
    prc_choice_rej.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from box_change_3
    if choice_key_3.keys == 'left' or choice_key_3.keys == '3': #accept
        #time = core.getTime()
        acc_box_6.lineColor = 'black'
        resp = 1
    elif choice_key_3.keys == 'right' or choice_key_3.keys == '1': #reject
        #time = core.getTime()
        rej_box_6.lineColor = 'black'
        resp = 0
    # store start times for prc_choice_rej
    prc_choice_rej.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    prc_choice_rej.tStart = globalClock.getTime(format='float')
    prc_choice_rej.status = STARTED
    thisExp.addData('prc_choice_rej.started', prc_choice_rej.tStart)
    prc_choice_rej.maxDuration = None
    # keep track of which components have finished
    prc_choice_rejComponents = prc_choice_rej.components
    for thisComponent in prc_choice_rej.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prc_choice_rej" ---
    prc_choice_rej.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from box_change_3
        keys = kb.getKeys(['t'])
        if 't' in keys:
            time = core.getTime()
            trigger_list.append(time)
        # wait for keypresses here
        #keys = kb.getKeys()
        #for thisKey in keys:
        #    if thisKey == 't':  # it is equivalent to the string 'q'
        #        time = core.getTime()
        #        print(time)
        #    else:
        #        print(thisKey.name, thisKey.tDown, thisKey.rt)
        
        #keys = kb.getKeys(['t'])
        #if 't' in keys:
        #    time = core.getTime()
        #    print(time)
        
        # *you_txt_8* updates
        
        # if you_txt_8 is starting this frame...
        if you_txt_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            you_txt_8.frameNStart = frameN  # exact frame index
            you_txt_8.tStart = t  # local t and not account for scr refresh
            you_txt_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(you_txt_8, 'tStartRefresh')  # time at next scr refresh
            # update status
            you_txt_8.status = STARTED
            you_txt_8.setAutoDraw(True)
        
        # if you_txt_8 is active this frame...
        if you_txt_8.status == STARTED:
            # update params
            pass
        
        # if you_txt_8 is stopping this frame...
        if you_txt_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > you_txt_8.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                you_txt_8.tStop = t  # not accounting for scr refresh
                you_txt_8.tStopRefresh = tThisFlipGlobal  # on global time
                you_txt_8.frameNStop = frameN  # exact frame index
                # update status
                you_txt_8.status = FINISHED
                you_txt_8.setAutoDraw(False)
        
        # *partner_txt_8* updates
        
        # if partner_txt_8 is starting this frame...
        if partner_txt_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            partner_txt_8.frameNStart = frameN  # exact frame index
            partner_txt_8.tStart = t  # local t and not account for scr refresh
            partner_txt_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(partner_txt_8, 'tStartRefresh')  # time at next scr refresh
            # update status
            partner_txt_8.status = STARTED
            partner_txt_8.setAutoDraw(True)
        
        # if partner_txt_8 is active this frame...
        if partner_txt_8.status == STARTED:
            # update params
            pass
        
        # if partner_txt_8 is stopping this frame...
        if partner_txt_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > partner_txt_8.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                partner_txt_8.tStop = t  # not accounting for scr refresh
                partner_txt_8.tStopRefresh = tThisFlipGlobal  # on global time
                partner_txt_8.frameNStop = frameN  # exact frame index
                # update status
                partner_txt_8.status = FINISHED
                partner_txt_8.setAutoDraw(False)
        
        # *dollar_Ytxt_8* updates
        
        # if dollar_Ytxt_8 is starting this frame...
        if dollar_Ytxt_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dollar_Ytxt_8.frameNStart = frameN  # exact frame index
            dollar_Ytxt_8.tStart = t  # local t and not account for scr refresh
            dollar_Ytxt_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dollar_Ytxt_8, 'tStartRefresh')  # time at next scr refresh
            # update status
            dollar_Ytxt_8.status = STARTED
            dollar_Ytxt_8.setAutoDraw(True)
        
        # if dollar_Ytxt_8 is active this frame...
        if dollar_Ytxt_8.status == STARTED:
            # update params
            pass
        
        # if dollar_Ytxt_8 is stopping this frame...
        if dollar_Ytxt_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dollar_Ytxt_8.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                dollar_Ytxt_8.tStop = t  # not accounting for scr refresh
                dollar_Ytxt_8.tStopRefresh = tThisFlipGlobal  # on global time
                dollar_Ytxt_8.frameNStop = frameN  # exact frame index
                # update status
                dollar_Ytxt_8.status = FINISHED
                dollar_Ytxt_8.setAutoDraw(False)
        
        # *dollar_Ptxt_8* updates
        
        # if dollar_Ptxt_8 is starting this frame...
        if dollar_Ptxt_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dollar_Ptxt_8.frameNStart = frameN  # exact frame index
            dollar_Ptxt_8.tStart = t  # local t and not account for scr refresh
            dollar_Ptxt_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dollar_Ptxt_8, 'tStartRefresh')  # time at next scr refresh
            # update status
            dollar_Ptxt_8.status = STARTED
            dollar_Ptxt_8.setAutoDraw(True)
        
        # if dollar_Ptxt_8 is active this frame...
        if dollar_Ptxt_8.status == STARTED:
            # update params
            pass
        
        # if dollar_Ptxt_8 is stopping this frame...
        if dollar_Ptxt_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dollar_Ptxt_8.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                dollar_Ptxt_8.tStop = t  # not accounting for scr refresh
                dollar_Ptxt_8.tStopRefresh = tThisFlipGlobal  # on global time
                dollar_Ptxt_8.frameNStop = frameN  # exact frame index
                # update status
                dollar_Ptxt_8.status = FINISHED
                dollar_Ptxt_8.setAutoDraw(False)
        
        # *you_image_8* updates
        
        # if you_image_8 is starting this frame...
        if you_image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            you_image_8.frameNStart = frameN  # exact frame index
            you_image_8.tStart = t  # local t and not account for scr refresh
            you_image_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(you_image_8, 'tStartRefresh')  # time at next scr refresh
            # update status
            you_image_8.status = STARTED
            you_image_8.setAutoDraw(True)
        
        # if you_image_8 is active this frame...
        if you_image_8.status == STARTED:
            # update params
            pass
        
        # if you_image_8 is stopping this frame...
        if you_image_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > you_image_8.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                you_image_8.tStop = t  # not accounting for scr refresh
                you_image_8.tStopRefresh = tThisFlipGlobal  # on global time
                you_image_8.frameNStop = frameN  # exact frame index
                # update status
                you_image_8.status = FINISHED
                you_image_8.setAutoDraw(False)
        
        # *partner_image_8* updates
        
        # if partner_image_8 is starting this frame...
        if partner_image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            partner_image_8.frameNStart = frameN  # exact frame index
            partner_image_8.tStart = t  # local t and not account for scr refresh
            partner_image_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(partner_image_8, 'tStartRefresh')  # time at next scr refresh
            # update status
            partner_image_8.status = STARTED
            partner_image_8.setAutoDraw(True)
        
        # if partner_image_8 is active this frame...
        if partner_image_8.status == STARTED:
            # update params
            pass
        
        # if partner_image_8 is stopping this frame...
        if partner_image_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > partner_image_8.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                partner_image_8.tStop = t  # not accounting for scr refresh
                partner_image_8.tStopRefresh = tThisFlipGlobal  # on global time
                partner_image_8.frameNStop = frameN  # exact frame index
                # update status
                partner_image_8.status = FINISHED
                partner_image_8.setAutoDraw(False)
        
        # *acc_txt_6* updates
        
        # if acc_txt_6 is starting this frame...
        if acc_txt_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            acc_txt_6.frameNStart = frameN  # exact frame index
            acc_txt_6.tStart = t  # local t and not account for scr refresh
            acc_txt_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(acc_txt_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            acc_txt_6.status = STARTED
            acc_txt_6.setAutoDraw(True)
        
        # if acc_txt_6 is active this frame...
        if acc_txt_6.status == STARTED:
            # update params
            pass
        
        # if acc_txt_6 is stopping this frame...
        if acc_txt_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > acc_txt_6.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                acc_txt_6.tStop = t  # not accounting for scr refresh
                acc_txt_6.tStopRefresh = tThisFlipGlobal  # on global time
                acc_txt_6.frameNStop = frameN  # exact frame index
                # update status
                acc_txt_6.status = FINISHED
                acc_txt_6.setAutoDraw(False)
        
        # *rej_txt_6* updates
        
        # if rej_txt_6 is starting this frame...
        if rej_txt_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rej_txt_6.frameNStart = frameN  # exact frame index
            rej_txt_6.tStart = t  # local t and not account for scr refresh
            rej_txt_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rej_txt_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            rej_txt_6.status = STARTED
            rej_txt_6.setAutoDraw(True)
        
        # if rej_txt_6 is active this frame...
        if rej_txt_6.status == STARTED:
            # update params
            pass
        
        # if rej_txt_6 is stopping this frame...
        if rej_txt_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rej_txt_6.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                rej_txt_6.tStop = t  # not accounting for scr refresh
                rej_txt_6.tStopRefresh = tThisFlipGlobal  # on global time
                rej_txt_6.frameNStop = frameN  # exact frame index
                # update status
                rej_txt_6.status = FINISHED
                rej_txt_6.setAutoDraw(False)
        
        # *acc_box_6* updates
        
        # if acc_box_6 is starting this frame...
        if acc_box_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            acc_box_6.frameNStart = frameN  # exact frame index
            acc_box_6.tStart = t  # local t and not account for scr refresh
            acc_box_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(acc_box_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            acc_box_6.status = STARTED
            acc_box_6.setAutoDraw(True)
        
        # if acc_box_6 is active this frame...
        if acc_box_6.status == STARTED:
            # update params
            pass
        
        # if acc_box_6 is stopping this frame...
        if acc_box_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > acc_box_6.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                acc_box_6.tStop = t  # not accounting for scr refresh
                acc_box_6.tStopRefresh = tThisFlipGlobal  # on global time
                acc_box_6.frameNStop = frameN  # exact frame index
                # update status
                acc_box_6.status = FINISHED
                acc_box_6.setAutoDraw(False)
        
        # *rej_box_6* updates
        
        # if rej_box_6 is starting this frame...
        if rej_box_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rej_box_6.frameNStart = frameN  # exact frame index
            rej_box_6.tStart = t  # local t and not account for scr refresh
            rej_box_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rej_box_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            rej_box_6.status = STARTED
            rej_box_6.setAutoDraw(True)
        
        # if rej_box_6 is active this frame...
        if rej_box_6.status == STARTED:
            # update params
            pass
        
        # if rej_box_6 is stopping this frame...
        if rej_box_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rej_box_6.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                rej_box_6.tStop = t  # not accounting for scr refresh
                rej_box_6.tStopRefresh = tThisFlipGlobal  # on global time
                rej_box_6.frameNStop = frameN  # exact frame index
                # update status
                rej_box_6.status = FINISHED
                rej_box_6.setAutoDraw(False)
        
        # *upperRight_12* updates
        
        # if upperRight_12 is starting this frame...
        if upperRight_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            upperRight_12.frameNStart = frameN  # exact frame index
            upperRight_12.tStart = t  # local t and not account for scr refresh
            upperRight_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upperRight_12, 'tStartRefresh')  # time at next scr refresh
            # update status
            upperRight_12.status = STARTED
            upperRight_12.setAutoDraw(True)
        
        # if upperRight_12 is active this frame...
        if upperRight_12.status == STARTED:
            # update params
            pass
        
        # if upperRight_12 is stopping this frame...
        if upperRight_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > upperRight_12.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                upperRight_12.tStop = t  # not accounting for scr refresh
                upperRight_12.tStopRefresh = tThisFlipGlobal  # on global time
                upperRight_12.frameNStop = frameN  # exact frame index
                # update status
                upperRight_12.status = FINISHED
                upperRight_12.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            prc_choice_rej.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prc_choice_rej.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prc_choice_rej" ---
    for thisComponent in prc_choice_rej.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for prc_choice_rej
    prc_choice_rej.tStop = globalClock.getTime(format='float')
    prc_choice_rej.tStopRefresh = tThisFlipGlobal
    thisExp.addData('prc_choice_rej.stopped', prc_choice_rej.tStop)
    # Run 'End Routine' code from box_change_3
    thisExp.addData('trigger down', trigger_list)
    # Run 'End Routine' code from box_clear_3
    acc_box_6.lineColor = 'white'
    rej_box_6.lineColor = 'white'
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if prc_choice_rej.maxDurationReached:
        routineTimer.addTime(-prc_choice_rej.maxDuration)
    elif prc_choice_rej.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "prc_reveal_rej" ---
    # create an object to store info about Routine prc_reveal_rej
    prc_reveal_rej = data.Routine(
        name='prc_reveal_rej',
        components=[you_txt_9, partner_txt_9, dollar_Ytxt_9, dollar_Ptxt_9, you_image_9, partner_image_9, upperRight_13],
    )
    prc_reveal_rej.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_11
    if resp == 0: #reject: no offer
        dollarY = "$ 0"
        dollarO = "$ 0"
        dollarImageY = 'cash/d0.png'
        dollarImageO = 'cash/d0.png'
    # store start times for prc_reveal_rej
    prc_reveal_rej.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    prc_reveal_rej.tStart = globalClock.getTime(format='float')
    prc_reveal_rej.status = STARTED
    thisExp.addData('prc_reveal_rej.started', prc_reveal_rej.tStart)
    prc_reveal_rej.maxDuration = None
    # keep track of which components have finished
    prc_reveal_rejComponents = prc_reveal_rej.components
    for thisComponent in prc_reveal_rej.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prc_reveal_rej" ---
    prc_reveal_rej.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_11
        keys = kb.getKeys(['t'])
        if 't' in keys:
            time = core.getTime()
            trigger_list.append(time)
        
        # *you_txt_9* updates
        
        # if you_txt_9 is starting this frame...
        if you_txt_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            you_txt_9.frameNStart = frameN  # exact frame index
            you_txt_9.tStart = t  # local t and not account for scr refresh
            you_txt_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(you_txt_9, 'tStartRefresh')  # time at next scr refresh
            # update status
            you_txt_9.status = STARTED
            you_txt_9.setAutoDraw(True)
        
        # if you_txt_9 is active this frame...
        if you_txt_9.status == STARTED:
            # update params
            pass
        
        # if you_txt_9 is stopping this frame...
        if you_txt_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > you_txt_9.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                you_txt_9.tStop = t  # not accounting for scr refresh
                you_txt_9.tStopRefresh = tThisFlipGlobal  # on global time
                you_txt_9.frameNStop = frameN  # exact frame index
                # update status
                you_txt_9.status = FINISHED
                you_txt_9.setAutoDraw(False)
        
        # *partner_txt_9* updates
        
        # if partner_txt_9 is starting this frame...
        if partner_txt_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            partner_txt_9.frameNStart = frameN  # exact frame index
            partner_txt_9.tStart = t  # local t and not account for scr refresh
            partner_txt_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(partner_txt_9, 'tStartRefresh')  # time at next scr refresh
            # update status
            partner_txt_9.status = STARTED
            partner_txt_9.setAutoDraw(True)
        
        # if partner_txt_9 is active this frame...
        if partner_txt_9.status == STARTED:
            # update params
            pass
        
        # if partner_txt_9 is stopping this frame...
        if partner_txt_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > partner_txt_9.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                partner_txt_9.tStop = t  # not accounting for scr refresh
                partner_txt_9.tStopRefresh = tThisFlipGlobal  # on global time
                partner_txt_9.frameNStop = frameN  # exact frame index
                # update status
                partner_txt_9.status = FINISHED
                partner_txt_9.setAutoDraw(False)
        
        # *dollar_Ytxt_9* updates
        
        # if dollar_Ytxt_9 is starting this frame...
        if dollar_Ytxt_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dollar_Ytxt_9.frameNStart = frameN  # exact frame index
            dollar_Ytxt_9.tStart = t  # local t and not account for scr refresh
            dollar_Ytxt_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dollar_Ytxt_9, 'tStartRefresh')  # time at next scr refresh
            # update status
            dollar_Ytxt_9.status = STARTED
            dollar_Ytxt_9.setAutoDraw(True)
        
        # if dollar_Ytxt_9 is active this frame...
        if dollar_Ytxt_9.status == STARTED:
            # update params
            pass
        
        # if dollar_Ytxt_9 is stopping this frame...
        if dollar_Ytxt_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dollar_Ytxt_9.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                dollar_Ytxt_9.tStop = t  # not accounting for scr refresh
                dollar_Ytxt_9.tStopRefresh = tThisFlipGlobal  # on global time
                dollar_Ytxt_9.frameNStop = frameN  # exact frame index
                # update status
                dollar_Ytxt_9.status = FINISHED
                dollar_Ytxt_9.setAutoDraw(False)
        
        # *dollar_Ptxt_9* updates
        
        # if dollar_Ptxt_9 is starting this frame...
        if dollar_Ptxt_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dollar_Ptxt_9.frameNStart = frameN  # exact frame index
            dollar_Ptxt_9.tStart = t  # local t and not account for scr refresh
            dollar_Ptxt_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dollar_Ptxt_9, 'tStartRefresh')  # time at next scr refresh
            # update status
            dollar_Ptxt_9.status = STARTED
            dollar_Ptxt_9.setAutoDraw(True)
        
        # if dollar_Ptxt_9 is active this frame...
        if dollar_Ptxt_9.status == STARTED:
            # update params
            pass
        
        # if dollar_Ptxt_9 is stopping this frame...
        if dollar_Ptxt_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dollar_Ptxt_9.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                dollar_Ptxt_9.tStop = t  # not accounting for scr refresh
                dollar_Ptxt_9.tStopRefresh = tThisFlipGlobal  # on global time
                dollar_Ptxt_9.frameNStop = frameN  # exact frame index
                # update status
                dollar_Ptxt_9.status = FINISHED
                dollar_Ptxt_9.setAutoDraw(False)
        
        # *you_image_9* updates
        
        # if you_image_9 is starting this frame...
        if you_image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            you_image_9.frameNStart = frameN  # exact frame index
            you_image_9.tStart = t  # local t and not account for scr refresh
            you_image_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(you_image_9, 'tStartRefresh')  # time at next scr refresh
            # update status
            you_image_9.status = STARTED
            you_image_9.setAutoDraw(True)
        
        # if you_image_9 is active this frame...
        if you_image_9.status == STARTED:
            # update params
            pass
        
        # if you_image_9 is stopping this frame...
        if you_image_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > you_image_9.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                you_image_9.tStop = t  # not accounting for scr refresh
                you_image_9.tStopRefresh = tThisFlipGlobal  # on global time
                you_image_9.frameNStop = frameN  # exact frame index
                # update status
                you_image_9.status = FINISHED
                you_image_9.setAutoDraw(False)
        
        # *partner_image_9* updates
        
        # if partner_image_9 is starting this frame...
        if partner_image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            partner_image_9.frameNStart = frameN  # exact frame index
            partner_image_9.tStart = t  # local t and not account for scr refresh
            partner_image_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(partner_image_9, 'tStartRefresh')  # time at next scr refresh
            # update status
            partner_image_9.status = STARTED
            partner_image_9.setAutoDraw(True)
        
        # if partner_image_9 is active this frame...
        if partner_image_9.status == STARTED:
            # update params
            pass
        
        # if partner_image_9 is stopping this frame...
        if partner_image_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > partner_image_9.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                partner_image_9.tStop = t  # not accounting for scr refresh
                partner_image_9.tStopRefresh = tThisFlipGlobal  # on global time
                partner_image_9.frameNStop = frameN  # exact frame index
                # update status
                partner_image_9.status = FINISHED
                partner_image_9.setAutoDraw(False)
        
        # *upperRight_13* updates
        
        # if upperRight_13 is starting this frame...
        if upperRight_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            upperRight_13.frameNStart = frameN  # exact frame index
            upperRight_13.tStart = t  # local t and not account for scr refresh
            upperRight_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upperRight_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            upperRight_13.status = STARTED
            upperRight_13.setAutoDraw(True)
        
        # if upperRight_13 is active this frame...
        if upperRight_13.status == STARTED:
            # update params
            pass
        
        # if upperRight_13 is stopping this frame...
        if upperRight_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > upperRight_13.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                upperRight_13.tStop = t  # not accounting for scr refresh
                upperRight_13.tStopRefresh = tThisFlipGlobal  # on global time
                upperRight_13.frameNStop = frameN  # exact frame index
                # update status
                upperRight_13.status = FINISHED
                upperRight_13.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            prc_reveal_rej.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prc_reveal_rej.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prc_reveal_rej" ---
    for thisComponent in prc_reveal_rej.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for prc_reveal_rej
    prc_reveal_rej.tStop = globalClock.getTime(format='float')
    prc_reveal_rej.tStopRefresh = tThisFlipGlobal
    thisExp.addData('prc_reveal_rej.stopped', prc_reveal_rej.tStop)
    # Run 'End Routine' code from code_11
    thisExp.addData('trigger down', trigger_list)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if prc_reveal_rej.maxDurationReached:
        routineTimer.addTime(-prc_reveal_rej.maxDuration)
    elif prc_reveal_rej.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "ins6" ---
    # create an object to store info about Routine ins6
    ins6 = data.Routine(
        name='ins6',
        components=[upperRight_14, main_txt_6, lowMid_6, ins1_key_6],
    )
    ins6.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for ins1_key_6
    ins1_key_6.keys = []
    ins1_key_6.rt = []
    _ins1_key_6_allKeys = []
    # store start times for ins6
    ins6.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ins6.tStart = globalClock.getTime(format='float')
    ins6.status = STARTED
    thisExp.addData('ins6.started', ins6.tStart)
    ins6.maxDuration = None
    # keep track of which components have finished
    ins6Components = ins6.components
    for thisComponent in ins6.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ins6" ---
    ins6.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *upperRight_14* updates
        
        # if upperRight_14 is starting this frame...
        if upperRight_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            upperRight_14.frameNStart = frameN  # exact frame index
            upperRight_14.tStart = t  # local t and not account for scr refresh
            upperRight_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upperRight_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            upperRight_14.status = STARTED
            upperRight_14.setAutoDraw(True)
        
        # if upperRight_14 is active this frame...
        if upperRight_14.status == STARTED:
            # update params
            pass
        
        # *main_txt_6* updates
        
        # if main_txt_6 is starting this frame...
        if main_txt_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            main_txt_6.frameNStart = frameN  # exact frame index
            main_txt_6.tStart = t  # local t and not account for scr refresh
            main_txt_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_txt_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            main_txt_6.status = STARTED
            main_txt_6.setAutoDraw(True)
        
        # if main_txt_6 is active this frame...
        if main_txt_6.status == STARTED:
            # update params
            pass
        
        # *lowMid_6* updates
        
        # if lowMid_6 is starting this frame...
        if lowMid_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lowMid_6.frameNStart = frameN  # exact frame index
            lowMid_6.tStart = t  # local t and not account for scr refresh
            lowMid_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lowMid_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            lowMid_6.status = STARTED
            lowMid_6.setAutoDraw(True)
        
        # if lowMid_6 is active this frame...
        if lowMid_6.status == STARTED:
            # update params
            pass
        
        # *ins1_key_6* updates
        waitOnFlip = False
        
        # if ins1_key_6 is starting this frame...
        if ins1_key_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ins1_key_6.frameNStart = frameN  # exact frame index
            ins1_key_6.tStart = t  # local t and not account for scr refresh
            ins1_key_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ins1_key_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ins1_key_6.started')
            # update status
            ins1_key_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ins1_key_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ins1_key_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ins1_key_6.status == STARTED and not waitOnFlip:
            theseKeys = ins1_key_6.getKeys(keyList=['space','4'], ignoreKeys=["escape"], waitRelease=False)
            _ins1_key_6_allKeys.extend(theseKeys)
            if len(_ins1_key_6_allKeys):
                ins1_key_6.keys = _ins1_key_6_allKeys[-1].name  # just the last key pressed
                ins1_key_6.rt = _ins1_key_6_allKeys[-1].rt
                ins1_key_6.duration = _ins1_key_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ins6.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ins6.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ins6" ---
    for thisComponent in ins6.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ins6
    ins6.tStop = globalClock.getTime(format='float')
    ins6.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ins6.stopped', ins6.tStop)
    thisExp.nextEntry()
    # the Routine "ins6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "exp_prep" ---
    # create an object to store info about Routine exp_prep
    exp_prep = data.Routine(
        name='exp_prep',
        components=[ExpStart_key, trigger_txt],
    )
    exp_prep.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for ExpStart_key
    ExpStart_key.keys = []
    ExpStart_key.rt = []
    _ExpStart_key_allKeys = []
    # store start times for exp_prep
    exp_prep.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    exp_prep.tStart = globalClock.getTime(format='float')
    exp_prep.status = STARTED
    thisExp.addData('exp_prep.started', exp_prep.tStart)
    exp_prep.maxDuration = None
    # keep track of which components have finished
    exp_prepComponents = exp_prep.components
    for thisComponent in exp_prep.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "exp_prep" ---
    exp_prep.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from main_code
        #keys = kb.getKeys(['t'])
        #if 't' in keys:
        #    time = core.getTime()
        #    trigger_list.append(time)
        
        # *ExpStart_key* updates
        waitOnFlip = False
        
        # if ExpStart_key is starting this frame...
        if ExpStart_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ExpStart_key.frameNStart = frameN  # exact frame index
            ExpStart_key.tStart = t  # local t and not account for scr refresh
            ExpStart_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExpStart_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ExpStart_key.started')
            # update status
            ExpStart_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ExpStart_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ExpStart_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ExpStart_key.status == STARTED and not waitOnFlip:
            theseKeys = ExpStart_key.getKeys(keyList=['t'], ignoreKeys=["escape"], waitRelease=False)
            _ExpStart_key_allKeys.extend(theseKeys)
            if len(_ExpStart_key_allKeys):
                ExpStart_key.keys = [key.name for key in _ExpStart_key_allKeys]  # storing all keys
                ExpStart_key.rt = [key.rt for key in _ExpStart_key_allKeys]
                ExpStart_key.duration = [key.duration for key in _ExpStart_key_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # *trigger_txt* updates
        
        # if trigger_txt is starting this frame...
        if trigger_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trigger_txt.frameNStart = frameN  # exact frame index
            trigger_txt.tStart = t  # local t and not account for scr refresh
            trigger_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trigger_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            trigger_txt.status = STARTED
            trigger_txt.setAutoDraw(True)
        
        # if trigger_txt is active this frame...
        if trigger_txt.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            exp_prep.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exp_prep.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "exp_prep" ---
    for thisComponent in exp_prep.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for exp_prep
    exp_prep.tStop = globalClock.getTime(format='float')
    exp_prep.tStopRefresh = tThisFlipGlobal
    thisExp.addData('exp_prep.stopped', exp_prep.tStop)
    # Run 'End Routine' code from main_code
    #thisExp.addData('trigger down', trigger_list)
    # check responses
    if ExpStart_key.keys in ['', [], None]:  # No response was made
        ExpStart_key.keys = None
    thisExp.addData('ExpStart_key.keys',ExpStart_key.keys)
    if ExpStart_key.keys != None:  # we had a response
        thisExp.addData('ExpStart_key.rt', ExpStart_key.rt)
        thisExp.addData('ExpStart_key.duration', ExpStart_key.duration)
    thisExp.nextEntry()
    # the Routine "exp_prep" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    team_block = data.TrialHandler2(
        name='team_block',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(conditionfolder), 
        seed=None, 
    )
    thisExp.addLoop(team_block)  # add the loop to the experiment
    thisTeam_block = team_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTeam_block.rgb)
    if thisTeam_block != None:
        for paramName in thisTeam_block:
            globals()[paramName] = thisTeam_block[paramName]
    
    for thisTeam_block in team_block:
        currentLoop = team_block
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisTeam_block.rgb)
        if thisTeam_block != None:
            for paramName in thisTeam_block:
                globals()[paramName] = thisTeam_block[paramName]
        
        # --- Prepare to start Routine "team" ---
        # create an object to store info about Routine team
        team = data.Routine(
            name='team',
            components=[team_img, team_txt1, team_key, text, team_txt2],
        )
        team.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        team_img.setImage(teamDir)
        # create starting attributes for team_key
        team_key.keys = []
        team_key.rt = []
        _team_key_allKeys = []
        team_txt2.setColor(teamColor, colorSpace='rgb')
        team_txt2.setText(team)
        # Run 'Begin Routine' code from team_rand
        random.shuffle(nc_offer)
        noControl = nc_first + nc_offer
        print("offer", noControl, len(noControl))
        
        random.shuffle(jitter)
        # store start times for team
        team.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        team.tStart = globalClock.getTime(format='float')
        team.status = STARTED
        thisExp.addData('team.started', team.tStart)
        team.maxDuration = None
        # keep track of which components have finished
        teamComponents = team.components
        for thisComponent in team.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "team" ---
        # if trial has changed, end Routine now
        if isinstance(team_block, data.TrialHandler2) and thisTeam_block.thisN != team_block.thisTrial.thisN:
            continueRoutine = False
        team.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *team_img* updates
            
            # if team_img is starting this frame...
            if team_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                team_img.frameNStart = frameN  # exact frame index
                team_img.tStart = t  # local t and not account for scr refresh
                team_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(team_img, 'tStartRefresh')  # time at next scr refresh
                # update status
                team_img.status = STARTED
                team_img.setAutoDraw(True)
            
            # if team_img is active this frame...
            if team_img.status == STARTED:
                # update params
                pass
            
            # *team_txt1* updates
            
            # if team_txt1 is starting this frame...
            if team_txt1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                team_txt1.frameNStart = frameN  # exact frame index
                team_txt1.tStart = t  # local t and not account for scr refresh
                team_txt1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(team_txt1, 'tStartRefresh')  # time at next scr refresh
                # update status
                team_txt1.status = STARTED
                team_txt1.setAutoDraw(True)
            
            # if team_txt1 is active this frame...
            if team_txt1.status == STARTED:
                # update params
                pass
            
            # *team_key* updates
            waitOnFlip = False
            
            # if team_key is starting this frame...
            if team_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                team_key.frameNStart = frameN  # exact frame index
                team_key.tStart = t  # local t and not account for scr refresh
                team_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(team_key, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'team_key.started')
                # update status
                team_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(team_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(team_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if team_key.status == STARTED and not waitOnFlip:
                theseKeys = team_key.getKeys(keyList=['space','4'], ignoreKeys=["escape"], waitRelease=False)
                _team_key_allKeys.extend(theseKeys)
                if len(_team_key_allKeys):
                    team_key.keys = _team_key_allKeys[-1].name  # just the last key pressed
                    team_key.rt = _team_key_allKeys[-1].rt
                    team_key.duration = _team_key_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # *team_txt2* updates
            
            # if team_txt2 is starting this frame...
            if team_txt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                team_txt2.frameNStart = frameN  # exact frame index
                team_txt2.tStart = t  # local t and not account for scr refresh
                team_txt2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(team_txt2, 'tStartRefresh')  # time at next scr refresh
                # update status
                team_txt2.status = STARTED
                team_txt2.setAutoDraw(True)
            
            # if team_txt2 is active this frame...
            if team_txt2.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from team_rand
            keys = kb.getKeys(['t'])
            if 't' in keys:
                time = core.getTime()
                trigger_list.append(time)
            
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                team.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in team.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "team" ---
        for thisComponent in team.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for team
        team.tStop = globalClock.getTime(format='float')
        team.tStopRefresh = tThisFlipGlobal
        thisExp.addData('team.stopped', team.tStop)
        # check responses
        if team_key.keys in ['', [], None]:  # No response was made
            team_key.keys = None
        team_block.addData('team_key.keys',team_key.keys)
        if team_key.keys != None:  # we had a response
            team_block.addData('team_key.rt', team_key.rt)
            team_block.addData('team_key.duration', team_key.duration)
        # Run 'End Routine' code from team_rand
        thisExp.addData('trigger down', trigger_list)
        # the Routine "team" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler2(
            name='trials',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(test), 
            seed=None, 
        )
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial in trials:
            currentLoop = trials
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    globals()[paramName] = thisTrial[paramName]
            
            # --- Prepare to start Routine "trial_prep" ---
            # create an object to store info about Routine trial_prep
            trial_prep = data.Routine(
                name='trial_prep',
                components=[],
            )
            trial_prep.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from settings_trial
            avatar_prop = name + " proposes"
            avatar_final = name + " gets:"
            
            offerY = noControl[offerIndex]
            offerO = 20-noControl[offerIndex]
            
            dollarY = '$ ' + str(offerY)
            dollarO = '$ ' + str(offerO)
            dollarImageY = 'cash\d' + str(offerY) + '.png'
            dollarImageO = 'cash\d' + str(offerO) + '.png'
            
            thisExp.addData('offer you', offerY)
            thisExp.addData('offer other', offerO)
            
            jitter_trial = jitter[offerIndex]
            # store start times for trial_prep
            trial_prep.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_prep.tStart = globalClock.getTime(format='float')
            trial_prep.status = STARTED
            thisExp.addData('trial_prep.started', trial_prep.tStart)
            trial_prep.maxDuration = None
            # keep track of which components have finished
            trial_prepComponents = trial_prep.components
            for thisComponent in trial_prep.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_prep" ---
            # if trial has changed, end Routine now
            if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                continueRoutine = False
            trial_prep.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from settings_trial
                keys = kb.getKeys(['t'])
                if 't' in keys:
                    time = core.getTime()
                    trigger_list.append(time)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_prep.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_prep.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_prep" ---
            for thisComponent in trial_prep.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_prep
            trial_prep.tStop = globalClock.getTime(format='float')
            trial_prep.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_prep.stopped', trial_prep.tStop)
            # Run 'End Routine' code from settings_trial
            thisExp.addData('trigger down', trigger_list)
            
            # the Routine "trial_prep" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "avatar_present" ---
            # create an object to store info about Routine avatar_present
            avatar_present = data.Routine(
                name='avatar_present',
                components=[avatar, offer_txt],
            )
            avatar_present.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            avatar.setImage(directory)
            offer_txt.setText(avatar_prop)
            # store start times for avatar_present
            avatar_present.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            avatar_present.tStart = globalClock.getTime(format='float')
            avatar_present.status = STARTED
            thisExp.addData('avatar_present.started', avatar_present.tStart)
            avatar_present.maxDuration = None
            # keep track of which components have finished
            avatar_presentComponents = avatar_present.components
            for thisComponent in avatar_present.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "avatar_present" ---
            # if trial has changed, end Routine now
            if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                continueRoutine = False
            avatar_present.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *avatar* updates
                
                # if avatar is starting this frame...
                if avatar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    avatar.frameNStart = frameN  # exact frame index
                    avatar.tStart = t  # local t and not account for scr refresh
                    avatar.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(avatar, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    avatar.status = STARTED
                    avatar.setAutoDraw(True)
                
                # if avatar is active this frame...
                if avatar.status == STARTED:
                    # update params
                    pass
                
                # if avatar is stopping this frame...
                if avatar.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > avatar.tStartRefresh + jitter_trial-frameTolerance:
                        # keep track of stop time/frame for later
                        avatar.tStop = t  # not accounting for scr refresh
                        avatar.tStopRefresh = tThisFlipGlobal  # on global time
                        avatar.frameNStop = frameN  # exact frame index
                        # update status
                        avatar.status = FINISHED
                        avatar.setAutoDraw(False)
                
                # *offer_txt* updates
                
                # if offer_txt is starting this frame...
                if offer_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    offer_txt.frameNStart = frameN  # exact frame index
                    offer_txt.tStart = t  # local t and not account for scr refresh
                    offer_txt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(offer_txt, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'offer_txt.started')
                    # update status
                    offer_txt.status = STARTED
                    offer_txt.setAutoDraw(True)
                
                # if offer_txt is active this frame...
                if offer_txt.status == STARTED:
                    # update params
                    pass
                
                # if offer_txt is stopping this frame...
                if offer_txt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > offer_txt.tStartRefresh + jitter_trial-frameTolerance:
                        # keep track of stop time/frame for later
                        offer_txt.tStop = t  # not accounting for scr refresh
                        offer_txt.tStopRefresh = tThisFlipGlobal  # on global time
                        offer_txt.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'offer_txt.stopped')
                        # update status
                        offer_txt.status = FINISHED
                        offer_txt.setAutoDraw(False)
                # Run 'Each Frame' code from code_3
                keys = kb.getKeys(['t'])
                if 't' in keys:
                    time = core.getTime()
                    trigger_list.append(time)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    avatar_present.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in avatar_present.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "avatar_present" ---
            for thisComponent in avatar_present.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for avatar_present
            avatar_present.tStop = globalClock.getTime(format='float')
            avatar_present.tStopRefresh = tThisFlipGlobal
            thisExp.addData('avatar_present.stopped', avatar_present.tStop)
            # Run 'End Routine' code from code_3
            thisExp.addData('trigger down', trigger_list)
            thisExp.addData('jitter_sec', jitter_trial)
            # the Routine "avatar_present" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "offer_present" ---
            # create an object to store info about Routine offer_present
            offer_present = data.Routine(
                name='offer_present',
                components=[you_txt, partner_txt, dollar_Ytxt, dollar_Ptxt, you_image, partner_image, acc_txt, rej_txt, acc_box, rej_box, choice_key],
            )
            offer_present.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            partner_txt.setText(name)
            dollar_Ytxt.setText(dollarY)
            dollar_Ptxt.setText(dollarO)
            you_image.setImage(dollarImageY)
            partner_image.setImage(dollarImageO)
            # create starting attributes for choice_key
            choice_key.keys = []
            choice_key.rt = []
            _choice_key_allKeys = []
            # store start times for offer_present
            offer_present.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            offer_present.tStart = globalClock.getTime(format='float')
            offer_present.status = STARTED
            thisExp.addData('offer_present.started', offer_present.tStart)
            offer_present.maxDuration = None
            # keep track of which components have finished
            offer_presentComponents = offer_present.components
            for thisComponent in offer_present.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "offer_present" ---
            # if trial has changed, end Routine now
            if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                continueRoutine = False
            offer_present.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *you_txt* updates
                
                # if you_txt is starting this frame...
                if you_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    you_txt.frameNStart = frameN  # exact frame index
                    you_txt.tStart = t  # local t and not account for scr refresh
                    you_txt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(you_txt, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    you_txt.status = STARTED
                    you_txt.setAutoDraw(True)
                
                # if you_txt is active this frame...
                if you_txt.status == STARTED:
                    # update params
                    pass
                
                # *partner_txt* updates
                
                # if partner_txt is starting this frame...
                if partner_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    partner_txt.frameNStart = frameN  # exact frame index
                    partner_txt.tStart = t  # local t and not account for scr refresh
                    partner_txt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(partner_txt, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    partner_txt.status = STARTED
                    partner_txt.setAutoDraw(True)
                
                # if partner_txt is active this frame...
                if partner_txt.status == STARTED:
                    # update params
                    pass
                
                # *dollar_Ytxt* updates
                
                # if dollar_Ytxt is starting this frame...
                if dollar_Ytxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    dollar_Ytxt.frameNStart = frameN  # exact frame index
                    dollar_Ytxt.tStart = t  # local t and not account for scr refresh
                    dollar_Ytxt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dollar_Ytxt, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    dollar_Ytxt.status = STARTED
                    dollar_Ytxt.setAutoDraw(True)
                
                # if dollar_Ytxt is active this frame...
                if dollar_Ytxt.status == STARTED:
                    # update params
                    pass
                
                # *dollar_Ptxt* updates
                
                # if dollar_Ptxt is starting this frame...
                if dollar_Ptxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    dollar_Ptxt.frameNStart = frameN  # exact frame index
                    dollar_Ptxt.tStart = t  # local t and not account for scr refresh
                    dollar_Ptxt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dollar_Ptxt, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    dollar_Ptxt.status = STARTED
                    dollar_Ptxt.setAutoDraw(True)
                
                # if dollar_Ptxt is active this frame...
                if dollar_Ptxt.status == STARTED:
                    # update params
                    pass
                
                # *you_image* updates
                
                # if you_image is starting this frame...
                if you_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    you_image.frameNStart = frameN  # exact frame index
                    you_image.tStart = t  # local t and not account for scr refresh
                    you_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(you_image, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    you_image.status = STARTED
                    you_image.setAutoDraw(True)
                
                # if you_image is active this frame...
                if you_image.status == STARTED:
                    # update params
                    pass
                
                # *partner_image* updates
                
                # if partner_image is starting this frame...
                if partner_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    partner_image.frameNStart = frameN  # exact frame index
                    partner_image.tStart = t  # local t and not account for scr refresh
                    partner_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(partner_image, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    partner_image.status = STARTED
                    partner_image.setAutoDraw(True)
                
                # if partner_image is active this frame...
                if partner_image.status == STARTED:
                    # update params
                    pass
                
                # *acc_txt* updates
                
                # if acc_txt is starting this frame...
                if acc_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    acc_txt.frameNStart = frameN  # exact frame index
                    acc_txt.tStart = t  # local t and not account for scr refresh
                    acc_txt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(acc_txt, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    acc_txt.status = STARTED
                    acc_txt.setAutoDraw(True)
                
                # if acc_txt is active this frame...
                if acc_txt.status == STARTED:
                    # update params
                    pass
                
                # *rej_txt* updates
                
                # if rej_txt is starting this frame...
                if rej_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rej_txt.frameNStart = frameN  # exact frame index
                    rej_txt.tStart = t  # local t and not account for scr refresh
                    rej_txt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rej_txt, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    rej_txt.status = STARTED
                    rej_txt.setAutoDraw(True)
                
                # if rej_txt is active this frame...
                if rej_txt.status == STARTED:
                    # update params
                    pass
                
                # *acc_box* updates
                
                # if acc_box is starting this frame...
                if acc_box.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    acc_box.frameNStart = frameN  # exact frame index
                    acc_box.tStart = t  # local t and not account for scr refresh
                    acc_box.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(acc_box, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    acc_box.status = STARTED
                    acc_box.setAutoDraw(True)
                
                # if acc_box is active this frame...
                if acc_box.status == STARTED:
                    # update params
                    pass
                
                # *rej_box* updates
                
                # if rej_box is starting this frame...
                if rej_box.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rej_box.frameNStart = frameN  # exact frame index
                    rej_box.tStart = t  # local t and not account for scr refresh
                    rej_box.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rej_box, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    rej_box.status = STARTED
                    rej_box.setAutoDraw(True)
                
                # if rej_box is active this frame...
                if rej_box.status == STARTED:
                    # update params
                    pass
                
                # *choice_key* updates
                waitOnFlip = False
                
                # if choice_key is starting this frame...
                if choice_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    choice_key.frameNStart = frameN  # exact frame index
                    choice_key.tStart = t  # local t and not account for scr refresh
                    choice_key.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(choice_key, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'choice_key.started')
                    # update status
                    choice_key.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(choice_key.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(choice_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if choice_key.status == STARTED and not waitOnFlip:
                    theseKeys = choice_key.getKeys(keyList=['left','right','3','1'], ignoreKeys=["escape"], waitRelease=False)
                    _choice_key_allKeys.extend(theseKeys)
                    if len(_choice_key_allKeys):
                        choice_key.keys = _choice_key_allKeys[-1].name  # just the last key pressed
                        choice_key.rt = _choice_key_allKeys[-1].rt
                        choice_key.duration = _choice_key_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                # Run 'Each Frame' code from code_4
                keys = kb.getKeys(['t'])
                if 't' in keys:
                    time = core.getTime()
                    trigger_list.append(time)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    offer_present.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in offer_present.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "offer_present" ---
            for thisComponent in offer_present.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for offer_present
            offer_present.tStop = globalClock.getTime(format='float')
            offer_present.tStopRefresh = tThisFlipGlobal
            thisExp.addData('offer_present.stopped', offer_present.tStop)
            # check responses
            if choice_key.keys in ['', [], None]:  # No response was made
                choice_key.keys = None
            trials.addData('choice_key.keys',choice_key.keys)
            if choice_key.keys != None:  # we had a response
                trials.addData('choice_key.rt', choice_key.rt)
                trials.addData('choice_key.duration', choice_key.duration)
            # Run 'End Routine' code from code_4
            thisExp.addData('trigger down', trigger_list)
            # the Routine "offer_present" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "offer_choice" ---
            # create an object to store info about Routine offer_choice
            offer_choice = data.Routine(
                name='offer_choice',
                components=[you_txt_2, partner_txt_2, dollar_Ytxt_2, dollar_Ptxt_2, you_image_2, partner_image_2, acc_txt_2, rej_txt_2, acc_box_2, rej_box_2],
            )
            offer_choice.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from box_change
            if choice_key.keys == 'left' or choice_key.keys == '3': #accept
                #time = core.getTime()
                acc_box_2.lineColor = 'black'
                resp = 1
            elif choice_key.keys == 'right' or choice_key.keys == '1': #reject
                #time = core.getTime()
                rej_box_2.lineColor = 'black'
                resp = 0
            partner_txt_2.setText(name)
            dollar_Ytxt_2.setText(dollarY)
            dollar_Ptxt_2.setText(dollarO)
            you_image_2.setImage(dollarImageY)
            partner_image_2.setImage(dollarImageO)
            # store start times for offer_choice
            offer_choice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            offer_choice.tStart = globalClock.getTime(format='float')
            offer_choice.status = STARTED
            thisExp.addData('offer_choice.started', offer_choice.tStart)
            offer_choice.maxDuration = None
            # keep track of which components have finished
            offer_choiceComponents = offer_choice.components
            for thisComponent in offer_choice.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "offer_choice" ---
            # if trial has changed, end Routine now
            if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                continueRoutine = False
            offer_choice.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from box_change
                keys = kb.getKeys(['t'])
                if 't' in keys:
                    time = core.getTime()
                    trigger_list.append(time)
                
                # *you_txt_2* updates
                
                # if you_txt_2 is starting this frame...
                if you_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    you_txt_2.frameNStart = frameN  # exact frame index
                    you_txt_2.tStart = t  # local t and not account for scr refresh
                    you_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(you_txt_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    you_txt_2.status = STARTED
                    you_txt_2.setAutoDraw(True)
                
                # if you_txt_2 is active this frame...
                if you_txt_2.status == STARTED:
                    # update params
                    pass
                
                # if you_txt_2 is stopping this frame...
                if you_txt_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > you_txt_2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        you_txt_2.tStop = t  # not accounting for scr refresh
                        you_txt_2.tStopRefresh = tThisFlipGlobal  # on global time
                        you_txt_2.frameNStop = frameN  # exact frame index
                        # update status
                        you_txt_2.status = FINISHED
                        you_txt_2.setAutoDraw(False)
                
                # *partner_txt_2* updates
                
                # if partner_txt_2 is starting this frame...
                if partner_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    partner_txt_2.frameNStart = frameN  # exact frame index
                    partner_txt_2.tStart = t  # local t and not account for scr refresh
                    partner_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(partner_txt_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    partner_txt_2.status = STARTED
                    partner_txt_2.setAutoDraw(True)
                
                # if partner_txt_2 is active this frame...
                if partner_txt_2.status == STARTED:
                    # update params
                    pass
                
                # if partner_txt_2 is stopping this frame...
                if partner_txt_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > partner_txt_2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        partner_txt_2.tStop = t  # not accounting for scr refresh
                        partner_txt_2.tStopRefresh = tThisFlipGlobal  # on global time
                        partner_txt_2.frameNStop = frameN  # exact frame index
                        # update status
                        partner_txt_2.status = FINISHED
                        partner_txt_2.setAutoDraw(False)
                
                # *dollar_Ytxt_2* updates
                
                # if dollar_Ytxt_2 is starting this frame...
                if dollar_Ytxt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    dollar_Ytxt_2.frameNStart = frameN  # exact frame index
                    dollar_Ytxt_2.tStart = t  # local t and not account for scr refresh
                    dollar_Ytxt_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dollar_Ytxt_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    dollar_Ytxt_2.status = STARTED
                    dollar_Ytxt_2.setAutoDraw(True)
                
                # if dollar_Ytxt_2 is active this frame...
                if dollar_Ytxt_2.status == STARTED:
                    # update params
                    pass
                
                # if dollar_Ytxt_2 is stopping this frame...
                if dollar_Ytxt_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dollar_Ytxt_2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        dollar_Ytxt_2.tStop = t  # not accounting for scr refresh
                        dollar_Ytxt_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dollar_Ytxt_2.frameNStop = frameN  # exact frame index
                        # update status
                        dollar_Ytxt_2.status = FINISHED
                        dollar_Ytxt_2.setAutoDraw(False)
                
                # *dollar_Ptxt_2* updates
                
                # if dollar_Ptxt_2 is starting this frame...
                if dollar_Ptxt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    dollar_Ptxt_2.frameNStart = frameN  # exact frame index
                    dollar_Ptxt_2.tStart = t  # local t and not account for scr refresh
                    dollar_Ptxt_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dollar_Ptxt_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    dollar_Ptxt_2.status = STARTED
                    dollar_Ptxt_2.setAutoDraw(True)
                
                # if dollar_Ptxt_2 is active this frame...
                if dollar_Ptxt_2.status == STARTED:
                    # update params
                    pass
                
                # if dollar_Ptxt_2 is stopping this frame...
                if dollar_Ptxt_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dollar_Ptxt_2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        dollar_Ptxt_2.tStop = t  # not accounting for scr refresh
                        dollar_Ptxt_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dollar_Ptxt_2.frameNStop = frameN  # exact frame index
                        # update status
                        dollar_Ptxt_2.status = FINISHED
                        dollar_Ptxt_2.setAutoDraw(False)
                
                # *you_image_2* updates
                
                # if you_image_2 is starting this frame...
                if you_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    you_image_2.frameNStart = frameN  # exact frame index
                    you_image_2.tStart = t  # local t and not account for scr refresh
                    you_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(you_image_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    you_image_2.status = STARTED
                    you_image_2.setAutoDraw(True)
                
                # if you_image_2 is active this frame...
                if you_image_2.status == STARTED:
                    # update params
                    pass
                
                # if you_image_2 is stopping this frame...
                if you_image_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > you_image_2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        you_image_2.tStop = t  # not accounting for scr refresh
                        you_image_2.tStopRefresh = tThisFlipGlobal  # on global time
                        you_image_2.frameNStop = frameN  # exact frame index
                        # update status
                        you_image_2.status = FINISHED
                        you_image_2.setAutoDraw(False)
                
                # *partner_image_2* updates
                
                # if partner_image_2 is starting this frame...
                if partner_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    partner_image_2.frameNStart = frameN  # exact frame index
                    partner_image_2.tStart = t  # local t and not account for scr refresh
                    partner_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(partner_image_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    partner_image_2.status = STARTED
                    partner_image_2.setAutoDraw(True)
                
                # if partner_image_2 is active this frame...
                if partner_image_2.status == STARTED:
                    # update params
                    pass
                
                # if partner_image_2 is stopping this frame...
                if partner_image_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > partner_image_2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        partner_image_2.tStop = t  # not accounting for scr refresh
                        partner_image_2.tStopRefresh = tThisFlipGlobal  # on global time
                        partner_image_2.frameNStop = frameN  # exact frame index
                        # update status
                        partner_image_2.status = FINISHED
                        partner_image_2.setAutoDraw(False)
                
                # *acc_txt_2* updates
                
                # if acc_txt_2 is starting this frame...
                if acc_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    acc_txt_2.frameNStart = frameN  # exact frame index
                    acc_txt_2.tStart = t  # local t and not account for scr refresh
                    acc_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(acc_txt_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    acc_txt_2.status = STARTED
                    acc_txt_2.setAutoDraw(True)
                
                # if acc_txt_2 is active this frame...
                if acc_txt_2.status == STARTED:
                    # update params
                    pass
                
                # if acc_txt_2 is stopping this frame...
                if acc_txt_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > acc_txt_2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        acc_txt_2.tStop = t  # not accounting for scr refresh
                        acc_txt_2.tStopRefresh = tThisFlipGlobal  # on global time
                        acc_txt_2.frameNStop = frameN  # exact frame index
                        # update status
                        acc_txt_2.status = FINISHED
                        acc_txt_2.setAutoDraw(False)
                
                # *rej_txt_2* updates
                
                # if rej_txt_2 is starting this frame...
                if rej_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rej_txt_2.frameNStart = frameN  # exact frame index
                    rej_txt_2.tStart = t  # local t and not account for scr refresh
                    rej_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rej_txt_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    rej_txt_2.status = STARTED
                    rej_txt_2.setAutoDraw(True)
                
                # if rej_txt_2 is active this frame...
                if rej_txt_2.status == STARTED:
                    # update params
                    pass
                
                # if rej_txt_2 is stopping this frame...
                if rej_txt_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rej_txt_2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        rej_txt_2.tStop = t  # not accounting for scr refresh
                        rej_txt_2.tStopRefresh = tThisFlipGlobal  # on global time
                        rej_txt_2.frameNStop = frameN  # exact frame index
                        # update status
                        rej_txt_2.status = FINISHED
                        rej_txt_2.setAutoDraw(False)
                
                # *acc_box_2* updates
                
                # if acc_box_2 is starting this frame...
                if acc_box_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    acc_box_2.frameNStart = frameN  # exact frame index
                    acc_box_2.tStart = t  # local t and not account for scr refresh
                    acc_box_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(acc_box_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    acc_box_2.status = STARTED
                    acc_box_2.setAutoDraw(True)
                
                # if acc_box_2 is active this frame...
                if acc_box_2.status == STARTED:
                    # update params
                    pass
                
                # if acc_box_2 is stopping this frame...
                if acc_box_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > acc_box_2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        acc_box_2.tStop = t  # not accounting for scr refresh
                        acc_box_2.tStopRefresh = tThisFlipGlobal  # on global time
                        acc_box_2.frameNStop = frameN  # exact frame index
                        # update status
                        acc_box_2.status = FINISHED
                        acc_box_2.setAutoDraw(False)
                
                # *rej_box_2* updates
                
                # if rej_box_2 is starting this frame...
                if rej_box_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rej_box_2.frameNStart = frameN  # exact frame index
                    rej_box_2.tStart = t  # local t and not account for scr refresh
                    rej_box_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rej_box_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    rej_box_2.status = STARTED
                    rej_box_2.setAutoDraw(True)
                
                # if rej_box_2 is active this frame...
                if rej_box_2.status == STARTED:
                    # update params
                    pass
                
                # if rej_box_2 is stopping this frame...
                if rej_box_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rej_box_2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        rej_box_2.tStop = t  # not accounting for scr refresh
                        rej_box_2.tStopRefresh = tThisFlipGlobal  # on global time
                        rej_box_2.frameNStop = frameN  # exact frame index
                        # update status
                        rej_box_2.status = FINISHED
                        rej_box_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    offer_choice.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in offer_choice.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "offer_choice" ---
            for thisComponent in offer_choice.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for offer_choice
            offer_choice.tStop = globalClock.getTime(format='float')
            offer_choice.tStopRefresh = tThisFlipGlobal
            thisExp.addData('offer_choice.stopped', offer_choice.tStop)
            # Run 'End Routine' code from box_change
            thisExp.addData('trigger down', trigger_list)
            # Run 'End Routine' code from box_clear
            acc_box_2.lineColor = 'white'
            rej_box_2.lineColor = 'white'
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if offer_choice.maxDurationReached:
                routineTimer.addTime(-offer_choice.maxDuration)
            elif offer_choice.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            
            # --- Prepare to start Routine "offer_reveal" ---
            # create an object to store info about Routine offer_reveal
            offer_reveal = data.Routine(
                name='offer_reveal',
                components=[you_txt_3, partner_txt_3, dollar_Ytxt_3, dollar_Ptxt_3, you_image_3, partner_image_3],
            )
            offer_reveal.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code
            if resp == 0: #reject: no offer
                dollarY = "$ 0"
                dollarO = "$ 0"
                dollarImageY = 'cash\d0.png'
                dollarImageO = 'cash\d0.png'
            partner_txt_3.setText(avatar_final)
            dollar_Ytxt_3.setText(dollarY)
            dollar_Ptxt_3.setText(dollarO)
            you_image_3.setImage(dollarImageY)
            partner_image_3.setImage(dollarImageO)
            # store start times for offer_reveal
            offer_reveal.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            offer_reveal.tStart = globalClock.getTime(format='float')
            offer_reveal.status = STARTED
            thisExp.addData('offer_reveal.started', offer_reveal.tStart)
            offer_reveal.maxDuration = None
            # keep track of which components have finished
            offer_revealComponents = offer_reveal.components
            for thisComponent in offer_reveal.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "offer_reveal" ---
            # if trial has changed, end Routine now
            if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                continueRoutine = False
            offer_reveal.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code
                keys = kb.getKeys(['t'])
                if 't' in keys:
                    time = core.getTime()
                    trigger_list.append(time)
                
                # *you_txt_3* updates
                
                # if you_txt_3 is starting this frame...
                if you_txt_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    you_txt_3.frameNStart = frameN  # exact frame index
                    you_txt_3.tStart = t  # local t and not account for scr refresh
                    you_txt_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(you_txt_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    you_txt_3.status = STARTED
                    you_txt_3.setAutoDraw(True)
                
                # if you_txt_3 is active this frame...
                if you_txt_3.status == STARTED:
                    # update params
                    pass
                
                # if you_txt_3 is stopping this frame...
                if you_txt_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > you_txt_3.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        you_txt_3.tStop = t  # not accounting for scr refresh
                        you_txt_3.tStopRefresh = tThisFlipGlobal  # on global time
                        you_txt_3.frameNStop = frameN  # exact frame index
                        # update status
                        you_txt_3.status = FINISHED
                        you_txt_3.setAutoDraw(False)
                
                # *partner_txt_3* updates
                
                # if partner_txt_3 is starting this frame...
                if partner_txt_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    partner_txt_3.frameNStart = frameN  # exact frame index
                    partner_txt_3.tStart = t  # local t and not account for scr refresh
                    partner_txt_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(partner_txt_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    partner_txt_3.status = STARTED
                    partner_txt_3.setAutoDraw(True)
                
                # if partner_txt_3 is active this frame...
                if partner_txt_3.status == STARTED:
                    # update params
                    pass
                
                # if partner_txt_3 is stopping this frame...
                if partner_txt_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > partner_txt_3.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        partner_txt_3.tStop = t  # not accounting for scr refresh
                        partner_txt_3.tStopRefresh = tThisFlipGlobal  # on global time
                        partner_txt_3.frameNStop = frameN  # exact frame index
                        # update status
                        partner_txt_3.status = FINISHED
                        partner_txt_3.setAutoDraw(False)
                
                # *dollar_Ytxt_3* updates
                
                # if dollar_Ytxt_3 is starting this frame...
                if dollar_Ytxt_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    dollar_Ytxt_3.frameNStart = frameN  # exact frame index
                    dollar_Ytxt_3.tStart = t  # local t and not account for scr refresh
                    dollar_Ytxt_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dollar_Ytxt_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    dollar_Ytxt_3.status = STARTED
                    dollar_Ytxt_3.setAutoDraw(True)
                
                # if dollar_Ytxt_3 is active this frame...
                if dollar_Ytxt_3.status == STARTED:
                    # update params
                    pass
                
                # if dollar_Ytxt_3 is stopping this frame...
                if dollar_Ytxt_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dollar_Ytxt_3.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        dollar_Ytxt_3.tStop = t  # not accounting for scr refresh
                        dollar_Ytxt_3.tStopRefresh = tThisFlipGlobal  # on global time
                        dollar_Ytxt_3.frameNStop = frameN  # exact frame index
                        # update status
                        dollar_Ytxt_3.status = FINISHED
                        dollar_Ytxt_3.setAutoDraw(False)
                
                # *dollar_Ptxt_3* updates
                
                # if dollar_Ptxt_3 is starting this frame...
                if dollar_Ptxt_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    dollar_Ptxt_3.frameNStart = frameN  # exact frame index
                    dollar_Ptxt_3.tStart = t  # local t and not account for scr refresh
                    dollar_Ptxt_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dollar_Ptxt_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    dollar_Ptxt_3.status = STARTED
                    dollar_Ptxt_3.setAutoDraw(True)
                
                # if dollar_Ptxt_3 is active this frame...
                if dollar_Ptxt_3.status == STARTED:
                    # update params
                    pass
                
                # if dollar_Ptxt_3 is stopping this frame...
                if dollar_Ptxt_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dollar_Ptxt_3.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        dollar_Ptxt_3.tStop = t  # not accounting for scr refresh
                        dollar_Ptxt_3.tStopRefresh = tThisFlipGlobal  # on global time
                        dollar_Ptxt_3.frameNStop = frameN  # exact frame index
                        # update status
                        dollar_Ptxt_3.status = FINISHED
                        dollar_Ptxt_3.setAutoDraw(False)
                
                # *you_image_3* updates
                
                # if you_image_3 is starting this frame...
                if you_image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    you_image_3.frameNStart = frameN  # exact frame index
                    you_image_3.tStart = t  # local t and not account for scr refresh
                    you_image_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(you_image_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    you_image_3.status = STARTED
                    you_image_3.setAutoDraw(True)
                
                # if you_image_3 is active this frame...
                if you_image_3.status == STARTED:
                    # update params
                    pass
                
                # if you_image_3 is stopping this frame...
                if you_image_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > you_image_3.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        you_image_3.tStop = t  # not accounting for scr refresh
                        you_image_3.tStopRefresh = tThisFlipGlobal  # on global time
                        you_image_3.frameNStop = frameN  # exact frame index
                        # update status
                        you_image_3.status = FINISHED
                        you_image_3.setAutoDraw(False)
                
                # *partner_image_3* updates
                
                # if partner_image_3 is starting this frame...
                if partner_image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    partner_image_3.frameNStart = frameN  # exact frame index
                    partner_image_3.tStart = t  # local t and not account for scr refresh
                    partner_image_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(partner_image_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    partner_image_3.status = STARTED
                    partner_image_3.setAutoDraw(True)
                
                # if partner_image_3 is active this frame...
                if partner_image_3.status == STARTED:
                    # update params
                    pass
                
                # if partner_image_3 is stopping this frame...
                if partner_image_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > partner_image_3.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        partner_image_3.tStop = t  # not accounting for scr refresh
                        partner_image_3.tStopRefresh = tThisFlipGlobal  # on global time
                        partner_image_3.frameNStop = frameN  # exact frame index
                        # update status
                        partner_image_3.status = FINISHED
                        partner_image_3.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    offer_reveal.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in offer_reveal.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "offer_reveal" ---
            for thisComponent in offer_reveal.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for offer_reveal
            offer_reveal.tStop = globalClock.getTime(format='float')
            offer_reveal.tStopRefresh = tThisFlipGlobal
            thisExp.addData('offer_reveal.stopped', offer_reveal.tStop)
            # Run 'End Routine' code from code
            thisExp.addData('trigger down', trigger_list)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if offer_reveal.maxDurationReached:
                routineTimer.addTime(-offer_reveal.maxDuration)
            elif offer_reveal.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            
            # --- Prepare to start Routine "mood" ---
            # create an object to store info about Routine mood
            mood = data.Routine(
                name='mood',
                components=[slider_2, surveyQ1_txt_2, ins_txt_2, slider_choose, good_img, bad_img, ok_img, slider_move],
            )
            mood.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            slider_2.reset()
            # create starting attributes for slider_choose
            slider_choose.keys = []
            slider_choose.rt = []
            _slider_choose_allKeys = []
            # Run 'Begin Routine' code from mood_code
            if mood[offerIndex] == 0:
                continueRoutine = False
            
            event.clearEvents('keyboard')
            slider_2.markerPos = 50
            # create starting attributes for slider_move
            slider_move.keys = []
            slider_move.rt = []
            _slider_move_allKeys = []
            # store start times for mood
            mood.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            mood.tStart = globalClock.getTime(format='float')
            mood.status = STARTED
            thisExp.addData('mood.started', mood.tStart)
            mood.maxDuration = None
            # keep track of which components have finished
            moodComponents = mood.components
            for thisComponent in mood.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mood" ---
            # if trial has changed, end Routine now
            if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                continueRoutine = False
            mood.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *slider_2* updates
                
                # if slider_2 is starting this frame...
                if slider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    slider_2.frameNStart = frameN  # exact frame index
                    slider_2.tStart = t  # local t and not account for scr refresh
                    slider_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    slider_2.status = STARTED
                    slider_2.setAutoDraw(True)
                
                # if slider_2 is active this frame...
                if slider_2.status == STARTED:
                    # update params
                    pass
                
                # *surveyQ1_txt_2* updates
                
                # if surveyQ1_txt_2 is starting this frame...
                if surveyQ1_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    surveyQ1_txt_2.frameNStart = frameN  # exact frame index
                    surveyQ1_txt_2.tStart = t  # local t and not account for scr refresh
                    surveyQ1_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(surveyQ1_txt_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    surveyQ1_txt_2.status = STARTED
                    surveyQ1_txt_2.setAutoDraw(True)
                
                # if surveyQ1_txt_2 is active this frame...
                if surveyQ1_txt_2.status == STARTED:
                    # update params
                    pass
                
                # *ins_txt_2* updates
                
                # if ins_txt_2 is starting this frame...
                if ins_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ins_txt_2.frameNStart = frameN  # exact frame index
                    ins_txt_2.tStart = t  # local t and not account for scr refresh
                    ins_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ins_txt_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ins_txt_2.status = STARTED
                    ins_txt_2.setAutoDraw(True)
                
                # if ins_txt_2 is active this frame...
                if ins_txt_2.status == STARTED:
                    # update params
                    pass
                
                # *slider_choose* updates
                waitOnFlip = False
                
                # if slider_choose is starting this frame...
                if slider_choose.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    slider_choose.frameNStart = frameN  # exact frame index
                    slider_choose.tStart = t  # local t and not account for scr refresh
                    slider_choose.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(slider_choose, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'slider_choose.started')
                    # update status
                    slider_choose.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(slider_choose.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(slider_choose.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if slider_choose.status == STARTED and not waitOnFlip:
                    theseKeys = slider_choose.getKeys(keyList=['space','4'], ignoreKeys=["escape"], waitRelease=False)
                    _slider_choose_allKeys.extend(theseKeys)
                    if len(_slider_choose_allKeys):
                        slider_choose.keys = _slider_choose_allKeys[-1].name  # just the last key pressed
                        slider_choose.rt = _slider_choose_allKeys[-1].rt
                        slider_choose.duration = _slider_choose_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                # Run 'Each Frame' code from mood_code
                keys = kb.getKeys(['t'])
                if 't' in keys:
                    time = core.getTime()
                    trigger_list.append(time)
                
                #keys = slider_move.getKeys(['left','3','right','1'], waitRelease=False,clear=False)
                #
                #for key in keys:
                #    if key == 'left' and slider_2.markerPos > 0:
                #        slider_2.markerPos -= 0.5
                ##    else:
                ##        continueRoutine=True 
                
                keys = event.getKeys()
                if len(keys):
                    if 'left' in keys:
                        slider_2.markerPos = slider_2.markerPos - 5
                    elif '3' in keys:
                        slider_2.markerPos = slider_2.markerPos - 5
                    elif 'right' in keys:
                        slider_2.markerPos = slider_2.markerPos + 5 
                    elif '1' in keys:
                        slider_2.markerPos = slider_2.markerPos + 5
                
                # *good_img* updates
                
                # if good_img is starting this frame...
                if good_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    good_img.frameNStart = frameN  # exact frame index
                    good_img.tStart = t  # local t and not account for scr refresh
                    good_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(good_img, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    good_img.status = STARTED
                    good_img.setAutoDraw(True)
                
                # if good_img is active this frame...
                if good_img.status == STARTED:
                    # update params
                    pass
                
                # *bad_img* updates
                
                # if bad_img is starting this frame...
                if bad_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    bad_img.frameNStart = frameN  # exact frame index
                    bad_img.tStart = t  # local t and not account for scr refresh
                    bad_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(bad_img, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    bad_img.status = STARTED
                    bad_img.setAutoDraw(True)
                
                # if bad_img is active this frame...
                if bad_img.status == STARTED:
                    # update params
                    pass
                
                # *ok_img* updates
                
                # if ok_img is starting this frame...
                if ok_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ok_img.frameNStart = frameN  # exact frame index
                    ok_img.tStart = t  # local t and not account for scr refresh
                    ok_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ok_img, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ok_img.status = STARTED
                    ok_img.setAutoDraw(True)
                
                # if ok_img is active this frame...
                if ok_img.status == STARTED:
                    # update params
                    pass
                
                # *slider_move* updates
                waitOnFlip = False
                
                # if slider_move is starting this frame...
                if slider_move.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    slider_move.frameNStart = frameN  # exact frame index
                    slider_move.tStart = t  # local t and not account for scr refresh
                    slider_move.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(slider_move, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    slider_move.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(slider_move.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(slider_move.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if slider_move.status == STARTED and not waitOnFlip:
                    theseKeys = slider_move.getKeys(keyList=['left','right','3','1'], ignoreKeys=["escape"], waitRelease=False)
                    _slider_move_allKeys.extend(theseKeys)
                    if len(_slider_move_allKeys):
                        slider_move.keys = _slider_move_allKeys[-1].name  # just the last key pressed
                        slider_move.rt = _slider_move_allKeys[-1].rt
                        slider_move.duration = _slider_move_allKeys[-1].duration
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    mood.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mood.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mood" ---
            for thisComponent in mood.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for mood
            mood.tStop = globalClock.getTime(format='float')
            mood.tStopRefresh = tThisFlipGlobal
            thisExp.addData('mood.stopped', mood.tStop)
            # check responses
            if slider_choose.keys in ['', [], None]:  # No response was made
                slider_choose.keys = None
            trials.addData('slider_choose.keys',slider_choose.keys)
            if slider_choose.keys != None:  # we had a response
                trials.addData('slider_choose.rt', slider_choose.rt)
                trials.addData('slider_choose.duration', slider_choose.duration)
            # Run 'End Routine' code from mood_code
            thisExp.addData('trigger down', trigger_list)
            if mood[offerIndex] == 1:
                thisExp.addData('rating', slider_2.markerPos)
            # the Routine "mood" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "fixation" ---
            # create an object to store info about Routine fixation
            fixation = data.Routine(
                name='fixation',
                components=[fix_txt],
            )
            fixation.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            fix_txt.setText('+')
            # store start times for fixation
            fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            fixation.tStart = globalClock.getTime(format='float')
            fixation.status = STARTED
            thisExp.addData('fixation.started', fixation.tStart)
            fixation.maxDuration = None
            # keep track of which components have finished
            fixationComponents = fixation.components
            for thisComponent in fixation.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "fixation" ---
            # if trial has changed, end Routine now
            if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                continueRoutine = False
            fixation.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code_12
                keys = kb.getKeys(['t'])
                if 't' in keys:
                    time = core.getTime()
                    trigger_list.append(time)
                
                # *fix_txt* updates
                
                # if fix_txt is starting this frame...
                if fix_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fix_txt.frameNStart = frameN  # exact frame index
                    fix_txt.tStart = t  # local t and not account for scr refresh
                    fix_txt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fix_txt, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix_txt.started')
                    # update status
                    fix_txt.status = STARTED
                    fix_txt.setAutoDraw(True)
                
                # if fix_txt is active this frame...
                if fix_txt.status == STARTED:
                    # update params
                    pass
                
                # if fix_txt is stopping this frame...
                if fix_txt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fix_txt.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fix_txt.tStop = t  # not accounting for scr refresh
                        fix_txt.tStopRefresh = tThisFlipGlobal  # on global time
                        fix_txt.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fix_txt.stopped')
                        # update status
                        fix_txt.status = FINISHED
                        fix_txt.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    fixation.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fixation.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fixation" ---
            for thisComponent in fixation.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for fixation
            fixation.tStop = globalClock.getTime(format='float')
            fixation.tStopRefresh = tThisFlipGlobal
            thisExp.addData('fixation.stopped', fixation.tStop)
            # Run 'End Routine' code from code_12
            thisExp.addData('trigger down', trigger_list)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if fixation.maxDurationReached:
                routineTimer.addTime(-fixation.maxDuration)
            elif fixation.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'team_block'
    
    
    # --- Prepare to start Routine "end" ---
    # create an object to store info about Routine end
    end = data.Routine(
        name='end',
        components=[text_9, expEnd_key],
    )
    end.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for expEnd_key
    expEnd_key.keys = []
    expEnd_key.rt = []
    _expEnd_key_allKeys = []
    # store start times for end
    end.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    end.tStart = globalClock.getTime(format='float')
    end.status = STARTED
    thisExp.addData('end.started', end.tStart)
    end.maxDuration = None
    # keep track of which components have finished
    endComponents = end.components
    for thisComponent in end.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end" ---
    end.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_9* updates
        
        # if text_9 is starting this frame...
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_9.status = STARTED
            text_9.setAutoDraw(True)
        
        # if text_9 is active this frame...
        if text_9.status == STARTED:
            # update params
            pass
        
        # *expEnd_key* updates
        waitOnFlip = False
        
        # if expEnd_key is starting this frame...
        if expEnd_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            expEnd_key.frameNStart = frameN  # exact frame index
            expEnd_key.tStart = t  # local t and not account for scr refresh
            expEnd_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(expEnd_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'expEnd_key.started')
            # update status
            expEnd_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(expEnd_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(expEnd_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if expEnd_key.status == STARTED and not waitOnFlip:
            theseKeys = expEnd_key.getKeys(keyList=['escape'], ignoreKeys=["escape"], waitRelease=False)
            _expEnd_key_allKeys.extend(theseKeys)
            if len(_expEnd_key_allKeys):
                expEnd_key.keys = _expEnd_key_allKeys[-1].name  # just the last key pressed
                expEnd_key.rt = _expEnd_key_allKeys[-1].rt
                expEnd_key.duration = _expEnd_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            end.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in end.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for end
    end.tStop = globalClock.getTime(format='float')
    end.tStopRefresh = tThisFlipGlobal
    thisExp.addData('end.stopped', end.tStop)
    # check responses
    if expEnd_key.keys in ['', [], None]:  # No response was made
        expEnd_key.keys = None
    thisExp.addData('expEnd_key.keys',expEnd_key.keys)
    if expEnd_key.keys != None:  # we had a response
        thisExp.addData('expEnd_key.rt', expEnd_key.rt)
        thisExp.addData('expEnd_key.duration', expEnd_key.duration)
    thisExp.nextEntry()
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
