from dice_roller.nodes import *

class Interpreter:
    def evaluate(self, node):
        method_name = f'evaluate_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)
    
    def evaluate_DieNode(self, node):
        return node.value
    
    def evaluate_NumberNode(self, node):
        return node.value
    
    def evaluate_AddNode(self, node):
        return self.evaluate(node.node_a) + self.evaluate(node.node_b)
    
    def evaluate_SubtractNode(self, node):
        return self.evaluate(node.node_a) - self.evaluate(node.node_b)
    
    def evaluate_MultiplyNode(self, node):
        return self.evaluate(node.node_a) * self.evaluate(node.node_b)
    
    def evaluate_DivideNode(self, node):
        try:
            return self.evaluate(node.node_a) / self.evaluate(node.node_b)
        except:
            raise Exception('Runtime math error')
        
    def evaluate_PlusNode(self, node):
        return self.evaluate(node.node)
    
    def evaluate_MinusNode(self, node):
        return -self.evaluate(node.node)