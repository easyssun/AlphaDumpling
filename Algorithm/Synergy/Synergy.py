from enum import Enum

# Synergy score EnumClass
class Synergy(Enum):
    MINT_CHOCOLATE = {"SESAME_OIL": 3, "KOCHUJANG": 10, "MAYONNAISE": 5, "SOJU": 20, "CHEESE": 15, "GALIC": 13, "ONION": 12, "JUICE": 25, "WATER": 8}
    SESAME_OIL = {"MINT_CHOCOLATE": 3, "KOCHUJANG": 25, "MAYONNAISE": 20, "SOJU": 5, "CHEESE": 12, "GALIC": 15, "ONION": 10, "JUICE": 3, "WATER": 8}
    KOCHUJANG = {"MINT_CHOCOLATE": 10, "SESAME_OIL": 25, "MAYONNAISE": 25, "SOJU": 5, "CHEESE": 12, "GALIC": 20, "ONION": 15, "JUICE": 3, "WATER": 10}
    MAYONNAISE = {"MINT_CHOCOLATE": 5, "SESAME_OIL": 20, "KOCHUJANG": 25, "SOJU": 3, "CHEESE": 20, "GALIC": 15, "ONION": 10, "JUICE": 5, "WATER": 8}
    SOJU = {"MINT_CHOCOLATE": 20, "SESAME_OIL": 5, "KOCHUJANG": 5, "MAYONNAISE": 3, "CHEESE": 5, "GALIC": 15, "ONION": 10, "JUICE": 3, "WATER": 5}
    CHEESE = {"MINT_CHOCOLATE": 15, "SESAME_OIL": 12, "KOCHUJANG": 12, "MAYONNAISE": 20, "SOJU": 5, "GALIC": 25, "ONION": 20, "JUICE": 5, "WATER": 8}
    GALIC = {"MINT_CHOCOLATE": 13, "SESAME_OIL": 15, "KOCHUJANG": 20, "MAYONNAISE": 15, "SOJU": 15, "CHEESE": 5, "ONION": 20, "JUICE": 5, "WATER": 8}
    ONION = {"MINT_CHOCOLATE": 12, "SESAME_OIL": 10, "KOCHUJANG": 15, "MAYONNAISE": 10, "SOJU": 10, "CHEESE": 20, "GALIC": 20, "JUICE": 5, "WATER": 10}
    JUICE = {"MINT_CHOCOLATE": 25, "SESAME_OIL": 3, "KOCHUJANG": 3, "MAYONNAISE": 5, "SOJU": 3, "CHEESE": 5, "GALIC": 5, "ONION": 5, "WATER": 3}
    WATER = {"MINT_CHOCOLATE": 8, "SESAME_OIL": 8, "KOCHUJANG": 10, "MAYONNAISE": 8, "SOJU": 5, "CHEESE": 8, "GALIC": 8, "ONION": 10, "JUICE": 3}
    
    def getSynergyList():
        return ['MINT_CHOCOLATE', 'SESAME_OIL', 'KOCHUJANG', 'MAYONNAISE', 'SOJU', 'CHEESE', 'GALIC', 'ONION', 'JUICE', 'WATER']

# Robot guessing synergy table
class Estimate_Synergy(Enum):
    MINT_CHOCOLATE = {"SESAME_OIL": 3, "KOCHUJANG": 10, "MAYONNAISE": 5, "SOJU": 20, "CHEESE": 15, "GALIC": 13, "ONION": 12, "JUICE": 25, "WATER": 8}
    SESAME_OIL = {"MINT_CHOCOLATE": 3, "KOCHUJANG": 25, "MAYONNAISE": 20, "SOJU": 5, "CHEESE": 12, "GALIC": 15, "ONION": 10, "JUICE": 3, "WATER": 8}
    KOCHUJANG = {"MINT_CHOCOLATE": 10, "SESAME_OIL": 25, "MAYONNAISE": 25, "SOJU": 5, "CHEESE": 12, "GALIC": 20, "ONION": 15, "JUICE": 3, "WATER": 10}
    MAYONNAISE = {"MINT_CHOCOLATE": 5, "SESAME_OIL": 20, "KOCHUJANG": 25, "SOJU": 3, "CHEESE": 20, "GALIC": 15, "ONION": 10, "JUICE": 5, "WATER": 8}
    SOJU = {"MINT_CHOCOLATE": 20, "SESAME_OIL": 5, "KOCHUJANG": 5, "MAYONNAISE": 3, "CHEESE": 5, "GALIC": 15, "ONION": 10, "JUICE": 3, "WATER": 5}
    CHEESE = {"MINT_CHOCOLATE": 15, "SESAME_OIL": 12, "KOCHUJANG": 12, "MAYONNAISE": 20, "SOJU": 5, "GALIC": 25, "ONION": 20, "JUICE": 5, "WATER": 8}
    GALIC = {"MINT_CHOCOLATE": 13, "SESAME_OIL": 15, "KOCHUJANG": 20, "MAYONNAISE": 15, "SOJU": 15, "CHEESE": 5, "ONION": 20, "JUICE": 5, "WATER": 8}
    ONION = {"MINT_CHOCOLATE": 12, "SESAME_OIL": 10, "KOCHUJANG": 15, "MAYONNAISE": 10, "SOJU": 10, "CHEESE": 20, "GALIC": 20, "JUICE": 5, "WATER": 10}
    JUICE = {"MINT_CHOCOLATE": 25, "SESAME_OIL": 3, "KOCHUJANG": 3, "MAYONNAISE": 5, "SOJU": 3, "CHEESE": 5, "GALIC": 5, "ONION": 5, "WATER": 3}
    WATER = {"MINT_CHOCOLATE": 8, "SESAME_OIL": 8, "KOCHUJANG": 10, "MAYONNAISE": 8, "SOJU": 5, "CHEESE": 8, "GALIC": 8, "ONION": 10, "JUICE": 3}
    
    def getSynergyList():
        return ['MINT_CHOCOLATE', 'SESAME_OIL', 'KOCHUJANG', 'MAYONNAISE', 'SOJU', 'CHEESE', 'GALIC', 'ONION', 'JUICE', 'WATER']

    # Update scores for Material 1 and Material 2
    def updateSynergy(ingredient1, ingredient2, score, add = False):
            if add == True:
                Estimate_Synergy[ingredient1].value[ingredient2] += score
                Estimate_Synergy[ingredient2].value[ingredient1] += score
            else:
                Estimate_Synergy[ingredient1].value[ingredient2] = score
                Estimate_Synergy[ingredient2].value[ingredient1] = score