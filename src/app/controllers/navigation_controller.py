from typing import Callable, Dict, Optional
from PySide6.QtWidgets import QStackedWidget, QWidget

class NavigationController:
    """Controller responsible for screen navigation logic."""
    
    def __init__(self, stacked_widget: QStackedWidget):
        self.stacked_widget = stacked_widget
        self._before_nav_callbacks: Dict[int, Callable] = {}
        self._after_nav_callbacks: Dict[int, Callable] = {}
    
    def register_before_navigation(self, screen_index: int, callback: Callable):
        """Register a callback to be executed before leaving a screen."""
        self._before_nav_callbacks[screen_index] = callback
        
    def register_after_navigation(self, screen_index: int, callback: Callable):
        """Register a callback to be executed after entering a screen."""
        self._after_nav_callbacks[screen_index] = callback
    
    def next_screen(self):
        """Move to the next screen."""
        current_index = self.stacked_widget.currentIndex()
        
        # Execute before-nav callback
        if current_index in self._before_nav_callbacks:
            self._before_nav_callbacks[current_index]()
            
        if current_index < self.stacked_widget.count() - 1:
            next_index = current_index + 1
            
            # Execute after-nav callback (preparation)
            if next_index in self._after_nav_callbacks:
                self._after_nav_callbacks[next_index]()
                
            self.stacked_widget.setCurrentIndex(next_index)
            
    def previous_screen(self):
        """Move to the previous screen."""
        current_index = self.stacked_widget.currentIndex()
        
        # Execute before-nav callback
        if current_index in self._before_nav_callbacks:
            self._before_nav_callbacks[current_index]()
            
        if current_index > 0:
            prev_index = current_index - 1
            
            # Execute after-nav callback (preparation)
            if prev_index in self._after_nav_callbacks:
                self._after_nav_callbacks[prev_index]()
                
            self.stacked_widget.setCurrentIndex(prev_index)
            
    def go_to_screen(self, widget: QWidget):
        """Move to a specific screen widget."""
        current_index = self.stacked_widget.currentIndex()
        target_index = self.stacked_widget.indexOf(widget)
        
        if target_index == -1 or target_index == current_index:
            return
            
        # Execute before-nav callback
        if current_index in self._before_nav_callbacks:
            self._before_nav_callbacks[current_index]()
            
        # Execute after-nav callback (preparation)
        if target_index in self._after_nav_callbacks:
            self._after_nav_callbacks[target_index]()
            
        self.stacked_widget.setCurrentIndex(target_index)
