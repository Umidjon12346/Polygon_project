class Rectangle:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b

    def is_valid(self) -> bool:
        """
        This method checks if the rectangle is valid
        
        Args:
            No
        Returns: 
            bool: True if the rectangle is valid, False otherwise
        """ 
        return True if self.a>0 and self.b>0 else False

    def perimeter(self) -> float:
        """
        This method finds the perimeter of the rectangle.
        Args:
            No
        Returns:
            float or int: return perimeter of the rectangle if the rectangle is valid, 0 otherwise
        """
        if self.a.is_valid() and self.b.is_valid():
            return 2*(self.a + self.b)
        else :
            return 0

    def area(self) -> float:
        """
        This method finds the area of the rectangle.
        Args:
            No
        Returns:
            float or int:  return area of the rectangle if the rectangle is valid, 0 otherwise 
        """
        if self.a.is_valid() and self.b.is_valid():
            return self.a*self.b
        else :
            return 0

