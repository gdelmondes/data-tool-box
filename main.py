from file_utils.excel_util import excel_to_csv

excel_to_csv("tests/input_data/Base de Vendas Varejo.xlsx", "tests/output_data/Base de Vendas Varejo.xlsx", sheet="Vendas", delimiter=",")