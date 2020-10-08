# encoding: utf-8
# module Scripts._asyncio
# from C:\Users\User\PycharmProjects\venv\Scripts\_asyncio.pyd
# by generator 1.145
""" Accelerator module for asyncio """

# imports
from _asyncio import Future, Task


# functions

def get_event_loop(): # real signature unknown; restored from __doc__
    """
    Return an asyncio event loop.
    
    When called from a coroutine or a callback (e.g. scheduled with
    call_soon or similar API), this function will always return the
    running event loop.
    
    If there is no running event loop set, the function will return
    the result of `get_event_loop_policy().get_event_loop()` call.
    """
    pass

def get_running_loop(*args, **kwargs): # real signature unknown
    """
    Return the running event loop.  Raise a RuntimeError if there is none.
    
    This function is thread-specific.
    """
    pass

def _enter_task(*args, **kwargs): # real signature unknown
    """
    Enter into task execution or resume suspended task.
    
    Task belongs to loop.
    
    Returns None.
    """
    pass

def _get_running_loop(*args, **kwargs): # real signature unknown
    """
    Return the running event loop or None.
    
    This is a low-level function intended to be used by event loops.
    This function is thread-specific.
    """
    pass

def _leave_task(*args, **kwargs): # real signature unknown
    """
    Leave task execution or suspend a task.
    
    Task belongs to loop.
    
    Returns None.
    """
    pass

def _register_task(*args, **kwargs): # real signature unknown
    """
    Register a new task in asyncio as executed by loop.
    
    Returns None.
    """
    pass

def _set_running_loop(*args, **kwargs): # real signature unknown
    """
    Set the running event loop.
    
    This is a low-level function intended to be used by event loops.
    This function is thread-specific.
    """
    pass

def _unregister_task(*args, **kwargs): # real signature unknown
    """
    Unregister a task.
    
    Returns None.
    """
    pass

# no classes
# variables with complex values

_all_tasks = None # (!) real value is ''

_current_tasks = {}

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

