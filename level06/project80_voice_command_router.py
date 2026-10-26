"""Project 80: Allowlisted command router. Never executes arbitrary commands."""
import re

def route_command(transcript):
    text=re.sub(r'\s+',' ',transcript.strip().casefold())
    if not text: return {'intent':'empty','response':'I did not hear a command.'}
    if text in {'help','what can you do','show commands'}: return {'intent':'help','response':'Supported commands: help, time, open notes, stop.'}
    if text in {'stop','exit','quit','cancel'}: return {'intent':'stop','response':'Stopping the assistant.'}
    if text in {'time','what time is it'}: return {'intent':'time','response':'Time lookup is not configured in this offline demo.'}
    if text in {'open notes','show notes'}: return {'intent':'open_notes','response':'Notes action requested; no file is opened by this demo.'}
    return {'intent':'unknown','response':"Command not recognized. Say 'help'."}
