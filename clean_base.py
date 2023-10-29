import csv

csv_file_path = r'C:\Users\Gabriel\Documents\iCloudDrive\iCloud~md~obsidian\Obsidian - Gabriel\01_Projeto\Donodozap\prestadoras_servicos_telecomunicacoes.csv'
output_file_path = r'C:\Users\Gabriel\Documents\iCloudDrive\iCloud~md~obsidian\Obsidian - Gabriel\01_Projeto\Donodozap\prestadoras_servicos_telecomunicacoes_cleaned.csv'

# Função para verificar se uma célula contém ',' '.' ou '/'
def contains_invalid_chars(cell):
    invalid_chars = ",./"
    return any(char in invalid_chars for char in cell)

# Abre o arquivo de entrada para leitura e o arquivo de saída para escrita
with open(csv_file_path, 'r', newline='') as input_file, open(output_file_path, 'w', newline='') as output_file:
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    for row in csv_reader:
        # Verifica se a linha contém caracteres ',', '.', ou '/'
        if not any(contains_invalid_chars(cell) for cell in row):
            # Se não contém, escreve a linha no arquivo de saída
            csv_writer.writerow(row)

print("Linhas com ',', '.', ou '/' removidas. O arquivo de saída foi salvo em:", output_file_path)
