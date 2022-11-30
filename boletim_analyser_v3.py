import PySimpleGUI as gui

# - Layout:
gui.theme('DarkBlue4')
layout = [
[gui.Text('Nome do aluno: '), gui.Input(key="NOME",do_not_clear=True, size=(30,1))],
[gui.Text('Número do aluno: '), gui.Input(key="NUMERO", do_not_clear=True, size=(15, 1))],
[gui.Text('Nota do trabalho: '), gui.Input(key="NOTA_TRABALHO", do_not_clear=True, size=(15, 1))],
[gui.Text('Nota do teste: '), gui.Input(key="NOTA_TESTE", do_not_clear=True, size=(15, 1))],
[gui.Text('Nota do projeto: '), gui.Input(key="NOTA_PROJETO", do_not_clear=True, size=(15, 1))],
[gui.Text('Nota da prova: '), gui.Input(key="NOTA_PROVA", do_not_clear=True, size=(15, 1))],
[gui.Text('Nota do comportamento: '), gui.Input(key="NOTA_COMPORT", do_not_clear=True, size=(15, 1))],
[gui.Text('Selecione o bimestre:')],
[gui.Checkbox('1° bi'), gui.Checkbox('2° bi'), gui.Checkbox('3° bi'), gui.Checkbox('4° bi')],
[gui.Button('Cadastrar'), gui.Button('Analisar'), gui.Exit()]
]

screen = gui.Window('Boletim Analyser', layout, size=(800, 600))

while True:
	event, values = screen.read()
	if event in (gui.WIN_CLOSED, 'Exit'):
		break
	
	elif event == 'Analisar':
		nota_teste = float(values["NOTA_TESTE"])
		nota_trabalho = float(values["NOTA_TRABALHO"])
		nota_projeto = float(values["NOTA_PROJETO"])
		nota_prova = float(values["NOTA_PROVA"])
		nota_comport = float(values["NOTA_COMPORT"])
		media = (nota_teste + nota_trabalho + nota_projeto + nota_prova + nota_comport) / 2
		gui.popup(f"A média de {values['NOME'].title()} é de: {media:.1f}")
	