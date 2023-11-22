from math import sqrt


class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        '''
        This method checks if the triangle is valid.
        
        Args: 
            No
        Returns:
            bool: True if the triangle is valid, False otherwise
        '''
        if 
        
    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.

        Note: typies are 'Teng yonli', 'Teng tomonli', 'Turli tomonli'
        '''
        a,b,c =(self.a,self.b,self.c)
        if a == b and b == c: 
            return 'Teng yonli'  
        elif a == b or b == c or a == c: 
            return 'Teng tomonli' 
        else:  
             return 'Turli tomonli'
        
    def perimeter(self) -> float:
        '''
        This method finds the perimeter of the triangle.
        Args:
            No
        Returns:
            float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        return self.a +self.b+self.c

    def area(self) -> float:
        '''
        This method finds the area of the triangle.
        Args:
            NO
        Returns:
            float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        a,b,c =(self.a,self.b,self.c)
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 
        return area 
