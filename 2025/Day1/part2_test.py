import pytest
from part2 import rotate_dial


class TestRotateDial:
    # Starting from zero
    def test_from_zero_no_wrapping(self):
        assert rotate_dial(0, 25) == (25, 0)
    
    def test_from_zero_single_wrap_forward(self):
        assert rotate_dial(0, 150) == (50, 1)
    
    def test_from_zero_multiple_wraps_forward(self):
        assert rotate_dial(0, 350) == (50, 3)
    
    def test_from_zero_single_wrap_backward(self):
        assert rotate_dial(0, -50) == (50, 0)
    
    def test_from_zero_multiple_wraps_backward(self):
        assert rotate_dial(0, -250) == (50, 2)
    
    def test_from_zero_exact_100(self):
        assert rotate_dial(0, 100) == (0, 1)
    
    # Starting from non-zero
    def test_from_nonzero_no_wrapping_forward(self):
        assert rotate_dial(25, 30) == (55, 0)
    
    def test_from_nonzero_no_wrapping_backward(self):
        assert rotate_dial(50, -25) == (25, 0)
    
    def test_from_nonzero_single_wrap_forward(self):
        assert rotate_dial(75, 50) == (25, 1)
    
    def test_from_nonzero_single_wrap_backward(self):
        assert rotate_dial(25, -50) == (75, 1)
    
    def test_from_nonzero_multiple_wraps_forward(self):
        assert rotate_dial(50, 250) == (0, 3)
    
    def test_from_nonzero_multiple_wraps_backward(self):
        assert rotate_dial(50, -350) == (0, 4)
    
    def test_from_nonzero_to_exact_zero(self):
        assert rotate_dial(50, 50) == (0, 1)
    
    def test_from_nonzero_wrap_to_exact_zero(self):
        assert rotate_dial(50, 150) == (0, 2)

    def test_from_nonzero_to_exact_zero_backward(self):
        assert rotate_dial(50, -50) == (0, 1)

    def test_from_nonzero_wrap_to_exact_zero_backward(self):
        assert rotate_dial(50, -150) == (0, 2)