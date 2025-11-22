"""Unit tests for NavigationController."""
import pytest
from unittest.mock import Mock, MagicMock
from PySide6.QtWidgets import QStackedWidget, QWidget

from app.controllers.navigation_controller import NavigationController

@pytest.fixture
def mock_stacked_widget():
    widget = Mock(spec=QStackedWidget)
    widget.count.return_value = 3
    widget.currentIndex.return_value = 0
    return widget

@pytest.fixture
def controller(mock_stacked_widget):
    return NavigationController(mock_stacked_widget)

class TestNavigationController:
    """Test suite for NavigationController."""
    
    def test_next_screen(self, controller, mock_stacked_widget):
        """Test navigating to the next screen."""
        controller.next_screen()
        mock_stacked_widget.setCurrentIndex.assert_called_with(1)
        
    def test_next_screen_at_end(self, controller, mock_stacked_widget):
        """Test next_screen does nothing if at last screen."""
        mock_stacked_widget.currentIndex.return_value = 2
        controller.next_screen()
        # Should not call setCurrentIndex with 3 (out of bounds)
        # Logic: index + 1 < count
        # 2 + 1 < 3 is False.
        mock_stacked_widget.setCurrentIndex.assert_not_called()
        
    def test_previous_screen(self, controller, mock_stacked_widget):
        """Test navigating to the previous screen."""
        mock_stacked_widget.currentIndex.return_value = 1
        controller.previous_screen()
        mock_stacked_widget.setCurrentIndex.assert_called_with(0)
        
    def test_previous_screen_at_start(self, controller, mock_stacked_widget):
        """Test previous_screen does nothing if at first screen."""
        mock_stacked_widget.currentIndex.return_value = 0
        controller.previous_screen()
        mock_stacked_widget.setCurrentIndex.assert_not_called()
        
    def test_go_to_screen(self, controller, mock_stacked_widget):
        """Test navigating to a specific screen widget."""
        widget = Mock(spec=QWidget)
        mock_stacked_widget.indexOf.return_value = 2
        
        controller.go_to_screen(widget)
        
        mock_stacked_widget.setCurrentIndex.assert_called_with(2)
        
    def test_callbacks(self, controller, mock_stacked_widget):
        """Test before and after navigation callbacks."""
        before_cb = Mock()
        after_cb = Mock()
        
        # Register for current index (0) and next index (1)
        controller.register_before_navigation(0, before_cb)
        controller.register_after_navigation(1, after_cb)
        
        controller.next_screen()
        
        before_cb.assert_called_once()
        after_cb.assert_called_once()
