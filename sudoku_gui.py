# sudoku_gui.py

import tkinter
import sudoku_button

DEFAULT_FONT = ('Helvetica', 20)
ALL_SIDES = tkinter.N + tkinter.S + tkinter.E + tkinter.W

class SudokuApplication:
	def __init__(self):
		# main window
		self._root_window = tkinter.Tk()
		
		# text that goes in the sidebar
		self._sidebar_text = tkinter.StringVar(master=self._root_window)

		self._create_main_window()
		string_append(self._sidebar_text, 'Log:\n')
		string_append(self._sidebar_text, 'abcdefg\n')

	def _create_main_window(self):
		# title text (row 0, column 0)
		self._create_title()

		# sidebar (row 0-1, column 1)
		self._create_sidebar()

		# board (row 1, column 0)
		self._create_board_view()

		# main window row configuration
		self._root_window.rowconfigure(0, weight=0)
		self._root_window.rowconfigure(1, weight=1)

		# main window column configuration
		self._root_window.columnconfigure(0, weight=1)
		self._root_window.columnconfigure(1, weight=0)

	def _create_title(self):
		self._top_text_box = tkinter.Label(master=self._root_window, font=DEFAULT_FONT, 
			text='SUDOKUUUUUU')
		self._top_text_box.grid(row=0, column=0, padx=10, pady=10,
			sticky=tkinter.N+tkinter.S)	

	def _create_sidebar(self):
		self._sidebar = tkinter.Label(master=self._root_window, 
			font=('Times New Roman', 15), textvariable=self._sidebar_text,
			background='#FFFFFF', width=40, wraplength=400, 
							# wraplength 400 is really 40. idk why.
							# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/label.html
			# anchors the text to the top of the widget
			anchor=tkinter.N + tkinter.W) 
		self._sidebar.grid(row=0, column=1, padx=10, pady=15, rowspan=2, sticky=ALL_SIDES)

	def _create_board_view(self):
		# sudoku board view
		self._board_frame = tkinter.Frame(master=self._root_window, background='#000000')
		self._board_frame.grid(row=1, column=0, padx=10, pady=10, sticky=ALL_SIDES)

		# boxes
		for row in range(3):
			for column in range(3):
				self._create_box(row, column)

		# box grid configuration
		for row in range(3):
			self._board_frame.rowconfigure(row, weight=1)
		for column in range(3):
			self._board_frame.columnconfigure(column, weight=1)


	def _create_box(self, board_row, board_column):
		# coords of the first cell in the box
		first_row = board_row * 3
		first_column = board_column * 3
		# box divider thickness
		box_pad = 1
		box = tkinter.Frame(master=self._board_frame)
		box.grid(row=board_row, column=board_column, padx=box_pad, pady=box_pad, 
			sticky=ALL_SIDES)
		for row in range(3):
			for column in range(3):
				cell = sudoku_button.SudokuButton(master=box, 
					text='{}, {}'.format(first_row + row, first_column + column))
					#command=self.handle_button_press)
				cell.bind('<Button-1>', self._handle_left_click)
				cell.bind('<Button-3>', self._handle_right_click)
				# add row and column attributes to make the button into a useful object
				cell.row = row + first_row
				cell.column = column + first_column
				cell.grid(row=row, column=column, sticky=ALL_SIDES)
				if row <=7 and column % 3 == 0:
					cell.lock()
					print(cell.cget('state'))

		# configuration of this box
		for row in range(3):
			box.rowconfigure(row, weight=1)
		for column in range(3):
			box.columnconfigure(column, weight=1)

	def _handle_left_click(self, button_press_event):
		button = button_press_event.widget
		if not button.is_locked():
			row, column = button.row, button.column 
			# string_append(self._sidebar_text, "button ({}, {}) pressed!\n".format(row, column))
			button.increment()

	def _handle_right_click(self, button_press_event):
		button = button_press_event.widget
		if not button.is_locked():
			button.clear()

	def run(self):
		self._root_window.mainloop()

def string_append(string_var, text):
	'Takes a tkinter.StringVar and appends text to it.'
	string_var.set(string_var.get() + text)

if __name__ == '__main__':
	SudokuApplication().run()
