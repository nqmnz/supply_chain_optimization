from data_model import DataModel
from .variable_builder import VariableBuilder
from ortools.sat.python import cp_model
class ConstraintBuilder:
    def __init__(self,
                 data_model: DataModel,
                 model: cp_model,
                 variable: VariableBuilder) -> None:
        self.data_model = data_model
        self.model = model
        self.variable = variable
        self.one_order_one_freight = []
        self.other_cosntraint = []

    def one_order_max_one_frieght(self) -> None:
        for _, freight in self.data_model.freight.items():
            one_order_one_freight = [
                self.variable.freight_order_association.get((freight.get_id(), order.get_id()), None)
                for _, order in self.data_model.order.items()
            ]
            one_order_one_freight = [
                var for var in one_order_one_freight
                if var is not None
            ]
            self.one_order_one_freight.extend(one_order_one_freight)
            self.model.AddAtMostOne(one_order_one_freight)
    
    def get_number_of_constraint(self):
        return len(self.one_order_one_freight)\
            + len(self.other_cosntraint)
    