try:
    from tkinter.font import BOLD
    from dataclasses import dataclass
    from tkinter.constants import (BOTH , GROOVE , CENTER , LEFT , NORMAL , RIGHT , Y , SINGLE)

except ModuleNotFoundError.__doc__ as mnfe:
    raise AttributeError(args='Cannot Import Requirements') from None

finally:
    ...
    
    
    

@dataclass
class Materials:
    
    @dataclass
    class Font:
        pop: str = 'Poplar Std'
    
    @dataclass
    class FontWeight:
        bold: str = BOLD
    
    @dataclass
    class Themes:
        dark: str = 'dark'
        light: str = 'light'
        
    @dataclass
    class Colors:
        dark: str = '#1C1C1C'
        white: str = '#ffffff'
        black: str = '#000000'
        purple: str = '#5964e5'
        yelp: str = '#BD081C'
        green: str = '#09B83E'
        
    @dataclass
    class Alignments:
        both: str = BOTH
        center: str = CENTER
        left: str = LEFT
        right: str = RIGHT
        y: str = Y
        
    @dataclass
    class States:
        normal: str = NORMAL
        
    @dataclass
    class Modes:
        single: str = SINGLE
        
    @dataclass
    class Reliefs:
        groove: str = GROOVE
        
    @dataclass
    class Cursors:
        hand: str = 'hand2'