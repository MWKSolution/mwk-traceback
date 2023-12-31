## Custom exception traceback  

---

```text


NAME
    custom_exception_traceback
PACKAGE CONTENTS
    custom_exc_tb
    custom_warn
CLASSES
    builtins.object
        custom_exception_traceback.custom_exc_tb.CustomTraceback
            SuperCompactTraceback
        custom_exception_traceback.custom_warn.CustomWarningFormatter
            SuperCompactWarningFormatter
    
    class CustomTraceback(builtins.object)
     |  CustomTraceback(exc: BaseException, *, chain: bool = True, reverse: bool = False) -> str
     |  
     |  Helper class for exceptions traceback handling. Doesn't create any instances of itself!!!
     |  
     |  General info:
     |  It goes down exceptions chain and gets traceback for each exception than format string with that.
     |  
     |  Usage:
     |  CustomTraceback(exc) -> get exception formatted string
     |  CustomTraceback.print_exception(exc) -> print formatted exception
     |  CustomTraceback.exception_hook -> to be used with sys.excepthook
     |  
     |  Class methods defined here:
     |  
     |  exception_hook(exc_type: type, exc_value: BaseException, trace_back: traceback) -> None from builtins.type
     |      Method to be used as system exception hook: 'sys.excepthook = CustomTraceback.exception_hook'
     |      :param exc_type: sys.excepthook signature
     |      :param exc_value: sys.excepthook signature
     |      :param trace_back: sys.excepthook signature
     |      :return: None
     |  
     |  print_exception(exc: BaseException, *, chain: bool = True, reverse: False = False, file: <class 'TextIO'> = <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>) -> None from builtins.type
     |      Just print formatted exception to the given io object (stdout, stderr, ...)
     |      :param exc: exception
     |      :param chain: chain exceptions or not
     |      :param reverse: reverse order of exceptions
     |      :param file: io object file
     |      :return: None
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(cls, exc: BaseException, *, chain: bool = True, reverse: bool = False) -> str
     |      Doesn't create instances. Returns formatted exception string.
     |      :param exc: exception
     |      :param chain: chain exceptions or not
     |      :param reverse: reverse order of exceptions
     |      :return: formatted exception string
    
    class CustomWarningFormatter(builtins.object)
     |  CustomWarningFormatter(message, category, filename, lineno, line=None)
     |  
     |  Static methods defined here:
     |  
     |  __new__(cls, message, category, filename, lineno, line=None)
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    compact_tb = class CustomTraceback(builtins.object)
     |  compact_tb(exc: BaseException, *, chain: bool = True, reverse: bool = False) -> str
     |  
     |  Helper class for exceptions traceback handling. Doesn't create any instances of itself!!!
     |  
     |  General info:
     |  It goes down exceptions chain and gets traceback for each exception than format string with that.
     |  
     |  Usage:
     |  CustomTraceback(exc) -> get exception formatted string
     |  CustomTraceback.print_exception(exc) -> print formatted exception
     |  CustomTraceback.exception_hook -> to be used with sys.excepthook
     |  
     |  Class methods defined here:
     |  
     |  exception_hook(exc_type: type, exc_value: BaseException, trace_back: traceback) -> None from builtins.type
     |      Method to be used as system exception hook: 'sys.excepthook = CustomTraceback.exception_hook'
     |      :param exc_type: sys.excepthook signature
     |      :param exc_value: sys.excepthook signature
     |      :param trace_back: sys.excepthook signature
     |      :return: None
     |  
     |  print_exception(exc: BaseException, *, chain: bool = True, reverse: False = False, file: <class 'TextIO'> = <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>) -> None from builtins.type
     |      Just print formatted exception to the given io object (stdout, stderr, ...)
     |      :param exc: exception
     |      :param chain: chain exceptions or not
     |      :param reverse: reverse order of exceptions
     |      :param file: io object file
     |      :return: None
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(cls, exc: BaseException, *, chain: bool = True, reverse: bool = False) -> str
     |      Doesn't create instances. Returns formatted exception string.
     |      :param exc: exception
     |      :param chain: chain exceptions or not
     |      :param reverse: reverse order of exceptions
     |      :return: formatted exception string
    
    compact_warn = class CustomWarningFormatter(builtins.object)
     |  compact_warn(message, category, filename, lineno, line=None)
     |  
     |  Static methods defined here:
     |  
     |  __new__(cls, message, category, filename, lineno, line=None)
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    super_compact_tb = class SuperCompactTraceback(custom_exception_traceback.custom_exc_tb.CustomTraceback)
     |  super_compact_tb(exc: BaseException, *, chain: bool = True, reverse: bool = False) -> str
     |  
     |  Helper class for exceptions traceback handling. Doesn't create any instances of itself!!!
     |  
     |  General info:
     |  It goes down exceptions chain and gets traceback for each exception than format string with that.
     |  
     |  Usage:
     |  CustomTraceback(exc) -> get exception formatted string
     |  CustomTraceback.print_exception(exc) -> print formatted exception
     |  CustomTraceback.exception_hook -> to be used with sys.excepthook
     |  
     |  Method resolution order:
     |      SuperCompactTraceback
     |      custom_exception_traceback.custom_exc_tb.CustomTraceback
     |      builtins.object
     |  
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from custom_exception_traceback.custom_exc_tb.CustomTraceback:
     |  
     |  exception_hook(exc_type: type, exc_value: BaseException, trace_back: traceback) -> None from builtins.type
     |      Method to be used as system exception hook: 'sys.excepthook = CustomTraceback.exception_hook'
     |      :param exc_type: sys.excepthook signature
     |      :param exc_value: sys.excepthook signature
     |      :param trace_back: sys.excepthook signature
     |      :return: None
     |  
     |  print_exception(exc: BaseException, *, chain: bool = True, reverse: False = False, file: <class 'TextIO'> = <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>) -> None from builtins.type
     |      Just print formatted exception to the given io object (stdout, stderr, ...)
     |      :param exc: exception
     |      :param chain: chain exceptions or not
     |      :param reverse: reverse order of exceptions
     |      :param file: io object file
     |      :return: None
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from custom_exception_traceback.custom_exc_tb.CustomTraceback:
     |  
     |  __new__(cls, exc: BaseException, *, chain: bool = True, reverse: bool = False) -> str
     |      Doesn't create instances. Returns formatted exception string.
     |      :param exc: exception
     |      :param chain: chain exceptions or not
     |      :param reverse: reverse order of exceptions
     |      :return: formatted exception string
    
    super_compact_warn = class SuperCompactWarningFormatter(custom_exception_traceback.custom_warn.CustomWarningFormatter)
     |  super_compact_warn(message, category, filename, lineno, line=None)
     |  
     |  Method resolution order:
     |      SuperCompactWarningFormatter
     |      custom_exception_traceback.custom_warn.CustomWarningFormatter
     |      builtins.object
     |  
     |  Static methods inherited from custom_exception_traceback.custom_warn.CustomWarningFormatter:
     |  
     |  __new__(cls, message, category, filename, lineno, line=None)
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from custom_exception_traceback.custom_warn.CustomWarningFormatter:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
DATA
    __all__ = ('compact_tb', 'super_compact_tb', 'compact_warn', 'super_co...
FILE
    c:\home\python\projects\custom_exception_traceback\src\custom_exception_traceback\__init__.py

```
